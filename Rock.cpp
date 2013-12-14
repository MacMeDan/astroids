//
//  Rock.cpp
//  prj4
//
//  Created by Peter Leonard on 3/29/12.
//  Copyright (c) 2012 Digital MTR. All rights reserved.
//
#include "uiInteract.h"  // interface with OpenGL
#include "uiDraw.h"  
#include "rock.h"
#define deg2rad(value) ((M_PI / 180) * (value))



Rock::Rock()
{   
   pos.setX(pos.getXMin() + 5);
   pos.setY(random(pos.getYMin(),pos.getYMax()));
   setDX(random(-5, 5));
   setDY(random(-5, 5));   
}


/**************************************************
 * Missle : MOVE
 * Move the missle accoss the screen
 *************************************************/
void Rock::move()
{
   
   pos.addX(dx); 
   pos.addY(dy);
}

/**************************************************
 * Missle : MOVE
 * Move the missle accoss the screen
 *************************************************/



/**************************************************
 * Missle : Check
 * see if the missle has gone off skreen
 *************************************************/
void Rock::check()
{
   
   if (pos.getX() >= pos.getXMax())
      pos.setX(pos.getXMin()); 
   else if(pos.getX() <= pos.getXMin())
      pos.setX(pos.getXMax());    
   
   if (pos.getY() >= pos.getYMax())
      pos.setY(pos.getYMin());
   else if (pos.getY() <= pos.getYMin())
      pos.setY(pos.getYMax());
}