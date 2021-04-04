import sqlite3 as sq
age = input("Введите возраст: ")
connect = sq.connect("db.sqlite")
cursor = connect.cursor()
f = cursor.execute('''SELECT f_name FROM users where age = (?)''', (age,)).fetchall()
#t(f)
#f = cursor.execute('''INSERT INTO users (f_name, l_name, age) values ('Иван', 'Сидоров', 22)''')
connect.commit()
#for i in f:
if f != []:
    for i in f:
        print(i[0])
else:
    print("Таких нет")
#connect.close()





#import os.path
#print(os.path.exists("file.txt"))





#f = open("file.txt","r")
#for line in f.readlines():
#    print("sfsf" + line)
#with open("file.txt", "r") as f:
#    for i in f:
#        print(i)
#open("file.txt", "w+")








#print(f.writelines(["sfksdhg\n","fasdjfgaskdhfaklsdjhfla"]))
#print(f.tell())
#print(f.read(5))
#f.seek(0)
#print(f.read(5))
#print(f.tell())
#f.close()
#print(f.readlines())
#print(f.readline())
#print(f.read(5))
#print(f.read(6))