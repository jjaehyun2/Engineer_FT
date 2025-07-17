package controls {
    import flash.desktop.Icon;
    import flash.display.Loader;
    import flash.events.Event;
    import flash.net.URLRequest;
      
    public class AppIcon extends Icon {		
		private var imageURLs:Array = [];
										
        public function AppIcon(icon_images:Array):void {
            super();
			for (var i:String in icon_images) {
				this.imageURLs.push(icon_images[i]);
			}
            bitmaps = new Array();
        }
        
        public function loadImages(event:Event = null):void {
        	if(event != null){
        		bitmaps.push(event.target.content.bitmapData);
        	}
			//trace('AppIcon.loadImages.1 --> imageURLs.length='+imageURLs.length);
        	if(imageURLs.length > 0){
        		var urlString:String = imageURLs.pop();
        		var loader:Loader = new Loader();
        		loader.contentLoaderInfo.addEventListener(Event.COMPLETE,loadImages,false,0,true);
				loader.load(new URLRequest(urlString));
        	} else {
        		var complete:Event = new Event(Event.COMPLETE,false,false);
        		dispatchEvent(complete);
        	}
        }
    }
}