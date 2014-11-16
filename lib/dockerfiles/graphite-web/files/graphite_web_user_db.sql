\set username graphite

CREATE USER :username WITH PASSWORD 'password';
CREATE DATABASE graphite WITH OWNER :username;
