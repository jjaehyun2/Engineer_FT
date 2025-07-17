package
{
	public class Ninja extends Personaje
	{
		public function Ninja()
		{
		}
		
		public override function atacar():void
		{
			// llamada al metodo de la clase base
			//super.atacar();
			trace("Ninja atacando asi bien peola");
		}
		
	}
}