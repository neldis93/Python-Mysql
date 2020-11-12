create database dbclient;

use dbclient;

create table Customer(id int, first_name varchar(30) not null, last_name varchar(30) not null, dni varchar(9) not null);

alter table Customer add unique (dni);

alter table Customer add primary key (id);

alter table Customer modify column id int auto_increment;

