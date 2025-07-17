package hall.view
{
	import common.baseui.UIBase;
	import common.event.EventCenter;
	
	import laya.display.Sprite;
	import laya.events.Event;
	import laya.ui.Box;
	import laya.ui.Button;
	import laya.ui.Label;
	import laya.utils.Handler;
	
	import net.Message;
	import net.ProtoMessage;
	
	import ui.hall.RecordViewUI;

	/**
	 * 对战详情
	 */
	public class RecordView extends UIBase
	{
		public var needViewDetail:Boolean = false;
		public var viewDeatailParam:Object;
		
		protected var _skin:RecordViewUI;
		//public var _onPlayView:OnPlayView;

		public function RecordView(container:Sprite=null)
		{
			super(container);
			skinRes = "";
			//this._onPlayView=new OnPlayView();
			
		}
		override protected function onLoaded():void
		{
			super.onLoaded();
			_skin = new RecordViewUI();
			_skin.mouseEnabled = true;
			if(_isShow)
			{
				container.addChild(_skin);
			}
			init();
			
		
		}
		
		private var data:Array;//list数据数组
		protected function init():void
		{
			_skin.record_list.array = [];
			
			_skin.record_list.mouseHandler = new Handler(this,function(e:Event,index:int):void{
				if(e.type!=Event.CLICK)return;
				if(!e.target is Button)return;
				trace(e.target['tag']);
				var getRecord:Object = {
					"type":e.target['tag']
				};
				var st:String
				switch(e.target['tag'])
				{
					case 3000:
						st="西周麻将";
						break;
					case 3010:
						st="象山麻将";
						break;
					
					default:
						break;
				}	
				RecordView.gameName=st;
				EventCenter.instance.event(EventCenter.SOCKET_SEND,ProtoMessage.getProtoMessage(Message.MSG_Home_Owner,getRecord));
				this.hide();
				//this._onPlayView.show();
			})
				
			EventCenter.instance.on(EventCenter.HALLVIEW_GETRECORD,this,function(data:*):void{
				trace(data.list)
				var aa:Array=[
					{"type":3000,"totalRoundCount":52,"ratio":12},
					{"type":3000,"totalRoundCount":52,"ratio":58},
					{"type":3000,"totalRoundCount":88,"ratio":12},
					{"type":3000,"totalRoundCount":52,"ratio":100},
					{"type":3000,"totalRoundCount":52,"ratio":12},
					{"type":3010,"totalRoundCount":95,"ratio":25},
					{"type":3010,"totalRoundCount":52,"ratio":12},
					{"type":3010,"totalRoundCount":52,"ratio":100},
					{"type":3010,"totalRoundCount":52,"ratio":12},
					{"type":3010,"totalRoundCount":95,"ratio":25},
					{"type":3010,"totalRoundCount":52,"ratio":12},
					{"type":3010,"totalRoundCount":59,"ratio":2}
				]
				var tmpData:*=(data.list as Array).sort(compareFunction)
				updata(tmpData);
//				updata(aa);
			});
		}
		protected function compareFunction(A:Object,B:Object):int
		{
			if(A.type>B.type)
			{
				return -1;
			}else if(A.type==B.type)
			{
				return 0;
			}else{
				return 1;
			}
		}
		public static var gameName:String=AppConfig.nameTitle;
		public function updata(dt:Array):void
		{
			this.data=[];
			var st:String=null;
			for (var i:int = 0,len:int=dt.length; i < len; ++i)
			{
				switch(dt[i].type)
				{
					case 3000:
						st="西周麻将";
						break;
					case 3010:
						st="象山麻将";
						break;
						
					default:
						break;
				}	
				RecordView.gameName=st;
				trace(RecordView.gameName)
				data.push({mjname:st,manumber:dt[i].totalRoundCount,Rate:dt[i].ratio|0,GoTo:dt[i].type});
			}
			_skin.record_list.array = data;	
			// 使用但隐藏滚动条
			_skin.record_list.vScrollBarSkin = "";
			_skin.record_list.repeatY=0;
			_skin.record_list.selectEnable = true;
			_skin.record_list.renderHandler = new Handler(this, onRender);
			_skin.record_list.refresh();
			
			//_onPlayView.needViewDetail = this.needViewDetail;
			
			if(needViewDetail)
			{
				EventCenter.instance.event(EventCenter.SOCKET_SEND,ProtoMessage.getProtoMessage(Message.MSG_Home_Owner,{"type":viewDeatailParam.gametype}));
				this.hide();
				//this._onPlayView.show();
			}
		}
		private function onRender(cell:Box, index:int):void 
		{
			//如果索引不再可索引范围，则终止该函数
			if(index > this.data.length)return;
			//获取当前渲染条目的数据
			var data:Object=cell.dataSource;
			//根据子节点的名字listNumber，获取子节点对象。   
			var mjName:Label=cell.getChildByName("mjName") as Label;
			mjName.text=data.mjname;
			
			var maNumber:Label=cell.getChildByName("maNumber") as Label;
			maNumber.text=data.manumber+"局";
			
			var rate:Label=cell.getChildByName("rate") as Label;
			rate.text=data.Rate+"%";
			
			var goTo:Button=cell as Button;
			goTo.tag=data.GoTo;
		}
		
		
		public override function show():void
		{
			super.show();
			if(_skin)
			{
				container.addChild(_skin);
			}
		}
		
		public override function hide():void
		{
			super.hide();
			if(_skin && _skin.parent)
			{
				_skin.parent.removeChild(_skin);
			}
			//_onPlayView && _onPlayView.hide();
		}
	}
}