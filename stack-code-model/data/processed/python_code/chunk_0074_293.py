package devoron.components.buttons
{
	import org.aswing.ASColor;
	import org.aswing.event.AWEvent;
	import org.aswing.Icon;
	import org.aswing.JRadioButton;
	
	/**
	 * ...
	 * @author Devoron
	 */
	public class DSRadioButton extends JRadioButton
	{
		
		public function DSRadioButton(text:String = "", icon:Icon = null)
		{
			super(text, icon);
			setForeground(new ASColor(0xFFFFFF, 0.4));
			
			addActionListener(omg);
		}
		
		private function omg(e:AWEvent):void
		{
			if (isSelected())
				setForeground(new ASColor(0xFFFFFF, 0.6));
			else
				setForeground(new ASColor(0xFFFFFF, 0.4));
		}
	}

}