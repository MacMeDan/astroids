//
//  mediumAsteroid.cpp
//  Prj4
//
//  Created by David Ivie on 3/29/12.
//  Copyright (c) 2012 Brigham Young University. All rights reserved.
//

#include <iostream>
#include "mediumAsteroid.h"

/***************************************************
 * MediumAsteroid :: CONSTRUCTOR
 * initializes the asteroid based on a BigAsteroid
 ***************************************************/
MediumAsteroid::MediumAsteroid(BigAsteroid & oldAsteroid, int change)
{   
   setAngle(oldAsteroid.getAngle());
   setPos(oldAsteroid.getPos());
   setDX(oldAsteroid.DX());
   setDY(oldAsteroid.DY() + change);   
}

void MediumAsteroid::draw()
{
   Point a = getPos();
   Point b = getPos();
   Point c = getPos();
   Point d = getPos();
   
   a.setX(a.getX() + 900);
   b.setX(b.getX() - 900);
   c.setY(c.getY() + 900);
   d.setY(d.getY() - 900);
   
   drawCircle(getPos(), 20, 7, getAngle());
   drawCircle(a, 20, 7, getAngle());   
   drawCircle(b, 20, 7, getAngle());   
   drawCircle(c, 20, 7, getAngle());   
   drawCircle(d, 20, 7, getAngle());
   setAngle(getAngle() + 5);
}