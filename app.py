import sqlite3 as sq
connect = sq.connect("db.sqlite")
cursor = connect.cursor()
f = cursor.execute('''insert into users (f_name, l_name, age) values ('Иван', 'Сидоров', 22)''')
connect.commit()
#for i in f:
print(f)
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