﻿/*
* Copyright (c) 2006-2007 Erin Catto http://www.gphysics.com
*
* This software is provided 'as-is', without any express or implied
* warranty.  In no event will the authors be held liable for any damages
* arising from the use of this software.
* Permission is granted to anyone to use this software for any purpose,
* including commercial applications, and to alter it and redistribute it
* freely, subject to the following restrictions:
* 1. The origin of this software must not be misrepresented; you must not
* claim that you wrote the original software. If you use this software
* in a product, an acknowledgment in the product documentation would be
* appreciated but is not required.
* 2. Altered source versions must be plainly marked as such, and must not be
* misrepresented as being the original software.
* 3. This notice may not be removed or altered from any source distribution.
*/

package Box2D.Dynamics{


import Box2D.Collision.*;
import Box2D.Collision.Shapes.*;
import Box2D.Dynamics.Contacts.*;
import Box2D.Dynamics.*;
import Box2D.Common.Math.*;
import Box2D.Common.*;

import Box2D.Common.b2internal;
use namespace b2internal;


/**
 * Implement this class to get contact information. You can use these results for
 * things like sounds and game logic. You can also get contact results by
 * traversing the contact lists after the time step. However, you might miss
 * some contacts because continuous physics leads to sub-stepping.
 * Additionally you may receive multiple callbacks for the same contact in a
 * single time step.
 * You should strive to make your callbacks efficient because there may be
 * many callbacks per time step.
 * @warning You cannot create/destroy Box2D entities inside these callbacks.
 */
public class b2ContactListener
{
	/**
	 * Called when two fixtures begin to touch.
	 */
	public virtual function BeginContact(contact:b2Contact):void { }

	/**
	 * Called when two fixtures cease to touch.
	 */
	public virtual function EndContact(contact:b2Contact):void { }

	/**
	 * This is called after a contact is updated. This allows you to inspect a
	 * contact before it goes to the solver. If you are careful, you can modify the
	 * contact manifold (e.g. disable contact).
	 * A copy of the old manifold is provided so that you can detect changes.
	 * Note: this is called only for awake bodies.
	 * Note: this is called even when the number of contact points is zero.
	 * Note: this is not called for sensors.
	 * Note: if you set the number of contact points to zero, you will not
	 * get an EndContact callback. However, you may get a BeginContact callback
	 * the next step.
	 */
	public virtual function PreSolve(contact:b2Contact, oldManifold:b2Manifold):void {}

	/**
	 * This lets you inspect a contact after the solver is finished. This is useful
	 * for inspecting impulses.
	 * Note: the contact manifold does not include time of impact impulses, which can be
	 * arbitrarily large if the sub-step is small. Hence the impulse is provided explicitly
	 * in a separate data structure.
	 * Note: this is only called for contacts that are touching, solid, and awake.
	 */
	public virtual function PostSolve(contact:b2Contact, impulse:b2ContactImpulse):void { }
	
	b2internal static var b2_defaultListener:b2ContactListener = new b2ContactListener();
};

}