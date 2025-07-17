package classes
{
	import com.greensock.TweenLite;
	import com.greensock.plugins.*;
	TweenPlugin.activate([AutoAlphaPlugin]);
	
	import flash.events.Event;
	
	import mx.events.FlexEvent;
	
	import spark.components.Image;
	import spark.components.SkinnableContainer;
	
	public class ImageLoader extends SkinnableContainer
	{
		private var _img0:Image = new Image();
		private var _img1:Image = new Image();
		private var _toLoad:int = 0;
		
		private var _sourceWidth:Number
		private var _sourceHeight:Number
		
		public static const FADE_TRANSITION:String = "fade"; 
		
		//Constructor
		public function ImageLoader()
		{
			super();
			//this.setStyle("backgroundColor","0x330000");
			this.addElement(_img0);
			this.addElement(_img1);
			this.addEventListener(Event.RESIZE, onResize);
			
			_img0.addEventListener(FlexEvent.READY, onImageReady);
			_img1.addEventListener(FlexEvent.READY, onImageReady);
		}
								
		public function nextImage(imageURL:String, direction:String = "next"):void
		{
			if(_toLoad == 0)
			{
				
				_img0.source = imageURL;
				this.swapElements(_img0,_img1);
				_toLoad = 1;
			}
			else if (_toLoad == 1)
			{
				
				_img1.source = imageURL;
				this.swapElements(_img0,_img1);
				_toLoad = 0
			}
		}
		
		private function doTransition(from:Object, to:Object, transition:String = "fade"):void
		{
			switch(transition)
			{
				case "fade":
					
					//TweenLite.to(from,0.1,{autoAlpha:0, onComplete:function():void{from.source=""}});
					from.visible = false;
					from.alpha = 0;
					from.source = "";
					TweenLite.to(to,0.3,{autoAlpha:1});		
					
				break;
			}
		}
		
		/*______________________________________________________________________________________________
		////////////////////////////////////////// EVENTS ////////////////////////////////////////////*/
		
				
		protected function onImageReady(e:FlexEvent):void
		{
			e.stopImmediatePropagation();
			switch(e.target)
			{
				//img0 ready
				case _img0:
					_img0.visible = true;
					_sourceWidth = _img0.sourceWidth
					_sourceHeight = _img0.sourceHeight
					doTransition(_img1,_img0);
					//_img1.visible = false;
					//_img1.source = "";
					
				break;
				
				case _img1:
					_img1.visible = true;
					_sourceWidth = _img1.sourceWidth
					_sourceHeight = _img1.sourceHeight
					doTransition(_img0,_img1);
					//_img0.visible = false;
					//_img0.source = "";
				break
			}
			dispatchEvent(e);
		}
		
		protected function onResize(event:Event):void
		{
			_img0.width = this.width;
			_img0.height = this.height;
			_img1.width = this.width;
			_img1.height = this.height;			
		}

		/*_____________________________________________________________________________
		//////////////////////////// Getters & Setters //////////////////////////////*/
		
		public function get sourceWidth():Number
		{
			return _sourceWidth;
		}

		public function set sourceWidth(value:Number):void
		{
			_sourceWidth = value;
		}

		public function get sourceHeight():Number
		{
			return _sourceHeight;
		}

		public function set sourceHeight(value:Number):void
		{
			_sourceHeight = value;
		}


	}
}