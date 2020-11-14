create database dbclient;

use dbclient;

create table Customer(
             id int not null auto_increment primary key, 
             first_name varchar(30) not null, 
             last_name varchar(30) not null, 
             dni varchar(9) not null
             );

alter table Customer add unique (dni);

