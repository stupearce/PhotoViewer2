

##
## this is an example SERGEY slideshow, demonstrating all the
## abilities. You will need to replace the image and music paths with
## some which actually exist on your system. It is recommended that
## you resize them so that the vertical dimension is the same as the
## size of the slideshow (currently defaults to 1024x768)
##
## there is a script called "sergey-ensure-resolution" to help with
## this
##

from sergey import *

import os


## NOTE: this bit isn't really part of the example; I will download
## some pictures from my Flickr account for you to see the features
## [keeps the download size low]

if not os.path.isfile('megamid-pano.jpeg') or not os.path.isfile('aspy-valley-climb.jpeg') or not os.path.isfile('chinamans-ne-ridge-corner.jpeg'):
    print("I am going to download some pictures from mike warren's flickr account; this may take a second and won't work if you don't have WGET\n")

    def cmd(c):
        print(c)
        os.system(c)

    cmd('wget "http://farm1.static.flickr.com/200/464155013_f7d1710aed_o.jpg" -O megamid-pano.jpeg')
    cmd('convert -resize 4816x768 megamid-pano.jpeg megamid-pano.jpeg')
    cmd('wget "http://farm3.static.flickr.com/2161/1681952722_571581409a_o.jpg" -O aspy-valley-climb.jpeg')
    cmd('wget "http://farm2.static.flickr.com/1094/1397824929_3940c79eaf_o.jpg" -O chinamans-ne-ridge-corner.jpeg')


#
# okay, we've got some pics; onto the example
#


        # initialize sergey; see the source for options
        # must do this before other stuff
sergey_init()


        # all the "stuff" to do is given as a list of "actions"
        # each action is a two-tuple: a function (probably imported from
        # sergey) and then the tuple of args to that function

actions = []


        # first, start some music, with a title and the album-art FIXME:
        # change paths to work with your system
        # as you can see, it takes three args: the track, a title (with three
        # lines in this case) and an optional album-art JPEG
        # the music will loop if it gets to the end; you can start new music
        # any time.

actions.append( (music, ('/home/mike/sound/artists/nofx/punk-in-drublic--linoleum.mp3','NOFX\n"Linoleum"\nPunk In Drublic','/home/mike/sound/albums/nofx--punk-in-drublic/art.jpeg')) )

        # first, a title (white on a black background)
        # as you can see, newlines are handled. not much else "fancy", though

actions.append( (title, ('Welcome to SERGEY\npygame-based slideshow software',)) )

        # now just show an image. in this case, it is best if you've re-sized
        # the image yourself so pygame doesn't have to do it "live", but
        # whichever.
        # args: the first is the image, the second is the delay (seconds) and
        # the third is an optional caption to put over the bottom of the
        # image. If the caption starts with ! then it is drawn black, not
        # white

actions.append( (show, (load('aspy-valley-climb.jpeg'),4,'I am a Caption')) )

        # panning along a panoramic shot; you should resize your panorama so
        # that the height is the same as the entire screen (default: 768) as
        # this will make the zooming/panning faster (less to resize for
        # pygame). It pre-calculates the images, so if you're getting silent
        # patches in the music this is probably why.
        #
        # args the same as "show", except the caption doesn't currently work

actions.append( (panzoom, (load('megamid-pano.jpeg'),4,'')) )

        # this zooms INTO a portion of a picture. for these, it is usually
        # best to leave the image at full resolution so it looks good when you
        # get all the way in.

        # args: image, delay at full-picture, delay at zoomed portion, portion
        # to zoom to (x, y, width) and an optional caption

actions.append( (zoomin, (load('aspy-valley-climb.jpeg'),5,4,(1700,1300,600),'')) )

        # this zooms out from a picture (the exact opposite of the above). The
        # arguments are the same

actions.append( (zoomout, (load('chinamans-ne-ridge-corner.jpeg'),3,2,(1600,900,500),'')) )

        # more args to "title": the delay and a colour (an RGB triple between
        # 0,255 for each, so this is medium-grey)

actions.append( (title, ('the end',0,(128,128,128))) )


        # start the slideshow
slideshow(actions)

