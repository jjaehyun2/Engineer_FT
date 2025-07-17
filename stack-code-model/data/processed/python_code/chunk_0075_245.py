package devoron.dataui.clipboard
{
	import devoron.dataui.clipboard.IDataContainerClipboard;
	import devoron.data.core.base.IDataContainer;
	import org.aswing.AssetIcon;
	import org.aswing.event.AWEvent;
	import org.aswing.geom.IntDimension;
	import org.aswing.Icon;
	import org.aswing.JButton;
	import org.aswing.JPanel;
	import org.aswing.layout.FlowLayout;
	
	/**
	 * ClipboardPanel
	 * @author Devoron
	 */
	public class ClipboardPanel extends JPanel
	{
		[Embed(source="../../../assets/icons/commons/copy_icon12.png")]
		private var COPY_ICON12:Class;
		
		private static var clipboard:IDataContainerClipboard;
		
		private var copyBtn:JButton;
		private var pasteBtn:JButton;
		private var dataContainer:IDataContainer;
		
		public function ClipboardPanel()
		{
			super(new FlowLayout(FlowLayout.LEFT));
			
			installComponents();
			
			//if (!ClipboardPanel.clipboard)
				//StudioMediator.getStudioComponent("Clipboard", setClipboard);
		}
		
		private function installComponents():void
		{
			copyBtn = createButton("copy", new AssetIcon(new COPY_ICON12, 12, 12), copyBtnHandler);
			pasteBtn = createButton("paste", new AssetIcon(new COPY_ICON12), pasteBtnHandler);
			super.appendAll(copyBtn, pasteBtn);
		}
		
		private function setClipboard(clipboard:*):void
		{
			//ClipboardPanel.clipboard = clipboard;
		}
		
		public function setRelatedDataContainer(dataContainer:IDataContainer):void
		{
			this.dataContainer = dataContainer;
		}
		
		private function copyBtnHandler(e:AWEvent):void
		{
			if (clipboard)
				clipboard.copy(dataContainer);
		}
		
		private function pasteBtnHandler(e:AWEvent):void
		{
			if (clipboard)
				clipboard.paste(dataContainer);
		}
		
		private function createButton(text:String, icon:Icon, listener:Function):JButton
		{
			var btn:JButton = new JButton("", icon);
			btn.setSize(new IntDimension(16, 16));
			btn.setPreferredSize(new IntDimension(16, 16));
			btn.alpha = 0;
			btn.setShiftOffset(1);
			btn.setToolTipText(text);
			return btn;
		}
	
	}

}