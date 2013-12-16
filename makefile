###############################################################
# Program:
#    Asteroids:         The playable game
# Authors:
#    David Ivie
#    Dan Leonard
# Summary:
#    This is the simple game of Skeet
###############################################################
a.out : main.cpp main.h uiInteract.o uiDraw.o ship.o bullet.o Rock.o bigAsteroid.o mediumAsteroid.o smallAsteroid.o
	g++ -o a.out main.cpp uiInteract.o uiDraw.o ship.o bullet.o Rock.o bigAsteroid.o mediumAsteroid.o smallAsteroid.o -lglut -lGLU

###############################################################
# Individual files
#    uiDraw.o      Draw polygons on the screen and do all OpenGL graphics
#    uiInteract.o  Handles input events
#    ship.o        What the player moves 
###############################################################
uiInteract.o : uiInteract.cpp uiInteract.h point.h
	g++ -c uiInteract.cpp

uiDraw.o : uiDraw.cpp uiDraw.h point.h
	g++ -c uiDraw.cpp

ship.o : ship.cpp ship.o point.h
	g++ -c ship.cpp

rock.o : Rock.cpp rock.h point.h
	g++ -c Rock.cpp

bullet.o : bullet.cpp bullet.h point.h
	g++ -c bullet.cpp

bigAsteroid.o : bigAsteroid.cpp bigAsteroid.h point.h
	g++ -c bigAsteroid.cpp

mediumAsteroid.o : mediumAsteroid.cpp mediumAsteroid.h point.h
	g++ -c mediumAsteroid.cpp

smallAsteroid.o : smallAsteroid.cpp smallAsteroid.h point.h
	g++ -c smallAsteroid.cpp


###############################################################
# General rules
###############################################################
clean :
	rm a.out *.o

all :  a.out
