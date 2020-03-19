from sense_hat import SenseHat;
from datetime import datetime;
import os
import csv
import sqlite3
import uuid

# Serialisation
ID=str(uuid.uuid4()).replace('-','')
conn = sqlite3.connect('rbpi-rmit-iot.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS info (id TEXT PRIMARY KEY)")

c.execute("SELECT id FROM info")
fetch = c.fetchone();
FETCH_ID = fetch[0] if fetch != None else None;

if(FETCH_ID == None):
	c.execute("INSERT INTO info (id) VALUES (?)", [ID])
	print('okay done' + ID)
else:
	ID = FETCH_ID

conn.commit();
conn.close();

# Setup
sense = SenseHat()
temp = sense.get_temperature()

# Directory
dir_name = './data/'
filename = ID + dir_name + datetime.now().strftime("%d-%m-%Y-%H-%M-%S") + '.csv'

# Initialize
try:
	os.makedirs(dir_name)
except FileExistsError:
	pass

with open(filename, 'a+') as f:
	writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	if(f.tell() == 0):
		writer.writerow(['temp'])
	writer.writerow([temp])


