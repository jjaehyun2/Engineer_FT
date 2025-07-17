package com.soenkerohde.foursquare {
	import com.adobe.serialization.json.JSONDecoder;
	import com.soenkerohde.foursquare.event.FourSquareOAuthEvent;
	
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.events.IOErrorEvent;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	import flash.net.URLVariables;
	import flash.net.navigateToURL;
	
	import org.iotashan.oauth.OAuthConsumer;
	import org.iotashan.oauth.OAuthRequest;
	import org.iotashan.oauth.OAuthSignatureMethod_HMAC_SHA1;
	import org.iotashan.oauth.OAuthToken;
	import org.iotashan.utils.URLEncoding;
	
	public class FourSquare extends EventDispatcher implements IFourSquare {
		
		private static const CLIENT_ID_SYMBOL:String = '{{CLIENT_ID}}';
		private static const YOUR_REGISTERED_REDIRECT_URI_SYMBOL:String = '{{YOUR_REGISTERED_REDIRECT_URI}}';
		
		private static const DISPLAY_TOUCH_SYMBOL:String = 'display=touch';
		
		public static const REQUEST_TOKEN:String = "https://foursquare.com/oauth2/authenticate?client_id="+CLIENT_ID_SYMBOL+"&response_type=token&redirect_uri="+YOUR_REGISTERED_REDIRECT_URI_SYMBOL+"&"+DISPLAY_TOUCH_SYMBOL;
		public static const ACCESS_TOKEN:String = "https://foursquare.com/oauth2/access_token";
		public static const AUTHORIZE:String = "https://foursquare.com/oauth2/authorize";
		
		public static function getTokenFromResponse( tokenResponse : String ) : OAuthToken {
			var result:OAuthToken = new OAuthToken();
			
			var params:Array = tokenResponse.split( "&" );
			for each ( var param : String in params ) {
				var paramNameValue:Array = param.split( "=" );
				if ( paramNameValue.length == 2 ) {
					if ( paramNameValue[0] == "oauth_token" ) {
						result.key = paramNameValue[1];
					} else if ( paramNameValue[0] == "oauth_token_secret" ) {
						result.secret = paramNameValue[1];
					}
				}
			}
			
			return result;
		}
		
		protected var signature:OAuthSignatureMethod_HMAC_SHA1 = new OAuthSignatureMethod_HMAC_SHA1();
		
		protected var requestToken:OAuthToken;
		protected var accessToken:OAuthToken;
		
		private var _clientid:String;
		private var _clientsecret:String;
		private var _uri:String;
		
		private var _consumer:OAuthConsumer;
		
		public function set clientid( key : String ) : void {
			_clientid = key;
		}
		
		public function set clientsecret( secret : String ) : void {
			_clientsecret = secret;
		}
		
		public function set uri( uri : String ) : void {
			_uri = uri;
		}
		
		private function get consumer() : OAuthConsumer {
			if ( _consumer == null && _clientid != null && _clientsecret != null ) {
				_consumer = new OAuthConsumer( _clientid, _clientsecret );
			}
			return _consumer;
		}
		
		public function FourSquare( clientid : String = null, clientsecret : String = null ) {
			_clientid = clientid;
			_clientsecret = clientsecret;
		}
		
		public function setAccessToken( token : OAuthToken ) : void {
			accessToken = token;
		}
		
		public function authenticate() : void {
			var token:String = REQUEST_TOKEN.replace(CLIENT_ID_SYMBOL,this._clientid).replace(YOUR_REGISTERED_REDIRECT_URI_SYMBOL,this._uri);
			trace('token='+token);
			var oauthRequest:OAuthRequest = new OAuthRequest( "GET", token, null, consumer, null );
			var request:URLRequest = new URLRequest( oauthRequest.buildRequest( signature ) );
			var loader:URLLoader = new URLLoader( request );
			loader.addEventListener( Event.COMPLETE, requestTokenHandler );
			loader.addEventListener(IOErrorEvent.IO_ERROR, 
				function (event:IOErrorEvent):void {
					trace(event.toString());
					trace(event.target.data);
				}
			);
		}
		
		protected function requestTokenHandler( e : Event ) : void {
			requestToken = getTokenFromResponse( e.currentTarget.data as String );
			if ( dispatchEvent( new FourSquareOAuthEvent( FourSquareOAuthEvent.REQUEST_TOKEN, requestToken ) ) ) {
				var request:URLRequest = new URLRequest( AUTHORIZE + "?oauth_token=" + requestToken.key + "&" + DISPLAY_TOUCH_SYMBOL);
				navigateToURL( request, "_blank" );
			}
		}
		
		public function obtainAccessToken( pin : uint ) : void {
			var oauthRequest:OAuthRequest = new OAuthRequest( "GET", ACCESS_TOKEN, { oauth_verifier: pin }, consumer, requestToken );
			var request:URLRequest = new URLRequest( oauthRequest.buildRequest( signature, OAuthRequest.RESULT_TYPE_URL_STRING ) );
			request.method = "GET";
			
			var loader:URLLoader = new URLLoader( request );
			loader.addEventListener( Event.COMPLETE, accessTokenResultHandler );
		}
		
		protected function accessTokenResultHandler( event : Event ) : void {
			var accessToken:OAuthToken = getTokenFromResponse( event.currentTarget.data as String );
			if ( dispatchEvent( new FourSquareOAuthEvent( FourSquareOAuthEvent.ACCESS_TOKEN, accessToken ) ) ) {
				setAccessToken( accessToken );
			}
		}
		
	}
}