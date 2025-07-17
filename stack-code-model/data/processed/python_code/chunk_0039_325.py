package  
{
	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Player extends Ori
	{
		private var _xSpeed:Number = 0;
		private var _ySpeed:Number = 0;
		private const ACCEL:Number = 0.5;
		private const MAX_SPEED:Number = 8;
		
		private var _shotCounter:int = 0;
		private var _shotCounterMax:int = 2; //10;
		
		private var _leftPressed:Boolean = false;
		private var _rightPressed:Boolean = false;
		private var _downPressed:Boolean = false;
		private var _upPressed:Boolean = false;
		private var _mousePressed:Boolean = false;
		
		public function Player() 
		{
			addEventListener(Event.ADDED_TO_STAGE, init);
			filters = [GlowData.OriGlow];
		}
		
		private function init(e:Event):void 
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			
			stage.addEventListener(KeyboardEvent.KEY_UP, kUp);
			stage.addEventListener(KeyboardEvent.KEY_DOWN, kDown);
			stage.addEventListener(MouseEvent.MOUSE_DOWN, mDown);
			stage.addEventListener(MouseEvent.MOUSE_UP, mUp);
		}
		
		private function mUp(e:MouseEvent):void 
		{
			_mousePressed = false;
		}
		
		private function mDown(e:MouseEvent):void 
		{
			_mousePressed = true;
		}
		
		private function kDown(e:KeyboardEvent):void 
		{
			if (e.keyCode == 40 || e.keyCode == 83)	_downPressed = true;
			if (e.keyCode == 37 || e.keyCode == 65)	_leftPressed = true;
			if (e.keyCode == 39 || e.keyCode == 68)	_rightPressed = true;
			if (e.keyCode == 38 || e.keyCode == 87)	_upPressed = true;
		}
		
		private function kUp(e:KeyboardEvent):void 
		{
			if (e.keyCode == 40 || e.keyCode == 83)	_downPressed = false;
			if (e.keyCode == 37 || e.keyCode == 65)	_leftPressed = false;
			if (e.keyCode == 39 || e.keyCode == 68)	_rightPressed = false;
			if (e.keyCode == 38 || e.keyCode == 87)	_upPressed = false;
		}
		
		public function frame():void
		{
			/*
			 * Movement
			 */
			if (_leftPressed) 	_xSpeed -= ACCEL;
			if (_rightPressed) 	_xSpeed += ACCEL;
			if (_upPressed)		_ySpeed -= ACCEL;
			if (_downPressed) 	_ySpeed += ACCEL;
			
			if (_xSpeed >  MAX_SPEED) _xSpeed =  MAX_SPEED;
			if (_ySpeed >  MAX_SPEED) _ySpeed =  MAX_SPEED;
			if (_xSpeed < -MAX_SPEED) _xSpeed = -MAX_SPEED;
			if (_ySpeed < -MAX_SPEED) _ySpeed = -MAX_SPEED;
			
			x += _xSpeed;
			y += _ySpeed;
			
			
			/*
			 * Shooting
			 */
			if (_mousePressed) fire();
		}
		
		private function fire():void 
		{
			_shotCounter++;
			if (_shotCounter > _shotCounterMax)
			{
				_shotCounter = 0;
				
				var shot:PlayerShot = new PlayerShot();
				shot.x = x;
				shot.y = y;
				parent.addChild(shot);
				PlayState.Shots.push(shot);
			}
		}
		
	}

}