/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2015 Andrew Salomatin (MerlinDS)
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

package systems
{

	import components.Destination;
	import components.Position;
	import components.Velocity;

	import org.gimmick.collections.IEntities;
	import org.gimmick.core.Gimmick;
	import org.gimmick.core.IEntity;
	import org.gimmick.core.IEntitySystem;

	/**
	 * System than move entities in application
	 */
	public class MovementSystem implements IEntitySystem
	{
		public var _entities:IEntities;
		//======================================================================================================================
//{region											PUBLIC METHODS
		public function MovementSystem()
		{
		}

		public function tick(time:Number):void
		{
			if(time > 60)return;//too big time
			for(_entities.begin(); !_entities.end(); _entities.next())
			{
				var entity:IEntity = _entities.current;
				var velocity:Velocity = entity.get(Velocity);
				var position:Position = entity.get(Position);
				var destivation:Destination = entity.get(Destination);
				var x:Number = destivation.x - position.x;
				var y:Number = destivation.y - position.y;
				//
				if(Math.abs(x) < 10 && Math.abs(y) < 10)
				{
					//set new destination
					destivation.x = Math.round( 1024 * Math.random() );
					destivation.y = Math.round( 768 * Math.random() );
					//set new velocity
					velocity.x = (destivation.x - position.x) / 5000;
					velocity.y = (destivation.y - position.y) / 5000;
				}
				//go to destination
				position.x += velocity.x * time;
				position.y += velocity.y * time;
			}
		}

		public function initialize():void
		{
			//initialize entities collection for future iterations
			_entities = Gimmick.getEntities(Position, Velocity, Destination);
		}

		public function dispose():void
		{
			//dispose collectop and remove link for it
			_entities.dispose();
			_entities = null;
		}

		public function activate():void
		{
		}

		public function deactivate():void
		{
		}

//} endregion PUBLIC METHODS ===========================================================================================
//======================================================================================================================
//{region										PRIVATE\PROTECTED METHODS

//} endregion PRIVATE\PROTECTED METHODS ================================================================================
//======================================================================================================================
//{region											GETTERS/SETTERS

//} endregion GETTERS/SETTERS ==========================================================================================
	}
}