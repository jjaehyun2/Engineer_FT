package framework.view.pages.profiles.events
{
	import flash.events.Event;

	public class CompanyEvent extends Event
	{
		public static const CHOOSE_COMPANY:String = "chooseCompany";
		
		/**
		 *  This property is company data.
		 */
		private var _data:Object;
		/**
		 *  This property is company name.
		 */
		private var _name:String;
		/**
		 *  This property is id of company.
		 */
		private var _id:Number;
		
		/**
		 *  CompanyEvent. Constructor.
		 */
		public function CompanyEvent(type:String)
		{
			super(type, bubbles, cancelable);
		}
		
		/**
		 *  @override
		 *  Duplicates an instance of an Event subclass.
		 *  
		 *  @see flash.events.Event#clone
		 */
		override public function clone():Event
		{
			return new CompanyEvent(type);
		}
		
		/**
		 *  Company name.
		 */
		public function get data():Object
		{
			return _data;
		}
		/**
		 *  @private
		 */
		public function set data(value:Object):void
		{
			_data = value;
		}
		
		/**
		 *  Company name.
		 */
		public function get name():String
		{
			return _name;
		}
		/**
		 *  @private
		 */
		public function set name(value:String):void
		{
			_name = value;
		}
		
		/**
		 *  Company name.
		 */
		public function get id():Number
		{
			return _id;
		}
		/**
		 *  @private
		 */
		public function set id(value:Number):void
		{
			_id = value;
		}
	}
}