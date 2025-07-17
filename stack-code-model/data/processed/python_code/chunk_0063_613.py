package com.illuzor.leaptest.away3d {
	
	import away3d.cameras.Camera3D;
	import away3d.containers.ObjectContainer3D;
	import away3d.containers.Scene3D;
	import away3d.containers.View3D;
	import away3d.controllers.HoverController;
	import away3d.debug.AwayStats;
	import away3d.textures.BitmapTexture;
	import com.illuzor.leaptest.away3d.events.RotatorEvent;
	import com.illuzor.leaptest.away3d.events.SceneEvent;
	import com.illuzor.leaptest.away3d.scene.LeapAwayScene;
	import com.illuzor.leaptest.away3d.tools.Rotator;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	//import com.leapmotion.leap.Controller;
	import com.illuzor.leaptest.away3d.tools.CameraController;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.utils.*;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	public class MainScreen extends Sprite {
		
		private var view:View3D;
		private var controller:CameraController;
		
		private var inMove:Boolean = false;
		private var lastPanAngle:Number;
		private var lastTiltAngle:Number;
		private var lastMouseX:Number;
		private var lastMouseY:Number;
		//private var tiltSpeed:Number = 5;
		//private var panSpeed:Number = 5;
		//private var distanceSpeed:Number = 15;
		private var tiltIncrement:Number = 0;
		private var panIncrement:Number = 0;
		private var distanceIncrement:Number = 0;
		private var twoToStart:Boolean;
		private var oneToStart:Boolean;
		private var rotator:Rotator;
		private var twoStarted:Boolean;
		private var oneStarted:Boolean;
		private var oneIntID:int;
		private var twoIntID:int;
		private var leapScene:LeapAwayScene;
		private var motionActiavted:Boolean;
		private var lastX:int;
		
		public function MainScreen() {
			addEventListener(Event.ADDED_TO_STAGE, onAdded);
		}
		
		private function onAdded(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, onAdded);
			initScene();
			initListeners();
		}
		
		private function initScene():void {
			var camera:Camera3D = new Camera3D();
			camera.lens.near = 10;
			camera.lens.far = 10000;
			
			
			
			//camera.y = 400
			
			var scene:Scene3D = new Scene3D();
			
			var container:ObjectContainer3D = new ObjectContainer3D();
			scene.addChild(container);
			//container.y = -200;
			
			leapScene = new LeapAwayScene();
			container.addChild(leapScene);
			
			view = new View3D(scene, camera);
			view.renderer.antiAlias = 8;
			view.antiAlias = 8;
			view.mouseEnabled = true;
			view.antiAlias = 16;
			view.background = new BitmapTexture(Assets.bacground.bitmapData);
			addChild(view);
			var stats:AwayStats = new AwayStats(view, false, false, 5);
			addChild(stats);
			
			controller = new CameraController(stage, camera, container, 0, 10, 1000, -90, 90);
			controller.yFactor = 1.4;
			controller.distance = 500;
			
			//leapScene.addEventListener(SceneEvent.SWYPE, onSwype);
			leapScene.addEventListener(SceneEvent.TWO_FINGERS, onSwype);
			leapScene.addEventListener(SceneEvent.ONE_FINGER, onSwype);
			leapScene.addEventListener(SceneEvent.OTHER_FINGER, onSwype);
		}
		
		private function onSwype(e:SceneEvent):void {
			//trace(e.direction);
			if (e.type == SceneEvent.TWO_FINGERS) {
				if (!twoToStart) {
					trace("two");
					twoToStart = true;
					twoIntID = setTimeout(twoStart, 500);
				}
			} else if (e.type == SceneEvent.ONE_FINGER) {
				
				if (!oneToStart) {
					trace("one");
					clearTimeout(twoIntID);
					oneToStart = true;
					oneIntID = setTimeout(oneStart, 500);
				}
			} else {
				trace("other");
				twoToStart = oneToStart = false;
				clearTimeout(twoIntID);
				clearTimeout(oneIntID);
				clearRotator()
			}

		}
		
		private function twoStart():void {
			
			if (!twoStarted) {
				motionActiavted = false;
				clearTimeout(oneIntID);
				clearRotator()
				twoStarted = true;
				rotator = new Rotator(Assets.rotator, new Rectangle(0,0, 128, 128));
				addChild(rotator)
				trace("two start");
				rotator.addEventListener(RotatorEvent.ROTATOR_ENDS, onRotatorEndsTwo);
				addEventListener(Event.ENTER_FRAME, updateRotatorTwo);
				//removeEventListener(Event.ENTER_FRAME, updateRotatorOne);
			}
		}

		private function oneStart():void {
			
			if (!oneStarted) {
				motionActiavted = false;
				clearTimeout(twoIntID);
				clearRotator()
				oneStarted = true;
				rotator = new Rotator(Assets.rotator, new Rectangle(0,0, 128, 128));
				addChild(rotator);
				rotator.addEventListener(RotatorEvent.ROTATOR_ENDS, onRotatorEndsOne);
				addEventListener(Event.ENTER_FRAME, updateRotatorOne);
				//removeEventListener(Event.ENTER_FRAME, updateRotatorTwo);
				trace("one start")
			}
		}
		
		private function updateRotatorOne(e:Event):void {
			removeEventListener(Event.ENTER_FRAME, updateRotatorTwo);
			rotator.x = view.project(leapScene.finger1.scenePosition).x - rotator.width/2;
			rotator.y = view.project(leapScene.finger1.scenePosition).y - rotator.height / 2;
			if (motionActiavted) {
				leapScene.startMoveCube();
			}
		}
		
		private function updateRotatorTwo(e:Event):void {
			//trace(view.project(leapScene.finger1.scenePosition).x)
			removeEventListener(Event.ENTER_FRAME, updateRotatorOne);
			var pointOne:Point = new Point(view.project(leapScene.finger1.scenePosition).x, view.project(leapScene.finger1.scenePosition).y);
			var pointTwo:Point = new Point(view.project(leapScene.finger2.scenePosition).x, view.project(leapScene.finger2.scenePosition).y);
			
			var center:Point = Point.interpolate(pointOne, pointTwo, .5);
			
			rotator.x = center.x - rotator.width/2;
			rotator.y = center.y - rotator.height / 2;
			
			if (motionActiavted) {
				//trace("motion activated")
				
				rotateCube(center.x - lastX);
				
				
				//var lastY:int = center.y;
			}
			lastX = center.x;
		}
		
		private function rotateCube(rot:int):void {
			trace(rot)
			leapScene.cube1.rotationY += rot;
		}
		
		private function onRotatorEndsTwo(e:RotatorEvent):void {
			rotator.visible = false;
			motionActiavted = true;
		}
		
		private function onRotatorEndsOne(e:RotatorEvent):void {
			rotator.visible = false;
			motionActiavted = true;
		}
		
		private function clearRotator():void {
			if (rotator) {
				rotator.removeEventListener(RotatorEvent.ROTATOR_ENDS, onRotatorEndsOne);
				rotator.removeEventListener(RotatorEvent.ROTATOR_ENDS, onRotatorEndsTwo);
				removeEventListener(Event.ENTER_FRAME, updateRotatorOne);
				removeEventListener(Event.ENTER_FRAME, updateRotatorTwo);
				
				removeChild(rotator);
				rotator = null;
				twoStarted = oneStarted = false;
				leapScene.stopMoveCube();
			}
		}
		
		private function initListeners():void {
			addEventListener(Event.ENTER_FRAME, renderUpdate);
			stage.addEventListener(Event.RESIZE, onResize);
			view.addEventListener(MouseEvent.MOUSE_DOWN, onMouseDown);
			view.addEventListener(MouseEvent.MOUSE_UP, onMouseUp);
		}
		
		private function renderUpdate(e:Event):void {
			view.render();
			
			if (inMove) {
				controller.panAngle = 0.3 * (stage.mouseX - lastMouseX) + lastPanAngle;
				controller.tiltAngle = 0.3 * (stage.mouseY - lastMouseY) + lastTiltAngle;
			}
			controller.panAngle += panIncrement;
			controller.tiltAngle += tiltIncrement;
			controller.distance += distanceIncrement;
		}
		
		private function onResize(e:Event):void {
			view.width = stage.stageWidth;
			view.height = stage.stageHeight;
		}
		
		private function onMouseDown(event:MouseEvent):void {
			inMove = true;
			lastPanAngle = controller.panAngle;
			lastTiltAngle = controller.tiltAngle;
			lastMouseX = stage.mouseX;
			lastMouseY = stage.mouseY;
			stage.addEventListener(Event.MOUSE_LEAVE, onStageMouseLeave);
		}
 
		private function onMouseUp(event:MouseEvent):void {
			inMove = false;
			stage.removeEventListener(Event.MOUSE_LEAVE, onStageMouseLeave);
		}
 
		private function onStageMouseLeave(event:Event):void {
			inMove = false;
			stage.removeEventListener(Event.MOUSE_LEAVE, onStageMouseLeave);
		}
		
	}

}