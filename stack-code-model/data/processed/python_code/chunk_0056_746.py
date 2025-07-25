package Systems
{
	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.events.MouseEvent;
	import flash.events.TouchEvent;
	
	import com.gestureworks.core.GestureWorks;
	import com.gestureworks.core.TouchSprite;
	
	import be.nascom.flash.graphics.Rippler;
	import util.LayerHandler;
	
	/**
	 * Systems.WaterSystem
	 *
	 * Keeps track of the background image and it's corresponding water ripples
	 *
	 * @author Adam Byléhn
	 * @contact adambylehn@hotmail.com
	 */
	
	public class WaterSystem extends Sprite
	{
		// Embed an image which will be used as a background
		[Embed(source = "../../bin/images/bottenbild3.png")]
		private var _sourceImage:Class;
		
		private var _dustEmitter:DustEmitter;
		
		// The "rippler" that instantiates water ripples at the surface 
		private var _rippler:Rippler;
		// The touch object, in this case the entire screen
		private var _touchSprite:TouchSprite;
		
		private var _flockFishes:Fishes;
		
		private var _active:Boolean;
		
		// Constructor
		public function WaterSystem()
		{
			_flockFishes = new Fishes();
			super();
		}
		
		public function Init():void
		{
			// Create the touch object wich will be used as the background for the application
			_touchSprite = new TouchSprite();
			// Fill the touch object with the "background image"
			_touchSprite.graphics.beginBitmapFill(new _sourceImage().bitmapData, null, true, true);
			_touchSprite.graphics.drawRect(0, 0, stage.stageWidth, stage.stageHeight);
			_touchSprite.graphics.endFill();
			
			// Add the touch sprite to the stage
			addChild(_touchSprite);
			setChildIndex(_touchSprite, 0);
			
			// Create the Rippler instance to affect the Bitmap object
			_rippler = new Rippler(_touchSprite, 20, 10);
			
			// Make the TouchSprite listen to the TOUCH_MOVE event
			//_touchSprite.addEventListener(TouchEvent.TOUCH_MOVE, handleDrag);
			stage.addEventListener(TouchEvent.TOUCH_MOVE, handleDrag);
			
			//_touchSprite.addEventListener(MouseEvent.MOUSE_MOVE, handleMouseMove);
			
			_dustEmitter = new DustEmitter(100, stage);
			
			_flockFishes.Init(stage, 16);
		}
		
		public function Update():void
		{
			_flockFishes.Update();
			_rippler.Update();
			_dustEmitter.Update();
		}
		
		private function handleDrag(event:TouchEvent):void
		{
			if (_active)
			{
				_rippler.drawRipple(event.stageX, event.stageY, 20, 1);
				
				var mousePos:Vector2D = new Vector2D(event.stageX, event.stageY);
				_flockFishes.scareFishPos(mousePos);
			}
		}
		
		private function handleMouseMove(event:MouseEvent):void
		{
			/*
			_rippler.drawRipple(event.stageX, event.stageY, 20, 1);
			
			var mousePos:Vector2D = new Vector2D(event.stageX, event.stageY);
			_flockFishes.scareFishPos(mousePos);
			*/
		}
		
		public function Deactivate():void
		{
			_active = false;
			_rippler.destroy();
			_touchSprite.visible = false;
			_dustEmitter.Deactivate();
			
			_flockFishes.Deactivate();
		}
		
		public function Activate():void
		{
			_active = true;
			_rippler = new Rippler(_touchSprite, 20, 10);
			_touchSprite.visible = true;
			_dustEmitter.Activate();
			_flockFishes.Activate();
		}
		
		public function Ripple():void
		{
			_rippler.drawRipple(Math.floor(Math.random() * stage.stageWidth), Math.floor(Math.random() * stage.stageHeight), 20, 1);
		}
	}
}

import flash.display.Sprite;
import flash.display.Stage;

class DustEmitter extends Sprite
{
	private var _particles:Array = new Array();
	private var _groupVelX:Number = .0;
	private var _groupVelY:Number = .0;
	private var _maxVel:uint = 5;
	
	public function DustEmitter(amount:uint, stage:Stage)
	{
		for (var i:int = 0; i < amount; i++)
		{
			_particles.push(new Particle(Math.floor(Math.random() * stage.stageWidth), Math.floor(Math.random() * stage.stageHeight), stage));
		}
	}
	
	public function Update():void
	{
		_groupVelX += Math.random() * 2 - 1;
		_groupVelY += Math.random() * 2 - 1;
		
		if (Math.abs(_groupVelX) > _maxVel)
			_groupVelX = _maxVel;
		if (Math.abs(_groupVelY) > _maxVel)
			_groupVelY = _maxVel;
		
		for (var i:int = 0; i < _particles.length; i++)
		{
			_particles[i].Update(_groupVelX, _groupVelY);
		}
	}
	
	public function Deactivate():void
	{
		for (var i:int = 0; i < _particles.length; i++)
		{
			_particles[i].Deactivate();
		}
	}
	
	public function Activate():void
	{
		for (var i:int = 0; i < _particles.length; i++)
		{
			_particles[i].Activate();
		}
	}
}

import util.LayerHandler;
class Particle extends Sprite
{
	private var _dot:Sprite;
	private var _stageWidth:uint;
	private var _stageHeight:uint;
	
	public function Particle(x:Number, y:Number, stage:Stage):void
	{
		_dot = new Sprite();
		_dot.x = x;
		_dot.y = y;
		_dot.graphics.beginFill(0xFFFFFF, Math.random());
		_dot.graphics.drawRect(0, 0, 1, 1);
		_dot.graphics.endFill();
		stage.addChild(_dot);
		_stageWidth = stage.stageWidth;
		_stageHeight = stage.stageHeight;
	}
	
	public function Update(groupVelX:Number, groupVelY:Number):void
	{
		if (_dot.x > _stageWidth)
			_dot.x = 0;
		else if (_dot.x < 0)
			_dot.x = _stageWidth;
		if (_dot.y > _stageHeight)
			_dot.y = 0;
		else if (_dot.y < 0)
			_dot.y = _stageHeight;
		
		_dot.x += groupVelX * Math.random() + (Math.random() * 2 - 1);
		_dot.y += groupVelY * Math.random() + (Math.random() * 2 - 1);
	}
	
	public function Deactivate():void
	{
		_dot.visible = false;
	}
	
	public function Activate():void
	{
		_dot.visible = true;
		LayerHandler.BRING_TO_FRONT(_dot);
	}
}