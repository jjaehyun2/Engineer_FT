package org.openPyro.containers
{
	import flash.display.DisplayObject;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.utils.getQualifiedClassName;
	
	import org.openPyro.core.ClassFactory;
	import org.openPyro.core.MeasurableControl;
	import org.openPyro.core.UIControl;
	import org.openPyro.layout.ILayout;
	import org.openPyro.layout.VLayout;
	import org.openPyro.managers.events.DragEvent;
	import org.openPyro.painters.GradientFillPainter;
	
	/**
	 * 
	 */ 
	public class VDividedBox extends DividedBox
	{
		/**
		 * Constructor
		 */ 
		public function VDividedBox(){
			super();
			_styleName = "VDividedBox";
		}
		
		override public function initialize():void{
			super.layout = new VLayout();
			super.initialize();
		}
		
		override protected function get defaultDividerFactory():ClassFactory{
			var df:ClassFactory = new ClassFactory(UIControl);
			df.properties = {percentWidth:100, height:6, backgroundPainter:new GradientFillPainter([0x999999, 0x666666])}
			return df;	
		}
			
		override protected function getDividerDragRect():Rectangle{
			var point:Point = new Point(0, 0);
			point = this.localToGlobal(point);
			return new Rectangle(point.x,point.y,0,this.height);
		}
		
		
		override protected function onDividerDragDrop(event:DragEvent):void{
			//if(!event.dragInitiator == this) return;
			/* 
			If the divider moves up, delta is -ve, otherwise +ve
			*/
			var delta:Number = event.mouseYDelta//point.y - event.dragInitiator.y 
		
			var topUIC:MeasurableControl
			var bottomUIC:MeasurableControl
			
			for(var i:int=0; i< dividerPane.numChildren; i++){
				var child:DisplayObject = dividerPane.getChildAt(i)
				if(child == event.dragInitiator){
					topUIC = MeasurableControl(contentPane.getChildAt(i));
					bottomUIC = MeasurableControl(contentPane.getChildAt(i+1));
					break;
				}
				
			}
			
			var unallocatedHeight:Number = (this.height - this.explicitlyAllocatedHeight);
			var newUnallocatedHeight:Number = unallocatedHeight;
			
			if(isNaN(topUIC.explicitHeight) && isNaN(bottomUIC.explicitHeight)){
				
				/*
				* The change in dimensions can be compensated by recalculating the 
				* two percents. 
				*/
				var newTopH:Number = topUIC.height + delta;
				var newBottomH:Number = bottomUIC.height - delta;
				topUIC.percentUnusedHeight = newTopH*100/unallocatedHeight;
				bottomUIC.percentUnusedHeight = newBottomH*100/unallocatedHeight
			}
			
			
			else if(!isNaN(topUIC.explicitHeight) && !isNaN(bottomUIC.explicitHeight)){
				
				/*
				 * The dimension changes can be safely calculated 
				 */
				topUIC.height+=delta
				bottomUIC.height-=delta;
			}
			
			
			else if(!isNaN(topUIC.explicitHeight)) {
				
				/*
				 * Left child is explicitly sized , right is percent sized
				 */ 
				
				topUIC.height+=delta;
				newUnallocatedHeight = unallocatedHeight-delta;
				for(var j:int=0; j<contentPane.numChildren; j++){
					var currChildL:MeasurableControl = contentPane.getChildAt(j) as MeasurableControl;
					if(dividers.indexOf(currChildL) != -1) continue;
					if(currChildL == topUIC) continue;
					if(currChildL == bottomUIC){
						var newH:Number = currChildL.height-delta;
						bottomUIC.percentUnusedHeight = newH*100/newUnallocatedHeight
					}
					else if(!isNaN(currChildL.percentUnusedHeight)){
						currChildL.percentUnusedHeight = currChildL.percentUnusedHeight*unallocatedHeight/newUnallocatedHeight;
						
					}
				}				
			}
			else{
				/*
				 * Right child is explicitly sized , left is percent sized
				 */ 
				bottomUIC.height-=delta;
				newUnallocatedHeight = unallocatedHeight+delta;
				
				for(var k:int=0; k<contentPane.numChildren; k++){
					var currChild:MeasurableControl = contentPane.getChildAt(k) as MeasurableControl;
					if(dividers.indexOf(currChild) != -1) continue;
					if(currChild == bottomUIC) continue;
					if(currChild == topUIC){
						var newLH:Number = currChild.height+delta;
						topUIC.percentUnusedHeight = newLH*100/newUnallocatedHeight
					}
					else if(!isNaN(currChild.percentUnusedHeight)){
						currChild.percentUnusedHeight = currChild.percentUnusedHeight*unallocatedHeight/newUnallocatedHeight;
					}
				}
			}
			forceInvalidateDisplayList=true;	
		}
		
		override public function updateDisplayList(unscaledWidth:Number, unscaledHeight:Number):void{
			super.updateDisplayList(unscaledWidth, unscaledHeight);
			if(contentPane.numChildren < 2) return; 
			for(var i:uint=1; i<this.contentPane.numChildren; i++){
				var child:DisplayObject = this.contentPane.getChildAt(i);
				dividerPane.getChildAt(i-1).y = child.y;
			} 
		}
		
		override public function set layout(l:ILayout):void{
			throw new Error(getQualifiedClassName(this)+" cannot have layouts applied to it")
		}
		
	}
}