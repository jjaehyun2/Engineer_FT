package com.illuzor.spinner.screens {
	
	import com.illuzor.spinner.constants.Color;
	import com.illuzor.spinner.constants.ShapeType;
	import com.illuzor.spinner.constants.SubscreenType;
	import com.illuzor.spinner.controllers.AppController;
	import com.illuzor.spinner.controllers.ControlManager;
	import com.illuzor.spinner.events.ControlManagerEvent;
	import com.illuzor.spinner.events.ScreenEvent;
	import com.illuzor.spinner.graphics.RotatorShape;
	import com.illuzor.spinner.graphics.Splash;
	import com.illuzor.spinner.utils.intRandom;
	import flash.geom.Point;
	import starling.display.Image;
	import starling.display.Sprite;
	import starling.events.Event;
	import starling.text.TextField;
	import starling.text.TextFieldAutoSize;
	import starling.textures.TextureAtlas;
	import starling.utils.deg2rad;

	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class GameScreen extends ScreenBase {
		
		private var shapeType:uint;
		private var colors:Vector.<uint>;
		private var atlas:TextureAtlas;
		private var shape:RotatorShape;
		private var circle:Image
		private var currentColor:uint;
		private var difficulty:uint;
		private var totalScores:uint;
		private var scoresTextField:TextField;
		private var controlManager:ControlManager;
		private var splash:Splash;
		private var speed:Number;
		
		public function GameScreen(shapeType:uint, difficulty:uint) {
			this.difficulty = difficulty;
			this.shapeType = shapeType;
			controlManager = new ControlManager();
			colors = Color.randomizeColors(Color.getColors(shapeType));
		}
		
		override protected function start():void {
			atlas = AppController.assetManager.getTextureAtlas("atlas1");
			var textureName:String;
			
			switch (shapeType) {
				case ShapeType.CIRCLE:
					textureName =  "circle_half";
				break;
				
				case ShapeType.TRIANGLE:
					textureName =  "triangle_part";
				break;
				
				case ShapeType.SQUARE:
					textureName =  "square_part";
				break;
				
				case ShapeType.PENTAGON:
					textureName =  "pentagon_part";
				break;
				
				case ShapeType.HEXAGON:
					textureName =  "hehagon_part";
				break;
			}
			
			shape = new RotatorShape(shapeType, colors, atlas.getTexture(textureName));
			
			shape.width = stage.stageWidth >> 1;
			shape.scaleY = shape.scaleX
			shape.x = stageWidth >> 1;
			shape.y = stageHeight - shape.height/2 - (stageWidth - shape.width) / 2;
			
			circle = new Image(atlas.getTexture("circle"));
			circle.pivotX = circle.pivotY = circle.width >> 1;
			circle.x = stageWidth >> 1;
			circle.scale = shape.scale;
			addChild(circle);
			
			splash = new Splash(atlas.getTexture("circle"), circle.width, stageWidth, stageHeight - (shape.y - shape.height / 2));
			splash.x = stageWidth >> 1;
			addChild(splash);
			
			addChild(shape);
			resetCircle();
			
			speed = shape.bounds.y / 85;
			
			var scoresTextContainer:Sprite = new Sprite();
			addChild(scoresTextContainer);
			
			scoresTextField = new TextField(stageWidth >> 1, 200, "0", "game_font", 180, 0x0);
			scoresTextField.autoSize = TextFieldAutoSize.BOTH_DIRECTIONS;
			scoresTextContainer.addChild(scoresTextField);
			
			scoresTextContainer.height = stageHeight * .08;
			scoresTextContainer.scaleX = scoresTextContainer.scaleY;
			
			scoresTextContainer.x = scoresTextContainer.width >> 1;
			scoresTextContainer.y = scoresTextContainer.width >> 1;
			
			this.addEventListener(Event.ENTER_FRAME, onUpdate);
			controlManager.addEventListener(ControlManagerEvent.ROTATE_CCW, onControllerEvent);
			controlManager.addEventListener(ControlManagerEvent.ROTATE_CW, onControllerEvent);
		}
		
		private function onControllerEvent(e:ControlManagerEvent):void {
			if (e.type == ControlManagerEvent.ROTATE_CW) {
				shape.rotateCW();
			} else {
				shape.rotateCCW();
			}
		}
		
		private function onUpdate(e:Event):void {
			var circleCenter:Point = new Point(circle.x, circle.y);
			var shapeCenter:Point = new Point(shape.x, shape.y);
			
			if (Point.distance(circleCenter, shapeCenter) <= circle.height/2 + shape.radius) {
				if (currentColor == shape.correntColor) {
					totalScores++;
					scoresTextField.text = String(totalScores);
				} else {
					this.removeEventListener(Event.ENTER_FRAME, onUpdate);
					controlManager.removeEventListener(ControlManagerEvent.ROTATE_CCW, onControllerEvent);
					controlManager.removeEventListener(ControlManagerEvent.ROTATE_CW, onControllerEvent);
					dispatchEvent(new ScreenEvent(ScreenEvent.SHOW_SUBSCREEN, SubscreenType.GAME_REPLAY))
				}
				splash.color = currentColor;
				splash.y = circleCenter.y + circle.height / 2;
				splash.splash();
				
				resetCircle();
			}
			
			circle.y += speed;
			circle.rotation += deg2rad(2);
		}
		
		private function resetCircle():void {
			circle.y = - circle.height;
			currentColor = randomColor;
			circle.color = currentColor;
		}
		
		private function get randomColor():uint {
			return colors[intRandom(0, colors.length - 1)];
		}
		
		public function replay():void {
			totalScores = 0;
			scoresTextField.text = "0";
			this.addEventListener(Event.ENTER_FRAME, onUpdate);
			controlManager.addEventListener(ControlManagerEvent.ROTATE_CCW, onControllerEvent);
			controlManager.addEventListener(ControlManagerEvent.ROTATE_CW, onControllerEvent);
		}
		
		override public function hide():void {
			super.hide();
		}
		
		override public function dispose():void {
			this.removeEventListener(Event.ENTER_FRAME, onUpdate);
			controlManager.removeEventListener(ControlManagerEvent.ROTATE_CCW, onControllerEvent);
			controlManager.removeEventListener(ControlManagerEvent.ROTATE_CW, onControllerEvent);
			controlManager.dispose();
			
			atlas = null;
			splash.dispose();
			
			super.dispose();
		}
		
	}
}