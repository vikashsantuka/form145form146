-- Spam guard for the public lead form (audit fix, 27 Nov 2026).
-- 1) Tighten grants: the website (anon) may only INSERT.
revoke truncate, trigger, references on public.nrif_leads from anon;
revoke truncate, trigger, references on public.nrif_leads from authenticated;
revoke all on public.nrif_staff from anon;
-- rls_auto_enable() is an internal helper; it must not be callable through the public API.
do $$ begin
  if exists (select 1 from pg_proc where proname = 'rls_auto_enable' and pronamespace = 'public'::regnamespace) then
    execute 'revoke execute on function public.rls_auto_enable() from public, anon, authenticated';
  end if;
end $$;

-- 2) Rate limits, enforced in the database so bots can't skip them by calling the API directly.
--    Same phone or email: max 3 enquiries per 10 minutes. Whole site: max 30 enquiries per 5 minutes.
create or replace function public.nrif_leads_rate_limit() returns trigger
language plpgsql security definer set search_path = '' as $$
declare n int;
begin
  -- staff adding leads from the CRM are not limited
  if public.nrif_is_staff() then return new; end if;
  if new.message ~* '(https?://|www\.)\S+.*(https?://|www\.)' then
    raise exception 'Message looks like spam' using errcode = 'P0001';
  end if;
  select count(*) into n from public.nrif_leads
   where created_at > now() - interval '10 minutes'
     and ((new.phone is not null and phone = new.phone) or (new.email is not null and lower(email) = lower(new.email)));
  if n >= 3 then raise exception 'Too many requests, please WhatsApp us' using errcode = 'P0001'; end if;
  select count(*) into n from public.nrif_leads where created_at > now() - interval '5 minutes';
  if n >= 30 then raise exception 'Too many requests, please WhatsApp us' using errcode = 'P0001'; end if;
  return new;
end $$;
revoke all on function public.nrif_leads_rate_limit() from public, anon, authenticated;
drop trigger if exists nrif_leads_rate_limit on public.nrif_leads;
create trigger nrif_leads_rate_limit before insert on public.nrif_leads for each row execute function public.nrif_leads_rate_limit();
