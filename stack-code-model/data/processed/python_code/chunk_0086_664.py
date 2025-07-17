package widgets.supportClasses
{
	import com.esri.ags.layers.Layer;
	
	import flash.utils.getQualifiedClassName;
	
	public class WebMapData
	{
		//--------------------------------------------------------------------------
		//
		//  Constructor
		//
		//--------------------------------------------------------------------------

		public function WebMapData()
		{
			this._wkid = 2193; // default to NZTM
		}
		
		//--------------------------------------------------------------------------
		//
		//  Properties
		//
		//--------------------------------------------------------------------------
		
		//--------------------------------------------------------------------------
		//  Operational Layers
		//--------------------------------------------------------------------------
		
		private var _operationalLayers:Array = [];
		
		public function get OperationalLayers():Array
		{
			return this._operationalLayers;
		}
		
		
		//--------------------------------------------------------------------------
		//  Basemap
		//--------------------------------------------------------------------------
		
		private var _basemap:Object = {};
		
		public function get BaseMap():Object
		{
			return this._basemap;
		}

		
		//--------------------------------------------------------------------------
		//  Spatial reference
		//--------------------------------------------------------------------------
		
		private var _wkid:int;
		
		public function get WKID():int
		{
			return this._wkid;
		}

		public function set WKID(value:int):void
		{
			this._wkid = value;
		}
		
		
		//--------------------------------------------------------------------------
		//
		//  Methods
		//
		//--------------------------------------------------------------------------
		
		public function addOperationalLayer(layer:Layer):void
		{
			var layerObj:Object = {
				id: layer.id,
				visibility: layer.visible,
				opacity: layer.alpha,
				title: layer.name
			};
			
			// Set layer type specific values
			
			_operationalLayers.push(layerObj);
		}
		
		public function addOperationalLayerObject(layer:Object):void
		{
			_operationalLayers.push(layer);
		}
		
		public function setBasemapObject(basemap:Object):void
		{
			this._basemap = basemap;
		}
		
		
		
		
		
		public function toObject():Object
		{
			return {
				operationalLayers: this._operationalLayers,
				baseMap: this._basemap,
				version: "2.0",
				spatialReference: {
					wkid: this._wkid,
					latestWkid: this._wkid
				},
				applicationProperties: {
					viewing: {
						routing: {
							enabled: true
						},
						measure: {
							enabled: true
						},
						basemapGallery: {
							enabled: true
						},
						search: {
							enabled: true,
							disablePlaceFinder: false,
							hintText: "Place or Address",
							layers: []
						}
					}
				}
			};
		}
	}
}