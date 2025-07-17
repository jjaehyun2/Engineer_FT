package 
{	
	import flash.net.Socket;
	public interface Service
	{
		function connect():Boolean;
		function sendMsg(Msg:String):void;
		function getMsg():String;
		function disconnect():void;
		function valifyOrAdd(username:String,password:String):Boolean;
	}
}