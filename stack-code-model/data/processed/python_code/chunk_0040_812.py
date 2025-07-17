package devoron.components.tables
{
	import devoron.studio.moduls.gui.components.forms.values.IntDimensionForm;
	import devoron.components.frames.StudioFrame;
	import devoron.components.pcfs.ImagePCF;
	import flash.events.Event;
	import org.aswing.AbstractCellEditor;
	import org.aswing.ASColor;
	import org.aswing.border.EmptyBorder;
	import org.aswing.Component;
	import org.aswing.Container;
	import org.aswing.decorators.ColorDecorator;
	import org.aswing.event.AWEvent;
	import org.aswing.ext.Form;
	import org.aswing.geom.IntDimension;
	import org.aswing.geom.IntRectangle;
	import org.aswing.Insets;
	import org.aswing.JNumberStepper;
	import org.aswing.JTextField;
	
	/**
	 * IntDimensionCellEditor
	 * @author Devoron
	 */
	public class PathCellEditor extends AbstractCellEditor
	{
		protected var iconPCF:ImagePCF;
		
		public function PathCellEditor()
		{
			super();
			setClickCountToStart(2);
		}
		
		override public function startCellEditing(owner:Container, value:*, bounds:IntRectangle):void
		{
			//bounds.y += 1;
			bounds.height += 2;
			
			/*
			 */
			bounds.height += 20;
			
			bounds.x -= 1.48;
			//bounds.width += 5;
			bounds.width = 180;
			
			/*
			 */
			bounds.width = 400;
			
			//bounds.height += 4;
			//bounds.y += 4;
			super.startCellEditing(owner, value, bounds);
		
		/*	widthST.removeEventListener(AWEvent.ACT, __editorComponentAct);
		 heightST.removeEventListener(AWEvent.ACT, __editorComponentAct);*/
			 //arrayEditor.removeEventListener(AWEvent.FOCUS_LOST, __editorComponentFocusLost);
			 //arrayEditor.removeEventListener(FocusKeyEvent.FOCUS_KEY_DOWN, __editorComponentKeyDown);
		/*
		   widthST.addEventListener(AWEvent.ACT, __editorComponentAct);
		 heightST.addEventListener(AWEvent.ACT, __editorComponentAct);*/
			 //arrayEditor.addEventListener(AWEvent.FOCUS_LOST, __editorComponentFocusLost);
			 //arrayEditor.addEventListener(FocusKeyEvent.FOCUS_KEY_DOWN, __editorComponentKeyDown);
			 //arrayEditor.validate();
		}
		
		private function __editorComponentAct(e:Event):void
		{
			stopCellEditing();
		}
		
		/**
		 * Subclass override this method to implement specified value transform
		 */
		protected function transforValueFromText(text:String):*
		{
			return text;
		}
		
		override public function getEditorComponent():Component
		{
			if (iconPCF == null)
			{
				//intDimensionForm = new Form();
				
				/*widthST = new JNumberStepper();
				   widthST.setPreferredWidth(70);
				   heightST = new JNumberStepper();
				   heightST.setPreferredWidth(70);
				   widthST.addActionListener(widthSTHandler);
				   heightST.addActionListener(heightSTHandler);
				
				   intDimensionForm.addLeftHoldRow(0, widthST, 10, heightST);
				
				 intDimensionForm.setSize(new IntDimension(150, 22));*/
				
				iconPCF = new ImagePCF("");
				/*var cbd:ColorDecorator = new ColorDecorator(new ASColor(0x262F2B, 1), new ASColor(0xFFFFFF, 0.4));
				   cbd.bottomGap = -1;
				   cbd.rightGap = -1;
				 intDimensionForm.setBackgroundDecorator(cbd);*/
				
				var id:ColorDecorator = new ColorDecorator(StudioFrame.defaultColor, new ASColor(0XFFFFFF, 0.24), 2);
				//var id:ColorDecorator = new ColorDecorator(new ASColor(0X000000, 0.08), new ASColor(0XFFFFFF, 0.24), 4);
				//id.setGaps(-2, 1, 1, -2);
				id.setGaps( -1, 0, 0, -1);
				StudioFrame.decorators.push(id);
				popup.setBackgroundDecorator(id);
				
				//intDimensionForm.setBorder(new EmptyBorder(null, new Insets(2, 0, 0, 0)));
				iconPCF.addActionListener(onValueChange);
				
				/*var iconPCF:ImagePCF = new ImagePCF(s + "x" + s);
				   comps["$url_" + s + "x" + s] = iconPCF;
				 iconsForm.addLeftHoldRow(0, iconPCF);*/
			}
			return iconPCF;
		}
		
		private function onValueChange(e:AWEvent):void
		{
			fireEditingStopped();
		}
		
		override public function getCellEditorValue():*
		{
			return iconPCF.getPath();
		}
		
		/**
		 * Sets the value of this cell.
		 * @param value the new value of this cell
		 */
		override protected function setCellEditorValue(value:*):void
		{
			//this.value = value;
			iconPCF.setPath(value);
		}
		
		public function toString():String
		{
			return "IntDimensionCellEditor[]";
		}
	}
}