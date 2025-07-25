/*
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

package Box2D.Collision 
{

	import Box2D.Common.Math.b2Sweep;
	
	/**
	 * Inpute parameters for b2TimeOfImpact
	 */
	public class b2TOIInput 
	{
		public var proxyA:b2DistanceProxy = new b2DistanceProxy();
		public var proxyB:b2DistanceProxy = new b2DistanceProxy();
		public var sweepA:b2Sweep = new b2Sweep();
		public var sweepB:b2Sweep = new b2Sweep();
		public var tolerance:Number;
		
	}
	
}