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

package mx.accessibility
{

import flash.accessibility.Accessibility;
import flash.events.Event;
import mx.accessibility.AccConst;
import mx.collections.CursorBookmark;
import mx.collections.IViewCursor;
import mx.controls.DataGrid;
import mx.controls.listClasses.IListItemRenderer;
import mx.core.UIComponent;
import mx.core.mx_internal;
import mx.events.DataGridEvent;

use namespace mx_internal;

/**
 *  DataGridAccImpl is a subclass of AccessibilityImplementation
 *  which implements accessibility for the DataGrid class.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class DataGridAccImpl extends ListBaseAccImpl
{
    include "../core/Version.as";

	//--------------------------------------------------------------------------
	//
	//  Class methods
	//
	//--------------------------------------------------------------------------

	/**
	 *  Enables accessibility in the DataGrid class.
	 * 
	 *  <p>This method is called by application startup code
	 *  that is autogenerated by the MXML compiler.
	 *  Afterwards, when instances of DataGrid are initialized,
	 *  their <code>accessibilityImplementation</code> property
	 *  will be set to an instance of this class.</p>
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public static function enableAccessibility():void
	{
		DataGrid.createAccessibilityImplementation =
			createAccessibilityImplementation;
	}

	/**
	 *  @private
	 *  Creates a DataGrid's AccessibilityImplementation object.
	 *  This method is called from UIComponent's
	 *  initializeAccessibility() method.
	 */
	mx_internal static function createAccessibilityImplementation(
								component:UIComponent):void
	{
		component.accessibilityImplementation =
			new DataGridAccImpl(component);
	}

	//--------------------------------------------------------------------------
	//
	//  Constructor
	//
	//--------------------------------------------------------------------------

	/**
	 *  Constructor.
	 *
	 *  @param master The UIComponent instance that this AccImpl instance
	 *  is making accessible.
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public function DataGridAccImpl(master:UIComponent)
	{
		super(master);
	}

	//--------------------------------------------------------------------------
	//
	//  Overridden properties: AccImpl
	//
	//--------------------------------------------------------------------------

	//----------------------------------
	//  eventsToHandle
	//----------------------------------

	/**
	 *  @private
	 *	Array of events that we should listen for from the master component.
	 */
	override protected function get eventsToHandle():Array
	{
		return super.eventsToHandle.concat([ DataGridEvent.ITEM_FOCUS_IN ]);
	}
	
	//--------------------------------------------------------------------------
	//
	//  Overridden methods: AccessibilityImplementation
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 *  Gets the role for the component.
	 *
	 *  @param childID Children of the component
	 */
	override public function get_accRole(childID:uint):uint
	{
		return childID == 0 ? role : AccConst.ROLE_SYSTEM_LISTITEM;
	}

	/**
	 *  @private
	 *  IAccessible method for returning the state of the GridItem.
	 *  States are predefined for all the components in MSAA.
	 *  Values are assigned to each state.
	 *  Depending upon the GridItem being Selected, Selectable, Invisible,
	 *  Offscreen, a value is returned.
	 *
	 *  @param childID uint
	 *
	 *  @return State uint
	 */
	override public function get_accState(childID:uint):uint
	{
		var dataGrid:DataGrid = DataGrid(master);

		var accState:uint = getState(childID);
		
		var row:int;
		var col:int;

		// 1 to columnCount * Rows -> ItemRenderers
		if (childID > 0)
		{
			var index:int = childID - 1;
			if (!dataGrid.editable)
			{
				row = index;
				if (row < dataGrid.verticalScrollPosition ||
					row >= dataGrid.verticalScrollPosition 
						+ dataGrid.rowCount - (dataGrid.headerVisible ? 1 : 0))
				{
					accState |= (AccConst.STATE_SYSTEM_OFFSCREEN | AccConst.STATE_SYSTEM_INVISIBLE);
				}
				else
				{
					accState |= AccConst.STATE_SYSTEM_SELECTABLE;

					var renderer:IListItemRenderer = dataGrid.itemToItemRenderer(
						getItemAt(row));

					if (renderer && dataGrid.isItemSelected(renderer.data))
						accState |= AccConst.STATE_SYSTEM_SELECTED | AccConst.STATE_SYSTEM_FOCUSED;
				}
			}
			else
			{
				row = Math.floor(index / dataGrid.columns.length);
				col = index % dataGrid.columns.length;
				
				if (row < dataGrid.verticalScrollPosition ||
					row >= dataGrid.verticalScrollPosition 
						+ dataGrid.rowCount - (dataGrid.headerVisible ? 1 : 0))
				{
					accState |= (AccConst.STATE_SYSTEM_OFFSCREEN | AccConst.STATE_SYSTEM_INVISIBLE);
				}
				else if (dataGrid.columns[col].editable)
				{
					accState |= AccConst.STATE_SYSTEM_SELECTABLE;
					
					var coord:Object = dataGrid.editedItemPosition;
					if (coord &&
						coord.rowIndex == row &&
						coord.columnIndex == col)
					{
						accState |= AccConst.STATE_SYSTEM_SELECTED | AccConst.STATE_SYSTEM_FOCUSED;
					}
				}
			}
		}

		return accState;
	}

	/**
	 *  @private
	 *  IAccessible method for executing the Default Action.
	 *
	 *  @param childID uint
	 */
	override public function accDoDefaultAction(childID:uint):void
	{
		var dataGrid:DataGrid = DataGrid(master);

		if (childID > 0) // see if this check needs to be given
		{
			// Assuming childID is always ItemID + 1
			// because getChildIDArray may not always be invoked.
			var index:int = childID - 1;
			// index is the (0 based) index of the elements after the headers
		
			if (!dataGrid.editable)
			{
				// index is the row id
				dataGrid.selectedIndex = index;
			}
			else
			{
				var row:int = Math.floor(index / dataGrid.columns.length);
				var col:int = index % dataGrid.columns.length;

				dataGrid.editedItemPosition = { rowIndex: row, columnIndex: col };
			}
		}
	}

	/**
	 *  @private
	 *  Method to return an array of childIDs.
	 *
	 *  @return Array
	 */
	override public function getChildIDArray():Array
	{
		var n:int = 0;
		
		var dataGrid:DataGrid = DataGrid(master);
		if (dataGrid.dataProvider)
		{
			// 0 is DataGrid, 1 to columnCount * Rows -> ItemRenderers
			if (!dataGrid.editable) // non editable case (itemRenderers)
				n = dataGrid.dataProvider.length;
			else // editable case (rows)
				n = dataGrid.columns.length * dataGrid.dataProvider.length;
		}

		return createChildIDArray(n);
	}

	/**
	 *  @private
	 *  IAccessible method for returning the bounding box of the GridItem.
	 *
	 *  @param childID uint
	 *
	 *  @return Location Object
	 */
	override public function accLocation(childID:uint):*
	{
		var dataGrid:DataGrid = DataGrid(master);

		var index:int = childID - 1;
		var row:int;
		var col:int;
		var addHeader:int = dataGrid.headerVisible ? 1 : 0;
		
		if (!dataGrid.editable)
		{
			row = index + addHeader;
			
			if (row < dataGrid.verticalScrollPosition ||
				row >= dataGrid.verticalScrollPosition + dataGrid.rowCount)
			{
				return null;
			}

			return dataGrid.indicesToItemRenderer(row - dataGrid.verticalScrollPosition, 0);

		}
		else
		{
			row = Math.floor(index / dataGrid.columns.length) + addHeader;
			col = index % dataGrid.columns.length;

			if (row < dataGrid.verticalScrollPosition ||
				row >= dataGrid.verticalScrollPosition + dataGrid.rowCount)
			{
				return null;
			}
			
			return dataGrid.indicesToItemRenderer(row - dataGrid.verticalScrollPosition, col);
		}
	}

	/**
	 *  @private
	 *  IAccessible method for returning the childFocus of the DataGrid.
	 *
	 *  @param childID uint
	 *
	 *  @return focused childID.
	 */
	override public function get_accFocus():uint
	{
		var dataGrid:DataGrid = DataGrid(master);

		if (!dataGrid.editable)
		{
			var index:uint = dataGrid.selectedIndex;
			
			return index >= 0 ? index + 1 : 0;
		}
		else
		{
			var coord:Object = dataGrid.editedItemPosition;
			if (!coord)
				return 0;

			var row:int = coord.rowIndex;
			var col:int = coord.columnIndex;

			return dataGrid.columns.length * row + col + 1;
		}
	}

	//--------------------------------------------------------------------------
	//
	//  Overridden methods: AccImpl
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 *  method for returning the name of the ListItem/DataGrid
	 *  which is spoken out by the screen reader
	 *  The ListItem should return the label as the name with m of n string and
	 *  DataGrid should return the name specified in the AccessibilityProperties.
	 *
	 *  @param childID uint
	 *
	 *  @return Name String
	 */
	override protected function getName(childID:uint):String
	{
		if (childID == 0)
			return "";

		var dataGrid:DataGrid = DataGrid(master);

		var name:String;

		//1 to columnCount * Rows -> ItemRenderers
		if (childID > 0) // see if this check needs to be given
		{
			// assuming childID is always ItemID + 1
			// because getChildIDArray may not always be invoked.
			var index:int = childID - 1;
			
			// index is the (0 based) index of the elements after the headers
			var row:int
			var item:Object;
			var columns:Array;
			var n:int;
			var i:int;
			
			if (!dataGrid.editable)
			{
				// index is the row id
				row = index;
				item = getItemAt(index);
				if (item is String)
				{
					name = "Row " + (row + 1) + " of " +
						   dataGrid.dataProvider.length + " " + item;
				}
				else
				{
					name = "Row " + (row + 1)  + " of " + dataGrid.dataProvider.length;
					columns = dataGrid.columns;
					n = columns.length;
					for (i = 0; i < n; i++)
					{
						name += " " + columns[i].headerText + " " + columns[i].itemToLabel(item);
					}
				}
			}
			else
			{
				row = Math.floor(index / dataGrid.columns.length);
				var col:int = index % dataGrid.columns.length;

				item = getItemAt(row);
				
				// sometimes item may be an object.
				if (item is String)
				{
					name = "Row " + (row + 1) + " of " +
						   dataGrid.dataProvider.length + " " + item;
				}
				else
				{
					columns = dataGrid.columns;
					
					var itemName:String = columns[i].itemToLabel(item);
					
					var headerText:String = columns[col].headerText;
					
					name = "Row " + (row + 1) + " of " + dataGrid.dataProvider.length;

					//if (dataGrid.selectable == true && dataGrid.isItemSelected(row.data))
					{
						n = columns.length;
						for (i = 0; i < columns.length; i++)
						{
							name += " " + columns[i].headerText + " " + columns[i].itemToLabel(item);
						}
					}
					
					name += ", Editing " + headerText + " " +
							itemName;
				}
			}
		}

		return name;
	}

	//--------------------------------------------------------------------------
	//
	//  Overridden event handlers: AccImpl
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 *  Override the generic event handler.
	 *  All AccImpl must implement this to listen
	 *  for events from its master component. 
	 */
	override protected function eventHandler(event:Event):void
	{
		// Let AccImpl class handle the events
		// that all accessible UIComponents understand.
		$eventHandler(event);

		var dataGrid:DataGrid = DataGrid(master);

		switch (event.type)
		{
			case "change":
			{
				if (!dataGrid.editable)
				{
					var index:int = dataGrid.selectedIndex;
					if (index >= 0)
					{
						var childID:uint = index + 1;

						Accessibility.sendEvent(dataGrid, childID,
												AccConst.EVENT_OBJECT_FOCUS);

						Accessibility.sendEvent(dataGrid, childID,
												AccConst.EVENT_OBJECT_SELECTION);
					}
				}
				break;
			}
			
			case DataGridEvent.ITEM_FOCUS_IN:
			{
				if (dataGrid.editable)
				{
					var item:int = DataGridEvent(event).rowIndex;
					var col:int = DataGridEvent(event).columnIndex;

					Accessibility.sendEvent(dataGrid,
									dataGrid.columns.length * item + col + 1,
									AccConst.EVENT_OBJECT_FOCUS);

					Accessibility.sendEvent(dataGrid,
									dataGrid.columns.length * item + col + 1,
									AccConst.EVENT_OBJECT_SELECTION);
				}
				break;
			}
		}
	}

	//--------------------------------------------------------------------------
	//
	//  Methods
	//
	//--------------------------------------------------------------------------

	/**
	 *  @private
	 */
	private function getItemAt(index:int):Object
	{
		var iterator:IViewCursor = DataGrid(master).collectionIterator;
		iterator.seek(CursorBookmark.FIRST, index);
		return iterator.current;
	}

}

}