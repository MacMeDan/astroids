//
//  smallAsteroid.cpp
//  Prj4
//
//  Created by David Ivie on 3/29/12.
//  Copyright (c) 2012 Brigham Young University. All rights reserved.
//

#include <iostream>
#include "smallAsteroid.h"

/***************************************************
 * SmallAsteroid :: CONSTRUCTOR
 * initializes the asteroid based on a BigAsteroid
 ***************************************************/
SmallAsteroid::SmallAsteroid(BigAsteroid & oldAsteroid)
{   
   setAngle(oldAsteroid.getAngle());
   setPos(oldAsteroid.getPos());
   setDX(oldAsteroid.DX() + 2);
   setDY(oldAsteroid.DY());   
}

/***************************************************
 * SmallAsteroid :: CONSTRUCTOR
 * initializes the asteroid based on a MediumAsteroid
 ***************************************************/
SmallAsteroid::SmallAsteroid(MediumAsteroid & oldAsteroid, int change)
{   
   setAngle(oldAsteroid.getAngle());
   setPos(oldAsteroid.getPos());
   setDX(oldAsteroid.DX() + 3 * change);
   setDY(oldAsteroid.DY());   
}

void SmallAsteroid::draw()
{
   Point a = getPos();
   Point b = getPos();
   Point c = getPos();
   Point d = getPos();
   
   a.setX(a.getX() + 900);
   b.setX(b.getX() - 900);
   c.setY(c.getY() + 900);
   d.setY(d.getY() - 900);
   
   drawCircle(getPos(), 10, 5, getAngle());   
   drawCircle(a, 10, 5, getAngle());   
   drawCircle(b, 10, 5, getAngle());   
   drawCircle(c, 10, 5, getAngle());   
   drawCircle(d, 10, 5, getAngle());
   setAngle(getAngle() + 10);
}