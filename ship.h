   //
   // ship.h
   //
   //  Created by Dan Leonard
   //         and David Ivie

#ifndef ship_h
#define ship_h
#include "point.h"


class Ship
{
public:
 
   Ship();           // Initilise the ship
   ~Ship();
   void draw();          
   void move();
   void Acc();
   void check();
      // Getters
   Point & getPos()                  { return pos;            };
   float DX()                  const { return dx;             };
   float DY()                  const { return dy;             };
   float getXX()                     {return pos.getX();      };
   float getYY()                     {return pos.getY();      };
   float getAngle()            const { return angle;          };
   float getSpeed();
   int getType()               const { return type;           };
   bool isDead()               const { return dead;           };

   //Setters
   void setSpeed(float speed, float angle);
   void setAngle(float angle)        { this->angle = angle;   };
   
   void setPos(Point pos)            { this->pos = pos;       };
   void setDX(float dx)              { this->dx = dx;         };             
   void setDY(float dy)              { this->dy = dy;         };
   void setType(int type)            { this->type = type;     };
   
private:                       
   float angle;
   Point pos;
   int type;
   float dx;     // horizontal velocity of the ship
   float dy;     // vertical velocity
   float ax;
   float ay;
   bool dead;  
}; 


#endif

