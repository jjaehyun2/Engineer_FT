/*
   Copyright aswing.org, see the LICENCE.txt.
 */

package devoron.components.filechooser
{
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Shape;
	import flash.filters.GlowFilter;
	import flash.geom.ColorTransform;
	import flash.geom.Rectangle;
	import org.aswing.ASColor;
	import org.aswing.AssetIcon;
	import org.aswing.Component;
	import org.aswing.event.AWEvent;
	import org.aswing.geom.*;
	import org.aswing.JLabel;
	import org.aswing.JPanel;
	import org.aswing.JSp;
	import org.aswing.JSpacer;
	import org.aswing.JSprH;
	import org.aswing.JTable;
	import org.aswing.JToggleButton;
	import org.aswing.layout.FlowLayout;
	import org.aswing.table.TableCell;
	
	/**
	 * FileChooserHelpersTableCellRender
	 * @author Devoron
	 */
	public class FileChooserHelpersTableCellRender extends JPanel implements TableCell
	{
		
		protected var fch:IFileChooserHelper;
		protected var label:JLabel;
		protected var enableFCHBtn:JToggleButton;
		
		public function FileChooserHelpersTableCellRender()
		{
			super();
			enableFCHBtn = new JToggleButton();
			enableFCHBtn.addActionListener(enableFCHBtnHandler);
			label = new JLabel();
			label.setForeground(new ASColor(0xFFFFFF, 0.8));
			
			setLayout(new FlowLayout(FlowLayout.LEFT, 0, 0, true));
			appendAll(enableFCHBtn, new JSp(2), label);
			
			//setHorizontalAlignment(LEFT);
			setOpaque(true);
			//super.setIconTextGap(2);
		}
		
		private function enableFCHBtnHandler(e:AWEvent):void 
		{
			fch.setEnabled(enableFCHBtn.isSelected());
		}
		
		/**
		 * Simpler this method to speed up performance
		 */
		override public function setComBounds(b:IntRectangle):void
		{
			readyToPaint = true;
			if (!b.equals(bounds))
			{
				if (b.width != bounds.width || b.height != bounds.height)
				{
					repaint();
				}
				bounds.setRect(b);
				locate();
				valid = false;
			}
		}
		
		/**
		 * Simpler this method to speed up performance
		 */
		override public function invalidate():void
		{
			valid = false;
		}
		
		/**
		 * Simpler this method to speed up performance
		 */
		override public function revalidate():void
		{
			valid = false;
		}
		
		//**********************************************************
		//				  Implementing TableCell
		//**********************************************************
		public function setCellValue(value:*):void
		{
			fch = value as IFileChooserHelper;
			enableFCHBtn.setIcon(fch.getIcon());
			label.setText(fch.getType());
			enableFCHBtn.setSelected(fch.isEnabled());
		}
		
		public function getCellValue():*
		{
			return fch;
		}
		
		public function setTableCellStatus(table:JTable, isSelected:Boolean, row:int, column:int):void
		{
			if (isSelected)
			{
				//setBackground(table.getSelectionBackground());
				//setForeground(table.getSelectionForeground());
			}
			else
			{
				setBackground(table.getBackground());
				setForeground(table.getForeground());
			}
			setFont(table.getFont());
		}
		
		public function getCellComponent():Component
		{
			return this;
		}
		
		override public function toString():String
		{
			return "ColorCell[label:" + super.toString() + "]\n";
		}
	}
}