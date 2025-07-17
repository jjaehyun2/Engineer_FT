package circuits
{
	public class Connector extends DigitalComponent
	{
		private var _powered:Boolean = false;
		private var _previouslyPowered:Boolean = true;
		
		public function Connector()
		{
			
		}
		
		public function get powered():Boolean
		{
			return _powered;
		}
		
		public function get edge():int
		{
			var Edge:int = 0;
			if (_powered && !_previouslyPowered)
				Edge = 1;
			else if (!_powered && _previouslyPowered)
				Edge = -1;
			
			return Edge;
		}
		
		public function get open():Boolean
		{
			return false;
		}
		
		public function reset():void
		{
			// TODO: BUGFIX
			// Since this is called every tick, it is causing all Connectors to "flicker", constantly being in either
			// a rising edge or falling edge state. This has no visual effect, since it happens every frame, but can
			// be a drag on performance and is also logically incorrect.
			_powered = false;
			_previouslyPowered = true;
		}
		
		public function connect(ConnectorToConnect:Connector):void
		{
			
		}
		
		public function tick():void
		{
			_previouslyPowered = _powered;
		}
		
		public function propagate(Powered:Boolean, Propagator:DigitalComponent):DigitalComponent
		{
			_previouslyPowered = _powered;
			_powered = Powered;
			
			return null;
		}
	}
}