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
	import BO.BaseBO;
	import BO.BonusCoreBO;
	import BO.BulletTypeBO;
	import BO.DesignElementBO;
	import BO.GameBO;
	import BO.GridBO;
	import BO.GridCoreBO;
	import BO.HexagonBO;
	import BO.HexagonContentBO;
	import BO.LayoutBO;
	import BO.MapBO;
	import BO.MatchBO;
	import BO.WallBO;

	import com.game.constant.FiringType;
	import com.game.constant.GameInit;
	import com.game.constant.HexagonDataType;
	import com.game.constant.HexagonDisplayProperties;
	import com.game.constant.HexagonOwnerType;
	import com.game.constant.KeyboardControls;
	import com.game.data.HexagonDictionary;
	import com.game.data.MapData;
	import com.game.view.mouse.AbstractMouseCursor;
	import com.utils.hexagon.drawHexagon;
	import com.utils.hexagon.getSafeArea;
	import com.utils.vector.getPointFromIndex;

	import flash.display.MovieClip;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	import flash.geom.Point;
	import flash.ui.Mouse;
	import flash.utils.getDefinitionByName;

	/**
	 * @author renaud.cousin
	 */
	public class Map extends Sprite {
		private var mapData:MapData;
		private var mapBO:MapBO;
		private var grid:Grid;
		private var matchBO:MatchBO;
		
		private var cursorContainer:Sprite;
		private var mouseCursor:Sprite;
		
		private var _currentCursor:AbstractMouseCursor;
		
		private var _wallContainer:Sprite;
		private var _bulletContainer:Sprite;
		

		public function Map(datas:MapData) {
			mapData = datas;
			
			addEventListener(Event.ADDED_TO_STAGE, onAddedToStage);
			
			initMap();
		}
		
		
		//----------------------------------------------------------------------
		// E V E N T S
		//----------------------------------------------------------------------

		private function onAddedToStage(event:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, onAddedToStage);
			
			// XXX XXX
			active();
		}

		private function rollOutMap(event:MouseEvent):void {
			removeEventListener(Event.ENTER_FRAME, onEnterFrame);
			
			if(mouseCursor != null)
				mouseCursor.visible = false;
			
			Mouse.show();
			currentCursor = null;
		}

		private function rollOverMap(event:MouseEvent):void {
			Mouse.hide();
			
			if(mouseCursor != null){
				mouseCursor.visible = true;
				if(!stage.contains(mouseCursor))
					stage.addChild(mouseCursor);
			} else {
				var klass:Class = getDefinitionByName("MapMouseCursor") as Class;
				mouseCursor = new klass() as Sprite;
				mouseCursor.mouseChildren = false;
				mouseCursor.mouseEnabled = false;
				stage.addChild(mouseCursor);
			}
			
			addEventListener(Event.ENTER_FRAME, onEnterFrame);
		}

		private function onEnterFrame(event:Event):void {
			mouseCursor.x = stage.mouseX;
			mouseCursor.y = stage.mouseY;
		}

		private function onKeyboardDown(event:KeyboardEvent):void {
			if(mouseCursor != null){
				if(event.keyCode == KeyboardControls.WALL_ROTATE_LEFT){
					_currentCursor.picto.rotation -= GameInit.WALL_ROTATION_RANGE;
				} else if(event.keyCode == KeyboardControls.WALL_ROTATE_RIGHT){
					_currentCursor.picto.rotation += GameInit.WALL_ROTATION_RANGE;
				}
			}
		}
		
		
		//----------------------------------------------------------------------
		// P R I V A T E
		//----------------------------------------------------------------------
		
		private function initMap():void{
			mapBO = MapBO.getInstance();
			
			matchBO = MatchBO.getInstance();
			
			mapBO.mapElements = createLayout();
			mapBO.grid = createGridData();
			
			matchBO.map = mapBO;
			
			createGrid();
			
			_wallContainer = new Sprite();
			_wallContainer.mouseChildren = false;
			_wallContainer.mouseEnabled = false;
			addChild(_wallContainer);
			
			_bulletContainer = new Sprite();
			_bulletContainer.mouseChildren = false;
			_bulletContainer.mouseEnabled = false;
			addChild(_bulletContainer);
			
			cursorContainer = new Sprite();
			cursorContainer.mouseChildren = false;
			cursorContainer.mouseEnabled = false;
			cursorContainer.x = grid.x;
			cursorContainer.y = grid.y;
			addChild(cursorContainer);
			
			GameBO.getInstance().map = this;
		}
		
		private function createLayout():LayoutBO{
			var layout:LayoutBO = new LayoutBO();
			
			layout.width = mapData.width;
			layout.height = mapData.height;
			
			layout.design = createDesignData();
			layout.bases = createBaseData();
			
			return layout;
		}
		
		private function createDesignData():Vector.<DesignElementBO>{
			var design:Vector.<DesignElementBO> = new Vector.<DesignElementBO>();
			var designElmnt:DesignElementBO;
			var length:uint = mapData.hexagons.length;
			var hexagonBO:HexagonBO;
			var hex:Hexagon;
			var hexContent:HexagonContentBO;
			var klass:Class;
			
			var hexagonDictionary:HexagonDictionary = HexagonDictionary.getInstance();
			var pos:String;
			for(var i:uint = 0; i < length; i++){
				designElmnt = new DesignElementBO();
				
				hexagonBO = new HexagonBO();
				hexagonBO.position = getPointFromIndex(i, mapData.width);
				if(mapData.hexagons[i].type > HexagonDataType.NEUTRAL){
					hexagonBO.occupied = true;
					hexagonBO.ownerNumber = HexagonOwnerType.GAME_OWNER;
				} else {
					hexagonBO.occupied = false;
					hexagonBO.ownerNumber = HexagonOwnerType.NO_OWNER;
				}
				
				designElmnt.type = mapData.hexagons[i].type;
				hex = new Hexagon(hexagonBO);
				pos = hexagonBO.position.x + "x" + hexagonBO.position.y;
				hexagonDictionary.addHexagon(pos, hex);
				
				designElmnt.parentHexagon = hex;
				klass = getDefinitionByName(mapData.hexagons[i].spriteClass) as Class;
				designElmnt.animationSprite = new klass() as MovieClip;
				
				hexContent = new HexagonContentBO();
				hexContent.parentHexagon = hex;
				hexContent.animationSprite = designElmnt.animationSprite;
				hex.hexagonBO.content = hexContent;
				
				design.push(designElmnt);
			}
			return design;
		}
		
		private function createBaseData():Vector.<BaseBO>{
			var bases:Vector.<BaseBO> = new Vector.<BaseBO>();
			var base:BaseBO;
			var bulletType:BulletTypeBO;
			var hexContent:HexagonContentBO;
			var pos:String;
			var p:Point;
			var stroke:Shape;
			var safeAreaColored:Shape;
			var length:uint = matchBO.players.length;
			for(var i:uint = 0; i < length; i++){
				base = new BaseBO();
				base.life = GameInit.LIFE;
				base.orientation = mapData.baseOrientations[i];
//				base.position = mapData.playerPositions[i];
				base.firingRate = GameInit.FIRING_RATE;
				bulletType = new BulletTypeBO();
				bulletType.name = FiringType.FIRE_DEFAULT;
//				bulletType.speed = GameInit.FIRING_RATE;
				bulletType.damage = GameInit.DAMAGE;
				base.firingRate = GameInit.FIRING_RATE;
				base.firingType = bulletType;
				
				base.owner = matchBO.players[i];
				
				base.safeArea = calculateSafeArea(mapData.playerPositions[i]);
				for each (var hex:Hexagon in base.safeArea) {
					hex.hexagonBO.ownerNumber = matchBO.players[i].playerNumber;
					safeAreaColored = new Shape();
					safeAreaColored.graphics.beginFill(matchBO.players[i].bulletsColor);
					drawHexagon(safeAreaColored.graphics, HexagonDisplayProperties.SIZE);
					safeAreaColored.graphics.endFill();
					safeAreaColored.alpha = HexagonDisplayProperties.SAFE_AREA_ALPHA;
				
					hex.hexagonBO.content.animationSprite.addChild(safeAreaColored);
				}
				
				base.activeBonuses = new Vector.<BonusCoreBO>();
//				base.walls = new Vector.<WallBO>();
//				base.nbWalls = 0;
				
				// XXX XXX XXX XXX
				p = mapData.playerPositions[i];
				pos = p.x + "x" + p.y;
				hexContent = HexagonDictionary.getInstance().getHexagon(pos).hexagonBO.content;
				base.parentHexagon = hexContent.parentHexagon;
				base.animationSprite = hexContent.animationSprite;
				
				stroke = new Shape();
				stroke.graphics.lineStyle(HexagonDisplayProperties.HEXAGON_BASE_STROKE_THICKNESS, matchBO.players[i].bulletsColor, HexagonDisplayProperties.HEXAGON_BASE_STROKE_ALPHA);
				drawHexagon(stroke.graphics, HexagonDisplayProperties.SIZE);
				base.animationSprite.addChild(stroke);
				// END XXX XXX XXX XXX
				
				bases.push(base);
			}
			return bases;
		}

		private function calculateSafeArea(p:Point):Vector.<Hexagon> {
			var vect:Vector.<String> = getSafeArea(p, mapBO.safeAreaSize);
			
			var hexagonsDict:HexagonDictionary = HexagonDictionary.getInstance();
			var safeArea:Vector.<Hexagon> = hexagonsDict.getHexagonsVect(vect);
			
			return safeArea;
		}

		private function createGridData():GridBO {
			var gridBO:GridBO = new GridBO();
			
			var nb:uint = mapData.hexagons.length;
			var hexagons:Vector.<HexagonBO> = new Vector.<HexagonBO>();
			var hexagonBO:HexagonBO;
			
			var gridCore:GridCoreBO = new GridCoreBO();
			for (var i:int = 0; i < nb; i++) {
				hexagonBO = mapBO.mapElements.design[i].parentHexagon.hexagonBO;
				
				if(hexagonBO.occupied){
					hexagons.push(hexagonBO);
				}
			}
			
			gridCore.hexagons = hexagons;
			gridBO.core = gridCore;
			
			return gridBO;
		}
		
		private function createGrid():void{
			grid = new Grid(mapBO.mapElements);
			grid.x = 50;
			grid.y = 50;
			addChild(grid);
		}
		
		
		//----------------------------------------------------------------------
		// P U B L I C
		//----------------------------------------------------------------------
		
		public function active():void{
			addEventListener(MouseEvent.ROLL_OVER, rollOverMap);
			addEventListener(MouseEvent.ROLL_OUT, rollOutMap);
			
			stage.addEventListener(KeyboardEvent.KEY_DOWN, onKeyboardDown);
		}
		
		public function desactive():void{
			removeEventListener(MouseEvent.ROLL_OVER, rollOverMap);
			removeEventListener(MouseEvent.ROLL_OUT, rollOutMap);
			
			stage.removeEventListener(KeyboardEvent.KEY_DOWN, onKeyboardDown);
		}
		
		
		//----------------------------------------------------------------------
		// G E T T E R / S E T T E R
		//----------------------------------------------------------------------

		public function get currentCursor():AbstractMouseCursor {
			return _currentCursor;
		}

		public function set currentCursor(value:AbstractMouseCursor):void {
			if(value == null){
				cursorContainer.removeChild(_currentCursor);
				_currentCursor = value;
				
			} else if(_currentCursor != value){
				if(_currentCursor != null && cursorContainer.contains(_currentCursor))
					cursorContainer.removeChild(_currentCursor);
				
				_currentCursor = value;
				cursorContainer.addChild(_currentCursor);
			}
		}
		
		public function get wallContainer():Sprite{
			return _wallContainer;
		}
		
		public function get bulletContainer():Sprite{
			return _bulletContainer;
		}
	}
}