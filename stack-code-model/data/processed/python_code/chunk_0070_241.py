package metaswarm.swarm.patternmaker   {
	import flash.display.*;
	import flash.utils.*;
	import flash.events.*;
	import flash.geom.*;
	import flash.text.*;
	import metaswarm.swarm.patterns.GeoMapper;
	import metaswarm.swarm.patterns.LorenzeMaker;
	import metaswarm.swarm.patterns.TypeMaker;
	import metaswarm.swarm.Swarm;
	import metaswarm.swarm.patterns.GridMaker;
	
	//class needs to be broken up
	
	public class PatternMaker extends Sprite{
		
		private var _swarm:Swarm;
		//var typeMaker:TypeMaker; //don't know why i don't localize to function
		
		public function PatternMaker(swarm:Swarm):void{
			this._swarm = swarm;
			//this.typeMaker = new TypeMaker();
		}
		
		public function make():void
		{
			//property count is hardcoded for now so can't
			//add/remove patterns w/out changing
			for(var j:uint=0; j<_swarm.propCnt; j++){
			  sortBy(j);
			  setUniqueTags(j);
			  grid(0, j);
			  scatter(1, j);
			  browning(2, j);
			  lorenze(3, j);
			  type(4,j);
			  map(5,j);
			}
		}
		
		public function setUniqueTags(tid:uint):void{
			var prevTag:String = new String();
			var curTag:String = new String();
			prevTag = "";
			for(var i:uint=0; i<_swarm.nodeCnt; i++){
				curTag = _swarm.nodes[i].dat[tid];
				if(curTag == prevTag){
					_swarm.nodes[i].tag.uniqArr[tid] = false;
				}else{
					_swarm.nodes[i].tag.uniqArr[tid] = true;
				}
				prevTag = _swarm.nodes[i].dat[tid];
			}
		}
		
		public function type(pid:uint, sid:uint):void
		{
			//trace("PatternMaker->type()");
			
			//generate coordinates
			var typeMaker:TypeMaker = new TypeMaker();
			var points:Array = typeMaker.make("me++", _swarm.nodeCnt, _swarm.w);
		
			//map coordinates to nodes positions
			for(var i:uint=0; i<_swarm.nodeCnt; i++){			
				_swarm.nodes[i].xpos[pid][sid] = points[i][0];
				_swarm.nodes[i].ypos[pid][sid] = points[i][1];
			}
		}
		
		//this is beastly for now
		public function grid(pid:uint, sid:uint):void
		{
			//generate coordinates
			var gridMaker:GridMaker = new GridMaker();
			var points:Array = gridMaker.make(_swarm.nodeCnt, _swarm.w, _swarm.h);
			
			//map coordinates to nodes positions
			for(var i:uint=0; i<_swarm.nodeCnt; i++){			
				_swarm.nodes[i].xpos[pid][sid] = points[i][0];
				_swarm.nodes[i].ypos[pid][sid] = points[i][1];
			}
		}
		
		public function scatter(pid:uint, sid:uint):void
		{
			for(var i:uint=0; i<_swarm.nodeCnt; i++){	
				_swarm.nodes[i].xpos[pid][sid] = Math.random()*_swarm.w;
				_swarm.nodes[i].ypos[pid][sid] = Math.random()*_swarm.h;
    		}
		}
		
		//Lorenze Attractor Pattern-just guessed on random range
		public function lorenze(pid:uint, sid:uint):void
		{
			//generate coordinates
			var lorenzeMaker:LorenzeMaker = new LorenzeMaker();
			var points:Array = lorenzeMaker.make(_swarm.nodeCnt, _swarm.w, _swarm.h);
			
			//map coordinates to nodes positions
			for(var i:uint=0; i<_swarm.nodeCnt; i++){			
				_swarm.nodes[i].xpos[pid][sid] = points[i][0];
				_swarm.nodes[i].ypos[pid][sid] = points[i][1];
			}
		}
		
		/*//genBrowning
		public function browning(pid:uint, sid:uint):void{
			var range:int = 20;
			swarm.nodes[0].xpos[pid][sid] = Math.random()*swarm.w;
			swarm.nodes[0].ypos[pid][sid] = Math.random()*swarm.h;
			for(var i:uint=1; i<swarm.nodeCnt; i++){
				if(swarm.nodes[i].tag.dat[sid] == swarm.nodes[i-1].tag.dat[sid]){
				  	swarm.nodes[i].xpos[pid][sid] = swarm.nodes[i-1].xpos[pid][sid] + (Math.random()-.5)*range;
				  	swarm.nodes[i].ypos[pid][sid] = swarm.nodes[i-1].ypos[pid][sid] + (Math.random()-.5)*range;
				}else{
					swarm.nodes[i].xpos[pid][sid] = Math.random()*swarm.w;
					swarm.nodes[i].ypos[pid][sid] = Math.random()*swarm.h;
				}
			}
		}*/
		
		//genBrowning
		public function browning(pid:uint, sid:uint):void
		{
			var range:int = 25;
			_swarm.nodes[0].xpos[pid][sid] = _swarm.w/2;
			_swarm.nodes[0].ypos[pid][sid] = _swarm.h/2;
			for(var i:uint=1; i<_swarm.nodeCnt; i++){
				_swarm.nodes[i].xpos[pid][sid] = _swarm.nodes[i-1].xpos[pid][sid] + (Math.random()-.5)*range;
				_swarm.nodes[i].ypos[pid][sid] = _swarm.nodes[i-1].ypos[pid][sid] + (Math.random()-.5)*range;
			}
		}
		
		//genBrowning
		public function map(pid:uint, sid:uint):void
		{
			var geoMapper:GeoMapper = new GeoMapper();
			
			//var coordinates:Array = new Array();
			var latIndex:Number = 6;
			var longIndex:Number = 5;
			
			//for each node
			for(var i:uint=1; i<_swarm.nodeCnt; i++){
				var geoPoint:Array = [_swarm.nodes[i].dat[longIndex], _swarm.nodes[i].dat[latIndex]];
				//coordinates.push(geoPoint);
				
				//convert node.dat to screen coordinates
				var point:Array = geoMapper.geoToScreen(geoPoint, _swarm.h/2);
				
				//assign to node pos
				_swarm.nodes[i].xpos[pid][sid] = point[0];
				_swarm.nodes[i].ypos[pid][sid] = point[1];
			}
		}
		
		//bubble sort. put in util class later
		public function sortBy(tid:uint):void
		{
			var a:Node = new Node();
			var b:Node = new Node();
			for(var i:uint=0; i<_swarm.nodeCnt; i++){
				for(var j:uint=0; j<_swarm.nodeCnt; j++){
					//assign neighbooring Nodes to tmp nodes
					a = _swarm.nodes[i];
          			b = _swarm.nodes[j];
					//if two strings not alphabetized then swap them
          			if(a.tag.dat[tid] > b.tag.dat[tid]){
						//swap
						//trace("swap: " + a.tag.dat[sid] + " with " + b.tag.dat[sid]);
						_swarm.nodes[i] = b;
						_swarm.nodes[j] = a;
					}
				}
			} 
		}
		
	}//end class
}//end pkg