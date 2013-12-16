//
//  smallAsteroid.h
//  Prj4
//
//  Created by David Ivie on 3/29/12.
//  Copyright (c) 2012 Brigham Young University. All rights reserved.
//

#ifndef Prj4_smallAsteroid_h
#define Prj4_smallAsteroid_h

#include "rock.h"
#include "bigAsteroid.h"
#include "mediumAsteroid.h"

class SmallAsteroid : public Rock
{
public:
   SmallAsteroid(BigAsteroid & oldAsteroid);
   SmallAsteroid(MediumAsteroid & oldAsteroid, int change);
   void draw();
};

#endif

