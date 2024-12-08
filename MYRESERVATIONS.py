import mysql.connector
mycon=mysql.connector.connect(host="local host",user="root",password="12345")
cursor=mycon.cursor()
mycon.autocommit=True
s1="create database if not exists myreservations"
cursor.execute(s1)
s1="use myreservations"
cursor.execute(s1)
s1="create table if not exists Passengers(p_id int NOT NULL,user_id int NOT NULL,ticket_id int NOT NULL,name varchar(20) NOT NULL,age int, book_date date,primary key(p_id))"
cursor.execute(s1)
s1="create table if not exists  Station(station_no int NOT NULL,station_name varchar(30) NOT NULL,hault int(),arrival_time (time))"
cursor.execute(s1)

print("____________________________________________________________________________")
while true:
    print("WELCOME TO THE RALIWAYS RESERVATIONS")
    print("________________________________________________")
    print("        1.SIGN IN")
    print("        2.SIGN UP")
    print("        3.EXIT")
    print("________________________________________________")
    print("________________________________________________________________________")

YOO=int(input("       ENTER  YOUR  CHOICE::"))
if YOO==1:
     signin()

elif YOO==2:
     signup()
elif YOO==3:
     print("_________________________")
     print("THANK YOUUUU")
     print("_________________________")
     break
else:
        print("ERROR 404 NOT FOUND")

def signin():
    a=input("USER NAME::")
    b=input("PASSWORD::")
    s="select user_name from user_accounts where  password='{}'".format(b)
    cursor.execute(s)
    data=cursor.fetchone()
    if data[0]==a:
        print("________________________")
        print("LOGINN  SUCESSFULLY")
        print("________________________")
        main()
    else:
        print("ACCOUNT DOES  NOT EXIST")
        
def signup():
    f=input("ETER YOUR FIRST NAME: ")
    L=input("ENTER YOUR LAST NAME : ")
    u=input("USER NAME : ")
    p=input("PASSWORD: ")
    r=input("RE-ENTER YOUR PASSWORD: ")
    ph=input("PHONE NUMBER: ")
    print("M=MALE")
    print("F=FEMALE")
    print("N=NOT TO MENTION")
    gen(input("ENTER YOU GENDER: "))
    print("ENTER OYUR DATE OF  BIRTH: ")
    d=input("DD:")
    d=input("MM:")
    d=input("YYYY:")
    dob=d+'/'+o+'/'+p
    age=input("your age: ")
    v=('m''MALE','f''FEMALE','n''NOT TO MENTION')
    if b==c:
        c1="insert your user_accounts values('{}','{}','{}','{}','{}','{}','{}','{}')".format(f,L,u,p,ph,v[gen],dob,age)
        cursor.execute(c1)
        print("______________________________________")
        print("_____________SIGN UP SUCESSFULLY___________")
        print("______________________________________")
        main()
    else:
        print("BOTH PASSWORD ARE NOT MATCHING")

def main():
    while true:
        print("________________________________________")
        print("                1.TICKET BOOKING")
        print("                2.TICKET CHECKING")
        print("                3.TICKET CANCELLING")
        print("                4.ACCOUNT DETAILS")
        print("                5.LOG OUT")
        print("________________________________________")
        YOO=int(input("        ENTER YOUR CHOICE:"))
        if YOO==1:
            ticket_booking()
        if YOO==2:
            ticket_checking()
        if YOO==3:
            ticket_cancelling()
        if YOO==4:
            display()
        if YOO==5:
            print("THANK YOUUU")
        break
    else:
        print("ERROR 404 NOT FOUND")

def ticket_booking():
    name=input("enter your name: ")
    pnh=int(input("enter your phone number: "))
    age=int(input("enter your age"))
    print('M=MALE')
    print('F=FEMALE')
    print('N= NOT TOO MENTION')
    gender=gender.upper()
    fr=("ENTER YOUR STARTING POINT; ")
    to=("ENTER YOUR ENDING POINT; ")
    date1=input("enter date (dd): ")
    date1=input("enter date (mm): ")
    date1=input("enter date (yyyy): ")
    date=date1+'/'+date2+'/'+date3
    print('M=MALE')
    print('F=FEMALE')
    print('N= NOT TOO MENTION')
    v=a[gender]
    s1="insert your railways values('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,pnh,age,v,fr,to,date)
    cursor.execute(s1)
    print("______________________________________")
    print("_____________TICKET BOOKED SUCESSFULLY___________")
    print("______________________________________")

def ticket_checking():
    pnh=int(input("NETER THE PHONE NO.: "))
    try:
        s1=("select * from railways where  phno='{}'".format(pnh))
        cursor.execute(s1)
        data=list(data)
        a=['NAME','PHONENUMBER','AGE','GENDER','STARTING POINT','DESTINSTION','DATE']
        print(a[0],':::',data[0])
        print(a[1],':::',data[1])
        print(a[2],':::',data[2])
        print(a[3],':::',data[3])
        print(a[4],':::',data[4])
        print(a[5],':::',data[5])
        print(a[6],':::',data[6])
    except:
        print("TICKET DOES NOT EXIST")

def ticket_cancelling():
    pnh=int(input("NETER THE PHONE NO.: "))
    s=("select * from railways where  phno='{}'".format(pnh))
    cursor.execute(s)
    data=cursor.fetchone()
    if data[0]==pnh:
        s1="delete from railway where pnh=pnh"
        cursor.rexecute(s1)
        print("______________________________________")
        print("_____________TICKET CANCELLED SUCESSFULLY___________")
        print("______________________________________")
        main()
    else:
        print("TICKET DOES NOT EXIST")

def display():
     u=input("USER NAME : ")
     p=input("PASSWORD: ")
try:
        s1="select user_name from user_accounts where  password='{}'".format(b)
        c1="select fname,user_name from user_accounts where  password='{}'".format(b)
        cursor.execute(s1)
        data1=cursor.fetchall()[0]
        data1=list(data)
        data1=data1[0]+''+data1[1]
        cursor.execute(s1)
        data1=cursor.fetchall()[0]
        data1=list(data)
        if data[0]==a:
             x=[' FIRST NAME','LAST NAME','PHONENUMBER','GENDER','DATE OF BIRTH','AGE']
             s1=("select fname,name,pnh,gender,dob,age from user_accounts where password='{}'".format(b))
             cursor.execute(s1)
             data1=cursor.fetchall()[0]
             data1=list(data)
             print(x[0],':::',data[0])
             print(x[1],':::',data[1])
             print(x[2],':::',data[2])
             print(a[3],':::',data[3])
             print(a[4],':::',data[4])
             print(a[5],':::',data[5])
             print(a[6],':::',data[6])
        else:
            return False
        except:
            print("ACCOUNT DOES NOT EXIST")
            
       
             
             
            
        
    
        
        
        
        
        
