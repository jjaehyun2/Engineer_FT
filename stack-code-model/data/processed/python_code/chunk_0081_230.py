package devoron.components.buttons
{
	import devoron.components.buttons.CircleButtonUI;
	import devoron.components.buttons.StateToggleButton;
	import flash.events.MouseEvent;
	import flash.filters.GlowFilter;
	import net.kawa.tween.easing.Linear;
	import net.kawa.tween.KTween;
	import org.aswing.ASColor;
	import org.aswing.AssetIcon;
	import org.aswing.Icon;
	import org.aswing.JButton;
	import org.aswing.JLabel;
	
	/**
	 * CircleButton
	 * @author CircleButton
	 */
	public class CircleButton extends StateToggleButton
	{
		[Embed(source="../../../../assets/icons/commons/logo.png")]
		private var CREATING_ICON:Class;
		[Embed(source="../../../../assets/icons/commons/logo.png")]
		private var CREATING_ROLLOVER_ICON:Class;
		private var cbd:CircleBackgroundDecorator;
		
		public function CircleButton(text:String = "", icon:Icon = null, animate:Boolean = true)
		{
			super(text, icon);
			cbd = new CircleBackgroundDecorator(new ASColor(0x070E0D, 0.6), new ASColor(0xFFFFFF, 0.14), 95);
			super.setBackgroundDecorator(cbd);
			setUI(new CircleButtonUI());
			
			setHorizontalAlignment(JLabel.CENTER);
			setVerticalAlignment(JLabel.TOP);
			setIcon(new AssetIcon(new CREATING_ICON, 47, 47, false));
			setRollOverIcon(new AssetIcon(new CREATING_ROLLOVER_ICON, 47, 47, false));
			setSelectedIcon(new AssetIcon(new CREATING_ROLLOVER_ICON, 47, 47, false));
			
			if (animate)
			{
				super.addEventListener(MouseEvent.MOUSE_OVER, onMouseOver);
				super.addEventListener(MouseEvent.MOUSE_OUT, onMouseOut);
				super.alpha = 0.42;
			}
			//var showBrushesBtn:StateToggleButton = new StateToggleButton("", new AssetIcon(new brushIcon, 20, 20));
			//showBrushesBtn.setRelatedObject(editor.options.brushes, PopupEvent.POPUP_OPENED, showBrushes, PopupEvent.POPUP_CLOSED, editor.options.brushes.hide);
		}
		
		override public function setIcon(defaultIcon:Icon):void
		{
			super.setIcon(defaultIcon);
			//defaultIcon.
			//getIcon().getDisplay(this).y = 20;
			//getIcon().getDisplay(this).x = 20;
		}
		
		private function onMouseOut(e:MouseEvent):void
		{
			//(e.currentTarget as JButton).setAlpha(
			KTween.to(e.currentTarget, 0.15, { alpha: 0.42 }, Linear.easeIn).init();
			cbd.setColor(new ASColor(0x070E0D, 0.6));
			cbd.getDisplay(this).filters = [];
		
		}
		
		private function onMouseOver(e:MouseEvent):void
		{
			KTween.to(e.currentTarget, 0.15, { alpha: 0.9 }, Linear.easeIn).init();
			cbd.setColor(new ASColor(0x070E0D, 0));
			cbd.getDisplay(this).filters = [new GlowFilter(0xFFFFFF, 0.86, 6, 6, 1, 2, false)];
		}
	
	}

}