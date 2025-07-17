package metaswarm.node.nodestates   {
	import metaswarm.node.NodeState;
	
	public class ThumbDraggingState implements NodeState{
		
		private var node:Node;
		
		function ThumbDraggingState(node:Node)
		{
			//trace("construct DraggingState");
			this.node = node;
		}
		public function select():void{}
		
		public function deSelect():void{}
		
		public function toggleSelect():void{}
		
		public function drag():void{}
		
		public function drop():void{
			//trace("PickedState drag: goto dragging state");
			//node.icon.visible = false;
			
			//node.icon.stopDrag();
			node.thumb.stopDrag();
			
			//node.thumb.x = node.icon.x;
			//node.thumb.y = node.icon.y;
			node.thumb.setTarget(node.thumb.x, node.thumb.y);
			//node.thumb.visible = true;
			
			//goto dropped state
			node.nodeState = node.prevState;
		}
		
		//public function dropThumb():void{}
		
		public function popout():void{}
		
		public function popin():void{}
		
		public function close():void{}
		
		public function setTarget(tgx:Number,
						   		  tgy:Number):void{
			//trace("DraggingState switch");
			//node.dot.setTarget(tgx, tgy);
		}
		
		public function rePosition():void{
			//trace("DraggingState rePosition");
			//node.dot.goToTarget();
			//node.thumb.x = node.icon.x;
			//node.thumb.y = node.icon.y;
			
			//dragging icon so snap dot to icon
			/*node.dot.x = node.dataBox.x;
			node.dot.y = node.dataBox.y;*/
			
			//snap data box to thumb while dragging
			node.dataBox.x = node.thumb.x + 125;
			node.dataBox.y = node.thumb.y;
		}
		
		public function reSize():void{
			//trace("DraggingState reSize");
			node.icon.scaleToTarget(); //???
		}
		
		public function startFocus():void{}
		
		public function stopFocus():void{}
		
		public function startHover():void{}
		
		public function stopHover():void{}
	}
}