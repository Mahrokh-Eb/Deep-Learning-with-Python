# start kaggle on google colab

pip install kaggle

import os
os.environ['KAGGLE_CONFIG_DIR'] = "/content/drive/MyDrive/dogVsCat/drive"

#Change your present working directory
%cd /content/drive/MyDrive/dogVsCat/kaggle

pwd

#download dataset
!kaggle competitions download -c dogs-vs-cats

!ls

#unzipping the zip files and deleting the zip files
!unzip \*.zip  && rm *.zip
