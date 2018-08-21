from bs4 import BeautifulSoup
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
import re
import sys
import wget
import pandas as pd
import os
import zipfile
from subprocess import call
from datetime import datetime

### Define paths

# Assign path of data download
temp_path = r'C:\Windows\Temp'
download_path = r'C:\Windows\Temp'
month = ""
year = datetime.now().year 

def NPPES_pull():

    months = ["January", "Feb", "March", "April", "May", "June",
              "July", "August", "September", "Oct", "November", "December"]
    
	# Get just the html page
    html_page = urlopen("http://download.cms.gov/nppes/NPI_Files.html")
    link_prefix = "http://download.cms.gov/nppes/"

    soup = BeautifulSoup(html_page, "html.parser")
	# get all links
    zipfilelinks = []
    for link in soup.findAll('a'):
        # print(link)
        # get just zips
        if link.get('href', "").endswith(".zip"):
            zipfilelinks.append(link.get('href', ""))
	
	# determine full v/s weekly
    weeklylinks = []
    full_link = ""
    for link in zipfilelinks:

        for m in months:
            if link.__contains__(m):
                full_link = link_prefix + link
                month = m
        if link.__contains__("Report"):
            deactivation_link = link

        else:
            weeklylinks.append(link)
    print(" ")
    print("DOWNLOADING NPPES FILE:")
    print(full_link)

    wget.download(full_link, temp_path)

    zipfile_name = os.path.basename(full_link)
    zipped_path = os.path.join(temp_path+"\\"+zipfile_name)
    yearstr=str(year)

    #Unzip Files
    with zipfile.ZipFile(zipped_path, "r") as zip_ref:
        zip_ref.extractall(os.path.join(download_path+"\\"+"NPPES_"+month+"_"+yearstr))

    unzipped_files = []
    files_to_keep = []
    datafile = []
    unzipped_path = os.path.join(download_path+"\\"+"NPPES_"+month+"_"+yearstr)
    unzipped_files = os.listdir(unzipped_path)
    for file in unzipped_files:
        if file.__contains__("npidata"):
            files_to_keep.append(file)
        else:
            print("Remove: "+file)
            os.remove(os.path.join(unzipped_path+"\\"+file))

    for file in files_to_keep:
        if file.__contains__("Header"):
            print("Remove: "+file)
            os.remove(os.path.join(unzipped_path+"\\"+file))
        else:
            datafile.append(file)
    print(" ")
    print("NPPES FILES UNZIPPED TO:")	
    print(unzipped_path)
    print(datafile)

    # Remove temp zipped file
    os.remove(zipped_path)
    
# Download the NPPES Full File to Downloads Folder, Unzip, and then cleanup files not needed
NPPES_pull()
