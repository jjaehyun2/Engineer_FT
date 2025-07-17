package com.hypixel.objects {

	public class hypixelBooster extends Object {

		private var data: Object = {};

		public function hypixelBooster(data: Object): void {
			this.data = data;
		}
		public function purchaser() :String{
			return data['purchaser'];
		}
		public function originalLength() :int{
			return data['originalLength'];
		}
		public function length() :int{
			return data['length'];
		}
		public function gameType() :int{
			return data['gameType'];
		}
		public function dateActivated() :int{
			return data['dateActivated'];
		}
		public function amount() :int{
			return data['amount'];
		}
	}

}