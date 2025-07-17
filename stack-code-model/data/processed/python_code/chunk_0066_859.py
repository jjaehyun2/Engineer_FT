package
{
	import com.coffeebean.view.fight.utils.FightUtil;
	import com.fw.view.comps.IRenderClickHandler;
	import com.fw.view.comps.WmListRender;
	import com.gameabc.sanguo.config.template.BuilderTemplate;
	import com.gameabc.sanguo.config.template.ShipTemplate;
	
	import feathers.controls.ImageLoader;
	
	import starling.events.Event;
	
	public class CloudRender extends WmListRender
	{
		private var _cloudImg:ImageLoader;
		
		public function CloudRender(handler:IRenderClickHandler=null)
		{
			super(handler);
		}
		
		private function setCloudImage(type:int = 1):void
		{
			var url:String = "assets/cloud" + type + ".png";
			_cloudImg = new ImageLoader();
			addChild(_cloudImg);
//			_cloudImg.addEventListener(Event.COMPLETE, onShipOk);
			_cloudImg.source = url;
			_cloudImg.width = 100;
			_cloudImg.height = 100;
			
//			function onShipOk(e:Event):void
//			{
//				_cloudImg.removeEventListener(Event.COMPLETE, onShipOk);
//				var scale:Number =Math.min(120/_cloudImg.width,100/_cloudImg.height)
//				_cloudImg.scaleX = scale;
//				_cloudImg.scaleY = scale;
//			}
		}
		
		override protected function commitData():void
		{
//			super.commitData();
			if(data)
			{
				setCloudImage(data.type);
			}
		}
	}
}