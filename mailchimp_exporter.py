#step one, get list of files you want to extract
from os import listdir
from os.path import isfile, join
mypath = r"master_mailchimp\\"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#step two, use the list of files, to make a list of paths to the files
paths = [mypath+i for i in onlyfiles]

#step three, make a directory to store my unzipped files
from os import mkdir
try:
    os.mkdir(r"master_mailchimp\unzipped_files\\")
except:
    print("Folder already made...")
    
#step four, unzip my files into the new directory
import zipfile
for i in paths:
    with zipfile.ZipFile(i, 'r') as zip_ref:
        zip_ref.extractall(mypath+r"unzipped_files\\")
        
#step five, create a list of the newly unzipped csv files
mypath_2 = r"master_mailchimp\unzipped_files\\"
onlyfiles_2 = [f for f in listdir(mypath_2) if isfile(join(mypath_2, f))]

#step six, use the list of unzipped csv files to make a list of paths to those files
paths_2 = [mypath_2+i for i in onlyfiles_2]

import pandas as pd

cleaned_list = []
subscribed_list = []
unsubscribed_list = []

for i in paths_2:
    if "cleaned" in i:
        df = pd.read_csv(i)
        cleaned_list.append(df)
    elif "\subscribed" in i:
        df = pd.read_csv(i)
        subscribed_list.append(df)
    else:
        df = pd.read_csv(i)
        unsubscribed_list.append(df)
        
clean = pd.concat(cleaned_list)
subscribed = pd.concat(subscribed_list)
unsubscribed = pd.concat(unsubscribed_list)

try:
    os.mkdir(r"master_mailchimp\master_files\\")
except:
    print("Folder already made...")

clean.to_csv(r"master_mailchimp\master_files\mailchimp_clean_backup.csv")
subscribed.to_csv(r"master_mailchimp\master_files\mailchimp_subscribed_backup.csv")
unsubscribed.to_csv(r"master_mailchimp\master_files\mailchimp_unsubscribed_backup.csv")
