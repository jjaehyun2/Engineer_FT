package widgets.Pmgd2.Skin.Propietario
{
	
	import com.esri.ags.FeatureSet;
	import com.esri.ags.Graphic;
	import com.esri.ags.tasks.QueryTask;
	import com.esri.ags.tasks.supportClasses.Query;
	
	import mx.collections.ArrayCollection;
	import mx.controls.Alert;
	import mx.rpc.AsyncResponder;
	
	import spark.components.supportClasses.SkinnableComponent;
	
	import widgets.Pmgd2.Url.Url;
	
	
	public class ListPropietario extends SkinnableComponent
	{
		[Bindable]public static var coleccionPropietarios:ArrayCollection = new ArrayCollection;
		[SkinPart]
	
	
				
		public function ListPropietario()
		{	
			setStyle("skinClass",ListPropietarioSkin);						
		}		
		
				
		override protected function getCurrentSkinState():String
		{
			return super.getCurrentSkinState();
		} 
		
		
		
		public static function queryPropietario():void{
			// TODO Auto-generated method stub
			coleccionPropietarios.removeAll();
			//	Alert.show("query");
			var queryTask:QueryTask = new QueryTask(widgets.Pmgd2.Url.Url.ServicePropietario);
			var query:Query = new Query();
			query.where = "EMPRESA_ID = 6";
			query.outFields = ['*'];
			query.returnGeometry = true;
			queryTask.execute(query, new AsyncResponder(onResultQuery, onFaultQuery));
			
			
			function onResultQuery(featureSet:FeatureSet, token:Object = null):void
			{      
				
				var k:int;
				
				for(k=0;k<featureSet.features.length;k++)
				{
					var recordGraphic:Graphic = featureSet.features[k];
					coleccionPropietarios.addItem({OBJECTID:recordGraphic.attributes["OBJECTID"], 
						PROPIETARIO_ID:recordGraphic.attributes["PROPIETARIO_ID"], 
						PROPIETARIO_PMGD:recordGraphic.attributes["PROPIETARIO_PMGD"],
						SIGLA_PMGD:recordGraphic.attributes["SIGLA_PMGD"],
						RUT_PMGD:recordGraphic.attributes["RUT_PMGD"],
						DIRECCION_PROPIETARIO:recordGraphic.attributes["DIRECCION_PROPIETARIO"],
						REPRESENTANTE:recordGraphic.attributes["REPRESENTANTE"],
						TELEFONO:recordGraphic.attributes["TELEFONO"],
						EMAIL:recordGraphic.attributes["EMAIL"],
						gra:recordGraphic});
					
				}
				
			
				
				
			}
			function onFaultQuery(info:Object, token:Object = null):void
			{   
				Alert.show("Error en consulta lista de propietarios","Carga de propietarios");
			}
		}
	
	}
}