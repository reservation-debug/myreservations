insert into Users values (1,'mohit','m',32,98453214111, 'jodhpur','jaipur', '560037'),
insert into Users values (2,'amit','M',36,98478214222,'Goa',raipur','403001'),
insert into Users values (3,'soniya','f',23,98987645777,'West Bengal', 'Kolkata', '700001'),
insert into Users values (4,'jhanvi','f', 27, 70194216666, 'rajasthan', 'Bangalore', '560001'),
insert into Users values (5,'prachi','f',30,97989991456,'Karnataka','rajasthan', '570039');

insert into Train values (10000,' JU JP exp','11:30:00','04:00:00',2,'20200410')
insert into Train values (10001,'MARUDHAR exp','21:30:00','10:00:00',3,'20200421'),
(10002,'SHALIMAAR exp','21:30:00','10:00:00',2,'20200415'),
(10003,'JODHPUR special','13:30:00','04:00:00',1,'20200413'),
(10004,'RANTHAMBORE exp','21:30:00','10:00:00',3,'20200413')

insert into Station values (1,'JODHPURJN',12,'11:30:00')
insert into Station values (2,'JAIPURJN',10,'21:30:00'),
(3,'KOTAJN',10,'21:30:00'),
(4,'DELHIJN',111,'13:30:00'),
(5,'AHEMDABADJN',30,'21:30:00')

insert into Start_at VALUES(10000,1),(10001,2),(10002,3),(10003,2),(10004,5)
insert into Stop_at VALUES(10000,2),(10001,5),(10002,2),(10003,4),(10004,1)

insert into Train_stats values (10000,5,5,2500)
insert into Train_stats values (10001,5,5,1500),(10002,5,5,1000),(10003,5,5,500),(10004,5,5,3500)

insert into Reaches VALUES(10000,1,'4:10:00'),(10001,2,'10:01:00'),(10002,3,'10:30:50'),(10003,4,'4:05:00'),(10004,5,'4:00:00')
