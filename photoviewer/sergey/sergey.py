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
## Slideshow software based on pygame. See README for more
## (You do not want to run this module...)
##

import sys
import pdb
import logging

if __name__=='__main__':
    print("Do not run this; see README or DOCUMENTATION for usage instructions.")
    sys.exit(-1)
    

# print('''
# sergey
# Copyright (C) 2007 Mike Warren <mike@mike-warren.com>

# This program comes with ABSOLUTELY NO WARRANTY; for details see
# http://mike-warren.com/sergey or the source code. This is free
# software, and you are welcome to redistribute it under certain
# conditions; see the source code for details.
# ''')




import os.path
import pygame
import time
import sys
import types
from photoviewer.transitions import transitions

options = {}
options['init'] = False
DEFAULT_DELAY = 4

def sergey_init(size=False,
                fontfile='/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf',
                cache=False):
    
    global options
    
    pygame.init()
    pygame.display.init()
    try:
        pygame.mixer.init()
        options['music'] = True
    except:
        options['music'] = False
    pygame.font.init()
    if size:
        screen = pygame.display.set_mode(size)
    else:
        screen = pygame.display.set_mode((0, 0),pygame.HWSURFACE|pygame.FULLSCREEN)
    
    options['screen'] = screen
    
    infoObject = pygame.display.Info()
    options['size'] = (infoObject.current_w, infoObject.current_h)
    
    transitions.init(screen,infoObject.current_w, infoObject.current_h)    
    try:
        options['font'] = pygame.font.SysFont("helvetica",12)
    except IOError:
        print()
        print("  Font file doesn't exist: \"%s\"" % fontfile)
        print("  Please specify something else to sergey_init()")
        print()
        raise
    options['quick_burn'] = False
    options['debug'] = False
    options['init'] = True
    if cache:
        options['cache_pics'] = True
    else:
        options['cache_pics'] = False

def sergy_shutdown():
    log.info("Shutdown")
    pygame.display.quit()


def ensurepic(image):
    if not (type(image) is bytes):
        return pygame.image.load(image).convert()
    return image

def waitForKey(key=None):
    while 1:
        evt = pygame.event.poll()
        if evt.type == pygame.KEYUP:
            if key is None:
                break
            elif evt.key == key:
                break

def music(sndtrack,t=None,art=None):
    global options
    log.debug("Queue Music %s",sndtrack)
    if not options['music']:
        print("ERROR: mixer not available")
        return

    if not os.path.isfile(sndtrack):
        print("ERROR: can't find \"%s\"" % sndtrack)
        return
    
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.fadeout(500)

    pygame.time.delay(400)
    pygame.mixer.music.load(sndtrack)
    pygame.mixer.music.play(2)

    if t:
        text = t
    else:
        text = sndtrack.split('/')[-1].split('.')[0]
        text = ' '.join([a.capitalize() for a in text.split('-')])

    if art and os.path.isfile(art):
        arttitle(text, pygame.image.load(art))
    else:
        title(text,2,(200,255,200))


def title(text,delay=3,color=(255,255,255)):
    if options['quick_burn']: delay = 0.25
    lines = None
    if '\n' in text:
        lines = text.split('\n')

    options['screen'].fill((0,0,0))
    (sWidth,sHeight) = options['size']

    if not lines:
        surf = options['font'].render(text, True, color, (0,0,0))
        (w,h) = surf.get_size()
        x = (sWidth/2) - (w/2)
        y = (sHeight/2) - (h/2)
        options['screen'].blit(surf, (x,y))
        pygame.display.update()

    else:
        # multiline
        yinc = options['font'].get_linesize() + 20
        y = (sHeight/2) - ((len(lines)*yinc)/2);
        for line in lines:
            surf = options['font'].render(line, True, color, (0,0,0))
            (w,h) = surf.get_size()
            x = (sWidth/2) - (w/2)
            options['screen'].blit(surf, (x,y))
            y = y + yinc
            
        pygame.display.update()

    if delay:
        pygame.time.delay(int(delay*1000))
    

