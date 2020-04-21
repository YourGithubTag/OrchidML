import os
import wget
import zipfile

################ GOOGLE COLAB ################

running_on_google_colab = False
files_downloaded = True

if running_on_google_colab:
   file_path = '/content/flower_data.zip'
   extract_to = '/content'
else:
   file_path = '../flower_data.zip'
   extract_to = '../'

################ DOWNLOAD DATA ################

if not files_downloaded:
   wget.download('https://s3.amazonaws.com/content.udacity-data.com/courses/nd188/flower_data.zip', '../')
   wget.download('https://raw.githubusercontent.com/udacity/pytorch_challenge/master/cat_to_name.json', '../')
   with zipfile.ZipFile(file_path, 'r') as zip_ref:
      zip_ref.extractall(extract_to)
   os.remove(file_path)

