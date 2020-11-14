create database dbclient;

use dbclient;

create table Customer(
             id int not null auto_increment primary key, 
             first_name varchar(30) not null, 
             last_name varchar(30) not null, 
             dni varchar(9) not null
             );

alter table Customer add unique (dni);

<<<<<<< HEAD

alter table Customer add primary key (id);

alter table Customer drop column primary key;
describe Customer;

alter table Customer modify column id int auto_increment;
=======
>>>>>>> cf35db830312eb99598af623ce7f31f30344566e

insert into Customer (first_name,last_name,dni)
values('Neldis','Barrios', 'Y34FRDS43');

alter table Customer drop column id;

delete from Customer where concat(id,first_name, last_name,dni) is null; 

delete from Customer where dni= 'Y7401678W';

update Customer set last_name=('Barrios') where last_name=('Heredia');