def arttitle(text,pic):
    global options
    lines = None
    color = (255,255,255)
    if '\n' in text:
        lines = text.split('\n')

    options['screen'].fill((0,0,0))
    (sWidth,sHeight) = options['size']

    y = 50
    if not lines:
        surf = options['font'].render(text, True, color, (0,0,0))
        (w,h) = surf.get_size()
        x = (sWidth/2) - (w/2)
        options['screen'].blit(surf, (x,y))
        pygame.display.update()

    else:
        # multiline
        yinc = options['font'].get_linesize() + 2
        for line in lines:
            surf = options['font'].render(line, True, color, (0,0,0))
            (w,h) = surf.get_size()
            x = (sWidth/2) - (w/2)
            options['screen'].blit(surf, (x,y))
            y = y + yinc
            
        pygame.display.update()

    if None:
        (w,h) = surf.get_size()
        x = (sWidth/2) - (w/2)
        y = 70
        options['screen'].blit(surf, (x,y))
    image = pygame.transform.scale(pic, (300,300))
    options['screen'].blit(image, (362,234))
    pygame.display.update()

    if options['quick_burn']:
        pygame.time.delay(250)
    else:
        pygame.time.delay(2000)
    
def credittitle(text,pic):
    global options
    lines = None
    options['screen'].fill((0,0,0))
    (sWidth,sHeight) = options['size']

    surf = options['font'].render(text, True, (255,255,255), (0,0,0))
    (w,h) = surf.get_size()
    x = (sWidth/2) - (w/2)
    y = 70
    options['screen'].blit(surf, (x,y))
    image = pygame.transform.scale(pic, (768,576))
    options['screen'].blit(image, (128, 150))
    pygame.display.update()

    if options['quick_burn']:
        pygame.time.delay(250)
    else:
        pygame.time.delay(3000)
    
def rendertitle(title):
    if title and len(title):
        if title[0] == '!':
            title = title[1:]
            color = (0,0,0)
        else:
            color = (255,255,255)
        return options['font'].render(title, True, color)

def realzoom(image,delay0,delay1, xxx_todo_changeme,title,dir):
    (x,y,zoomwidth) = xxx_todo_changeme
    image = ensurepic(image)
    global options
    if options['quick_burn']: delay=0.25

    (width,height) = image.get_size()
    (sWidth,sHeight) = options['size']

    title = rendertitle(title)

    print(title," width,height:",width,height)
    if height > sHeight:
        if width < height:
            scaleratio = height/sHeight
            newheight = sHeight
            newwidth = int(width / scaleratio)
            #print "scaling to",newwidth,newheight

        else:
            scaleratio = width/sWidth
            newwidth = sWidth
            newheight = int(height/scaleratio)
            print("scaling to",newwidth,newheight)

        scaled = pygame.transform.scale(image, (newwidth,newheight))
        scaled.set_colorkey()
        
    else:
        scaled = image
        newwidth = width
        newheight = height



    ratio = height/float(width)
    xrange = zoomwidth
    yrange = xrange * ratio
    
    options['screen'].fill((0,0,0))
    start = time.time()
    
    if dir == 'in':
        options['screen'].fill((0,0,0))
        options['screen'].blit(scaled, ((sWidth-scaled.get_size()[0])/2,0))
        if title:
            options['screen'].blit(title,((sWidth/2) - title.get_size()[0]/2,sHeight-title.get_size()[1]))
        pygame.display.flip()

    ## make zoomed images

    steps = 20
    r = image.get_rect()
    stepwidth = (r[2] - xrange) / (float(steps))
    stepheight = (r[3] - yrange) / (float(steps))
    stepx = (x) / (float(steps))
    stepy = (y) / (float(steps))
    w = sWidth
    h = int(w * ratio)
    zooms = []
    thex = x
    they = y
    shown = False
    for foo in range(steps+1):
        zoom = image.subsurface( (int(thex), int(they), int(xrange), int(yrange)) )
        zoom = pygame.transform.scale(zoom, (w,h))
        zooms.append( (zoom,(sHeight/2)-(h/2),w) )
        thex = thex - stepx
        they = they - stepy
        xrange = xrange + stepwidth
        yrange = yrange + stepheight

        if not shown:
            shown = True
            if dir == 'out':
                options['screen'].blit(zoom, (0,(sheight/2)-(h/2)))
                if title:
                    options['screen'].blit(title,((sWidth/2) - title.get_size()[0]/2,sHeight-title.get_size()[1]))
                pygame.display.flip()
            else:
                if 0:
                    options['screen'].blit(scaled, (0,0))
                    if title:
                        options['screen'].blit(title,((sWidth/2) - title.get_size()[0]/2,sHeight-title.get_size()[1]))
                    pygame.display.flip()

    if dir == 'in':
        zooms.reverse()
    else:
        pass
    
    pygame.time.delay(int((delay0*1000)/2))

    if dir == 'out':
        zooms = zooms[1:]
    for (zoom,y,mywidth) in zooms:
        options['screen'].blit(zoom, (0,y))
        if title:
            options['screen'].blit(title,((sWidth/2) - title.get_size()[0]/2,sHeight-title.get_size()[1]))
        pygame.display.flip()
        evt = pygame.event.poll()
        if evt.type == pygame.KEYUP and evt.key == 32:
            break

    if 0:#dir == 'out':
        options['screen'].fill((0,0,0))
        options['screen'].blit(scaled, ((sWidth-scaled.get_size()[0])/2,0))
        if title:
            options['screen'].blit(title,((sWidth/2) - title.get_size()[0]/2,sHeight-title.get_size()[1]))
        pygame.display.flip()
        
    pygame.time.delay(int((delay1*1000)/2))

