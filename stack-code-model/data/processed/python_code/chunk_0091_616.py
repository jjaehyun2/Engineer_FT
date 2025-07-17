package services.data
{
	public class RequestInfo
	{
		/**
		 *  This property is active gateway.
		 *  
		 *  @default ""
		 */
		public var gateway:String = "";
		/**
		 *  This property is active operation.
		 *  
		 *  @default ""
		 */
		public var operation:String = "";
		/**
		 *  This property is list of arguments for operation.
		 */
		public var args:Object;
	}
}