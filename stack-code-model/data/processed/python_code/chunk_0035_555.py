package
{
	import flash.display.MovieClip;
	import flash.display.Shape;
	import flash.display.BitmapData;
	import flash.display.Bitmap;
	import flash.events.Event;
	public class PlacementArea extends MovieClip
	{
		
		var BitMapData:BitmapData;
		var BitMap:Bitmap;
		var w:int;
		var h:int;
		var a:Boolean;
		public function PlacementArea()
		{
			alpha = 0.2;
			a = true;
			addEventListener("enterFrame",enterFrame);
			mouseEnabled = false;
			mouseChildren = false;
			BitMapData=new BitmapData(500,600,true,0x00000000);
			BitMap=new Bitmap(BitMapData);
			
			
			
				drawRectangle();
		}
		function drawRectangle()
		{
			var rectangle:Shape = new Shape; // initializing the variable named rectangle
			 // choosing the colour for the fill, here it is red
			var cannon=Game.cannons
			
			for(var i in cannon)
			{
				w = 25;
				h = 25;
				if(cannon[i].type == "SpreadCannon")
				{
					w = 30
					h = 30
				}
				if(cannon[i].type == "SniperCannon")
				{
					w = 25
					h = 20
				}
				if(cannon[i].type == "RocketLauncher")
				{
					w = 30
					h = 30
				}
				if(cannon[i].type == "Shield")
				{
					w = 30
					h = 30
				}
				w+=10;
				h+=10;
				if(cannon[i] != FakeCannon.DragCannon)
				{
					rectangle.graphics.beginFill(0xFF0000);
					rectangle.graphics.drawRect(cannon[i].x-w/2,cannon[i].y-h/2,w,h); // (x spacing, y spacing, width, height)
					rectangle.graphics.endFill();
				}
			}
			 // not always needed but I like to put it in to end the fill
			BitMapData.draw(rectangle);
			addChild(BitMap);
		}
		function enterFrame(e:Event)
		{
			if(a == true)
			{
				alpha += 0.01;
				if(alpha > 0.4) a = false;
			}else{
				alpha -= 0.01;
				if(alpha < 0.2) a = true;
			}
		}
		public function remove()
		{
			removeEventListener("enterFrame",enterFrame)
			parent.removeChild(this);
		}
	}
}