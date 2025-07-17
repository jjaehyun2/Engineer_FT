package
{
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.geom.Point;
	import flash.system.Capabilities;
	
	import dorkbots.dorkbots_broadcasters.IBroadcastedEvent;
	import dorkbots.dorkbots_iso.IIsoMaker;
	import dorkbots.dorkbots_iso.IsoMaker;
	import dorkbots.dorkbots_iso.entity.Entity;
	import dorkbots.dorkbots_iso.entity.IEnemy;
	import dorkbots.dorkbots_iso.room.IIsoRoomsManager;
	import dorkbots.dorkbots_iso.room.IsoRoomsManager;
	
	import entities.EntityDorkbotsFactory;
	
	import rooms.Room1Data;
	import rooms.Room2Data;
	import rooms.Room3Data;
	import rooms.Room4Data;
	
	[SWF(width='800', height='600', backgroundColor='#FFFFFF', frameRate='30')]
	public class Main extends Sprite
	{	
		private var isoMaker:IIsoMaker;
		private var roomsManager:IIsoRoomsManager;
		
		public function Main()
		{
			// use this for mobile
			this.stage.align = StageAlign.TOP_LEFT;
			this.stage.scaleMode = StageScaleMode.NO_SCALE;
			this.stage.stageHeight = Capabilities.screenResolutionY;
			this.stage.stageWidth = Capabilities.screenResolutionX;
			
			roomsManager = new IsoRoomsManager();
			roomsManager.addRoom( Room1Data );
			roomsManager.addRoom( Room2Data );
			roomsManager.addRoom( Room3Data );
			roomsManager.addRoom( Room4Data );
			
			var isoContainer:Sprite = new Sprite();
			addChild(isoContainer);
			
			isoMaker = new IsoMaker( isoContainer, roomsManager, new EntityDorkbotsFactory());
			isoMaker.viewHeight = this.stage.stageHeight;
			isoMaker.viewWidth = this.stage.stageWidth;
			isoMaker.borderOffsetX = 320;
			isoMaker.borderOffsetY = 20;
			isoMaker.addEventListener( IsoMaker.ROOM_CHANGE, roomChange );
			isoMaker.addEventListener( IsoMaker.PICKUP_COLLECTED, pickupCollected );
			isoMaker.addEventListener( IsoMaker.HERO_SHARING_NODE_WITH_ENEMY, heroSharingNodeWithEnemy );
			isoMaker.start();
			
			isoMaker.hero.addEventListener( Entity.WALKING_ON_NODE_TYPE_OTHER, heroWalkingOnNodeTypeOther );
			
			setUpEnemies();
			
			addEventListener(Event.ENTER_FRAME, loop);
		}
		
		private function loop(event:Event):void
		{
			isoMaker.loop();
		}
		
		private function roomChange(event:IBroadcastedEvent):void
		{
			trace("{Main} roomChange -> roomNumber = " + event.object().roomNumber);
			setUpEnemies();
		}
		
		private function setUpEnemies():void
		{
			for (var i:int = 0; i < roomsManager.roomCurrent.enemies.length; i++) 
			{
				roomsManager.roomCurrent.enemies[i].addEventListener( Entity.PATH_COMPLETE, enemyPathComplete );
			}
		}
		
		private function enemyPathComplete(event:IBroadcastedEvent):void
		{
			var enemy:IEnemy =  IEnemy(event.owner());
			trace("{Main} enemyPathComplete -> enemy = " + enemy );
			if (roomsManager.roomCurrent.roomWalkable[enemy.node.y][enemy.node.x] == 4 && roomsManager.roomCurrent.roomWalkable[isoMaker.hero.node.y][isoMaker.hero.node.x] == 3)
			{
				trace("all your base are belong to us!!!!!");
				isoMaker.enemyDestroy(enemy);
			}
		}
		
		private function pickupCollected(event:IBroadcastedEvent):void
		{
			trace("{Main} pickupCollected -> type = " + event.object().type);
		}
		
		private function heroSharingNodeWithEnemy(event:IBroadcastedEvent):void
		{
			trace("{Main} heroSharingNodeWithEnemy -> enemy = " + event.object().enemy);
		}
		
		// you can use this for adding damage or adding health (in the future, no health or damage yet). Also can create a safe zone from enemies, or a destroy zone for enemies.
		// use the setupWalkableList() method in the entity class, polymorph it. Look at the Hero class.
		private function heroWalkingOnNodeTypeOther(event:IBroadcastedEvent):void
		{
			var nodeType:uint = event.object().nodeType;
			//trace("{Main} heroWalkingOnNodeTypeOther -> type = " + nodeType);
			if (nodeType == 3)
			{
				var i:int;
				var enemyBase:Point;
				
				// label for the first loop, used for break
				toploop: 
				for (i = 0; i < roomsManager.roomCurrent.roomNodeGridHeight; i++) 
				{
					for (var j:int = 0; j < roomsManager.roomCurrent.roomNodeGridWidth; j++) 
					{
						if (roomsManager.roomCurrent.roomWalkable[i][j] == 4)
						{
							enemyBase = new Point(j, i);
							break toploop;
						}
					}
					
				}
				
				if (enemyBase) 
				{
					isoMaker.hero.addEventListener( Entity.NEW_NODE, heroNewNode );
					isoMaker.enemiesSeekHero = false;
					isoMaker.enemyTargetNode = enemyBase;
				}
			}
		}
		
		private function heroNewNode(event:IBroadcastedEvent):void
		{
			var node:Point = event.object().node;
			//trace("{Main} heroNewNode -> node = " + event.object.node);
			var nodeWalkableType:uint = roomsManager.roomCurrent.roomWalkable[node.y][node.x];
			//trace("{Main} heroNewNode -> nodeWalkableType = " + nodeWalkableType);
			if (nodeWalkableType == 0)
			{
				//trace("{Main} heroNewNode -> reset enemies to seek hero");
				isoMaker.hero.removeEventListener( Entity.NEW_NODE, heroNewNode );
				isoMaker.enemiesSeekHero = true;
			}
		}
	}
}