/*
   Copyright aswing.org, see the LICENCE.txt.
 */

package devoron.dataui.multicontainers.timeline
{
	
	import devoron.components.labels.DSLabel;
	import devoron.data.core.base.DataStructurObject;
	import devoron.utils.gtrace;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Shape;
	import flash.events.Event;
	import flash.events.MouseEvent;
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
	 * TimelineTrackCellRenderer
	 * @author Devoron
	 */
	public class TimelineTrackRenderer extends JPanel implements TableCell
	{
		protected var value:DataStructurObject;
		protected var label:JLabel;
		protected var enableFCHBtn:JToggleButton;
		
		public function TimelineTrackRenderer()
		{
			super(new FlowLayout(FlowLayout.LEFT));
			enableFCHBtn = new JToggleButton();
			enableFCHBtn.addActionListener(enableFCHBtnHandler);
			label = new JLabel();
			label.setForeground(new ASColor(0xFFFFFF, 0.8));
			//setDr
			//setLayout(new FlowLayout(FlowLayout.LEFT, 0, 0, true));
			//appendAll(enableFCHBtn, new JSp(2), label);
			
			//setHorizontalAlignment(LEFT);
			setOpaque(true);
			setPreferredWidth(950);
			setWidth(950);
			//super.setIconTextGap(2);
			addEventListener(MouseEvent.RIGHT_CLICK, onRigthClick);
		}
		
		private function onRigthClick(e:MouseEvent):void 
		{
			
		}
		
		private function enableFCHBtnHandler(e:AWEvent):void
		{
			//fch.setEnabled(enableFCHBtn.isSelected());
		}
		
		/**
		 * Simpler this method to speed up performance
		 */ /*override public function setComBounds(b:IntRectangle):void
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
		 }*/
		
		/**
		 * Simpler this method to speed up performance
		 */ /*override public function invalidate():void
		   {
		   valid = false;
		 }*/
		
		/**
		 * Simpler this method to speed up performance
		 */ /*override public function revalidate():void
		   {
		   valid = false;
		   }
		 */
		//**********************************************************
		//				  Implementing TableCell
		//**********************************************************
		public function setCellValue(value:*):void
		{
			if (this.value != value.data.data)
			{
				if (this.value)
				{
					this.value.removeEventListener(Event.CHANGE, onChange);
				}
				
				this.value = value.data.data;
				this.value.addEventListener(Event.CHANGE, onChange);
				setDSO(this.value);
			}
		
			//gtrace(value);
		
		/*fch = value as IFileChooserHelper;
		   enableFCHBtn.setIcon(fch.getIcon());
		   label.setText(fch.getType());
		 enableFCHBtn.setSelected(fch.isEnabled());*/
		}
		
		private function setDSO(DSO:DataStructurObject):void
		{
			//var DSO:DataStructurObject = value.data.data as DataStructurObject;
			//DSO.addEventListener(Event.CHANGE, onChange);
			
			var containers:Array = DSO.modifier;
			var selId:uint = DSO.selectedId;
			
			gtrace("2:containers " + containers.length);
			
			super.removeAll();
			
			var dso:Object;
			var lb:DSLabel;
			for (var i:int = 0; i < containers.length; i++)
			{
				dso = containers[i];
				
				lb = new DSLabel(dso.name);
				if (i == selId)
					lb.setForeground(new ASColor(0x008000, 0.4));
				super.append(lb);
				lb.setVisible(true);
			}
		
			super.invalidate();
			//super.repaintAndRevalidate();
		/*for each (var item:*in containers)
		   {
		   super.append(new DSLabel(item.name));
		 }*/
			 //repaint();
			 //revalidate();
			 //pack();
			 //super.getParent().revalidate();
			 //revalidate();
		}
		
		private function onChange(e:Event):void
		{
			gtrace("DSO change");
			setDSO(value);
		}
		
		public function getCellValue():*
		{
			//return fch;
			return null;
		}
		
		public function setTableCellStatus(table:JTable, isSelected:Boolean, row:int, column:int):void
		{
			if (isSelected)
			{
				setBackground(table.getSelectionBackground());
				setForeground(table.getSelectionForeground());
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