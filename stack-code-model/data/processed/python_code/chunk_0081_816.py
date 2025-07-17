package
{
	import flash.display.Sprite;
	
	public class Proyecto1 extends Sprite
	{
		public function Proyecto1()
		{
			trace("---------------------------------------------------------------");
			trace("Nice build biatch"); // Mensaje de debug en consola flash (No se muestra en ventana)
			trace("---------------------------------------------------------------");
			
			// Declaracion de variables
			var num1:int = -150;
			var num2:uint = 10;
			var num3:Number = 10.0;
			var tOf:Boolean = true;
			var texto:String = "Texto";
			
			for(var i:int = 0; i < 10; i++)
			{
				trace("I " + (i + 1) );
			}
			trace("---------------------------------------------------------------");
			
			for(i = 10; i < 20; i++)
			{
				trace("I " + (i + 1) );
			}
			trace("---------------------------------------------------------------");
			
			var Jugador:Personaje = new Personaje();
			Jugador.setVida(10);
			Jugador.atacar();
			trace("---------------------------------------------------------------");
			
			var JugadorNinja:Ninja = new Ninja();
			JugadorNinja.setVida(10);
			JugadorNinja.atacar();
			trace("---------------------------------------------------------------");
			
			// Randoms
			// Del 0 al 1
			trace(Math.random());
			trace("---------------------------------------------------------------");
			
			// del 0 al 10
			trace(Math.random() * 10);
			trace("---------------------------------------------------------------");
			
			// del 0 al 100, solo parte entera
			var randNumber:int = Math.random() * 100;
			trace(randNumber);
			trace("---------------------------------------------------------------");
			
			// del 25 al 50
			var randNumber2:int = Math.random() * 25 + 25;
			trace(randNumber2);
			trace("---------------------------------------------------------------");
			
			// Vectores
			var numbersArray:Vector.<int> = new Vector.<int>;
			
			// Agrego elementos
			numbersArray.push(5);
			numbersArray.push(11);
			numbersArray.push(54);
			numbersArray.push(7);
			
			for(i = 0; i < numbersArray.length; i++)
			{
				trace( numbersArray[i] );
			}
			trace("---------------------------------------------------------------");
			
			//Vectores de clases (objetos)
			var jugadores:Vector.<Personaje> = new Vector.<Personaje>;
			jugadores.push( new Personaje() );
			jugadores[0].atacar();
			trace("---------------------------------------------------------------");
			
			
			
		}
	}
}