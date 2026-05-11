create table if not exists listings (
  listing_id uuid primary key,
  building_id uuid,
  address text not null,
  borough text not null,
  asking_price numeric(12, 2),
  status text not null,
  listed_at timestamptz,
  updated_at timestamptz
);

create table if not exists buildings (
  building_id uuid primary key,
  normalized_address text not null,
  borough text not null,
  building_class text,
  unit_count integer,
  updated_at timestamptz
);

create table if not exists agents (
  agent_id uuid primary key,
  display_name text not null,
  brokerage text,
  updated_at timestamptz
);
