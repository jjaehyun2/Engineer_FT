package cn.seisys.TGISViewer.managers
{
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.events.IEventDispatcher;
	import flash.system.MessageChannel;
	import flash.system.Worker;
	import flash.system.WorkerDomain;
	import flash.utils.ByteArray;
	
	import cn.seisys.TGISViewer.AppEvent;
	import cn.seisys.TGISViewer.ConfigData;
	
	public class WorkerManger extends EventDispatcher
	{
		public function WorkerManger(target:IEventDispatcher=null)
		{
			super(target);
			AppEvent.addListener(AppEvent.CONFIG_LOADED, configLoadedHandler);
		}
		
		private function init( event:Event ):void
		{
			
		}
		
		private var _mainToWorker:MessageChannel;
		private var _workerToMain:MessageChannel;
		
		private function configLoadedHandler( event:AppEvent ):void
		{
			var configData:ConfigData = event.data as ConfigData;
			if ( configData.socketInfo )
			{
				var mainWorker:Worker = Worker.current;
				
				//初始化worker
				var socketWorkerBytes:ByteArray = Workers.workers_SocketWorker;
				var socketWorker:Worker = WorkerDomain.current.createWorker( socketWorkerBytes );
				//共享socket配置给worker读取
				socketWorker.setSharedProperty( "socketInfo", configData.socketInfo );
				
				//初始化MessageChanel
				_mainToWorker = mainWorker.createMessageChannel( socketWorker );
				_workerToMain = socketWorker.createMessageChannel( mainWorker );
				//共享MessageChanel
				socketWorker.setSharedProperty( "mainToWorker", _mainToWorker );
				socketWorker.setSharedProperty( "workerToMain", _workerToMain );
				
				//监听work传给主线程的数据
				_workerToMain.addEventListener( Event.CHANNEL_MESSAGE, workerToMain_ChannelMessageHandler );
				
				socketWorker.start();
			}
		}
		
		private function workerToMain_ChannelMessageHandler( event:Event ):void
		{
			var msg:String = _workerToMain.receive();
			try
			{
				var msgObj:Object = JSON.parse( msg );
				var operation:String = msgObj.operation;
				AppEvent.dispatch( operation, msg );
			}
			catch( error:Error )
			{
				AppEvent.showError( "JSON解析错误", "socket管理模块" );
			}
		}
	}
}