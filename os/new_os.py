import os
from datetime import datetime

# αλλαγη παθ
# os.chdir('D:\Προγραμματισμος\myproject\totorial\os')
#φτιαχνω ενα φακελο
# os.mkdir('test')
#φακελο και υποφαελο 
# os.makedirs('messinis/kostas')
#Μετανομασια  αρχειο και φακελων 
# os.rename( 'test',  'messinis')
# στατιστικα αρχειον
# info = os.stat('messinis')
# print(datetime.fromtimestamp(info.st_ctime))
# print(os.getcwd("messinis")) #ektiponi tin diadromh toy arxeioy
# del director poy einai adios
#os.rmdir('demo')
# exaganastiki  diagrafi fakelon kai ypofakelon se detro 
#os.removedirs('kostas\\spiti\\ergasia')
#diagrafi  arxiou
# os.remove('nikos.py')
#Εκτυπονη καταλογο
print(next(os.walk('.')))
