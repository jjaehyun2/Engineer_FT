package ageofai.building.view 
{
	import ageofai.bar.BaseBarView;
	/**
	 * ...
	 * @author Tibor Túri
	 */
	public class BuildProgressBarView extends BaseBarView
	{
		
		public function BuildProgressBarView() 
		{
			this.barWidth = 20;
			this.barHeight = 3;
			this.backgroundColor = 0x222222;
			this.barColor = 0x00CCFF;
			this.createChildren( );				
		}
		
	}

}