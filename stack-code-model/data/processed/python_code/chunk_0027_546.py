package MyClases
{
	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	import flash.events.TimerEvent;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	import flash.text.TextFormat;
	import flash.ui.Keyboard;
	import flash.utils.Timer;

	public class InGame extends Sprite
	{
		
		[Embed(source="Assets/Floor1.png")]
		private var Floor:Class;
		private var TileFloorOne:Bitmap = new Floor; 
		
		[Embed(source="Assets/Floor2.png")]
		private var FloorTwo:Class;
		private var TileFloorTwo:Bitmap = new FloorTwo; 
		
		[Embed(source="Assets/Floor3.png")]
		private var FloorThree:Class;
		private var TileFloorThree:Bitmap = new FloorThree; 
		
		protected var MyFloor:Vector.<Bitmap> = new Vector.<Bitmap>;
		protected var MyEnemy:Vector.<Enemy> = new Vector.<Enemy>;
		
		private var MyPlayer:Player = new Player();
		private var Oleada:uint = 1;
		private var Vidas:TextField = new TextField();
		private var HPTextFormat:TextFormat = new TextFormat();
		private var MyTimer:Timer = new flash.utils.Timer(1000, 0);
		private var Score:uint;
		private var TextScore:TextField = new TextField;
		
		public function InGame()
		{
			
			Score = 0;
			MyTimer.start();
			
			HPTextFormat.bold = true;
			HPTextFormat.size = 15;
			HPTextFormat.font = "Courier New" ;
			HPTextFormat.color = 0x0000ff;
			
			MyPlayer.x = 200;
			MyPlayer.y = 200;
			// Genero aleatoriamente el floor
			var randNumber:int;
			var TempBitmap:Bitmap = new Bitmap;
			
			for(var i:uint = 0; i < 50; i++) // Columnas
			{
				for(var c:uint = 0; c < 32; c++) // Filas
				{
					randNumber = Math.random() * 3;
					TempBitmap.x = i * 16;
					TempBitmap.y = c * 16;

					switch (randNumber)
					{
						case 0:
							TempBitmap = new Floor;
							break;
						case 1:
							TempBitmap = new FloorTwo;
							break;
						case 2:
							TempBitmap = new FloorThree;
							break;
					}
					MyFloor.push(TempBitmap);
				}
			}
			
			// Añado todos los tiles a la lista de visualizacion
			for(i = 0; i < MyFloor.length; i++)
			{
				addChild( MyFloor[i] );
			}
			
			// Inicializo los enemigos
			for(i = 0; i < Oleada; i++)
			{
				MyEnemy.push(new Enemy);
			}
			
			// Agrego todos los enemigos
			for(i = 0; i < Oleada; i++)
			{
				addChild( MyEnemy[i] );
			}
			
			addChild( MyPlayer );
		}
		
		public function ProcessPlayerMoves(event:KeyboardEvent):void
		{
			
			if( event.keyCode == Keyboard.W || event.keyCode == Keyboard.UP )
			{
				MyPlayer.MovePlayerUp();
			}
			
			if( event.keyCode == Keyboard.D || event.keyCode == Keyboard.RIGHT )
			{
				MyPlayer.MovePlayerRight();
			}
			
			if( event.keyCode == Keyboard.S || event.keyCode == Keyboard.DOWN )
			{
				MyPlayer.MovePlayerDown();
			}
			
			if( event.keyCode == Keyboard.A || event.keyCode == Keyboard.LEFT )
			{
				MyPlayer.MovePlayerLeft();
			}
			
			MyPlayer.DoMove();
			
		}
		
		public function StopProcessPlayerMoves(event:KeyboardEvent):void
		{
			if( event.keyCode == Keyboard.W || event.keyCode == Keyboard.UP )
			{
				MyPlayer.StopMovingPlayerUp();
			}
			
			if( event.keyCode == Keyboard.A || event.keyCode == Keyboard.RIGHT )
			{
				MyPlayer.StopMovingPlayerLeft();
			}
			
			if( event.keyCode == Keyboard.S || event.keyCode == Keyboard.DOWN )
			{
				MyPlayer.StopMovingPlayerDown();
			}
			
			if( event.keyCode == Keyboard.D || event.keyCode == Keyboard.LEFT )
			{
				MyPlayer.StopMovingPlayerRight();
			}
			
		}
		
		public function MoveEnemies():void
		{
			for(var i:int = 0; i < Oleada; i++)
			{
				MyEnemy[i].GoToPlayer(MyPlayer.x - 20, MyPlayer.y  );
			}
			
			
			
		}
		
		protected function IncrementScore(event:TimerEvent):void
		{
			Score += 100;
		}
		
		public function ProcessEnemies():void
		{
			
			TextScore.text = "Score: " + Score;
			TextScore.defaultTextFormat = HPTextFormat;
			TextScore.x = 500;
			TextScore.autoSize = TextFieldAutoSize.CENTER;
			TextScore.y = 512 - TextScore.height;
			addChild( TextScore );
			
			Vidas.text = "Salud: " + MyPlayer.getHP();
			Vidas.defaultTextFormat = HPTextFormat;
			Vidas.x = 0;
			Vidas.autoSize = TextFieldAutoSize.CENTER;
			Vidas.y = 512 - Vidas.height;
			addChild(Vidas);
			
			MyTimer.addEventListener(TimerEvent.TIMER, IncrementScore);
			
			for( var i:int = 0; i < MyEnemy.length; i++)
			{
				if( MyEnemy[i].hitTestObject(MyPlayer) )
				{
					MyPlayer.getHit( MyEnemy[i].getDamage() );
				}
			}
			
			if( MyPlayer.IsDead() )
			{
				if(contains(MyPlayer ))
				{
					removeChild( MyPlayer );
					Vidas.alpha = 0.0;
					TextScore.alpha = 0.0;
						
					for( i = 0; i < MyEnemy.length; i++)
					{
						removeChild( MyEnemy[i] );
					}
					
					var FinalColor:Sprite = new Sprite();
					FinalColor.graphics.beginFill(0x000000);
					FinalColor.graphics.drawRect(0, 0, 800, 512);
					FinalColor.graphics.endFill();
					FinalColor.x = 0;
					FinalColor.y = 0;
					
					var EndTextFormat:TextFormat = new TextFormat();
					
					EndTextFormat.bold = true;
					EndTextFormat.size = 72;
					EndTextFormat.font = "Courier New" ;
					EndTextFormat.color = 0xFF0000;
					
					var EndText:TextField = new TextField();
					EndText.defaultTextFormat = EndTextFormat;
					EndText.autoSize = TextFieldAutoSize.CENTER;
					EndText.mouseEnabled = false;
					EndText.text = "Perdiste!";
					EndText.x = 400 - ( EndText.width / 2 );
					EndText.y = 256 - ( EndText.height / 2 );
					
					addChild( FinalColor );
					addChild( EndText );
					
				}
			} 
			else if( contains(MyPlayer ) )
				{
					addChild( MyPlayer );
				}
		}
	}
}