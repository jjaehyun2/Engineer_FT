package devoron.components.filechooser.contentviews
{
	import org.aswing.Component;
	import org.aswing.VectorListModel;
	
	/**
	 * IContentView
	 * @author Devoron
	 */
	public interface IContentView
	{
		function setData(dataArray:Array):void
		function getViewFIComponent():Component;
		function getData():Array;
		function getName():String;
		function setConsoleComands(commands:Array):void;
		function addActionListener(listener:Function, useCapture:Boolean = false, priority:int = 0, useWeakReference:Boolean = false):void;
		function removeActionListener(listener:Function):void;
		function getSupportedModels():Array;
		function getSelectedValue():*;
		function clear():void;
		function setFilesModel(model:VectorListModel):void;
	}

}