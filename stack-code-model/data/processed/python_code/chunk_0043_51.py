package devoron.components.tables.arrays
{
	
	import devoron.components.tables.variables.ArrayTableCellEditor;
	import flash.events.Event;
	import flash.ui.Keyboard;
	import org.aswing.CellEditor;
	import org.aswing.Container;
	import org.aswing.event.AWEvent;
	import org.aswing.event.CellEditorListener;
	import org.aswing.event.FocusKeyEvent;
	import org.aswing.event.PopupEvent;
	import org.aswing.geom.IntRectangle;
	import org.aswing.table.TableCellEditor;
	import org.aswing.tree.TreeCellEditor;
	import org.aswing.util.ArrayUtils;
	
	/**
	 * @author iiley
	 */
	public class DefaultArrayCellEditor implements CellEditor, TableCellEditor, TreeCellEditor
	{
		private var listeners:Array;
		private var clickCountToStart:int;
		
		protected var arrayEditor:ArrayTableCellEditor;
		
		public function DefaultArrayCellEditor()
		{
			listeners = new Array();
			clickCountToStart = 2;
		}
		
		/**
		 * Specifies the number of clicks needed to start editing.
		 * Default is 0.(mean start after pressed)
		 * @param count  an int specifying the number of clicks needed to start editing
		 * @see #getClickCountToStart()
		 */
		public function setClickCountToStart(count:Number):void
		{
			clickCountToStart = count;
		}
		
		/**
		 * Returns the number of clicks needed to start editing.
		 * @return the number of clicks needed to start editing
		 */
		public function getClickCountToStart():Number
		{
			return clickCountToStart;
		}
		
		/**
		 * Calls the editor's component to update UI.
		 */
		public function updateUI():void
		{
			arrayEditor.updateUI();
		}
		
		public function getCellEditorValue():*
		{
			return arrayEditor.getValues();
		}
		
		/**
		 * Sets the value of this cell. Subclass must override this method to
		 * make editor display this value.
		 * @param value the new value of this cell
		 */
		protected function setCellEditorValue(value:*):void
		{
			if (value as Array)
			{
				if (value.length>0)
				{
					if (value[0] is String)
					{
						
					}
					if (value[0] is Object)
					{
						for each (var v:Object in value)
						{
							var type:String = String(v.type);
							if (type.indexOf("::") != -1)
							{
								v.type = type.split("::")[1];
							}
							
						}
					}
				}
			}
			
			arrayEditor.setValues(value as Array);
		}
		
		public function isCellEditable(clickCount:int):Boolean
		{
			return clickCount == clickCountToStart;
		}
		
		public function startCellEditing(owner:Container, value:*, bounds:IntRectangle):void
		{
			if (!arrayEditor)
				arrayEditor = new ArrayTableCellEditor();
			arrayEditor.show();
			arrayEditor.setLocationRelativeTo();
			arrayEditor.toFront();
			setCellEditorValue(value);
			
			//arrayEditor.addEventListener(PopupEvent.POPUP_OPENED, 
			arrayEditor.addEventListener(PopupEvent.POPUP_CLOSED, __editorComponentAct, false, 0, true);
			
			//"popupOpened", lightPickerManager.show, "popupClosed", lightPickerManager.hide);
			
			arrayEditor.removeEventListener(AWEvent.ACT, __editorComponentAct);
			arrayEditor.removeEventListener(AWEvent.FOCUS_LOST, __editorComponentFocusLost);
			arrayEditor.removeEventListener(FocusKeyEvent.FOCUS_KEY_DOWN, __editorComponentKeyDown);
			
			arrayEditor.addEventListener(AWEvent.ACT, __editorComponentAct);
			arrayEditor.addEventListener(AWEvent.FOCUS_LOST, __editorComponentFocusLost);
			arrayEditor.addEventListener(FocusKeyEvent.FOCUS_KEY_DOWN, __editorComponentKeyDown);
			arrayEditor.validate();
		}
		
		private function __editorComponentFocusLost(e:Event):void
		{
			//gtrace("__editorComponentFocusLost");
			cancelCellEditing();
		}
		
		private function __editorComponentAct(e:Event):void
		{
			stopCellEditing();
		}
		
		private function __editorComponentKeyDown(e:FocusKeyEvent):void
		{
			if (e.keyCode == Keyboard.ESCAPE)
			{
				cancelCellEditing();
			}
		}
		
		public function stopCellEditing():Boolean
		{
			removeEditorComponent();
			fireEditingStopped();
			return true;
		}
		
		public function cancelCellEditing():void
		{
			removeEditorComponent();
			fireEditingCanceled();
		}
		
		public function isCellEditing():Boolean
		{
			return arrayEditor != null && arrayEditor.isShowing();
		}
		
		public function addCellEditorListener(l:CellEditorListener):void
		{
			listeners.push(l);
		}
		
		public function removeCellEditorListener(l:CellEditorListener):void
		{
			ArrayUtils.removeFromArray(listeners, l);
		}
		
		protected function fireEditingStopped():void
		{
			for (var i:Number = listeners.length - 1; i >= 0; i--)
			{
				var l:CellEditorListener = CellEditorListener(listeners[i]);
				l.editingStopped(this);
			}
		}
		
		protected function fireEditingCanceled():void
		{
			for (var i:Number = listeners.length - 1; i >= 0; i--)
			{
				var l:CellEditorListener = CellEditorListener(listeners[i]);
				l.editingCanceled(this);
			}
		}
		
		protected function removeEditorComponent():void
		{
			//arrayEditor.removeFromContainer();
			arrayEditor.stopCellEditing();
		}
	}
}