package zombie.worlds
{
	import net.flashpunk.graphics.Spritemap;
	import net.flashpunk.Sfx;
	import net.flashpunk.World;
	import net.flashpunk.Entity;
	import net.flashpunk.FP;
	import net.flashpunk.utils.Input;
	import net.flashpunk.utils.Key;
	import net.flashpunk.graphics.Text;
	import zombie.Assets;
	import zombie.CustomCreator;
	import zombie.entities.GameManager;
	import fplib.gui.Button;
	
	/**
	 * ...
	 * @author Diogo Muller
	 */
	public class Credits extends World
	{
		private var _sfx:Sfx;
		private var textBasePosY:Number;
		private var textBasePosX:Number = 0;
		
		public function Credits()
		{
			textBasePosY = FP.height / 7;
			
			CreateCategory("Game Design", "Diogo Muller de Miranda\r\nRicardo Takeda");
			CreateCategory("Developers ", "Diogo Muller de Miranda\r\nJoao Vitor Pietsiaki Moraes\r\nErik Onuki");
			CreateCategory("Game Art", "Diogo Muller de Miranda\r\nRicardo Takeda");
			CreateCategory("Music and Sound Effects", "Ricardo Takeda");
			
			var button:Button = new Button(Assets.BUTTON_NORMAL, Assets.BUTTON_OVER, Assets.BUTTON_PRESSED, "Return", FP.width / 2 - 64, textBasePosY + 20, 128, 32, Return);
			button.active = true;
			add(button);
			
			var x : Number = 80;
			var y : Number = 80;
			
			var map : Spritemap;
			var ent : Entity;
			var img : Class;
			
			for each( img in Assets.SPRITE_NPC_ZOMBIE )
			{
				map = new Spritemap(img, 16, 16);
				map.add("dance", [0, 1, 2, 3, 4, 5], 5, true);
				map.scale = 4;
				map.play("dance", true);
				
				ent = new Entity( x, y, map );
				add( ent );
				
				y += 80;
			}
			
			map = new Spritemap(Assets.SPRITE_MAIN_ZOMBIE, 16, 16);
			map.add("dance", [0, 1, 2, 3, 4, 5], 5, true);
			map.scale = 4;
			map.play("dance", true);
			
			ent = new Entity( x, y, map );
			add( ent );
			
			x = 160;
			y = 80;			
			
			for each( img in Assets.SPRITE_NPC_NORMAL )
			{
				map = new Spritemap(img, 16, 16);
				map.add("dance", [5, 4, 3, 2, 1, 0], 5, true);
				map.scale = 4;
				map.play("dance", true);
				
				ent = new Entity( x, y, map );
				add( ent );
				
				y += 80;
			}
			
			map = new Spritemap(Assets.SPRITE_MAIN_NORMAL, 16, 16);
			map.add("dance", [5, 4, 3, 2, 1, 0], 5, true);
			map.scale = 4;
			map.play("dance", true);
			
			ent = new Entity( x, y, map );
			add( ent );
			
			_sfx = new Sfx(Assets.MUSIC_CREDITS);
			_sfx.loop();
		}
		
		public function Return():void
		{
			_sfx.stop();
			FP.world = new TitleScreen();
		}
		
		private function CreateCategory(title:String, text:String):void
		{
			var cat1Title:Text = new Text(title);
			cat1Title.color = 0x00ff00;
			cat1Title.size = 24;
			var cat1TitleEnt:Entity = new Entity(0, 0, cat1Title);
			cat1TitleEnt.x = textBasePosX == 0 ? (FP.width / 2) - (cat1Title.width / 2) : textBasePosX;
			cat1TitleEnt.y = textBasePosY;
			add(cat1TitleEnt);
			textBasePosY += cat1Title.height;
			
			if (textBasePosX == 0)
				textBasePosX = cat1TitleEnt.x;
			
			var cat1Text:Text = new Text(text);
			var cat1TextEnt:Entity = new Entity(0, 0, cat1Text);
			cat1TextEnt.x = textBasePosX == 0 ? cat1TitleEnt.x : textBasePosX;
			cat1TextEnt.y = textBasePosY;
			add(cat1TextEnt);
			textBasePosY += cat1Text.height + 20;
		}
	}

}