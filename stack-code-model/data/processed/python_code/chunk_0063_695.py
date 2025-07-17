package services.vo.response
{
	[Bindable]
	[RemoteClass(alias="MapStackTrace")]
	public class StackTraceVO
	{
		/**
		 *  This property contain exception message.
		 */
		public var sExceptionMessage:String;
		/**
		 *  This property contain method, have making exception.
		 */
		public var sMethodName:String;
		/**
		 *  This property contain file name, have making exception.
		 */
		public var sFileName:String;
		/**
		 *  This property contain line number in file with name 
		 *  <code>sFileName</code>. It is place of exception.
		 */
		public var iLineNumber:int;
		/**
		 *  This property contain some description of exception.
		 */
		public var sMapMold:String;
		/**
		 *  This property contain creation date of exception.
		 */
		public var sExceptionDate:String;
	}
}