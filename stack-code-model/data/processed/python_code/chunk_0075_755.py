package com.hypixel.objects {

	public class hypixelGuild extends Object {

		private var data: Object = {};

		public function hypixelGuild(data: Object): void {
			this.data = data;
		}
		public function id(): String {
			return data['id'];
		}
		public function name(): String {
			return data['name'];
		}
		public function motd(): String {
			return data['motd'];
		}
		public function canMotd(): Boolean {
			return data['canMotd'];
		}
		public function canParty(): Boolean {
			return data['canParty'];
		}
		public function canTag(): Boolean {
			return data['canTag'];
		}
		public function coins(): int {
			return data['coins'];
		}
		public function coinsEver(): int {
			return data['coinsEver'];
		}
		public function members(): Array {
			return data['members'];
		}
		public function created(): int {
			return data['created'];
		}
		public function memberSizeLevel(): int {
			return data['memberSizeLevel'];
		}
		public function bankSizeLevel(): int {
			return data['bankSizeLevel'];
		}
	}

}