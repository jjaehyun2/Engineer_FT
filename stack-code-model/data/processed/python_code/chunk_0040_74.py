package com.utilities
{
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.TimerEvent;
	import flash.utils.Timer;
	import flash.display.PixelSnapping
	public class BitMapper
	{
		public var seqAr : Array = new Array ()
		public var maxFrame : uint = 0
		public var curFrame : uint = 1
		public var drvFrame : Number = 0
		public var externalArt : MovieClip
		public var Bitz : Bitmap = new Bitmap ()
		public var hotZone : Sprite = new Sprite
		public var capsule : Sprite = new Sprite ()
		public var charArRef : Object = new Object ()
		public var actionTimer : Timer
		public var currentAction : Array
		public var bitDisposalList : Array = new Array ()
		
		
		public function BitMapper () : void
		{
			//externalArt=externalArtz
		
		}
		public function buildDataObject (nm : String, strtFrame : Number, endFrame : Number, clp : MovieClip) :Array
		{
			
			var artArray:Array=new Array()
			for (var D : Number = strtFrame; D < (endFrame + 1); D ++)
			{
				var bTem : BitmapData = new BitmapData (clp.width, clp.height, true, 0x00ffffff)
				
				clp.inner.gotoAndStop (D)
				bTem.draw (clp)
				artArray.push(bTem)
			}
			return artArray
		}
		//public function artConverter(mov:MovieClip):Object{
		//}
		public function prepareFrames (dataWrap : Object) : void
		{
			for (var bit : String in dataWrap)
			{
				maxFrame ++
				seqAr.push (dataWrap ["bit" + maxFrame])
			}
			Bitz.x = - (dataWrap ["bit" + 1].width / 2)
			Bitz.y = - (dataWrap ["bit" + 1].height / 2)
			capsule.addChild (Bitz)
			Bitz.pixelSnapping=PixelSnapping.NEVER
			//Bitz.cacheAsBitmap=true
			Bitz.smoothing=false
			
		}
		public function accessor (frm : Number) : void
		{
			Bitz.bitmapData = seqAr [frm]
			
		}
		public function sequencePlayer (ar :Array, sp : Number, loop : Boolean) : void
		{
			//trace("panBug1"+ar)
			
			curFrame = ar [0]
			accessor (curFrame - 1)
			currentAction = ar
			if (actionTimer)
			{
				actionTimer.removeEventListener (TimerEvent.TIMER, actionPack)
				actionTimer.reset ()
			}
			if (loop)
			{
				actionTimer = new Timer (sp)
				actionTimer.addEventListener (TimerEvent.TIMER, actionPack)
				actionTimer.start ()
			}else
			{
				actionTimer = new Timer (sp, ar [ar.length - 1])
				actionTimer.addEventListener (TimerEvent.TIMER, singleShot)
				actionTimer.start ()
			}
		}
		public function actionPack (event : Event) : void
		{
			frameChecker ()
			
				if (curFrame < currentAction [currentAction.length - 1])
				{
					curFrame ++
					accessor (curFrame - 1)
				}else
				{
					curFrame = currentAction [0]
					accessor (curFrame - 1)
				}
		
		}
		public function frameChecker () : void
		{
		}
		public function singleShot (event : Event) : void
		{
			//trace(currentAction)
			
			
				if (curFrame <= currentAction [currentAction.length - 1])
				{
					curFrame ++ 
				}else
				{
					actionTimer.stop ()
					singleShotDone ()
				}
				accessor (curFrame - 1)
			
		
		}
		public function framLoc () : void
		{
			curFrame = currentAction [0]
		}
		public function singleShotDone () : void
		{
			//trace ("signelshotdone")
		}
		public function drawHotty (width : Number, height : Number) : void
		{
			hotZone.name = "hotZone"
			hotZone.graphics.beginFill (0xFF);
			hotZone.graphics.drawRect (0, 0, width, height);
			hotZone.graphics.endFill ();
			capsule.addChild (hotZone)
		}
		public function get DisposalList () : Array
		{
			return bitDisposalList
		}
	}
}