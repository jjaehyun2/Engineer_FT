package widgets.PMGD.Skin.Central
{
	import com.esri.ags.FeatureSet;
	import com.esri.ags.Graphic;
	import com.esri.ags.tasks.QueryTask;
	import com.esri.ags.tasks.supportClasses.Query;
	
	import mx.collections.ArrayCollection;
	import mx.controls.Alert;
	import mx.rpc.AsyncResponder;
	
	import widgets.PMGD.Url.Url;

	public class ListCentral
	{
		public static var coleccioncentral:ArrayCollection = new ArrayCollection;
		public function ListCentral()
		{
		}
		
		public static function queryCentrales():void{
			var queryTask:QueryTask = new QueryTask(widgets.PMGD.Url.Url.ServiceCentral);
			var query:Query = new Query();
			query.where = "1=1";
			query.outFields = ['*'];
			query.returnGeometry = true;
			queryTask.execute(query, new AsyncResponder(onResultQuery, onFaultQuery));
			
			var arrProp:Array = new Array;
			
			function onResultQuery(featureSet:FeatureSet, token:Object = null):void
			{
				
				//coleccion.addAll(new ArrayCollection(featureSet.attributes));
				//DataPropietario.dataProvider = coleccion;
				
				//var ac:ArrayCollection = new ArrayCollection();
				var k:int;
				coleccioncentral.removeAll();
				for(k=0;k<featureSet.features.length;k++)
				{
					
					var recordGraphic:Graphic = featureSet.features[k];
					coleccioncentral.addItem({OBJECTID:recordGraphic.attributes["OBJECTID"], 
						EMPRESA_ID:recordGraphic.attributes["EMPRESA_ID"], 
						PERIODO_STAR:recordGraphic.attributes["PERIODO_STAR"],
						CENTRAL_ID:recordGraphic.attributes["CENTRAL_ID"],
						FECHA_RECEPCION:recordGraphic.attributes["FECHA_RECEPCION"],
						NOMBRE_CENTRAL:recordGraphic.attributes["NOMBRE_CENTRAL"],
						DIRECCION_CENTRAL:recordGraphic.attributes["DIRECCION_CENTRAL"],
						COMUNA_ID:recordGraphic.attributes["COMUNA_ID"],
						SISTEMA_ID:recordGraphic.attributes["SISTEMA_ID"],
						POTENCIA_INSTALADA:recordGraphic.attributes["POTENCIA_INSTALADA"],
						NIVEL_TENSION:recordGraphic.attributes["NIVEL_TENSION"],
						TIPO_ENERGETICO_PRIMARIO_ID:recordGraphic.attributes["TIPO_ENERGETICO_PRIMARIO_ID"],
						ALIMENTADOR_ID:recordGraphic.attributes["ALIMENTADOR_ID"],
						PUNTO_CONEXION:recordGraphic.attributes["PUNTO_CONEXION"],
						NUMERO_UNIDADES:recordGraphic.attributes["NUMERO_UNIDADES"],
						FECHA_PUESTA_SERVICIO:recordGraphic.attributes["FECHA_PUESTA_SERVICIO"],
						ESTADO_ID:recordGraphic.attributes["ESTADO_ID "],
						PROPIETARIO_ID:recordGraphic.attributes["PROPIETARIO_ID"],
						CAPACIDAD_INSTALADA:recordGraphic.attributes["CAPACIDAD_INSTALADA"],
						NOMBRE_ESTADO:recordGraphic.attributes["NOMBRE_ESTADO"],
						NOMBRE_ALIMENTADOR:recordGraphic.attributes["NOMBRE_ALIMENTADOR"],
						NOMBRE_TIPO_ENERGETICO:recordGraphic.attributes["NOMBRE_TIPO_ENERGETICO"],
						NOMBRE_PROPIETARIO:recordGraphic.attributes["NOMBRE_PROPIETARIO"],
						gra:recordGraphic });
				}
				
				
			}
			function onFaultQuery(info:Object, token:Object = null):void
			{   
				Alert.show("Error en consulta","Carga de Centrales");
			}
		}
	}
}