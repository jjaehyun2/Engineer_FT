package MyClases
{
	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	import flash.text.TextFormat;

	public class Menu extends Sprite
	{
		
		// Propiedades de la clase menú
		private var PlayButton:SDButton = new SDButton( "Jugar" , 104);
		private var OptionsButton:SDButton = new SDButton( "Opciones" , 208);
		private var CreditsButton:SDButton = new SDButton( "Creditos" , 316);
		
		// Imagen del menú
		[Embed(source="Assets/BackGround.PNG")]
		private var MenuBackground:Class;
		private var MyMenuBackground:Bitmap = new MenuBackground;
		
		// Titulo del juego
		private var GameTitle:TextField = new TextField();
		
		public function Menu()
		{
			// Formato de texto de titulo
			var TitleFormat:TextFormat = new TextFormat();
			
			TitleFormat.bold = true;
			TitleFormat.size = 40;
			TitleFormat.font = "Courier New" ;
			TitleFormat.color = 0x4B705A;
			
			// Titulo
			GameTitle.autoSize = TextFieldAutoSize.CENTER;
			GameTitle.mouseEnabled = false;
			GameTitle.defaultTextFormat = TitleFormat; 
			GameTitle.text = "SquareDeath";
			GameTitle.x = ( 800 / 2 ) - ( GameTitle.width / 2 );
			GameTitle.y = -2;
			
			// Escalado de imagen de background
			MyMenuBackground.scaleX = 1.1;
			MyMenuBackground.scaleY = 1.09;
			
			PlayButton.addEventListener("IWantToPlay", GoToPlay);
			
			addChild( MyMenuBackground );
			addChild( GameTitle );
			addChild( PlayButton );
			addChild( OptionsButton );
			addChild( CreditsButton );
		}
		
		protected function GoToPlay(event:Event):void
		{
			dispatchEvent(new Event("IWantToPlay"));
		}
	}
}