package models.smsi {
	import com.DebuggerUtils;
	import com.geolocation.GeolocationDistance;
	import com.google.maps.LatLng;
	import com.google.maps.LatLngBounds;
	
	import controls.Alert.AlertPopUp;

	public class SmithMicroHeatMapDataModel {
		public var data:Array = [];
		
		public var target:String;
		
		public var total_count:Number;
		
		public var min_lat:Number;
		public var max_lat:Number;

		public var min_lng:Number;
		public var max_lng:Number;

		public var map_bounds:LatLngBounds;
		public var map_center:LatLng;
		
		private var _i_:int = -1;
		
		public var status:String;
		
		public var results:*; // DO NOT ASSIGN ANY VARIABLES HERE...
		
		public static var OK_SYMBOL:String = 'OK';

		public static var HEAT_LAT_SYMBOL:String = 'heat_lat';
		public static var HEAT_LNG_SYMBOL:String = 'heat_lng';
		public static var HEAT_X_SYMBOL:String = 'heat_x';
		public static var HEAT_Y_SYMBOL:String = 'heat_y';
		public static var HEAT_NUM_SYMBOL:String = 'heat_num';
		
		public static var REQUIRED_COLUMNS:Array = [
			HEAT_LAT_SYMBOL,	
			HEAT_LNG_SYMBOL,	
			HEAT_X_SYMBOL,	
			HEAT_Y_SYMBOL,	
			HEAT_NUM_SYMBOL	
		];
		
		public static var PERCENT_SYMBOL:String = '%';
		public static var GPS_SYMBOL:String = '@';
		
		public function get is_target_valid():Boolean {
			return ( (this.target is String) && (this.target.length > 0) );
		}
		
		private function determine_target(cols:Array):void {
			var j:int;
			if (this.target is String) {
				return;
			}
			for (j = 0; j < REQUIRED_COLUMNS.length; j++) {
				REQUIRED_COLUMNS[j] = String(REQUIRED_COLUMNS[j]).toLowerCase();
			}
			for (j = 0; j < cols.length; j++) {
				if (REQUIRED_COLUMNS.indexOf(String(cols[j]).toLowerCase()) == -1) {
					this.target = cols[j];
					break;
				}
			}
		}
		
		private function determine_percents():void {
			var i:int;
			var aBucket:Object;
			for (i = 0; i < this.data.length; i++) {
				aBucket = this.data[i];
				aBucket[PERCENT_SYMBOL] = aBucket[this.target] / this.total_count;
			}
		}
		
		private function determine_map_center():void {
			this.min_lat = 99;
			this.max_lat = -99;
			this.min_lng = 180;
			this.max_lng = -180;
			var i:int;
			var aBucket:Object;
			var aLatLng:LatLng;
			for (i = 0; i < this.data.length; i++) {
				aBucket = this.data[i];
				aLatLng = aBucket[GPS_SYMBOL] as LatLng;
				//trace(DebuggerUtils.getFunctionName(new Error())+'.1 --> aLatLng='+aLatLng);
				if (aLatLng is LatLng) {
					this.min_lat = Math.min(this.min_lat,aLatLng.lat());
					this.min_lng = Math.min(this.min_lng,aLatLng.lng());
					//trace(DebuggerUtils.getFunctionName(new Error())+'.2 --> this.min_lat='+this.min_lat+', this.min_lng='+this.min_lng);

					this.max_lat = Math.max(this.max_lat,aLatLng.lat());
					this.max_lng = Math.max(this.max_lng,aLatLng.lng());
					//trace(DebuggerUtils.getFunctionName(new Error())+'.3 --> this.max_lat='+this.max_lat+', this.max_lng='+this.max_lng);
				}
			}
			this.map_bounds = new LatLngBounds(new LatLng(this.min_lat,this.max_lng),new LatLng(this.max_lat,this.min_lng));
			//trace(DebuggerUtils.getFunctionName(new Error())+'.4 --> this.map_bounds.getNorthWest='+this.map_bounds.getNorthWest());
			//trace(DebuggerUtils.getFunctionName(new Error())+'.5 --> this.map_bounds.getNorthEast='+this.map_bounds.getNorthEast());
			//trace(DebuggerUtils.getFunctionName(new Error())+'.6 --> this.map_bounds.getSouthWest='+this.map_bounds.getSouthWest());
			//trace(DebuggerUtils.getFunctionName(new Error())+'.7 --> this.map_bounds.getSouthEast='+this.map_bounds.getSouthEast());
			var units:String = GeolocationDistance.convertible_units[0].label;
			var distLeft:Number = GeolocationDistance.distance(this.map_bounds.getNorthWest(),this.map_bounds.getSouthWest(),units);
			var distTop:Number = GeolocationDistance.distance(this.map_bounds.getNorthWest(),this.map_bounds.getNorthEast(),units);
			//trace(DebuggerUtils.getFunctionName(new Error())+'.8 --> distLeft='+distLeft);
			//trace(DebuggerUtils.getFunctionName(new Error())+'.9 --> distTop='+distTop);
			var newLat:Number = this.map_bounds.getNorthWest().lat()+GeolocationDistance.hemispherical_offset_for_lat_or_lng(this.map_bounds.getNorthWest().lat(),GeolocationDistance.delta_from_units_lat((distLeft/2),units),false);
			var newLng:Number = this.map_bounds.getNorthWest().lng()+GeolocationDistance.hemispherical_offset_for_lat_or_lng(this.map_bounds.getNorthWest().lng(),GeolocationDistance.delta_from_units_lng((distTop/2),units),false);
			this.map_center = new LatLng(newLat,newLng);
			//trace(DebuggerUtils.getFunctionName(new Error())+'.10 --> this.map_center='+this.map_center);
			//trace(DebuggerUtils.getFunctionName(new Error())+'.11 --> this.map_bounds.getCenter='+this.map_bounds.getCenter());
			//trace(DebuggerUtils.getFunctionName(new Error())+'.12 --> this.map_bounds='+this.map_bounds);
		}
		
		public function get next_record():Object {
			var i:int = this._i_ + 1;
			if (i < this.data.length) {
				this._i_ = i;
				return this.data[i];
			}
			this._i_ = 0;
			return null;
		}
		
		public function get i():int {
			return (this.data is Array) ? this._i_ : 0;
		}
		
		public function get length():int {
			return (this.data is Array) ? this.data.length : 0;
		}
		
		public function SmithMicroHeatMapDataModel(data:Object) {
			var i:int;
			var j:int;
			var aBucket:Object;
			var datum:Array;
			if ( (data.columns) && (data.results) ) {
				this.determine_target(data.columns);
				this.total_count = 0;
				for (i = 0; i < data.results.length; i++) {
					aBucket = {};
					datum = data.results[i];
					for (j = 0; j < data.columns.length; j++) {
						aBucket[data.columns[j]] = int(datum[j]);
					}
					if (this.is_target_valid) {
						try {
							aBucket[this.target] = Number(aBucket[this.target]);
							this.total_count += aBucket[this.target];
							aBucket[GPS_SYMBOL] = new LatLng(aBucket[HEAT_LAT_SYMBOL]+(aBucket[HEAT_Y_SYMBOL]/aBucket[HEAT_NUM_SYMBOL]),aBucket[HEAT_LNG_SYMBOL]+(aBucket[HEAT_X_SYMBOL]/aBucket[HEAT_NUM_SYMBOL]));
						} catch (err:Error) {}
					}
					this.data.push(aBucket);
				}
				this.determine_percents();
				this.determine_map_center();
				this.status = OK_SYMBOL;
			} else {
				AlertPopUp.surpriseNoOkay('Cannot process your data request at this time due to a data formatting issue.','WARNING');
			}
		}
	}
}