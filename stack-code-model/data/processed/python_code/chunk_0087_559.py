package com.arxterra.vo
{
	public class AccData
	{
		public var accelerationX:Number;
		public var accelerationY:Number;
		public var accelerationZ:Number;
		
		public function AccData (
			accelerationX:Number = 0,
			accelerationY:Number = 0,
			accelerationZ:Number = 0
		) 
		{
			this.accelerationX = accelerationX;
			this.accelerationY = accelerationY;
			this.accelerationZ = accelerationZ;
		}
	}
}