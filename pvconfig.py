import os
import pathlib

ROOT_DIR = os.path.join(pathlib.Path.home(),"Pictures")

PHOTO_DIR = os.path.join(ROOT_DIR, "testPics")

# The location of the photo tree.
DATA_DIR = "/home/pi/Pictures"
# The location of the preprocessed photos.
PROCESSED_ROOT_DIR = os.path.join(DATA_DIR, "processed_photos")

FILE_FORMATS = [".jpg", ".jpeg"]