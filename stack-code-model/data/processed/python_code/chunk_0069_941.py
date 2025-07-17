package  
{
	import Assets;
	import Derps.DerpsClimber;
	import Derps.DerpsGelly;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Loader;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	import XML;
	import flash.events.ProgressEvent;
	import flash.events.Event;
	import Pointer;	
	import Derps.DerpsBasic;
	import Derps.DerpsFallers;
	import Derps.DerpsRunner;
	import Derps.DerpsCrybaby;
	import Derps.DerpsExploder;
	import Layers.LayerBG;
	import Layers.LayerHazards;
	import Layers.LayerLocations;
	import Layers.LayerTerrain;
	import net.flashpunk.World;
	import net.flashpunk.FP;
	import net.flashpunk.utils.Input;
	import net.flashpunk.utils.Key;
	
	/**
	 * ...
	 * @author Joseph O'Connor
	 */
	public class Level extends World 
	{
		private var     pointer:Pointer;
		private var   locations:LayerLocations;
		private var       width:int = 0;
		private var      height:int = 0;
		private var facingRight:Boolean = false;
		private var    leveldir:String ;
		
		private var    levelXML:XML;
		
		public var    xmlloader:URLLoader = new URLLoader();
		public var       loader:Loader = new Loader();
		
		public function Level(LEVEL:String) 
		{
			leveldir = LEVEL;
			
			// Pointer
			pointer = new Pointer();
			this.add(pointer);
			
			xmlloader.addEventListener(Event.COMPLETE, setLevel)
			xmlloader.load(new URLRequest("Levels/" +leveldir+ "/Level.xml"));
			
			// Start Loading the Level
			var request:URLRequest = new URLRequest("Levels/" + leveldir + "/Background.png");
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE, setBG);
			loader.load(request);			
		}
		
		public function setLevel(e:Event):void
		{
			levelXML = new XML(e.target.data);
			
			width = levelXML.width.*;
			height = levelXML.height.*;
			
			
			var TorF:String = levelXML.facingRight.*;
			
			if (TorF == "false")
			{
				facingRight = false; 
			}
			else if (TorF == "true")
			{
				facingRight = true;
			}
			
		}
		
		public function setBG(e:Event):void
		{
			var bmp:Bitmap = Bitmap(loader.content);
			var bmpd:BitmapData = bmp.bitmapData;
			this.add(new LayerBG(bmpd));			
			loader.contentLoaderInfo.removeEventListener(Event.COMPLETE, setBG);
			
			var request:URLRequest = new URLRequest("Levels/" + leveldir + "/Hazards.png");
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE, setHazards);
			loader.load(request);
		}
		
		public function setHazards(e:Event):void
		{
			var bmp:Bitmap = Bitmap(loader.content);
			var bmpd:BitmapData = bmp.bitmapData;
			this.add(new LayerHazards(bmpd));
			loader.contentLoaderInfo.removeEventListener(Event.COMPLETE, setHazards);
			
			var request:URLRequest = new URLRequest("Levels/" + leveldir + "/Locations.png");
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE, setLocations);
			loader.load(request);
		}
		
		public function setLocations(e:Event):void
		{
			var bmp:Bitmap = Bitmap(loader.content);
			var bmpd:BitmapData = bmp.bitmapData;
			locations = new LayerLocations(bmpd)
			this.add(locations);
			loader.contentLoaderInfo.removeEventListener(Event.COMPLETE, setLocations);
			
			//locations.startPoint.y -= 256;
			
			var request:URLRequest = new URLRequest("Levels/" + leveldir + "/UnbreakableTerrain.png");
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE, setUnbreakableTerrain);
			loader.load(request);
		}
		
		public function setUnbreakableTerrain(e:Event):void
		{
			var bmp:Bitmap = Bitmap(loader.content);
			var bmpd:BitmapData = bmp.bitmapData;
			this.add(new LayerTerrain(bmpd));
			loader.contentLoaderInfo.removeEventListener(Event.COMPLETE, setUnbreakableTerrain);
			
			var request:URLRequest = new URLRequest("Levels/" + leveldir + "/BreakableTerrain.png");
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE, setBreakableTerrain);
			loader.load(request);
		}
		
		public function setBreakableTerrain(e:Event):void
		{
			var bmp:Bitmap = Bitmap(loader.content);
			var bmpd:BitmapData = bmp.bitmapData;
			this.add(new LayerTerrain(bmpd, true));
			loader.contentLoaderInfo.removeEventListener(Event.COMPLETE, setBreakableTerrain);
		}
		
		override public function update():void 
		{
			
			if (Input.released(Key.DIGIT_1))
			{
				this.add(new DerpsFallers(locations.startPoint.x,locations.startPoint.y, facingRight));
			}
			
			if (Input.released(Key.DIGIT_2))
			{
				this.add(new DerpsRunner(locations.startPoint.x,locations.startPoint.y, facingRight));
			}
			
			if (Input.released(Key.DIGIT_3))
			{
				this.add(new DerpsGelly(locations.startPoint.x,locations.startPoint.y, facingRight));
			}
			
			if (Input.released(Key.DIGIT_4))
			{
				this.add(new DerpsClimber(locations.startPoint.x,locations.startPoint.y, facingRight));
			}
			
			if (Input.released(Key.DIGIT_5))
			{
				this.add(new DerpsCrybaby(locations.startPoint.x,locations.startPoint.y, facingRight));
			}
			
			if (Input.released(Key.DIGIT_6))
			{
				this.add(new DerpsExploder(locations.startPoint.x,locations.startPoint.y, facingRight));
			}
			
			// Camera Controls
			cameraLogic();
			cameraBounds();
			
			super.update();
		}
		
		private function cameraLogic():void
		{
			if (pointer.pointerState == Pointer.drag)
			{
				FP.camera.x += pointer.dragPoint.x/-25;
				FP.camera.y += pointer.dragPoint.y/-25;
			}
			else if (pointer.dragPoint.x != 0 || pointer.dragPoint.y != 0 )
			{
				if (pointer.dragPoint.x > 0)
				{
					pointer.dragPoint.x -= pointer.dragPoint.x/20;
				}
				else if (pointer.dragPoint.x < 0)
				{
					pointer.dragPoint.x += pointer.dragPoint.x/-20;
				}
				
				if (pointer.dragPoint.y > 0)
				{
					pointer.dragPoint.y -= pointer.dragPoint.y/20;
				}
				else if (pointer.dragPoint.y < 0)
				{
					pointer.dragPoint.y += pointer.dragPoint.y/-20;
				}
				
				FP.camera.x += pointer.dragPoint.x/-25;
				FP.camera.y += pointer.dragPoint.y/-25;
			}
		}
		
		private function cameraBounds():void
		{
			// Camera Limits
			if (FP.camera.x < 0)
			{
				FP.camera.x = 0;
			}
			else if (FP.camera.x + FP.screen.width > width)
			{
				FP.camera.x = width - FP.screen.width;
			}
			
			if (FP.camera.y < 0)
			{
				FP.camera.y = 0;
			}
			else if (FP.camera.y + FP.screen.height > height)
			{
				FP.camera.y = height - FP.screen.height;
			}
		}
		
	}

}