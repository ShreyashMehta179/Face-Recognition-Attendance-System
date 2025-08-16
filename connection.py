
import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="Shreyash@123",database="mydata")
if con.is_connected():
    print("successfully connected")
else:
    print("error")