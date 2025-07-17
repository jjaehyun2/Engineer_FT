package devoron.components.buttons 
{
	import net.kawa.tween.easing.Linear;
	import net.kawa.tween.KTween;
	import org.aswing.AbstractButton;
	import org.aswing.ASColor;
	import org.aswing.ButtonModel;
	import org.aswing.Component;
	import org.aswing.decorators.ColorDecorator;
	import org.aswing.geom.IntRectangle;
	import org.aswing.graphics.Graphics2D;
	import org.aswing.plaf.basic.BasicToggleButtonUI;
	
	/**
	 * AboutButtonUI
	 * @author Devoron
	 */
	public class AboutButtonUI extends BasicToggleButtonUI 
	{
		public var defaultTextColor:ASColor = new ASColor(0xFFFFFF, 0.4);
		public var selectedTextColor:ASColor = new ASColor(0xFFFFFF, 0.6)
		public var defaultBgColor:ASColor = new ASColor(0xFFFFFF, 0.1);
		public var selectedBgColor:ASColor = new ASColor(0xFFFFFF, 0.20)
		public var decorator:ColorDecorator;
		
		public function AboutButtonUI() 
		{
			super();
			decorator = new ColorDecorator(defaultBgColor, new ASColor(0xFFFFFF, 0), 2);
		}
		
		override public function paint(c:Component, g:Graphics2D, r:IntRectangle):void{
			super.paint(c, g, r);
			
			var b:AbstractButton = AbstractButton(c);
			var model:ButtonModel = b.getModel();
			b.setBackgroundDecorator(decorator);
		
			if (model.isSelected())
			{
				b.setForeground(selectedTextColor);
				decorator.setColor(selectedBgColor);
				//trace("выбран " + isSelected());
				KTween.to(b, 0.25, {alpha: 1}, Linear.easeIn).init();
			}
			else
			{
				b.setForeground(defaultTextColor);
				decorator.setColor(defaultBgColor);
				KTween.to(b, 0.25, {alpha: 0.44}, Linear.easeIn).init();
			}
			
		}
		
	}

}