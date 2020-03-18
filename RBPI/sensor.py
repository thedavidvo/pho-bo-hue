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

try:
	c.execute("INSERT INTO info VALUES (" + ID + ")")
except sqlite3.IntegrityError:
	# ID already exists
	print("Already exists ID")
	c.execute("SELECT id FROM info")
	print(c.fetchone())

# Setup
sense = SenseHat()
temp = sense.get_temperature()

# Directory
dir_name = './data/'
filename = dir_name + datetime.now().strftime("%d-%m-%Y-%H-%M-%S") + '.csv'

# Initialize
try:
	os.makedirs(dir_name)
except FileExistsError:
	pass

with open(filename, 'a+') as f:
	writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	if(f.tell() == 0):
		f.write(['temp'])
	writer.writerow([temp])


