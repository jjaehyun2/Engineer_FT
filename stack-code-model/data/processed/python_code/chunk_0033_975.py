package workers
{
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.events.ProgressEvent;
	import flash.events.SecurityErrorEvent;
	import flash.events.TimerEvent;
	import flash.net.Socket;
	import flash.system.MessageChannel;
	import flash.system.Security;
	import flash.system.Worker;
	import flash.utils.ByteArray;
	import flash.utils.Timer;
	
	import mx.collections.ArrayCollection;
	import mx.controls.Alert;
	import mx.utils.UIDUtil;
	
	public class SocketWorker extends Sprite
	{
		private var _mainToWorker:MessageChannel;
		private var _workerToMain:MessageChannel;
		
		private var _clientSocket:Socket;
		/**
		 * socket配置信息
		 * */
		private var _socketInfo:Object;
		
		/**
		 * 重连定时器
		 * */
		private var _reconnectTimer:Timer;
		
		/**
		 * 心跳定时器
		 * */
		public var _heartBeatTimer:Timer;
		/**
		 * 检查心跳计数定时器
		 * */
		public var _heartBeatCheckTimer:Timer;
		/**
		 * 已发送的心跳guid，收到服务端回复时删除回复的guid
		 * */
		public var _heartBeatGuidAC:ArrayCollection;
		/**
		 * 最大心跳失败计数，超过此数要中断连接重连
		 * */
		private const MAX_HEART_BEAT_FAIL_COUNT:uint = 3;
		
		private const OPERATION_HEART_BEAT:String = "activetest";
		
		public function SocketWorker()
		{
			super();
			_heartBeatGuidAC = new ArrayCollection();
			
			var worker:Worker = Worker.current;
			//获取socket配置信息
			_socketInfo = worker.getSharedProperty( "socketInfo" );
			
			//获取MessageChannel
			_mainToWorker = worker.getSharedProperty( "mainToWorker" );
			_workerToMain = worker.getSharedProperty( "workerToMain" );
			//监听主线程传给worker的数据
			if ( _mainToWorker )
			{
				_mainToWorker.addEventListener( Event.CHANNEL_MESSAGE, mainToWorker_channelMessageHandler );
			}
			
			//发起连接
			if ( _socketInfo )
			{
				var reconnectInterval:Number = 5000;
				var heartBeatInterval:Number = 30000;
				
				//初始化重连定时器
				_reconnectTimer = new Timer( reconnectInterval );
				_reconnectTimer.addEventListener( TimerEvent.TIMER, reconnectTimer_timerHandler );
				
				//初始化心跳定时器
				_heartBeatTimer = new Timer( heartBeatInterval );
				_heartBeatTimer.addEventListener( TimerEvent.TIMER, heartBeatTimer_timerHandler );
				
				//初始化检查心跳定时器
				_heartBeatCheckTimer = new Timer( heartBeatInterval );
				_heartBeatCheckTimer.addEventListener( TimerEvent.TIMER, heartBeatCheckTimer_timerHandler );
				
				//初始化socket
				_clientSocket = new Socket();
				_clientSocket.addEventListener( Event.CONNECT, socket_connectHandler );
				_clientSocket.addEventListener( IOErrorEvent.IO_ERROR, socket_errorHandler );
				_clientSocket.addEventListener( SecurityErrorEvent.SECURITY_ERROR, socket_securityErrorHandler );
				_clientSocket.addEventListener( Event.CLOSE, socket_closeHandler );
				_clientSocket.addEventListener( ProgressEvent.SOCKET_DATA, socket_socketDataHandler );
				
				connectSocket();
			}
		}
		
		private function connectSocket():void
		{
			//载入安全策略文件
			var securityUrl:String = "xmlsocket://" + _socketInfo.securitySocketIp + ":" + _socketInfo.securitySocketPort;
			Security.loadPolicyFile( securityUrl );
			
			//连接服务端
			_clientSocket.connect( _socketInfo.dataSocketIp, _socketInfo.dataSocketPort );
		}
		
		private function reconnectTimer_timerHandler( event:TimerEvent ):void
		{
			connectSocket();
		}
		
		private function socket_connectHandler( event:Event ):void
		{
			trace( "连接成功" );
			//清除心跳记录
			_heartBeatGuidAC.removeAll();
			
			//停止重连
			if ( _reconnectTimer.running )
			{
				_reconnectTimer.stop();
			}
			
			//开始发送心跳
			if ( !_heartBeatTimer.running )
			{
				_heartBeatTimer.start();
			}
			
			//开始检查心跳
			if ( !_heartBeatCheckTimer.running )
			{
				_heartBeatCheckTimer.start();
			}
		}
		
		private function socket_errorHandler( event:IOErrorEvent ):void
		{
			//开始重连
			if ( !_reconnectTimer.running )
			{
				trace( "IOError, 开始重连。" );
				_reconnectTimer.start();
			}
			
			//停止发送心跳
			if ( _heartBeatTimer.running )
			{
				_heartBeatTimer.stop();
			}
			
			//停止检查心跳
			if ( _heartBeatCheckTimer.running )
			{
				_heartBeatCheckTimer.stop();
			}
		}
		
		private function socket_securityErrorHandler( event:SecurityErrorEvent ):void
		{
			//开始重连
			if ( !_reconnectTimer.running )
			{
				trace( "SecurityError, 开始重连。" );
				_reconnectTimer.start();
			}
			
			//停止发送心跳
			if ( _heartBeatTimer.running )
			{
				_heartBeatTimer.stop();
			}
			
			//停止检查心跳
			if ( _heartBeatCheckTimer.running )
			{
				_heartBeatCheckTimer.stop();
			}
		}
		
		/**
		 * 服务端关闭连接
		 * */
		private function socket_closeHandler( event:Event ):void
		{
			//开始重连
			if ( !_reconnectTimer.running )
			{
				trace( "连接关闭, 开始重连。" );
				_reconnectTimer.start();
			}
			
			//停止发送心跳
			if ( _heartBeatTimer.running )
			{
				_heartBeatTimer.stop();
			}
			
			//停止检查心跳
			if ( _heartBeatCheckTimer.running )
			{
				_heartBeatCheckTimer.stop();
			}
		}
		
		/**
		 * 从服务端接受到数据
		 * */
		private function socket_socketDataHandler( event:ProgressEvent ):void
		{
			var byteArray:ByteArray = new ByteArray();
			_clientSocket.readBytes( byteArray, 0, _clientSocket.bytesAvailable );
			var result:String = byteArray.toString();
			trace( "接收消息: " + result );
			
			//正常的消息以#2开始，#3结束
			if ( result.charCodeAt( 0 ) == 2 && result.charCodeAt( result.length - 1 ) == 3 )
			{
				var msgArray:Array = result.split( String.fromCharCode( 3 ) );
				for each ( var msg:String in msgArray )
				{
					//调用split后已去除结尾的#3
					if ( msg.charCodeAt( 0 ) == 2 )
					{
						//去掉开头的#2
						msg = msg.slice( 1 );
						try
						{
							var msgObj:Object = JSON.parse( msg );
							var operation:String = msgObj.operation;
							switch( operation )
							{
								//心跳消息
								case OPERATION_HEART_BEAT:
									var guid:String = msgObj.guid;
									heartBeatMessageHandler( guid );
									break;
								
								/*case AppEvent.ADD_POINTS:
								var pointType:String = msgObj.type;
								var pointArray:Array = msgObj.points;
								addPointsMessageHandler( pointType, pointArray );
								break;*/
								
								default:
									//消息发送到主线程
									_workerToMain.send( msg );
									break;
							}
						}
						catch (error:Error)
						{
							Alert.show( "JSON解析错误\n" + error.message );
						}
					}
				}
			}
		}
		
		private function mainToWorker_channelMessageHandler( event:Event ):void
		{
			
		}
		
		/**
		 * 向服务端定时发送心跳消息
		 * */
		private function heartBeatTimer_timerHandler( event:TimerEvent ):void
		{
			var guid:String = UIDUtil.createUID();
			var heartBeatDataObj:Object = { operation: OPERATION_HEART_BEAT, guid: guid };
			var heartBeatString:String = JSON.stringify( heartBeatDataObj );
			sendMessage( heartBeatString );
			_heartBeatGuidAC.addItem( guid );
		}
		
		/**
		 * 定时检查服务器回复心跳情况
		 * */
		private function heartBeatCheckTimer_timerHandler( event:TimerEvent ):void
		{
			if ( _heartBeatGuidAC.length >= MAX_HEART_BEAT_FAIL_COUNT )
			{
				_clientSocket.close();
				connectSocket();
			}
		}
		
		/**
		 * 向服务端发送消息。消息以#2开始，#3结束
		 * */
		private function sendMessage( message:String ):void
		{
			var msg:String = String.fromCharCode( 2 ) + message + String.fromCharCode( 3 );
			_clientSocket.writeUTFBytes( msg );
			_clientSocket.flush();
			trace( "发送消息: " + message );
		}
		
		private function heartBeatMessageHandler( guid:String ):void
		{
			if ( _heartBeatGuidAC.getItemIndex( guid ) > -1 )
			{
				//在列表中清除此guid之前的所有记录
				while ( _heartBeatGuidAC.getItemAt( 0 ) != guid )
				{
					_heartBeatGuidAC.removeItemAt( 0 );
				}
				//删除此guid
				_heartBeatGuidAC.removeItemAt( 0 );
			}
		}
		
		private function addPointsMessageHandler( type:String, pointsArray:Array ):void
		{
			_workerToMain.send( type );
		}
		
		/*private function convertStringToAscii( string:String ):String
		{
			var result:String = "";
			for ( var i:uint = 0; i < string.length; i++ )
			{
				result += string.charCodeAt( i ) + " ";
			}
			
			return result;
		}
		
		private function convertArrayCollectionToString( arrayCollection:ArrayCollection ):String
		{
			var result:String = "";
			for ( var i:uint = 0; i < arrayCollection.length; i++ )
			{
				result += i + ":" + arrayCollection.getItemAt( i ) + ",";
			}
			
			return result;
		}*/
	}
}