def zoomout(image,delay0,delay1, xxx_todo_changeme1,title=None):
    (x,y,zoomwidth) = xxx_todo_changeme1
    realzoom(image,delay0,delay1,(x,y,zoomwidth),title=title,dir='out')
def zoomin(image,delay0,delay1, xxx_todo_changeme2,title=None):
    (x,y,zoomwidth) = xxx_todo_changeme2
    realzoom(image,delay0,delay1,(x,y,zoomwidth),title=title,dir='in')

def show(image,delay,title=None):
    global options
    if options['debug']:
        title = str(image)
    (sWidth,sHeight) = options['size']
        
    image = ensurepic(image)
    if options['quick_burn']: delay=0.25
    if int(delay) == 4:
        delay = 3

    (width,height) = image.get_size()

    titleImg = rendertitle("{} {}x{}".format(title,width,height))

    log.debug("%s width,height:%d %d",title,width,height)
    if height > sHeight:
        if height > width:
            scaleratio = height/sHeight
            newheight = sHeight
            newwidth = int(width / scaleratio)
            log.debug("scaling by height to %d,%d",newwidth,newheight)

        else:
            scaleratio = width/sWidth
            newwidth = sWidth
            newheight = int(height/scaleratio)
            log.debug("scaling by width to %d,%d",newwidth,newheight)

        scaled = pygame.transform.scale(image, (newwidth,newheight))
        scaled.set_colorkey()
    else:
        scaled = image
        newwidth = width
        newheight = height

    x = (sWidth/2) - (newwidth/2)
    y = (sHeight/2) - (newheight/2)
    options['screen'].blit(scaled, (x,y))
    if titleImg:
        options['screen'].blit(titleImg,((sWidth/2) - titleImg.get_size()[0]/2,sHeight-titleImg.get_size()[1]))

    pygame.display.flip()
    pygame.time.wait(int(delay*1000))

