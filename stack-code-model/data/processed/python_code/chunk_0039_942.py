package com.hypixel.objects {

	public class hypixelPlayer extends Object {

		private var data: Object = {};

		public function hypixelPlayer(data: Object): void {
			this.data = data;
		}
		public function id(): String {
			return data['_id'];
		}
		public function playerName(): String {
			return data['playername'];
		}
		public function displayName(): String {
			return data['displayname'];
		}
		public function uuid(): String {
			return data['uuid'];
		}
		public function chat(): Boolean {
			return data['chat'];
		}
		public function stoggle(): Boolean {
			return data['stoggle'];
		}
		public function gore(): Boolean {
			return data['gore'];
		}
		public function silence(): Boolean {
			return data['silence'];
		}
		public function vanished(): Boolean {
			if(data['vanished'] != null) {
				return data['vanished'];
			} else {
				return false;
			}
		}
		public function rank(): String {
			if(data['rank'] != null && data['rank'] != "NORMAL") {
				return data['rank'];
			} else if(data['newPackageRank'] != null) {
				return data['newPackageRank'];
			} else if(data['packageRank'] != null) {
				return data['packageRank'];
			} else {
				return "guest";
			}
		}
		public function prefix(): String {
			return data['prefix'];
		}
		public function mutedTime(): Boolean {
			return data['mutedTime'];
		}
		public function firstLogin(): Number {
			return data['firstLogin'];
		}
		public function lastLogin(): Number {
			return data['lastLogin'];
		}
		public function eulaCoins(): Boolean {
			if(data['eulaCoins'] != null) {
				return data['eulaCoins'];
			} else {
				return false;
			}
		}
		public function karma(): int {
			return data['karma'];
		}
		public function networkLevel(): int {
			return data['networkLevel'] + 1;
		}
		public function networkExp(): int {
			return data['networkExp'];
		}
		public function vanityTokens(): int {
			return data['vanityTokens'];
		}
		public function tournamentTokens(): int {
			return data['tournamentTokens'];
		}
		public function timePlaying(): int {
			return data['timePlaying'];
		}
		public function channel(): String {
			return data['channel'];
		}
		public function testPass(): String {
			return data['testPass'];
		}
		public function quests(): Array {
			var quests: Array = [];
			for(var i in data['quests']) {
				quests.push(new hypixelQuest(i, data['quests'][i]));
			}
			return quests;
		}
		public function clock(): Boolean {
			return data['clock'];
		}
		public function achievements(): Object {
			return data['achievements'];
		}
		public function achievementsOneTime(): Object {
			return data['achievementsOneTime'];
		}
		public function fireworkStorage(): Object {
			return data['fireworkStorage'];
		}
		public function mostRecentMinecraftVersion(): int {
			return data['mostRecentMinecraftVersion'];
		}
		public function thanksSent(): int {
			if(data['thanksSent'] != null) {
				return data['thanksSent'];
			} else {
				return 0;
			}
		}
		public function thanksReceived(): int {
			if(data['thanksReceived'] != null) {
				return int(data['thanksReceived']);
			} else {
				return 0;
			}
		}
		public function tipReceived(): int {
			if(data['tipReceived'] != null) {
				return int(data['tipReceived']);
			} else {
				return 0;
			}
		}
		public function tipsSent(): int {
			if(data['tipsSent'] != null) {
				return data['tipsSent'];
			} else {
				return 0;
			}
		}
		public function spectators_invisible(): Boolean {
			if(data['spectators_invisible'] != null) {
				return data['spectators_invisible'];
			} else {
				return false;
			}
		}
		public function spec_spectators_invisible(): Boolean {
			if(data['spec_spectators_invisible'] != null) {
				return data['spec_spectators_invisible'];
			} else {
				return false;
			}
		}
		public function spec_speed(): int {
			return data['spec_speed'];
		}
		public function spec_night_vision(): Boolean {
			return data['spec_night_vision'];
		}
		public function mostRecentlyThanked(): Boolean {
			return data['mostRecentlyThanked'];
		}
		public function mostRecentlyTipped(): String {
			return data['mostRecentlyTipped'];
		}
		public function mostRecentGameType(): String {
			return data['mostRecentGameType'];
		}
		public function vanityMeta(): Array {
			return data['vanityMeta']['packages'];
		}
		public function wardrobe(): Array {
			return data['wardrobe'].split(",");
		}
		public function gadget(): String {
			return data['gadget'];
		}
		public function customFilter(): String {
			return data['customFilter'];
		}
		public function friendRequests(): Array {
			return data['friendRequests'];
		}
		public function petActive(): Boolean {
			return data['petActive'];
		}
		public function auto_spawn_pet(): Boolean {
			if(data['auto_spawn_pet'] != null) {
				return data['auto_spawn_pet'];
			} else {
				return false;
			}
		}
		public function newClock(): String {
			return data['newClock'];
		}
		public function particles(): String {
			return data['pp'];
		}
		public function fly(): Boolean {
			if(data['fly'] != null) {
				return data['fly'];
			} else {
				return false;
			}
		}
		public function packages(): Array {
			return data['packages'];
		}
		public function parkourCompletions(): Object {
			return data['parkourCompletions'];
		}
		public function guildNotifications(): Boolean {
			return data['guildNotifications'];
		}
		public function knownAliases(): Array {
			return data['knownAliases'];
		}
		public function seeRequests(): Boolean {
			if(data['seeRequests'] != null) {
				return data['seeRequests'];
			} else {
				return true;
			}
		}
		public function stats(type: String): Object {
			if(data['stats'][type] != null) {
				return data['stats'][type];
			} else {
				return {};
			}
		}
	}

}