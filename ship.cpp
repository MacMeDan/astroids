   //
   //  missle.cpp
   //  test
   //
   //  Created by Peter Leonard on 2/16/12.
   // 
   //
#include "point.h"       // the missle has a position
#include "uiDraw.h"      // all the draw primitives exist here
#include "ship.h"
#define deg2rad(value) ((M_PI / 180) * (value))


/***************************************************
 * Ship :: CONSTRUCTOR
 * Give the Ship a starting position in the middle, 
 * and a starting angle, and a starting velocity
 ***************************************************/
Ship::Ship() : pos()
{
   type = SHIP;
   pos.setX(450);
   pos.setY(450);
   dy = 2;
   dx = 0;
   angle = 270;
   Acc();
   dead = false;
   
};

/***************************************************
 * Ship :: DECONSTRUCTOR
 * Uninitialize all data linked with the ship.
 ***************************************************/
Ship::~Ship()
{
   type = NULL;
   dead = true;
   angle = NULL;
   dx = NULL;
   dy = NULL;
   ax = NULL;
   ay = NULL;
   pos.~Point();
}

/*************************************************
 * Missle : Acc
 * makes the missle move like a plane not a spaceship
 ************************************************/
void Ship::Acc()
{
   
   
   ax = .25 * cos(deg2rad(angle)); // code to move like a spaceship
   ay = .25 * sin(deg2rad(angle));
   dy -= ay;
   dx -= ax;
}
/**************************************************
 * Missle : MOVE
 * Move the missle accoss the screen
 *************************************************/
void Ship::move()
{
   pos.addX(dx); 
   pos.addY(dy);
     
}

/**************************************************
 * Ship : getSpeed
 * returns the speed
 *************************************************/
float Ship::getSpeed()
{
   return 1 / (sin(atan(dy/dx)) * dy);
}

/**************************************************
 * Ship : setSpeed
 * sets the dx and dy according to the float passed
 *************************************************/
void Ship::setSpeed(float speed, float angle)
{
   setDX(-cos(deg2rad(angle)) * speed);
   setDY(-sin(deg2rad(angle)) * speed);
}

/*************************************************
 * Ship : DRAW
 * Draw the stuff
 ************************************************/
void Ship::draw()
{
      //  draw ship
   Point a (getPos());
   Point b (getPos());
   Point c (getPos());
   Point d (getPos());
   
   a.setX(a.getX() + 900);
   b.setX(b.getX() - 900);
   c.setY(c.getY() + 900);
   d.setY(d.getY() - 900);
   
   drawShip(getPos(), angle);
   drawShip(a, angle);
   drawShip(b, angle);
   drawShip(c, angle);
   drawShip(d, angle);
}

/**************************************************
 * Ship : Check
 * see if the Ship has gone off skreen
 *************************************************/
void Ship::check()
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
