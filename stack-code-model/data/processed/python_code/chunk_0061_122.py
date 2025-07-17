package services.business.frontend
{
	import services.cairngorm.BaseDelegate;
	import services.events.frontend.LoginEvent;
	import services.Services;
	import services.vo.frontend.UserCredentialsVO;
	
	import h2olib.crypt.MD5;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;
	
	public class LoginDelegate extends BaseDelegate
	{
		public function LoginDelegate(responder:IResponder)
		{
			super(responder);
		}
		
		public function sendLogin(event:LoginEvent):void
		{
			var userCredentials:UserCredentialsVO = new UserCredentialsVO(event.userLogin,MD5.encrypt(event.userPassword));			
			operation = service.getRemoteObject(Services.SERVICE_LOGIN).getOperation("LoginAction");
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(userCredentials);
		}
	}
}