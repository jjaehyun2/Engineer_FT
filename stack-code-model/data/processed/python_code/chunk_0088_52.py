package com.gamesparks.api.requests
{

	import com.gamesparks.api.responses.*;
	import com.gamesparks.*;
	
	
	/**
	* Allows a WeChat access token to be used as an authentication mechanism.
	* Once authenticated the platform can determine the current players details from the WeChat platform and store them within GameSparks.
	* If the WeChat user is already linked to a player, the current session will switch to the linked player.
	* If the current player has previously created an account using either DeviceAuthenticationRequest or RegistrationRequest AND the WeChat user is not already registered with the game, the WeChat user will be linked to the current player.
	* If the current player has not authenticated and the WeChat user is not known, a new player will be created using the WeChat details and the session will be authenticated against the new player.
	* If the WeChat user is already known, the session will switch to being the previously created user.
	*/
	public class WeChatConnectRequest extends GSRequest
	{
	
		function WeChatConnectRequest(gs:GS)
		{
			super(gs);
			data["@class"] =  ".WeChatConnectRequest";
		}
		
		/**
		* set the timeout for this request
		*/
		public function setTimeoutSeconds(timeoutSeconds:int=10):WeChatConnectRequest
		{
			this.timeoutSeconds = timeoutSeconds; 
			return this;
		}
		
		/**
		* Send the request to the server. The callback function will be invoked with the response
		*/
		public override function send (callback : Function) : String{
			return super.send( 
				function(message:Object) : void{
					if(callback != null)
					{
						callback(new AuthenticationResponse(message));
					}
				}
			);
		}
		
	
		public function setScriptData(scriptData:Object):WeChatConnectRequest{
			data["scriptData"] = scriptData;
			return this;
		}
	



		/**
		* The access token sould be obtained from WeChat
		* It is used by the client to make authenticated requests on behalf of the end user.
		*/
		public function setAccessToken( accessToken : String ) : WeChatConnectRequest
		{
			this.data["accessToken"] = accessToken;
			return this;
		}


		/**
		* Indicates that the server should not try to link the external profile with the current player.  If false, links the external profile to the currently signed in player.  If true, creates a new player and links the external profile to them.  Defaults to false.
		*/
		public function setDoNotLinkToCurrentPlayer( doNotLinkToCurrentPlayer : Boolean ) : WeChatConnectRequest
		{
			this.data["doNotLinkToCurrentPlayer"] = doNotLinkToCurrentPlayer;
			return this;
		}


		/**
		* Indicates whether the server should return an error if an account switch would have occurred, rather than switching automatically.  Defaults to false.
		*/
		public function setErrorOnSwitch( errorOnSwitch : Boolean ) : WeChatConnectRequest
		{
			this.data["errorOnSwitch"] = errorOnSwitch;
			return this;
		}


		/**
		* The open ID corresponding to the WeChat user
		*/
		public function setOpenId( openId : String ) : WeChatConnectRequest
		{
			this.data["openId"] = openId;
			return this;
		}



		/**
		* An optional segment configuration for this request.
		* If this request creates a new player on the gamesparks platform, the segments of the new player will match the values provided
		*/
		public function setSegments( segments : Object ) : WeChatConnectRequest
		{
			this.data["segments"] = segments;
			return this;
		}


		/**
		* Indicates that the server should switch to the supplied profile if it isalready associated to a player. Defaults to false.
		*/
		public function setSwitchIfPossible( switchIfPossible : Boolean ) : WeChatConnectRequest
		{
			this.data["switchIfPossible"] = switchIfPossible;
			return this;
		}


		/**
		* Indicates that the associated players displayName should be kept in syn with this profile when it's updated by the external provider.
		*/
		public function setSyncDisplayName( syncDisplayName : Boolean ) : WeChatConnectRequest
		{
			this.data["syncDisplayName"] = syncDisplayName;
			return this;
		}
				
	}
	
}