package devoron.data.core.history
{
	import MAINS.other.editors.Main_PRICE2000;
	import devoron.studio.core.IHistoryProvider;
	import org.aswing.util.HashMap;
	import org.aswing.util.Stack;
	
	/**
	 * ...
	 * @author Devoron
	 */
	public class HistoryManager
	{
		//private static var historyStack:Stack;
		//static private var hp:IHistoryProvider;
		private static var currentHistory:History;
		
		public function HistoryManager()
		{
		
		}
		
		public static function undo():void
		{
		
		}
		
		public static function redo():void
		{
		
		}
		
		public static function registerProvider(hp:IHistoryProvider):void
		{
			//HistoryManager.hp = hp;
		}
		
		public static function registerPoint(p:HistoryPoint):void
		{
			
			// создать ScriptByteArray из p
			// 
			
			/*if (!historyStack)
			   historyStack = new Stack();
			
			   historyStack.append(p);
			 gtrace("history " + historyStack.size());*/
			if (currentHistory)
				currentHistory.registerPoint(p);
			// кто-то должен отрисовывать историю
		
			// именно здесь должна быть запись в БД
			//Db.registerEntity(Person); // one Entity
			//Db.registerEntitys([Person, Animal]); // many Entity
		}
	
	}

}