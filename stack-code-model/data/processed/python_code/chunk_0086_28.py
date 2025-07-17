package devoron.aslc.moduls.project.data
{
	import away3d.arcane;
	import devoron.data.CompositeParserBase;
	import devoron.world.mesh.MeshExt;
	import away3d.entities.Mesh;
	import devoron.data.AllSubParsers;
	import devoron.data.CompositeParserBase;
	
	use namespace arcane;
	
	public class SWCBuilderProjectParser extends CompositeParserBase
	{
		private var _mesh:Mesh;
		private var _projectSettingsParser:CompositeParserBase;
		
		public function SWCBuilderProjectParser(dataCollector:Object = null)
		{
			super(dataCollector);
		}
		
		public static function supportsType(extension:String):Boolean
		{
			extension = extension.toLowerCase();
			return extension == "mesh";
		}
		
		public static function supportsData(data:*):Boolean
		{
			var serializedData:Object;
			
			try
			{
				serializedData = JSON.parse(data);
			}
			catch (e:Error)
			{
				return false;
			}
			
			return serializedData.hasOwnProperty('Mesh');
		}
		
		override protected function proceedParsing():Boolean
		{
			if (_isFirstParsing)
			{
				// ЗАГЛУШКА!!!
				//return PARSING_DONE;
				
				// материал
				var materialData:Object = _data.material;
				if (!materialData)
					dieWithError("Empty material data");
				var id:Object = materialData.id;
				var subData:Object = materialData.data;
				var parserCls:Class = AllSubParsers.getRelatedParser(id, AllSubParsers.ALL_MATERIALS);
				if (!parserCls)
					dieWithError("Unknown material parser");
				_projectSettingsParser = new parserCls();
				addSubParser(_projectSettingsParser);
				_projectSettingsParser.parseAsync(subData);
				
				// геометрия
				var geometryData:Object = _data.geometry;
				
					//addDependency("dfsd", new URLRequest("D:/projects/flash/Wheater/bin/decal.jpg"), false);
				
			}
			
			if (super.proceedParsing() == PARSING_DONE)
			{
				
				_mesh = new Mesh(_geometryParser.geometry, _projectSettingsParser.material);
				
				_mesh.transform = _transformParser.transform;
				
				finalizeAsset(_mesh);
				return PARSING_DONE;
			}
			else
				return MORE_TO_PARSE;
		}
		
		public function get mesh():Mesh
		{
			return _mesh;
		}
	
	}
}