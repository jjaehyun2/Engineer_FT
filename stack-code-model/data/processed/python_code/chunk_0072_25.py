package entity.gadget 
{
	import data.CLASS_ID;
	import entity.player.Player;
    import flash.geom.Point;
	import org.flixel.FlxGroup;
    import org.flixel.FlxPoint;
	import org.flixel.FlxSprite;
	import org.flixel.FlxObject;
	import org.flixel.FlxG;
	import global.Registry;
	import states.PlayState;
	/**
	 *	Single push blocks...push em from one direction, they move a tile. yeah WHAT
	 * @author seagaia
	 */
	//Aury: rework most of this in this in a hacky way cuz what
	public class SinglePushBlock extends FlxSprite
	{
		private var dir:int;
		private var pushdir:int;
		private var arrayIndex:int = 0;
		private var hasBeenPushed:Boolean = false;
		private var sound_played:Boolean = false;
		private var distanceToGo:int = Registry.TILE_HEIGHT;
		private var startedMoving:Boolean = false;
        public var type:String = "SinglePushBlock";
		public var xml:XML;
		public var detector:FlxGroup = new FlxGroup(4);
		public var sentup:FlxSprite = new FlxSprite(x, y);
		public var sentdw:FlxSprite = new FlxSprite(x, y);
		public var sentlf:FlxSprite = new FlxSprite(x, y);
		public var sentrt:FlxSprite = new FlxSprite(x, y);
        public var timeToPush:Number = 0.3;
        public var initial_coords:Point = new Point();
        public var final_coords:Point = new Point();
        public var MOVE_VEL:int = 24;
		public var INCREMENTED_REG:Boolean = false;
		public var BEDROOM_INDEX:int = 4;
		public var STREET_INDEX:int = 5;
		public var cid:int = CLASS_ID.SINGLEPUSHBLOCK;
		
		private var is_non_puzzle:Boolean = false;
		[Embed (source = "../../res/sprites/gadgets/pushyblocks.png")] public var C_PUSH_BLOCKS:Class;
		
		public var player:Player;
		public var parent:PlayState;
//frame mod 4 determines direction

		public function SinglePushBlock(_x:int, _y:int, _xml:XML, _p:Player,_parent:PlayState) 
		{
			super(_x, _y);
            initial_coords.x = x;
            initial_coords.y = y;
			xml = _xml;
			parent = _parent;
			player = _p;
			
					sentdw.makeGraphic(16, 2, 0xFFFFFF80);
                    sentrt.x = x;
                    sentrt.y = y - 2;
					sentdw.exists = true;
					detector.add(sentdw)
					
					sentup.makeGraphic(16, 2, 0xFF33FFFF);
                    sentup.x = x;
                    sentup.y = y + Registry.TILE_WIDTH;
					sentup.exists = true;
					detector.add(sentup)
					
					sentlf.makeGraphic(2, 16, 0xFF3333FF);
                    sentlf.x = x + Registry.TILE_WIDTH;
                    sentlf.y = y;
					sentlf.exists = true;
					detector.add(sentlf)
					
					sentrt.makeGraphic(2, 16, 0xFF33FF33);
                    sentrt.x = x - 2;
                    sentrt.y = y;
					sentrt.exists = true;
					detector.add(sentrt)
					
            switch (parseInt(xml.@frame) % 6) {
                case 0: pushdir = FlxObject.UP; break;
                case 1: pushdir = FlxObject.DOWN; break;
                case 2: pushdir = FlxObject.LEFT; break;
                case 3: pushdir = FlxObject.RIGHT; break;
                case 4: pushdir = FlxObject.ANY; break;
                case 5: pushdir = FlxObject.NONE; break;
            }
			
			loadGraphic(C_PUSH_BLOCKS,true, false, 16, 16);
			if (Registry.CURRENT_MAP_NAME == "BEDROOM") {
				trace("SET PUSH BLOCK FRAME: ", BEDROOM_INDEX);
				frame = BEDROOM_INDEX;
			} else if (Registry.CURRENT_MAP_NAME == "STREET") {
				frame = STREET_INDEX;
			} else {
				frame = STREET_INDEX;
			}
			
			if (parseInt(xml.@type) == 1) {
				is_non_puzzle = true;
			}
			immovable = true;
			arrayIndex = Registry.subgroup_blocks.length;
			trace(arrayIndex);
			Registry.subgroup_blocks.push(this);
			
		}
		
		override public function update():void {
        
			FlxG.collide(this, parent.curMapBuf)
			
			if (player.overlaps(sentup)) {
				dir = FlxObject.UP;
			} else if (player.overlaps(sentdw)){
				dir = FlxObject.DOWN;
			} else if (player.overlaps(sentlf)){
				dir = FlxObject.LEFT;
			} else if (player.overlaps(sentrt)){
				dir = FlxObject.RIGHT;
			} else dir = FlxObject.NONE;
			
			updateSentinel();
			
				if (FlxG.collide( player, this)) {
				if (pushdir != FlxObject.NONE && (pushdir == dir || pushdir == FlxObject.ANY)){
					//actually lets just pop off the collision if it's within the last two pixels
					if ((Math.abs(x - initial_coords.x) >= 14 || Math.abs(y - initial_coords.y) >= 14)) {
					}else{
					switch (dir) {
						case FlxObject.UP:
							if (checkOtherBlocks(sentdw) || FlxG.collide(sentdw, parent.curMapBuf) || FlxG.collide(sentdw, parent.map_bg_2)){
								//reset if fires right after starting to be pushed
								if(Math.abs(y - initial_coords.y) < 2){
									y = initial_coords.y;
									hasBeenPushed = false;
								}
								startedMoving = false;
								velocity.x = 0;
								velocity.y = 0;
							}else {
								startMoving();
							}
							break;
						case FlxObject.DOWN:
							if(checkOtherBlocks(sentup) || FlxG.collide(sentup,parent.curMapBuf) || FlxG.collide(sentup, parent.map_bg_2)){
								if(Math.abs(y - initial_coords.y) < 2){
									y = initial_coords.y;
									hasBeenPushed = false;
								}
								startedMoving = false;
								velocity.x = 0;
								velocity.y = 0;
							}else {
								startMoving();
							}
							break;
						case FlxObject.RIGHT:
							if(checkOtherBlocks(sentlf) || FlxG.collide(sentlf,parent.curMapBuf) || FlxG.collide(sentlf, parent.map_bg_2)){
								if(Math.abs(x - initial_coords.x) < 2){
									x = initial_coords.x;
									hasBeenPushed = false;
								}
								startedMoving = false;
								velocity.x = 0;
								velocity.y = 0;
							}else {
								startMoving();
							}
							break;
						case FlxObject.LEFT:
							if(checkOtherBlocks(sentrt) || FlxG.collide(sentrt,parent.curMapBuf) || FlxG.collide(sentrt, parent.map_bg_2)){
								if(Math.abs(x - initial_coords.x) < 2){
									x = initial_coords.x;
									hasBeenPushed = false;
								}
								startedMoving = false;
								velocity.x = 0;
								velocity.y = 0;
							}else {
								startMoving();
							}
							break;
						}
					}
					
					}
				}

			if (timeToPush < 0) {
				if (!sound_played) {
					hasBeenPushed = true;
					Registry.sound_data.push_block.play();
					sound_played = true;
				}
			switch (dir) {
				case FlxObject.UP:
					velocity.y = -MOVE_VEL;
					break;
				case FlxObject.DOWN:
                    velocity.y = MOVE_VEL;
					break;
				case FlxObject.RIGHT:
					velocity.x = MOVE_VEL;
					break;
				case FlxObject.LEFT:
					velocity.x = -MOVE_VEL;
					break;
                }
			}
            
            if (Math.abs(x - initial_coords.x) >= 15.5 || Math.abs(y - initial_coords.y) >= 15.5) {
				if (!INCREMENTED_REG) {
					if (!is_non_puzzle) {
						Registry.GRID_PUZZLES_DONE++;
					}
					INCREMENTED_REG = true;
				}
				if ((x - initial_coords.x) > 15.5) {
					x = initial_coords.x + 16;
				} else if ((x - initial_coords.x) < -15.5) {
					x = initial_coords.x - 16;
				}
				
				if ((y - initial_coords.y > 15.5)) {
					y = initial_coords.y + 16;
				} else if ((y - initial_coords.y) < -15.5) {
					y = initial_coords.y - 16;
				}
                velocity.x = velocity.y = 0;
            }
			
            
            if (!startedMoving) timeToPush = 0.3;
            startedMoving = false;
			super.update();
		}
		
		public function startMoving():void {
			if (hasBeenPushed) return;
            timeToPush -= FlxG.elapsed;
			startedMoving = true;
		}
		
		private function checkOtherBlocks(entity:FlxSprite):Boolean{
			/*for each (var block:SinglePushBlock in Registry.subgroup_blocks){
				if (entity == null || block == null) continue;
				if (block.overlaps(entity)){
					trace(Registry.subgroup_blocks.indexOf(block));
					trace(Registry.subgroup_blocks.indexOf(this));
					trace(arrayIndex);
					if(Registry.subgroup_blocks.indexOf(block) == arrayIndex){
						return false;
					}
					return true;
				}
				
			}*/
			//probablly what we want
			for (var i:String in Registry.subgroup_blocks){
				var block:SinglePushBlock = Registry.subgroup_blocks[i];
				if (entity == null || block == null) continue;
				if(Registry.subgroup_blocks.indexOf(this)+"" == i){
					 continue;
				}
				if (block.overlaps(entity)){
					return true;
				}
				
			}
			return false;
		}
		
		public function updateSentinel():void {			

					sentdw.x = x; 
					sentdw.y = y - 2;
					
                    sentup.x = x;
                    sentup.y = y + Registry.TILE_WIDTH;
					
                    sentlf.x = x + Registry.TILE_WIDTH;
                    sentlf.y = y;
					
                    sentrt.x = x - 2;
                    sentrt.y = y;
			
		}
	}

}