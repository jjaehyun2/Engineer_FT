package metaswarm.swarm.swarmstates   {
	import metaswarm.swarm.Swarm;
	import metaswarm.swarm.SwarmState;
	
	public class MapState implements SwarmState{
		
		private static const MAP:Number = 5;
		
		private var _swarm:Swarm;
		
		public function MapState(swarm:Swarm)
		{
			//trace("construct ScatterState");
			this._swarm = swarm;
			init();
		}
		public function init():void{
			//do nothing
		}
		public function incrState():void{
			//trace("ScatterState setPattern");
			_swarm.swarmState = _swarm.grid;
			_swarm.setPattern();
		}
		public function decrState():void{
			//trace("ScatterState setPattern");
			_swarm.swarmState = _swarm.type;
			_swarm.setPattern();
		}
		public function setPattern():void{
			//trace("ScatterState setPattern");
			for(var i:uint=0; i<_swarm.nodeCnt; i++){
				_swarm.nodes[i].setTarget(MAP, _swarm.sortOrder);
			}
		}
		
	}//end class
}//end pkg