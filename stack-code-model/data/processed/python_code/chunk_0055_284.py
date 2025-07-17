package {
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.utils.ByteArray;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	public class Main extends Sprite {
		
		public function Main():void {
			if (stage)
				init();
			else
				addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			// entry point
			
			var bytes:ByteArray = new ByteArray();
			bytes.writeUnsignedInt(5);
			bytes.writeUnsignedInt(4);
			bytes.position = 0;
			//bytes.writeUnsignedInt(5)
			//var value:uint = 5;
			// manual writing (big-endian)
			//bytes[0] = (value & 0xFF000000) >> 24;
			//bytes[1] = (value & 0x00FF0000) >> 16;
			//bytes[2] = (value & 0x0000FF00) >> 8;
			//bytes[3] = value & 0xFF;
			
			//var finalValue:uint = bytes[0] << 24 | bytes[1] << 16 | bytes[2] << 8 | bytes[3];
			// outputs : 5
			//var toTrace:
			//var finalValue:uint = bytes.readUnsignedInt();
			trace(bytes.readUTF());
		}
	
	}

}