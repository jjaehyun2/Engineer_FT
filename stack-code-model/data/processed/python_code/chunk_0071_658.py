package cascade.animation
{
	import fl.motion.*;
	import fl.transitions.easing.*;
	import fl.transitions.*;
	import flash.display.*;
	import flash.text.*;
	import flash.events.*;
	import flash.utils.*;

	public class Animation
	{
		var timer:Timer = new Timer(1000,1);
		var stageMain:Stage;
		var textToBeAnimated:TextField = new TextField();
		var speacialFont:Font = new myFont();
		var myFormat:TextFormat = new TextFormat(speacialFont.fontName,50,Math.random() * 0xFFFFFF);

		public function AnimateText(textToBeAnimated:TextField):void
		{
			this.textToBeAnimated = textToBeAnimated;
			stageMain = textToBeAnimated.stage;
			stageMain.addEventListener(Event.ENTER_FRAME,onEnter);

			timer.addEventListener(TimerEvent.TIMER, onTick);
			timer.start();

			textToBeAnimated.embedFonts = true;
			textToBeAnimated.setTextFormat(myFormat);

			var gateNumber:int = Math.random() * 3;
			switch (gateNumber)
			{
				case 0 :
					new Tween(textToBeAnimated,"rotationX",None.easeInOut,0,360,2,true);
					break;
				case 1 :
					new Tween(textToBeAnimated,"rotationY",None.easeInOut,0,360,2,true);
					break;
				case 2 :
					new Tween(textToBeAnimated,"rotationZ",None.easeInOut,0,360,2,true);
					break;
			}
			new Tween(textToBeAnimated,"x",None.easeInOut,randomRange(0,stageMain.stageWidth),randomRange(0,stageMain.stageWidth),2,true);
			new Tween(textToBeAnimated,"y",Regular.easeOut,stageMain.stageHeight,randomRange(stageMain.stageHeight / 5,stageMain.stageHeight),1,true);
		}

		function randomRange(minNum:Number, maxNum:Number):Number
		{
			return (Math.floor(Math.random() * (maxNum - minNum + 1)) + minNum);
		}

		function onTick(event:TimerEvent):void
		{
			var verticalTween:Tween = new Tween(textToBeAnimated,"y",Regular.easeIn,textToBeAnimated.y,stageMain.stageHeight,1,true);
			verticalTween.addEventListener(TweenEvent.MOTION_FINISH, onFinish);
		}

		function onFinish(e:TweenEvent):void
		{
			textToBeAnimated.parent.removeChild(textToBeAnimated);
		}

		var i:Number = 0;
		function onEnter(e:Event):void
		{
			if (i%10==0)
			{
				myFormat.color = Math.random() * 0xFFFFFF;
				textToBeAnimated.setTextFormat(myFormat);
			}
			i++;
		}
	}
}