package devoron.components.comboboxes
{
	import devoron.file.FileInfo;
	import flash.display.Bitmap;
	import flash.events.MouseEvent;
	import flash.filters.ColorMatrixFilter;
	import net.kawa.tween.easing.Linear;
	import net.kawa.tween.KTween;
	import org.aswing.AbstractListCell;
	import org.aswing.ASColor;
	import org.aswing.AssetIcon;
	import org.aswing.border.LineBorder;
	import org.aswing.Component;
	import org.aswing.decorators.ColorBackgroundDecorator;
	import org.aswing.decorators.ColorDecorator;
	import org.aswing.ext.Form;
	import org.aswing.JLabel;
	import org.aswing.JList;
	import org.aswing.ListCell;
	
	public class CellFact extends AbstractListCell
	{
		protected var selectedColor:ASColor = new ASColor(0XFFFFFF, 0.15);
		protected var unselectedColor:ASColor = new ASColor(0xFFFFFF, 0.14);
		protected var comp:Form;
		
		protected var nameLB:JLabel;
		
		public function CellFact()
		{
			comp = new Form();
			//comp.addEventListener(MouseEvent.MOUSE_OUT, onMOut);
			//comp.addEventListener(MouseEvent.MOUSE_OVER, onMOver);
			nameLB = new JLabel();
			nameLB.setForeground(new ASColor(0XFFFFFF, 0.6));
			//nameLB.setSelectable(true);
			nameLB.setOpaque(false);
			//nameLB
			//nameLB.setBackground(new ASColor(0x000000, 0.4));
			clb = new ColorDecorator(new ASColor(0x000000, 0), null, 2);
			comp.setBackgroundDecorator(clb);
			comp.addLeftHoldRow(0, 5, nameLB);
			comp.buttonMode = true;
			
			
			comp.addEventListener(MouseEvent.ROLL_OVER, onRollOver);
			comp.addEventListener(MouseEvent.ROLL_OUT, onRollOut);
			comp.alpha = 0.54;
		}
		
		private function onRollOut(e:MouseEvent):void
		{
			if (isSelected)
				comp.alpha = 1;
			else
				KTween.to(comp, 0.15, {alpha: 0.54}, Linear.easeIn).init();
		
		/*if (v)
		   {
		   alpha = 0;
		   super.setVisible(true);
		   KTween.to(this, 0.15, {alpha: 1}, Linear.easeIn).init();
		   }
		   else
		   {
		   //super.setVisible(false);
		   KTween.to(this, 0.08, {alpha: 0}, Linear.easeIn, onAlphaReduceComplete).init();
		 }*/
		}
		
		private function onRollOver(e:MouseEvent):void
		{
			KTween.to(comp, 0.15, {alpha: 1}, Linear.easeIn).init();
		}
		
		private function onMOver(e:MouseEvent):void
		{
			//KTween.to(clb, 0.15, {alpha: 1}, Linear.easeIn).init();
			nameLB.setForeground(new ASColor(0XFFFFFF, 0.8));
			clb.setColor(new ASColor(0x000000, 0.14));
		}
		
		private function onMOut(e:MouseEvent):void
		{
			clb.setColor(new ASColor(0x000000, 0));
			nameLB.setForeground(new ASColor(0XFFFFFF, 0.4));
		}
		
		public override function getCellComponent():Component
		{
			return comp;
		}
		private var rootDirectory:FileInfo;
		private var clb:ColorDecorator;
		private var isSelected:Boolean;
		
		public override function getCellValue():*
		{
			return rootDirectory;
		}
		
		public override function setCellValue(value:*):void
		{
			//if (!value)
				//return;
			//rootDirectory = FileInfo(value);
		/**
		 * Было !!
		 *
		 * nameLB.setText(value.text);
		 */
		
			nameLB.setText(value);
			//nameLB.setIcon(value.icon);
		
			//nameLB.setText(rootDirectory.name);
			//var bi:Bitmap = new Bitmap(rootDirectory.icons[1]);
			//bi.filters = [new ColorMatrixFilter([0.3086, 0.6094, 0.0820, 0, 0, 0.3086, 0.6094, 0.0820, 0, 0, 0.3086, 0.6094, 0.0820, 0, 0, 0, 0, 0, 1, 0])];
		
			//nameLB.setIcon(new AssetIcon(bi));
		}
		
		public function setListCellStatus2(list:JList, isSelected:Boolean, index:int):void
		{
			//clb.setColor( isSelected ? selectedColor : unselectedColor);
			nameLB.setForeground(isSelected ? list.getSelectionForeground() : list.getForeground());
			//comp.setBorder(new LineBorder(null, isSelected ? selectedColor : unselectedColor, 1, 2));
		}
		
		public override function  setListCellStatus(list:JList, isSelected:Boolean, index:int):void
		{
			this.isSelected = isSelected;
			//var com:Component = getCellComponent();
			if (isSelected)
			{
				/*nameLB.setBackground(list.getSelectionBackground());
				 nameLB.setForeground(list.getSelectionForeground());*/
				
				//nameLB.setForeground(new ASColor(0xFFFFFF, 0.4));
				clb.setColor(new ASColor(0x000000, 0.14));
				
			}
			else
			{
				nameLB.setBackground(list.getBackground());
				//nameLB.setForeground(list.getForeground());
				//nameLB.setForeground(new ASColor(0xFFFFFF, 0.4));
				clb.setColor(new ASColor(0x000000, 0));
			}
			nameLB.setFont(list.getFont());
		}
	
	}
}