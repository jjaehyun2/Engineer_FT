package com.appfw.view.ui.battle
{
	import com.coffeebean.view.city.item.BuilderItemImage;
	
	import flash.geom.Point;
	
	import starling.animation.IAnimatable;
	import starling.display.Image;
	import starling.display.QuadBatch;
	import starling.textures.Texture;
	import starling.textures.TextureAtlas;
	
	public class Brigand extends QuadBatch implements IAnimatable
	{
		private static const WALK_UP:String = "wup_";
		private static const WALK_DOWN:String = "wdown_";
		private static const WALK_RIGHT:String = "wright_";
		private static const WALK_LEFT:String = "wright_";// 同一个纹理集，但是要水平翻转
		private static const ATK:String = "atk_";
		private static const DEAD:String = "dead_";
		private static const STAND:String = "stand_";
		
		public static const STATE_WALK_LEFT:String = "STATE_WALK_LEFT";
		public static const STATE_WALK_UP:String = "STATE_WALK_UP";
		public static const STATE_WALK_DOWN:String = "STATE_WALK_DOWN";
		public static const STATE_WALK_RIGHT:String = "STATE_WALK_RIGHT";
		public static const STATE_ATK:String = "STATE_ATK";
		public static const STATE_DEAD:String = "STATE_DEAD";
		public static const STATE_STAND:String = "STATE_STAND";
		
		private var _textureAtlas:TextureAtlas;
		
		private var _pasue:Boolean = false;
		private var _repeatTime:Number=0.1;//动画频率
		private var _stopRepeatTime:Number=20;//停止频率
		private var _timeSpan:Number = 0;
		
		private var _now:String;//当前状态
		private var _nowTextures:Vector.<Texture>;
		private var _crtFrame:int;
		private var _totalFrame:int;//总帧数
		private var _crtImage:Image;
		private var _imgPx:Number;
		private var _imgPy:Number;
		
		protected var _movePath:Array;
		protected var _movePoint:Point;
		
		public function get pasue():Boolean
		{
			return _pasue;
		}
		
		public function set pasue(value:Boolean):void
		{
			_pasue = value;
		}
		
		public function get now():String
		{
			return _now;
		}
		
		public function set now(value:String):void
		{
			_now = value;
			resetState();
		}
		
		protected function resetState():void
		{
			_crtFrame = 0;
			_totalFrame = 0;
			_timeSpan = 0;
		}

		public function Brigand()
		{
			super();
		}
		
		public function testWalk():void
		{
			
		}
		
		public function willWalk(path:Array):void
		{
			if(path==null||path.length==0)
			{
				willStand();
				return;
			}
			_movePath = path;
			now = getNextPointDir(path[0] as Point);
			_nowTextures = getTextures();
			_totalFrame = _nowTextures.length;
			
			if(_totalFrame>0)
			{
				if(_crtImage==null)
				{
					_crtImage = new Image(_nowTextures[_crtFrame]);
					addImage(_crtImage);
					this.pivotX = _imgPx;
					this.pivotY = _imgPy;
				}					
				else
				{
					_crtImage.texture = _nowTextures[_crtFrame];
					_crtImage.readjustSize();
					addImage(_crtImage);
				}
				
			}
		}
		/**
		 * 比较对角线
		 * 0-1
		 * 2-3
		 * 如果0到1的距离大于0到2的距离就左右移动方向，反之就是上下移动方向
		 * @param p
		 * @return 
		 */		
		private function getNextPointDir(p:Point):String
		{
			var dir:String = "";
			var crtX:int = this.x;
			var crtY:int = this.y;
			var absW:int = Math.abs(crtX - p.x);
			var absH:int = Math.abs(crtY - p.y);
			if(absW >= absH)
			{
				// 左右移动
				if(crtX > p.x)
					dir = STATE_WALK_LEFT;
				else
					dir = STATE_WALK_RIGHT;
			}
			else
			{
				// 上下移动
				if(crtY > p.y)
					dir = STATE_WALK_UP;
				else
					dir = STATE_WALK_DOWN;
			}
			return dir;
		}
		/*
		protected function playWalk():void
		{
			var dx:Number = _moveX - x;
			var dy:Number = _moveX - y;
			var juli:Number = Math.sqrt(dx * dx + dy * dy);//斜边的长速
			//			trace(MoveX+","+MoveY+","+","+y+","+juli);
			//如果当前这帧移动的C边距离长度已经小于或者等于10速度，说明已经很近目标，或者已经等于目标的位置了，就停止移动
			if (speed*timeSpan >= juli)
			{
				x = MoveX;//因为是以10像素以下为步长移动，总会有偏差1-3个像素的误差，所以近了就把人物放到标准的目标位置
				y = MoveY;//把人物放到标准的目标位置
				if(movePath&&movePath.length>0)
				{
					if(_order)
						var p:Array = movePath.pop();
					else
						p = movePath.shift();
					var pt:Point = CityUtil.getPixelPoint(p[0],p[1]);
					gopoint(pt.x,pt.y)
				}					
				else
					roundgo()
				
				return;//中断退出方法
			}
			
			//如果没有移动目标位置，人物的的X和Y 坐标就每帧执行里就加上 上面算出的每帧距离，直接接近目标
			x += newSpeedX*timeSpan;
			y += newSpeedY*timeSpan;
		}
		*/
		public function willAtk():void
		{
			_nowTextures = _textureAtlas.getTextures(ATK);
		}
		
		public function willDead():void
		{
			_nowTextures = _textureAtlas.getTextures(DEAD);
		}
		
		public function willStand():void
		{
			_nowTextures = _textureAtlas.getTextures(STAND);
		}
		
		public function advanceTime(time:Number):void
		{
			if(_pasue)
				return;
			_timeSpan += time;
			
			if(_timeSpan >= _repeatTime)
			{
				_timeSpan = _timeSpan - _repeatTime //m_TimeSpan%m_RepeatTime;
				_crtFrame++;
				if(_crtFrame >= _totalFrame)
				{
					_crtFrame = 0;
				}
				if(_crtImage)
					_crtImage.texture = _nowTextures[_crtFrame];
			}
			goonPlay();
		}
		
		private function goonPlay():void
		{
			// TODO Auto Generated method stub
			if(now == STATE_WALK_LEFT || now == STATE_WALK_RIGHT || now == STATE_WALK_UP || now == STATE_WALK_DOWN)
			{
//				playWalk();
			}
			else if(now == STATE_ATK)
			{
//				dirStr = ATK;
			}
			else if(now == STATE_DEAD)
			{
//				dirStr = DEAD;
			}
			else if(now == STATE_STAND)
			{
//				dirStr = STAND;
			}
		}
		
		protected function getTextures():Vector.<Texture>
		{
			if(!_textureAtlas)
			{
				return null;
			}
			var dirStr:String = "";
			if(now == STATE_WALK_LEFT)
			{
				dirStr = WALK_RIGHT;
			}
			else if(now == STATE_WALK_RIGHT)
			{
				dirStr = WALK_RIGHT;
			}
			else if(now == STATE_WALK_UP)
			{
				dirStr = WALK_UP;
			}
			else if(now == STATE_WALK_DOWN)
			{
				dirStr = WALK_DOWN;
			}
			else if(now == STATE_ATK)
			{
				dirStr = ATK;
			}
			else if(now == STATE_DEAD)
			{
				dirStr = DEAD;
			}
			else if(now == STATE_STAND)
			{
				dirStr = STAND;
			}
			
			return _textureAtlas.getTextures(dirStr);
		}
		
	}
}