def panzoom(image,delay,author=None):
    image = ensurepic(image)
    global options
    (width,height) = image.get_size()

    if author:
        author = options['font'].render(author, True, (128,128,128))
        author = pygame.transform.rotate(author, 90)

    #print "width,height:",width,height
    if height > 768:
        if width > height:
            scaleratio = height/768.0
            newheight = 768
            newwidth = int(width / scaleratio)
            print("scaling to",newwidth,newheight)

        else:
            scaleratio = height/768.0
            newheight = 768
            newwidth = int(width / scaleratio)
            #print "scaling to",newwidth,newheight

        scaled = pygame.transform.scale(image, (newwidth,newheight))
        scaled.set_colorkey()
    else:
        scaled = image
        newwidth = width
        newheight = height

    if newwidth > 1024:
        dims = (1024,int(1024*float(height)/float(width)))
        #print "TINY is",dims
        tiny = pygame.transform.scale(image, dims)
        options['screen'].fill((0,0,0))
        options['screen'].blit(tiny, (0,384-(dims[1]/2)))
        pygame.display.update()
        start = time.time()
        if options['quick_burn']:
            pygame.time.delay(250)
            return
        
        ## make zoomed images

        steps = 20
        step = (768-dims[1]) / steps
        w = 1024
        h = dims[1]
        zooms = []
        for foo in range(steps):
            h = int(h + step)
            w = int(h * (float(width)/height))
            zoom = pygame.transform.scale(image, (w,h))
            zooms.append( (zoom,384-(h/2),w) )

        ## check time
        if None:
            elapsed = time.time() - start
            if elapsed < delay:
                #print "EXTRA DELAY:",delay-elapsed
                pygame.time.delay(int((delay-elapsed)*1000))
        else:
            pygame.time.delay(2000)

        for (zoom,y,mywidth) in zooms:
            options['screen'].blit(zoom, (0,y))
            pygame.display.flip()
            evt = pygame.event.poll()
            if evt.type == pygame.KEYUP and evt.key == 32:
                break
            
        ## pan
        
        xrange = newwidth - 1024
        step = 8
        steps = int(xrange/step)
        x = 0
        #print "step is",step
        for foo in range(steps):
            options['screen'].blit(scaled, (int(x),0))
            x = x - step
            pygame.display.flip()
            evt = pygame.event.poll()
            if evt.type == pygame.KEYUP and evt.key == 32:
                break
            #pygame.display.update()
            #pygame.time.delay(10)

        zooms.reverse()
        for (zoom,y,mywidth) in zooms:
            options['screen'].fill((0,0,0))
            options['screen'].blit(zoom, (1024-mywidth,y))
            pygame.display.flip()
            evt = pygame.event.poll()
            if evt.type == pygame.KEYUP and evt.key == 32:
                break
            
        options['screen'].fill((0,0,0))
        options['screen'].blit(tiny, (0,384-(dims[1]/2)))
        pygame.display.flip()
        pygame.time.delay(1500)
        
    else:
        x = (1024/2) - (newwidth/2)
        y = (768/2) - (newheight/2)
        options['screen'].blit(scaled, (x,y))
        if author:
            options['screen'].blit(author,(0,0))
        pygame.display.flip()
        pygame.time.delay(int(delay*1000))
    
def fade(image,delay,title=None):
    image = ensurepic(image)
    global options
    (width,height) = image.get_size()

    (sWidth,sHeight) = options['size']

    (width,height) = image.get_size()

    titleImg = rendertitle("{} {}x{}".format(title,width,height))

    log.debug("%s width,height:%d %d",title,width,height)
    if height > sHeight:
        if height > width:
            scaleratio = height/sHeight
            newheight = sHeight
            newwidth = int(width / scaleratio)
            log.debug("scaling by height to %d,%d",newwidth,newheight)

        else:
            scaleratio = width/sWidth
            newwidth = sWidth
            newheight = int(height/scaleratio)
            log.debug("scaling by width to %d,%d",newwidth,newheight)

        scaled = pygame.transform.scale(image, (newwidth,newheight))
        scaled.set_colorkey()
    else:
        scaled = image
        newwidth = width
        newheight = height

    x = (sWidth/2) - (newwidth/2)
    y = (sHeight/2) - (newheight/2)
    
    newImage = pygame.Surface((sWidth,sHeight))
    newImage.blit(scaled, (x,y))
    
    if titleImg:
        newImage.blit(titleImg,((sWidth/2) - titleImg.get_size()[0]/2,sHeight-titleImg.get_size()[1]))
                        
    clock = pygame.time.Clock()
    transitions.run(newImage,'fade')
    print("tx start")    
       
    while transitions.updateScreen() != False:
        pygame.display.flip()

        clock.tick(50)
            
    print("tx fin")    
    
