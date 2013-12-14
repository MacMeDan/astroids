//
//  bullet.cpp
//  test
//


#include "uiInteract.h"  // interface with OpenGL
#include "uiDraw.h"      // all the draw primitives exist here
#include "bullet.h"
#include "ship.h"
#define deg2rad(value) ((M_PI / 180) * (value))

/***************************************************
 * Bullet :: CONSTRUCTOR
 * Give the pigoen a random vertical velocity and set
 * the positions of everything else.
 ***************************************************/
Bullet::Bullet(Ship & ship) 
{
   setType(BULLET);
   setPos(ship.getPos());
   setAngle(ship.getAngle());
   setSpeed(20, getAngle());
   move();
   aLife = 30 * 1;
   setDX(DX() + ship.DX());
   setDY(DY() + ship.DY());
   
};


/**************************************************
 * Bullet : drawb
 * Draw the Bullet
 *************************************************/
void Bullet::drawb()
{
  
   drawCircle(getPos(), 1, 4, 0);
   aLife--;
   
}
