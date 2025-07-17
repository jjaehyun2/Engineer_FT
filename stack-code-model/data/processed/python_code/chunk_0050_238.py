package com.arxterra.vo
{
	import com.smartfoxserver.v2.entities.data.ISFSObject;
	import com.smartfoxserver.v2.entities.data.SFSObject;
	
	import com.arxterra.interfaces.IPilotMessageSerialize;
	
	/**
	 * Used with ping message to transfer timestamp and lag values from control panel to robot,
	 * and with pong message to return values from robot to control panel.
	 */		
	public class Ping implements IPilotMessageSerialize
	{
		public var controlLagSfs:int;
		public var controlTimeStamp:Number;
		public var intervalMsecs:int;
		public var robotLagSfs:int;
		public var robotTimeStamp:Number;
		
		/**
		 * @param intervalMsecs
		 * @param controlTimeStamp
		 * @param controlLagSfs
		 * @param robotTimeStamp
		 * @param robotLagSfs
		 */		
		public function Ping (
			intervalMsecs:int = 2000,
			controlTimeStamp:Number = 0,
			controlLagSfs:int = 0,
			robotTimeStamp:Number = 0,
			robotLagSfs:int = 0
		)
		{
			this.intervalMsecs = intervalMsecs;
			this.controlTimeStamp = controlTimeStamp;
			this.controlLagSfs = controlLagSfs;
			this.robotTimeStamp = robotTimeStamp;
			this.robotLagSfs = robotLagSfs;
		}
		
		public function toSFSObject ( ) : ISFSObject
		{
			var sfso:ISFSObject = new SFSObject ( );
			
			sfso.putInt ( 'i', intervalMsecs );
			sfso.putDouble ( 'c', controlTimeStamp );
			sfso.putInt ( 'd', controlLagSfs );
			sfso.putDouble ( 'r', robotTimeStamp );
			sfso.putInt ( 's', robotLagSfs );
			return sfso;
		}
		
		public static function newFromSFSObject ( sfso:ISFSObject ) : Ping
		{
			return new Ping (
				sfso.getInt ( 'i' ),
				sfso.getDouble ( 'c' ),
				sfso.getInt ( 'd' ),
				sfso.getDouble ( 'r' ),
				sfso.getInt ( 's' )
			);
		}
	}
}