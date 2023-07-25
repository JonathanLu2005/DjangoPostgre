from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import psycopg2
# Create your views here.

# new code
conn = psycopg2.connect(dbname="djangohosttest", user="djangohosttest_user", password="C4QWRdDYAoy35pxGrbuAUJ6BjHkHvdHl", host="dpg-civs3dunqql48o2fhai0-a", port="5432")
cur = conn.cursor()
conn.autocommit = True

cur.execute("""CREATE TABLE IF NOT EXISTS Property(
PropertyID SERIAL PRIMARY KEY NOT NULL,
CountyName VARCHAR(100) NOT NULL,
NoOfRooms INT NOT NULL,
NoOfKitchens INT NOT NULL,
NoOfBathrooms INT NOT NULL,
Rating FLOAT NOT NULL,
Price FLOAT NOT NULL);""")
# new code

def home(response):
    return render(response, "main/home.html", {})
