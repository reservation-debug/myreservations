
use myreservations


create table Users(user_id int NOT NULL, name varchar(20),gender varchar(2) check(gender in ('M','F','m','f')),age int, mobile_no VARCHAR(20), state varchar(20), city varchar(20), pin varchar(10),primary key(user_id))

create table Passengers(p_id int NOT NULL,user_id int NOT NULL,ticket_id int NOT NULL,name varchar(20) NOT NULL,age int, book_date date,primary key(p_id))

create table Station(station_no int NOT NULL,station_name varchar(30) NOT NULL,hault int,arrival_time time)


create table Train(train_no int NOT NULL, train_name varchar(30),arrival_time time, dept_time time,availabilty int,Date date, primary key(train_no))

create table Train_stats(train_id int NOT NULL,ac_seats int, non_ac_seats int,base_fare int)

create table ticket(ticket_no int NOT NULL,user_id int NOT NULL,status varchar(2),Ac_nonAc varchar(2),fare int,train_no int NOT NULL)


create table Cancel(user_id int ,p_id int ,ticket_id int )

create table Books(ticket_id int,p_id int)

create table Stop_at(train_no int NOT NULL,station_no int NOT NULL)
create table Start_at(train_no int NOT NULL,station_no int NOT NULL)

create table Reaches(train_no int NOT NULL,station_no int NOT NULL,arr_time time)





