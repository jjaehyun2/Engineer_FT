package org.osflash.ui.components.component
{
	/**
	 * @author Simon Richardson - simon@ustwo.co.uk
	 */
	public class UIComponentModel implements IUIComponentModel
	{
		
		/**
		 * @private
		 */
		private var _id : String;
		
		/**
		 * @private
		 */
		private var _tabIndex : int;
		
		/**
		 * @private
		 */
		private var _keyChar : String;
		
		/**
		 * @private
		 */
		private var _tooltipText : String;
				
		/**
		 * @private
		 */
		private var _component : IUIComponent;
		
		public function UIComponentModel()
		{
			_tabIndex = -1;
		}

		/**
		 * @inheritDoc
		 */		
		public function bind(component : IUIComponent) : void
		{
			if(null == component) throw new ArgumentError('IUIComponent can not be null');
			
			_component = component;
		}

		/**
		 * @inheritDoc
		 */
		public function unbind() : void
		{
			_component = null;
		}
						
		/**
		 * @inheritDoc
		 */
		public function get id() : String { return _id; }
		public function set id(value : String) : void { _id = value; }

		/**
		 * @inheritDoc
		 */
		public function get tabIndex() : int { return _tabIndex; }
		public function set tabIndex(value : int) : void { _tabIndex = value; }

		/**
		 * @inheritDoc
		 */
		public function get keyChar() : String { return _keyChar; }
		public function set keyChar(value : String) : void { _keyChar = value; }
		
		/**
		 * @inheritDoc
		 */
		public function get tooltipText() : String { return _tooltipText; }
		public function set tooltipText(value : String) : void { _tooltipText = value; }
	}
}