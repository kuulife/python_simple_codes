import zipfile #to work with zipping,unzipping
import shutil
import zlib
import os

#create file txt
with open('filename.txt', 'w+') as t:
	t.write('hello world!')

with open('filename2.txt', 'w+') as t:
	t.write('hello world!')

#1--------------------------------------

# #create zip file
comp_file = zipfile.ZipFile('comp_file.zip','w')

# #add filename.txt contents to the comp_file.zip and zip it
comp_file.write('filename.txt',compress_type = zipfile.ZIP_DEFLATED)
comp_file.write('filename2.txt',compress_type = zipfile.ZIP_DEFLATED)

# #close compressed file
comp_file.close()

# #make zip object that you want to extract
zip_obj = zipfile.ZipFile('comp_file.zip','r')

# #extract zip file to new folder named extracted_content
zip_obj.extractall('extracted_content')

#2----------------------------------------------------
#Second way of zipping files faster

print(os.getcwd()) #this line of code helps you to find in which folder youre located currently

#which folder you gonna zip
dir_to_zip = '/Users/macbook/Progi/python_simple_codes/zip_unzip_file/extracted_content'

#name of zipped folder that you expected
output_filename = 'newzip' #you can call your file whatever you want

#archivate your folder
shutil.make_archive(output_filename,'zip',dir_to_zip)

#extract it again with faster way too
shutil.unpack_archive('newzip.zip','final_unzip',zip)
'''
first parameter in unpack_archive is: directory to unzip
second parameter is unzip to directory name 
third is what type of file 
'''