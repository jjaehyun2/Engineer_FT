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

package mx.controls.dataGridClasses
{

import flash.display.DisplayObject;
import flash.events.Event;
import flash.utils.Dictionary;

import mx.controls.TextInput;
import mx.controls.listClasses.IListItemRenderer;
import mx.core.ClassFactory;
import mx.core.ContextualClassFactory;
import mx.core.IEmbeddedFontRegistry;
import mx.core.IFactory;
import mx.core.IFlexModuleFactory;
import mx.core.IIMESupport;
import mx.core.Singleton;
import mx.core.mx_internal;
import mx.styles.CSSStyleDeclaration;
import mx.styles.StyleManager;
import mx.utils.StringUtil;

use namespace mx_internal;

//--------------------------------------
//  Styles
//--------------------------------------

include "../../styles/metadata/TextStyles.as";

/**
 *  The Background color of the column.
 *  The default value is <code>undefined</code>, which means it uses the value of the 
 *  <code>backgroundColor</code> style of the associated DataGrid control.
 *  The default value for the DataGrid control is <code>0xFFFFFF</code>.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="backgroundColor", type="uint", format="Color", inherit="no")]

/**
 *  The name of a CSS style declaration for controlling other aspects of
 *  the appearance of the column headers.
 *  The default value is <code>undefined</code>, which means it uses the value of the 
 *  <code>headerStyleName</code> style of the associated DataGrid control.
 *  The default value for the DataGrid control is 
 *  <code>".dataGridStyles"</code>.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="headerStyleName", type="String", inherit="no")]

/**
 *  The number of pixels between the container's left border and its content 
 *  area.
 *  @default 0
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="paddingLeft", type="Number", format="Length", inherit="no")]

/**
 *  The number of pixels between the container's right border and its content 
 *  area.
 *  @default 0
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
[Style(name="paddingRight", type="Number", format="Length", inherit="no")]

/**
 *  The DataGridColumn class describes a column in a DataGrid control.
 *  There is one DataGridColumn per displayable column, even if a column
 *  is hidden or off-screen.
 *  The data provider items of a DataGrid control 
 *  can contain properties that are not displayed
 *  and, therefore, do not need a DataGridColumn.
 *  A DataGridColumn allows specification of the color and font of the text
 *  in a column; what kind of component displays the data for the column;
 *  whether the column is editable, sortable, or resizable;
 *  and the text for the column header.
 *
 *  <p><strong>Notes:</strong><ul>
 *  <li>A DataGridColumn only holds information about a column;
 *  it is not the parent of the item renderers in the column.</li>
 *  <li>If you specify a DataGridColumn class without a <code>dataField</code>
 *  property, you must specify a <code>sortCompareFunction</code>
 *  property. Otherwise, sort operations may cause run-time errors.</li></ul> 
 *  </p>
 *
 *  @mxml
 *
 *  <p>You use the <code>&lt;mx.DataGridColumn&gt;</code> tag to configure a column
 *  of a DataGrid control.
 *  You specify the <code>&lt;mx.DataGridColumn&gt;</code> tag as a child
 *  of the columns property in MXML.
 *  The <code>&lt;mx.DataGridColumn&gt;</code> tag inherits all of the 
 *  tag attributes of its superclass, and adds the following tag attributes:</p>
 *
 *  <pre>
 *  &lt;mx:DataGridColumn
 *  <b>Properties </b>
 *    dataField="<i>No default</i>"
 *    dataTipField="<i>No default</i>"
 *    dataTipFunction="<i>No default</i>"
 *    editable="true|false"
 *    editorDataField="text"
 *    editorHeightOffset="0"
 *    editorUsesEnterKey="false|true"
 *    editorWidthOffset="0"
 *    editorXOffset="0"
 *    editorYOffset="0"
 *    headerRenderer="DataGridItemRenderer"
 *    headerText="<i>No default</i>"
 *    headerWordWrap="undefined"
 *    imeMode="null"
 *    itemEditor="TextInput"
 *    itemRenderer="DataGridItemRenderer"
 *    labelFunction="<i>No default</i>"
 *    minWidth="20"
 *    rendererIsEditor="false|true"
 *    resizable="true|false"
 *    showDataTips="false|true"
 *    sortable="true|false"
 *    sortCompareFunction="<i>No default</i>"
 *    sortDescending="false|true"
 *    visible="true|false"
 *    width="100"
 *    wordWrap="false|true"
 * 
 *  <b>Styles</b>
 *    backgroundColor="0xFFFFFF"
 *    color="<i>No default.</i>"
 *    disabledColor="0xAAB3B3"
 *    fontAntiAliasType="advanced"
 *    fontFamily="<i>No default</i>"
 *    fontGridFitType="pixel"
 *    fontSharpness="0"
 *    fontSize="<i>No default</i>"
 *    fontStyle="normal|italic"
 *    fontThickness="0"
 *    fontWeight="normal|bold"
 *    headerStyleName="<i>No default</i>"
 *    paddingLeft="0"
 *    paddingRight="0"
 *    textAlign="right|center|left"
 *    textDecoration="none|underline"
 *    textIndent="0"
 *  /&gt;
 *  </pre>
 *  </p>
 *
 *  @see mx.controls.DataGrid
 *
 *  @see mx.styles.CSSStyleDeclaration
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class DataGridColumn extends CSSStyleDeclaration implements IIMESupport
{
    include "../../core/Version.as";

    //--------------------------------------------------------------------------
    //
    //  Class properties
    //
    //--------------------------------------------------------------------------

    //----------------------------------
    //  embeddedFontRegistry
    //----------------------------------

    private static var noEmbeddedFonts:Boolean;

    /**
     *  @private
     *  Storage for the embeddedFontRegistry property.
     *  This gets initialized on first access,
     *  not at static initialization time, in order to ensure
     *  that the Singleton registry has already been initialized.
     */
    private static var _embeddedFontRegistry:IEmbeddedFontRegistry;

    /**
     *  @private
     *  A reference to the embedded font registry.
     *  Single registry in the system.
     *  Used to look up the moduleFactory of a font.
     */
    private static function get embeddedFontRegistry():IEmbeddedFontRegistry
    {
        if (!_embeddedFontRegistry && !noEmbeddedFonts)
        {
            try
            {
                _embeddedFontRegistry = IEmbeddedFontRegistry(
                    Singleton.getInstance("mx.core::IEmbeddedFontRegistry"));
            }
            catch (e:Error)
            {
                noEmbeddedFonts = true;
            }
        }

        return _embeddedFontRegistry;
    }

    private static var _defaultItemEditorFactory:IFactory;

    mx_internal static function get defaultItemEditorFactory():IFactory
    {
        if (!_defaultItemEditorFactory)
            _defaultItemEditorFactory = new ClassFactory(TextInput);
        return _defaultItemEditorFactory;
    }

    //--------------------------------------------------------------------------
    //
    //  Constructor
    //
    //--------------------------------------------------------------------------

    /**
     *  Constructor.
     *
     *  @param columnName The name of the field in the data provider 
     *  associated with the column, and the text for the header cell of this 
     *  column.  This is equivalent to setting the <code>dataField</code>
     *  and <code>headerText</code> properties.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function DataGridColumn(columnName:String = null)
    {
        super();

        if (columnName)
        {
            dataField = columnName;
            headerText = columnName;
        }
    }

    //--------------------------------------------------------------------------
    //
    //  Variables
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     *  The DataGrid that owns this column.
     */
    mx_internal var owner:DataGridBase;

    /**
     *  @private
     */
    mx_internal var explicitWidth:Number;

    /**
     *  @private
     *  cached header renderer so we don't have to keep
     *  making new ones
     */
    mx_internal var cachedHeaderRenderer:IListItemRenderer;

    /**
     *  @private
     * Holds the last recorded value of the module factory used to create the font.
     */
    private var oldEmbeddedFontContext:IFlexModuleFactory = null;
    private var oldHeaderEmbeddedFontContext:IFlexModuleFactory = null;

    /**
     *  @private
     * 
     * Columns has complex data field named.
     */
    protected var hasComplexFieldName:Boolean = false;

    /**
     *  @private
     * 
     * Array of split complex field name derived when set so that it is not derived each time.
     */
    protected var complexFieldNameComponents:Array;
         
    //--------------------------------------------------------------------------
    //
    //  Overridden properties
    //
    //--------------------------------------------------------------------------

    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------

    //----------------------------------
    //  sortDescending
    //----------------------------------

    /**
     *  Indicates whether the column sort is
     *  in ascending order, <code>false</code>, 
     *  or <code>descending</code> order, true.
     *
     *  <p>Setting this property does not start a sort; it only sets the sort direction.
     *  Click on the column header to perform the sort.</p>
     *  
     *  @default false;
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var sortDescending:Boolean = false;

    //----------------------------------
    //  itemRenderer
    //----------------------------------
    /**
     *  @private
     *  Storage for the itemRenderer property.
     */
    private var _itemRenderer:IFactory;
    private var _contextItemRenderer:IFactory;

    [Bindable("itemRendererChanged")]
    [Inspectable(category="Other")]

    /**
     *  The class factory for item renderer instances that display the 
     *  data for each item in the column.
     *  You can specify a drop-in item renderer,
     *  an inline item renderer, or a custom item renderer component as the 
     *  value of this property.
     *
     *  <p>The default item renderer is the DataGridItemRenderer class,
     *  which displays the item data as text. </p>
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get itemRenderer():IFactory
    {
        return _itemRenderer;
    }

    /**
     *  @private
     */
    public function set itemRenderer(value:IFactory):void
    {
        _itemRenderer = value;
        
        // this is expensive... but unless set after init (not recommended), ok.
        if (owner)
        {
            owner.invalidateList();
            owner.columnRendererChanged(this);
            _contextItemRenderer = null;
        }

        dispatchEvent(new Event("itemRendererChanged"));
    }

    //----------------------------------
    //  colNum
    //----------------------------------

    /**
     *  @private
     *  The zero-based index of this column as it is displayed in the grid.
     *  It is not related to the structure of the data being displayed.
     *  In MXML, the default order of the columns is the order of the
     *  <code>mx:DataGridColumn</code> tags.
     */
    mx_internal var colNum:Number;

    //----------------------------------
    //  dataField
    //----------------------------------

    /**
     *  @private
     *  Storage for the dataField property.
     */
    private var _dataField:String;

    [Inspectable(category="General", defaultValue="")]

    /**
     *  The name of the field or property in the data provider item associated 
     *  with the column. 
     *  Each DataGridColumn control
     *  requires this property and/or the <code>labelFunction</code> property 
     *  to be set in order to calculate the displayable text for the item
     *  renderer.
     *  If the <code>dataField</code>
     *  and <code>labelFunction</code> properties are set, 
     *  the data is displayed using the <code>labelFunction</code> and sorted
     *  using the <code>dataField</code>.  If the property named in the
     *  <code>dataField</code> does not exist, the 
     *  <code>sortCompareFunction</code> must be set for the sort to work
     *  correctly.
     *
     *  <p>This value of this property is not necessarily the String that 
     *  is displayed in the column header.  This property is
     *  used only to access the data in the data provider. 
     *  For more information, see the <code>headerText</code> property.</p>
     *
     *  @see #headerText 
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
     public function get dataField():String
     {
          return _dataField;
     }

     /**
      *  @private
      */
     public function set dataField(value:String):void
     {
        _dataField = value;
  
        if ( value.indexOf( "." ) != -1 ) 
        {
            hasComplexFieldName = true;
            complexFieldNameComponents = value.split( "." );
            
            if ( _sortCompareFunction == null ) 
            {
                //if the sort field is null, but the user supplied a complex dataField, we will assign a generic
                //sort compare that handles this situation. It will yield identical results to the sort created in
                //datagrid under normal circumstances
                
                //intentionally not using the setter, the user might still override this or be looking for that change
                //we want to this to be purely happen behind the scenes if there is no function provided
                _sortCompareFunction = complexColumnSortCompare;
            }
            
        }
        else
            hasComplexFieldName = false;

        if (owner)
            owner.invalidateList();
     }

    //----------------------------------
    //  dataTipField
    //----------------------------------

    /**
     *  @private
     *  Storage for the dataTipField property.
     */
    private var _dataTipField:String;

    [Bindable("dataTipFieldChanged")]
    [Inspectable(category="Advanced", defaultValue="label")]

    /**
     *  The name of the field in the data provider to display as the datatip. 
     *  By default, the DataGrid control looks for a property named 
     *  <code>label</code> on each data provider item and displays it.
     *  However, if the data provider does not contain a <code>label</code>
     *  property, you can set the <code>dataTipField</code> property to
     *  specify a different property.  
     *  For example, you could set the value to "FullName" when a user views a
     *  set of people's names included from a database.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get dataTipField():String
    {
        return _dataTipField;
    }

    /**
     *  @private
     */
    public function set dataTipField(value:String):void
    {
        _dataTipField = value;

        if (owner)
        {
            owner.invalidateList();
        }

        dispatchEvent(new Event("dataTipChanged"));
    }

    //----------------------------------
    //  dataTipFunction
    //----------------------------------

    /**
     *  @private
     *  Storage for the dataTipFunction property.
     */
    private var _dataTipFunction:Function;

    [Bindable("dataTipFunctionChanged")]
    [Inspectable(category="Advanced")]

    /**
     *  Specifies a callback function to run on each item of the data provider 
     *  to determine its dataTip.
     *  This property is used by the <code>itemToDataTip</code> method.
     * 
     *  <p>By default the control looks for a property named <code>label</code>
     *  on each data provider item and displays it as its dataTip.
     *  However, some data providers do not have a <code>label</code> property 
     *  nor do they have another property that you can use for displaying data 
     *  in the rows.
     *  For example, you might have a data provider that contains a lastName 
     *  and firstName fields, but you want to display full names as the dataTip.
     *  You can specify a function to the <code>dataTipFunction</code> property 
     *  that returns a single String containing the value of both fields. You 
     *  can also use the <code>dataTipFunction</code> property for handling 
     *  formatting and localization.</p>
     * 
     *  <p>The function must take a single Object parameter, containing the
     *  data provider element, and return a String.</p>
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get dataTipFunction():Function
    {
        return _dataTipFunction;
    }

    /**
     *  @private
     */
    public function set dataTipFunction(value:Function):void
    {
        _dataTipFunction = value;

        if (owner)
        {
            owner.invalidateList();
        }

        dispatchEvent(new Event("labelFunctionChanged"));
    }

    //----------------------------------
    //  draggable
    //----------------------------------

    [Inspectable(category="General")]

    /**
     *  A flag that indicates whether the user is allowed to drag
     *  the column to a new position
     *  If <code>true</code>, the user can drag the 
     *  the column headers to a new position
     *
     *  @default true
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var draggable:Boolean = true;

    //----------------------------------
    //  editable
    //----------------------------------

    private var _editable:Boolean = true;

    [Inspectable(category="General")]

    /**
     *  A flag that indicates whether the items in the column are editable.
     *  If <code>true</code>, and the DataGrid's <code>editable</code>
     *  property is also <code>true</code>, the items in a column are 
     *  editable and can be individually edited
     *  by clicking on an item or by navigating to the item by using the 
     *  Tab and Arrow keys.
     *
     *  @default true
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get editable():Boolean
    {
        return _editable;
    }

    /**
     *  @private
     */
    public function set editable(value:Boolean):void
    {
        _editable = value;
    }


    //----------------------------------
    //  itemEditor
    //----------------------------------

    [Inspectable(category="General")]

    /**
     *  A class factory for the instances of the item editor to use for the 
     *  column, when it is editable.
     *
     *  @default new ClassFactory(mx.controls.TextInput)
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var itemEditor:IFactory = defaultItemEditorFactory;

    //----------------------------------
    //  editorDataField
    //----------------------------------

    [Inspectable(category="General")]

    /**
     *  The name of the property of the item editor that contains the new
     *  data for the list item.
     *  For example, the default <code>itemEditor</code> is
     *  TextInput, so the default value of the <code>editorDataField</code> 
     *  property is <code>"text"</code>, which specifies the 
     *  <code>text</code> property of the TextInput control.
     *
     *  @default "text"
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var editorDataField:String = "text";

    //----------------------------------
    //  editorHeightOffset
    //----------------------------------

    [Inspectable(category="General", defaultValue="0")]

    /**
     *  The height of the item editor, in pixels, relative to the size of the 
     *  item renderer.  This property can be used to make the editor overlap
     *  the item renderer by a few pixels to compensate for a border around the
     *  editor.  
     *  Note that changing these values while the editor is displayed
     *  will have no effect on the current editor, but will affect the next
     *  item renderer that opens an editor.
     *
     *  @default 0
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var editorHeightOffset:Number = 0;

    //----------------------------------
    //  editorWidthOffset
    //----------------------------------

    [Inspectable(category="General", defaultValue="0")]

    /**
     *  The width of the item editor, in pixels, relative to the size of the 
     *  item renderer.  This property can be used to make the editor overlap
     *  the item renderer by a few pixels to compensate for a border around the
     *  editor.
     *  Note that changing these values while the editor is displayed
     *  will have no effect on the current editor, but will affect the next
     *  item renderer that opens an editor.
     *
     *  @default 0
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var editorWidthOffset:Number = 0;

    //----------------------------------
    //  editorXOffset
    //----------------------------------

    [Inspectable(category="General", defaultValue="0")]

    /**
     *  The x location of the upper-left corner of the item editor,
     *  in pixels, relative to the upper-left corner of the item.
     *  This property can be used to make the editor overlap
     *  the item renderer by a few pixels to compensate for a border around the
     *  editor.
     *  Note that changing these values while the editor is displayed
     *  will have no effect on the current editor, but will affect the next
     *  item renderer that opens an editor.
     * 
     *  @default 0
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var editorXOffset:Number = 0;

    //----------------------------------
    //  editorYOffset
    //----------------------------------

    [Inspectable(category="General", defaultValue="0")]

    /**
     *  The y location of the upper-left corner of the item editor,
     *  in pixels, relative to the upper-left corner of the item.
     *  This property can be used to make the editor overlap
     *  the item renderer by a few pixels to compensate for a border around the
     *  editor.
     *  Note that changing these values while the editor is displayed
     *  will have no effect on the current editor, but will affect the next
     *  item renderer that opens an editor.
     *
     *  @default 0
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var editorYOffset:Number = 0;

    //----------------------------------
    //  editorUsesEnterKey
    //----------------------------------

    [Inspectable(category="General", defaultValue="false")]

    /**
     *  A flag that indicates whether the item editor uses Enter key.
     *  If <code>true</code> the item editor uses the Enter key and the
     *  DataGrid will not look for the Enter key and move the editor in
     *  response.
     *  Note that changing this value while the editor is displayed
     *  will have no effect on the current editor, but will affect the next
     *  item renderer that opens an editor.
     *
     *  @default false.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var editorUsesEnterKey:Boolean = false;

    //----------------------------------
    //  enableIME
    //----------------------------------

    /**
     *  A flag that indicates whether the IME should
     *  be enabled when the component receives focus.
     *
     *  If an editor is up, it will set enableIME
     *  accordingly.
     *
     *  @langversion 3.0
     *  @playerversion Flash 10
     *  @playerversion AIR 1.5
     *  @productversion Flex 4
     */
    public function get enableIME():Boolean
    {
        return false;
    }

    //----------------------------------
    //  headerRenderer
    //----------------------------------

    /**
     *  @private
     *  Storage for the headerRenderer property.
     */
    private var _headerRenderer:IFactory;
    private var _contextHeaderRenderer:IFactory;

    [Bindable("headerRendererChanged")]
    [Inspectable(category="Other")]

    /**
     *  The class factory for item renderer instances that display the 
     *  column header for the column.
     *  You can specify a drop-in item renderer,
     *  an inline item renderer, or a custom item renderer component as the 
     *  value of this property.
     *
     *  <p>The default item renderer is the DataGridItemRenderer class,
     *  which displays the item data as text. </p>
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get headerRenderer():IFactory
    {
        return _headerRenderer;
    }

    /**
     *  @private
     */
    public function set headerRenderer(value:IFactory):void
    {
        _headerRenderer = value;

        // rebuild the headers
        if (owner)
        {
            owner.invalidateList();
            owner.columnRendererChanged(this);
            _contextHeaderRenderer = null;
        }

        dispatchEvent(new Event("headerRendererChanged"));
    }

    //----------------------------------
    //  headerText
    //----------------------------------

    /**
     *  @private
     *  Storage for the headerText property.
     */
    private var _headerText:String;

    [Bindable("headerTextChanged")]
    [Inspectable(category="General")]

    /**
     *  Text for the header of this column. By default, the DataGrid
     *  control uses the value of the <code>dataField</code> property 
     *  as the header text.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get headerText():String
    {
        return (_headerText != null) ? _headerText : dataField;
    }

    /**
     *  @private
     */
    public function set headerText(value:String):void
    {
        _headerText = value;

        if (owner)
            owner.invalidateList();

        dispatchEvent(new Event("headerTextChanged"));
    }

    //----------------------------------
    //  headerWordWrap
    //----------------------------------

    /**
     *  @private
     *  Storage for the headerWordWrap property.
     */
    private var _headerWordWrap:*;

    [Inspectable(category="Advanced")]

    /**
     *  A flag that indicates whether text in the header will be
     *  word wrapped if it doesn't fit on one line.
     *  If <code>undefined</code>, the DataGrid control's <code>wordWrap</code> property 
     *  is used.
     *
     *  @default undefined
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get headerWordWrap():*
    {
        return _headerWordWrap;
    }

    /**
     *  @private
     */
    public function set headerWordWrap(value:*):void
    {
        _headerWordWrap = value;

        if (owner)
        {
            owner.invalidateList();
        }
    }

    //----------------------------------
    //  imeMode
    //----------------------------------

    /**
     *  @private
     *  Storage for the imeMode property.
     */
    private var _imeMode:String;

    [Inspectable(category="Other")]

    /**
     *  Specifies the IME (input method editor) mode. 
     *  The IME enables users to enter text in Chinese, Japanese, and Korean.  
     *  Flex sets the IME mode when the <code>itemFocusIn</code> event occurs, 
     *  and sets it back
     *  to the previous value when the <code>itemFocusOut</code> event occurs. 
     *  The flash.system.IMEConversionMode class defines constants for 
     *  the valid values for this property.  
     *
     *  <p>The default value is null, in which case it uses the value of the 
     *  DataGrid control's <code>imeMode</code> property.</p>
     *
     *  @see flash.system.IMEConversionMode
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get imeMode():String
    {
        return _imeMode;
    }

    /**
     *  @private
     */
    public function set imeMode(value:String):void
    {
        _imeMode = value;
    }

    //----------------------------------
    //  rendererIsEditor
    //----------------------------------

    [Inspectable(category="General", defaultValue="false")]

    /**
     *  A flag that indicates that the item renderer is also an item editor.
     *  If this property is <code>true</code>, Flex
     *  ignores the <code>itemEditor</code> property and uses the item
     *  renderer for that item as the editor.
     *
     *  @default false
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var rendererIsEditor:Boolean = false;

    //----------------------------------
    //  labelFunction
    //----------------------------------

    /**
     *  @private
     *  Storage for the labelFunction property.
     */
    private var _labelFunction:Function;

    [Bindable("labelFunctionChanged")]
    [Inspectable(category="Other")]

    /**
     *  A function that determines the text to display in this column.  By default
     *  the column displays the text for the field in the data that matches the
     *  column name.  However, sometimes you want to display text based on
     *  more than one field in the data, or display something that does not
     *  have the format that you want.
     *  In such a case you specify a callback function using <code>labelFunction</code>.
     *
     *  <p>For the DataGrid control, the method signature has the following form:</p>
     *
     *  <pre>labelFunction(item:Object, column:DataGridColumn):String</pre>
     *
     *  <p>Where <code>item</code> contains the DataGrid item object, and
     *  <code>column</code> specifies the DataGrid column.</p>
     *
     *  <p>A callback function might concatenate the firstName and
     *  lastName fields in the data, or do some custom formatting on a Date,
     *  or convert a number for the month into the string for the month.</p>
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get labelFunction():Function
    {
        return _labelFunction;
    }

    /**
     *  @private
     */
    public function set labelFunction(value:Function):void
    {
        _labelFunction = value;

        if (owner)
        {
            owner.invalidateList();
        }

        dispatchEvent(new Event("labelFunctionChanged"));
    }

    //----------------------------------
    //  minWidth
    //----------------------------------

    /**
     *  @private
     *  Storage for the minWidth property.
     */
    private var _minWidth:Number = 20;

    [Bindable("minWidthChanged")]
    [Inspectable(category="General", defaultValue="100")]

    /**
     *  The minimum width of the column.
     *  @default 20
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get minWidth():Number
    {
        return _minWidth;
    }

    /**
     *  @private
     */
    public function set minWidth(value:Number):void
    {
        _minWidth = value;

        if (owner)
        {
            owner.invalidateList();
        }

        if (_width < value)
            _width = value;

        dispatchEvent(new Event("minWidthChanged"));
    }

    //----------------------------------
    //  nullItemRenderer
    //----------------------------------

    /**
     *  @private
     *  Storage for the nullItemRenderer property.
     */
    private var _nullItemRenderer:IFactory;
    private var _contextNullItemRenderer:IFactory;

    [Bindable("nullItemRendererChanged")]
    [Inspectable(category="Other")]

    /**
     *  The class factory for item renderer instances that display the 
     *  data for each item in the column.
     *  You can specify a drop-in item renderer,
     *  an inline item renderer, or a custom item renderer component as the 
     *  value of this property.
     *
     *  <p>The default item renderer is the DataGridItemRenderer class,
     *  which displays the item data as text. </p>
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get nullItemRenderer():IFactory
    {
        return _nullItemRenderer;
    }

    /**
     *  @private
     */
    public function set nullItemRenderer(value:IFactory):void
    {
        _nullItemRenderer = value;

        // this is expensive... but unless set after init (not recommended), ok.
        if (owner)
        {
            owner.invalidateList();
            owner.columnRendererChanged(this);
            _contextNullItemRenderer = null;
        }

        dispatchEvent(new Event("nullItemRendererChanged"));
    }

    //----------------------------------
    //  resizable
    //----------------------------------

    [Inspectable(category="General")]

    /**
     *  A flag that indicates whether the user is allowed to resize
     *  the width of the column.
     *  If <code>true</code>, the user can drag the grid lines between 
     *  the column headers to resize
     *  the column. 
     *
     *  @default true
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var resizable:Boolean = true;

    //----------------------------------
    //  showDataTips
    //----------------------------------

    /**
     *  @private
     *  Storage for the showDataTips property.
     */
    private var _showDataTips:*;

    [Inspectable(category="Advanced")]

    /**
     *  A flag that indicates whether the datatips are shown in the column.
     *  If <code>true</code>, datatips are displayed for text in the rows. Datatips
     *  are tooltips designed to show the text that is too long for the row.
     *
     *  @default false
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get showDataTips():*
    {
        return _showDataTips;
    }

    /**
     *  @private
     */
    public function set showDataTips(value:*):void
    {
        _showDataTips = value;

        if (owner)
        {
            owner.invalidateList();
        }
    }

    //----------------------------------
    //  sortable
    //----------------------------------

    [Inspectable(category="General")]

    /**
     *  A flag that indicates whether the user can click on the
     *  header of this column to sort the data provider.
     *  If this property and the DataGrid <code>sortableColumns</code> property 
     *  are both <code>true</code>, the DataGrid control dispatches a 
     *  <code>headerRelease</code> event when a user releases the mouse button 
     *  on this column's header. 
     *  If no other handler calls the <code>preventDefault()</code> method on
     *  the <code>headerRelease</code> event, the <code>dataField</code>
     *  property or <code>sortCompareFunction</code> in the column is used 
     *  to reorder the items in the dataProvider.
     * 
     *  @default true
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var sortable:Boolean = true;

    //----------------------------------
    //  sortCompareFunction
    //----------------------------------

    /**
     *  @private
     *  Storage for the sortCompareFunction property.
     */
    private var _sortCompareFunction:Function;

    [Bindable("sortCompareFunctionChanged")]
    [Inspectable(category="Advanced")]

    /**
     *
     *  A callback function that gets called when sorting the data in
     *  the column.  If this property is not specified, the sort tries
     *  to use a basic string or number sort on the data.
     *  If the data is not a string or number or if the <code>dataField</code>
     *  property is not a valid property of the data provider, the sort does
     *  not work or will generate an exception.
     *  If you specify a value of the <code>labelFunction</code> property,
     *  you typically also provide a function to the <code>sortCompareFunction</code> property,
     *  unless sorting is not allowed on this column. 
     *  That means you specify a function when the value from the column's <code>dataField</code> 
     *  does not sort in the same way as the computed value from the <code>labelFunction</code> property.
     *
     *  <p>The DataGrid control uses this function to sort the elements of the data
     *  provider collection. The function signature of
     *  the callback function takes two parameters and have the following form:</p>
     *
     *  <pre>mySortCompareFunction(obj1:Object, obj2:Object):int </pre>
     *
     *  <p><code>obj1</code> &#x2014; A data element to compare.</p>
     * 
     *  <p><code>obj2</code> &#x2014; Another data element to compare with obj1.</p>
     * 
     *  <p>The function should return a value based on the comparison
     *  of the objects: </p>
     *  <ul>
     *    <li>-1 if obj1 should appear before obj2 in ascending order. </li>
     *    <li>0 if obj1 = obj2. </li>
     *    <li>1 if obj1 should appear after obj2 in ascending order.</li>
     *  </ul>
     * 
     *  <p><strong>Note:</strong> The <code>obj1</code> and
     *  <code>obj2</code> parameters are entire data provider elements and not
     *  just the data for the item.</p>
     *
     *  @default null
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get sortCompareFunction():Function
    {
        return _sortCompareFunction;
    }

    /**
     *  @private
     */
    public function set sortCompareFunction(value:Function):void
    {
        _sortCompareFunction = value;

        dispatchEvent(new Event("sortCompareFunctionChanged"));
    }

    //----------------------------------
    //  visible
    //----------------------------------

    /**
     *  @private
     *  Storage for the visible property.
     */
    private var _visible:Boolean = true;

    [Inspectable(category="General", defaultValue="true")]

    /**
     *  A flag that indicates whethe the column is visible.
     *  If <code>true</code>, the column is visible.
     *
     *  @default true
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get visible():Boolean
    {
        return _visible;
    }

    /**
     *  @private
     */
    public function set visible(value:Boolean):void
    {
        if (_visible != value)
        {
            _visible = value;

            if (value)
                newlyVisible = true;

            if (owner)
            {
                owner.columnsInvalid = true;

                owner.invalidateSize();
                owner.invalidateList();
            }
        }
    }

    mx_internal var newlyVisible:Boolean = false;

    //----------------------------------
    //  width
    //----------------------------------

    /**
     *  @private
     *  Storage for the width property.
     */
    private var _width:Number = 100;

    // preferred width is the number we should use when measuring
    // regular width will be changed if we shrink columns to fit.
    mx_internal var preferredWidth:Number = 100;

    [Bindable("widthChanged")]
    [Inspectable(category="General", defaultValue="100")]

    /**
     *  The width of the column, in pixels. 
     *  If the DataGrid's <code>horizontalScrollPolicy</code> property 
     *  is <code>false</code>, all visible columns must fit in the displayable 
     *  area, and the DataGrid will not always honor the width of
     *  the columns if the total width of the columns is too
     *  small or too large for the displayable area.
     *
     *  @default 100
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get width():Number
    {
        return _width;
    }

    /**
     *  @private
     */
    public function set width(value:Number):void
    {
        // remove any queued equal spacing commands
        explicitWidth = value;
        // use this value for future measurements
        preferredWidth = value;
        if (owner != null)
        {
            // if we aren't resizing as part of grid layout, resize it's column
            var oldVal:Boolean = resizable;
            // anchor this column to not accept any overflow width for accurate sizing
            resizable = false;
            owner.resizeColumn(colNum, value);
            resizable = oldVal;
        }
        else
        {
            // otherwise, just store the size
            _width = value;
        }
        dispatchEvent(new Event("widthChanged"));
    }

    /**
     *  @private
     *  Internal function to allow the DataGrid to set the width of the
     *  column without locking it as an explicitWidth
     */
    mx_internal function setWidth(value:Number):void
    {
         var oldValue:Number = _width;
        _width = value;
         if (oldValue != value)
             dispatchEvent(new Event("widthChanged"));
    }

    //----------------------------------
    //  wordWrap
    //----------------------------------

    /**
     *  @private
     *  Storage for the wordWrap property.
     */
    private var _wordWrap:*;

    [Inspectable(category="Advanced")]

    /**
     *  A flag that indicates whether the text in a row of this column
     *  is word wrapped if it doesn't fit on one line.
     *  If <code>undefined</code>, the DataGrid control's <code>wordWrap</code> property 
     *  is used.
     *
     *  <p>Only takes effect if the <code>DataGrid.variableRowHeight</code> property is also 
     *  <code>true</code>.</p>
     *
     *  @default undefined
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get wordWrap():*
    {
        return _wordWrap;
    }

    /**
     *  @private
     */
    public function set wordWrap(value:*):void
    {
        _wordWrap = value;

        if (owner)
        {
            owner.invalidateList();
        }
    }

    //--------------------------------------------------------------------------
    //
    //  Overridden methods
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     */
    override mx_internal function addStyleToProtoChain(
                                chain:Object, target:DisplayObject, filterMap:Object = null):Object
    {
        var parentGrid:DataGridBase = owner;
        var item:IListItemRenderer = IListItemRenderer(target);

        // If there is a DataGridColumn.styleName property,
        // add it to the head of the proto chain.
        // (The fact that styles can be set on both DataGridColumn
        // and DataGridColumn.styleName seems a bit redundant,
        // but both are supported for backward compatibility.)
        var styleName:Object = styleName;
        if (styleName)
        {
            if (styleName is String)
            {
                chain = addStylesToProtoChain(String(styleName), chain, target);
            }
            else if (styleName is CSSStyleDeclaration)
            {
                chain = styleName.addStyleToProtoChain(chain, target);
            }
        }

        chain = super.addStyleToProtoChain(chain, target);
        
        // If the target data is a DataGridColumn and has a data
        // field in its data, then it is a header so add the
        // DataGrid.headerStyleName object to the head of the proto chain.
        if (item.data && (item.data is DataGridColumn))
        {
            var s:Object;

            var headerStyleName:Object =
                parentGrid.getStyle("headerStyleName");
            if (headerStyleName)
            {
                if (headerStyleName is String)
                {
                    chain = addStylesToProtoChain(String(headerStyleName), chain, target);
                }
                else if (headerStyleName is CSSStyleDeclaration)
                {
                    chain = headerStyleName.addStyleToProtoChain(chain, target);
                }
            }

            headerStyleName = getStyle("headerStyleName");
            if (headerStyleName)
            {
                if (headerStyleName is String)
                {
                    chain = addStylesToProtoChain(String(headerStyleName), chain, target);
                }
                else if (headerStyleName is CSSStyleDeclaration)
                {
                    chain = headerStyleName.addStyleToProtoChain(chain, target);
                }
            }
        }

        return chain;
    }

    /**
     *  @private
     */
    override public function setStyle(styleProp:String, value:*):void
    {
     
        if (styleProp == "fontFamily" || styleProp == "fontWeight" || styleProp == "fontStyle")
        {
            if (owner)
            {
                owner.fontContextChanged = true;
                owner.invalidateProperties();
            }
        }

        var oldValue:Object = getStyle(styleProp);
        var regenerate:Boolean = false;

        // If this DataGridColumn didn't previously have a factory, defaultFactory, or
        // overrides object, then this DataGridColumn hasn't been added to the item
        // renderers proto chains.  In that case, we need to regenerate all the item
        // renderers proto chains.
        if (factory == null &&
            defaultFactory == null &&
            !overrides &&
            (oldValue !== value)) // must be !==
        {
            regenerate = true;
        }

        super.setLocalStyle(styleProp, value);

        // The default implementation of setStyle won't always regenerate
        // the proto chain when headerStyleName is set, and we need to make sure
        // that they are regenerated
        if (styleProp == "headerStyleName")
        {
            if (owner)
            {
                owner.regenerateStyleCache(true);
                owner.notifyStyleChangeInChildren("headerStyleName", true);
            }
            return;
        }

        if (owner)
        {
            if (regenerate)
            {
                owner.regenerateStyleCache(true);
            }
            
            owner.invalidateList();            
        }

    }

    //--------------------------------------------------------------------------
    //
    //  Methods
    //
    //--------------------------------------------------------------------------

    /**
     *  Returns the String that the item renderer displays for the given data object.
     *  If the DataGridColumn or its DataGrid control 
     *  has a non-null <code>labelFunction</code> 
     *  property, it applies the function to the data object. 
     *  Otherwise, the method extracts the contents of the field specified by the 
     *  <code>dataField</code> property, or gets the string value of the data object.
     *  If the method cannot convert the parameter to a String, it returns a
     *  single space.
     *
     *  @param data Object to be rendered.
     * 
     *  @return Displayable String based on the data.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function itemToLabel(data:Object):String
    {
        if (!data)
            return " ";

        if (labelFunction != null)
            return labelFunction(data, this);

        if (owner.labelFunction != null)
            return owner.labelFunction(data, this);

        if (typeof(data) == "object" || typeof(data) == "xml")
        {
            try
            {
                if ( !hasComplexFieldName ) 
                data = data[dataField];
                else 
                    data = deriveComplexColumnData( data );
            }
            catch(e:Error)
            {
                data = null;
            }
        }

        if (data is String)
            return String(data);

        try
        {
            return data.toString();
        }
        catch(e:Error)
        {
        }

        return " ";
    }

    /**
     *  Returns a String that the item renderer displays as the datatip for the given data object,
     *  based on the <code>dataTipField</code> and <code>dataTipFunction</code> properties.
     *  If the method cannot convert the parameter to a String, it returns a
     *  single space.
     * 
     *  <p>This method is for use by developers who are creating subclasses 
     *  of the DataGridColumn class.
     *  It is not for use by application developers.</p>
     *
     *  @param data Object to be rendered.
     *
     *  @return Displayable String based on the data.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function itemToDataTip(data:Object):String
    {
        if (dataTipFunction != null)
            return dataTipFunction(data);

        if (owner.dataTipFunction != null)
            return owner.dataTipFunction(data);

        if (typeof(data) == "object" || typeof(data) == "xml")
        {
            var field:String = dataTipField;
            if (!field)
                field = owner.dataTipField;
            try
            {
                if (data[field] != null)
                    data = data[field];
                else if (data[dataField] != null)
                    data = data[dataField];
            }
            catch(e:Error)
            {
                data = null;
            }
        }

        if (data is String)
            return String(data);

        try
        {
            return data.toString();
        }
        catch(e:Error)
        {
        }

        return " ";
    }

    /**
     * @private
     */
    protected function deriveComplexColumnData( data:Object ):Object 
    {
        var currentRef:Object = data;
        if ( complexFieldNameComponents ) 
        {
            for ( var i:int=0; i<complexFieldNameComponents.length; i++ )
                currentRef = currentRef[ complexFieldNameComponents[ i ] ];
        }
        
        return currentRef;
    }

    /**
     * @private
     */
    protected function complexColumnSortCompare( obj1:Object, obj2:Object ):int 
    {
        if ( !obj1 && !obj2 )
            return 0;
        
        if ( !obj1 )
            return 1;
        
        if ( !obj2 )
            return -1;
        
        var obj1Data:String = String(deriveComplexColumnData( obj1 ));
        var obj2Data:String = String(deriveComplexColumnData( obj2 ));
        
        if ( obj1Data < obj2Data )
            return -1;
        
        if ( obj1Data > obj2Data )
            return 1;
        
        return 0;
    }

    /**
     *  Return the appropriate factory, using the default factory if none specified.
     *
     *  @param forHeader <code>true</code> if this is a header renderer.
     *
     *  @param data The data to be presented by the item renderer.
     *
     *  @return if <code>data</code> is null, the default item renderer, 
     *  otherwis it returns the custom item renderer.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function getItemRendererFactory(forHeader:Boolean, data:Object):IFactory
    {
        if (forHeader)
        {
            if (!_contextHeaderRenderer)
                _contextHeaderRenderer = replaceItemRendererFactory(headerRenderer, true);
            return _contextHeaderRenderer;
        }

        if (!data)
        {
            if (!_contextNullItemRenderer)
                _contextNullItemRenderer = replaceItemRendererFactory(nullItemRenderer);
            return _contextNullItemRenderer;
        }

        if (!_contextItemRenderer)
            _contextItemRenderer = replaceItemRendererFactory(itemRenderer);
        return _contextItemRenderer;
    }

    /**
     * @private
     * 
     * This methods does two things:
     * 
     * 1. If the column uses styles that require an embedded font and the column has no renderer,
     *    then use the owner's item render, so we can replace it.
     * 2. If the column uses styles that require an embedded font, then replace
     *    the existing class factory with a ContextualClassFactory so the item can
     *    be created in the correct context.
     */
    private function replaceItemRendererFactory(rendererFactory:IFactory, forHeader:Boolean = false):IFactory
    {
        // No use of embedded font so just return
        if (oldEmbeddedFontContext == null)
            return rendererFactory;
        
        // Using an embedded font, but no local item renderer, so 
        // grab the owner's renderer and see if we can convert
        // it to a ContextualClassFactory.
        if (rendererFactory == null && owner != null)
            rendererFactory = owner.itemRenderer;
        
        if (rendererFactory is ClassFactory) {
            var contextualClassFactory: ContextualClassFactory = 
                new ContextualClassFactory(ClassFactory(rendererFactory).generator, 
                                           forHeader ? oldHeaderEmbeddedFontContext : oldEmbeddedFontContext);
            contextualClassFactory.properties = ClassFactory(rendererFactory).properties;
            return contextualClassFactory;
        }
        
        return rendererFactory;
    }
    
    mx_internal function getMeasuringRenderer(forHeader:Boolean, data:Object):IListItemRenderer
    {
        var factory:IFactory = getItemRendererFactory(forHeader, data);
        if (!factory)
            factory = owner.itemRenderer;

        if (!measuringObjects)
            measuringObjects = new Dictionary(false);

        var item:IListItemRenderer = measuringObjects[factory];
        if (!item)
        {
            item = factory.newInstance();           
            item.visible = false;
            item.styleName = this;
            measuringObjects[factory] = item;
        }

        return item;
    }

    /**
     * @private
     * 
     * Reset the factories so they get re-generated.
     */
    mx_internal function resetFactories():void
    {
        _contextHeaderRenderer = null;
        _contextItemRenderer = null;
        _contextNullItemRenderer = null;
        determineFontContext();
    }

    /**
     * @private
     * 
     * Save the current font context to member fields.
     */
    mx_internal function determineFontContext():void
    {
        var embeddedFontContext:IFlexModuleFactory;

        // Save for hasFontContextChanged()
        var fontName:String = StringUtil.trimArrayElements(getStyle("fontFamily"), ",");
        var fontWeight:String = getStyle("fontWeight");
        var fontStyle:String = getStyle("fontStyle");
        if (fontName == null)
            fontName = StringUtil.trimArrayElements(owner.getStyle("fontFamily"), ",");
        if (fontWeight == null)
            fontWeight = owner.getStyle("fontWeight");
        if (fontStyle == null)
            fontStyle = owner.getStyle("fontStyle");
        var bold:Boolean = fontWeight == "bold";
        var italic:Boolean = fontStyle == "italic";
                
        embeddedFontContext = (noEmbeddedFonts || !embeddedFontRegistry) ? 
            null : 
            embeddedFontRegistry.getAssociatedModuleFactory(
                fontName, bold, italic, this, owner.moduleFactory, 
                owner.systemManager);    

        if (embeddedFontContext != oldEmbeddedFontContext)
        {
            oldEmbeddedFontContext = embeddedFontContext;
            owner.invalidateList();
            owner.columnRendererChanged(this);
            _contextItemRenderer = null;
            _contextNullItemRenderer = null;
        }
            
        var headerStyleName:Object =
            owner.getStyle("headerStyleName");
        if (headerStyleName)
        {
            if (headerStyleName is String)
            {
                headerStyleName = owner.styleManager.getMergedStyleDeclaration(String(headerStyleName));
            }
        }
        if (headerStyleName)
        {
            var headerFontName:String = StringUtil.trimArrayElements(headerStyleName.getStyle("fontFamily"), ",");
            if (headerFontName)
                fontName = headerFontName;
            var headerFontWeight:String = headerStyleName.getStyle("fontWeight");
            if (headerFontWeight)
                fontWeight = headerFontWeight;
            var headerFontStyle:String = headerStyleName.getStyle("fontStyle");
            if (headerFontStyle)
                fontStyle = headerFontStyle;
            bold = fontWeight == "bold";
            italic = fontStyle == "italic";
        }

        headerStyleName = getStyle("headerStyleName");
        if (headerStyleName)
        {
            if (headerStyleName is String)
            {
                headerStyleName = owner.styleManager.getMergedStyleDeclaration(String(headerStyleName));
            }
        }

        if (headerStyleName)
        {
            headerFontName = StringUtil.trimArrayElements(headerStyleName.getStyle("fontFamily"), ",");
            if (headerFontName)
                fontName = headerFontName;
            headerFontWeight = headerStyleName.getStyle("fontWeight");
            if (headerFontWeight)
                fontWeight = headerFontWeight;
            headerFontStyle = headerStyleName.getStyle("fontStyle");
            if (headerFontStyle)
                fontStyle = headerFontStyle;
            bold = fontWeight == "bold";
            italic = fontStyle == "italic";
        }
        
        embeddedFontContext = (noEmbeddedFonts || !embeddedFontRegistry) ? 
            null : 
            embeddedFontRegistry.getAssociatedModuleFactory(
                fontName, bold, italic, this, owner.moduleFactory,
                owner.systemManager);    
        
        if (embeddedFontContext != oldHeaderEmbeddedFontContext)
        {
            oldHeaderEmbeddedFontContext = embeddedFontContext;
            cachedHeaderRenderer = null;
            owner.dataGridHeader.headerItemsChanged = true;
            _contextHeaderRenderer = null;
        }
    }
    
    /**
     *  @private
     */
    private function addStylesToProtoChain(styles:String, chain:Object, target:DisplayObject):Object
    {
        var styleNames:Array = styles.split(/\s+/);
        for (var c:int=0; c < styleNames.length; c++)
        {
            if (styleNames[c].length) 
            {
                var declaration:CSSStyleDeclaration = 
                    owner.styleManager.getMergedStyleDeclaration("." + styleNames[c]);
                    
                if (declaration)
                    chain = declaration.addStyleToProtoChain(chain, target);
            }
        }
        return chain;
    }
    
    /**
     *  @private
     *  A hash table of objects used to calculate sizes
     */
    mx_internal var measuringObjects:Dictionary;

    /**
     *  A map of free item renderers by factory.
     *  This property is a Dictionary indexed by factories
     *  where the values are Dictionaries of itemRenderers
     *
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    mx_internal var freeItemRenderersByFactory:Dictionary;

}

}