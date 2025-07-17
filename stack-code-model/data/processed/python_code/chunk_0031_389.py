package {
	import Box2D.Dynamics.*;
	import Box2D.Collision.*;
	import Box2D.Collision.Shapes.*;
	import Box2D.Common.Math.*;
        import flash.display.Sprite;
        import flash.display.BitmapData;

  public class Orb {
    [Embed(source="data/orb.png")] private var orbGraphic:Class;
    public var body:b2Body;
    public var body_def:b2BodyDef;
    public var the_box:b2PolygonDef;
    public var graphic:Sprite;
    public var onscreen:Boolean;
    public var w:Number;
    public var h:Number;
 
    function Orb(x:Number, y:Number,w1:Number, h1:Number,f:Number,d:Number){
        graphic = new Sprite();
        body_def = new b2BodyDef();
	body_def.linearDamping = 16;
	body_def.angularDamping = 16;
	body_def.position.Set(x,y);
	the_box = new b2PolygonDef();
	w =w1;
	h = h1;
	the_box.SetAsBox(w, h);

	the_box.friction=f;
	the_box.density=d;

        var pixels:BitmapData;
        pixels = (new orbGraphic).bitmapData;
	graphic.graphics.beginBitmapFill(pixels, null, true);
        graphic.graphics.drawRect(0,0,14,14);
	graphic.x=-15;
	graphic.y=-15;

	
    }
    
  }

}