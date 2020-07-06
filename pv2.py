
##
## you resize them so that the vertical dimension is the same as the
## size of the slideshow (currently defaults to 1024x768)
##
## there is a script called "sergey-ensure-resolution" to help with
## this
##

from sergey import *
import os
import pvlogger
import pvconfig
from PIL import Image
from PIL.ExifTags import TAGS

from photoviewer_model import Photo

def main():
    log.info('PV Started')
    photos = getPhotos(pvconfig.PHOTO_DIR)
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

    for photo in photos:
        actions.append( (show, (load(photo.path),4,photo.label)) )


        # now just show an image. in this case, it is best if you've re-sized
        # the image yourself so pygame doesn't have to do it "live", but
        # whichever.
        # args: the first is the image, the second is the delay (seconds) and
        # the third is an optional caption to put over the bottom of the
        # image. If the caption starts with ! then it is drawn black, not
        # white

    #actions.append( (show, (load('aspy-valley-climb.jpeg'),4,'I am a Caption')) )

        # panning along a panoramic shot; you should resize your panorama so
        # that the height is the same as the entire screen (default: 768) as
        # this will make the zooming/panning faster (less to resize for
        # pygame). It pre-calculates the images, so if you're getting silent
        # patches in the music this is probably why.
        #
        # args the same as "show", except the caption doesn't currently work

    #actions.append( (panzoom, (load('megamid-pano.jpeg'),4,'')) )

        # this zooms INTO a portion of a picture. for these, it is usually
        # best to leave the image at full resolution so it looks good when you
        # get all the way in.

        # args: image, delay at full-picture, delay at zoomed portion, portion
        # to zoom to (x, y, width) and an optional caption

    #actions.append( (zoomin, (load('aspy-valley-climb.jpeg'),5,4,(1700,1300,600),'')) )

        # this zooms out from a picture (the exact opposite of the above). The
        # arguments are the same

    #actions.append( (zoomout, (load('chinamans-ne-ridge-corner.jpeg'),3,2,(1600,900,500),'')) )

        # more args to "title": the delay and a colour (an RGB triple between
        # 0,255 for each, so this is medium-grey)

    actions.append( (title, ('the end',0,(128,128,128))) )

        # start the slideshow
    slideshow(actions)

# Get a list of photos to display
def getPhotos(dir):
    photolist = list()

    log.info("Scan photos at %s" % dir)
           
    for dirpath, dirnames, filenames in os.walk(dir):
        if filenames:
            for filename in sorted(filenames):
                if is_image(filename):
                    pathname = os.path.join(dirpath, filename)
                    pathname = str(pathname)

                    rotation = get_photo_rotation(pathname) or 0
                    mtime = os.path.getmtime(pathname)
                    file_date = time_to_string(mtime)
                    transition = ''
                    photolist.append(Photo(0,pathname,filename,rotation,transition,5))

    log.debug("%d photo files found. " % (len(photolist)))

    return photolist
# Get the Photos rotation
def get_photo_rotation(path):
    rotation_degrees = None

    try:
        image = Image.open(path)
    except IOError:
        image = None

    if image and hasattr(image, "_getexif"):
        try:
            exif = image._getexif()
        except Exception as e:
            exif = None
            log.error("Exception Rotation for %s: %s" % (path, e))
        if exif:
            rotation = exif.get(0x0112, 1)
            log.debug("Rotation for %s: %s" % (path, rotation))
            if rotation == 6:
                rotation_degrees = -90
            elif rotation == 8:
                rotation_degrees = 90
            title = exif.get(0x010e,1)
            log.debug("Image description %s",title)

    return rotation_degrees

def time_to_string(t):
    # Convert to a tuple.
    localtime = time.localtime(t)
    # Convert to a nice string.
    return time.strftime("%B %-d, %Y", localtime)

# Filter image files 
def is_image(pathname):
    _, ext = os.path.splitext(pathname)
    return ext.lower() in pvconfig.FILE_FORMATS


if __name__ == "__main__":
    # Create a custom logger
    log = pvlogger.logInit()
    main()
