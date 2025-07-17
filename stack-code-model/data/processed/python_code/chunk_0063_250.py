package 
{
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	import flash.geom.ColorTransform;
	import flash.net.SharedObject;
	import flash.utils.getTimer;
	import flash.ui.Keyboard;
	import flash.events.KeyboardEvent;
	import flash.geom.Point;
	/**
	 * ...
	 * @author Stephen Birsa
	 */
	[SWF(width = 800, height = 600, frameRate = 240, backgroundColor = 0xFFFFFF)]
	final public class Main extends Sprite
	{
		private var colref:ColoursRef = new ColoursRef();
		private const _STAGE_WIDTH:int = 800;
		private const _STAGE_HEIGHT:int = 600;
		private const _BLOCK_WIDTH:int = 20;
		private const _BLOCK_HEIGHT:int = 20;
		public static const trace:OnScreenTrace = new OnScreenTrace(800, 600, 0x000000, true, 0xFFFFFF);
		private const _STATS:Stats = new Stats(); //debug
		
		private var _leftKey:Boolean = false;
		private var _rightKey:Boolean = false;
		private var _upKey:Boolean = false;
		internal var player:Player = new Player();
		internal var canvas:Bitmap = new Bitmap(new BitmapData(_STAGE_WIDTH, _STAGE_HEIGHT, true, 0));
		
		private var _lowestChunk:int;
		private var _highestChunk:int;
		internal var posChunks:Array = [];
		internal var negChunks:Array = [];
		internal var chunk:int = 0;
		internal var tempBD:BitmapData;
		internal var tempCol:ColorTransform;
		internal static var chunkUpdate:Boolean = false;
		private var _lastTick:int = 0;
		private var _delta:int = 0;
		private var _lastUpdate:int = 0;
		private const _FRAME_CAP:int = 60;
		
		final public function Main() 
		{
			tempBD = new BitmapData(_BLOCK_WIDTH, _BLOCK_HEIGHT, true, 0xFF000000);
			tempCol = new ColorTransform();
			player.x = (stage.stageWidth / 2) - player.width / 2;
			player.y = (stage.stageHeight / 2) + player.height;
			stage.addChild(canvas);
			stage.addChild(player);
			stage.addChild(_STATS); //debug
			stage.addChild(trace);
			stage.addEventListener(KeyboardEvent.KEY_DOWN, keyDown);
			stage.addEventListener(KeyboardEvent.KEY_UP, keyUp);
			stage.addEventListener(MouseEvent.MOUSE_DOWN, mouseClick);
			stage.addEventListener(MouseEvent.RIGHT_MOUSE_DOWN, rightClick);
			stage.addEventListener(MouseEvent.MOUSE_UP, mouseUp);
			stage.addEventListener(MouseEvent.RIGHT_MOUSE_UP, rightUp);
			chunkUpdate = true;
			stage.addEventListener(Event.ENTER_FRAME, update);
		}
		
		final private function update(e:Event):void
		{
			if (stage.getChildIndex(_STATS) < stage.numChildren - 2)
			{
				stage.setChildIndex(_STATS, stage.numChildren - 2);
			}
			if (stage.getChildIndex(trace) < stage.numChildren - 1)
			{
				stage.setChildIndex(trace, stage.numChildren - 1);
			}
			render();
			_delta += getTimer() - _lastTick;
			_lastTick = getTimer();
			while (_delta > (1000 / _FRAME_CAP))
			{
				_delta -= 1000 / _FRAME_CAP;
				tick();
			}
			if (getTimer() - _lastUpdate > 1000)
			{
				_lastUpdate = getTimer();
			}
		}
		
		final private function render():void
		{
			if (chunkUpdate)
			{
				canvas.bitmapData.fillRect(canvas.bitmapData.rect, 0x00000000);
				maintainWorld();
				traceUpdate();
				updateChunkHeight();
				chunkUpdate = false;
			}
		}
		
		final private function updateChunkHeight():void
		{
			_lowestChunk > chunk ? _lowestChunk = chunk : _lowestChunk;
			_highestChunk < chunk ? _highestChunk = chunk : _highestChunk;
		}
		
		final private function traceUpdate():void
		{
			trace.trace("\n\n\n\n\n\n\n" + (posChunks.length + (negChunks.length > 0 ? negChunks.length - 1 : negChunks.length)) + " createdChunks");
			trace.multilineTrace("chunk" + chunk + " loadedChunk");
			trace.multilineTrace("chunk" + _lowestChunk + " lowestCreatedChunk");
			trace.multilineTrace("chunk" + _highestChunk + " highestCreatedChunk");
		}
		
		final private function tick():void
		{
			playerMovement();
			playerCollision();
			if (player.x > 800 - (player.width / 2))
			{
				player.x = player.width;
				player.y = player.y - 20;
				chunk++;
				chunkUpdate = true;
			}
			if (player.x < 0)
			{
				player.x = 800 - player.width;
				player.y = player.y - 20;
				chunk--;
				chunkUpdate = true;
			}
		}
		
		final private function rightUp(e:MouseEvent):void { }
		
		final private function mouseUp(e:MouseEvent):void { }
		
		final private function rightClick(e:MouseEvent):void
		{
			checkWorld("placeBlock");
		}
		
		final private function mouseClick(e:MouseEvent):void
		{
			checkWorld("removeBlock");
		}
		
		final private function keyDown(e:KeyboardEvent):void 
		{
			if (e.keyCode == Keyboard.D)
			{
				_rightKey = true;
			}
			if (e.keyCode == Keyboard.A)
			{
				_leftKey = true;
			}
			if (e.keyCode == Keyboard.W)
			{
				_upKey = true;
			}
			if (e.keyCode == Keyboard.LEFT)
			{
				chunk--;
				chunkUpdate = true;
			}
			if (e.keyCode == Keyboard.RIGHT)
			{
				chunk++;
				chunkUpdate = true;
			}
			if (e.keyCode == Keyboard.K)
			{
				saveGame();
			}
			if (e.keyCode == Keyboard.L)
			{
				loadGame();
			}
		}
		
		final private function loadGame():void
		{
			var so:SharedObject = SharedObject.getLocal("MiniSandboxSave", "/");
			player.x = so.data.playerX;
			player.y = so.data.playerY;
			chunk = so.data.chunk;
			for (var i:int = 0; i < so.data.posChunksLength; i++)
			{
				posChunks[i] = new Chunk(i);
				for (var x:int = 0; x < _STAGE_WIDTH / _BLOCK_WIDTH; x++)
				{
					posChunks[i].blocks[x] = [];
					for (var y:int = 0; y < _STAGE_HEIGHT / _BLOCK_HEIGHT; y++)
					{
						var breakable:Boolean = true;
						if (y > 28) {
							breakable = false;
						}
						var broken:Boolean = false;
						if (so.data.posChunks[i][x][y] == 43) {
							broken = true;
						}
						posChunks[i].blocks[x][y] = new Block(so.data.posChunks[i][x][y], broken, breakable);
					}
				}
			}
			for (i = 0; i < so.data.negChunksLength; i++)
			{
				if (i > 0)
				{
					negChunks[i] = new Chunk(i);
					for (x = 0; x < _STAGE_WIDTH / _BLOCK_WIDTH; x++)
					{
						negChunks[i].blocks[x] = [];
						for (y = 0; y < _STAGE_HEIGHT / _BLOCK_HEIGHT; y++)
						{
							breakable = true;
							if (y > 28) {
								breakable = false;
							}
							broken = false;
							if (so.data.negChunks[i][x][y] == 43) {
								broken = true;
							}
							negChunks[i].blocks[x][y] = new Block(so.data.negChunks[i][x][y], broken, breakable);
						}
					}
				}
			}
			chunkUpdate = true;
		}
		
		final private function saveGame():void
		{
			var so:SharedObject = SharedObject.getLocal("MiniSandboxSave", "/")
			so.data.playerX = player.x;
			so.data.playerY = player.y;
			so.data.chunk = chunk;
			so.data.posChunksLength = posChunks.length;
			so.data.negChunksLength = negChunks.length;
			so.data.posChunks = [];
			so.data.negChunks = [];
			for (var i:int = 0; i < posChunks.length; i++)
			{
				so.data.posChunks[i] = [];
				for (var x:int = 0; x < _STAGE_WIDTH / _BLOCK_WIDTH; x++)
				{
					so.data.posChunks[i][x] = [];
					for (var y:int = 0; y < _STAGE_HEIGHT / _BLOCK_HEIGHT; y++)
					{
						//game bug here when saving at higher chunk eg. 120
						//bug found in: posChunks[i].blocks
						//bug found in: posChunks[i].blocks[x][y]
						//bug not found in: posChunks[i];
						//bug not found in: posChunks;
						//[Fault] exception, information=TypeError: Error #1010: A term is undefined and has no properties.
						so.data.posChunks[i][x][y] = posChunks[i].blocks[x][y].colId;
					}
				}
			}
			for (i = 0; i < negChunks.length; i++)
			{
				so.data.negChunks[i] = [];
				for (x = 0; x < _STAGE_WIDTH / _BLOCK_WIDTH; x++)
				{
					so.data.negChunks[i][x] = [];
					for (y = 0; y < _STAGE_HEIGHT / _BLOCK_HEIGHT; y++)
					{
						if (i > 0)
						{
							so.data.negChunks[i][x][y] = negChunks[i].blocks[x][y].colId;
						}
					}
				}
			}
			so.flush();
			//so.clear(); //clear save to start from scratch (test file size saving)
			trace.trace(so.size + " byteDump\nGame Saved Successfully");
		}
		
		final private function keyUp(e:KeyboardEvent):void 
		{
			if (e.keyCode == Keyboard.D)
			{
				_rightKey = false;
			}
			if (e.keyCode == Keyboard.A)
			{
				_leftKey = false;
			}
			if (e.keyCode == Keyboard.W)
			{
				_upKey = false;
			}
		}
		
		final private function playerCollision():void //player collision with canvas and vertical movement
		{
			if (player.COLLISION.hitTest(new Point(player.x, player.y + 20), 255, canvas, new Point(canvas.x, canvas.y)))
			{
				player.leftCol = true;
			}
			else {
				player.leftCol = false;
			}
			if (player.COLLISION.hitTest(new Point(player.x + 20, player.y + 20), 255, canvas, new Point(canvas.x, canvas.y)))
			{
				player.rightCol = true;
			}
			else {
				player.rightCol = false;
			}
			if (player.COLLISION.hitTest(new Point(player.x + 10, player.y + 40), 255, canvas, new Point(canvas.x, canvas.y)))
			{
				player.downCol = true;
			}
			else {
				player.downCol = false;
			}
			if (player.COLLISION.hitTest(new Point(player.x + 10, player.y), 255, canvas, new Point(canvas.x, canvas.y)))
			{
				player.upCol = true;
			}
			else {
				player.upCol = false;
			}
			if (player.downCol)
			{
				if (player.ySpeed > 0)
				{
					player.ySpeed *= -0.5;
				}
				if (_upKey)
				{
					player.ySpeed = player.JUMP_SPEED;
				}
				player.xSpeed *= player.FRICTION;
				player.ySpeed *= player.FRICTION;
			}
			else if (player.downCol == false)
			{
				player.ySpeed += player.GRAVITY;
				player.xSpeed *= player.FRICTION;
			}
			if (player.leftCol) {
				if (player.xSpeed < 0) {
					player.xSpeed *= -0.5;
				}
			}
			if (player.rightCol) {
				if (player.xSpeed > 0) {
					player.xSpeed *= -0.5;
				}
			}
			if (player.upCol) {
				if (player.ySpeed < 0) {
					player.ySpeed *= -0.5;
				}
			}
		}
		
		final private function playerMovement():void //main player movement
		{
			player.x += player.xSpeed;
			player.y += player.ySpeed;
			if (_rightKey)
			{
				player.xSpeed += player.SPEED;
			}
			if (_leftKey)
			{
				player.xSpeed -= player.SPEED;
			}
			if (Math.abs(player.xSpeed) < 0.5)
			{
				player.xSpeed = 0;
			}
			if (player.xSpeed > player.MAX_SPEED)
			{
				player.xSpeed = player.MAX_SPEED;
			}
			else if (player.xSpeed < -player.MAX_SPEED)
			{
				player.xSpeed = -player.MAX_SPEED;
			}
		}
		
		final private function checkWorld(type:String):void //check whether to place or remove block
		{
			if (chunk > -1)
			{
				for (var x:int = 0; x < _STAGE_WIDTH / _BLOCK_WIDTH; x++)
				{
					for (var y:int = 0; y < _STAGE_HEIGHT / _BLOCK_HEIGHT; y++)
					{
						if (checkChunksToMouse("pos", x, y) && checkPlayerToMouse())
						{
							if (type == "removeBlock" && posChunks[chunk].blocks[x][y].broken == false && posChunks[chunk].blocks[x][y].breakable == true)
							{
								posChunks[chunk].blocks[x][y].colId = 43;
								posChunks[chunk].blocks[x][y].broken = true;
								chunkUpdate = true;
							}
							if (type == "placeBlock" && posChunks[chunk].blocks[x][y].broken == true && checkBlockDirections("pos", x, y) && posChunks[chunk].blocks[x][y].breakable == true)
							{
								posChunks[chunk].blocks[x][y].colId = Math.floor(Math.random() * 43);
								posChunks[chunk].blocks[x][y].broken = false;
								chunkUpdate = true;
							}
						}
					}
				}
			}
			if (chunk < 0)
			{
				for (x = 0; x < _STAGE_WIDTH / _BLOCK_WIDTH; x++)
				{
					for (y = 0; y < _STAGE_HEIGHT / _BLOCK_HEIGHT; y++)
					{
						if (checkChunksToMouse("neg", x, y) && checkPlayerToMouse())
						{
							if (type == "removeBlock" && negChunks[Math.abs(chunk)].blocks[x][y].broken == false && negChunks[Math.abs(chunk)].blocks[x][y].breakable == true)
							{
								negChunks[Math.abs(chunk)].blocks[x][y].colId = 43;
								negChunks[Math.abs(chunk)].blocks[x][y].broken = true;
								chunkUpdate = true;
							}
							if (type == "placeBlock" && negChunks[Math.abs(chunk)].blocks[x][y].broken == true && checkBlockDirections("neg", x, y) && negChunks[Math.abs(chunk)].blocks[x][y].breakable == true)
							{
								negChunks[Math.abs(chunk)].blocks[x][y].colId = Math.floor(Math.random() * 43);
								negChunks[Math.abs(chunk)].blocks[x][y].broken = false;
								chunkUpdate = true;
							}
						}
					}
				}
			}
		}
		
		final private function checkBlockDirections(type:String, x:int, y:int):Boolean //check if placing a block next to a block (not placing in air)
		{
			if (type == "neg")
			{
				if (negChunks[Math.abs(chunk)].blocks[x - 1][y].broken == false)
				{
					return true;
				}
				if (negChunks[Math.abs(chunk)].blocks[x + 1][y].broken == false)
				{
					return true;
				}
				if (negChunks[Math.abs(chunk)].blocks[x][y - 1].broken == false)
				{
					return true;
				}
				if (negChunks[Math.abs(chunk)].blocks[x][y + 1].broken == false)
				{
					return true;
				}
			}
			if (type == "pos")
			{
				if (posChunks[chunk].blocks[x - 1][y].broken == false)
				{
					return true;
				}
				if (posChunks[chunk].blocks[x + 1][y].broken == false)
				{
					return true;
				}
				if (posChunks[chunk].blocks[x][y - 1].broken == false)
				{
					return true;
				}
				if (posChunks[chunk].blocks[x][y + 1].broken == false)
				{
					return true;
				}
			}
			return false;
		}
		
		final private function checkPlayerToMouse():Boolean //check reach on how far you can place blocks (mouse) away from player.x, y
		{
			if (player.x > mouseX - 60 && player.x < mouseX + 40 && player.y > mouseY - 80 && player.y < mouseY + 50)
			{
				return true;
			}
			return false
		}
		
		final private function checkChunksToMouse(type:String, x:int, y:int):Boolean //check mouse bounds x and y against 1 block x and y
		{
			if (type == "pos" && x * _BLOCK_WIDTH > mouseX - 20 && x * _BLOCK_WIDTH < mouseX + 1 && y * _BLOCK_HEIGHT > mouseY - 20 && y * _BLOCK_HEIGHT < mouseY + 1)
			{
				return true;
			}
			if (type == "neg" && x * _BLOCK_WIDTH > mouseX - 20 && x * _BLOCK_WIDTH < mouseX + 1 && y * _BLOCK_HEIGHT > mouseY - 20 && y * _BLOCK_HEIGHT < mouseY + 1)
			{
				return true;
			}
			return false
		}
		
		final private function maintainWorld():void //creates and maintains chunks to blocks of the world
		{
			if (chunk > -1) //positive chunks
			{
				if (posChunks[chunk] == null)
				{
					posChunks[chunk] = new Chunk(chunk);
					for (var x:int = 0; x < _STAGE_WIDTH / _BLOCK_WIDTH; x++)
					{
						posChunks[chunk].blocks[x] = [];
						for (var y:int = 0; y < _STAGE_HEIGHT / _BLOCK_HEIGHT; y++)
						{
							var broken:Boolean = false;
							var breakable:Boolean = true;
							if (y < 20)
							{
								broken = true;
							}
							if (y > 28)
							{
								breakable = false;
							}
							if (broken) {
								posChunks[chunk].blocks[x][y] = new Block(43, broken, breakable);
							}
							else {
								posChunks[chunk].blocks[x][y] = new Block(Math.floor(Math.random() * 43), broken, breakable);
							}
						}
					}
				}
				if (posChunks[chunk] != null)
				{
					for (x = 0; x < _STAGE_WIDTH / _BLOCK_WIDTH; x++)
					{
						for (y = 0; y < _STAGE_HEIGHT / _BLOCK_HEIGHT; y++)
						{
							if (posChunks[chunk].blocks[x][y].broken == false)
							{
								tempCol.color = colref.getColour(posChunks[chunk].blocks[x][y].colId);
								tempBD.colorTransform(tempBD.rect, tempCol);
								canvas.bitmapData.copyPixels(tempBD, tempBD.rect, new Point(x * _BLOCK_WIDTH, y * _BLOCK_HEIGHT));
							}
						}
					}
				}
			}
			if (chunk < 0) //negative chunks
			{
				if (negChunks[Math.abs(chunk)] == null)
				{
					negChunks[Math.abs(chunk)] = new Chunk(chunk);
					for (x = 0; x < _STAGE_WIDTH / _BLOCK_WIDTH; x++)
					{
						negChunks[Math.abs(chunk)].blocks[x] = [];
						for (y = 0; y < _STAGE_HEIGHT / _BLOCK_HEIGHT; y++)
						{
							broken = false;
							breakable = true;
							if (y < 20)
							{
								broken = true;
							}
							if (y > 28)
							{
								breakable = false;
							}
							if (broken) {
								negChunks[Math.abs(chunk)].blocks[x][y] = new Block(43, broken, breakable);
							}
							else {
								negChunks[Math.abs(chunk)].blocks[x][y] = new Block(Math.floor(Math.random() * 43), broken, breakable);
							}
						}
					}
				}
				if (negChunks[Math.abs(chunk)] != null)
				{
					for (x = 0; x < _STAGE_WIDTH / _BLOCK_WIDTH; x++)
					{
						for (y = 0; y < _STAGE_HEIGHT / _BLOCK_HEIGHT; y++)
						{
							if (negChunks[Math.abs(chunk)].blocks[x][y].broken == false)
							{
								tempCol.color = colref.getColour(negChunks[Math.abs(chunk)].blocks[x][y].colId);
								tempBD.colorTransform(tempBD.rect, tempCol);
								canvas.bitmapData.copyPixels(tempBD, tempBD.rect, new Point(x * _BLOCK_WIDTH, y * _BLOCK_HEIGHT));
							}
						}
					}
				}
			}
		}
		
	}

}