package {
	import Box2D.Dynamics.*;
	import Box2D.Collision.*;
	import Box2D.Collision.Shapes.*;
	import Box2D.Common.Math.*;
        import flash.display.Sprite;
        import flash.display.BitmapData;
        import flash.geom.Matrix;

  public class BackgroundAnimation extends Sprite {
    [Embed(source="data/anim1.png")] private var Anim1Graphic:Class;
    public var xLoc:int;
    public var yLoc:int;
    public var scale:int;
    private var pixels:BitmapData;

    function BackgroundAnimation(x:int, y:int, s:int)  {
        pixels = (new Anim1Graphic).bitmapData;
	this.graphics.beginBitmapFill(pixels, null, true);
        this.graphics.drawRect(0,0,157,67);
	xLoc=x;
	yLoc=y;
	scale=s;
      this.x=-xLoc;
      this.y=-yLoc;
    }   
    public function show():void  {
      this.x=xLoc;
      this.y=yLoc;
    } 
    public function hide():void  {
      this.x=-xLoc;
      this.y=-yLoc;
    } 
  }

}