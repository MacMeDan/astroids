//
//  main.h
//  prj4
//
//  Created by Peter Leonard on 3/19/12.
//  Copyright (c) 2012 Digital MTR. All rights reserved.
//

#ifndef prj4_main_h
#define prj4_main_h
#include "ship.h"
#include <vector>
#include "bullet.h"
#include "rock.h"
#include "bigAsteroid.h"
#include "mediumAsteroid.h"
#include "smallAsteroid.h"

class Asteroids
{
public:
   Asteroids();
   Ship ship;
   std::vector <Bullet> bullets;
   std::vector <BigAsteroid> bigRocks;
   std::vector <MediumAsteroid> medRocks;
   std::vector <SmallAsteroid> smallRocks;
   void draw(); 
   void drawCollision();// draw everything
   void move(int up, int down, int right, int left);     // move everything
   void strike();
   int delay;
   int getScore() { return score; };
   int setScore(int score) {this->score = score; }; 
private:
   int score;    // current score.. how many times did we hit the ball?
}; 

#endif
