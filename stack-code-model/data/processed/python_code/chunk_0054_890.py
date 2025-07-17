package screens
{
	
	import flash.text.TextField;
	import flash.text.TextFormatAlign;
	
	import com.pixeldroid.r_c4d3.game.control.Signals;
	import com.pixeldroid.r_c4d3.game.control.Notifier;
	import com.pixeldroid.r_c4d3.game.screen.ScreenBase;
	
	import FontAssets;
	
	
	
	public class TitleScreen extends ScreenBase
	{
		
		
		public function TitleScreen():void
		{
			C.out(this, "constructor");
			super();
		}
		
		
		override protected function onFirstScreen():void
		{
			backgroundColor = 0x777777;
			var title:TextField = addChild(FontAssets.createTextField("GET TO THE SPOT", FontAssets.frucadeMedium(60, 0xffffff, TextFormatAlign.CENTER), width)) as TextField;
			title.x = width*.5 - title.width*.5;
			title.y = height*.5 - title.height*.75;
		}
		
		override public function onUpdateRequest(dt:int):void
		{
			super.onUpdateRequest(dt);
			
			if (timeElapsed > 2*1000) timeOut();
		}
		
		
		private function timeOut():void
		{
			C.out(this, "timeOut - sending SCREEN_GO_NEXT signal");
			Notifier.send(Signals.SCREEN_GO_NEXT);
		}
		
	}
}