## SERGEY: slideshow software based on pygame
## Copyright (C) 2007 Mike Warren
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.
                                               

##
## SERGEY
## http://www.mike-warren.com/sergey
##
## This helper script resizes all images in the current directory (or
## files listed on the command-line) so that the height is not greater
## than TARGET_HEIGHT (768 by default). This is suitable for panoramas
## and still shots, but you probably don't want to resize images used
## for zooming into or out of.
##
## WARNING: this WILL CHANGE THE PICTURES in the current directory.
##


from PIL import Image
import os
import sys

TARGET_HEIGHT = 768

if len(sys.argv) == 1:
    files = os.listdir('.')
else:
    files = sys.argv[1:]

for f in files:
    try:
        img = Image.open(f)
    except:
        print("error on",f)
        continue

    (w,h) = img.size
    print(f,w,h)

    if h > TARGET_HEIGHT:
        print("   making backup \"%s\"" % f+'~')
        img.save(f + '~')
        ratio = float(h)/float(TARGET_HEIGHT)
        newwidth = int(w / ratio)
        print("   scaling to",newwidth,TARGET_HEIGHT)
        img = img.resize( (newwidth, TARGET_HEIGHT), Image.ANTIALIAS )
        print("   saving...")
        img.save(f)
    
