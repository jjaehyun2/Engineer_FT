package
{
	public class LevelMap
	{
		protected var _tiles:Vector.<VoxelCube>;
		protected var _sprites:Vector.<SpriteBillboard>;
		protected var _camera:ViewpointCamera;
		protected var _widthInTiles:uint;
		protected var _heightInTiles:uint;
		
		public function LevelMap(Width:uint = 16, Height:uint = 16)
		{
			_tiles = new Vector.<VoxelCube>();
			_sprites = new Vector.<SpriteBillboard>();
			_widthInTiles = Width;
			_heightInTiles = Height;
			
			var _seed:Number;
			var _textureIndex:int;
			var _voxelCube:VoxelCube;
			for (var x:int = 0; x < _widthInTiles; x++)
			{
				for (var z:int = 0; z < _heightInTiles; z++)
				{
					if (x == 0 || x == _widthInTiles - 1 || z == 0 || z == _heightInTiles - 1)
						_textureIndex = Entity.TEX_GRAY_STONE;
					else
					{
						if ((x % 8) == 4 && (z % 8) == 4)
							_textureIndex = Entity.TEX_LIT_FLOOR;
						else
							_textureIndex = Entity.TEX_EMPTY_FLOOR;
						
						_seed = Math.random();
						if (_seed < 0.05)
						{
							var _itemIndex:uint = _seed * 20 * TextureAtlas.ITEMS.length;
							_sprites.push(new SpriteBillboard(TextureAtlas.ITEMS[_itemIndex], x, 0, z));
						}
						else if (_seed < 0.07)
							_textureIndex = Entity.TEX_BLUE_STONE;
						else if (_seed < 0.09)
						{
							_sprites.push(new MovingSprite(Entity.TEX_PLAYER_WALK[0], x, 0, z, true));
						}
					}
					_voxelCube = new VoxelCube(_textureIndex, x, 0, z);
					_tiles.push(_voxelCube);
				}
			}
		}
		
		public function addSprite(SpriteToAdd:SpriteBillboard):void
		{
			_sprites.push(SpriteToAdd);
		}
		
		private function sortingFunction(EntityA:Entity, EntityB:Entity):Number
		{
			var distA:Number = EntityA.getCameraDistance(_camera);
			var distB:Number = EntityB.getCameraDistance(_camera);
			if (distA < distB) return 1;
			else if (distA > distB) return -1;
			else return 0;
		}
		
		public function getTileAt(X:int, Z:int):VoxelCube
		{
			if (X < 0 || X >= _widthInTiles || Z < 0 || Z >= _heightInTiles)
				return null;
			else
				return _tiles[X * _widthInTiles + Z];
		}
		
		public function update():void
		{
			var i:int;
			var _voxelCube:VoxelCube;
			for (i = 0; i < _tiles.length; i++)
			{
				_voxelCube = _tiles[i];
				_voxelCube.update();
			}
			
			var _sprite:SpriteBillboard;
			for (i = 0; i < _sprites.length; i++)
			{
				_sprite = _sprites[i];
				_sprite.update(this);
				for (var j:int = 0; j < i; j++)
				{
					_sprite.overlaps(_sprites[j]);
				}
			}
		}
		
		public function render(Camera:ViewpointCamera):void
		{
			Entity.preRender();
			
			_camera = Camera;
			_sprites.sort(sortingFunction);
			
			var i:int;
			var _voxelCube:VoxelCube;
			for (i = 0; i < _tiles.length; i++)
			{
				_voxelCube = _tiles[i];
				_voxelCube.renderScene(Camera);
			}
			
			var _sprite:SpriteBillboard;
			for (i = 0; i < _sprites.length; i++)
			{
				_sprite = _sprites[i];
				_sprite.renderScene(Camera);
			}
			
			Entity.postRender();
		}
	}
}