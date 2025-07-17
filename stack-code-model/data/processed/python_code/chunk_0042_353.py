package widgets.AddShapefile 
{
	import com.esri.ags.geometry.Extent;
	import com.esri.ags.geometry.MapPoint;
	import com.esri.ags.symbols.Symbol;
	
	import flash.events.EventDispatcher;
	
	[Bindable] public class ShapeFileResult extends EventDispatcher
	{
		public var title:String;
		
		public var symbol:Symbol = null;
		
		public var extent:Extent = null;
		
		public var content:String;
		
		public var removemsg:String;
		
		public var layerids:Array = [];
	}
}