package widgets.supportClasses
{
	public class WebMapResult
	{
		public function WebMapResult(webmapitem:WebMapItem, webmapdata:WebMapData)
		{
			if (webmapitem)
			{
				this.item = webmapitem.toObject();
			}
			else 
			{
				this.item = {};	
			}
			
			if (webmapdata)
			{
				this.itemData = webmapdata.toObject();
			}
			else
			{
				this.itemData = {};
			}
		}	
		
		public var item:Object;
		public var itemData:Object;
	}
}