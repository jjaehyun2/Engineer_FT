package widgets.PMGD.Class
{
	import com.esri.ags.FeatureSet;
	import com.esri.ags.Graphic;
	import com.esri.ags.tasks.QueryTask;
	import com.esri.ags.tasks.supportClasses.Query;
	
	import flash.events.Event;
	
	import mx.collections.ArrayCollection;
	import mx.controls.Alert;
	import mx.rpc.AsyncResponder;
	import mx.utils.StringUtil;
	
	import widgets.PMGD.Skin.Propietario.ListPropietarioSkin;
	import widgets.PMGD.Url.Url;
	

	public class QPropietario
	{
		
		
	
		
		
		
		public function QPropietario()
		{
			
	
		}
		/*
		
		protected function filterGrid(event:Event):void
		{
			Alert.show("filter");
			/* To get this function to work, only edit variables filterText, columnArray, gridDataProvider, and dataGridName. 
			Everything else is dynamic. Do not edit variable names. */
		//	var filterText:String = StringUtil.trim(LpSk.txtFilterPropietario.text.toLowerCase()); //Trimmed text String to filter by
		//	var columnArray:Array = ['PERIODO_STAR','PROPIETARIO_PMGD','SIGLA_PMGD','RUT_PMGD','DIRECCION_PROPIETARIO','REPRESENTANTE','TELEFONO','EMAIL']; //Datagrid column names to filter on
			//var gridDataProvider:ArrayCollection = coleccionPropietarios as ArrayCollection; //Name of datagrid's dataprovider. In this case e.g. databases
			//var dataGridName:String = 'DataPropietario'; //Name of the datagrid you are filtering by
		/*	
			//Do not edit code past this point
			var filteredData:Array = [];
			var added:Boolean=false;
			var i:int;
			var j:int;
			
			// Loop Through Grid
			for(i=0; i < gridDataProvider.length; i++){    
				added = false;
				
				//Loop through grid column
				for(j=0; j<columnArray.length; j++){            
					if(gridDataProvider[i][columnArray[j]]!=null){
						
						//Grab datagrid cell contents, trim it, and convert to lowercase for comparison.
						var filterString:String = gridDataProvider[i][columnArray[j]].toString().toLowerCase();
						
						//Compare the datagrid string(filterString) to the user typed string(filterText).  
						if(!added){      
							//If the datagrid string matches the users string, put it into the array.
							if(filterString.indexOf(filterText) != -1){
								filteredData.push(gridDataProvider[i]);
								added = true;
							} 
						}else{
							//Do nothing, break out.
							break;
						}
					}    
				}
			}
		/*	
			//Set datagrid dataprovider
			if(filterText.length == 0){
				this[dataGridName].dataProvider = gridDataProvider; //Display the original unfiltered data
			}else{
				this[dataGridName].dataProvider = filteredData; //Pusht he filtered data into the datagrid
			}
		}
		*/
		
		
		public static function queryPropietarioID(p:String):int
		{
			var pid:int;
			var queryTask:QueryTask = new QueryTask(widgets.PMGD.Url.Url.ServicePropietario);
			var query:Query = new Query();
			query.where = "EMPRESA_ID = 6 AND PROPIETARIO_PMGD='" + p + "'";
			query.outFields = ['*'];
			query.returnGeometry = false;
			queryTask.execute(query, new AsyncResponder(onResultQuery, onFaultQuery));
			
				
			function onResultQuery(featureSet:FeatureSet, token:Object = null):void
			{      
				pid = featureSet.features[0].attributes["PROPIETARIO_ID"];
					
			}
			function onFaultQuery(info:Object, token:Object = null):void
			{   
				Alert.show("Error en consulta","Carga de propietarios");
			}
			
			return pid;
		}
		
	}
}