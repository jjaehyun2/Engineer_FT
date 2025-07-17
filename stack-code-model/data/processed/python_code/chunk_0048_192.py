package devoron.aslc.moduls.output
{
	//import devoron.studio.moduls.code.core.editor.as3editor.AS3Editor;
	import devoron.data.core.base.IDataProcessor;
	//import devoron.studio.core.data.dsprocessor.BaseDataStructurProcessor;
	//import devoron.components.icons.WatchingIcon;
	import devoron.file.FileInfo;
	//import devoron.studio.core.project.processor.StudioProjectProcessor;
	import flash.events.MouseEvent;
	import flash.net.navigateToURL;
	import net.kawa.tween.KTween;
	import net.kawa.tween.easing.Linear;
	import org.aswing.ASColor;
	import org.aswing.AssetIcon;
	import org.aswing.Component;
	import org.aswing.DefaultListCell;
	import org.aswing.Icon;
	import org.aswing.JLabel;
	import org.aswing.JScrollPane;
	import org.aswing.JTree;
	import org.aswing.border.EmptyBorder;
	import org.aswing.decorators.ColorDecorator;
	import org.aswing.tree.DefaultTreeCell;
	
	public class CompilerMessagesListCellRenderer extends DefaultListCell
	{
		//[Embed(source = "../../../../../../assets/icons/FileChooser/rename_icon16.png")]
		private var bg:ColorDecorator;
		private var selected:Boolean;
		
		public function CompilerMessagesListCellRenderer()
		{
			//setPreferredWidth(267);
			//setMinimumWidth(267);
			
			
		
			//mouseEnabled = true;
			//mouseChildren = false;
		
		}
		
		override protected function initJLabel(jlabel:JLabel):void
		{
			super.initJLabel(jlabel);
			jlabel.doubleClickEnabled = true;
			jlabel.addEventListener(MouseEvent.DOUBLE_CLICK, onDoubleClick);
			jlabel.addEventListener(MouseEvent.ROLL_OVER, onRollOver);
			jlabel.addEventListener(MouseEvent.ROLL_OUT, onRollOut);
			jlabel.alpha = 0.54;
			jlabel.setIconTextGap(2);
			bg = new ColorDecorator(new ASColor(0x000000, 0), null, 2);
			jlabel.setBackgroundDecorator(bg);
		}
		
		private function onRollOut(e:MouseEvent):void
		{
			var lb:JLabel = e.currentTarget as JLabel;
			bg.setColor(new ASColor(0x000000, 0));
			if (selected)
				lb.alpha = 1;
			else
				KTween.to(lb, 0.15, {alpha: 0.54}, Linear.easeIn).init();
		}
		
		private function onDoubleClick(e:MouseEvent):void
		{
			//StudioProjectProcessor.instance.openFile((value as FileInfo).nativePath);
		}
		
		private function onRollOver(e:MouseEvent):void
		{
			var lb:JLabel = e.currentTarget as JLabel;
			//comp.setOpaque(true);
			bg.setColor(new ASColor(0x000000, 0.14));
			//comp.setBackground(new ASColor(0x000000, 0.08));
			KTween.to(lb, 0.15, {alpha: 1}, Linear.easeIn).init();
		
		}
		
		/*public override function setTreeCellStatus(tree:JTree, selected:Boolean, expanded:Boolean, leaf:Boolean, row:int):void
		   {
		   super.setTreeCellStatus(tree, selected, expanded, leaf, row);
		   if (value is ScriptNode)
		   {
		   super.setIcon(new AssetIcon(new SCRIPT_ICON16, 16, 16));
		   getCellComponent().addEventListener(MouseEvent.MOUSE_OVER, onMouseOver, false, 0, false);
		   }
		
		   //setBackground(new ASColor(0x59CB56, 0.3));
		   }
		 */
		
		/*override public function getLeafIcon():Icon
		   {
		   //return super.getLeafIcon();
		   if (value)
		   {
		   var fi:FileInfo = value as FileInfo;
		   if (fi.isDirectory)
		   {
		   return new AssetIcon(new FOLDER_ICON16, 16, 16);
		   }
		   else
		   return new AssetIcon(new SCRIPT_ICON16, 16, 16);
		   }
		   return null;
		   }*/
		
		//public override function setTreeCellStatus(tree:JTree, selected:Boolean, expanded:Boolean, leaf:Boolean, row:int):void
		//{
		//this.selected = selected;
		//super.setTreeCellStatus(tree, selected, expanded, leaf, row);
		//
		//if (selected)
		//{
		////setBackground(tree.getSelectionBackground());
		////setForeground(tree.getSelectionForeground());
		//
		////setBackground(tree.getBackground());
		////setForeground(tree.getForeground());
		//
		//setBackground(new ASColor(0, 0));
		//setForeground(new ASColor(0xFFFFFF, 0.5));
		//bg.setColor(tree.getSelectionForeground());
		//}
		//else
		//{
		////setBackground(tree.getBackground());
		////setForeground(tree.getForeground());
		//
		//setBackground(new ASColor(0, 0));
		//setForeground(new ASColor(0xFFFFFF, 0.24));
		//bg.setColor(new ASColor(0, 0));
		//}
		//}
		
		override public function setCellValue(value:*):void
		{
			if (value == null)
				return;
			
			//if ("userObject" in value){
			//var fi:FileInfo = value.userObject as FileInfo;
			//super.setCellValue(fi.name);
			//}
			//userObject
			
			super.setCellValue(value);
			//(super.getCellComponent() as JLabel).setIcon(new AssetIcon(new SCRIPT_ICON16));
			
			//var ic:WatchingIcon = new WatchingIcon("F:\\Projects\\projects\\flash\\studio\\DevoronStudio\\assets\\icons\\script_icon16.png", 16, 16);
			//(super.getCellComponent() as JLabel).setIcon(ic);
			//var fi:FileInfo = value.getUserObject() as FileInfo;
			//super.setCellValue(fi);
		
		/*	var file:FileInfo = value.userObject as FileInfo;
		   if (file)*/
			   //super.setCellValue(file.name);
			   //super.setCellValue(value);
		
			   //if(cel
		}
	
		//override public function getText():String
		//{
		//if (value)
		//{
		//return (value as FileInfo).name;
		//}
		//
		//return "";
		//}
	
		//private function onMouseOver(e:MouseEvent):void
		//{
		///*var cm:CircleMenu = new CircleMenu();
		//cm.show();*/
		//}
		//
		//protected override function createExpandedFolderIcon(tree:JTree):Icon
		//{
		//return new AssetIcon(new FOLDER_ICON16, 16, 16);
		//}
		//
		//protected override function createCollapsedFolderIcon(tree:JTree):Icon
		//{
		//return new AssetIcon(new COLLAPSED_FOLDER_ICON16, 16, 16);
		//}
		//
		//protected override function createLeafIcon(tree:JTree):Icon
		//{
		//return new AssetIcon(new FOLDER_ICON16, 16, 16);
		//}
	}
}