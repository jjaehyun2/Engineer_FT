package  {
	
	import flash.display.MovieClip;
	import flash.events.Event;
	
	
	public class DocClass extends MovieClip {
		
		public var sc0var= new sc0();
		public function DocClass() {
			// constructor code
			
			stage.addChild(sc0var);
			sc0var.addEventListener(StartGameEvent.onbtpressed,startthegame);
			
		}

		public function startthegame(e:StartGameEvent):void{
			trace("my event dispatched")
			stage.removeChild(sc0var);
			var sc1var= new cargame(stage);
			stage.addChild(sc1var);
		}
	}
	
}