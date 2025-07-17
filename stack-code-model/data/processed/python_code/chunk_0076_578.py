package widgets.Identify.components.supportClasses
{
	import com.esri.ags.Graphic;
	import com.esri.ags.geometry.Geometry;
	import com.esri.ags.geometry.MapPoint;
	import com.esri.ags.symbols.Symbol;
	
	import flash.events.EventDispatcher;
	import flash.events.IEventDispatcher;
	
	public class IdentifyFeature extends EventDispatcher
	{
		public function IdentifyFeature(target:IEventDispatcher=null)
		{
			super(target);
		}
		
		public var title:String;
		
		public var point:MapPoint;
		
		public var links:Array;
		
		public var geometry:Geometry;
		
		public var graphic:Graphic;
		
		public var attributes:Array;
		
		public var source:String;
		
		public var layerID:int;
		
		public var layername:String;
		
		public var image:String;
		
		public var titlefield:String;
		
		public var objectIdField:String;
	}
}