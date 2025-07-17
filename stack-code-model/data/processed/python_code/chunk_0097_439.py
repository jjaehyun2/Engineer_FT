package  
{
	import flash.text.TextField;
	import flash.text.TextFormat;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class RetryWindow extends Window 
	{
		public var waveBonus:TextField = new TextField();
		public var oriGraphic:OriStaticGraphic = new OriStaticGraphic();
		public var bankGraphic:BankStaticGraphic = new BankStaticGraphic();
		public var toContinue:TextField = new TextField();
		
		public function RetryWindow(width:int = 320, height:int = 240, windowTitle:String = "Wave Incomplete.") 
		{
			super(width,height,windowTitle);
			
			waveBonus.defaultTextFormat = new TextFormat("_typewriter", 16,0xFFFFFF,true,null,null,null,null,"center");
			waveBonus.text = "Incomplete Bonus: x 1";
			waveBonus.x = -width/2 + 5;
			waveBonus.width = width - 10
			waveBonus.height = 35;
			waveBonus.y = -waveBonus.height;
			waveBonus.selectable = false;
			addChild(waveBonus);
			
			oriGraphic.x = -width / 3;
			oriGraphic.y = height / 4;
			addChild(oriGraphic);
			
			bankGraphic.x = width / 3;
			bankGraphic.y = height / 4;
			addChild(bankGraphic);
			
			toContinue.defaultTextFormat = new TextFormat("_typewriter", 14, 0xFFFFFF, true, null, null, null, null, "center");
			toContinue.text = "SPACE to Continue";
			toContinue.x = -width/2 + 5;
			toContinue.width = width - 10
			toContinue.height = 16;
			toContinue.y = height/2 - toContinue.height - 5;
			toContinue.selectable = false;
			//toContinue.border = true;
			//toContinue.borderColor = 0xFFFFFF
			addChild(toContinue);
		}
		
		override public function fadeIn():void 
		{
			super.fadeIn();
			hookSpaceListener();
		}
		
		override public function die():void 
		{
			super.die();
			PlayState.StartSameWaveAndUnpause();
		}
		
	}

}