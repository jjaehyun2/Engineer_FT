package 
{
	import Entidades.Cuadro;
	import net.flashpunk.Entity;
	import net.flashpunk.World;
	import net.flashpunk.graphics.Image;
	import net.flashpunk.graphics.Text;
	import net.flashpunk.FP;
	import net.flashpunk.utils.Input;
	import net.flashpunk.utils.Key;
	
	/**
	 * ...
	 * @author ...
	 */
	public class Menu extends World 
	{
		[Embed(source = "../img/menu.png")]
		public static const FON:Class;
		
		public function Menu() 
		{
			super();
			add(new Entity(740, 775, new Text("Aldrin Salazar @ AlphaSigma.web.ve", 0, 0, { font: "aldrin" } )));
			add(new Entity(100, 100, new Image(FON)));
		}
		
		override public function update():void {
			super.update();	
			
			if (Input.pressed(Key.S)) {
				FP.world = new Transition(Secuencial);
			}
			
			if (Input.pressed(Key.B)) {
				FP.world = new Transition(Binaria);
			}
		}
		
	}

}