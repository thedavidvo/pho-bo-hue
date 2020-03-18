from sense_hat import SenseHat;
from datetime import datetime;
import csv

# Setup
sense = SenseHat()
temp = sense.get_temperature()

# Directory
dir_name = './data/'
filename = dir_name + datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

with open(filename, 'a+') as f:
	writer = csv.writer(filename, delimiter=',', quotechar='"', 
						quoting=csv.QUOTE_MINIMAL)
	writer.writerow(['test', temp])
