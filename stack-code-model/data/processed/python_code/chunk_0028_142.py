package game
{
	import com.greensock.TweenLite;
	import com.greensock.easing.Linear;
	
	import flash.display.DisplayObject;

	public class AnimationManager
	{
		public static function dropAndScale(target:DisplayObject,delay:Number=0,dropTime:Number=0.4,scaleTime=0.3,
											scaleX=1.2,scaleY=0.8):void{
			target.visible = true;
			TweenLite.from(target,dropTime,{delay:delay,x:target.x,y:Game.instance().getPosition().y,ease:Linear.easeOut,
				onComplete:function ():void{
					TweenLite.from(target,scaleTime,{scaleX:scaleX,scaleY:scaleY,ease:Linear.easeInOut});
				}});
		}
		
		public static function Scale(target:DisplayObject,scaleTime=0.3,
											scaleX=1.2,scaleY=0.8):void{
			target.visible = true;
			TweenLite.from(target,scaleTime,{scaleX:scaleX,scaleY:scaleY,ease:Linear.easeInOut});
		}
		
		
		
		
	}
}