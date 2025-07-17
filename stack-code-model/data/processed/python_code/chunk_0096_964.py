package metaswarm.swarm.swarmstates {
	import metaswarm.swarm.Swarm;
	import metaswarm.swarm.SwarmState;
	
	public class BrowningState implements SwarmState{
		
		private static const BROWNING:Number = 2;
		
		private var swarm:Swarm;
		
		public function BrowningState(swarm:Swarm)
		{
			//trace("construct GridState");
			this.swarm = swarm;
			init();
		}	
		public function init():void{
			//genPattern();
		}
		public function incrState():void{
			//trace("ScatterState setPattern");
			swarm.swarmState = swarm.lorenze;
			swarm.setPattern();
		}
		public function decrState():void{
			//trace("ScatterState setPattern");
			swarm.swarmState = swarm.scatter;
			swarm.setPattern();
		}
		//make this private
		public function setPattern():void{
			//trace("GridState setPattern");
			for(var i:uint=0; i<swarm.nodeCnt; i++){
				swarm.nodes[i].setTarget(BROWNING, swarm.sortOrder);
			}
		}
		
	}//end class
}//end pkg