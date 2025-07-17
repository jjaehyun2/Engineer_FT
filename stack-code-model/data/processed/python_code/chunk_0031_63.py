package cn.seisys.TGISViewer.components
{
	import com.esri.ags.portal.supportClasses.PopUpInfo;
	
	public class PopUpInfoWithButtons extends PopUpInfo
	{
		public function PopUpInfoWithButtons()
		{
			super();
		}
		
		public var buttonArray:Array;
		
		public var idFieldName:String;
		
		public var showDetailLink:Boolean;
	}
}