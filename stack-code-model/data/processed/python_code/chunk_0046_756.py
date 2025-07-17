package ageofai.unit.view 
{
	import ageofai.bar.BaseBarView;
	/**
	 * ...
	 * @author Tibor Túri
	 */
	public class LifeBarView extends BaseBarView
	{
		
		public function LifeBarView() 
		{	
			this.barWidth = 20;
			this.barHeight = 3;
			this.backgroundColor = 0x222222;
			this.barColor = 0x669900;
			this.createChildren( );	
		}
		
	}

}