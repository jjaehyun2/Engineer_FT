package com.hypixel {

	import flash.display.MovieClip;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	import flash.events.Event;
	import com.adobe.serialization.json.JSON;
	import com.hypixel.events.*;
	import com.hypixel.objects.*;

	public class hypixelAPI extends MovieClip {

		private var URL_BASE: String = "https://api.hypixel.net/";
		private var apiKey: String = "";
		private var debug: Boolean = false;
		private var approvedKey: Boolean = false;
		private var keyData: Object = {};
		private var players: Array = [];
		private var guilds: Array = [];
		private var sessions: Array = [];


		public function hypixelAPI(debug: Boolean = false): void {
			this.debug = debug;
			debugTrace("hypixel api enable!");
		}
		public function loadKey(apiKey: String) {
			if(apiKey != null) {
				this.apiKey = apiKey;
				getKeyInfo();
			}
		}
		public function getApiOwner(): String {
			if(approvedKey)
				return keyData['owner'];
			return "";
		}
		public function loadGuildById(id: String) :void{
			if(approvedKey) {
				var loader: URLLoader = new URLLoader();
				var request: URLRequest = new URLRequest(URL_BASE + "guild?key=" + this.apiKey + "&id=" + id);
				loader.addEventListener(Event.COMPLETE, getGuildData);
				loader.load(request);
			}
		}
		public function loadGuildByName(name: String) :void{
			if(approvedKey) {
				var loader: URLLoader = new URLLoader();
				var request: URLRequest = new URLRequest(URL_BASE + "findGuild?key=" + this.apiKey + "&byName=" + name);
				loader.addEventListener(Event.COMPLETE, getFindGuildData);
				loader.load(request);
			}
		}
		public function loadGuildByPlayerName(name: String) :void{
			if(approvedKey) {
				var loader: URLLoader = new URLLoader();
				var request: URLRequest = new URLRequest(URL_BASE + "findGuild?key=" + this.apiKey + "&byPlayer=" + name);
				loader.addEventListener(Event.COMPLETE, getFindGuildData);
				loader.load(request);
			}
		}
		public function loadPlayerByName(name: String) :void{
			if(approvedKey) {
				var loader: URLLoader = new URLLoader();
				var request: URLRequest = new URLRequest(URL_BASE + "player?key=" + this.apiKey + "&name=" + name);
				loader.addEventListener(Event.COMPLETE, getPlayerData);
				loader.load(request);
			}
		}
		public function loadPlayerByUUID(uuid: String) :void{
			if(approvedKey) {
				var loader: URLLoader = new URLLoader();
				var request: URLRequest = new URLRequest(URL_BASE + "player?key=" + this.apiKey + "&uuid=" + uuid);
				loader.addEventListener(Event.COMPLETE, getPlayerData);
				loader.load(request);
			}
		}
		public function loadFriendsByName(name: String) :void{
			if(approvedKey) {
				var loader: URLLoader = new URLLoader();
				var request: URLRequest = new URLRequest(URL_BASE + "friends?key=" + this.apiKey + "&player=" + name);
				loader.addEventListener(Event.COMPLETE, getFriendsData);
				loader.load(request);
			}
		}
		public function loadSessionByName(name: String) :void{
			if(approvedKey) {
				var loader: URLLoader = new URLLoader();
				var request: URLRequest = new URLRequest(URL_BASE + "session?key=" + this.apiKey + "&player=" + name);
				loader.addEventListener(Event.COMPLETE, getSessionData);
				loader.load(request);
			}
		}
		public function loadBoosters() :void{
			if(approvedKey) {
				var loader: URLLoader = new URLLoader();
				var request: URLRequest = new URLRequest(URL_BASE + "boosters?key=" + this.apiKey);
				loader.addEventListener(Event.COMPLETE, getBoostersData);
				loader.load(request);
			}
		}
		public function getPlayer(name: String) :hypixelPlayer{
			return players[name.toLocaleLowerCase()];
		}
		public function getGuild(name: String) :hypixelGuild{
			return guilds[name.toLocaleLowerCase()];
		}
		public function getSession(id: String) {
			return sessions[id];
		}
		private function getKeyInfo(): void {
			var loader: URLLoader = new URLLoader();
			var request: URLRequest = new URLRequest(URL_BASE + "key?key=" + this.apiKey);
			loader.addEventListener(Event.COMPLETE, getKeyData);
			loader.load(request);
		}
		private function getKeyData(evt: Event): void {
			var data: Object = jsonDecode(evt.target.data);
			if(data['success'] && data['record'] != null) {
				debugTrace("key approved!");
				keyData = data['record'];
				approvedKey = true;
				dispatchEvent(new keyApproved(true));
			} else {
				dispatchEvent(new keyApproved(false));
				debugTrace(data['cause']);
			}
		}
		private function getPlayerData(evt: Event): void {
			var data: Object = jsonDecode(evt.target.data);
			if(data['success'] && data['player'] != null) {
				var Name: String = String(data['player']['playername']);
				var Player: hypixelPlayer = new hypixelPlayer(data['player']);
				players[Name.toLocaleLowerCase()] = Player;
				dispatchEvent(new playerLoaded(Player));
				debugTrace("get data of player: " + Name);
			} else {
				dispatchEvent(new playerLoaded(null));
			}
		}
		private function getGuildData(evt: Event): void {
			var data: Object = jsonDecode(evt.target.data);
			if(data['success'] && data['guild'] != null) {
				var Name: String = data['guild']['name'];
				var Guild: hypixelGuild = new hypixelGuild(data['guild']);
				guilds[Name.toLocaleLowerCase()] = Guild;
				dispatchEvent(new guildLoaded(Guild));
				debugTrace("get data of guild: " + Name);
			}
		}
		private function getFindGuildData(evt: Event): void {
			var data: Object = jsonDecode(evt.target.data);
			if(data['success'] && data['guild'] != null) {
				this.loadGuildById(data['guild']);
				debugTrace("get data of guild id: " + data['guild']);
			} else {
				dispatchEvent(new guildLoaded(null));
			}
		}
		private function getFriendsData(evt: Event): void {
			var data: Object = jsonDecode(evt.target.data);
			if(data['success'] && data['records'] != null) {
				dispatchEvent(new friendsLoaded(data['records']));
				debugTrace("friends loaded.");
			}
		}
		private function getSessionData(evt: Event): void {
			var data: Object = jsonDecode(evt.target.data);
			if(data['success'] && data['session'] != null) {
				var session: hypixelSession = new hypixelSession(data['session']);
				sessions[data['session']['_id']] = data['session'];
				dispatchEvent(new sessionLoaded(session));
			} else {
				dispatchEvent(new sessionLoaded(null));
			}
		}
		private function getBoostersData(evt: Event) :void{
			var data: Object = jsonDecode(evt.target.data);
			if(data['success'] && data['boosters'] != null) {
				var Boosters:Array = [];
				for (var i in data['boosters']) {
					Boosters.push(new hypixelBooster(data['boosters'][i]));
				}
				dispatchEvent(new boostersLoaded(Boosters));
			} else {
				dispatchEvent(new boostersLoaded(null));
			}
		}
		private function debugTrace(text: String): void {
			if(this.debug)
				trace(text);
		}
		private function jsonDecode(data: String): Object {
			return com.adobe.serialization.json.JSON.decode(data);
		}
	}

}