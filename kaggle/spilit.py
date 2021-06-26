from __future__ import print_function
import pandas as pd
import shutil
import os
import sys

labels = pd.read_csv(r'/content/drive/MyDrive/dogVsCat/kaggle/sampleSubmission.csv') # give the address of your csv file

train_dir =r'/content/drive/MyDrive/dogVsCat/kaggle/train' #the address od train set folder
DR = r"/content/drive/MyDrive/dogVsCat/kaggle/DR" #the DR folder is maded by me outside of the train folder
if not os.path.exists(DR):
    os.mkdir(DR)

for filename, class_name in labels.values:
    # Create subdirectory with `class_name`
    if not os.path.exists(DR + str(class_name)):
        os.mkdir(DR + str(class_name))
    src_path = train_dir + '/'+'cat.'+ str(filename) + '.jpg' #be carefull with the image name. check it in train folder
    dst_path = str(DR) + str(class_name) + '/' + str(filename) + str('.jpg')
    try:
        shutil.copy(src_path, dst_path)
        print("sucessful")
    except IOError as e:
        print('Unable to copy file {} to {}'
              .format(src_path, dst_path))
    except:
        print('When try copy file {} to {}, unexpected error: {}'
              .format(src_path, dst_path, sys.exc_info()))
