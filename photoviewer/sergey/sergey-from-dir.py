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
## This helper script will read a directory of pictures and produce
## some "actions" suitable to be included in your slideshow script. It
## will just "show" each picture; you will have to change the action
## function if you want it to do something else (like pan-zoom,
## etcetera).
##

import sys
import os

for x in sys.argv[1:]:
    foo = os.listdir(x)
    foo.sort()
    for y in foo:
        caption = ''
        if '_' in y:
            z = y.split('_')[1]
            caption = ' '.join(z.split('-'))
        print("actions.append( (show, (load('%s%s'),4,'%s')) )" % (x,y,caption))
