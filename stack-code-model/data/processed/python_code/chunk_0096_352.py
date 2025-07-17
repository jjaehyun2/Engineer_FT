package
{	
		import flash.display.Bitmap;
		import flash.display.Sprite;
		import flash.events.*;
		import flash.geom.Point;
		import flash.utils.Timer;

		public class ScoreFloater extends Sprite
		{
			public var Bitz : Bitmap = new Bitmap ()
			private var maxFrame : Number = 0
			private var seqAr : Array = new Array ()
			private var _externalArt : Array
			private var storedLength : Number = 0
			
			private var _accel : Number = 0
			private var _myTm : Timer
			private var offset:Point;
			public function ScoreFloater ( incomingNum : String,externalArt :Array, offset:Point) : void
			{
				trace("new ScoreFloater ...offset: " + offset);
				_externalArt = externalArt
				prepareFrames (externalArt)
				this.scaleX = .6
				this.scaleY = .6
				this.offset = offset;
	
				
				if (incomingNum.substr (0,1) == "-")
				{
					var tempBit : Bitmap = new Bitmap (_externalArt [10])
					this.addChild (tempBit)
					var tempNum : Number = 1
				}else
				{
					tempNum = 0
				}
				for (var cnt : Number = tempNum; cnt < incomingNum.length; cnt ++)
				{
					//seqAr [Number (incomingNum.substr (cnt, 1))]
					tempBit = new Bitmap (_externalArt[Number (incomingNum.substr (cnt, 1))])
					tempBit.x += cnt * 20
					this.addChild (tempBit)
					this.x -= (tempBit.width/3)
					storedLength = cnt
					//trace("BITTZ" + Number (incomingNum.substr (cnt, 1)))
					
				}
				tempBit = new Bitmap (seqAr [13])
				tempBit.x += (incomingNum.length) * 20
				this.addChild (tempBit)
				this.y += offset.y;
				this.x += offset.x;
				this.mouseEnabled=false
				this.mouseChildren=false
				_myTm = new Timer (20)
				_myTm.addEventListener (TimerEvent.TIMER, float)
				_myTm.start ()
			}
			public function prepareFrames (dataWrap : Object) : void
			{
				for (var bit : String in dataWrap)
				{
					maxFrame ++
						seqAr.push (dataWrap ["bit" + maxFrame])
				}
				
				Bitz.smoothing = false
			}
			public function kill () : void
			{
				if (_myTm)
				{
					_myTm.stop ()
				}
				if (this.parent) {
					this.parent.removeChild (this)}
			}
			private function float (event : Event) : void
			{
				//trace("floating: " + event)
				
				
				_accel +=.1
				this.y -= (_accel)
				
				if (this.alpha > 0)
				{
					//capsule.alpha -= (_accel / 200)
				}
				if (this.y < - 400)
				{
					//trace(capsule.y)
					kill ()
				}
				
				
			}
		}
	}