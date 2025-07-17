/* AS3
	Copyright 2007 gotoAndPlay().
*/
package
{
	import com.smartfoxserver.openspace.avatar.IAvatarMovieClip
	import com.smartfoxserver.openspace.events.AvatarEvent
	import flash.display.MovieClip
	import flash.display.Sprite
	import flash.utils.getDefinitionByName
	import flash.text.TextField
	import flash.text.TextFieldAutoSize
	import flash.text.TextFormat
	import flash.utils.*
	import flash.events.TimerEvent
	
	
	/*
	*	Dummy Avatar MovieClip.
	*
	*	@langversion ActionScript 3.0
	*	@playerversion Flash 9.0
	*
	*	@author Paolo Bassino
	*	@since  22.08.2007
	*/
	public class DummyAvatarMovieClip extends MovieClip implements IAvatarMovieClip
	{
		//--------------------------------------
		// CONSTANTS
		//--------------------------------------
		private const ACTION_STAND:String = "stand"
		private const ACTION_WALK:String = "walk"
		private const DIRECTIONS:Array = ["N","NE","E","SE","S","SW","W","NW"]
		private const X_OFFSET:int = -29
		private const Y_OFFSET:int = -72
		private const TEXT_FORMAT:TextFormat = new TextFormat("Verdana", 10, 0xFF0000, true)
		private const TEXT_Y_OFFSET:int = -65
		private const MESSAGE_DURATION:int = 4000
		
		//--------------------------------------
		//  PRIVATE VARIABLES
		//--------------------------------------
		private var _isMyAvatar:Boolean
		private var _avatarName:String
		private var _currentSkin:Object
		private var _currentAction:String
		private var _currentDir:int
		
		private var nameTextField:TextField
		private var highLighter:Sprite
		private var messagesQueue:Array
		private var balloonTimer:Timer
		
		//--------------------------------------
		//  CONSTRUCTOR
		//--------------------------------------
		function DummyAvatarMovieClip()
		{
			super()
			
			// Set defaults
			_isMyAvatar = false
			_avatarName = ""
			_currentSkin = {}
			
			var defaultAction:String = ACTION_STAND
			var defaultDir:int = 6

			var defaultSkin:Object = {}
			defaultSkin.sex = "m"
			defaultSkin.race = "european"
			defaultSkin.hair = ""
			defaultSkin.bust = ""
			defaultSkin.legs = ""
			
			// Display avatar highlighter
			displayHighlight()
			
			// Display avatar name
			displayName()
			
			// Display default avatar
			displayAvatar(defaultSkin, defaultDir, defaultAction)
			
			// Hide chat balloon
			getChildByName("balloon").visible = false
			
			// Start timer to check balloon messages
			balloonTimer = new Timer(1000)
			balloonTimer.addEventListener(TimerEvent.TIMER, onBalloonTimer)
			balloonTimer.start()
		}
		
		//--------------------------------------
		//  GETTER/SETTERS
		//--------------------------------------
		public function set isMyAvatar(myAv:Boolean):void
		{
			_isMyAvatar = myAv
			displayHighlight()
		}
		
		public function set avatarName(avName:String):void
		{
			_avatarName = (avName != null ? avName : "")
			displayName()
		}

		public function get avatarName():String
		{
			return _avatarName
		}
		
		public function get skin():Object
		{
			return _currentSkin
		}
		
		//--------------------------------------
		//  OPENSPACE EVENT HANDLERS
		//--------------------------------------
		
		public function onSkinChange(evt:AvatarEvent):void
		{
			var skin:Object = evt["params"].skin
			
			if (skin != null)
				displayAvatar(skin, _currentDir, _currentAction)
		}
		
		public function onCustomAction(evt:AvatarEvent):void
		{
			var action:Object = evt["params"].action
			
			if (action != null)
				trace ("'onCustomAction' method called on DummyAvatarMovieClip")
		}
		
		public function onMessage(evt:AvatarEvent):void
		{
			var message:String = evt["params"].message
			var isPrivate:Boolean = evt["params"].isPrivate
			
			var balloon:MovieClip = getChildByName("balloon") as MovieClip
			balloon.visible = true
			balloon.tf_msg.autoSize = TextFieldAutoSize.LEFT
			balloon.nextTime = getTimer() + MESSAGE_DURATION
			balloon.tf_msg.text += message + "\t\n"
			updateBalloon()
		}
		
		public function onMovementStart(evt:AvatarEvent):void
		{
			var dir:int = evt["params"].dir
			displayAvatar(_currentSkin, dir, ACTION_WALK)
		}
		
		public function onMovementStop(evt:AvatarEvent):void
		{
			displayAvatar(_currentSkin, _currentDir, ACTION_STAND)
		}
		
		public function onTileEnter(evt:AvatarEvent):void
		{
			// Nothing to do
		}
		
		public function onDirectionChange(evt:AvatarEvent):void
		{
			var dir:int = evt["params"].dir
			
			if (dir != _currentDir)
				displayAvatar(_currentSkin, dir, _currentAction)
		}
		
		public function onDestroy(evt:AvatarEvent):void
		{
			balloonTimer.stop()
			balloonTimer.removeEventListener(TimerEvent.TIMER, onBalloonTimer)
		}
		
		//--------------------------------------
		//  EVENT HANDLERS
		//--------------------------------------
		public function onBalloonTimer(evt:TimerEvent):void
		{
			var balloon:MovieClip = getChildByName("balloon") as MovieClip

			if (getTimer() > balloon.nextTime)
			{
				var txt:String = balloon.tf_msg.text
				txt = txt.substr(txt.indexOf("\t") + 2, txt.length)

				balloon.tf_msg.text = txt
				updateBalloon()

				balloon.nextTime = getTimer() + MESSAGE_DURATION

				if (balloon.tf_msg.text.length == 0)
					balloon.visible = false
			}
		}
		
		//--------------------------------------
		//  PRIVATE & PROTECTED INSTANCE METHODS
		//--------------------------------------
		private function displayHighlight():void
		{
			if (_isMyAvatar == true && highLighter == null)
			{
				highLighter = new highlight()
				addChildAt(highLighter, 0)
				highLighter.x = 0
				highLighter.y = 0
			}
		}
		
		private function displayName():void
		{
			if (nameTextField == null)
			{
				nameTextField = new TextField()
				nameTextField.embedFonts = true
				nameTextField.defaultTextFormat = TEXT_FORMAT
				nameTextField.autoSize = "center"
				addChild(nameTextField)
				nameTextField.x = 0
				nameTextField.y = TEXT_Y_OFFSET
				nameTextField.selectable = false
			}
			
			nameTextField.text = _avatarName + " "
		}
		
		private function displayAvatar(avSkin:Object, dir:int, action:String):void
		{
			var newSex:String = (avSkin.sex != undefined) ? avSkin.sex : _currentSkin.sex
			var newRace:String = (avSkin.race != undefined) ? avSkin.race : _currentSkin.race
			var newHair:String = (avSkin.hair != undefined) ? avSkin.hair : _currentSkin.hair
			var newBust:String = (avSkin.bust != undefined) ? avSkin.bust : _currentSkin.bust
			var newLegs:String = (avSkin.legs != undefined) ? avSkin.legs : _currentSkin.legs
			
			// Display body
			if (newSex != _currentSkin.sex || newRace != _currentSkin.race || action != _currentAction || dir != _currentDir)
			{
				var oldBodyClassName:String = _currentSkin.sex + "_" + _currentSkin.race + "_" + _currentAction
				var newBodyClassName:String = newSex + "_" + newRace + "_" + action
				var bodyMC:MovieClip
				
				if (newBodyClassName != oldBodyClassName)
				{
					if (getChildByName(oldBodyClassName) != null)
						removeChild(getChildByName(oldBodyClassName))
				
					var bodyClass:Class = getDefinitionByName(newBodyClassName) as Class
					bodyMC = new bodyClass() as MovieClip
				
					bodyMC.name = newBodyClassName
					addChild(bodyMC)
					bodyMC.x = X_OFFSET
					bodyMC.y = Y_OFFSET
				}
				else
				{
					bodyMC = getChildByName(oldBodyClassName) as MovieClip
				}
				
				bodyMC.gotoAndPlay(DIRECTIONS[dir])
			}
			
			// Display hair
			if (newHair != _currentSkin.hair || action != _currentAction || dir != _currentDir)
			{
				var oldHairClassName:String = _currentSkin.hair + "_" + _currentAction
				var newHairClassName:String = newHair + "_" + action
				var hairMC:MovieClip
				
				if (newHairClassName != oldHairClassName)
				{
					if (getChildByName(oldHairClassName) != null)
						removeChild(getChildByName(oldHairClassName))
					
					if (newHair != "")
					{
						var hairClass:Class = getDefinitionByName(newHairClassName) as Class
						hairMC = new hairClass() as MovieClip
						
						hairMC.name = newHairClassName
						addChild(hairMC)
						hairMC.x = X_OFFSET
						hairMC.y = Y_OFFSET
					}
				}
				else
				{
					hairMC = getChildByName(oldHairClassName) as MovieClip
				}
				
				if (hairMC != null)
					hairMC.gotoAndPlay(DIRECTIONS[dir])
			}

			// Display bust
			if (newBust != _currentSkin.bust || action != _currentAction || dir != _currentDir)
			{
				var oldBustClassName:String = _currentSkin.bust + "_" + _currentAction
				var newBustClassName:String = newBust + "_" + action
				var bustMC:MovieClip

				if (newBustClassName != oldBustClassName)
				{
					if (getChildByName(oldBustClassName) != null)
						removeChild(getChildByName(oldBustClassName))

					if (newBust != "")
					{
						var bustClass:Class = getDefinitionByName(newBustClassName) as Class
						bustMC = new bustClass() as MovieClip

						bustMC.name = newBustClassName
						addChild(bustMC)
						bustMC.x = X_OFFSET
						bustMC.y = Y_OFFSET
					}
				}
				else
				{
					bustMC = getChildByName(oldBustClassName) as MovieClip
				}

				if (bustMC != null)
					bustMC.gotoAndPlay(DIRECTIONS[dir])
			}
			
			// Display legs
			if (newLegs != _currentSkin.legs || action != _currentAction || dir != _currentDir)
			{
				var oldLegsClassName:String = _currentSkin.legs + "_" + _currentAction
				var newLegsClassName:String = newLegs + "_" + action
				var legsMC:MovieClip

				if (newLegsClassName != oldLegsClassName)
				{
					if (getChildByName(oldLegsClassName) != null)
						removeChild(getChildByName(oldLegsClassName))

					if (newLegs != "")
					{
						var legsClass:Class = getDefinitionByName(newLegsClassName) as Class
						legsMC = new legsClass() as MovieClip

						legsMC.name = newLegsClassName
						addChild(legsMC)
						legsMC.x = X_OFFSET
						legsMC.y = Y_OFFSET
					}
				}
				else
				{
					legsMC = getChildByName(oldLegsClassName) as MovieClip
				}

				if (legsMC != null)
					legsMC.gotoAndPlay(DIRECTIONS[dir])
			}
			
			// Set current params
			_currentSkin.sex = newSex
			_currentSkin.race = newRace
			_currentSkin.hair = newHair
			_currentSkin.bust = newBust
			_currentSkin.legs = newLegs
			_currentAction = action
			_currentDir = dir
		}
	
		private function updateBalloon():void
		{
			var balloon:MovieClip = getChildByName("balloon") as MovieClip
			
			balloon.center.height = balloon.tf_msg.textHeight - 5
			balloon.bottom.y = balloon.center.y + balloon.center.height
			balloon.y = - balloon.height - 50
		}
	}
}