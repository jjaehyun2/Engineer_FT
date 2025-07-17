package com.illuzor.firstflat 
{
	import alternativa.engine3d.containers.*;
	import alternativa.engine3d.controllers.SimpleObjectController;
	import alternativa.engine3d.core.Camera3D;
	import alternativa.engine3d.core.Object3DContainer;
	import alternativa.engine3d.core.View;
	import alternativa.engine3d.primitives.Box;
	import alternativa.engine3d.primitives.Plane;
	import alternativa.engine3d.materials.*;
	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.display.Stage;
	import flash.events.Event;
	
	
	/**
	 * ...
	 * @author iLLuzor // illuzor.com // illuzor@gmail.com
	 * 
	 */
	public class Flat3d extends Sprite {
		private var stag:Stage
		private var stageWidth:uint;
		private var stageHeight:uint;
		private var camera:Camera3D;
		private var container:BSPContainer;
		private var controller:SimpleObjectController;
		
		//...walls begin
		private var livingRoomFloorPlane:Plane;
		private var livingWallRight:Plane
		private var livingWallLeft:Box;
		
		private var livingWallBottom:Plane;
		
		private var livingTopRight:Box;
		private var livingTopLeft:Box;
		
		private var bottomLeft:Plane;
		
		private var livingBottomBottom:Box;
		
		private var leftWall:Plane;
		
		private var bedroomTopRight:Plane;
		private var bedroomTopLeft:Plane;
		
		private var kitchenTopRight:Plane;
		private var kitchenTopLeft:Plane;
		
		private var bedroomLeftWall:Box;
		private var bedroomLeftBottom:Box;
		private var bedroomRightBottom:Box;
		
		private var bathroomRightBottom:Box
		private var bathroomRightTop:Box
		
		private var bathroomTop:Box;
		
		private var kitchenBottomLeft:Box;
		
		private var windowContainerKitchen:Object3DContainer;
		
		private var windowTop:Plane;
		private var windowBottom:Plane;
		private var windowCenter:Plane;
		private var windowBalcony:Plane;
		
		private var windowContainerBedroom:Object3DContainer;
		
		private var windowContainerBalcony:Object3DContainer;
		
		private var windowBalconyTop:Plane;
		private var windowBalconyBottom:Plane;
		private var windowBalconyWindow:Plane;
		
		private var windowLivingTop:Box;
		private var windowLivingBottom:Box;
		private var windowLivingCenter:Box;
		//private var windowLivingDoorBootom:Box;
		//... walls end
		
		[Embed(source = '../../../../lib/floorTexture.png')] private var bm:Class;
		private var bmd:Bitmap;
		
		[Embed(source = '../../../../lib/window1.png')] private var winbm:Class;
		private var windowbd:Bitmap;
		
		public function Flat3d(sw:uint, sh:uint, st:Stage) {
			bmd = new bm() as Bitmap;
			windowbd = new winbm() as Bitmap;
			
			stag = st;
			stageWidth = sw;
			stageHeight = sh;
			
			camera = new Camera3D();
			camera.view = new View(stageWidth, stageHeight);
			
			camera.rotationX = (-120*Math.PI/180)-0.2;
			camera.y = -100;
			camera.z = 100;
			camera.x = 100;
			
			addChild(camera.view);
			addChild(camera.diagram);
			
			container = new BSPContainer();
			container.addChild(camera);
			buildPlanes();
		}
		
		private function buildPlanes():void {
			livingRoomFloorPlane = new Plane(944, 744, 1, 1, false, false, false, null, new TextureMaterial(bmd.bitmapData));
			
			livingRoomFloorPlane.y = 60;
			livingRoomFloorPlane.x = -320;
			container.addChild(livingRoomFloorPlane);
			
			livingWallRight = new Plane(240, 740, 1, 1, false, true, false, null, new FillMaterial(0xFF0000));
			livingWallRight.rotationY = 1.5708;
			livingWallRight.x = 150;
			livingWallRight.z = 120;
			livingWallRight.y = 60;
			container.addChild(livingWallRight);
			
			
			
			////
			livingWallBottom = new Plane(420, 240, 1, 1, false, true, false, null, new FillMaterial(0x00FF00));
			livingWallBottom.y = -310;
			livingWallBottom.z = 120;
			livingWallBottom.x = -60;
			livingWallBottom.rotationX = 1.5708;
			container.addChild(livingWallBottom);
			
			livingTopRight = new Box(76, 240, 20);
			livingTopRight.rotationX = 1.5708;
			livingTopRight.y = 320;
			livingTopRight.z = 120;
			livingTopRight.x = 112;
			livingTopRight.setMaterialToAllFaces(new FillMaterial(0x0000FF));
			container.addChild(livingTopRight);
			
			livingTopLeft = new Box(76, 240, 20);
			livingTopLeft.rotationX = 1.5708;
			livingTopLeft.y = 320;
			livingTopLeft.z = 120;
			livingTopLeft.x = -112;
			livingTopLeft.setMaterialToAllFaces(new FillMaterial(0x0000FF));
			container.addChild(livingTopLeft);
			
			livingBottomBottom = new Box(32, 240, 20);
			livingBottomBottom.rotationX = 1.5708;
			livingBottomBottom.rotationZ = 1.5708;
			livingBottomBottom.y = -294;
			livingBottomBottom.z = 120;
			livingBottomBottom.x = -160;
			livingBottomBottom.setMaterialToAllFaces(new FillMaterial(0x0000FF));
			container.addChild(livingBottomBottom);
			
			livingWallLeft = new Box(20, 644, 240);
			livingWallLeft.x = -160;
			livingWallLeft.y = 108;
			livingWallLeft.z = 120;
			livingWallLeft.setMaterialToAllFaces(new FillMaterial(0x669900));
			container.addChild(livingWallLeft);
			
			bottomLeft = new Plane(240, 444, 1,1,false,true,false,null,new FillMaterial(0xFFFF00));
			bottomLeft.rotationY = 1.5708;
			bottomLeft.rotationX = 1.5708;
			bottomLeft.x = -568;
			bottomLeft.z = 120;
			bottomLeft.y = -310;
			container.addChild(bottomLeft);
			
			leftWall = new Plane(240, 620, 1, 1, false, false, false, null, new FillMaterial(0xFF0000));
			leftWall.rotationY = 1.5708;
			leftWall.x = -790;
			leftWall.z = 120;
			container.addChild(leftWall);
			
			bedroomTopRight = new Plane(300, 240, 1, 1, false, false, false, null, new FillMaterial(0xd88a03));
			bedroomTopRight.rotationX = 1.5708;
			bedroomTopRight.y = 310;
			bedroomTopRight.z = 120;
			bedroomTopRight.x = -320//-320;
			container.addChild(bedroomTopRight);
			
			kitchenTopRight = new Plane(300, 240, 1, 1, false, false, false, null, new FillMaterial(0xd803a8));
			kitchenTopRight.rotationX = 1.5708;
			kitchenTopRight.y = 310;
			kitchenTopRight.z = 120;
			kitchenTopRight.x = -640;
			container.addChild(kitchenTopRight);
			
			bedroomLeftWall = new Box(20, 490, 240);
			//new Box(
			bedroomLeftWall.x = -480;
			bedroomLeftWall.y = 65;
			bedroomLeftWall.z = 120;
			bedroomLeftWall.setMaterialToAllFaces(new FillMaterial(0x669900));
			container.addChild(bedroomLeftWall);
			
			bedroomLeftBottom = new Box(32, 240, 20);
			bedroomLeftBottom.rotationX = 1.5708;
			bedroomLeftBottom.y = -170;
			bedroomLeftBottom.z = 120;
			bedroomLeftBottom.x = -454;
			bedroomLeftBottom.setMaterialToAllFaces(new FillMaterial(0x0000FF));
			container.addChild(bedroomLeftBottom);
			
			bedroomRightBottom = new Box (204, 240, 20);
			bedroomRightBottom.rotationX = 1.5708;
			bedroomRightBottom.y = -170;
			bedroomRightBottom.z = 120;
			bedroomRightBottom.x = -272;
			bedroomRightBottom.setMaterialToAllFaces(new FillMaterial(0x0000FF));
			container.addChild(bedroomRightBottom);
			
			bathroomRightBottom = new Box(53, 240, 20);
			bathroomRightBottom.rotationX = 1.5708;
			bathroomRightBottom.rotationZ = 1.5708;
			bathroomRightBottom.y = -283;
			bathroomRightBottom.z = 120;
			bathroomRightBottom.x = -600;
			bathroomRightBottom.setMaterialToAllFaces(new FillMaterial(0xF000FF));
			container.addChild(bathroomRightBottom);
			
			bathroomRightTop = new Box(53, 240, 20);
			bathroomRightTop.rotationX = 1.5708;
			bathroomRightTop.rotationZ = 1.5708;
			bathroomRightTop.y = -164;
			bathroomRightTop.z = 120;
			bathroomRightTop.x = -600;
			bathroomRightTop.setMaterialToAllFaces(new FillMaterial(0xF000FF));
			container.addChild(bathroomRightTop);
			
			bathroomTop = new Box(180, 240, 20);
			bathroomTop.rotationX = 1.5708;
			bathroomTop.y = -147;
			bathroomTop.z = 120;
			bathroomTop.x = -700;
			bathroomTop.setMaterialToAllFaces(new FillMaterial(0xF0F0FF));
			container.addChild(bathroomTop);
			
			kitchenBottomLeft = new Box(222, 240, 20);
			kitchenBottomLeft.rotationX = 1.5708;
			kitchenBottomLeft.y = -147+80;
			kitchenBottomLeft.z = 120;
			kitchenBottomLeft.x = -679;
			kitchenBottomLeft.setMaterialToAllFaces(new FillMaterial(0xF0F0FF));
			container.addChild(kitchenBottomLeft);
			
			windowBalcony = new Plane(300, 240, 1, 1, false, false, false, null, new FillMaterial(0xd88a03));
			windowBalcony.rotationX = 1.5708;
			windowBalcony.y = 430;
			windowBalcony.z = 120;
			windowBalcony.x = 0//-320;
			container.addChild(windowBalcony);
			
			
			windowLivingTop = new Box(148, 60, 20);
			windowLivingTop.rotationX = 1.5708;
			windowLivingTop.y = 320;
			windowLivingTop.z = 210;
			//windowLivingTop.x = -74;
			windowLivingTop.setMaterialToAllFaces(new FillMaterial(0xFF00FF));
			//container.addChild(windowLivingTop);
			
			windowLivingBottom = new Box(74, 60, 20);
			windowLivingBottom.rotationX = 1.5708;
			windowLivingBottom.y = 320;
			windowLivingBottom.z = 30;
			windowLivingBottom.x = 37;
			windowLivingBottom.setMaterialToAllFaces(new FillMaterial(0xFF00FF));
			//container.addChild(windowLivingBottom);
			
			windowLivingCenter = new Box(74, 120, 20);
			windowLivingCenter.rotationX  = 1.5708;
			windowLivingCenter.y = 320;
			windowLivingCenter.z = 120;
			windowLivingCenter.x = 37;
			windowLivingCenter.setMaterialToAllFaces(new TextureMaterial(windowbd.bitmapData));
			//container.addChild(windowLivingCenter);
			
			
			controller = new SimpleObjectController(stag, camera, 300);
			addEventListener(Event.ENTER_FRAME, test)
		}
		
		private function test(e:Event):void {
			camera.render();
			controller.update();
		}
		
	}

}