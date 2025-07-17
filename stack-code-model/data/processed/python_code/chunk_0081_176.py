package 
{
	import com.greensock.TweenLite;
	import com.greensock.easing.Bounce;
	import com.utilities.EmbedSecure;
	
	import flash.display.Bitmap;
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.filters.GlowFilter;
	/**
	 * ...
	 * @author ian
	 */
	public class WindowsSystem extends Sprite
	{
		private var _window_instructions:MovieClip
		private var storyboard:MovieClip;
		private var instructions:MovieClip;
		
		private var _window_avatarpicker:Sprite;
		private var _window_won:Sprite;
		private var _window_end:Sprite;
		private var _window_innovation:Sprite;
		private var _window_goal:Sprite;
		public var _windowsAr:Array = new Array()
		public var _currentWindow:MovieClip
		private var _window_ui_standard:Sprite = new Sprite();
		private var _window_ui_standardOrigin:Number = 0;
		//private var _tempButCls:Class;
		private var _dispatchType:String;
		private var _boyChoice:MovieClip;
		private var _girlChoice:MovieClip;
		private var _finalChoice:MovieClip;
		private var _avatarChoiceType:String;
		public static const EVENT_WINDOW:String = "dispatch window event";
		public static const EVENT_WINDOWCLOSED:String = "window closed";
		public static const EVENT_CHANGE_AVATAR:String = "change avatar";
		private var _plotYorigin:Number = 0;
		private var _plot:MovieClip
		private var _maleYorigin:Number = 0;
		private var _femaleYorigin:Number = 0;
		private var _instructionsCreated:Boolean=false;
		public var final_win_message:String;
		
		public function WindowsSystem(emb:EmbedSecure = null) 
		{
			
			//_tempButCls=emb.grabClass("button_multipurpose");
			
			//var win_inst:Class = emb.grabClass("window_instructions");
			//_window_instructions = new window_instructions();
			_window_instructions = new Screens();//new window_instructions();
			_windowsAr.push(_window_instructions);
			addChild(_window_instructions);
			
			
			//var win_ava:Class = emb.grabClass("window_avatarpicker");
			_window_avatarpicker = new window_avatarpicker();
			_windowsAr.push(_window_avatarpicker);
			addChild(_window_avatarpicker);
			setupAvatarPicker();
			
			//var win_won:Class = emb.grabClass("window_game_won");
			_window_won = new window_game_won();
			_windowsAr.push(_window_won);
			addChild(_window_won);
			
			//var win_end:Class = emb.grabClass("window_game_end");
			_window_end = new window_game_end();
			_windowsAr.push(_window_end);
			addChild(_window_end);
			
			// need to add innovation and goal screens intot the mix.
			_window_innovation = new InnovationScreen();
			_windowsAr.push(_window_innovation);
			addChild(_window_innovation);
			
			_window_goal = new GoalScreen();
			_windowsAr.push(_window_goal);
			addChild(_window_goal);
			
			//
			_window_ui_standard.mouseEnabled=true;
			_window_ui_standard.graphics.beginFill(0xFFFF00,0);
			_window_ui_standard.graphics.drawRect(0, 0, Preloader.stageObj.stageWidth , 100);
			_window_ui_standard.graphics.endFill();
			_window_ui_standard.y = Preloader.stageObj.height - 101;
			_window_ui_standardOrigin = _window_ui_standard.y;
			_window_ui_standard.y+=300
			addChild(_window_ui_standard);
			Main.soundSet["ambient"].play(0,1000)
			//
			
		}
		
		
		public function hideAll():void {
			for (var d:Number = 0; d < _windowsAr.length; d++) {
				_windowsAr[d].alpha = 0;
				_windowsAr[d].visible = false;
			}
		}
	
		
		
		public function show(nm:String):void {
			
			trace("show " + nm);
			hideAll()
			mouseEnabled = true
			mouseChildren=true
			var temp:Boolean = true;
			
			switch(nm) {
				case "instruct":
					
					_currentWindow = _windowsAr[0];
					if (!_instructionsCreated) {
						welcomeSetup()
					}
					break
				case "avatarPicker":
					resetUI();
					_currentWindow = _windowsAr[1];
					animateAvatarWindow()
					TweenLite.to(_window_ui_standard, .5, { delay:1, y:_window_ui_standardOrigin } );
					break
				case "gameEnd":
					temp = false;
					_currentWindow = _windowsAr[3];
					resetUI();
					addPlayAgainButton();
					addRetryButton();
					TweenLite.to(_window_ui_standard, .5, { delay:1, y:_window_ui_standardOrigin } );
					break
				case "levelWin":
					_currentWindow = _windowsAr[2];
					resetUI();
					addPlayAgainButton();
					// if there's final win message that means they just played the last level. 
					if(!final_win_message){
						addNextLevelButton();
					}else{
						_currentWindow.message.text = final_win_message;
					}
					//addRetryButton();
					TweenLite.to(_window_ui_standard, .5, { delay:1, y:_window_ui_standardOrigin } );
					break
				// not sure if adding this last line is smart or not but we'll see. originally done to update currentwindow to the Screensmovie clip 
				case "innovation":
					_currentWindow = _windowsAr[3];
					_currentWindow.addEventListener(MouseEvent.CLICK, showGoalScreen);
					_currentWindow.mouseChildren = false;
					
				case "goal":
					_currentWindow = _windowsAr[5];
					_currentWindow.addEventListener(MouseEvent.CLICK, dispatchFromWindowHandler);
					_currentWindow.mouseChildren = false;		
			}
			
			_currentWindow.visible = true;
			_currentWindow.gotoAndStop(1);
			TweenLite.to(_currentWindow, .5, { alpha:1 } )
			addChild(_window_ui_standard);
		}
		
	
		private function showGoalScreen():void{
			show("goal");
		}
		
		public function fade():void {
			TweenLite.to(_currentWindow,.5,{delay:.5,alpha:0,onComplete:function():void{dispatchEvent(new Event(EVENT_WINDOWCLOSED,true))}})
			TweenLite.to(_window_ui_standard,1,{y:_window_ui_standardOrigin+300})
		}
		
		public function disable():void {
			mouseEnabled = false
			mouseChildren = false
		}
		
		private function ot(event:Event):void {
			event.target.butback.gotoAndStop(1)	
		}
		private function ov(event:Event):void {
			Main.soundSet["button_over"].play()
			event.target.butback.gotoAndStop(2)		
		}
		private function dispatchFromWindowHandler(event:Event):void {
			Main.soundSet["button_down"].play()
			//trace("dispatch")
			_dispatchType=event.target.name
			dispatchEvent(new Event(EVENT_WINDOW, true));
		}
		
		public function get dispatchType():String {
			return _dispatchType;
		}
		
		//avatarPicker
		private function setupAvatarPicker():void {
			_boyChoice = _windowsAr[1].player_male;
			_boyChoice.buttonMode = true;
			_boyChoice.useHandCursor = true;
			_boyChoice.addEventListener(MouseEvent.MOUSE_DOWN, avatarChoice)
			_boyChoice.addEventListener(MouseEvent.MOUSE_OVER, addStroke)
			_boyChoice.addEventListener(MouseEvent.MOUSE_OUT,removeStroke)
			_girlChoice = _windowsAr[1].player_female;
			_girlChoice.buttonMode = true;
			_girlChoice.useHandCursor = true;
			_girlChoice.addEventListener(MouseEvent.MOUSE_DOWN,avatarChoice)
			_girlChoice.addEventListener(MouseEvent.MOUSE_OVER, addStroke)
			_girlChoice.addEventListener(MouseEvent.MOUSE_OUT, removeStroke)
			
			
			
			_plot=_windowsAr[1].plot
			_plotYorigin= _plot.y
			_maleYorigin= _boyChoice.y
			_femaleYorigin = _girlChoice.y
		}
		public function animateAvatarWindow():void {
			_plot.alpha = 0
			_plot.y -= 100
			TweenLite.to(_plot, .6, { delay:.5, alpha:1, y:_plotYorigin, ease:Bounce.easeOut } )
			//
			_boyChoice.alpha = 0
			_boyChoice.y -= 100
			TweenLite.to(_boyChoice, .6, { delay:1, alpha:1, y:_maleYorigin, ease:Bounce.easeOut } )
			//
			_girlChoice.alpha = 0
			_girlChoice.y -= 100
			TweenLite.to(_girlChoice, .6, { delay:1.5, alpha:1, y:_femaleYorigin, ease:Bounce.easeOut } )
			
		}
		private function addStroke(event:Event):void {
			//trace("add avatar stroke")
			Main.soundSet["select"].play()
			if(_finalChoice!=event.target as MovieClip){
				var filt:Array = new Array();
				var g:GlowFilter = new GlowFilter(0xFFFF00, 1, 3, 3, 100);
				filt.push(g);
				event.target.filters = filt}
		}
		private function removeStroke(event:Event):void {
			if(_finalChoice!=event.target as MovieClip){
				var filt:Array = new Array();
				event.target.filters = new Array()}		
		}
		
		private function avatarChoice(event:Event):void {
			Main.soundSet["tribal_beat"].play()
			addPlayButton();
			if (_finalChoice) {
				//Main.soundSet["select2"].play()
				var filt:Array = new Array();
				_finalChoice.filters = new Array()}	
			_finalChoice = event.target as MovieClip;
			_avatarChoiceType = _finalChoice.name
			
			dispatchEvent(new Event(EVENT_CHANGE_AVATAR, true));
		}
		
		private function addPlayAgainButton(): void
		{
			var tempPlay:MovieClip = new button_multipurpose();
			tempPlay.x = Math.round((Preloader.stageObj.stageWidth / 2) - tempPlay.width / 2) + 25;
			tempPlay.name = "replay";
			tempPlay.y = -110;
			tempPlay.mouseChildren = false;
			tempPlay.useHandCursor = true;
			tempPlay.buttonMode = true;
			tempPlay.addEventListener(MouseEvent.MOUSE_OVER, ov);
			tempPlay.addEventListener(MouseEvent.MOUSE_OUT, ot);
			tempPlay.addEventListener(MouseEvent.MOUSE_DOWN, dispatchFromWindowHandler);
			tempPlay.copy.text = "PLAY AGAIN";
			
			_window_ui_standard.addChild(tempPlay);
		}
		
		private function addNextLevelButton(): void
		{
			var tempPlay:MovieClip = new button_multipurpose();
			tempPlay.x = Math.round((Preloader.stageObj.stageWidth / 2) - tempPlay.width / 2) + 25;
			tempPlay.name = "nextLevel";
			tempPlay.y = -140;
			tempPlay.mouseChildren = false;
			tempPlay.useHandCursor = true;
			tempPlay.buttonMode = true;
			tempPlay.addEventListener(MouseEvent.MOUSE_OVER, ov);
			tempPlay.addEventListener(MouseEvent.MOUSE_OUT, ot);
			tempPlay.addEventListener(MouseEvent.MOUSE_DOWN, dispatchFromWindowHandler);
			tempPlay.copy.text = "Next Level";
			
			_window_ui_standard.addChild(tempPlay);
		}
		
		
		private function addRetryButton(): void{
			var tempPlay:MovieClip = new button_multipurpose();
			tempPlay.x = Math.round((Preloader.stageObj.stageWidth / 2) - tempPlay.width / 2) + 25;
			tempPlay.name = "retry level";
			tempPlay.y = -170;
			tempPlay.mouseChildren = false;
			tempPlay.useHandCursor = true;
			tempPlay.buttonMode = true;
			tempPlay.addEventListener(MouseEvent.MOUSE_OVER, ov);
			tempPlay.addEventListener(MouseEvent.MOUSE_OUT, ot);
			tempPlay.addEventListener(MouseEvent.MOUSE_DOWN, dispatchFromWindowHandler);
			tempPlay.copy.text = "Retry Level";
			
			_window_ui_standard.addChild(tempPlay);
		}
		
		private function addPlayButton(): void{
			var tempPlay:MovieClip = new button_multipurpose();
			tempPlay.x = Math.round((Preloader.stageObj.stageWidth / 2) - tempPlay.width / 2) + 25;
			tempPlay.name = "play";
			tempPlay.y = 10;
			tempPlay.mouseChildren = false;
			tempPlay.useHandCursor = true;
			tempPlay.buttonMode = true;
			tempPlay.addEventListener(MouseEvent.MOUSE_OVER, ov);
			tempPlay.addEventListener(MouseEvent.MOUSE_OUT, ot);
			tempPlay.addEventListener(MouseEvent.MOUSE_DOWN, dispatchFromWindowHandler);
			tempPlay.copy.text = "PLAY";
			trace("button");
			_window_ui_standard.addChild(tempPlay);
		}
		
		
		public function get avatarType():String {
			return _avatarChoiceType; 
		}
		private function welcomeSetup():void {
			_currentWindow.x = 0;
			_currentWindow.y = 0;
			_currentWindow.welcomescreen.continue_button.text = "play";
			_currentWindow.welcomescreen.continue_button.mouseChildren = false;
			_currentWindow.welcomescreen.continue_button.useHandCursor = true;
			_currentWindow.welcomescreen.continue_button.buttonMode = true;
			_currentWindow.welcomescreen.continue_button.addEventListener(MouseEvent.MOUSE_OVER, ov);
			_currentWindow.welcomescreen.continue_button.addEventListener(MouseEvent.MOUSE_OUT, ot);
			_currentWindow.welcomescreen.continue_button.addEventListener(MouseEvent.MOUSE_DOWN, removeInstructions);
			//
			_currentWindow.welcomescreen.instructions_button.copy.text = "instructions";
			_currentWindow.welcomescreen.instructions_button.mouseChildren = false;
			_currentWindow.welcomescreen.instructions_button.useHandCursor = true;
			_currentWindow.welcomescreen.instructions_button.buttonMode = true;
			_currentWindow.welcomescreen.instructions_button.addEventListener(MouseEvent.MOUSE_OVER, ov);
			_currentWindow.welcomescreen.instructions_button.addEventListener(MouseEvent.MOUSE_OUT, ot);
			_currentWindow.welcomescreen.instructions_button.addEventListener(MouseEvent.MOUSE_DOWN,gotoIntructions);
			//
			_currentWindow.welcomescreen.storyboard_button.copy.text = "story";
			_currentWindow.welcomescreen.storyboard_button.mouseChildren = false;
			_currentWindow.welcomescreen.storyboard_button.useHandCursor = true;
			_currentWindow.welcomescreen.storyboard_button.buttonMode = true;
			_currentWindow.welcomescreen.storyboard_button.addEventListener(MouseEvent.MOUSE_OVER, ov);
			_currentWindow.welcomescreen.storyboard_button.addEventListener(MouseEvent.MOUSE_OUT, ot);
			_currentWindow.welcomescreen.storyboard_button.addEventListener(MouseEvent.MOUSE_DOWN,gotoStoryBoard);
		}
		
		private function gotoIntructions(event:Event):void {
			_currentWindow.gotoAndStop("instructionsframe");
			_currentWindow.instructions.continue_button.x = 580;
			_currentWindow.instructions.continue_button.y = 440;
			_currentWindow.instructions.continue_button.visible = true;
			_currentWindow.instructions.continue_button.mouseChildren = false;
			_currentWindow.instructions.continue_button.addEventListener(MouseEvent.MOUSE_OVER, ov);
			_currentWindow.instructions.continue_button.addEventListener(MouseEvent.MOUSE_OUT, ot);
			_currentWindow.instructions.continue_button.addEventListener(MouseEvent.MOUSE_DOWN, removeInstructions);
			
		}
		private function gotoStoryBoard(event:Event):void {
			
			
			//_currentWindow.clip.gotoAndStop("storyboard");
			_currentWindow.gotoAndStop("storyboardframe");
			_currentWindow.storyboard.gotoInstructionsButton.copy.text = "Next ->";
			_currentWindow.storyboard.gotoInstructionsButton.mouseChildren = false;
			_currentWindow.storyboard.gotoInstructionsButton.useHandCursor = true;
			_currentWindow.storyboard.gotoInstructionsButton.buttonMode = true;
			_currentWindow.storyboard.gotoInstructionsButton.addEventListener(MouseEvent.MOUSE_DOWN,gotoIntructions);
			_currentWindow.storyboard.gotoInstructionsButton.addEventListener(MouseEvent.MOUSE_OVER, ov);
			_currentWindow.storyboard.gotoInstructionsButton.addEventListener(MouseEvent.MOUSE_OUT, ot);
			/*
			_currentWindow.StoryBoard.continue_button.visible = false;
			_currentWindow.StoryBoard.storyboard_button.visible = false;
			_currentWindow.StoryBoard.instructions_button.visible = true;
			_currentWindow.StoryBoard.instructions_button.x = 580;
			_currentWindow.StoryBoard.instructions_button.y = 470;
			*/
			//Do i need these visible invisible statements anymore?
		}
		private function removeInstructions(event:Event):void {
			Main.soundSet["tribal_1"].play()
			TweenLite.to(_currentWindow, .5, { alpha:1,onComplete:show("avatarPicker") } )
		}
		
		private function resetUI():void
		{
			while (_window_ui_standard.numChildren > 0)
			{
				_window_ui_standard.removeChildAt(0);
			}
		}
	}
}