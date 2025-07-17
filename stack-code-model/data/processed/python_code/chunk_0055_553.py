package model.vo {
	import flash.Boot;
	public class PersonVO {
		public function PersonVO(name : String = null,power : int = 0) : void { if( !flash.Boot.skip_constructor ) {
			this.set_name(name);
			this.set_power(power);
		}}
		
		public function get name() : String { return get_name(); }
		public function set name( __v : String ) : void { set_name(__v); }
		protected var $name : String;
		public function get power() : int { return get_power(); }
		public function set power( __v : int ) : void { set_power(__v); }
		protected var $power : int;
		public function get_name() : String {
			return this.$name;
		}
		
		public function set_name(value : String) : String {
			return this.$name = value;
		}
		
		public function get_power() : int {
			return this.$power;
		}
		
		public function set_power(value : int) : int {
			return this.$power = value;
		}
		
	}
}