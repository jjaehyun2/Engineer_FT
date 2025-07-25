﻿/**
 *	Creates main UI for the slot machine, including bet, lines, play,sound buttons, max bet.
 * 	This has only one event listner for this class.  Thus when a button is clicked, it updates the
 *	mGameStatus Object and dispatches an event.  SlotmachineCore will listen for it and
 *	update the game according to mGameStatus
 *
 *	@langversion ActionScript 3.0
 *	@playerversion Flash 9.0 
 *	@author Abraham Lee
 *	@since  03.26.2009
 */

package com.neopets.games.inhouse.blackPawkeetSlots
{
	//----------------------------------------
	//IMPORTS 
	//----------------------------------------
	import flash.display.MovieClip;
	import flash.events.MouseEvent;
	import flash.events.Event;
	import flash.utils.getDefinitionByName;
	
	import flash.text.TextField;
	import flash.text.TextFormat;
	import flash.text.TextFieldAutoSize;
	import flash.text.TextFormatAlign;
	
	import flash.external.ExternalInterface; //added
	import flash.net.URLRequest; //added
	import flash.net.navigateToURL; //added
	
	import com.neopets.users.abelee.resource.easyCall.QuickFunctions;
	
	public class ControlPanel extends MovieClip
	{
		//----------------------------------------
		//VARIABLES
		//----------------------------------------
		private var mMainGame:Object;	// MainGame Class
		private var mMaxBet:int;	// max possible bet, used for max bet button
		private var mMaxLine:int;	// max possible line, used for max bet button
		private var mNPInc:int;		// amount of np increments (only for display purposes when np counts up)
		private var mGameStatus:Object;	//game information: bet, line, active, total bet, np won, etc.
		private var mCurrentBet:MovieClip;	
		private var mCurrentLine:MovieClip;
		private var mMaxBetBtn:MovieClip;	//used for max bet button
		private var mMaxLineBtn:MovieClip;	// used for max bet button
		//		
		//----------------------------------------
		//CONSTRUCTOR 
		//----------------------------------------
		public function ControlPanel(pMainGame:Object = null):void
		{	
			//variable setup
			mMainGame = pMainGame;
			mGameStatus= new Object ();
			mGameStatus.bet = 1;
			mGameStatus.lines = 1;
			mGameStatus.playSlot = false;	// roll teh slots when set to ture
			mGameStatus.endGame = false;	// end the game when true
			mGameStatus.abled = false;		// disable all buttons when false
			mGameStatus.totalBet = mGameStatus.bet * mGameStatus.lines;
			mGameStatus.won = 0;
			mGameStatus.jackpot = 0;
			mGameStatus.np = 0;
			placeTextFields();
			placeButtons();
			mMaxBetBtn = searchBtn("bet", mMaxBet.toString());
			mMaxLineBtn = searchBtn("line", mMaxLine.toString())
			setCurrentBtn(searchBtn("bet", "1"), "bet")
			setCurrentBtn(searchBtn("line", "1"), "line")
			addEventListener(MouseEvent.MOUSE_DOWN, carryOutFunction)
		}
		
		//----------------------------------------
		//GETTERS AND SETTORS
		//----------------------------------------
		public function get gameStatus():Object
		{
			return mGameStatus;
		}
		//----------------------------------------
		//PUBLIC METHODS
		//----------------------------------------
		
		////
		// Clean up is never called since there is no end game button.  But it's here for the future
		////		
		public function cleanup():void 
		{  
			removeEventListener(MouseEvent.MOUSE_DOWN, carryOutFunction);
			var util:QuickFunctions = new QuickFunctions ();
			util.removeChildren(this);
		}
		
		////
		// updates the display of the jackpot nubmer
		////
		public function updateJackpot():void
		{
			updateVariousNumber ("jackpotNum", mGameStatus.jackpot.toString(), "IDS_HTML_OPEN_CENTER")
		}
		
		////
		// updates the display of the won np nubmer (after the slots come to stop)
		////
		public function updateWon():void
		{
			updateVariousNumber ("wonNum", mGameStatus.won.toString())
		}
		
		////
		// updates the display of user's total NP
		////
		public function updateNp():void
		{
			updateVariousNumber ("npNum", mGameStatus.np.toString(), "IDS_HTML_OPEN_CENTER")
		}
		
		////
		// when a user wins NP, np will increase over time (just a display gimmick)
		////
		public function updateNpInTime():void
		{
			var tf:TextField = MovieClip(getChildByName("npNum")).textField
			var currNum:int = int(tf.text)
			var difference:int = int(mGameStatus.np) - currNum
			mNPInc = Math.abs(Math.ceil(difference / 60))
			trace ("increments", mNPInc)
			addEventListener(Event.ENTER_FRAME, catchUpToRealNp);
		}
		
		//----------------------------------------
		//PRIVATE METHODS
		//----------------------------------------
		
		
		////
		// Places all the necessary buttons (bet, lines, play, max bet, music and sound buttons)
		// The data is retrieved from config XML
		////
		private function placeButtons ():void {
				
			var xml:XMLList = mMainGame.configXML.GAME
			var betArray:Array = xml.bet.@values.split("||");
			var lineArray:Array = xml.lines.@values.split("||");
			
			mMaxBet = betArray[betArray.length -1]
			mMaxLine = lineArray[lineArray.length -1]
			
			for (var i:int = 0; i < betArray.length; i++)
			{
				placeBetButton(
							   "BetButton", 
							   "bet", 
							   betArray[i], 
							   Number(xml.bet.@x) + Number(xml.bet.@xgap) *i, 
							   Number(xml.bet.@y)
							   )
			}
			
			for (var j:int = 0; j < lineArray.length; j++)
			{
				placeLineButton(
								"LineButton", 
								"line", 
								lineArray[j], 
								Number(xml.lines.@x) +  Number(xml.lines.@xgap) *j, 
								Number(xml.lines.@y)
								)
			}
			
			placePresetButton(
							  "PlayButton", 
							  "play", 
							  xml.playBtn.@x, 
							  xml.playBtn.@y, 
							  mMainGame.system.getFlashParam("sLang")
							  )
			
			placePresetButton(
							  "MaxButton", 
							  "max", 
							  xml.maxBtn.@x, 
							  xml.maxBtn.@y, 
							  mMainGame.system.getFlashParam("sLang")
							  )
			
			placeToggleButton(
							  "MusicToggleButton", 
							  "music", 
							  xml.musicBtn.@x, 
							  xml.musicBtn.@y, 
							  mMainGame.musicOn
							  )

			placeToggleButton(
							  "SoundToggleButton", 
							  "sound", 
							  xml.soundBtn.@x, 
							  xml.soundBtn.@y, 
							  mMainGame.soundOn)
		}
		
		
		////
		// defult function for setting a button:  not currently used
		////
		private function placeButton (
									  pBtnClass:String, 
									  pName:String, 
									  pValue:String, 
									  px:Number, 
									  py:Number
									  ):void 
		{
			var btnClass:Class = mMainGame.assetInfo.getDefinition(pBtnClass)
			var	btn:MovieClip = new btnClass ();
			btn.name = pName
			btn.x = px
			btn.y = py
			btn.buttonMode = true;
			addChild(btn)
		}
		
		
		////
		// For artistic rasons, the artist made buttwon with each language drawn 
		// instead of creating the text dynamically. so it accounts for that
		//	
		//	@PARAM		pBtnClass		Export class name from the asset library
		//	@PARAM		pName			Name of the button
		//	@PARAM		px				x position
		//	@PARAM		py				y position
		//	@PARAM		language		FlashParam (the current languag setting from gaming system)
		//
		////
		private function placePresetButton (
											pBtnClass:String, 
											pName:String, 
											px:Number, 
											py:Number, 
											language:String
											):void 
		{
			var btnClass:Class = mMainGame.assetInfo.getDefinition(pBtnClass)
			var	btn:MovieClip = new btnClass ();
			btn.name = pName
			btn.x = px
			btn.y = py
			btn.buttonMode = true;
			btn.gotoAndStop(language.toUpperCase())
			btn.button.mouseEnabled = false;
			addChild(btn)
		}
		
		////
		//	Deals with "on" or "off" display setting of the button (music, sound etc.)
		//	The actual control of the sound and music happens at the main game level "mMainGame.musicOn"
		//	
		//	@PARAM		pBtnClass		Export class name from the asset library
		//	@PARAM		pName			Name of the button
		//	@PARAM		px				x position
		//	@PARAM		py				y position
		//	@PARAM		pb				is "on" or "off"
		////
		private function placeToggleButton (
											pBtnClass:String, 
											pName:String, 
											px:Number, 
											py:Number, 
											pb:Boolean = true
											):void 
		{
			var btnClass:Class = mMainGame.assetInfo.getDefinition(pBtnClass)
			var	btn:MovieClip = new btnClass ();
			btn.name = pName
			btn.x = px
			btn.y = py
			btn.scaleX = btn.scaleY = .5
			btn.buttonMode = true;
			pb? btn.gotoAndStop("on"): btn.gotoAndStop("off");			
			addChild(btn)
		}
		
		
		////
		// 	places bet buttons with assigned value (bet)
		//	
		//	@PARAM		pBtnClass		Export class name from the asset library
		//	@PARAM		pName			Name of the button
		//	@PARAM		pValue			line value/num of lines
		//	@PARAM		px				x position
		//	@PARAM		py				y position
		////
		private function placeBetButton (
										 pBtnClass:String, 
										 pName:String, 
										 pValue:String, 
										 px:Number, 
										 py:Number
										 ):void 
		{
			var btnClass:Class = mMainGame.assetInfo.getDefinition(pBtnClass)
			var	btn:MovieClip = new btnClass ();
			btn.name = pName+"_" + pValue
			btn.x = px
			btn.y = py
			btn.button.btnText.text = pValue
			btn.buttonMode = true;
			btn.button.btnText.mouseEnabled = false
			btn.button.mouseEnabled = false
			btn.button.button.mouseEnabled = false
			btn.button.gotoAndStop("off")
			addChild(btn)
		}
		
		
		////
		// 	For artistic rasons, the artist made a button with each line number drawn. 
		//	
		//	@PARAM		pBtnClass		Export class name from the asset library
		//	@PARAM		pName			Name of the button
		//	@PARAM		pValue			line value/num of lines
		//	@PARAM		px				x position
		//	@PARAM		py				y position
		////
		private function placeLineButton (
										  pBtnClass:String, 
										  pName:String, 
										  pValue:String, 
										  px:Number, 
										  py:Number
										  ):void 
		{
			var btnClass:Class = mMainGame.assetInfo.getDefinition(pBtnClass)
			var	btn:MovieClip = new btnClass ();
			btn.name = pName+"_" + pValue
			btn.x = px
			btn.y = py
			btn.buttonMode = true;
			btn.offButton.mouseEnabled = false
			btn.onButton.mouseEnabled = false
			btn.offButton.gotoAndStop(pValue)
			btn.onButton.gotoAndStop(pValue)
			btn.onButton.visible = false
			addChild(btn)
			
			
		}
		
		////
		// 	Everytime when any buttons are clicked, mGameStatus is updated and the event is dispatched
		//	Slotmachine Core class is listening for this to excute appropriate actions
		////
		private function dispatchUpdate():void
		{
			dispatchEvent(new Event ("statusUpdate"))
		}

		////
		// 	function to places all the texts for the game
		////
		private function placeTextFields():void
		{
			
			var xml:XMLList = mMainGame.configXML.GAME
			var betText:String = mMainGame.system.getTranslation("IDS_GAME_BET_TEXT");
			var lineText:String = mMainGame.system.getTranslation("IDS_GAME_LINE_TEXT");
			var totalBetText:String = mMainGame.system.getTranslation("IDS_GAME_TOTAL_BET_TEXT");
			var npText:String = mMainGame.system.getTranslation("IDS_GAME_NP_TEXT");
			var jackText:String = mMainGame.system.getTranslation("IDS_GAME_JACKPOT_TEXT");
			var wonText:String = mMainGame.system.getTranslation("IDS_GAME_WON_TEXT");
			//
			var jackpotTitleClass:Class = mMainGame.assetInfo.getDefinition("JackpotTitle")
			var jackpotTitle:MovieClip = new jackpotTitleClass ();
			jackpotTitle.x = 318
			jackpotTitle.y = 19
			jackpotTitle.gotoAndStop(mMainGame.system.getFlashParam("sLang").toUpperCase());
			addChild(jackpotTitle)
			//
			placeTextField(
						   "headerFont", 
						   "bets", 
						   betText, 
						   xml.betTxt.@x, 
						   xml.betTxt.@y, 
						   xml.betTxt.@width
						   );
			
			placeTextField(
						   "headerFont",
						   "lines", 
						   lineText, 
						   xml.linesTxt.@x, 
						   xml.linesTxt.@y, 
						   xml.linesTxt.@width
						   );
			
			placeTextField(
						   "headerFont",
						   "totalBet", 
						   totalBetText, 
						   xml.totalTxt.@x, 
						   xml.totalTxt.@y, 
						   xml.totalTxt.@width
						   );
			
			placeTextField(
						   "headerFont",
						   "np", 
						   npText, 
						   xml.npTxt.@x, 
						   xml.npTxt.@y, 
						   xml.npTxt.@width
						   );
			
			placeTextField(
						   "headerFont",
						   "won", 
						   wonText, 
						   xml.wonTxt.@x, 
						   xml.wonTxt.@y, 
						   xml.wonTxt.@width
						   );
			
			placeTextField(
						   "headerFont",
						   "totalBetNum", 
						   htmlText(mGameStatus.totalBet.toString()), 
						   xml.totalNum.@x, 
						   xml.totalNum.@y, 
						   xml.totalNum.@width
						   );
			
			placeTextField(
						   "headerFont",
						   "jackpotNum", 
						   htmlText(mGameStatus.jackpot.toString(), "IDS_HTML_OPEN_CENTER"), 
						   xml.jackpotNum.@x, 
						   xml.jackpotNum.@y, 
						   xml.jackpotNum.@width
						   );
			
			placeTextField(
						   "headerFont",
						   "npNum", 
						   htmlText(mGameStatus.np.toString(), "IDS_HTML_OPEN_CENTER"), 
						   xml.npNum.@x, 
						   xml.npNum.@y, 
						   xml.npNum.@width
						   );
			
			placeTextField(
						   "headerFont",
						   "wonNum", 
						   htmlText(mGameStatus.won.toString()), xml.wonNum.@x, 
						   xml.wonNum.@y, 
						   xml.wonNum.@width
						   );			
		}
		
		////
		// 	turns regular string (words or number) into html wrapped text.
		//	just so that it can work with our system
		//	
		//	@PARAM		pText		Text that needs to be wrapped in html tags
		//	@PARAM		openingTag	Look under the translation files for various opening tags
		////
		private function htmlText(pText:String, openingTag:String = "IDS_HTML_OPEN_LEFT"):String
		{
			var openString:String = mMainGame.system.getTranslation(openingTag);
			var closeString:String = mMainGame.system.getTranslation("IDS_HTML_OPEN_LEFT");
			var htmlString:String = openString + pText + closeString;
			return htmlString
		}
		
		
		////
		// 	places text filed on the stage
		//	
		//	@PARAM		pFont		name of the font (what is added to the gaming system)
		//	@PARAM		pName		name of this text box
		//	@PARAM		pText		this should be html tagged text
		//	@PARAM		pWidth		The width of the text field
		////
		private function placeTextField (
										 pFont:String, 
										 pName:String, 
										 pText:String, 
										 px:Number, 
										 py:Number, 
										 pWidth:Number
										 ):void
		{
			var textBoxClass:Class = mMainGame.assetInfo.getDefinition("TextBox") as Class
			var textBox:MovieClip = new textBoxClass ()
			textBox.x = px;
			textBox.y = py;
			textBox.textField.width = pWidth;
			textBox.textField.autoSize = TextFieldAutoSize.LEFT;
			textBox.name = pName
			mMainGame.setText(pFont, textBox.textField, pText)
			addChild (textBox)
		}		
		
		////
		// 	if button clicked is one of the line or bet buttons, when ever is clicked 
		// 	then it becomes the current bet or line mGameStatus is updated 
		//	
		//	@PARAM		pBtn		The btn MC that is clicked
		//	@PARAM		pKind		accounts for either bet or line
		////
		private function setCurrentBtn(pBtn:MovieClip, pKind:String):void
		{
			if (pKind == "bet")
			{
				if (mCurrentBet != null) mCurrentBet.button.gotoAndStop("off");
				mCurrentBet = pBtn
				pBtn.button.gotoAndStop("on")
			}
			else if (pKind == "line")
			{
				if (mCurrentLine != null)
				{
					mCurrentLine.onButton.visible = false
					mCurrentLine.offButton.visible = true
				}
				mCurrentLine = pBtn
				mCurrentLine.onButton.visible = true
				mCurrentLine.offButton.visible = false
			}
			
		}
		
		
		////
		// 	Returns a button if you give the name and the value (used for looking bet or line button)
		//	
		//	@PARAM		pName		Name of teh button. (*all bet and line buttons are named bet or line)
		//	@PARAM		pValue		Thus value of teh button is needed to isolate a single bet or line btn.
		////
		private function searchBtn(pName:String, pValue:String):MovieClip
		{
			var btnName:String = pName+"_"+pValue;
			
			var num:int = this.numChildren
			for (var i:int = 0; i < num; i++)
			{
				var child:MovieClip = MovieClip(getChildAt(i))
				if (child.name == btnName) return child;
			}
			return null;
			
		}
		
		////
		// 	general function to update any numbers on the display UI (user NP, jackpot, NP won, bet, etc.)
		//	
		//	@PARAM		pTf			Name of the textfield
		//	@PARAM		pValue		What the text should be
		//	@PARAM		pOpeningTag	To wrap this in html text setting
		////
		private function updateVariousNumber(
											 pTf:String, 
											 pValue:String, 
											 pOpeningTag:String = "IDS_HTML_OPEN_LEFT"
											 ):void
		{
			var tf:TextField = MovieClip(getChildByName(pTf)).textField
			var htmlString:String = htmlText(pValue, pOpeningTag)
			//trace (htmlString)
			mMainGame.setText("headerFont", tf, htmlString)
		}
		
		private function updateVariousNumber2(
											  pTf:String, 
											  pValue:String, 
											  pOpeningTag:String = "IDS_HTML_OPEN_LEFT"
											  ):void
		{
			var tf:TextField = MovieClip(getChildByName(pTf)).textField
			
			var htmlString:String = htmlText(pValue, pOpeningTag)
			//trace (htmlString)
			mMainGame.setText("headerFont", tf, htmlString)
		}
		
		
		////
		// 	update the displayed total bet based on actual total bet
		////
		private function upDateTotal():void
		{
			mGameStatus.totalBet = mGameStatus.bet * mGameStatus.lines;
			updateVariousNumber("totalBetNum", mGameStatus.totalBet.toString())
		}
		
		
		////
		// 	if total user NP display is in the middle of changing (user wins NP, NP display is incremented
		//	by small amount), it is stoped and user NP display is updated to what it should be 
		////
		private function setNp():void
		{
			if (hasEventListener(Event.ENTER_FRAME))removeEventListener(Event.ENTER_FRAME, catchUpToRealNp);
			updateNp()
			
		}
		
		////
		// 	After each turn, NP won is set to zero
		////
		private function setWon():void
		{
			
			mGameStatus.won = 0
			updateWon()
			
		}
		
		//----------------------------------------
		//EVENT LISTENERS
		//----------------------------------------
		
		////
		// 	based on what button is clicked, it carries out various actions
		//	but mainly it udpates mGameStatus (except for music and sound btns)
		////
		private function carryOutFunction (evt:MouseEvent):void {
			if (mGameStatus.abled) {
				var btnName:String = evt.target.name
				var divider:int = btnName.search("_")
				var btnKind:String = divider != -1? btnName.slice(0, divider): btnName;
				switch (btnKind)
				{
					case "bet":
						setNp()
						setWon()
						mMainGame.playThisSound(mMainGame.soundBank.button, mMainGame.soundOn);
						mGameStatus.bet = int(evt.target.button.btnText.text) 
						setCurrentBtn(MovieClip(evt.target), "bet")
						upDateTotal();
						dispatchUpdate()
						break;
						
					case "line":
						setNp()
						setWon()
						mMainGame.playThisSound(mMainGame.soundBank.button, mMainGame.soundOn);
						mGameStatus.lines = int(btnName.slice(divider+1,btnName.length)) 
						setCurrentBtn(MovieClip(evt.target), "line")
						upDateTotal();
						dispatchUpdate()
						break
						
					case "play":
						setNp()
						setWon()
						mMainGame.playThisSound(mMainGame.soundBank.button, mMainGame.soundOn);
						mGameStatus.playSlot = true
						dispatchUpdate()
						break;
					
					case "max":
						setNp()
						setWon()
						mMainGame.playThisSound(mMainGame.soundBank.button, mMainGame.soundOn);
						mGameStatus.bet = mMaxBet;
						mGameStatus.lines = mMaxLine;
						mGameStatus.playSlot = true
						setCurrentBtn(mMaxBetBtn, "bet")
						setCurrentBtn(mMaxLineBtn, "line")
						upDateTotal()
						dispatchUpdate()
						break;
						
					case "end":
						setNp()
						setWon()
						mGameStatus.gameEnd = true;
						dispatchUpdate()
						break;
					
					case "music":
						setNp()
						setWon()
						mMainGame.playThisSound(mMainGame.soundBank.button, mMainGame.soundOn);
						if (mMainGame.musicOn)
						{
							mMainGame.musicOn = false
							evt.target.gotoAndStop("off")
						}
						else 
						{
							mMainGame.musicOn = true
							evt.target.gotoAndStop("on")
						}
						mMainGame.dispatchEvent(new Event("updateMusicStatus"))
						break;
					
					case "sound":
						setNp()
						setWon()
						mMainGame.playThisSound(mMainGame.soundBank.button, mMainGame.soundOn);
						if (mMainGame.soundOn)
						{
							mMainGame.soundOn = false
							evt.target.gotoAndStop("off")
						}
						else 
						{
							mMainGame.soundOn = true
							evt.target.gotoAndStop("on")
						}
						break;
				}
			}
		}
		
		
		
		////
		// 	should a user win NP, this is a display gimmick so it looks like user's NP is being added on
		//	in small increments over time.
		////
		private function catchUpToRealNp(evt:Event):void
		{
			//
			var tf:TextField = MovieClip(getChildByName("npNum")).textField
			var currNum:int = int(tf.text)
			if (currNum >= mGameStatus.np) 
			{
				setNp();
			}
			else 
			{
				currNum += mNPInc
				updateVariousNumber ("npNum", currNum.toString(), "IDS_HTML_OPEN_CENTER")
			}
		}
	}
	
}