package common.components
{
	import hu.vizoli.common.mvc.view.base.BaseView;
	import hu.vizoli.common.mvc.view.base.interfaces.IView;
	
	/**
	 * Abstract table game field.
	 * 
	 * @author vizoli
	 */
	public class ATableGameField extends BaseView implements IView
	{
		protected var _elementWidth:int;
		protected var _elementHeight:int;
		protected var _elementDistance:int;
		protected var _rowCount:int;
		protected var _columnCount:int;
		protected var _field:Array;
		
		public function ATableGameField() 
		{
			
		}
		
	}

}