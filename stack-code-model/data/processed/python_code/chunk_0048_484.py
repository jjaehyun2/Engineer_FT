package robotlegs.bender.extensions.starlingViewMap.impl
{
	import org.osflash.signals.ISignal;
	import robotlegs.bender.extensions.starlingViewMap.impl.core.ISignalMap;

	public class SignalMediator extends StarlingMediator
	{

		protected var _signalMap:ISignalMap;
	
		public function SignalMediator()
		{
			super();
		}
	
		override public function destroy():void
		{
			signalMap.removeAll();
			super.destroy();
		}
	
		protected function get signalMap():ISignalMap
		{
			return _signalMap ||= new SignalMap();
		}
	
		protected function addToSignal(signal:ISignal, handler:Function):void
		{
			signalMap.addToSignal(signal, handler);
		} 
		
		protected function addOnceToSignal(signal:ISignal, handler:Function):void
		{
			signalMap.addOnceToSignal(signal, handler);
		}
	
	}           

}