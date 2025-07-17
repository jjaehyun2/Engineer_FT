package
{
	import common.event.EventCenter;
	
	import laya.events.Event;
	import laya.media.SoundManager;
	import laya.net.HttpRequest;
	import laya.utils.Browser;
	
	import net.Message;
	import net.ProtoMessage;

	public class WX
	{
		/**
		 * 微信授权登陆
		 */	
		public static var wx:* = Browser.window.wx;
		public function WX()
		{
			this.Getwx_token();
		}
		
		public static function GetTarget(name):*
		{
			var reg:RegExp = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
			var location:String = Browser.window.location;
			
			var r:* = location.search.substr(1).match(reg);
			if(r!=null)return  unescape(r[2]); return null;
		}
		
		private var hr:HttpRequest;
		public function Getwx_token():void{
			
			
			
			hr = new HttpRequest();
			hr.once(Event.COMPLETE, this, function(e:*=null):void{
				try
				{
					this.signature(hr.data);
					trace(hr.data,"-*---------------------------",this.configSuccess)
				} 
				catch(e:Error) 
				{
					trace(e,this.configSuccess)
					trace("授权报错！！！！！！！！！")
//					alert("分享授权报错！！！！！！！！！");
				}
				
			});
			hr.send("jsapi/jsapi.php",null, "get", "json");
//			hr.send("/wechat/api/jsconfig?url="+encodeURIComponent(Browser.window.location.href.split('#')[0]),null, "get", "json");
		}
		private function signature(data:Object):void
		{
			var string:String = "jsapi_ticket="+data.jsapi_ticket+"&noncestr="+data.nonceStr+"&timestamp="+data.timestamp+"&url="+Browser.window.location.href;
			var signature:String = Browser.window.hex_sha1(string);
			
			this.wxobj={
				"appId":data.appId,
					"timestamp":data.timestamp,
					"nonceStr":data.nonceStr,
					"signature":signature
			};
			this.wx_config();
//			var string:String = "jsapi_ticket="+data.jsapi_ticket+"&noncestr="+data.nonceStr+"&timestamp="+data.timestamp+"&url="+Browser.window.location.href;
//			var signature:String = Browser.window.hex_sha1(string);
			
//			if(data.status==1){
//				this.wxobj={
//					"appId":data.info.appId,
//					"timestamp":data.info.timestamp,
//					"nonceStr":data.info.nonceStr,
//					"signature":data.info.signature
//				};
//				this.wx_config();
//			
//			}else{
//				Browser.window.alert(data.info);
//			}
		}
		private var wxobj:*;
		private function wx_config():void{
			var e:* = {};
			e.debug = false;
			e.appId = this.wxobj.appId;
			e.timestamp = this.wxobj.timestamp;
			e.nonceStr = this.wxobj.nonceStr;
			e.signature = this.wxobj.signature;
			e.jsApiList = [
				"onMenuShareTimeline", 
				"onMenuShareAppMessage", 
				"onMenuShareQQ", "onMenuShareQZone",
				"onMenuShareWeibo", 
				"chooseImage", 
				"uploadImage", 
				"startRecord", 
				"stopRecord", 
				"onVoiceRecordEnd",
				"playVoice", 
				"onVoicePlayEnd",
				"pauseVoice", 
				"stopVoice", 
				"uploadVoice",
				"downloadVoice",
				"chooseWXPay"
			],
			wx.config(e);
			wx.ready(function():void {
				//alert("WX config success");
				
				WX.onMenuShareTimeline();
				WX.onMenuShareAppMessage();
//				wx.hideOptionMenu();
//				onVoicePlayEnd();
//				onVoiceRecordEnd();
			})
		}
		
		/**
		 * 分享到朋友圈
		 */
		public static function onMenuShareTimeline(tit:String=null,parameter:String=null):void
		{
			var str:String
			if(AppConfig.isNewHall){
				str="?tp="+parameter;
			}else{
				str="?room="+parameter;
			}
			wx.onMenuShareTimeline({//朋友圈
				title: tit||AppConfig.nameTitle, // 分享标题
				link: WX.splitStr(Browser.window.location.href,"?")[0]+(parameter==null?"":str), // 分享链接
				imgUrl: AppConfig.locactionHref + "share.png", // 分享图标
				success: function ():void { 
					//用户确认分享后执行的回调函数
				},
				cancel: function ():void { 
					//用户取消分享后执行的回调函数
				}
			});
		}
		
		/**
		 * 分享给朋友
		 */
		public static function onMenuShareAppMessage(tit:String=null,desc:String=null,parameter:String=null,caller:*=null,successFun:Function=null):void
		{
			var str:String
			if(AppConfig.isNewHall){
				str="?tp="+parameter;
			}else{
				str="?room="+parameter;
			}
			wx.onMenuShareAppMessage({//朋友
				title: tit||AppConfig.nameTitle, // 分享标题
				desc: desc||'分享了微信打牌神器-'+AppConfig.nameTitle +'，邀您一起浪！', // 分享描述
				link: WX.splitStr(Browser.window.location.href,"?")[0]+(parameter==null?"":str), // 分享链接
				imgUrl: AppConfig.locactionHref + "share.png", // 分享图标
				type: '', // 分享类型,music、video或link，不填默认为link
				dataUrl: '', // 如果type是music或video，则要提供数据链接，默认为空
				success: function ():void {  
					if(successFun)
					{
						successFun.apply(caller);
					}
					// 用户确认分享后执行的回调函数
				},
				cancel: function ():void { 
					// 用户取消分享后执行的回调函数
				}
			});
		}
		
		
		public static var isStartedRecord:Boolean = false;
		
		/**
		 * 开始录音
		 */
		public static function startRecord():void{
			
			wx.stopRecord({
				success: function (res):void {
					isStartedRecord = false;
				}
			});
			
			if(isStartedRecord)
			{
				return;
			}
			
			SoundManager.stopAllSound();
			SoundManager.stopMusic();
			
			wx.startRecord({
				cancel: function ():void {
					alert('用户拒绝授权录音');
				}
			});
			isStartedRecord = true;
			
			wx.onVoiceRecordEnd({
				complete: function (res):void {
					isStartedRecord = false;
					if(WX.isDownLoading)
					{
						WX.uploadArr.push(res.localId);
					}
					else
					{
						WX.uploadVoice(res.localId);
					}
				}
			});
		}
		
		/**
		 * 停止录音
		 */
		public static var voiceArr:Array=[];
		public static var uploadArr:Array = [];
		private static var localTime:int=0;
		public static function stopRecord(t:int=0,caller:*=null,callback:Function=null):void
		{
				wx.stopRecord({
					success: function (res):void {
						isStartedRecord = false;
						if(t==-2){
//							QuickUtils.VoiceTip(5);
							return;
						}else if(t==-1){
//							QuickUtils.VoiceTip(5);
							return;
						}else{
							
							if(WX.isDownLoading)
							{
								WX.uploadArr.push(res.localId);
							}
							else
							{
								WX.uploadVoice(res.localId);
							}
							
						}
					}
				});
		}
		
		
		/**
		 * 上传语音
		 */
		public static function uploadVoice(localId:String):void
		{
			trace("开始上传语音",localId)
			isUpLoading = true;
			
			wx.uploadVoice({
				localId: localId, // 需要上传的音频的本地ID，由stopRecord接口获得
				isShowProgressTips: 0, // 默认为1，显示进度提示
				success: function (res):void 
				{
					trace("上传成功了",localId);
					var serverId:String = res.serverId; // 返回音频的服务器端ID
					var obj:Object = {message:UserData.uid+"#VoiceId|" + serverId,type:1};
					EventCenter.instance.event(EventCenter.SOCKET_SEND,ProtoMessage.getProtoMessage(net.Message.MSG_Chat,obj));
					
					isUpLoading = false;
					
					if(WX.voiceArr.length>0)//还有要下载的，继续下载
					{
						ModuleDef.CurGameModule.instance.gameContext.view.Voice();
					}
					else//没有下载的，可以录音了
					{
						ModuleDef.CurGameModule.instance.gameContext.view.gui.tableInfoPage.voiceIntercomBtn.disabled=false;
						ModuleDef.CurGameModule.instance.gameContext.view.gui.tableInfoPage.voiceDis.visible=false;
					}
				}
			});
		}
		
		public static var isUpLoading:Boolean = false;
		public static var isDownLoading:Boolean = false;
		
		/**
		 * 播放声音
		 */
		public static function downloadVoice(serverId:String,caller:*,call:Function,args:Array):void
		{
			
			WX.isDownLoading = true;
			
			//****一旦开始下载，就不让录音了
			ModuleDef.CurGameModule.instance.gameContext.view.gui.tableInfoPage.voiceIntercomBtn.disabled=true;
			ModuleDef.CurGameModule.instance.gameContext.view.gui.tableInfoPage.voiceDis.visible=true;
			
			wx.downloadVoice({
				serverId: serverId, // 需要下载的音频的服务器端ID，由uploadVoice接口获得
				isShowProgressTips: 0, // 默认为1，显示进度提示
				success: function (res):void {
					
					trace("语音加载完成");
					
					WX.playVoice(res.localId);
					call.apply(caller,args);
				}
			});
		}
		
		/**
		 * 播放声音
		 */
		private static function playVoice(localId:String):void
		{
			
			AppConfig.isPlayingRecord = true;
			
			SoundManager.stopAllSound();
			SoundManager.stopMusic();
			
			
//			SoundManager.setMusicVolume(0);
//			SoundManager.setSoundVolume(0);
			
			if(QuickUtils.systemType() == "ios" || QuickUtils.systemType() == "ipad")
			{
				wx.pauseVoice({
					localId:localId // 需要播放的音频的本地ID，由stopRecord接口获得
				});
			}
			else
			{
				wx.stopVoice({
					localId:localId // 需要播放的音频的本地ID，由stopRecord接口获得
				});
			}

			wx.playVoice({
				localId:localId // 需要播放的音频的本地ID，由stopRecord接口获得
			});
			
			trace("播放外面还挂不掉！！");
		}
		

		
		/**
		 * 切割字符串
		 * t:String 需要切割的字符串，
		 * e:String 切割符
		 */
		public static function splitStr(t, e):* {
			if(t is String)
			{
				return t.split(e);
			}
			trace("niaole ge dan |||");
			return "";
			
		}
	}
}