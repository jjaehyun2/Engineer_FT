package com.illuzor.circles.tools {
	
	import com.illuzor.circles.events.PlayEvent;
	import com.milkmangames.nativeextensions.*;
	import com.milkmangames.nativeextensions.events.*;
	import starling.events.EventDispatcher;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class PlayManager {
		
		public static const PLAY_100_TIMES:String = "";
		public static const REACH_100_IN_SPEED:String = "";
		public static const REACH_100_IN_SIZE:String = "";
		public static const REACH_100_IN_INSANE:String = "";
		public static const REACH_50_IN_INSANE:String = "";
		
		public static const LEADERBOARD_SPEED:String = "";
		public static const LEADERBOARD_SIZE:String = "";
		public static const LEADERBOARD_INSANE:String = "";
		
		private static var _signedIn:Boolean;
		
		public static var dispatcher:EventDispatcher = new EventDispatcher();
		
		public static function init():void {
			if (GoogleGames.isSupported()) {
				GoogleGames.create();
				GoogleGames.games.addEventListener(GoogleGamesEvent.SIGN_IN_SUCCEEDED, onGoogleGamesEvent);
				GoogleGames.games.addEventListener(GoogleGamesEvent.SIGN_IN_FAILED, onGoogleGamesEvent);
				GoogleGames.games.addEventListener(GoogleGamesEvent.SIGNED_OUT, onGoogleGamesEvent);
				GoogleGames.games.addEventListener(GoogleGamesEvent.SUBMIT_SCORE_SUCCEEDED, onGoogleGamesEvent);
				GoogleGames.games.addEventListener(GoogleGamesEvent.SUBMIT_SCORE_FAILED, onGoogleGamesEvent);
				GoogleGames.games.addEventListener(GoogleGamesEvent.UNLOCK_ACHIEVEMENT_SUCCEEDED, onGoogleGamesEvent);
				GoogleGames.games.addEventListener(GoogleGamesEvent.UNLOCK_ACHIEVEMENT_FAILED, onGoogleGamesEvent);
				GoogleGames.games.signIn();
			}
		}
		
		private static function onGoogleGamesEvent(e:GoogleGamesEvent):void {
			switch (e.type) {
				case GoogleGamesEvent.SIGN_IN_SUCCEEDED: 
					_signedIn = true;
					dispatcher.dispatchEvent(new PlayEvent(PlayEvent.SIGN_IN_SUCCESS));
					trace("SIGN_IN_SUCCEEDED");
				break;
				
				case GoogleGamesEvent.SIGN_IN_FAILED: 
					dispatcher.dispatchEvent(new PlayEvent(PlayEvent.SIGN_IN_FAIL));
					trace("SIGN_IN_FAILED");
				break;
				
				case GoogleGamesEvent.SIGNED_OUT:
					dispatcher.dispatchEvent(new PlayEvent(PlayEvent.SIGN_IN_FAIL));
					trace("SIGNED_OUT");
				break;

				case GoogleGamesEvent.SUBMIT_SCORE_SUCCEEDED: 
					trace("SUBMIT_SCORE_SUCCEEDED");
				break;
				case GoogleGamesEvent.SUBMIT_SCORE_FAILED: 
					trace("SUBMIT_SCORE_FAILED");
				break;
				case GoogleGamesEvent.UNLOCK_ACHIEVEMENT_SUCCEEDED: 
					trace("UNLOCK_ACHIEVEMENT_SUCCEEDED");
				break;
				case GoogleGamesEvent.UNLOCK_ACHIEVEMENT_FAILED: 
					trace("UNLOCK_ACHIEVEMENT_FAILED");
				break;
			}
		}
		
		public static function unlockAchievement(id:String):void {
			GoogleGames.games.unlockAchievement(id);
		}
		
		public static function submitScore(id:String, amount:uint):void {
			GoogleGames.games.submitScore(id, amount);
		}
		
		public static function showLeaderboards():void {
			GoogleGames.games.showLeaderboard();
		}
		
		public static function get signedIn():Boolean {
			return _signedIn;
		}
	
	}
}