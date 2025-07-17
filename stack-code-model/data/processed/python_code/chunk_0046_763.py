package {
	
	import flash.display.Sprite;
	import flash.events.Event;
	import com.illuzor.dialog.DialogManager;
	import flash.display.StageScaleMode;
	import flash.display.StageAlign;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com  //  illuzor@gmail.com
	 */
	
	public class Main extends Sprite {
		
		public function Main():void {
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			
			DialogManager.init(stage);
			//DialogManager.addAsk("Just simple message");
			//DialogManager.addAsk("You see this message", [ {label:"OK"} ] );
			// entry point
			/*;
			
			//
			
			//var askButtons0:Array = [ { label:"OKAY..."}];
			//DialogManager.addAsk("Вот такое окно тебе!", askButtons0);
			
			DialogManager.addAsk("You see this message", [{label:"OK"}]);
			
			var askButtons:Array = [ { label:"YES", func:yesFunc }, { label:"NO", func:noFunc },{ label:"YES", func:yesFunc }, { label:"NO", func:noFunc },{ label:"YES", func:yesFunc }, { label:"NO", func:noFunc },{ label:"YES", func:yesFunc }, { label:"NO", func:noFunc },{ label:"YES", func:yesFunc }, { label:"NO", func:noFunc },{ label:"YES", func:yesFunc }, { label:"NO", func:noFunc },{ label:"YES", func:yesFunc }, { label:"NO0", func:noFunc } ];
			DialogManager.addAsk("Do you want to do it?", askButtons);
			
			DialogManager.backgroundColor = 0xFA0A5E;
	
			
			var askButtons1:Array = [ { label:"YES", func:yesFunc }, { label:"NO", func:noFunc }];
			DialogManager.addAsk("Do you want to do it?", askButtons1);
			
			var askButtons2:Array = [ { label:"NOOO!!!", func:yesFunc }, { label:"NO", func:noFunc }];
			DialogManager.addAsk("1And this thing?", askButtons2);
			
			var askButtons4:Array = [ { label:"NOOO!!!!!!!!!!!!!!!!!!!!!!!", func:yesFunc }, { label:"NO", func:noFunc }];
			DialogManager.addAsk("2And this thing?", askButtons4);
			
			DialogManager.addAsk("Just simple text...");
			
			//DialogManager.removeAllAsks();*/
			
			DialogManager.addDialog("Do you want to do it?", [ { label:"YES" }, { label:"NO", func:noFunction }, { label:"MAYBE" }, { label:"DON`T KNOW" }, { label:"OK" } ] );
			//DialogManager.removeDialog();
			//DialogManager.removeAllDialogs();
		}
		
		private function yesFunction():void{
			trace("YES pressed");
		}

		private function noFunction():void{
			trace("NO pressed");
		}
		
		/*private function yesFunc():void {
			trace("yes pressed");
		}
		
		private function noFunc():void {
			trace("no pressed");
		}*/
		
	}
}