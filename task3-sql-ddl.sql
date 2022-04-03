create table Visits(
	customer_id int NOT NULL,
	city_id_visited int NOT NULL,
	date_visited date NOT NULL
);

create table Customer(
	customer_id int NOT NULL,
	customer_name VARCHAR (20) NOT NULL,
	gender char(1) NOT NULL,
	age int NOT NULL
);

create table City(
	city_id int NOT NULL,
	city_name VARCHAR (20) NOT NULL,
	expense int NOT NULL
);


insert into visits VALUES (1001,2003,'01-Jan-03")
insert into visits VALUES (1001,2004,'01-Jan-04')
insert into visits VALUES (1002,2001,'01-Jan-01')
insert into visits VALUES (1004,2003,'01-Jan-03')


insert into Customer VALUES (1001,'John','M',25)
insert into Customer VALUES (1002,'Mark','M',30)
insert into Customer VALUES (1003,'Martha','F',55)
insert into Customer VALUES (1004,'Selena','F',34)

insert into City VALUES (2001,'Chicago',500)
insert into City VALUES (2002,'Newyork',1000)
insert into City VALUES (2003,'SFO',2000)
insert into City VALUES (2004,'Florida',800)