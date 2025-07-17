package {

  import flash.display.BitmapData;
  import flash.events.Event;

  public class FluxlyG {
    static private var _cache:Object;

    static public function init():void {
        _cache = new Object();
    }

    static public function createBitmap(Width:uint, Height:uint, Color:uint):BitmapData	{
	var key:String = Width+"x"+Height+":"+Color;
	if((_cache[key] == undefined) || (_cache[key] == null))
	 	_cache[key] = new BitmapData(Width,Height,true,Color);
	return _cache[key];
    }

    static public function addBitmap(Graphic:Class):BitmapData 	{
	var needReverse:Boolean = false;
	var key:String = String(Graphic);
	if((_cache[key] == undefined) || (_cache[key] == null)) {
   	    _cache[key] = (new Graphic).bitmapData;
	}
	var pixels:BitmapData = _cache[key];
        return pixels;   
    }
  }
}