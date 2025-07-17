package libs.effects
{
	import flash.events.*;
	import utils.displayObject.LoopIterator;
	
	
	public class Resize extends EventDispatcher
	{
		
		
	    private var tweener:LoopIterator = new LoopIterator();
	    private var obj:Object;
	    
	    
	    
	    public function Resize() {
	    }
	    
	    
		public function init(obj:Object):void {
			this.obj = obj;
	    	obj.asset.scaleContent = true;
	    	obj.asset.maintainAspectRatio = false;
	    	
	    	obj.iterator = tweener;
	    	obj.iterator.stop();
			obj.iterator.init(obj);
			obj.iterator.addEventListener(Event.CHANGE,onChange);
			obj.iterator.addEventListener(Event.COMPLETE,onComplete);
			obj.iterator.play();
		}
		
		
		public function onChange(e:Event):void {
			obj.value = e.currentTarget.value;
			dispatchEvent(new Event(Event.CHANGE));
		}
		
		
		public function onComplete(e:Event):void {
			dispatchEvent(new Event(Event.COMPLETE));
		}
		
		
		public function get value():Number {
			return obj.value;
		}

	}
	
}