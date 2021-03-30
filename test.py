import sqlite3
def select_all():
	with sqlite3.connect("sportshoedata.db") as db:
	  cursor = db.cursor()
	  cursor.execute("SELECT * FROM Sports")
	  Shoes = cursor.fetchall()
    print(Shoes)
  
select_all()