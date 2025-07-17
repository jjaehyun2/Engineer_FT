package modules.sddzGame.sddzInerGame.view.playerInfoPart
{
	
	import laya.display.Sprite;
	import laya.events.Event;
	import laya.utils.Handler;
	
	import manager.UIManager;
	
	import modules.sddzGame.SDdzGameModule;
	
	import ui.gameCommon.UserInfoUI;

	public class UserInfoPage
	{
		protected var uid:int = 0;
		
		private static var _instance:UserInfoPage;
		
		public static function get instance():UserInfoPage
		{
			if(_instance == null)
			{
				_instance = new UserInfoPage(new SingleForcer());
			}
			
			return _instance;
		}
		
		protected var _skin:UserInfoUI;
		
		public function UserInfoPage(forcer:SingleForcer)
		{
			_skin = new UserInfoUI();
			
			_skin.giftList.itemRender = GiftItem;
			//_skin.giftList.vScrollBarSkin = "";
			_skin.giftList.spaceX = 10;
			_skin.giftList.selectEnable = true;
			_skin.giftList.selectHandler = new Handler(this, onSelectRound);
			_skin.giftList.renderHandler = new Handler(this, updateRoundItem);
			_skin.giftList.dataSource = AppConfig.giftConfig;
			_skin.giftList.refresh();
		}
		
		public function show(uid:int,ip:String,icon:String):void
		{
			this.uid = uid;
			_skin.idTf.text="ID: "+uid;
			_skin.nickName.text=SDdzGameModule.instance.gameContext.model.playerByUid(uid).nickname;
			_skin.diamondTf.text = UserData.Diamond+"";
			QuickUtils.AddCenter(_skin,UIManager.instance.popLayer);
			var photo:Sprite=new Sprite();
			photo.loadImage(icon,0,0,_skin.imgPhoto.width,_skin.imgPhoto.height );
			_skin.imgPhoto.addChild(photo); 
			_skin.mouseEnabled=true;
			_skin.clickBg.once(Event.CLICK,this,onCloseUserInfo);
			_skin.giftList.refresh();
			
			if(uid == UserData.uid)
			{
				_skin.diamond.visible = true;
				_skin.diamondTf.visible = true;
			}
			else
			{
				_skin.diamond.visible = false;
				_skin.diamondTf.visible = false;
			}
			
			
		}
		
		
		protected function onCloseUserInfo(e:Event):void
		{
			if(_skin && e.target == _skin.clickBg)
			{
				_skin && _skin.removeSelf();
			}
		}
		
		public function hide():void
		{
			_skin && _skin.removeSelf();
		}
		
		private function onSelectRound(index:int):void
		{
			trace("当前选择的索引：" + index);
		}
		
		private function updateRoundItem(cell:GiftItem, index:int):void 
		{
			cell.setData(cell.dataSource,this.uid);
		}
	}
}

class SingleForcer{}