//
//  mediumAsteroid.h
//  Prj4
//
//  Created by David Ivie on 3/29/12.
//  Copyright (c) 2012 Brigham Young University. All rights reserved.
//

#ifndef Prj4_mediumAsteroid_h
#define Prj4_mediumAsteroid_h

#include "rock.h"
#include "bigAsteroid.h"

class MediumAsteroid : public Rock
{
public:
   MediumAsteroid(BigAsteroid & oldAsteroid, int change);
   void draw();

};

#endif
