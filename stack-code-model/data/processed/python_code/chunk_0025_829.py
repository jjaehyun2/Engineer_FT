package
{
	import com.fw.view.comps.IRenderClickHandler;
	
	import feathers.controls.ImageLoader;
	import feathers.controls.List;
	import feathers.controls.renderers.IListItemRenderer;
	import feathers.data.ListCollection;
	import feathers.layout.VerticalLayout;
	
	import lzm.starling.STLMainClass;
	
	import starling.events.Event;

	public class GameMainClass extends STLMainClass implements IRenderClickHandler
	{
		private var _bgStr:String;
		private var _mapScene:MapScene;
		private var _list:List;
		
		public function GameMainClass()
		{
			super();
			
			this.addEventListener(Event.ENTER_FRAME, onEf);
		}
		
		private function onEf(e:Event):void
		{
			if(stage != null)
			{
				this.removeEventListener(Event.ENTER_FRAME, onEf);
				createMap();
				createCloudList();
			}
		}
		
		private function createCloudList():void
		{
			_list = new List();
			_list.width = 180;
			_list.height = 600;
			const vlayout:VerticalLayout = new VerticalLayout;
			vlayout.useVirtualLayout = true;
			vlayout.gap = 5;
			vlayout.manageVisibility = true;
			_list.layout = vlayout;
			_list.y = 0;
			_list.x = 500;
			_list.itemRendererFactory = tileListItemRendererFactory;
			addChild(_list);
			_list.dataProvider = new ListCollection([{type:1},{type:2},{type:3}]);
		}
		
		private function tileListItemRendererFactory():IListItemRenderer
		{
			const render:CloudRender = new CloudRender(this);
			return render;
		}
		
		public function clickItem(data:Object = null):void
		{
			var type:int = data.type;
			
		}
		
		private function createCloudImage(type:int = 1):void
		{
			var url:String = "assets/cloud" + type + ".png";
			var _cloudImg:ImageLoader = new ImageLoader();
			addChild(_cloudImg);
			_cloudImg.source = url;
			_cloudImg.width = 100;
			_cloudImg.height = 100;
		}
		
		private function createMap():void
		{
			_mapScene = new MapScene();
			addChild(_mapScene);
			_mapScene.drawBg("assets/map.jpg");
		}
				
	}
}