create user de_user with encrypted password 'de_pass';

create database metabase;

grant all privileges on database metabase to de_user;