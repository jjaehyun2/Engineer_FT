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
package mx.controls
{
	import org.apache.royale.core.IRollOverModel;
	import org.apache.royale.core.IMultiSelectionModel;
	import mx.controls.listClasses.ListBase;
	import org.apache.royale.core.IListPresentationModel;
		import org.apache.royale.core.IDataProviderModel;
import org.apache.royale.html.DataContainer;
	COMPILE::JS
	{
		import org.apache.royale.core.WrappedHTMLElement;
	}

	/**
	 *  Indicates that the initialization of the list is complete.
	 *
	 *  @toplevel
	 *  @langversion 3.0
	 *  @playerversion Flash 10.2
	 *  @playerversion AIR 2.6
	 *  @productversion Royale 0.9.7
	 */
	[Event(name="initComplete", type="org.apache.royale.events.Event")]

	/**
	 * The change event is dispatched whenever the list's selection changes.
	 *
	 *  @langversion 3.0
	 *  @playerversion Flash 10.2
	 *  @playerversion AIR 2.6
	 *  @productversion Royale 0.9.7
	 */
	[Event(name="change", type="org.apache.royale.events.Event")]

	/**
	 *  The MultiSelectionList class is a component that displays multiple data items. The MultiSelectionList uses
	 *  the following bead types:
	 *
	 *  org.apache.royale.core.IBeadModel: the data model, which includes the dataProvider, selectedItems, and
	 *  so forth.
	 *  org.apache.royale.core.IBeadView:  the bead that constructs the visual parts of the list.
	 *  org.apache.royale.core.IBeadController: the bead that handles input and output.
	 *  org.apache.royale.core.IBeadLayout: the bead responsible for the size and position of the itemRenderers.
	 *  org.apache.royale.core.IDataProviderItemRendererMapper: the bead responsible for creating the itemRenders.
	 *  org.apache.royale.core.IItemRenderer: the class or factory used to display an item in the list.
	 *
	 *  @langversion 3.0
	 *  @playerversion Flash 10.2
	 *  @playerversion AIR 2.6
	 *  @productversion Royale 0.9.7
	 */
	public class MultiSelectionList  extends DataContainer
	{
		/**
		 *  constructor.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.9.7
		 */
		public function MultiSelectionList()
		{
			super();
			typeNames += " MultiSelectionList";
		}

		/**
		 *  The index of the currently selected item. Changing this value
		 *  also changes the selectedItems property.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.9.7
		 *  @royaleignorecoercion org.apache.royale.core.IMultiSelectionModel
		 */
		[Bindable("change")]
		 public function get selectedIndices():Array
		{
			return IMultiSelectionModel(model).selectedIndices;
		}

		/**
		 * @royaleignorecoercion org.apache.royale.core.IMultiSelectionModel
		 */
		 public function set selectedIndices(value:Array):void
		{
			IMultiSelectionModel(model).selectedIndices = value;
		}

		/**
		 *  The index of the item currently below the pointer.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.9.7
		 *  @royaleignorecoercion org.apache.royale.core.IRollOverModel
		 */
		 public function get rollOverIndex():int
		{
			return IRollOverModel(model).rollOverIndex;
		}

		/**
		 * @royaleignorecoercion org.apache.royale.core.IRollOverModel
		 */
		 public function set rollOverIndex(value:int):void
		{
			IRollOverModel(model).rollOverIndex = value;
		}

	
		/**
		 *  The items currently selected. Changing this value also
		 *  changes the selectedIndices property.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 10.2
		 *  @playerversion AIR 2.6
		 *  @productversion Royale 0.9.7
		 *  @royaleignorecoercion org.apache.royale.core.IMultiSelectionModel
		 */
		[Bindable("change")]
		 public function get selectedItems():Array
		{
			return IMultiSelectionModel(model).selectedItems;
		}

		/**
		 * @royaleignorecoercion org.apache.royale.core.IMultiSelectionModel
		 */
		 public function set selectedItems(value:Array):void
		{
			IMultiSelectionModel(model).selectedItems = value;
		}
		
		//----------------------------------
		//  includeInLayout
		//----------------------------------

		/**
		 *  @private
		 *  Storage for the includeInLayout property.
		 */
		private var _includeInLayout:Boolean = true;

		/**
		 *  @copy mx.core.UIComponent#includeInLayout
		 *  
		 *  @langversion 3.0
		 *  @playerversion Flash 9
		 *  @playerversion AIR 1.1
		 *  @productversion Flex 3
		 */
		public function get includeInLayout():Boolean
		{
			return _includeInLayout;
		}

		/**
		 *  @private
		 */
		public function set includeInLayout(value:Boolean):void
		{
			if (_includeInLayout != value)
			{
				_includeInLayout = value;
			}
		}
   	}
}