/*
 * FLINT PARTICLE SYSTEM
 * .....................
 * 
 * Author: Richard Lord
 * Copyright (c) Richard Lord 2008-2011
 * http://flintparticles.org
 * 
 * 
 * Licence Agreement
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

package org.flintparticles.common.actions 
{
	import org.flintparticles.common.emitters.Emitter;
	import org.flintparticles.common.particles.Particle;	

	/**
	 * The ChangeCollisionRadius action adjusts the collision radius of the particle as it ages.
	 * It uses the particle's energy level to decide what radius the particle
	 * should have.
	 * 
	 * <p>Usually a particle's energy changes from 1 to 0 over its lifetime, but
	 * this can be altered via the easing function set within the age action.</p>
	 * 
	 * <p>This action should be used in conjunction with the Age action.</p>
	 * 
	 * @see org.flintparticles.common.actions.Action
	 * @see org.flintparticles.common.actions.Age
	 */

	public class ChangeCollisionRadius extends ActionBase
	{
		private var _diffRadius:Number;
		private var _endRadius:Number;
		
		/**
		 * The constructor creates a ChangeCollisionRadius action for use by an emitter. 
		 * To add a Radius to all particles created by an emitter, use the
		 * emitter's addAction method.
		 * 
		 * @see org.flintparticles.common.emitters.Emitter#addAction()
		 * 
		 * @param startRadius The collision radius for the particle when its energy
		 * is 1 - usually at the start of its lifetime.
		 * @param endRadius The collision radius for the particle when its energy
		 * is 0 - usually at the end of its lifetime.
		 */
		public function ChangeCollisionRadius( startRadius:Number = 1, endRadius:Number = 1 )
		{
			_diffRadius = startRadius - endRadius;
			_endRadius = endRadius;
		}
		
		/**
		 * The collision radius for the particle when its energy
		 * is 1 - usually at the start of its lifetime.
		 */
		public function get startRadius():Number
		{
			return _endRadius + _diffRadius;
		}
		public function set startRadius( value:Number ):void
		{
			_diffRadius = value - _endRadius;
		}
		
		/**
		 * The collision radius for the particle when its energy
		 * is 0 - usually at the end of its lifetime.
		 */
		public function get endRadius():Number
		{
			return _endRadius;
		}
		public function set endRadius( value:Number ):void
		{
			_diffRadius = _endRadius + _diffRadius - value;
			_endRadius = value;
		}
		
		/**
		 * Sets the collision radius of the particle based on the values defined
		 * and the particle's energy level.
		 * 
		 * <p>This method is called by the emitter and need not be called by the 
		 * user</p>
		 * 
		 * @param emitter The Emitter that created the particle.
		 * @param particle The particle to be updated.
		 * @param time The duration of the frame - used for time based updates.
		 * 
		 * @see org.flintparticles.common.actions.Action#update()
		 */
		override public function update( emitter:Emitter, particle:Particle, time:Number ):void
		{
			particle.collisionRadius = _endRadius + _diffRadius * particle.energy;
		}
	}
}