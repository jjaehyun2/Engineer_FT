package  
{
	import net.flashpunk.Entity;
	import net.flashpunk.World;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class MainMenu extends World 
	{
		private var _level:Level;
		private var _player:Player;
		private var _backdrop:Entity;
		private var _messageBox:MessageBox;
		private var _overlay:Overlay;
		private var _itemBar:ItemBar;
		public function MainMenu() 
		{
			_backdrop = new Entity(0, 0, new Background());
			_backdrop.layer = 999999;
			add(_backdrop);
			
			_level = new Level();
			add(_level);
			
			
		}
		
		override public function begin():void 
		{
			_player = new Player(_level.getPlayerLocation());
			add(_player);
			
			_messageBox = new MessageBox();
			add(_messageBox);
			
			_overlay = new Overlay();
			add(_overlay);
			
			_itemBar = new ItemBar();
			add(_itemBar);
		}
		
		public function getMessageBox():MessageBox
		{
			return _messageBox;
		}
		public function getPlayer():Player
		{
			return _player;
		}
		public function getLevel():Level
		{
			return _level;
		}
		
	}

}