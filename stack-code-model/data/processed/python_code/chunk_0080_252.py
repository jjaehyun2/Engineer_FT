package fplib.maping 
{
	import adobe.utils.CustomActions;
	import flash.display.BitmapData;
	import net.flashpunk.Entity;
	import net.flashpunk.FP;
	import net.flashpunk.graphics.Backdrop;
	import net.flashpunk.graphics.Image;
	import net.flashpunk.graphics.Tilemap;
	import net.flashpunk.masks.Grid;
	import net.flashpunk.Sfx;
	import net.flashpunk.World;
	
	/**
	 * ...
	 * @author Diogo Muller
	 */
	public class OgmoMap extends World
	{
		//{ region Attributes
		protected var _mapWidth : int = 0;
		protected var _mapHeight : int = 0; 
		protected var _tileSize : int = 0;
		
		protected var _background : Backdrop;
		protected var _backgroundEntity : Entity;
		
		protected var _mapGrid : Grid;
		protected var _mapImage : Image;
		protected var _mapGridEntity : Entity;
		
		protected var _mainTileLayer : Tilemap;
		protected var _mainTileLayerEntity : Entity;
		
		protected var _secondaryTileLayer : Tilemap;
		protected var _secondaryTileLayerEntity : Entity;
		
		protected var _entityCreator : EntityCreator;
		
		protected var _sfx : Sfx;
		//} endregion Attributes
		
		//{ region Constructor
		public function OgmoMap( levelAsset : Class, mainTileSetAsset : Class, secondaryTileSetAsset : Class, backgroundAsset : Class, entityCreator : EntityCreator, bgmAsset : Class = null ) 
		{ 
			_entityCreator = entityCreator;
			createMap( levelAsset, mainTileSetAsset, secondaryTileSetAsset, backgroundAsset, bgmAsset );
		}
		//} endregion Constructor
		
		//{ region Constructor Helper Methods
		/**
		 * Constructor auxiliary function, initializes world from a OGMO map.
		 * @param	levelAsset Level (OGMO file) asset reference.
		 * @param	mainTileSetAsset Main Tileset asset reference.
		 * @param	secondaryTileSetAsset Secondary Tileset asset reference.
		 * @param	backgroundAsset Background asset reference.
		 */
		protected function createMap( levelAsset : Class, mainTileSetAsset : Class, secondaryTileSetAsset : Class, backgroundAsset : Class, bgmAsset : Class ) : void
		{
			//TODO: Load from any number of tilesets?
			
			if ( bgmAsset ) 
			{
				_sfx = new Sfx(bgmAsset);
				_sfx.loop();
			}
			
			// Loads XML.
			var xmlData : XML = FP.getXML( levelAsset );
			
			// Map properties
			_mapWidth = xmlData["@width"];
			_mapHeight = xmlData["@height"];
			// TODO: Load from file?
			_tileSize = 16;
			
			// Loads a backdrop.
			_background = new Backdrop(backgroundAsset);
			// TODO: Create property so we can change this anytime.
			_background.scrollX = 0.5;
			_background.scrollY = 0.5;
			_backgroundEntity = new Entity( 0, 0, _background );
			_backgroundEntity.layer = 1001;
			add(_backgroundEntity);
			
			// Loads collision layer.
			_mapGrid = new Grid( _mapWidth, _mapHeight, _tileSize, _tileSize );
			_mapGrid.loadFromString( String( xmlData["Collision"] ), "", "\n" );
			_mapImage = new Image( _mapGrid.data );
			_mapImage.scale = _tileSize;
			_mapGridEntity = new Entity( 0, 4, _mapImage, _mapGrid );
			_mapGridEntity.visible = false;
			_mapGridEntity.type = "solid";
			_mapGridEntity.layer = 1000;
			add(_mapGridEntity);
			
			// Load main tileset layer
			var x : XML;
			
			_mainTileLayer = new Tilemap( mainTileSetAsset, _mapWidth, _mapHeight, _tileSize, _tileSize);
			for each( x in xmlData["MainLayer"]["tile"] )
			{
				_mainTileLayer.setTile( int( x["@x"] ), int( x["@y"]), int( x["@id"] ) );
			}
			_mainTileLayerEntity = new Entity(0, 0, _mainTileLayer );
			_mainTileLayerEntity.layer = 999;
			add(_mainTileLayerEntity);
			
			// Load secondary tileset layer
			_secondaryTileLayer = new Tilemap( secondaryTileSetAsset, _mapWidth, _mapHeight, _tileSize, _tileSize);
			for each( x in xmlData["SecondaryLayer"]["tile"] )
			{
				_secondaryTileLayer.setTile( int( x["@x"] ), int( x["@y"]), int( x["@id"] ) );
			}
			_secondaryTileLayerEntity = new Entity(0, 0, _secondaryTileLayer );
			_secondaryTileLayerEntity.layer = -999;
			add(_secondaryTileLayerEntity);
			
			createEntities(xmlData["Entities"]);
		}
		
		public function createEntities( xmlData : XMLList ) : void
		{
			var newEntity : Entity = null;
			
			for each( var xml : XML in xmlData.elements() )
			{
				newEntity = _entityCreator.CreateEntity( xml.name(), xml );
				
				if ( newEntity ) add(newEntity);
			}
		}
		//} endregion Constructor Helper Methods
		
		
		public function stopMusic() : void
		{
			_sfx.stop();
		}
	}

}