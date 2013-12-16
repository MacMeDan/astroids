   //
   //  main.cpp
   //  prj4
   //
   //  Created by Peter Leonard on 3/19/12.
   //
   //  Created by David Ivie on 3/19/12.
   //  Copyright (c) 2012 Digital MTR. All rights reserved.
   //

#include "main.h"
#include <vector>
#include "uiInteract.h"  // interface with OpenGL
#include "uiDraw.h"      // all the draw primitives exist here
#include <cmath>
#include <cassert>
#define GUN 20
#define deg2rad(value) ((M_PI / 180) * (value))
#define NUMBULLETS 15
#define ROCKS 1

/***************************************************
 * Asteroids :: CONSTRUCTOR
 * initializes all the data for the asteroids game
 ***************************************************/
Asteroids::Asteroids() 
{
   for (int i = 0; i < 6; i++)
   {
      bigRocks.push_back(BigAsteroid());
   }

   score = 0;
   
};

/*********************************************
 * CALLBACK
 * The main interaction loop of the engine.
 *********************************************/
void callBack(const Interface *pUI, void *p)
{
   
   Asteroids *pAsteroids = (Asteroids *)p;
   
   pAsteroids->strike();
   if (pAsteroids->getScore() == 10)
   for (int i = 0; i < 2; i++)
       {
      pAsteroids->bigRocks.push_back(BigAsteroid());
      pAsteroids->setScore(pAsteroids->getScore()+1);
       }
   
   if (pAsteroids->getScore() == 30)
      for (int i = 0; i < 4; i++)
          {
         pAsteroids->bigRocks.push_back(BigAsteroid());
         pAsteroids->setScore(pAsteroids->getScore()+1);
          }
   if (pAsteroids->getScore() == 100)
      for (int i = 0; i < 8; i++)
          {
         pAsteroids->bigRocks.push_back(BigAsteroid());
         pAsteroids->setScore(pAsteroids->getScore()+1);
          }
   if  (pAsteroids->getScore() == 200)
      for (int i = 0; i < 16; i++)
          {
         pAsteroids->bigRocks.push_back(BigAsteroid());
         pAsteroids->setScore(pAsteroids->getScore()+1);
          }
   
   Point pointScore(pAsteroids->ship.getPos().getXMax() - 50, pAsteroids->ship.getPos().getYMax() - 20);
   drawNumber(pointScore, pAsteroids->getScore());

   if (pUI->isSpace())
       {
          if (pAsteroids->bullets.size() < NUMBULLETS)
          {
             pAsteroids->bullets.push_back(Bullet(pAsteroids->ship));
          }
       }
   for (int i = 0; i < pAsteroids->bullets.size(); i++)
   {
      if (pAsteroids->bullets[i].getALife() > 0)
          {
         pAsteroids->bullets[i].check();
         
         pAsteroids->bullets[i].move();
         
         pAsteroids->bullets[i].drawb();
          }
      else
         pAsteroids->bullets.erase(pAsteroids->bullets.begin() + i);
   }
   
   
   
    pAsteroids->ship.check();
   
   if (pUI->isLeft())
      pAsteroids->ship.setAngle(pAsteroids->ship.getAngle() + 10);
   else if (pUI->isRight())
      pAsteroids->ship.setAngle(pAsteroids->ship.getAngle() - 10);
   
   if (pUI->isUp())
   pAsteroids->ship.Acc();
   
   pAsteroids->ship.move();   
   
   if (!pAsteroids->ship.isDead())
      pAsteroids->ship.draw();
   
   if (pAsteroids->getScore() == 30) {
      for(int i = 0; i < pAsteroids->bigRocks.size(); i++)
          {
         
         pAsteroids->bigRocks[i].draw();
         
         pAsteroids->bigRocks[i].move();
         
         pAsteroids->bigRocks[i].check();
          }
   }
   
   
   for(int i = 0; i < pAsteroids->bigRocks.size(); i++)
   {
       
      pAsteroids->bigRocks[i].draw();
   
      pAsteroids->bigRocks[i].move();
   
      pAsteroids->bigRocks[i].check();
   }
   
   for(int i = 0; i < pAsteroids->medRocks.size(); i++)
   {
      
      pAsteroids->medRocks[i].draw();
      
      pAsteroids->medRocks[i].move();
      
      pAsteroids->medRocks[i].check();
   }
   for(int i = 0; i < pAsteroids->smallRocks.size(); i++)
   {
      pAsteroids->smallRocks[i].draw();
      
      pAsteroids->smallRocks[i].move();
      
      pAsteroids->smallRocks[i].check();
       }
}


