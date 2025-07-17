package worlds {
	import flash.geom.Point;
	import net.flashpunk.graphics.Text;
	import net.flashpunk.World;
	import net.flashpunk.FP;
	import characters.Batracio;
	
	public class World1 extends World {
		private var batracio:Batracio;
		private var level1:Level1;

		override public function begin():void {
			level1 = new Level1(GC.LEVEL1_OEL);
			add(level1);

			var batracioPos:XML = level1.xmlData.Entities.batracio[0];
			batracio = new Batracio(batracioPos.@x, batracioPos.@y);
			add(batracio);
		}
		
		override public function update():void {
			if (batracio.y > level1.xmlData.@height) {
				var batracioPos:XML = level1.xmlData.Entities.batracio[0];
				batracio.x = batracioPos.@x;
				batracio.y = batracioPos.@y;
			}
			updateCamera();
			super.update();
		}
		
		private function updateCamera():void {
			FP.camera.x = batracio.x - FP.width / 2 + batracio.width / 2;
			FP.camera.y = batracio.y - FP.height / 2 + batracio.height / 2;
			
			FP.camera.x = FP.camera.x < 0 ? 0 : FP.camera.x > level1.xmlData.@width - FP.width ? level1.xmlData.@width - FP.width : FP.camera.x;
			FP.camera.y = FP.camera.y < 0 ? 0 : FP.camera.y > level1.xmlData.@height - FP.height ? level1.xmlData.@height - FP.height : FP.camera.y;
		}
	}
}