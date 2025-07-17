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
	 * AboutButtonUI2
	 * @author Devoron
	 */
	public class AboutButtonUI2 extends BasicToggleButtonUI 
	{
		//public var defaultTextColor:ASColor = new ASColor(0XFFFFFF, 0.2);
		public var defaultTextColor:ASColor = new ASColor(0x4a626e, 1);
		//public var selectedTextColor:ASColor = new ASColor(0xFFFFFF, 0.6)
		//public var selectedTextColor:ASColor = new ASColor(0XFFFFFF, 0.7)
		public var selectedTextColor:ASColor = new ASColor(0x5a868f, 0.7)
		public var defaultBgColor:ASColor = new ASColor(0xFFFFFF, 0);
		//public var selectedBgColor:ASColor = new ASColor(0xFFFFFF, 0.20)
		public var selectedBgColor:ASColor = new ASColor(0X000000, 0.04)
		public var decorator:ColorDecorator;
		
		public function AboutButtonUI2() 
		{
			super();
			//decorator = new ColorDecorator(defaultBgColor, new ASColor(0xFFFFFF, 0), 2);
			//decorator = new ColorDecorator(null, new ASColor(0xFFFFFF, 0.4), 2);
			decorator = new ColorDecorator(null, new ASColor(0xFFFFFF, 0), 2);
			//decorator.setBorderColor(new ASColor(0x4a626e, 1));
			decorator.setBorderColor(new ASColor(0x5a868f, 0.8));
			decorator.setGaps(-2, 1, 1, -2);
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
				
				//decorator.setBorderColor(new ASColor(0x4a626e, 1));
				//trace("выбран " + isSelected());
				KTween.to(b, 0.45, {alpha: 1}, Linear.easeIn).init();
			}
			else
			{
				b.setForeground(defaultTextColor);
				decorator.setColor(defaultBgColor);
				//decorator.setBorderColor(new ASColor(0x4a626e, 0.5));
				
				
				KTween.to(b, 0.45, {alpha: 0.5}, Linear.easeIn).init();
			}
			
		}
		
	}

}