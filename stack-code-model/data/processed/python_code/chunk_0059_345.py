//yoyo

package
{
	import as3isolib.display.scene.IsoGrid;
	import as3isolib.geom.IsoMath;
	import as3isolib.geom.Pt;
	
	import com.greensock.TweenLite;
	import com.utilities.EmbedSecure;
	
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.events.TimerEvent;
	import flash.filters.GlowFilter;
	import flash.geom.Point;
	import flash.trace.Trace;
	import flash.utils.Timer;
	import masputih.isometric.*;
	
	
	public class Avatar extends Character
	{
		public function Avatar(iso:IsoGrid, typ:String, artz:EmbedSecure=null, world:World=null)
		{
			trace("new Avatar: "+ typ);
			super(iso,typ,artz,world);
	
			this.newContainer.avatar = this
			this.newContainer.orderNumber = undefined
			
		}
		
		override public function onAnimationStart():void
		{
			if (_myPlot!=null) 
			{
				_myPlot.strokeState = true;
				_myPlot.addStroke();
			}
		}
		
		public override function onAnimationComplete():void {
			
			trace("onAnimationComplete in Avatar...");
			// erik 
			if (_myPlot!=null) {
				_myPlot.strokeState = false;
				_myPlot.removeStroke();
			}
			
			if (atTrash) {
				trace ("at trash");
				this.container.dispatchEvent(new Event(AllSettings.EVENT_AT_TRASH, true));
			}

			dirInc=0
			sprites[0].gotoAndStop("stand")
				
			if (_myPlot && _myPlot.currentVisitor) {
				//_myPlot.playerPresent = true 
				
				switch(_myPlot.currentVisitor.orderStage) {
					case 0:
						enabled=true
						break
					case 1:
						_myPlot.plotOrderObj.mySprite.visible=false
						_myPlot.plotOrderObj.mySprite.gotoAndStop( _myPlot.currentVisitor._myOrder.currentFrame)
						_myPlot.currentVisitor.orderTaken()
						_myPlot.currentVisitor.orderStage = 2
						_myPlot.currentVisitor.itemOnTable=null
						break
					case 2:
						
						//trace(atTable+"  "+itemGot.numChildren)
						if (atTable) {
							this.container.dispatchEvent(new Event(AllSettings.EVENT_AT_TABLE, true)) 
						} 
						
						if (!atTable && itemGot.numChildren > 0 && !_myPlot.currentVisitor.plotCompleted ) {
							
							for (var s:Number = 0; s < itemGot.numChildren; s++) {
								if (Number(_myPlot.currentVisitor._myOrder.currentFrame) == Number(itemGot.getChildAt(s).name)) {
									var itemToRem:MovieClip = itemGot.getChildAt(s) as MovieClip
									break
								}
							}
							if (itemToRem) {
								Main.soundSet["order_delivered"].play()
								switch(Number(_myPlot.currentVisitor._myOrder.currentFrame)) {
									// what are these consts?  Need to make them const with descriptive names.
									case 3:
										TweenLite.to(plot.crops.plot,.3,{delay:8,alpha:1})
										_myPlot.currentVisitor.waterCrops();
										break
									case 2:
										TweenLite.to(plot.crops.plot,.3,{delay:8,alpha:1})
										break
									case 4:
										var crops_driptech:Crops_Ground_DripTech = new Crops_Ground_DripTech(_grid_reference);
										crops_driptech.moveToCell(plot.crops.column, plot.crops.row);
										_world_reference.addGroundObject(crops_driptech);
										plot.crops = crops_driptech;
										TweenLite.to(plot.crops.plot,.3,{delay:4,alpha:1})
										_myPlot.currentVisitor.waterCrops();
										break
									
								}
								itemGot.removeChild(itemToRem)
								//art.orderObjHolder.alpha = 0;
								var _frame_number:int = _myPlot.currentVisitor._myOrder.currentFrame;
								( _frame_number == 4 ) ?  ( _myPlot.plotOrderObj.mySprite.visible = false ) : ( _myPlot.plotOrderObj.mySprite.visible = true ) ;
								_myPlot.currentVisitor.itemOnTable=null
								itemOnTable = null;
								
								TweenLite.to(_myPlot.currentVisitor._myOrder, .5, { alpha:0 } );
								_myPlot.currentVisitor.plotCompleted = true
								atTable = false;
								atTrash = false;
								var ev:VillageEvent =  new VillageEvent(AllSettings.EVENT_ORDER_COMPLETED,false, false, _myPlot.currentVisitor) ;
								ev.farmer = _myPlot.currentVisitor;
								this.newContainer.dispatchEvent(ev);
								trace("Avatar Dispatching EVENT_ORDER_COMPLETED");
							};
						}
						
						break
				}}
		
		
			
				activelyMoving=false
				this.newContainer.dispatchEvent(new Event(AllSettings.EVENT_CHECK_MOVEMENT_SEQUENCER,true))	
			
		}
	}
}