/*****************************************
 * POINT
 * A very simple point class.  You will most
 * likely want to use something much better
 * than this
 ****************************************/
#ifndef POINT_H
#define POINT_H

#include <iostream>
enum { ASTEROID, BULLET, SHIP };

/*******************
 * POINT
 *******************/
class Point
{
public:
   // constructors
   Point()                : x(0.0 ),  y(0.0 ) {};
   Point(const Point &pt) : x(pt.x),  y(pt.y) {};
   Point(bool noError)    : x(0.0 ),  y(0.0 ) {};
   Point(float x, float y): x(x   ),  y(y  )  {};
   ~Point()
   {
      x = NULL;
      y = NULL;
   }
      
   // getters
   float getX()    const { return x;     };
   float getY()    const { return y;     };
   float getXMax() const { return  900;  };
   float getYMax() const { return  900;  };
   float getXMin() const { return  0;  };
   float getYMin() const { return  0;  };
   
   void operator = (Point & rhs)
   {
      x = rhs.x;
      y = rhs.y;
   }
   
   Point operator - (const Point & rhs)
   {
      Point temp;
      temp.x = x - rhs.x;
      temp.y = y - rhs.y;
      return temp;
   }
   
   void operator -= (const Point & rhs)
   {
      x -= rhs.x;
      y -= rhs.y;
   }
   
   
   
   Point operator + (const int input) const;

   // setters
   void setX(float x)    { this->x = x;   };
   void setY(float y)    { this->y = y;   };
   void addX(float dx)   { this->x += dx; };
   void addY(float dy)   { this->y += dy; };
   void multX(float ax)  { this->x *= ax; };
   void multY(float ay)  { this->y *= ay; };
    

private:
   float x;
   float y;
};

#endif 
