package com.soenkerohde.foursquare {
	
	import flash.events.IEventDispatcher;
	
	import org.iotashan.oauth.OAuthToken;
	
	public interface IFourSquare extends IEventDispatcher {
		
		/**
		 * @param key OAuth Consumer Key
		 */
		function set clientid( clientid : String ) : void;
		
		/**
		 * @param secret OAuth Consumer Secret
		 */
		function set clientsecret( clientsecret : String ) : void;
		
		/**
		 * @param key Redirect URI
		 */
		function set uri( uri : String ) : void;
		
		/**
		 * Call this method if the user is not authenticated yet.
		 * An OAuth RequestToken will be requested from the TwitterAPI using
		 * the consumerKey and consumerSecret.
		 *
		 * NOTE: consumerKey and consumerSecret have to be set upfront.
		 * Otherwise a TwitterOAuthEvent.CONSUMER_ERROR event will be fired.
		 *
		 * When the RequestToken is retrieved a TwitterOAuthEvent.REQUEST_TOKEN event will be fired.
		 * If this event is not canceled the Twitter Authorize Website will be opened.
		 *
		 * After the user has granted access he will obtain a PIN which he has to enter somewhere
		 * in the application. After the user has done that the AccessToken can be obtained.
		 */
		function authenticate() : void;
		
		/**
		 * @param pin 6 digit PIN which the user has gathered from the Twitter authorize website
		 * after he has granted access to his Twitter account.
		 *
		 * If the PIN is not valid a TwitterOAuthEvent.PIN_ERROR event will be fired.
		 * If the PIN matches an OAuth AccessToken will the requested from the Twitter API
		 * and finally the TwitterOAuthEvent.ACCESS_TOKEN event will be fired.
		 */
		function obtainAccessToken( pin : uint ) : void;
		
		/**
		 *
		 * @param status
		 *
		 */
//		function setStatus( accessToken : OAuthToken, status : String ) : void;
	
	}
}