package devoron.data.core.history 
{
	import devoron.data.core.history.HistoryPoint;
	
	/**
	 * IHistory
	 * @author Devoron
	 */
	public interface IHistory 
	{
		function undo():void;
		function redo():void;
		function registerPoint(p:HistoryPoint):void;
		function getPoints():Array;
	}
	
}