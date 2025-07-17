package devoron.components.labels 
{
	import flash.filters.BitmapFilterQuality;
	import flash.filters.BlurFilter;
	import org.aswing.ASColor;
	import org.aswing.ASFont;
	import org.aswing.ASFontAdvProperties;
	import org.aswing.Icon;
	import org.aswing.JLabel;
	
	import devoron.studio.tools.RegistrationFonts;
	
	/**
	 * ...
	 * @author ...
	 */
	public class DSLabel extends JLabel 
	{
		
		public function DSLabel(text:String="", icon:Icon=null, horizontalAlignment:int=JLabel.LEFT) 
		{
			super(text, icon, horizontalAlignment);
			//super.setForeground(new ASColor(0xFFFFFF, 0.8));
			//super.setForeground(new ASColor(0xFFFFFF, 0.5));
			super.setForeground(new ASColor(0xFFFFFF, 0.45));
		}
		
	}

}