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

package com.game.view {
	import BO.GameBO;
	import BO.HexagonBO;
	import BO.WallBO;
	import BO.WallCoreBO;

	import com.game.constant.HexagonDisplayProperties;
	import com.game.constant.HexagonOwnerType;
	import com.game.constant.MouseCursorType;
	import com.game.data.manager.WallManager;
	import com.game.view.mouse.AbstractMouseCursor;
	import com.game.view.mouse.MouseCursor;
	import com.utils.hexagon.drawHexagon;

	import flash.display.Graphics;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.geom.Point;

	/**
	 * @author renaud.cousin
	 */
	public class Hexagon extends Sprite {
		public var hexagonBO:HexagonBO;
		
		private var zone:Sprite;
		private var strokeContainer:Sprite;
		private var designContainer:Sprite;
		private var designMask:Sprite;
		private var container:Sprite;
		
		private var size:int;
		private var clickEnabled:Boolean;

		public function Hexagon(bo:HexagonBO) {
			addEventListener(Event.ADDED_TO_STAGE, onAddedToStage);
			hexagonBO = bo;
		}
		
		
		//----------------------------------------------------------------------
		// E V E N T S
		//----------------------------------------------------------------------

		private function onAddedToStage(event:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, onAddedToStage);
			
			create();
			
			// XXX XXX XXX
			active();
			// END XXX XXX XXX
		}

		private function onOverZone(event:MouseEvent):void {
			var gameBo:GameBO = GameBO.getInstance();
			clickEnabled = (!occupied && ownerNumber == (HexagonOwnerType.NO_OWNER || gameBo.currentPlayer.playerNumber)) || ownerNumber == gameBo.currentPlayer.playerNumber;
			
			var cursor:AbstractMouseCursor = MouseCursor.getCursor(MouseCursorType.CURSOR_WALL, clickEnabled);
			
			cursor.x = x;
			cursor.y = y;
			GameBO.getInstance().map.currentCursor = cursor;
		}

		private function onClickZone(event:MouseEvent):void {
			if(clickEnabled){
				var wall:Wall = new Wall();
				var wallBo:WallBO = new WallBO();
				var wallCore:WallCoreBO = new WallCoreBO();
				wallCore.position = hexagonBO.position;
				wall.rotation = wallCore.orientation = GameBO.getInstance().map.currentCursor.picto.rotation;
				wallCore.owner = GameBO.getInstance().currentPlayer;
				wallBo.core = wallCore;
				wall.wallBo = wallBo;
				var p:Point = this.parent.localToGlobal(new Point(x, y));
				wall.x = p.x;
				wall.y = p.y;
				
				WallManager.getInstance().addWall(wall);
			}
		}
		
		
		//----------------------------------------------------------------------
		// P R I V A T E
		//----------------------------------------------------------------------
		
		private function create():void{
			size = HexagonDisplayProperties.SIZE;
			var g:Graphics;
			
			designContainer = new Sprite();
			designContainer.addChild(hexagonBO.content.animationSprite);
			addChild(designContainer);
			
			designMask = new Sprite();
			g = designMask.graphics;
			g.beginFill(0xFF0000);
			drawHexagon(g, size +1);
			g.endFill();
			addChild(designMask);
			designContainer.mask = designMask;
			
			container = new Sprite();
			addChild(container);
			
			if(HexagonDisplayProperties.HAS_STROKE){
				strokeContainer = new Sprite();
				g = strokeContainer.graphics;
				g.lineStyle(HexagonDisplayProperties.STROKE_WEIGHT, HexagonDisplayProperties.STROKE_COLOR, HexagonDisplayProperties.STROKE_ALPHA);
				drawHexagon(g, size);
				strokeContainer.mouseChildren = false;
				strokeContainer.mouseEnabled = false;
				addChild(strokeContainer);
			}
			
			zone = new Sprite();
			g = zone.graphics;
			g.beginFill(0xFF0000);
			drawHexagon(g, size);
			g.endFill();
			zone.alpha = 0;
			addChild(zone);
		}
		
		
		//----------------------------------------------------------------------
		// P U B L I C
		//----------------------------------------------------------------------
		
		public function active():void{
			zone.mouseChildren = false;
			zone.buttonMode = true;
			zone.addEventListener(MouseEvent.CLICK, onClickZone);
			zone.addEventListener(MouseEvent.ROLL_OVER, onOverZone);
		}
		
		public function desactive():void{
			zone.buttonMode = false;
			zone.removeEventListener(MouseEvent.CLICK, onClickZone);
			zone.removeEventListener(MouseEvent.ROLL_OVER, onOverZone);
		}
		
		public function kill():void{
			
		}
		
		
		
		//----------------------------------------------------------------------
		// G E T T E R / S E T T E R
		//----------------------------------------------------------------------
		
		public function get position():Point{
			return hexagonBO.position;
		}
		
		public function get occupied():Boolean{
			return hexagonBO.occupied;
		}
		
		public function get ownerNumber():int{
			return hexagonBO.ownerNumber;
		}
	}
}