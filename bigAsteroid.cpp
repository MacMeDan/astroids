//
//  bigAsteroid.cpp
//  Prj4
//
//  Created by David Ivie on 3/29/12.
//  Copyright (c) 2012 Brigham Young University. All rights reserved.
//

#include <iostream>
#include "bigAsteroid.h"

/***************************************************
 * BigAsteroid :: CONSTRUCTOR
 * initializes the asteroid
 ***************************************************/
BigAsteroid::BigAsteroid()
{   
   setAngle(0);
   getPos().setX(getPos().getXMin() + 5);
   getPos().setY(random(getPos().getYMin(),getPos().getYMax()));
   setDX(random(-5, 5));
   setDY(random(-5, 5));   
}

void BigAsteroid::draw()
{
   Point a = getPos();
   Point b = getPos();
   Point c = getPos();
   Point d = getPos();
   
   a.setX(a.getX() + 900);
   b.setX(b.getX() - 900);
   c.setY(c.getY() + 900);
   d.setY(d.getY() - 900);
   
   drawCircle(getPos(), 30, 10, getAngle());
   drawCircle(a, 30, 10, getAngle());   
   drawCircle(b, 30, 10, getAngle());   
   drawCircle(c, 30, 10, getAngle());   
   drawCircle(d, 30, 10, getAngle());
   setAngle(getAngle() + 2);
}
