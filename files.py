import os
import shutil

source_directory = 'unorganized_files/'
destination_directory = 'organized_files/'

for filename in os.listdir(source_directory):
    source = os.path.join(source_directory, filename)
    destination = os.path.join(destination_directory, filename)
    shutil.move(source, destination)


import csv

data = [
    ['Name', 'Age'],
    ['Alice', 25],
    ['Bob', 30]
]

# Write data to a CSV file
with open('data.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
