package framework.module
{
	[Bindable]
	public class ForgotPasswordModule
	{
		public var currentPage:int = 0;
		
		public var forgotPasswordQuestion:String;
		
		public var loginFormEnable:Boolean = true;
		public var questionFormEnable:Boolean = true;
		public var confirmFormEnable:Boolean = true;
	}
}