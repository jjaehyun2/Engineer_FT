package org.flixel
{
	import flash.events.MouseEvent;
	
	/**
	 * A simple button class that calls a function when clicked by the mouse.
	 * 
	 * @author	Adam Atomic
	 */
	public class FlxButton extends FlxSprite
	{
  [Embed(source="data/vis/bounds.png", mimeType="application/octet-stream")] static public var ImgBounds:Class;
		//[Embed(source="data/button.png")] protected var ImgDefaultButton:Class;
		[Embed(source="data/beep.mp3")] static public var SndBeep:Class;
		
		/**
		 * Used with public variable <code>status</code>, means not highlighted or pressed.
		 */
		static public var NORMAL:uint = 0;
		/**
		 * Used with public variable <code>status</code>, means highlighted (usually from mouse over).
		 */
		static public var HIGHLIGHT:uint = 1;
		/**
		 * Used with public variable <code>status</code>, means pressed (usually from mouse click).
		 */
		static public var PRESSED:uint = 2;
		
		/**
		 * The text that appears on the button.
		 */
		public var label:FlxText;
		/**
		 * Controls the offset (from top left) of the text from the button.
		 */
		public var labelOffset:FlxPoint;
		/**
		 * This function is called when the button is released.
		 * We recommend assigning your main button behavior to this function
		 * via the <code>FlxButton</code> constructor.
		 */
		public var onUp:Function;
		/**
		 * This function is called when the button is pressed down.
		 */
		public var onDown:Function;
		/**
		 * This function is called when the mouse goes over the button.
		 */
		public var onOver:Function;
		/**
		 * This function is called when the mouse leaves the button area.
		 */
		public var onOut:Function;
		/**
		 * Shows the current state of the button.
		 */
		public var status:uint;
		/**
		 * Set this to play a sound when the mouse goes over the button.
		 * We recommend using the helper function setSounds()!
		 */
		public var soundOver:FlxSound;
		/**
		 * Set this to play a sound when the mouse leaves the button.
		 * We recommend using the helper function setSounds()!
		 */
		public var soundOut:FlxSound;
		/**
		 * Set this to play a sound when the button is pressed down.
		 * We recommend using the helper function setSounds()!
		 */
		public var soundDown:FlxSound;
		/**
		 * Set this to play a sound when the button is released.
		 * We recommend using the helper function setSounds()!
		 */
		public var soundUp:FlxSound;

		/**
		 * Used for checkbox-style behavior.
		 */
		protected var _onToggle:Boolean;
		
		/**
		 * Tracks whether or not the button is currently pressed.
		 */
		protected var _pressed:Boolean;
		/**
		 * Whether or not the button has initialized itself yet.
		 */
		protected var _initialized:Boolean;
		
		/**
		 * Creates a new <code>FlxButton</code> object with a gray background
		 * and a callback function on the UI thread.
		 * 
		 * @param	X			The X position of the button.
		 * @param	Y			The Y position of the button.
		 * @param	Label		The text that you want to appear on the button.
		 * @param	OnClick		The function to call whenever the button is clicked.
		 */
		public function FlxButton(X:Number=0,Y:Number=0,Label:String=null,OnClick:Function=null)
		{
			super(X,Y);
			if(Label != null)
			{
				label = new FlxText(0,0,80,Label);
				label.setFormat(null,8,0x333333,"center");
				labelOffset = new FlxPoint(-1,3);
			}
			//loadGraphic(ImgDefaultButton,true,false,80,20);
			
			onUp = OnClick;
			onDown = null;
			onOut = null;
			onOver = null;
			
			soundOver = null;
			soundOut = null;
			soundDown = null;
			soundUp = null;

			status = NORMAL;
			_onToggle = false;
			_pressed = false;
			_initialized = false;
		}
		
		/**
		 * Called by the game state when state is changed (if this object belongs to the state)
		 */
		override public function destroy():void
		{
			if(FlxG.stage != null)
				FlxG.stage.removeEventListener(MouseEvent.MOUSE_UP, onMouseUp);
			if(label != null)
			{
				label.destroy();
				label = null;
			}
			onUp = null;
			onDown = null;
			onOut = null;
			onOver = null;
			if(soundOver != null)
				soundOver.destroy();
			if(soundOut != null)
				soundOut.destroy();
			if(soundDown != null)
				soundDown.destroy();
			if(soundUp != null)
				soundUp.destroy();
			super.destroy();
		}
		
		/**
		 * Since button uses its own mouse handler for thread reasons,
		 * we run a little pre-check here to make sure that we only add
		 * the mouse handler when it is actually safe to do so.
		 */
		override public function preUpdate():void
		{
			super.preUpdate();
			
			if(!_initialized)
			{
				if(FlxG.stage != null)
				{
					FlxG.stage.addEventListener(MouseEvent.MOUSE_UP, onMouseUp);
					_initialized = true;
				}
			}
		}
		
		/**
		 * Called by the game loop automatically, handles mouseover and click detection.
		 */
		override public function update():void
		{
			updateButton(); //Basic button logic

			//Default button appearance is to simply update
			// the label appearance based on animation frame.
			//if(label == null)
				return;/*
			switch(frame)
			{
				case HIGHLIGHT:	//Extra behavior to accomodate checkbox logic.
					label.alpha = 1.0;
					break;
				case PRESSED:
					label.alpha = 0.5;
					label.y++;
					break;
				case NORMAL:
				default:
					label.alpha = 0.8;
					break;
			}*/
		}
		
		/**
		 * Basic button update logic
		 */
		protected function updateButton():void
		{
			//Figure out if the button is highlighted or pressed or what
			// (ignore checkbox behavior for now).
			if(FlxG.mouse.visible)
			{
				if(cameras == null)
					cameras = FlxG.cameras;
				var camera:FlxCamera;
				var i:uint = 0;
				var l:uint = cameras.length;
				var offAll:Boolean = true;
				while(i < l)
				{
					camera = cameras[i++] as FlxCamera;
					FlxG.mouse.getWorldPosition(camera,_point);
					if(overlapsPoint(_point,true,camera))
					{
						offAll = false;
						if(FlxG.mouse.justPressed())
						{
							status = PRESSED;
							if(onDown != null)
								onDown();
							if(soundDown != null)
								soundDown.play(true);
						}
						if(status == NORMAL)
						{
							status = HIGHLIGHT;
							if(onOver != null)
								onOver();
							if(soundOver != null)
								soundOver.play(true);
						}
					}
				}
				if(offAll)
				{
					if(status != NORMAL)
					{
						if(onOut != null)
							onOut();
						if(soundOut != null)
							soundOut.play(true);
					}
					status = NORMAL;
				}
			}
		
			//Then if the label and/or the label offset exist,
			// position them to match the button.
			if(label != null)
			{
				label.x = x;
				label.y = y;
			}
			if(labelOffset != null)
			{
				label.x += labelOffset.x;
				label.y += labelOffset.y;
			}
			
			//Then pick the appropriate frame of animation
			/*if((status == HIGHLIGHT) && _onToggle)
				frame = NORMAL;
			else
				frame = status;*/
		}
		
		/**
		 * Just draws the button graphic and text label to the screen.
		 */
		override public function draw():void
		{
			super.draw();
			if(label != null)
			{
				label.scrollFactor = scrollFactor;
				label.cameras = cameras;
				label.draw();
			}
		}
		
		/**
		 * Updates the size of the text field to match the button.
		 */
		override protected function resetHelpers():void
		{
			super.resetHelpers();
			if(label != null)
				label.width = width;
		}
		
		/**
		 * Set sounds to play during mouse-button interactions.
		 * These operations can be done manually as well, and the public
		 * sound variables can be used after this for more fine-tuning,
		 * such as positional audio, etc.
		 * 
		 * @param SoundOver			What embedded sound effect to play when the mouse goes over the button. Default is null, or no sound.
		 * @param SoundOverVolume	How load the that sound should be.
		 * @param SoundOut			What embedded sound effect to play when the mouse leaves the button area. Default is null, or no sound.
		 * @param SoundOutVolume	How load the that sound should be.
		 * @param SoundDown			What embedded sound effect to play when the mouse presses the button down. Default is null, or no sound.
		 * @param SoundDownVolume	How load the that sound should be.
		 * @param SoundUp			What embedded sound effect to play when the mouse releases the button. Default is null, or no sound.
		 * @param SoundUpVolume		How load the that sound should be.
		 */
		public function setSounds(SoundOver:Class=null, SoundOverVolume:Number=1.0, SoundOut:Class=null, SoundOutVolume:Number=1.0, SoundDown:Class=null, SoundDownVolume:Number=1.0, SoundUp:Class=null, SoundUpVolume:Number=1.0):void
		{
			if(SoundOver != null)
				soundOver = FlxG.loadSound(SoundOver, SoundOverVolume);
			if(SoundOut != null)
				soundOut = FlxG.loadSound(SoundOut, SoundOutVolume);
			if(SoundDown != null)
				soundDown = FlxG.loadSound(SoundDown, SoundDownVolume);
			if(SoundUp != null)
				soundUp = FlxG.loadSound(SoundUp, SoundUpVolume);
		}
		
		/**
		 * Use this to toggle checkbox-style behavior.
		 */
		public function get on():Boolean
		{
			return _onToggle;
		}
		
		/**
		 * @private
		 */
		public function set on(On:Boolean):void
		{
			_onToggle = On;
		}
		
		/**
		 * Internal function for handling the actual callback call (for UI thread dependent calls like <code>FlxU.openURL()</code>).
		 */
		protected function onMouseUp(event:MouseEvent):void
		{
			if(!exists || !visible || !active || (status != PRESSED))
				return;
			if(onUp != null)
				onUp();
			if(soundUp != null)
				soundUp.play(true);
		}
	}
}