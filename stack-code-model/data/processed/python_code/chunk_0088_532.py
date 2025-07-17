package  
{
	import net.flashpunk.Entity;
	import net.flashpunk.graphics.Text;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class MenuText extends Entity 
	{
		private var _text:Text;
		public function MenuText() 
		{
			_text = new Text("miniPassage", 100,262, { align:"center", width:640,size:32 } );
			graphic = _text;
		}
		
	}

}