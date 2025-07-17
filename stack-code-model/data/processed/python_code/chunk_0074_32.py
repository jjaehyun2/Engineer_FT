package hall.view.creatRoom
{
	import common.baseui.UIBase;
	
	import laya.display.Sprite;
	import laya.events.Event;
	import laya.ui.Button;
	
	import ui.hall.creatRoom.CCoinViewUI;
	
	public class CCoinView extends UIBase
	{
		
		protected var _skin:CCoinViewUI;
		
		protected var _typeBtns:Vector.<Button> = new Vector.<Button>();
		
		protected var _gameLv:int = 0;//0初级 1中级 2高级
		
		public function get gameLv():int{return QuickUtils.getLocalVar("mygame_gameLv",_gameLv);}
		public function set gameLv(value:int):void{QuickUtils.setLocalVar("mygame_gameLv",value);}
		
		
		public function CCoinView(container:Sprite=null)
		{
			super(container);
			skinRes = "";
		}
		
		protected var _roomtype:int;
		
		public function showWithParam(roomType:int):void
		{
			_roomtype = roomType;
			show();
			
		}
		
		public override function show():void
		{
			super.show();
			if(_skin)
			{
				container.addChild(_skin);
			}
			
			if (_isLoaded){
				updateUI();
			}
			
		}
		
		public override function hide():void
		{
			super.hide();
			if(_skin && _skin.parent)
			{
				_skin.parent.removeChild(_skin); 
			}
		}
		
		override protected function onLoaded():void
		{
			super.onLoaded();
			_skin = new CCoinViewUI();
			if(_isShow)
			{
				container.addChild(_skin);
			}
			
			init();
			updateUI();
		}
		
		protected function init():void{
			_typeBtns.push(_skin.chujiBtn,_skin.zhongjiBtn,_skin.gaojiBtn);
			_skin.backBtn.on(Event.CLICK,this,onClickBackBtn);
			
			_skin.chujiBtn.on(Event.CLICK,this,onClickLv,[0]);
			_skin.zhongjiBtn.on(Event.CLICK,this,onClickLv,[1]);
			_skin.gaojiBtn.on(Event.CLICK,this,onClickLv,[2]);
		}
		
		
		//刷新界面
		protected function updateUI():void{
			onClickLv(gameLv);
			_skin.ganmeTf.text = UserData.roomtype_reference[""+_roomtype];
			
			
			
			
		}
		
		
		
		//
		
		protected function onClickLv(idx:int,e:Event=null):void{
			
			var i:int;
			for(i=0;i<_typeBtns.length;i++){
				if (i==idx){
					_typeBtns[i].selected = true;
				}else{
					_typeBtns[i].selected = false;
				}
			}
			
			gameLv = idx;
			
		}
		
		
		
		
		protected function onClickBackBtn(e:Event):void
		{
			hide();
		}
		
	}
}