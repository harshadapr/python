import os
import shutil

source_directory = 'unorganized_files/'
destination_directory = 'organized_files/'

for filename in os.listdir(source_directory):
    source = os.path.join(source_directory, filename)
    destination = os.path.join(destination_directory, filename)
    shutil.move(source, destination)
