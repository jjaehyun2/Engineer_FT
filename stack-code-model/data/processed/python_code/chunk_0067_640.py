package devoron.data.core.base 
{
	import devoron.data.core.base.IDataProcessorsProvider;
	/**
	 * DataProcessorsProvider
	 * @author Devoron
	 */
	public class DataProcessorsProvider implements IDataProcessorsProvider
	{
		
		public function DataProcessorsProvider() 
		{
			
		}
		
		/* INTERFACE devoron.data.core.IDataProcessorsProvider */
		
		public function getDataProcessor(title:String, editorCls:Class, fullpath:String, isDir:Boolean, useControlPanel:Boolean = false):IDataProcessor 
		{
			return null;
		}
		
	}

}