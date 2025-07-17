package com.arxterra.vo
{
	public class MotorStates
	{
		// CONSTANTS
		
		/**
		 * Motor state FORWARD
		 */
		public static const FORWARD:uint = 1;
		/**
		 * Motor state BACKWARD
		 */
		public static const BACKWARD:uint = 2;
		/**
		 * Motor state BRAKE (not yet supported, use RELEASE instead)
		 */
		public static const BRAKE:uint = 3;
		/**
		 * Motor state RELEASE
		 */
		public static const RELEASE:uint = 4;
		
		private static const __STATES:Array = [ FORWARD, BACKWARD, RELEASE ]; // BRAKE not yet supported
		
		// PUBLIC METHODS
		
		public function MotorStates()
		{
		}
		
		public static function ValidateState ( value:uint ) : uint
		{
			if ( __STATES.indexOf ( value ) < 0 )
				return RELEASE;
			return value;
		}
	}
}