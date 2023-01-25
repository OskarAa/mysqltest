import sqlite3
#import os
import re

#file_exists = os.path.exists('mydb.db')

#if file_exists == True:
  #os.remove("mydb.db")

#conn = sqlite3.connect('mydb.db')
conn_1 = sqlite3.connect('mydb_1.db')
cursor = conn_1.cursor()

def code_2():
  #Kursora izvedošana
  
  #create the salesman table, tabulu var izveidot vienu reizi!
  #cursor.execute('''CREATE TABLE salesman(salesman_id INTEGER PRIMARY KEY UNIQUE, name char(15), city char(35), uzvards text char(35), commission decimal(7,2), valsts char default[LV], gada_apgrozijums decimal(7,2));''')


#def code_1():
  #Kursora izvedošana
  #cursor = conn.cursor()
  #create the salesman table, tabulu var izveidot vienu reizi!
  #cursor.execute( "CREATE TABLE salesman(salesman_id INTEGER PRIMARY KEY UNIQUE, name char(15), city char(35), uzvards text char(35), commission decimal(7,2), valsts char default[LV], gada_apgrozijums decimal(8,2));")


  #Lietotaja datu ievade
  s_id = input('Salesman ID:')
  s_name = input('Name:')

  if not re.match("^[A-z]*$", s_name):
    print("Error! Only letters A-z allowed!")
    exit()
  elif len(s_name) > 15:
    print("Error! Only 15 characters allowed!")
    exit()
  s_uzvards = input("Uzvards:")
  s_city = input('City:')
  s_commision = input('Commission:')
  s_GA = input("Gada apgrozijums:")
  s_valsts = input("Ievadi Valsti:")
    
  cursor.execute("""INSERT INTO salesman(salesman_id, name, city, commission, uzvards, gada_apgrozijums, valsts) VALUES (?,?,?,?,?,?,?)""", (s_id, s_name, s_city, s_commision, s_uzvards, s_GA, s_valsts))
  
  conn_1.commit()
  print('Data entered successfully.')

  query = cursor.execute("SELECT * FROM salesman")
  data = cursor.fetchall()
  for d in data:
    print (d)

    cursor.execute(''' SELECT salesman_id, Name, commission FROM salesman WHERE commission = (SELECT MAX(commission) FROM salesman);  ''')

  cursor.execute('''SELECT salesman_id, name , commission FROM salesman ORDER BY commission DESC;''')   

  cursor.execute('''UPDATE salesman SET commission=commission+20 WHERE valsts = "LV";''')

  

"""
    if (conn):
        conn.close()
        print("\nThe SQLite connection is closed.")
"""

  #cursor.execute('''SELECT salesman_id, name , commission FROM salesman ORDER BY commission DESC;''')
   


def round_year():
#Noapaļo gada ienākumus līdz veselam skaitlim
  query = "SELECT ROUND(AVG(gada_apgrozijums),0) FROM salesman;"  
  cursor.execute(query)
  year_avg=cursor.fetchall()
  print("Noapaļots gada apgrozijums: ",year_avg)

def print_all():
  cursor.execute("SELECT * FROM salesman")
  data = cursor.fetchall()
  for d in data:
    print (d)

def sum_year():
  #Izvadi gada apgrozijumu summu valstīm atsevišķi (LV,EST, LT)  un visām kopā
  query = "SELECT SUM(gada_apgrozijums) FROM salesman WHERE valsts='LV';"
  cursor.execute(query)
  lv_year = cursor.fetchall()
  print("LV gada apgrozijums: ",lv_year)
  
  query = ("SELECT SUM(gada_apgrozijums) FROM salesman WHERE valsts='EST';")
  cursor.execute(query)
  EST_year = cursor.fetchall()
  print("EST gada apgrozijums: ",EST_year)
  
  query = ("SELECT SUM(gada_apgrozijums) FROM salesman WHERE valsts='LT';")
  cursor.execute(query)
  LT_year = cursor.fetchall()
  print("LT gada apgrozijums: ",LT_year)
  

  query = ("SELECT SUM(gada_apgrozijums) FROM salesman;")
  # WHERE valsts= 'LT' WHERE valsts= 'EST' WHERE valsts= 'LV'
  kop_year = cursor.fetchall()
  print("Kopa gada apgrozijums: ",kop_year)

  print("Kopa gada apgrozijums: ",LT_year + EST_year + lv_year)


def ag_id():
  a = input("Ievadi agenta ID:")
  b = input("Ievadi Agenta Vardu:")

  
#code_1()
#code_2()

#code_2()
print_all()
#round_year()
#sum_year()

ag_id()
conn_1.close()