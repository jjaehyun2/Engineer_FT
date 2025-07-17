package metaswarm.node.nodestates   {
	import flash.geom.ColorTransform;
	import metaswarm.node.NodeState;
	
	public class IdleState implements NodeState{
		
		private var redTransform:ColorTransform;
		private var blkTransform:ColorTransform;
		
		private var node:Node;
		
		function IdleState(node:Node)
		{
			//trace("construct IdleState");
			this.node = node;
			
			redTransform = new ColorTransform( );
			redTransform.color = 0xFF0000;
			blkTransform = new ColorTransform( );
			blkTransform.color = 0xCCCCCC;
		}
		public function select():void{
			//trace("IdleState select:goto picked state");
			
			//node.dot.mouseEnabled = false;
			//stopFocus();
			
			node.dot.visible = false;
			
			//position icon at dot and make visible
			node.icon.x = node.dot.x;
			node.icon.y = node.dot.y;
			node.icon.setTargetWidth(6);
			node.icon.setTarget(node.dot.x, node.dot.y);
			node.icon.visible = true;
			
			//position tag at dot and make visible
			node.tag.x = node.dot.x;
			node.tag.y = node.dot.y;
			//node.tag.visible = true;
			
			//goto picked state
			node.nodeState = node.picked;
		}
		
		public function deSelect():void{}
		
		public function toggleSelect():void{
			select();
		}
		
		//public function filter():void{}
		
		public function drag():void{}
		
		public function drop():void{}
		
		//public function dropThumb():void{}
		
		public function popout():void{}
		
		public function popin():void{}
		
		public function close():void{}
		
		public function setTarget(tgx:Number,
						   		  tgy:Number):void{
			//trace("IdleState setTarget: " + tgx + ", " + tgy);
			node.dot.setTarget(tgx, tgy);
		}
		
		public function rePosition():void{
			//trace("IdleState rePosition");
			node.dot.goToTarget();
			
			node.tag.x = node.dot.x;
			node.tag.y = node.dot.y;
		}
		
		public function reSize():void{}
		
		public function startFocus():void{
			//trace("startFocus");
			//node.dot.transform.colorTransform = redTransform;
			
			/*private function doDrawCircle():void {
            var bounds:Shape = new Shape();
			var r:Rectangle = getRect(node.dot);
            //bounds.graphics.beginFill(bgColor);
			bounds.graphics.lineStyle(0, 0xFF3333); //red
			bounds.graphics.drawRect(r.x, r.y, r.width, r.height);
			//bounds.graphics.endFill();
			node.addChild(bounds);
        	}*/
			
			node.dot.dotButton.forceOver();
			node.tag.t.borderColor = 0xFF0000;
		
			node.tag.x = node.dot.x;
			node.tag.y = node.dot.y;
			//node.tag.visible = true;
		}
		public function stopFocus():void{
			//trace("stopFocus");
			//node.dot.transform.colorTransform = blkTransform;
			//node.tag.visible = false;
			
			node.dot.dotButton.restoreOver();
			node.tag.t.borderColor = 0xCCCCCC;
		}
		
		public function startHover():void{}
		
		public function stopHover():void{}
		
	}
}