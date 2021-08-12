# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 09:52:27 2021

@author: m252047
"""
import os
import os.path, time
import datetime
from datetime import date
    
def is_file( path, filename):
    file = os.path.join( path, filename)
    return os.path.isfile( file)
    
def is_dir( path, filename):
    dirpath = os.path.join( path, filename)
    return os.path.isdir( dirpath)

def check_age( path, filename):
      file = os.path.join( path, filename)
      seconds = time.time() - os.path.getmtime(file)
      minutes = int(seconds) / 60
      hours = minutes / 60
      days = hours / 24
      return days
  
def clean_up( path, older_than):
    # This function scans your designated path for files whose date created is older than
    # some time 'older_than' todays date. It allows you to check over all the files then
    # makes a new folder in that same path called 'old files' and moves them all into there.
    global new_dir
    if not os.path.isdir( path + '\\'+ 'old_files'):
         os.makedirs( path+ '\\'+ 'old_files')
    else:
         new_dir = path + '\\' + 'old_files'
        
    global files, extensions, file, e2, e, only_files
    for roots, dirs, files in os.walk( path):   
        
        for file in files:
            if is_file( path, file) == True:
                only_files = files
                for i in only_files:
                    if check_age( path, i) > older_than: # greater than 2 days
                        os.rename( path + '\\' + i , new_dir + '\\' + i )
                        only_files.remove( i)
                
        for durs in dirs:
            if is_dir( path, durs) == True:
                only_dirs = dirs
                for i in only_dirs:
                    if check_age( path, i) > older_than:
                        os.rename( path + '\\' + i , new_dir + '\\' + i )
                        only_dirs.remove( i)

if __name__ == "__main__":
    path = r'\\mfad\researchmn\ULTRASOUND\FATEMI\EXCHANGE\Anas Adith test scripts\Doppler_Denoising2' #CHANGE PATH
    # path = r'\\mfad\researchmn\ULTRASOUND\FATEMI\MEMBERS\PUTHAWALA\Poster images'
    
    older_than = 1 #days
    clean_up( path, older_than) 