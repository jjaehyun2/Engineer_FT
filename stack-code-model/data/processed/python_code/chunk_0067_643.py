////////////////////////////////////////////////////////////////////////////////
//
//  Licensed to the Apache Software Foundation (ASF) under one or more
//  contributor license agreements.  See the NOTICE file distributed with
//  this work for additional information regarding copyright ownership.
//  The ASF licenses this file to You under the Apache License, Version 2.0
//  (the "License"); you may not use this file except in compliance with
//  the License.  You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
//
////////////////////////////////////////////////////////////////////////////////
package org.apache.royale.jewel.beads.views
{
	import org.apache.royale.core.IItemRendererParent;
	import org.apache.royale.core.ILayoutView;
	import org.apache.royale.core.IRollOverModel;
	import org.apache.royale.core.ISelectableItemRenderer;
	import org.apache.royale.core.ISelectionModel;
	import org.apache.royale.core.IStrand;
	import org.apache.royale.events.Event;
	import org.apache.royale.events.IEventDispatcher;
	import org.apache.royale.html.beads.DataContainerView;

	/**
	 *  The ListView class creates the visual elements of the org.apache.royale.jewel.List
	 *  component. A List consists of the area to display the data (in the dataGroup), any
	 *  scrollbars, and so forth.
	 *
	 *  @viewbead
	 *  @langversion 3.0
	 *  @playerversion Flash 10.2
	 *  @playerversion AIR 2.6
	 *  @productversion Royale 0.9.4
	 */
	COMPILE::JS
	public class ListView extends DataContainerView
	{
		public function ListView()
		{
			super();
		}

		/**
		 *  @copy org.apache.royale.core.IBead#strand
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.9.4
		 */
		override public function set strand(value:IStrand):void
		{
			super.strand = value;

		}
		private var _dataGroup:IItemRendererParent;
		/**
		 * @royaleignorecoercion org.apache.royale.core.IItemRendererParent
		 */
		override public function get dataGroup():IItemRendererParent
		{
			if(!_dataGroup)
			{
				var c:ILayoutView = contentView;
				if(c && c is IItemRendererParent)
					_dataGroup = c as IItemRendererParent;
				else
					_dataGroup = super.dataGroup;
			}
			return _dataGroup;
		}


		protected var listModel:ISelectionModel;

		protected var lastSelectedIndex:int = -1;

		/**
		 * @private
		 * @royaleignorecoercion org.apache.royale.core.ISelectionModel
		 */
		override protected function handleInitComplete(event:Event):void
		{
			listModel = _strand.getBeadByType(ISelectionModel) as ISelectionModel;
			listModel.addEventListener("selectionChanged", selectionChangeHandler);
			listModel.addEventListener("rollOverIndexChanged", rollOverIndexChangeHandler);
			IEventDispatcher(_strand).addEventListener("itemsCreated", itemsCreatedHandler);

			super.handleInitComplete(event);
		}

		/**
		 * @private
		 * Ensure the list selects the selectedItem if someone is set by the user at creation time
		 */
		override protected function itemsCreatedHandler(event:Event):void
		{
            super.itemsCreatedHandler(event);
			if(listModel.selectedIndex != -1)
				selectionChangeHandler(null);
		}

		/**
		 * @private
		 * @royaleignorecoercion org.apache.royale.core.ISelectableItemRenderer
		 */
		protected function selectionChangeHandler(event:Event):void
		{
			var ir:ISelectableItemRenderer = dataGroup.getItemRendererAt(lastSelectedIndex) as ISelectableItemRenderer;
			if(ir)
				ir.selected = false;
			ir = dataGroup.getItemRendererAt(listModel.selectedIndex) as ISelectableItemRenderer;
			if(ir)
				ir.selected = true;

			lastSelectedIndex = listModel.selectedIndex;
		}

		protected var lastRollOverIndex:int = -1;

		/**
		 * @private
		 * @royaleignorecoercion org.apache.royale.core.ISelectableItemRenderer
		 * * @royaleignorecoercion org.apache.royale.core.IRollOverModel
		 */
		protected function rollOverIndexChangeHandler(event:Event):void
		{
			var ir:ISelectableItemRenderer = dataGroup.getItemRendererAt(lastRollOverIndex) as ISelectableItemRenderer;
			if(ir)
				ir.hovered = false;
			ir = dataGroup.getItemRendererAt((listModel as IRollOverModel).rollOverIndex) as ISelectableItemRenderer;
			if(ir)
				ir.hovered = true;
			lastRollOverIndex = (listModel as IRollOverModel).rollOverIndex;
		}
	}

	COMPILE::SWF
	public class ListView extends DataContainerView
	{
		public function ListView()
		{
			super();
		}

		protected var listModel:ISelectionModel;

		/**
		 *  @copy org.apache.royale.core.IBead#strand
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.9.4
		 */
		override public function set strand(value:IStrand):void
		{
			_strand = value;
			super.strand = value;
		}
		private var _dataGroup:IItemRendererParent;
		override public function get dataGroup():IItemRendererParent
		{
			if(!_dataGroup)
			{
				var c:ILayoutView = contentView;
				if(c && c is IItemRendererParent)
					_dataGroup = c as IItemRendererParent;
				else
					_dataGroup = super.dataGroup;
			}
			return _dataGroup;
		}

		/**
		 * @private
		 */
		override protected function handleInitComplete(event:Event):void
		{
			super.handleInitComplete(event);

			listModel = _strand.getBeadByType(ISelectionModel) as ISelectionModel;
			listModel.addEventListener("selectionChanged", selectionChangeHandler);
			listModel.addEventListener("rollOverIndexChanged", rollOverIndexChangeHandler);
		}

		protected var lastSelectedIndex:int = -1;

		/**
		 * @private
		 */
		protected function selectionChangeHandler(event:Event):void
		{
			var ir:ISelectableItemRenderer = dataGroup.getItemRendererAt(lastSelectedIndex) as ISelectableItemRenderer;
            if (ir)
				ir.selected = false;
			ir = dataGroup.getItemRendererAt(listModel.selectedIndex) as ISelectableItemRenderer;
			if (ir)
				ir.selected = true;
            lastSelectedIndex = listModel.selectedIndex;
		}

		protected var lastRollOverIndex:int = -1;

		/**
		 * @private
		 */
		protected function rollOverIndexChangeHandler(event:Event):void
		{
			var ir:ISelectableItemRenderer = dataGroup.getItemRendererAt(lastRollOverIndex) as ISelectableItemRenderer;
			if(ir)
				ir.hovered = false;
			ir = dataGroup.getItemRendererAt(IRollOverModel(listModel).rollOverIndex) as ISelectableItemRenderer;
			if(ir)
				ir.hovered = true;

			lastRollOverIndex = IRollOverModel(listModel).rollOverIndex;
		}
	}
}