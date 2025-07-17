package eu.claudius.iacob.ui.components {
	import flash.events.Event;
	
	/**
	 * Custom event to be used for comunication between Parameter List Items and the parent List
	 */
	public class ParameterChangeEvent extends Event {
		
		public static const SWATCH_CLICK : String = 'swatchClick';
		public static const VISIBILITY_CHANGE : String = 'visibilityChange';
		public static const LOCK_CHANGE : String = 'lockChange';
		public static const COLOR_CHANGE : String = 'colorChange';
		public static const PARAMETER_CHANGE : String = 'parameterChange';
		public static const NODES_CHANGE : String = 'nodesChange';
		
		private var _type : String;
		private var _data : Object;
		
		override public function get type () : String {
			return _type;
		}
		
		public function get data () : Object {
			return _data;
		} 
		
		/**
		 * Custom event to be used for comunication between Parameter List Items and the parent List
		 * @param	type
		 * 			One of ParameterListEvent.SWATCH_CLICK, ParameterListEvent.VISIBILITY_CLICK or ParameterListEvent.LOCK_CLICK,
		 * 			representing a click on one of the three additional cells in Parameter List Items.
		 * 
		 * @param	data
		 * 			Optional. The current dataset item populating the current item the click occured on.
		 */
		public function ParameterChangeEvent (type : String, data : Object = null) {
			_type = type;
			_data = data;
			super (type, false, false);
		}
		
		/**
		 * @see flash.events.Event.clone
		 */
		override public function clone() : Event {
			return new ParameterChangeEvent (_type, _data);
		}
	}
}