-- NRI Foundation lead pipeline (CRM) for Form145Form146.com
-- Website visitors (anon key) can only INSERT a new lead. Only team members listed in nrif_staff can read or edit.

create table if not exists public.nrif_staff (
  email text primary key,
  name text,
  role text not null default 'agent' check (role in ('admin','agent','viewer')),
  created_at timestamptz not null default now()
);
alter table public.nrif_staff enable row level security;

create or replace function public.nrif_is_staff()
returns boolean language sql stable security definer set search_path = '' as $$
  select exists (select 1 from public.nrif_staff s where lower(s.email) = lower(coalesce(auth.jwt() ->> 'email', '')));
$$;
revoke all on function public.nrif_is_staff() from public;
grant execute on function public.nrif_is_staff() to authenticated;

create table if not exists public.nrif_leads (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  name text not null check (char_length(name) between 1 and 120),
  phone text check (char_length(phone) <= 40),
  email text check (char_length(email) <= 200),
  country text check (char_length(country) <= 60),
  purpose text check (char_length(purpose) <= 60),
  amount_band text check (char_length(amount_band) <= 40),
  bank text check (char_length(bank) <= 60),
  message text check (char_length(message) <= 2000),
  lead_type text not null default 'nri' check (lead_type in ('nri','business','bank_partner','other')),
  channel text not null default 'direct' check (channel in ('direct','bank','referral','social','manual')),
  source_page text check (char_length(source_page) <= 300),
  landing_page text check (char_length(landing_page) <= 300),
  referrer text check (char_length(referrer) <= 300),
  utm_source text check (char_length(utm_source) <= 100),
  utm_medium text check (char_length(utm_medium) <= 100),
  utm_campaign text check (char_length(utm_campaign) <= 100),
  stage text not null default 'new' check (stage in ('new','contacted','docs_pending','docs_received','certificate_issued','remittance_done','won','lost')),
  owner text check (char_length(owner) <= 80),
  next_follow_up date,
  fee_quoted numeric(12,2),
  remittance_amount_inr numeric(16,2),
  notes text check (char_length(notes) <= 20000)
);
create index if not exists nrif_leads_created_idx on public.nrif_leads (created_at desc);
create index if not exists nrif_leads_stage_idx on public.nrif_leads (stage);
alter table public.nrif_leads enable row level security;

create or replace function public.nrif_touch() returns trigger language plpgsql set search_path = '' as $$
begin new.updated_at = now(); return new; end; $$;
drop trigger if exists nrif_leads_touch on public.nrif_leads;
create trigger nrif_leads_touch before update on public.nrif_leads for each row execute function public.nrif_touch();

-- Website form: insert only, and only as a fresh lead (no CRM fields set by the public)
drop policy if exists nrif_leads_public_insert on public.nrif_leads;
create policy nrif_leads_public_insert on public.nrif_leads for insert to anon, authenticated
  with check (stage = 'new' and owner is null and notes is null and fee_quoted is null and remittance_amount_inr is null and next_follow_up is null);

drop policy if exists nrif_leads_staff_all on public.nrif_leads;
create policy nrif_leads_staff_all on public.nrif_leads for all to authenticated
  using (public.nrif_is_staff()) with check (public.nrif_is_staff());

drop policy if exists nrif_staff_read on public.nrif_staff;
create policy nrif_staff_read on public.nrif_staff for select to authenticated using (public.nrif_is_staff());

grant insert on public.nrif_leads to anon;
grant select, insert, update, delete on public.nrif_leads to authenticated;
grant select on public.nrif_staff to authenticated;

-- First admin (edit / add more team members later)
insert into public.nrif_staff (email, name, role) values ('vikashsantuka@gmail.com', 'Vikash', 'admin') on conflict do nothing;
