package metaswarm.swarm    {
	import flash.display.DisplayObject;
	import flash.display.Sprite;
	import flash.display.Graphics;
    import flash.display.Shape;
    import metaswarm.swarm.swarmstates.BrowningState;
    import metaswarm.swarm.swarmstates.GridState;
    import metaswarm.swarm.swarmstates.LorenzeState;
    import metaswarm.swarm.swarmstates.ScatterState;
    import metaswarm.swarm.swarmstates.TypeState;
    import metaswarm.swarm.swarmstates.MapState;
    import metaswarm.subset.Subset;
	
	public class Swarm extends Sprite{
		
		//omit constants for now
		
		//Except for TextField and Video objects, 
		//a display object with no content has a 
		//width of 0, even if you try to set width 
		//to a different value, so need these
		public var w:int;
		public var h:int;
		
		//internal composite objects
		public var nodes:Array;
		public var nodeCnt:uint;
		public var propCnt:uint;
		public var sortOrder:uint;
		
		//internal states
		public var lorenze:SwarmState;
		public var browning:SwarmState;
		public var scatter:SwarmState;
		public var grid:SwarmState;
		public var type:SwarmState;
		public var map:SwarmState;
		
		//internal state holder
		public var swarmState:SwarmState;
		
		//var swarmLoader:SwarmLoader;
		//var patternMaker:PatternMaker;
		
		//constructor:	
		public function Swarm(){
			
			//instantiate composite objs
			nodes = new Array();
			
			lorenze = new LorenzeState(this);
			browning = new BrowningState(this);
			scatter = new ScatterState(this);
			grid = new GridState(this);
			type = new TypeState(this);
			map = new MapState(this);
			
			init();
		}
		private function init():void{
			//set intial state and show unique 
			//tags for that state
			swarmState = grid;
			sortOrder = 2;
			showUniqueTags();
		}
		
		
		//these need to be changed
		public function preview():void {
			var dropped:Subset = new Subset();
			//var undropped:Subset = new Subset();
			for(var i:uint=0; i<nodeCnt; i++){
				if(nodes[i].isDropped() || nodes[i].isPopped()){
					dropped.nodes.push(nodes[i]);
				}else{
					//undropped.push(nodes[i]);
					nodes[i].visible = false;
				}
			}
			dropped.tile();
			//undropped.disable();
		}
		
		public function explore():void {
			var dropped:Subset = new Subset();
			//var undropped:Subset = new Subset();
			for(var i:uint=0; i<nodeCnt; i++){
				if(nodes[i].isDropped() || nodes[i].isPopped()){
					dropped.nodes.push(nodes[i]);
				}else{
					//undropped.push(nodes[i]);
					nodes[i].visible = true;
				}
			}
			dropped.restore();
			//undropped.disable();
		}
		
		//methods
		public function select(node:Node):void {
			clearSelection();
			node.select();
		}
		public function add(node:Node):void {
			node.select();
		}
		public function remove(node:Node):void {
			node.deSelect();
		}
		public function toggleSelect(node:Node):void {
			node.toggleSelect();
		}
		public function clearSelection():void {
			for(var i:uint=0; i<nodeCnt; i++){
				nodes[i].deSelect();
			}
		}
		public function selectBy(t:String):void {
			clearSelection();
			for(var i:uint=0; i<nodeCnt; i++){
				if(nodes[i].tag.t.text == t){
					nodes[i].select();
				}
			}
		}
		public function addBy(t:String):void {
			for(var i:uint=0; i<nodeCnt; i++){
				if(nodes[i].tag.t.text == t){
					nodes[i].select();
				}
			}
		}
		public function filterBy(t:String):void {
			for(var i:uint=0; i<nodeCnt; i++){
				if(nodes[i].tag.t.text != t){
					//trace("deSelect");
					nodes[i].deSelect();
				}
			}
		}
		public function popin(node:Node):void{
			node.popin();
		}
		public function popout(node:Node):void{
			node.popout();
		}
		
		public function close(node:Node):void{
			node.close();
		}
		
		public function drag(node:Node):void{
			node.drag();
		}
		
		public function drop(node:Node):void{
			node.drop();
		}
		public function dropSelected():void{
			for(var i:uint=0; i<nodeCnt; i++){
				if(nodes[i].isPicked()){
					nodes[i].drop();
				}
			}
		}
		public function startHover(node:Node):void{
			node.startHover();
		}
		
		public function stopHover(node:Node):void{
			//trace("swarm.stopHover");
			node.stopHover();
		}
		
		public function startFocusBy(t:String):void {
			for(var i:uint=0; i<nodeCnt; i++){
				if(nodes[i].tag.t.text == t){
					nodes[i].startFocus();
				}
			}
		}
		
		public function startSelectByFocus(t:String):void {
			for(var i:uint=0; i<nodeCnt; i++){
				if(nodes[i].tag.t.text == t){
					nodes[i].startFocus();
				}
			}
		}
		
		public function startFilterByFocus(t:String):void {
			for(var i:uint=0; i<nodeCnt; i++){
				if(nodes[i].tag.t.text == t && nodes[i].isPicked()){
					nodes[i].startFocus();
				}
			}
		}
		
		public function stopFocusBy():void {
			for(var i:uint=0; i<nodeCnt; i++){
				nodes[i].stopFocus();
			}
		}
		
		public function printOutNodes():void{
			trace("printOutCoordinates: *****************************************************");
			for(var i:uint=0; i<nodeCnt; i++){
				trace("node " + i + ": ");
				for(var j:uint=0; j<propCnt; j++){
					trace("xpos,ypos " + j + ": " + nodes[i].xpos[0][j] + ", " + nodes[i].ypos[0][j]);
				}
			}
		}
		
		public function rePosition():void{
			//trace("swarm rePosition");
			for(var i:uint=0; i<nodeCnt; i++){
				nodes[i].rePosition();
			}
		}
		
		public function reSize():void{
			//trace("swarm reSize");
			for(var i:uint=0; i<nodeCnt; i++){
				nodes[i].reSize();
			}
		}
		
		public function incrSort():void{
			//trace("incrSort");
			if(sortOrder < propCnt-1){
				sortOrder++;
			}else{
				sortOrder = 0;
			}
			for(var i:uint=0; i<nodeCnt; i++){
				//swarm.nodes[i].tag.setTxt(1);
				nodes[i].tag.incr();
			}
			setPattern();
			showUniqueTags();
		}
		public function decrSort():void{
			//trace("decrSort");
			if(sortOrder > 0){
				sortOrder--;
			}else{
				sortOrder = propCnt-1;
			}
			for(var i:uint=0; i<nodeCnt; i++){
				//swarm.nodes[i].tag.setTxt(1);
				nodes[i].tag.decr();
			}
			setPattern();
			showUniqueTags();
		}
		
		
		public function showUniqueTags():void{
			for(var i:uint=0; i<nodeCnt; i++){
				nodes[i].tag.visible = nodes[i].tag.isUniq;
			}
		}
		
		
		//delegated tasks*********************************************
		public function incrState():void{
			//trace("delegate incrState");
			swarmState.incrState();
		}
		public function decrState():void{
			//trace("delegate decrState");
			swarmState.decrState();
		}
		public function setPattern():void{
			//trace("delegate swarm switch");
			swarmState.setPattern();
		}
		
	}//end swarm
}//end pkg