void Asteroids::strike()
{
   if (!ship.isDead())
   {
      for (int i = 0; i < bullets.size(); i++)
      {
         double distXShip = bullets[i].getPos().getX() - ship.getPos().getX();
         double distYShip = bullets[i].getPos().getY() - ship.getPos().getY();
         double distShip = sqrt(pow(distXShip, 2) + pow(distYShip, 2));
         if (distShip < 2) 
         {
            ship.~Ship();
            bullets.erase(bullets.begin() + i);
         }
      }
      for(int i = 0; i < bigRocks.size(); i++)
      {
         double distXShip = bigRocks[i].getPos().getX() - ship.getPos().getX();
         double distYShip = bigRocks[i].getPos().getY() - ship.getPos().getY();
         double distShip = sqrt(pow(distXShip, 2) + pow(distYShip, 2));
      
         if (distShip < 30)
         {
            ship.~Ship();
            medRocks.push_back(MediumAsteroid(bigRocks[i], 1));
            medRocks.push_back(MediumAsteroid(bigRocks[i], -1));
            smallRocks.push_back(SmallAsteroid(bigRocks[i]));
            bigRocks.erase(bigRocks.begin() + i);
            score++;
         }
         for(int j = 0; j < bullets.size(); j++)
         {
            double distXBullet = bigRocks[i].getPos().getX() - bullets[j].getPos().getX();
            double distYBullet = bigRocks[i].getPos().getY() - bullets[j].getPos().getY();
            double distBullet = sqrt(pow(distXBullet, 2) + pow(distYBullet, 2));
            if (distBullet < 30)
            {
               medRocks.push_back(MediumAsteroid(bigRocks[i], 1));
               medRocks.push_back(MediumAsteroid(bigRocks[i], -1));
               smallRocks.push_back(SmallAsteroid(bigRocks[i]));
               bigRocks.erase(bigRocks.begin() + i);
               bullets.erase(bullets.begin() + j);
               score++;
            }
         }
      }
      for(int i = 0; i < medRocks.size(); i++)
      {
         double distXShip = medRocks[i].getPos().getX() - ship.getPos().getX();
         double distYShip = medRocks[i].getPos().getY() - ship.getPos().getY();
         double distShip = sqrt(pow(distXShip, 2) + pow(distYShip, 2));
         if (distShip < 20)
         {
            ship.~Ship();
            smallRocks.push_back(SmallAsteroid(medRocks[i], 1));
            smallRocks.push_back(SmallAsteroid(medRocks[i], -1));
            medRocks.erase(medRocks.begin() + i);
            score++;
         }
         for(int j = 0; j < bullets.size(); j++)
         {
            double distXBullet = medRocks[i].getPos().getX() - bullets[j].getPos().getX();
            double distYBullet = medRocks[i].getPos().getY() - bullets[j].getPos().getY();
            double distBullet = sqrt(pow(distXBullet, 2) + pow(distYBullet, 2));
            if (distBullet < 20)
            {
               smallRocks.push_back(SmallAsteroid(medRocks[i], 1));
               smallRocks.push_back(SmallAsteroid(medRocks[i], -1));
               medRocks.erase(medRocks.begin() + i);
               bullets.erase(bullets.begin() + 1);
               score++;
            }
         }
      }
   
      for(int i = 0; i < smallRocks.size(); i++)
      {
         double distXShip = smallRocks[i].getPos().getX() - ship.getPos().getX();
         double distYShip = smallRocks[i].getPos().getY() - ship.getPos().getY();
         double distShip = sqrt(pow(distXShip, 2) + pow(distYShip, 2));
         if (distShip < 20)
         {
            ship.~Ship();
            smallRocks.erase(smallRocks.begin() + i);
            score++;
         }
         for(int j = 0; j < bullets.size(); j++)
         {
            double distXBullet = smallRocks[i].getPos().getX() - bullets[j].getPos().getX();
            double distYBullet = smallRocks[i].getPos().getY() - bullets[j].getPos().getY();
            double distBullet = sqrt(pow(distXBullet, 2) + pow(distYBullet, 2));
            if (distBullet < 20)
            {
               smallRocks.erase(smallRocks.begin() + i);
               bullets.erase(bullets.begin() + j);
               score++;
            }
         }
      }
   }
}

/*********************************
 * MAIN
 * initialize the drawing window, initialize
 * the game,and run it!
 *********************************/
int main(int argc, char **argv)
{
      // Start the drawing
   Interface ui(argc, argv, "Asteroids!");
   
      // play the game.  Our function callback will get called periodically
   Asteroids asteroids;
   
   ui.run(callBack, &asteroids);
   
   return 0;
   
}


