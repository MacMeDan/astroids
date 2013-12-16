//
//  bullet.h
//  test
//

#ifndef bullet_h
#define bullet_h
#include "ship.h"

class Bullet : public Ship
{
   
public:
   Bullet(Ship & ship);
   void drawb();
   void bmove();
   int getALife()              { return aLife; };

private:
   int aLife;
   
      
}; 


#endif
