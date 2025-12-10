import psycopg2,os,sys
f=open("fwfiw.txt",'r')
name=f.read()

database="fwfiw"
user="fwfiw"
password="fwfiw2024"
host="fwfiw-postgresql.postgres.database.azure.com"
port="5432"

conn=None

conn=psycopg2.connect(database=database,user=user,password=password,host=host,port=port)
cur=conn.cursor()
cur.execute('''Select * from Table1 Where name = '{}' ''',(name,))
result=cur.fetchall()

for i in result:
    print(i[0])
cur.close()
conn.close()
