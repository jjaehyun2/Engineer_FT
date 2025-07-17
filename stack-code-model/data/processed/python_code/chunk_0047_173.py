package devoron.values.models
{
	import devoron.studio.core.managers.scenebrowser.ContentTree;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import org.aswing.event.AWEvent;
	import org.aswing.tree.TreeModel;
	import devoron.values.models.TreeModelValue;
	
	[Event(name="act",type="org.aswing.event.AWEvent")]
	
	/**
	 * Компонент, который содержит только данные
	 * без представления.
	 * @author Devoron
	 */
	public class TreeModelValueComponent extends EventDispatcher
	{
		private var contentTree:ContentTree;
		protected var model:TreeModelValue;
		
		public function TreeModelValueComponent(contentTree:ContentTree)
		{
			this.contentTree = contentTree;
		}
		
		public function setModel(model:TreeModelValue/*value:*, dispatchAWEvent:Boolean = true*/):void
		{
			contentTree.setModel(model.getRelatedModel());
			if (this.model == model)
				return;
			this.model = model;
			/*if (dispatchAWEvent)
				super.dispatchEvent(new AWEvent(AWEvent.ACT));*/
		}
		
		public function getModel():TreeModelValue
		{
			return model;
		}
		
		public function changeData(value:*):void
		{
			//super.dispatchEvent(new AWEvent(AWEvent.ACT));
		}
		
		public function addActionListener(listener:Function, useCapture:Boolean = false, priority:int = 0, useWeakReference:Boolean = false):void
		{
			super.addEventListener(AWEvent.ACT, listener, useCapture, priority, useWeakReference);
		}
		
		public function removeActionListener(listener:Function):void
		{
			super.removeEventListener(AWEvent.ACT, listener);
		}
	
	}

}