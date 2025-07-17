package devoron.dataui.clipboard
{
	import devoron.data.core.base.IDataContainer;
	
	/**
	 * IDataContainerClipboard
	 * @author Devoron
	 */
	public interface IDataContainerClipboard
	{
		function copyFromDataContainersTable(data:*, _dataType:String):void
		function pasteToDataContainersTable(_dataType:String):*
		function copy(source:IDataContainer):void
		function paste(target:IDataContainer):void
	}

}