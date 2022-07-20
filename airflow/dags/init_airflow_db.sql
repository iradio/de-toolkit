create user de_user with encrypted password 'de_pass';

create database airflow;

grant all privileges on database airflow to de_user;