def startmovie(fname, sndtrack,size=None):
    global options
    
    movie = pygame.movie.Movie(fname)
    if sndtrack:
        pygame.mixer.music.load(sndtrack)

    options['screen'].fill((0,0,0))
    (sWidth,sHeight) = options['size']

    pygame.display.update()
    if size == None:
        movie.set_display(screen, (0,0,sWidth,sHeight))
    else:
        (w,h) = size
        movie.set_display(screen, ((sWidth/2)-int(w/2),0,w,h))
    movie.play()
    if sndtrack:
        pygame.mixer.music.play()

    if not movie.has_video():
        raise "No video in movie " + str(fname)
    return movie

def makeimages(dir,delay=DEFAULT_DELAY):
    rtn = []
    directory = os.listdir(dir)
    directory.sort()
    for x in directory:
        path = os.path.join(dir,x)
        if x.split('.')[-1].lower() in ['jpg','jpeg']:
            rtn.append( (pygame.image.load(path),delay,x) )
            title('loading...\n%s'%x,0,(100,100,100))
    return rtn

def makeactions(imgs):
    rtn = []
    for (img,delay,path) in imgs:
        author = None
        if '_' in path:
            author = ' '.join(path.split('_')[1].split('-'))
        rtn.append( (show, (img,delay,author)))
    return rtn




def load(path):
    global options
    if not options['cache_pics']:
        return path
    title('loading...\n%s'%path,0,(100,100,100))
    return pygame.image.load(path).convert()
    



def slideshow(actions,wait=True):
    try:
        global options
        if options['init'] == False:
            print("WARNING: you didn't initialize SERGEY; using defaults")
            sergey_init()
            
        if wait:
            title(str.format("(press space to start) screen res {}",options['size']))
            waitForKey()
            pygame.mouse.set_visible(False)

        start = time.time()
        movie = None
        paused = False
        nextActionImmediately = True
        autopilot = True
        action = None
        while 1:
            evt = pygame.event.poll()

            doaction = False
            if evt.type == pygame.NOEVENT:
                if nextActionImmediately is True or autopilot:
                    if not movie or not movie.get_busy():
                        doaction = True
                        nextActionImmediately = False

                pygame.time.delay(25)

            if evt.type == pygame.KEYUP:
                if evt.key == 113:
                    print("QUIT!")
                    break
                elif evt.key == 112:
                    if movie:
                        if not paused:
                            print("pausing movie")
                            movie.pause()
                            pygame.mixer.music.pause()
                            paused = True
                        else:
                            print("resuming movie")
                            movie.pause()
                            pygame.mixer.music.unpause()
                            paused = False

                elif evt.key == 32 or evt.key == 110:
                    if movie and movie.get_busy():
                        if evt.key == 32:
                            print("  movie still playing; be patient")
                            continue
                        else:
                            movie.stop()
                            pygame.mixer.music.stop()
                    doaction = True

            if doaction:
                doaction = False

                                                # try to use ref-counting, not
                                                # the garbage-collector
                if action:
                    (fn, args) = action
                    for foo in args:
                        del foo
                    del args

                if len(actions) == 0:
                    break;
                action = actions[0]
                if type(action) == type([]):
                    actions = action + actions[1:]
                    action = actions[0]
                actions = actions[1:]
                (fn,args) = action
                
                rtn = fn(*args)
                if rtn:
                    movie = rtn

        end = time.time()

        pygame.mouse.set_visible(True)
        
        if wait:
            waitForKey()

        elapsed = (end-start)
        print("total running time: ",elapsed,"seconds")
        print("   minutes:", elapsed/60.0)
    finally:
        sergy_shutdown()

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


