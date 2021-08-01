import psycopg2
import json

#connect to the db
con = psycopg2.connect(host="db",
                       database="database", 
                       user="username", 
                       password="2skV9Vc1", 
                       port=5432)

#cursor 
cur = con.cursor()

cur.execute("""CREATE TABLE employees
            (
            UserID int,
            name varchar(100)
            );"""
)
cur.execute("insert into employees (UserID, name) values (1, 'Teacher Paul')")
con.commit()

cur.execute("select UserID, name FROM employees")
rows = cur.fetchall()

data = {}
for r in rows:
    if r not in data:
        data[r[0]] = r[1]

# with open("data.json", 'w') as f:
#     for r in rows:
#         f.write(f"\{ {r[0]}: {r[1]} \}")
#         print(f"UserID {r[0]} name {r[1]}")

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
f.close()

cur.close()
#close the connection
con.close()