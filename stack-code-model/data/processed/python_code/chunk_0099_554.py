/*
 * @author Ryan C. Knaggs
 * @date 04/30/2007
 * @description: To dispatch data thru
 * a specific channel from one class to \
 * other classes
 */


package eventexchange {
 
	public class EventDispatch {
		
		
		private var chn:Object;	// Global properties
		private static var RESERVED_COMMAND_SLOT:Number = 0;
		
		/*
		 * Constructor
		 * Known by inheritance of the class extends
		 */
		 
		public function EventDispatch(chn:Object) {
			this.chn = chn;
		}
		
		
		
		
		/**
		* Dispatch data thru a specific channel
		* @param	e:Object - Object wrapper containing all data
		* @param	c:Number - Which channel to send data thru
		*/
		
		public function dispatch(e:Object,c:Number):void {
			
			
			if(chn.ch[c] == undefined) {
				chn.ch[c] = new EventFactory();
				chn.ch[c]._name = "Slot"+c;
			}
			
			chn.ch[c].notifyObserver(e);
		}
		
		
		public function sendEvent(commandName:String,arg:Object):void {
			var e:Object = {commandName:commandName,arg:arg};
			chn.ch[RESERVED_COMMAND_SLOT].notifyObserver(e);
		}
		
	}
	
}