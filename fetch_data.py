import os
import tarfile
from six.moves import urllib
from pathlib import Path

DOWNLOAD_ROOT = 'https://raw.githubusercontent.com/ageron/handson-ml/master/'
HOUSING_PATH = Path('./datasets/housing/')
HOUSING_URL = DOWNLOAD_ROOT + 'datasets/housing/housing.tgz'

os.makedirs(HOUSING_PATH)

if HOUSING_PATH.is_dir():
    tgz_path = HOUSING_PATH / 'housing.tgz'
    urllib.request.urlretrieve(HOUSING_URL, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=str(HOUSING_PATH))
    housing_tgz.close()
