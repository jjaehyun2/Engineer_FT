package game
{
	import game.element.MapElement;
	
	import system.loader.Res;
	import system.loader.ResManager;
	import system.loader.ResPath;
	
	public class MapManager
	{
		public static var MAXROW:Number = 8;
		public static var MAXCOLUMN:Number = 8;
		private static var _instance:MapManager = null;
		private var _mapData:Array;
		private var _unUsedMap:Array;
		private var _usedMapType:Array;
		private var _elementPool:Array;
		private var _usedElements:Array;
		private var _mapBlockElement:MapElement;
		
		public function MapManager()
		{
			_mapData = [];
			_unUsedMap = [];
			_usedMapType = [];
			_elementPool = [];
			_usedElements = [];
			_mapBlockElement = new MapElement(-1,-1,-1);
			for(var i:int=0;i<MAXROW;++i){
				for(var j:int=0;j<MAXCOLUMN;++j){
					_elementPool.push(new MapElement(i,j,-2));
				}
			}
			initMap();
			
		}
		
		public function initMap():void{
			var idx:int = 0;
			for(var i:int=0;i<MapManager.MAXROW;++i){
				_mapData[i] = [];
				for(var j:int = 0;j<MapManager.MAXCOLUMN;++j){
					_mapData[i][j] = _elementPool[idx++];
				}
			}
		}
		
		public function createMap():MapManager{
			var mapEle:MapElement
			for(var i:int=0;i<MAXROW;++i){
				for(var j:int=0;j<MAXCOLUMN;++j){
					if(_mapData[i][j].map_type!=-1){
						mapEle = createElement(i,j);
						if(i>=2&&j>=2){
							do{
								if(mapEle.map_type==_mapData[i][j-1].map_type&&_mapData[i][j-1].map_type==_mapData[i][j-2].map_type){
									mapEle = createElement(i,j,mapEle);
								}else if(mapEle.map_type==_mapData[i-1][j].map_type&&_mapData[i-1][j].map_type==_mapData[i-2][j].map_type){
									mapEle = createElement(i,j,mapEle);
								}else{
									break;
								}
							}while(true)
						}else if(i>=2){
							if(mapEle.map_type==_mapData[i-1][j].map_type&&_mapData[i-1][j].map_type==_mapData[i-2][j].map_type){
								mapEle = createElement(i,j,mapEle);
							}
						}else if(j>=2){
							if(mapEle.map_type==_mapData[i][j-1].map_type&&_mapData[i][j-1].map_type==_mapData[i][j-2].map_type){
								mapEle = createElement(i,j,mapEle);
							}
						}
					}
				}
			}
			return MapManager.instance();
		}
		
		public function showMap():MapManager{
			var arr:Array = [];
			for(var i:int=0;i<MAXROW;++i){
				arr[i] = []
				for(var j:int=0;j<MAXCOLUMN;++j){
					arr[i].push(_mapData[i][j].map_type);
				}
				trace(arr[i]);
			}
			return MapManager.instance();
		}
		
		private function createElement(x:int,y:int,mapEle:MapElement=null):MapElement{
			if(mapEle || _elementPool.length>0){
				var mapTypeIdx:int = -1;
				var removeType:int = -1;
				if(mapEle){
					removeType = mapEle.map_type;
					mapTypeIdx = _usedMapType.indexOf(removeType);
					_usedMapType.splice(mapTypeIdx,1);
				}else{
					mapEle = _elementPool.pop();
				}
				mapEle.map_type = _usedMapType[Math.floor(Math.random()*_usedMapType.length)];
				if(mapTypeIdx!=-1){
					_usedMapType.push(removeType);
				}
				_mapData[x][y] = mapEle;
				return mapEle;
			}
			return null;
		}
		
		public function loadMapConfig(level:int):MapManager{
			var res:Res = ResManager.instance().getRes(ResPath.ROOT+"config/level"+level+".json");
			_unUsedMap = res.data.map;
			_usedMapType = res.data.elements;
			for(var i:int=0;i<_unUsedMap.length;++i){
				var location:int = _unUsedMap[i];
				var row:int = MapManager.location2row(location);
				var column:int = MapManager.location2column(location);
				_mapData[row][column] = _mapBlockElement;
			}
			return MapManager.instance();
		}
		
		public static function instance():MapManager{
			if(null == _instance)
				_instance = new MapManager();
			return _instance;
		}
		
		public static function location2row(location:int):int{
			return location/MAXCOLUMN;
		}
		
		public static function location2column(location:int):int{
			return location%MAXCOLUMN;
		}
	}
}