package net.psykosoft.psykopaint2.core.managers.pen
{

	import net.psykosoft.wacom.WacomExtension;
	import net.psykosoft.wacom.events.WacomExtensionEvent;

	public class WacomPenManager
	{
		
		
		public function WacomPenManager()
		{
		}
		
		private static var wacomPen : WacomExtension;
		private static var _pressure : int = -1;
		private static var _hasPen:Boolean = false;
		private static var _buttonState:int = 0;
		private static var _batteryLevel:int = -1;
		
		public static function get currentPressure():int
		{
			return _pressure;
		}
		
		public static function get hasPen():Boolean
		{
			return _hasPen;
		}
		
		public static function get buttonState():int
		{
			return _buttonState;
		}
		
		public static function initializePen():void
		{
			wacomPen.initialize();
		}

		[PostConstruct]
		public function init() : void
		{
			
		wacomPen = new WacomExtension();
			wacomPen.addEventListener( WacomExtensionEvent.DEVICE_DISCOVERED, onDeviceDiscovered );
			wacomPen.addEventListener( WacomExtensionEvent.BATTERY_LEVEL_CHANGED, onBatteryLevelChanged );
			wacomPen.addEventListener( WacomExtensionEvent.BUTTON_1_PRESSED, onButton1Pressed );
			wacomPen.addEventListener( WacomExtensionEvent.BUTTON_2_PRESSED, onButton2Pressed );
			wacomPen.addEventListener( WacomExtensionEvent.BUTTON_1_RELEASED, onButton1Released );
			wacomPen.addEventListener( WacomExtensionEvent.BUTTON_2_RELEASED, onButton2Released );
			wacomPen.addEventListener( WacomExtensionEvent.PRESSURE_CHANGED, onPressureChanged );
			
		}
		
		

		private function onBatteryLevelChanged( event:WacomExtensionEvent ):void {
			trace( "Pen battery level changed: " + event.data );
			_batteryLevel = event.data;
		}
		
		private function onButton1Pressed( event:WacomExtensionEvent ):void {
			trace( "Button 1 pressed." );
			//PsykoSocket.sendString("<msg src='Pen.onButton1Pressed'/>");
			_hasPen = true;
			_buttonState |= 1;
		}
		
		private function onButton2Pressed( event:WacomExtensionEvent ):void {
			trace( "Button 2 pressed." );
			//PsykoSocket.sendString("<msg src='Pen.onButton2Pressed'/>");
			_hasPen = true;
			_buttonState |= 2;
		}
		
		private function onButton1Released( event:WacomExtensionEvent ):void {
			trace( "Button 1 released." );
			//PsykoSocket.sendString("<msg src='Pen.onButton1Released'/>");
			_hasPen = true;
			_buttonState &= 2;
		}
		
		private function onButton2Released( event:WacomExtensionEvent ):void {
			trace( "Button 2 released." );
			//PsykoSocket.sendString("<msg src='Pen.onButton2Released'/>");
			_hasPen = true;
			_buttonState &= 1;
		}
		
		private function onPressureChanged( event:WacomExtensionEvent ):void {
			trace( "Pen pressure changed: " + event.data );
			_pressure = event.data;
			_hasPen = true;
			//PsykoSocket.sendString("<msg src='Pen.onPressureChanged' pressure='"+_pressure+"'/>");
		}
		
		private function onDeviceDiscovered( event:WacomExtensionEvent ):void {
			trace( "Device discovered.");
			//PsykoSocket.sendString("<msg src='Pen.onDeviceDiscovered'/>");
			_hasPen = true;
		}
	}
}