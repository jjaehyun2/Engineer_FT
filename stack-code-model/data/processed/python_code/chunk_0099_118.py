package  
{
	import net.flashpunk.Entity;
	import net.flashpunk.graphics.Text;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class InstructionsText extends Entity 
	{
		private var _text:Text;
		private var _mute:Text;
		private var _developers:Text;
		private var _sponsor:Text;
		private var _detailed:Text;
		private var _run:Text;
		public function InstructionsText() 
		{
			_text = new Text("Arrow Keys Direct your player. Z to Jump.", 0,680, { align:"center", width:640,size:24 } );
			graphic = _text;
			
			_mute = new Text("< Sound", 150, 480, { align:"left", width:320, size:16 } );
			addGraphic(_mute);
			
			_developers = new Text("< Developers", 120, 400, { align:"left", width:320, size:16 } );
			addGraphic(_developers);
			
			_sponsor = new Text("< Sponsor", 120, 592, { align:"left", width:320, size:16 } );
			addGraphic(_sponsor);
			
			_detailed = new Text("Run fast for the lowest combined score!", 615, 542, { align:"left", width:640, size:18 } );
			addGraphic(_detailed);
			
			_run = new Text("Run >", 315, 480, { align:"right", width:100, size:16 } );
			addGraphic(_run);
		}
		
	}

}