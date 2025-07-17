package devoron.dataui.multicontainers.gridlist
{
	import org.aswing.event.AWEvent;
	import org.aswing.event.ListDataEvent;
	import org.aswing.event.ListDataListener;
	import org.aswing.ext.GridList;
	import org.aswing.JTable;
	
	public class DataContainersGridListChangeListener implements ListDataListener
	{
		private var gridList:GridList;
		
		public function DataContainersGridListChangeListener(gl:GridList)
		{
			gridList = gl;
		}
		
		/* INTERFACE org.aswing.event.ListDataListener */
		
		public function contentsChanged(e:ListDataEvent):void
		{
			gridList.dispatchEvent(new AWEvent(AWEvent.ACT));
		}
		
		public function intervalAdded(e:ListDataEvent):void
		{
			gridList.dispatchEvent(new AWEvent(AWEvent.ACT));
		}
		
		public function intervalRemoved(e:ListDataEvent):void
		{
			gridList.dispatchEvent(new AWEvent(AWEvent.ACT));
		}
	
	}
}