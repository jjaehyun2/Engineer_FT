package widgets.Workspace
{
	import com.esri.ags.symbols.Symbol;
	
	import widgets.supportClasses.WebMapData;
	import widgets.supportClasses.WebMapItem;
	import widgets.supportClasses.WebMapResult;

	public class WorkspaceConverterUtil
	{
		//--------------------------------------------------------------------------
		//
		//  Constructor
		//
		//--------------------------------------------------------------------------

		public function WorkspaceConverterUtil()
		{
		}
		
		/**
		 * Converts the workspace object into a webmap equivalent.  Requires the extent be supplied as wgs84 which must be projected
		 * before rather than projected within the function (since this can be done in line). 
		 */
		public static function ConvertToWebMapResult(workspace:WorkspaceData, extentminx:Number, extentminy:Number, 
													 extentmaxx:Number, extentmaxy:Number, basemaps:Array = null):WebMapResult
		{
			// Create the new webmapitem
			var webmapitem:WebMapItem = new WebMapItem(workspace.WorkspaceID, "", workspace.CreatedTime, workspace.LastModified,
				workspace.Title, workspace.Description, null, "", null, extentminx, extentminy, extentmaxx, extentmaxy,"","private");
			
			// Create the new webmapdata
			var webmapdata:WebMapData = new WebMapData();
			
			var layerSetting:Object;
			var setting:Object;
			
			// Iterate through mapservices
			for each (var mapservice:Object in workspace.MapServices)
			{
				// Check if this is a possible basemap
				if (basemaps && basemaps.indexOf(String(mapservice.url).toLowerCase()) > -1) 
				{
					// Add as a basemap to the web map, but only if it is visible
					if (mapservice.visible)
					{
						var basemap:Object = {
							title: mapservice.name,
							baseMapLayers: []
						};

						(basemap.baseMapLayers as Array).push({
							id: getServiceName(mapservice.url),
							layerType: mapservice.MapServiceLayerType,
							opacity: mapservice.alpha,
							visibility: true,
							url: mapservice.url
						});
					
						webmapdata.setBasemapObject(basemap);
					}
					else
					{
						// Ignore
					}
				}
				else
				{
					var layer:Object = {
						id: getServiceName(mapservice.url),
						layerType: mapservice.MapServiceLayerType,
						url: mapservice.url,
						visibility: mapservice.visible,
						opacity: mapservice.alpha,
						title: mapservice.name
					};

					var layers:Array = [];
					
					// Set the layer specific settings
					switch (mapservice.MapServiceLayerType)
					{
						case "ArcGISTiledMapServiceLayer":
							// Set popup infos
							if (mapservice.infoWindowSettings && mapservice.infoWindowSettings.popUpInfos)
							{
								for each (setting in mapservice.infoWindowSettings.popUpInfos)
								{
									layerSetting = {
										id: setting.layerId,
										popupInfo: {
											title: setting.title,
											fieldInfos: setting.fieldInfos,
											mediaInfos: setting.mediaInfos,
											description: setting.description,
											showAttachments: setting.showAttachments
										}
									};
									
									layers.push(layerSetting);
								}
							}
							
							break;
						
						case "ArcGISDynamicMapServiceLayer":
							// Set visible layers
							layer.visibleLayers = mapservice.visibleLayers;
							
							// Set popup infos
							if (mapservice.infoWindowSettings && mapservice.infoWindowSettings.popUpInfos)
							{
								for each (setting in mapservice.infoWindowSettings.popUpInfos)
								{
									layerSetting = {
										id: setting.layerId,
										popupInfo: {
											title: setting.title,
											fieldInfos: setting.fieldInfos,
											mediaInfos: setting.mediaInfos,
											description: setting.description,
											showAttachments: setting.showAttachments
										}
									};
									
									layers.push(layerSetting);
								}
							}
							
							break
						
						case "FeatureLayer":
							// Update the layer type definition
							layer.layerType = "ArcGISFeatureLayer";
							
							// Set the feature layer mode - default to 1 (on Demand)
							layer.mode = 1;
							
							// Do not set the layer definition details (will use default settings)
							
							// Set the popup details (if any)
							if (mapservice.infoWindowSettings && mapservice.infoWindowSettings.popUpInfos)
							{ 
								setting = mapservice.infoWindowSettings.popUpInfos[0];
								if (setting)
								{
									layer.popupInfo = {
										title: setting.title,
										fieldInfos: setting.fieldInfos,
										mediaInfos: setting.mediaInfos,
										description: setting.description,
										showAttachments: setting.showAttachments
									};
								}
							}
							break;
						
						default:
							// Do nothing
							break;						
					}
					
					if (layers.length > 0)
					{
						layer.layers = layers;
					}
					
					// Add the layer to the webmapdata object
					webmapdata.addOperationalLayerObject(layer);
				}
			}
			
			// Iterate through graphics layers
			for each (var graphicsLayer:Object in workspace.GraphicLayers)
			{
				// Create a new operational layer
				var glayer:Object = {
					id: graphicsLayer.id,
					layerType: "ArcGISFeatureLayer",
					visibility: graphicsLayer.visible,
					opacity: graphicsLayer.alpha,
					title: graphicsLayer.name,
					featureCollection: {
						layers: [],
						showLegend: false
					}
				};
				
				// Create placeholder layers
				
				
				// Iterate through each graphic in the provider and sort each of the geometry types into separate layers in a feature set
				for each (var graphic:Object in graphicsLayer.graphics)
				{
					
				}
			
			}
			
			
			
			
			
			return new WebMapResult(webmapitem, webmapdata);
		}
		
		private static function getServiceName(url:String):String
		{
			var name:String = "";
			var path:String;
			// Determine what kind of arcgis server layer is being loaded
			if (url.match(/\/MapServer$/i) != null)
			{
				path = url.replace(/\/MapServer$/i,"");
			}
			else if (url.match(/\/MapServer\/\d$/i) != null)
			{
				path = url.replace(/\/MapServer\/\d$/i,"");
			}
			else if (url.match(/\/FeatureServer$/i) != null)
			{
				path = url.replace(/\/FeatureServer$/i,"");
			}
			else if (url.match(/\/FeatureServer\/\d$/i) != null)
			{
				path = url.replace(/\/FeatureServer\/\d$/i,"");
			}
			else
			{
				trace("Invalid URL");
			}
			
			if (path)
			{
				var parts:Array = path.split("/");
				name = parts[parts.length - 1] + "_" + getUniqueID().toString();
			}
			
			return name;
		}
		
		private static function getUniqueID():int
		{
			return int(Math.random()*10000);
		}
		
		/**
		 * Create a layer stub for a graphics layer.  Used in converting graphics layers to feature collections in a webmap.
		 */
		private static function createGraphicLayerStub(geometryType:String, isText:Boolean = false):Object
		{
			var label:String;
			var name:String;
			var symbol:Object;
			
			switch(geometryType)
			{
				case "esriGeometryPoint":
					
					if (isText)
					{
						label = "Text";
						name = "Text";
						symbol = {
							horizontalAlignment: "Left",
							verticalAlignment: "baseline",
							color: [0,0,0,255],
							font: {
								weight: "bold",
								style: "normal",
								family: "Arial",
								size: 12
							},
							type: "esriTS"
						};
					}
					else
					{
						label = "Text";
						name = "Points";
						symbol = {
							horizontalAlignment: "Left",
							verticalAlignment: "baseline",
							color: [0,0,0,255],
							font: {
								weight: "bold",
								style: "normal",
								family: "Arial",
								size: 12
							},
							type: "esriTS"
						};
					}
					
					break;
				
				case "esriGeometryPolyline":
					
					break;
				
				
				case "esriGeometryPolygon":
				default:
				
					break;

			}
			
			return {
				layerDefinition: {
					objectIdField: "OBJECTID",
					templates: [],
					type: "Feature Layer",
					drawingInfo: {
						renderer: {
							field1: "TYPEID",
							type: "uniqueValue",
							uniqueValueInfos: [
								{
									description: "",
									value: "0",
									label: label,
									symbol: symbol
								}
							]
						}
					},
					displayField: "TITLE",
					visibilityField: "VISIBLE",
					name: "",
					hasAttachments: false,
					typeIdField: "TYPEID",
					capabilities: "Query,Editing",
					types: [],
					geometryType: geometryType,
					fields: [],
					extent: {
						
					}
				},
				popupInfo: {
					
				},
				featureSet: {
					
				},
				nextObjectId: 0
			};		
		}
		
	}
}