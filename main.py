import xml.etree.ElementTree as ET
import shutil
import sys,getopt,re
#TODO: Read files from command line arguments
#https://www.tutorialspoint.com/python/python_command_line_arguments.htm

old_file = 'files/android.txt'
new_file = 'files/android.es.txt'
out_file = 'files/ios.txt'

#Copying out file before change it
temp_file = 'files/ios.es.txt'
temp_file = shutil.copyfile(out_file,temp_file)

old_xml = ET.parse(old_file)
old = old_xml.getroot()
new_xml = ET.parse(new_file)
new = new_xml.getroot()

temp = open (temp_file,mode='r')
tempo = temp.read()
for newstr in new.iter('string'):
    for oldstr in old.iter('string'):
        new_name = newstr.get('name')
        old_name = oldstr.get('name')
        if new_name == old_name:
            tempo = tempo.replace(oldstr.text,newstr.text)

temp = open(temp_file,mode='w')
temp.write(tempo)

