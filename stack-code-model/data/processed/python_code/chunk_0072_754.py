/*
Feathers
Copyright 2012-2013 Joshua Tynjala. All Rights Reserved.

This program is free software. You can redistribute and/or modify it in
accordance with the terms of the accompanying license agreement.
*/
package feathers.controls.renderers
{
	import feathers.controls.LayoutGroup;
	import feathers.controls.GroupedList;

	import starling.events.Event;

	/**
	 * Based on <code>LayoutGroup</code>, this component is meant as a base
	 * class for creating a custom item renderer for a <code>GroupedList</code>
	 * component.
	 *
	 * <p>Sub-components may be created and added inside <code>initialize()</code>.
	 * This is a good place to add event listeners and to set the layout.</p>
	 *
	 * <p>The <code>data</code> property may be parsed inside <code>commitData()</code>.
	 * Use this function to change properties in your sub-components.</p>
	 *
	 * <p>Sub-components may be positioned manually, but a layout may be
	 * provided as well. An <code>AnchorLayout</code> is recommended for fluid
	 * layouts that can automatically adjust positions when the list resizes.
	 * Create <code>AnchorLayoutData</code> objects to define the constraints.</p>
	 *
	 * <p><strong>Beta Component:</strong> This is a new component, and its APIs
	 * may need some changes between now and the next version of Feathers to
	 * account for overlooked requirements or other issues. Upgrading to future
	 * versions of Feathers may involve manual changes to your code that uses
	 * this component. The
	 * <a href="http://wiki.starling-framework.org/feathers/deprecation-policy">Feathers deprecation policy</a>
	 * will not go into effect until this component's status is upgraded from
	 * beta to stable.</p>
	 *
	 * @see feathers.controls.GroupedList
	 */
	public class LayoutGroupGroupedListItemRenderer extends LayoutGroup implements IGroupedListItemRenderer
	{
		/**
		 * Constructor.
		 */
		public function LayoutGroupGroupedListItemRenderer()
		{
		}

		/**
		 * @private
		 */
		protected var _groupIndex:int = -1;

		/**
		 * @inheritDoc
		 */
		public function get groupIndex():int
		{
			return this._groupIndex;
		}

		/**
		 * @private
		 */
		public function set groupIndex(value:int):void
		{
			this._groupIndex = value;
		}

		/**
		 * @private
		 */
		protected var _itemIndex:int = -1;

		/**
		 * @inheritDoc
		 */
		public function get itemIndex():int
		{
			return this._itemIndex;
		}

		/**
		 * @private
		 */
		public function set itemIndex(value:int):void
		{
			this._itemIndex = value;
		}

		/**
		 * @private
		 */
		protected var _layoutIndex:int = -1;

		/**
		 * @inheritDoc
		 */
		public function get layoutIndex():int
		{
			return this._layoutIndex;
		}

		/**
		 * @private
		 */
		public function set layoutIndex(value:int):void
		{
			this._layoutIndex = value;
		}

		protected var _owner:GroupedList;

		/**
		 * @inheritDoc
		 */
		public function get owner():GroupedList
		{
			return this._owner;
		}

		/**
		 * @private
		 */
		public function set owner(value:GroupedList):void
		{
			if(this._owner == value)
			{
				return;
			}
			this._owner = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected var _data:Object;

		/**
		 * @inheritDoc
		 */
		public function get data():Object
		{
			return this._data;
		}

		/**
		 * @private
		 */
		public function set data(value:Object):void
		{
			if(this._data == value)
			{
				return;
			}
			this._data = value;
			this.invalidate(INVALIDATION_FLAG_DATA);
		}

		/**
		 * @private
		 */
		protected var _isSelected:Boolean;

		/**
		 * @inheritDoc
		 */
		public function get isSelected():Boolean
		{
			return this._isSelected;
		}

		/**
		 * @private
		 */
		public function set isSelected(value:Boolean):void
		{
			if(this._isSelected == value)
			{
				return;
			}
			this._isSelected = value;
			this.invalidate(INVALIDATION_FLAG_SELECTED);
			this.dispatchEventWith(Event.CHANGE);
		}

		/**
		 * @private
		 */
		override public function dispose():void
		{
			this.owner = null;
			super.dispose();
		}

		/**
		 * @private
		 */
		override protected function draw():void
		{
			const dataInvalid:Boolean = this.isInvalid(INVALIDATION_FLAG_DATA);
			if(dataInvalid)
			{
				this.commitData();
			}
			super.draw();
		}

		/**
		 * Updates the renderer to display the item's data. Override this
		 * function to pass data to sub-components and react to data changes.
		 *
		 * <p>Don't forget to handle the case where the data is <code>null</code>.</p>
		 */
		protected function commitData():void
		{

		}

	}
}