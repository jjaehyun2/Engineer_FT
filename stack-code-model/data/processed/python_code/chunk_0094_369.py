package org.openPyro.containers
{
	import flash.display.DisplayObject;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.utils.getQualifiedClassName;
	
	import org.openPyro.containers.events.DividerEvent;
	import org.openPyro.core.ClassFactory;
	import org.openPyro.core.MeasurableControl;
	import org.openPyro.core.UIControl;
	import org.openPyro.layout.HLayout;
	import org.openPyro.layout.ILayout;
	import org.openPyro.managers.events.DragEvent;
	import org.openPyro.painters.GradientFillPainter;
	
	/**
	 * 
	 */ 
	public class HDividedBox extends DividedBox
	{
		/**
		 * Constructor
		 */ 
		public function HDividedBox(){
			super();
			_styleName = "HDividedBox";
		}
		
		override public function initialize():void{
			super.layout = new HLayout();
			super.initialize()
		}
		
		override protected function get defaultDividerFactory():ClassFactory{
			var df:ClassFactory = new ClassFactory(UIControl);
			df.properties = {percentHeight:100, width:6, backgroundPainter:new GradientFillPainter([0x999999, 0x666666])}			
			return df;
		}
		
		
		protected var leftUIC:MeasurableControl
		protected var rightUIC:MeasurableControl
		
		/**
		 * @inheritDoc
		 */ 
		override protected function getDividerDragRect():Rectangle{
			var point:Point = new Point(0,0);
			point = this.localToGlobal(point);
			
			return new Rectangle(point.x,point.y,this.width, 0)
		}
		
		
		override protected function onDividerDragDrop(event:DragEvent):void{
			/* 
			If the divider moves left, delta is -ve, otherwise +ve
			*/
			var delta:Number = event.mouseXDelta
			
			for(var i:int=0; i<dividerPane.numChildren; i++){
				var child:DisplayObject = dividerPane.getChildAt(i)
				if(child == event.dragInitiator){
					leftUIC = MeasurableControl(contentPane.getChildAt(i));
					rightUIC = MeasurableControl(contentPane.getChildAt(i+1));
					break;
				}
				
			}
			
			/*
			Disable mouseEvents so that rollovers etc are 
			not triggered if the mouse rolls over them
			*/
			leftUIC.cancelMouseEvents();
			rightUIC.cancelMouseEvents();
			
			
			var unallocatedWidth:Number = (this.width - this.explicitlyAllocatedWidth);
			var newUnallocatedWidth:Number = unallocatedWidth;
			
			if(isNaN(leftUIC.explicitWidth) && isNaN(rightUIC.explicitWidth)){
				
				/*
				* The change in dimensions can be compensated by recalculating the 
				* two percents. 
				*/
				var newLeftW:Number = leftUIC.width + delta;
				var newRightW:Number = rightUIC.width - delta;
				leftUIC.percentUnusedWidth = newLeftW*100/unallocatedWidth;
				rightUIC.percentUnusedWidth = newRightW*100/unallocatedWidth
			}
			
			
			else if(!isNaN(leftUIC.explicitWidth) && !isNaN(rightUIC.explicitWidth)){
				
				/*
				 * The dimension changes can be safely calculated 
				 */
				leftUIC.width+=delta
				rightUIC.width-=delta;
			}
			
			
			else if(!isNaN(leftUIC.explicitWidth)) {
				
				/*
				 * Left child is explicitly sized , right is percent sized
				 */ 
				
				leftUIC.width+=delta;
				newUnallocatedWidth = unallocatedWidth-delta;
				for(var j:int=0; j<contentPane.numChildren; j++){
					var currChildL:MeasurableControl = contentPane.getChildAt(j) as MeasurableControl;
					if(dividers.indexOf(currChildL) != -1) continue;
					if(currChildL == leftUIC) continue;
					if(currChildL == rightUIC){
						var newW:Number = currChildL.width-delta;
						rightUIC.percentUnusedWidth = newW*100/newUnallocatedWidth
					}
					else if(!isNaN(currChildL.percentUnusedWidth)){
						currChildL.percentUnusedWidth = currChildL.percentUnusedWidth*unallocatedWidth/newUnallocatedWidth;
						
					}
				}				
			}
			else{
				/*
				 * Right child is explicitly sized , left is percent sized
				 */ 
				rightUIC.width-=delta;
				newUnallocatedWidth = unallocatedWidth+delta;
				
				for(var k:int=0; k<contentPane.numChildren; k++){
					var currChild:MeasurableControl = contentPane.getChildAt(k) as MeasurableControl;
					if(dividers.indexOf(currChild) != -1) continue;
					if(currChild == rightUIC) continue;
					if(currChild == leftUIC){
						var newLW:Number = currChild.width+delta;
						leftUIC.percentUnusedWidth = newLW*100/newUnallocatedWidth
					}
					else if(!isNaN(currChild.percentUnusedWidth)){
						currChild.percentUnusedWidth = currChild.percentUnusedWidth*unallocatedWidth/newUnallocatedWidth;
					}
				}
			}
			
			leftUIC.enableMouseEvents()
			rightUIC.enableMouseEvents();
			forceUpdateDisplayList = true;
			dispatchEvent(new DividerEvent(DividerEvent.DIVIDER_DROP));
		}
		
		/**
		 * @inheritDoc
		 */ 
		override public function updateDisplayList(unscaledWidth:Number, unscaledHeight:Number):void{
			super.updateDisplayList(unscaledWidth, unscaledHeight);
			if(this.contentPane.numChildren < 2) return;
			for(var i:uint=1; i<this.contentPane.numChildren; i++){
				var child:DisplayObject = this.contentPane.getChildAt(i);
				dividerPane.getChildAt(i-1).x = child.x;
			} 
		}
		
		override public function set layout(l:ILayout):void{
			throw new Error(getQualifiedClassName(this)+" cannot have layouts applied to it")
		}
		
	}
}