package com.illuzor.engine3d.tools {
	
	import alternativa.engine3d.core.events.MouseEvent3D;
	import alternativa.engine3d.core.Object3D;
	import flash.display.DisplayObjectContainer;
	import flash.events.MouseEvent;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	public class ModelRotator {
		
		static private var container:DisplayObjectContainer;
		static private var oldX:Number = 0; // координаты для вращения
		static private var oldY:Number = 0;
		static private var mouseDowned:Boolean = false; // нажата ли кнопка мыши
		static private var modelContainer:Object3D;
		
		static public function init(cont:DisplayObjectContainer):void {
			container = cont;
		}
		
		static public function setParameters(modContainer:Object3D):void {
			modelContainer = modContainer;
			modelContainer.addEventListener(MouseEvent3D.MOUSE_DOWN, onMouseDown);
			container.addEventListener(MouseEvent.MOUSE_UP, onMouseUp)
		}
		
		static private function onMouseDown(e:MouseEvent3D):void {
			trace("down");
			oldX = container.mouseX;
			oldY = container.mouseY;
			mouseDowned = true;
			container.addEventListener(MouseEvent.MOUSE_MOVE, onMouseMove);
		}
		
		static private function onMouseMove(e:MouseEvent):void {
			if (mouseDowned){
				var speedX:Number = container.mouseX - oldX;
				var speedY:Number = container.mouseY - oldY;
				modelContainer.rotationY += speedX / 100;
				modelContainer.rotationX += speedY / 100;
				oldX = container.mouseX;
				oldY = container.mouseY;
			}
		}
		
		static private function onMouseUp(e:MouseEvent):void {
			mouseDowned = false;
		}
		
	}
}