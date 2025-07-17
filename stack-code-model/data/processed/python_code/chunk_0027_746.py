/**
 *
 * Blackhole/Repulsor
 *
 * https://github.com/AbsolutRenal
 *
 * Copyright (c) 2012 AbsolutRenal (Renaud Cousin). All rights reserved.
 * 
 * This ActionScript source code is free.
 * You can redistribute and/or modify it in accordance with the
 * terms of the accompanying Simplified BSD License Agreement.
**/

package test {
	import flash.text.TextFieldAutoSize;
	import flash.text.TextField;
	import flash.events.Event;
	import flash.display.Sprite;

	/**
	 * @author renaud.cousin
	 */
	public class BlackHoleTest extends Sprite {
		public static const RADIUS_EFFECT:uint = 100 ;
		
		private const CENTER_RADIUS:uint = 8;
		private const CENTER_COLOR:uint = 0x008800;
		private const EFFECT_COLOR:uint = 0x77CC33;
		private const INVERT_EFFECT_COLOR:uint = 0xCC5555;
		private const INVERT_CENTER_COLOR:uint = 0xCC0000;
		
		private var centerContainer:Sprite;
		private var zoneContainer:Sprite;
		private var tf:TextField;
		
		private var _gravity:int;
		private var _repulse:Boolean;

		public function BlackHoleTest() {
			init();
		}
		
		
		//----------------------------------------------------------------------
		// E V E N T S
		//----------------------------------------------------------------------

		
		
		//----------------------------------------------------------------------
		// P R I V A T E
		//----------------------------------------------------------------------

		private function init():void {
			zoneContainer = new Sprite();
			addChild(zoneContainer);
			
			centerContainer = new Sprite();
			addChild(centerContainer);
		}

		private function setRepulse():void {
			zoneContainer.graphics.clear();
			centerContainer.graphics.clear();
			
			zoneContainer.graphics.beginFill(INVERT_EFFECT_COLOR);
			zoneContainer.graphics.drawCircle(0, 0, RADIUS_EFFECT);
			zoneContainer.graphics.endFill();
			
			centerContainer.graphics.beginFill(INVERT_CENTER_COLOR);
			centerContainer.graphics.drawCircle(0, 0, CENTER_RADIUS);
			centerContainer.graphics.endFill();
		}
		
		private function setAttract():void{
			zoneContainer.graphics.clear();
			centerContainer.graphics.clear();
			
			zoneContainer.graphics.beginFill(EFFECT_COLOR);
			zoneContainer.graphics.drawCircle(0, 0, RADIUS_EFFECT);
			zoneContainer.graphics.endFill();
			
			centerContainer.graphics.beginFill(CENTER_COLOR);
			centerContainer.graphics.drawCircle(0, 0, CENTER_RADIUS);
			centerContainer.graphics.endFill();
		}
		
		
		//----------------------------------------------------------------------
		// P U B L I C
		//----------------------------------------------------------------------
		
		
		//----------------------------------------------------------------------
		// G E T T E R / S E T T E R
		//----------------------------------------------------------------------
		
		public function set gravity(value:int):void{
			_gravity = value;
			
			tf = new TextField();
			tf.textColor = 0x000000;
			tf.autoSize = TextFieldAutoSize.LEFT;
			tf.text = String(_gravity);
			tf.x = -tf.width / 2;
			tf.y = -tf.height / 2;
			addChild(tf);
		}
		
		public function get gravity():int{
			return _gravity;
		}

		public function get repulse():Boolean {
			return _repulse;
		}

		public function set repulse(value:Boolean):void {
			_repulse = value;
			
			if(_repulse)
				setRepulse();
			else
				setAttract();
		}
	}
}