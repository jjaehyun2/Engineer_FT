package {
	import org.flixel.FlxEmitter;
	import org.flixel.FlxPoint;
	import org.flixel.FlxSprite;
	import org.flixel.FlxG;
	
	public class PoliceCar extends Car {
		
		[Embed(source = './data/cop_car.png')] private var policeCar:Class;
		[Embed(source = './data/cop_car_lights.png')] private var policeCarLights:Class;
		
		public function PoliceCar() {
			super( policeCar, policeCarLights, 111 );		
		}
	}
}