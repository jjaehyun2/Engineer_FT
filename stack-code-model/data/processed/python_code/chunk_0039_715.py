package com.illuzor.solarsystem {
	
	import away3d.cameras.Camera3D;
	import away3d.containers.ObjectContainer3D;
	import away3d.containers.Scene3D;
	import away3d.containers.View3D;
	import away3d.controllers.HoverController;
	import away3d.entities.Mesh;
	import away3d.materials.TextureMaterial;
	import away3d.primitives.SphereGeometry;
	import away3d.textures.BitmapTexture;
	import com.illuzor.solarsystem.engine.FreeCamController;
	import flash.display.Sprite;
	import away3d.debug.AwayStats;
	import flash.events.Event;
	import com.illuzor.solarsystem.tools.Bitmaps;
	import flash.geom.Vector3D;
	import flash.events.KeyboardEvent;
	import flash.ui.Keyboard;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	public class SolarSystem extends Sprite {
		
		private var container:ObjectContainer3D;
		private var view:View3D;
		//private var controller:HoverController;
		
		
		private var earth:Mesh;
		private var earthContainer:ObjectContainer3D;
		private var controller:FreeCamController;
		
		public function SolarSystem() {
		
			addEventListener(Event.ADDED_TO_STAGE, addedToStage);
		}
		
		private function addedToStage(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, addedToStage);
			initStage();
			initModels();
			initListeners();
		}
		
		private function initStage():void {
			var camera:Camera3D = new Camera3D();
			camera.lens.near = 10;
			camera.lens.far = 10000;
			
			var scene:Scene3D = new Scene3D();
			
			container = new ObjectContainer3D();
			scene.addChild(container);
			
			view = new View3D(scene, camera);
			view.background = new BitmapTexture(Bitmaps.backgroundTexture);
			
			view.antiAlias = 8;
			addChild(view);
			
			var stats:AwayStats = new AwayStats(view,false,false,5);
			addChild(stats);
			
			controller = new FreeCamController(stage, camera, container);
			
			//controller = new HoverController(camera, container);
			//controller.lookAtPosition = new Vector3D(0,0,0)
			//controller.yFactor = 1.4;
		}
		
		private function initModels():void {
			var sunTexture:BitmapTexture = new BitmapTexture(Bitmaps.sunTexture);
			var sunMaterial:TextureMaterial = new TextureMaterial(sunTexture);
			
			var sun:Mesh = new Mesh(new SphereGeometry(300, 64, 12, false), sunMaterial);
			sun.rotationX = 90;
			container.addChild(sun);
			
			earthContainer = new ObjectContainer3D();
			container.addChild(earthContainer);
			
			var earthTexture:BitmapTexture = new BitmapTexture(Bitmaps.earthTexture);
			var earthMaterial:TextureMaterial = new TextureMaterial(earthTexture);
			earth = new Mesh(new SphereGeometry(100, 64, 12, false), earthMaterial);
			earth.x = -600;
			
			earth.rotationX = 90;
			
			earthContainer.addChild(earth);
		}
		
		private function initListeners():void {
			addEventListener(Event.ENTER_FRAME, update);
			
			stage.addEventListener(Event.RESIZE, resize);
		}
		
		

		private function update(e:Event):void {
			view.render();
			
			//earthContainer.rotationY += 1;
			earth.rotationY ++
			//trace(controller.panAngle);
			//trace(controller.tiltAngle);
			
			//controller.autoUpdate = true
			controller.updateMove();
			
			//trace(tilt)
		}
		
		private function resize(e:Event):void {
			view.width = stage.stageWidth;
			view.height = stage.stageHeight;
		}
		
	}
}