create table if not exists fact_trips(
trip                       INTEGER,
date                       VARCHAR,
location                   VARCHAR,
tyres                      VARCHAR,
temperature_start_c        REAL,
temperature_end_c          REAL,
distance_km                INTEGER,
duration_minutes           INTEGER,
average_speed_kmh          INTEGER,
average_consumption_kwhkm  REAL,
charge_level_start         REAL,
charge_level_end           REAL,
ac_c                       VARCHAR,
heated_front_seats_level   INTEGER,
mode                       VARCHAR
 )