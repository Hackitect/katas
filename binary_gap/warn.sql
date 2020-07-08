create table logs (
    user_id integer not null,
    login_time timestamp not null
);

SELECT DISTINCT(logs.user_id) from logs WHERE login_time >  "2020-02-20 11:22:00";