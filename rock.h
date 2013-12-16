//
//  rock.h
//  prj4
//
//  Created by Peter Leonard on 3/29/12.
//  Copyright (c) 2012 Digital MTR. All rights reserved.
//

#ifndef prj4_rock_h
#define prj4_rock_h
#include "point.h"
#include "uiDraw.h"

class Rock
{
public:
   
   Rock();
   virtual void draw() = 0;
   float DX()                  const { return dx;             };
   float DY()                  const { return dy;             };
   void move();
   void check();
   float speed();
   bool dead;
   Point getPos()              const { return pos;            };
  
   void setPos(Point pos)            { this->pos = pos;       };
   void setSpeed(float speed, float getAngle());
   void setAngle(float angle)        { this->angle = angle;   };
   float getAngle()                  { return angle;          };
   void setDX(float dx)              { this->dx = dx;         };             
   void setDY(float dy)              { this->dy = dy;         };
   
private:
   Point pos;
   float angle;
   float dx;     // horizontal velocity of the ship
   float dy;
   
};

#endif
