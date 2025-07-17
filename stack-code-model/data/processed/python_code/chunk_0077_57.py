package com.illuzor.flat {
	
	import alternativa.engine3d.controllers.SimpleObjectController;
	import alternativa.engine3d.core.Camera3D;
	import alternativa.engine3d.core.Object3D;
	import alternativa.engine3d.core.Resource;
	import alternativa.engine3d.core.View;
	import alternativa.engine3d.materials.FillMaterial;
	import alternativa.engine3d.materials.TextureMaterial;
	import alternativa.engine3d.primitives.Box;
	import alternativa.engine3d.primitives.GeoSphere;
	import alternativa.engine3d.resources.BitmapTextureResource;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.display.StageAlign;
	import flash.display.Stage3D;
	import flash.display.StageScaleMode;
	import com.illuzor.flat.tools.ObjectsGenerator;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	//[Frame(factoryClass = "com.illuzor.flat.Preloader")]
	
	public class Main extends Sprite {
		
		private var camera:Camera3D;
		private var rootContainer:Object3D;
		private var stage3d:Stage3D;
		private var controller:SimpleObjectController;

		public function Main():void {
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}

		private function init(e:Event = null):void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.align = StageAlign.TOP_LEFT;
			
			rootContainer = new Object3D();
			
			camera = new Camera3D(0.1, 10000);
			camera.view = new View(stage.stageWidth, stage.stageHeight);
			/*camera.rotationX = -120*Math.PI/180;
			camera.y = -800;
			camera.z = 400;*/
			camera.rotationX = (-120*Math.PI/180)-0.2;
			camera.y = -100;
			camera.z = 100;
			camera.x = 100;
			addChild(camera.view);
			addChild(camera.diagram);
			rootContainer.addChild(camera);
			
			/*var box:Box = new Box(100, 100, 100);
			box.setMaterialToAllSurfaces(new FillMaterial(0xFF00FF));
			rootContainer.addChild(box);*/
			
			ObjectsGenerator.generate(rootContainer, Settings.elements);
			
			controller = new SimpleObjectController(stage, camera, 400);
			
			stage3d = stage.stage3Ds[0];
			stage3d.addEventListener(Event.CONTEXT3D_CREATE, onContext3dCreated);
			stage3d.requestContext3D();
		}
		
		private function onContext3dCreated(e:Event):void {
			for each (var resource:Resource in rootContainer.getResources(true)) {
				resource.upload(stage3d.context3D);
			}
			startRender();
		}
		
		private function startRender():void {
			addEventListener(Event.ENTER_FRAME, render);
		}
		
		private function render(e:Event):void {
			camera.render(stage3d);
			controller.update();
		}

	}
}