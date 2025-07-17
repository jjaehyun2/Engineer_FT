package devoron.components.filechooser.renderers 
{
	import org.aswing.GeneralListCellFactory;
	/**
	 * ...
	 * @author Devoron
	 */
	public class FileChooserListCellFactory extends GeneralListCellFactory
	{
		
		public function FileChooserListCellFactory(listCellClass:Class, shareCelles:Boolean=true, sameHeight:Boolean=true, height:int=22) 
		{
			super(listCellClass, shareCelles, sameHeight, height);
		}
		
		
		
	}

}