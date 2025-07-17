package  
{
	import flash.events.MouseEvent;
	import flash.net.navigateToURL;
	import flash.net.URLRequest;
	import net.flashpunk.Entity;
	import net.flashpunk.FP;
	import net.flashpunk.graphics.Image;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class Sign extends Entity 
	{
		[Embed(source="Assets/Graphics/Items & Objects/n_sign.png")]private const SIGN:Class;
		private var _image:Image;
		public var message:String = "";
		
		public static var Simple:Sign;
		public static var Tricky:Sign;
		public static var Adventure:Sign;
		public static var Music:Sign;
		public static var Profusion:Sign;
		public var timeout:int = 240;
		
		public function Sign(X:int,Y:int, Info:String) 
		{
			super(X, Y);
			_image = new Image(SIGN);
			graphic = _image;
			message = Info;
			setHitbox(26, 26, 5, 5);
			type = "Sign";
			layer = 270;
			
			trace(Info);
			if (message.indexOf("Simple:") == 0) Simple = this;
			if (message.indexOf("Tricky:") == 0) Tricky = this;
			if (message.indexOf("Adventure:") == 0) Adventure = this;
			if (message.indexOf("Press Space to toggle MUSIC!") == 0)
			{
				Music = this;
				setHitbox(30, 30, 7, 7);
			}
			if (message.indexOf("ProfusionGames.com") == 0)
			{
				Profusion = this;
				setHitbox(30, 30, 7, 7);
			}			
		}

		
		
		
		
		public function setMessage(s:String):void
		{
			message = s;
		}
		
		
		
	}

}