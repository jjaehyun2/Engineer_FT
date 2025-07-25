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

package mx.collections
{
import org.apache.royale.events.Event;
import org.apache.royale.utils.Timer;

/* 
import flash.events.TimerEvent;
import flash.utils.Dictionary;
import flash.utils.Timer;
import flash.xml.XMLNode;
 */
//import mx.collections.errors.ItemPendingError;
import mx.core.mx_internal;
import mx.events.CollectionEvent;
import mx.events.CollectionEventKind;
import mx.utils.UIDUtil;

use namespace mx_internal;

//--------------------------------------
//  Other metadata
//--------------------------------------

[DefaultProperty("grouping")]

/**
 *  The GroupingCollection2 class lets you create grouped data from flat data 
 *  for display in the AdvancedDataGrid control.
 *  When you create the instance of the GroupingCollection2 from your flat data, 
 *  you specify the field or fields of the data used to create the hierarchy.
 *
 *  <p><b>Note: </b>In the previous release of Flex, you used the GroupingCollection class 
 *  with the AdvancedDataGrid control. 
 *  The GroupingCollection2 class is new for Flex 4 and provides better performance 
 *  than GroupingCollection.</p>
 *
 *  <p>To populate the AdvancedDataGrid control with grouped data, 
 *  you create an instance of the GroupingCollection2 class from your flat data, 
 *  and then pass that GroupingCollection2 instance to the data provider 
 *  of the AdvancedDataGrid control. 
 *  To specify the grouping fields of your flat data, 
 *  you pass a Grouping instance to 
 *  the <code>GroupingCollection2.grouping</code> property. 
 *  The Grouping instance contains an Array of GroupingField instances, 
 *  one per grouping field. </p>
 *
 *  <p>The following example uses the GroupingCollection2 class to define
 *  two grouping fields: Region and Territory.</p>
 *
 *  <pre>
 *  &lt;mx:AdvancedDataGrid id=&quot;myADG&quot;    
 *    &lt;mx:dataProvider&gt; 
 *      &lt;mx:GroupingCollection2 id=&quot;gc&quot; source=&quot;{dpFlat}&quot;&gt; 
 *        &lt;mx:grouping&gt; 
 *          &lt;mx:Grouping&gt; 
 *            &lt;mx:GroupingField name=&quot;Region&quot;/&gt; 
 *            &lt;mx:GroupingField name=&quot;Territory&quot;/&gt; 
 *          &lt;/mx:Grouping&gt; 
 *        &lt;/mx:grouping&gt; 
 *      &lt;/mx:GroupingCollection2&gt; 
 *    &lt;/mx:dataProvider&gt;  
 *     
 *    &lt;mx:columns&gt; 
 *      &lt;mx:AdvancedDataGridColumn dataField=&quot;Region&quot;/&gt; 
 *      &lt;mx:AdvancedDataGridColumn dataField=&quot;Territory&quot;/&gt; 
 *      &lt;mx:AdvancedDataGridColumn dataField=&quot;Territory_Rep&quot;/&gt; 
 *      &lt;mx:AdvancedDataGridColumn dataField=&quot;Actual&quot;/&gt; 
 *      &lt;mx:AdvancedDataGridColumn dataField=&quot;Estimate&quot;/&gt; 
 *    &lt;/mx:columns&gt; 
 *  &lt;/mx:AdvancedDataGrid&gt;
 *  </pre>
 *
 *  @mxml
 *
 *  The <code>&lt;mx.GroupingCollection2&gt;</code> inherits all the tag attributes of its superclass, 
 *  and defines the following tag attributes:</p>
 *
 *  <pre>
 *  &lt;mx:GroupingCollection2
 *  <b>Properties </b>
 *    grouping="<i>No default</i>"
 *    source="<i>No default</i>"
 *    summaries="<i>No default</i>"
 *  /&gt;
 *  </pre>
 *
 *  @see mx.controls.AdvancedDataGrid
 *  @see mx.collections.Grouping
 *  @see mx.collections.GroupingField
 *  
 *  @langversion 3.0
 *  @playerversion Flash 10
 *  @playerversion AIR 1.5
 *  @productversion Flex 4
 *  @royalesuppresspublicvarwarning
 */
public class GroupingCollection2 extends HierarchicalData implements IGroupingCollection2
{


    //include "../core/Version.as";
    
    //--------------------------------------------------------------------------
    //
    //  Constructor
    //
    //--------------------------------------------------------------------------

    /**
     *  Constructor.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 10
     *  @playerversion AIR 1.5
     *  @productversion Royale 0.9.3
     */
    public function GroupingCollection2()
    {
        super();
        
        newCollection = new ArrayCollection();
        super.source = newCollection;
        
        /*
        objectSummaryMap = new Dictionary(false);
        */
        objectSummaryMap = {};
        
        parentMap = {};
    }
    
    //--------------------------------------------------------------------------
    //
    //  Variables
    //
    //--------------------------------------------------------------------------
    
    /**
     *  @private
     *  
     *  denotes if the refresh is asynchronous.
     */
    private var async:Boolean = false;
    
    /**
     *  @private
     *  
     *  if true, dispatch collection change events 
     */
    private var dispatchCollectionEvents:Boolean = false;
    
    /**
     *  @private
     */
    private var newCollection:ArrayCollection;
    
    /**
     *  @private
     */
    private var _sourceCol:ICollectionView;
    
    /**
     *  @private
     *  
     *  the object summary map.
     *  keeps summaries corresponding to different objects
     */
   // private var objectSummaryMap:Dictionary;
    private var objectSummaryMap:Object;
    
    /**
     *  @private
     *  
     *  the original sort applied to the source collection 
     */
    private var oldSort:Sort;
    
    /**
     *  @private
     */
    private var prepared:Boolean = false;
    
    /**
     *  @private
     */
    private var flatView:ICollectionView;
    
    /**
     *  @private
     */
    private var flatCursor:IViewCursor;
    
    /**
     *  @private
     */
    private var hView:ICollectionView;
    
    /**
     *  @private
     */
    private var currentPosition:CursorBookmark = CursorBookmark.FIRST;
    
    /**
     *  @private
     */
    private var gf:Array;
    
    /**
     *  @private
     */
    private var fieldCount:int;
    
    /**
     *  @private
     *  
     *  contains current data being compared
     */
    private var currentData:Object;
    
    /**
     *  @private
     *  
     *  contains current group objects for different group fields
     */
    private var currentGroups:Array;
    
    /**
     *  @private
     *  
     *  contains current group labels for different group fields
     */
    private var currentGroupLabels:Array;
    
    /**
     *  @private
     *  
     *  contains next index for different group fields
     */
    private var currentIndices:Array;
    
    /**
     *  @private
     *  
     *  item index
     */
    private var itemIndex:int;
    
    /**
     *  @private
     *  
     *  the children array for the group
     */
    private var childrenArray:Array;
    
    /**
     *  @private
     */
    private var summaryPresent:Boolean;
    
    /**
     *  The timer which is associated with an asynchronous refresh operation.
     *  You can use it to change the timing interval, pause the refresh, 
     *  or perform other actions.
     *  
     *  The default value for the <code>delay</code> property of the 
     *  Timer instance is 1, corresponding to 1 millisecond.
     *
     *  
     *  @langversion 3.0
     *  @playerversion Flash 10
     *  @playerversion AIR 1.5
     *  @productversion Royale 0.9.3
     */
    protected var timer:Timer;
    
    /**
     *  @private
     *  Mapping of UID to parents.  Must be maintained as things get removed/added
     *  This map is created as objects are visited
     */
    protected var parentMap:Object;
    
    /**
     *  @private
     *  A Dictionary to maintain summaries
     */
    //private var summariesTracker:Dictionary;
    private var summariesTracker:Object;
    
    /**
     *  @private
     *  An array to store all the summary fields.
     */
    private var summaryFields:Array;
    
    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------   
    
    //----------------------------------
    // grouping
    //----------------------------------
    
    private var _grouping:Grouping;
    
    /**
     *  Specifies the Grouping instance applied to the source data. 
     *  Setting the <code>grouping</code> property  
     *  does not automatically refresh the view,
     *  so you must call the <code>refresh()</code> method
     *  after setting this property.
     *
     *  @see mx.collections.GroupingCollection2#refresh()
     *  
     *  @langversion 3.0
     *  @playerversion Flash 10
     *  @playerversion AIR 1.5
     *  @productversion Royale 0.9.3
     */
    public function get grouping():Grouping
    {
        return _grouping;
    }
       
    /**
     *  @private
     */
    public function set grouping(value:Grouping):void
    {
        _grouping = value;
    }
    
    //----------------------------------
    // summaries
    //----------------------------------
    
    /**
     *  Array of SummaryRow instances that define any root-level data summaries.
     *  Specify one or more SummaryRow instances to define the data summaries, 
     *  as the following example shows:
     *
     *  <pre>
     *  &lt;mx:AdvancedDataGrid id="myADG" 
     *     width="100%" height="100%" 
     *     initialize="gc.refresh();"&gt;        
     *     &lt;mx:dataProvider&gt;
     *         &lt;mx:GroupingCollection2 id="gc" source="{dpFlat}"&gt;
     *             &lt;mx:summaries&gt;
     *                 &lt;mx:SummaryRow summaryPlacement="last"&gt;
     *                     &lt;mx:fields&gt;
     *                         &lt;mx:SummaryField2 dataField="Actual" 
     *                             label="Min Actual" summaryOperation="MIN"/&gt;
     *                         &lt;mx:SummaryField2 dataField="Actual" 
     *                             label="Max Actual" summaryOperation="MAX"/&gt;
     *                     &lt;/mx:fields&gt;
     *                   &lt;/mx:SummaryRow&gt;
     *                 &lt;/mx:summaries&gt;
     *             &lt;mx:Grouping&gt;
     *                 &lt;mx:GroupingField name="Region"/&gt;
     *                 &lt;mx:GroupingField name="Territory"/&gt;
     *             &lt;/mx:Grouping&gt;
     *         &lt;/mx:GroupingCollection2&gt;
     *     &lt;/mx:dataProvider&gt;        
     *     
     *     &lt;mx:columns&gt;
     *         &lt;mx:AdvancedDataGridColumn dataField="Region"/&gt;
     *         &lt;mx:AdvancedDataGridColumn dataField="Territory_Rep"
     *             headerText="Territory Rep"/&gt;
     *         &lt;mx:AdvancedDataGridColumn dataField="Actual"/&gt;
     *         &lt;mx:AdvancedDataGridColumn dataField="Estimate"/&gt;
     *         &lt;mx:AdvancedDataGridColumn dataField="Min Actual"/&gt;
     *         &lt;mx:AdvancedDataGridColumn dataField="Max Actual"/&gt;
     *     &lt;/mx:columns&gt;
     *  &lt;/mx:AdvancedDataGrid&gt;</pre>
     *
     *  @see mx.collections.SummaryRow
     *  @see mx.collections.SummaryField2
     *  
     *  @langversion 3.0
     *  @playerversion Flash 10
     *  @playerversion AIR 1.5
     *  @productversion Royale 0.9.3
     */
    public var summaries:Array; 

    //--------------------------------------------------------------------------
    //
    //  Overriden Methods
    //
    //--------------------------------------------------------------------------
    
    /**
     *  The source collection containing the flat data to be grouped.
     *  
     *  If the source is not a collection, it will be auto-wrapped into a collection.
     *  
     *  
     *  @langversion 3.0
     *  @playerversion Flash 10
     *  @playerversion AIR 1.5
     *  @productversion Royale 0.9.3
     */
    override public function get source():Object
    {
        return _sourceCol;
    }
    
    override public function set source(value:Object):void
    {
        if (_sourceCol)
            _sourceCol.removeEventListener(CollectionEvent.COLLECTION_CHANGE, collectionChangeHandler);
        
        if (!value)
        {
            _sourceCol = null;
            return;
        }
            
        _sourceCol = getCollection(value);
        
        if(_sourceCol is ICollectionView)
            _sourceCol.addEventListener(CollectionEvent.COLLECTION_CHANGE, collectionChangeHandler);
    }
    
    /**
     * @private
     */ 
    override public function getChildren(node:Object):Object
    {
        var children:Object = super.getChildren(node);
        
        // populate the parentMap
        // parentMap will be populated only if the children is ICollectionView
        var uid:String;
        if (children != null)
        {
            if (children is ICollectionView)
            {
                var cursor:IViewCursor = ICollectionView(children).createCursor();
                while (!cursor.afterLast)
                {                
                    uid = UIDUtil.getUID(cursor.current);
                    parentMap[uid] = node;
                    cursor.moveNext();
                }
            }
            else
            {
                //if the children is not ICollectionView then
                //it was not introduced by GC. (this happens in the case of XML.) 
                return null;
            }
        }
        
        return children;
    }
    
    /**
     *  Return <code>super.source</code>, if the <code>grouping</code> property is set, 
     *  and an ICollectionView instance that refers to <code>super.source</code> if not.
     *  
     *  @return The object to return.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 10
     *  @playerversion AIR 1.5
     *  @productversion Royale 0.9.3
     */
    override public function getRoot():Object
    {
        return super.source;
    }
    
    //--------------------------------------------------------------------------
    //
    //  Methods
    //
    //--------------------------------------------------------------------------
    
    /**
     *  @inheritDoc
     *  
     *  @langversion 3.0
     *  @playerversion Flash 10
     *  @playerversion AIR 1.5
     *  @productversion Royale 0.9.3
     */
    public function refresh(async:Boolean = false, dispatchCollectionEvents:Boolean = false):Boolean
    {
        if (!async && _sourceCol == null)
            async = true;
        this.async = async;
        this.dispatchCollectionEvents = async ? true : dispatchCollectionEvents;
        
        var resetEvent:CollectionEvent;
        
        // return if no grouping or groupingFields are supplied
        if (!grouping || grouping.fields.length < 1 )
        {
            super.source = source;
            // dispatch collection change event of kind reset.
            resetEvent =
                    new CollectionEvent(CollectionEvent.COLLECTION_CHANGE);
            resetEvent.kind = CollectionEventKind.RESET;
            dispatchEvent(resetEvent);
            return true;
        }
        
        super.source = newCollection;
		
		// remove the items from the source collection if there are any.
		newCollection.removeAll();
		
        
        // dispatch collection change event of kind reset.
        resetEvent =
                new CollectionEvent(CollectionEvent.COLLECTION_CHANGE);
        resetEvent.kind = CollectionEventKind.RESET;
        dispatchEvent(resetEvent);
        
        // reset the parent map
        parentMap = {};
        
        // reset the object summary map
        //objectSummaryMap = new Dictionary(false);
        objectSummaryMap = {};
        
        // reset the summaryTracker
        summariesTracker = null;
        
        // check if any summary is specified
        summaryPresent = false;
        prepareSummaryFields();
        
        var grouped:Boolean;
        if(source && grouping)
        {
            grouped = makeGroupedCollection();
        }
        else if (async)
        {
            timer = new Timer(1);
            timer.addEventListener(Timer.TIMER, timerHandler);
            timer.start();
        }

       
        return grouped; 
    }
    
    /**
     *  @inheritDoc
     *  
     *  @langversion 3.0
     *  @playerversion Flash 10
     *  @playerversion AIR 1.5
     *  @productversion Royale 0.9.3
     */
    public function cancelRefresh():void
    {
        /*
        if (timer)
        {
            timer.stop();
            timer = null;
            cleanUp();
        }
        */
    }
    
    /**
     *  @private
     *  
     *  check for the existing groups if they can accomodate the item
     *  otherwise create new group and place the item.
     */  
    private function addItem(node:Object, depth:int = 0):void
    {   
        var coll:ICollectionView = super.source as ICollectionView;
        var parent:Object = null;
        var i:int = 0;
        while (i < grouping.fields.length)
        {
            // check for the parent item
            var obj:Object = checkForParentExistence(coll, node, i);
            // if no parent, then use the previous parent
            if (!obj)
                break;
            // change the parent to point to its parent and start looking for parent again
            parent = obj;
            
            if (parent)
            {
                coll = getChildren(parent) as ICollectionView;
                i++;
            }       
        }
        
        // parent found
        if (parent)
        {
            coll = getChildren(parent) as ICollectionView;
            
            // create groups for the item as no existing group matched with the item
            if (i <= grouping.fields.length-1)
            {
                // create groups and place item
                createGroupsAndInsertItem(coll, node, i);
                // update the summary for the parents
                updateSummary(node);
                return;
            }
            // if there already exist a group for the item and insert the item in that group
            if (coll is IList)
            {
                // insert the item
                IList(coll).addItem(node);
                // update the parent map
                updateParentMap(parent, node);
                // update the summary for the parents
                updateSummary(node);
            }
        }
        else
        {
            // no groups for the item, create groups and add item to them
            createGroupsAndInsertItem(super.source as ICollectionView, node);
            // update the summary for the parents
            updateSummary(node);
        }
        
    }
    
    /**
     *  @private
     *  
     *  check for existence of the groups for an item in the collection
     *  and return all the parent of that item.
     */  
    private function checkForParentExistence(coll:ICollectionView, node:Object, depth:int):Object
    {
        var cursor:IViewCursor = coll.createCursor();
        
        var label:String = getDataLabel(node, grouping.fields[depth]);
        
        while (!cursor.afterLast)
        {
            var current:Object = cursor.current;
            // check for matching fields
            if (current.hasOwnProperty(grouping.label) && 
                current[grouping.label] == label)
            {
                return current;
            }
            cursor.moveNext();
        }
        
        return null;
    }
    
    /**
     *  @private
     *  
     *  creating the group for the item in the collection
     *  and placing it there.
     */  
    private function createGroupsAndInsertItem(coll:ICollectionView, node:Object, depth:int = 0):void
    {
        var parent:Object;
        var n:int = grouping.fields.length;
        for (var i:int = depth; i < n ; i++)
        {
            // get the dataField and value
            var dataField:String = grouping.fields[i].name;
            var value:String = getDataLabel(node, grouping.fields[i]);
            
            if (!value)
                return;
                
            // create a new group
            var obj:Object;
            if (grouping.fields[i].groupingObjectFunction != null)
                obj = grouping.fields[i].groupingObjectFunction(value);
            else if (grouping.groupingObjectFunction != null)
                obj = grouping.groupingObjectFunction(value);
            else
                obj = {};
            
            obj[childrenField] = new ArrayCollection();
            
            obj[grouping.label] = value;
            
            if (coll is IList)
            {
                IList(coll).addItem(obj);
                
                // get the parent and update parent map
                parent = parent != null ? parent : getParent(coll.createCursor().current);
                updateParentMap(parent, obj);
                
                coll = getChildren(obj) as ICollectionView;
                parent = obj;
                // if we reach the end of the fields, just insert the item in the collection
                if (i == n - 1)
                {
                    IList(coll).addItem(node);
                    // update the parent map
                    updateParentMap(obj, node);
                    break;
                }
            }
        }
    }
    
    /**
     * @private
     * 
     * returns the collection view of the given object
     */ 
    private function getCollection(value:Object):ICollectionView
    {
        // handle strings and xml
        if (typeof(value)=="string")
            value = new XML(value);
        /*
        else if (value is XMLNode)
            value = new XML(XMLNode(value).toString());
        */
        else if (value is XMLList)
            value = new XMLListCollection(value as XMLList);
        
        if (value is XML)
        {
            var xl:XMLList = new XMLList();
            xl += value;
            return new XMLListCollection(xl);
        }
        //if already a collection dont make new one
        else if (value is ICollectionView)
        {
            return ICollectionView(value);
        }
        else if (value is Array)
        {
            return new ArrayCollection(value as Array);
        }
        //all other types get wrapped in an ArrayCollection
        else if (value is Object)
        {         
            // convert to an array containing this one item
            var tmp:Array = [];
            tmp.push(value);
            return new ArrayCollection(tmp);
        }
        else
        {
            return new ArrayCollection();
        }
    }
    
    /**
     *  @private
     *  get the data label from user specified function.
     *  otherwise get the label from the data.
     */ 
    private function getDataLabel(data:Object,field:GroupingField):String
    {
        if (field.groupingFunction != null)
            return field.groupingFunction(data, field);
        
        // should we create a defaultGroupLabelValue property
        return data.hasOwnProperty(field.name) ? data[field.name] : "Not Available";
    }
    
    /**
     *  Returns the parent of a node.  
     *  The parent of a top-level node is <code>null</code>.
     *
     *  @param node The Object that defines the node.
     *
     *  @return The parent node containing the node as child, 
     *  <code>null</code> for a top-level node,  
     *  and <code>undefined</code> if the parent cannot be determined.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 10
     *  @playerversion AIR 1.5
     *  @productversion Royale 0.9.3
     */
    protected function getParent(node:Object):*
    {
        var uid:String = UIDUtil.getUID(node);
        if (parentMap.hasOwnProperty(uid))
            return parentMap[uid];
            
        return undefined;
    }
    
    /**
     *  @private
     *  Generate the root level summaries
     */
    private function generateRootSummaries(flatData:Boolean = false):void
    {
        var coll:ICollectionView = super.source as ICollectionView;
        
        getSummaries(coll, -1);
    }
    
    /**
     *  @private
     *  Calculate summaries for a node.
     */
    private function getSummariesForRow(node:Object, collection:ICollectionView, depth:int):void
    {
        // calculate the summary at the last level
        var hd:HierarchicalData = new HierarchicalData(collection);
        hd.childrenField = this.childrenField;
        var hColl:ICollectionView = new HierarchicalCollectionView(hd, {});
        var hCursor:IViewCursor = new LeafNodeCursor(HierarchicalCollectionView(hColl), hColl, hd);
        
        // for all summary fields
        var m:int = summaryFields.length;
        var i:int = 0;
        
        var defaultSummaryCalculator:DefaultSummaryCalculator = new DefaultSummaryCalculator();
        //var summaryMap:Dictionary = new Dictionary(false);
        var summaryMap:Object = {};
        var summaryField:SummaryField2;
        var summaryCalculator:ISummaryCalculator;
        
        for (i = 0; i < m; i++)
        {
            summaryField = summaryFields[i];
            
            if (!(summaryField.summaryOperation is String) &&
                summaryField.summaryOperation is ISummaryCalculator)
                summaryCalculator = ISummaryCalculator(summaryField.summaryOperation);
            else
                summaryCalculator = defaultSummaryCalculator;
            
            summaryMap[summaryField] = summaryCalculator.summaryCalculationBegin(summaryField);
        }
        
        while (!hCursor.afterLast)
        {
            for (i = 0; i < m; i++)
            {
                summaryField = summaryFields[i];
                
                if (!(summaryField.summaryOperation is String) &&
                    summaryField.summaryOperation is ISummaryCalculator)
                    summaryCalculator = ISummaryCalculator(summaryField.summaryOperation);
                else
                    summaryCalculator = defaultSummaryCalculator;
                
                summaryCalculator.calculateSummary(summaryMap[summaryField], summaryField, hCursor.current);
            }
            
            hCursor.moveNext();
        }
        
        for (i = 0; i < m; i++)
        {
            var summary:Number = 0.0;
            summaryField = summaryFields[i];
            
            if (!(summaryField.summaryOperation is String) &&
                summaryField.summaryOperation is ISummaryCalculator)
                summaryCalculator = ISummaryCalculator(summaryField.summaryOperation);
            else
                summaryCalculator = defaultSummaryCalculator;
            
            summary = summaryCalculator.returnSummary(summaryMap[summaryField], summaryField);
            
            populateSummary(node, summaryField, summaryMap[summaryField], summary);
        }
    }
    
    /**
     *  @private
     *  Store the summary in a dictionary for later use.
     */
    private function populateSummary(node:Object, summaryField:SummaryField2, summaryObject:Object, summary:Number):void
    {
        var op:String = summaryField.summaryOperation.toString();
        
        if (summariesTracker == null)
            summariesTracker = {}; // new Dictionary(false);
        
        if (summariesTracker[UIDUtil.getUID(node)] == undefined)
            summariesTracker[UIDUtil.getUID(node)] = {}; // new Dictionary(false);
        if (summariesTracker[UIDUtil.getUID(node)][op] == undefined)
            summariesTracker[UIDUtil.getUID(node)][op] = {}; // new Dictionary(false);
        if (summariesTracker[UIDUtil.getUID(node)][op][summaryField.dataField] == undefined)
            summariesTracker[UIDUtil.getUID(node)][op][summaryField.dataField] = {}; // new Dictionary(false);
        
        summariesTracker[UIDUtil.getUID(node)][op][summaryField.dataField] = {summaryObject:summaryObject, value:summary};
    }
    
    /**
     *  @private
     *  Get the summary from the dictionary 
     */
    private function getSummary(node:Object, summaryField:SummaryField2):Object
    {
        var op:String = summaryField.summaryOperation.toString();
        
        if (summariesTracker == null || 
            summariesTracker[UIDUtil.getUID(node)] == undefined ||
            summariesTracker[UIDUtil.getUID(node)][op] == undefined ||
            summariesTracker[UIDUtil.getUID(node)][op][summaryField.dataField] == undefined)
        return null;
        
        return summariesTracker[UIDUtil.getUID(node)][op][summaryField.dataField];
    }
    
    /**
     *  @private
     *  Calcualte and insert summary for a node
     */
    private function getSummaries(node:Object, depth:int):void
    {
        if (depth > grouping.fields.length - 1)
            return;
        
        var children:ICollectionView = this.getChildren(node) as ArrayCollection;
        
        if (node == super.source)
            children = node as ICollectionView;
        
        if (!children || children.length == 0)
            return;
        
        if (depth == grouping.fields.length - 1)
        {
            // calculate actual summaries here
            getSummariesForRow(node, children, depth);
        }
        else
        {
            var cursor:IViewCursor = children.createCursor();
            var isFirst:Boolean = true;
            
            var defaultSummaryCalculator:DefaultSummaryCalculator = new DefaultSummaryCalculator();
            var summaryField:SummaryField2;
            var summaryMap:Object = {} // Dictionary = new Dictionary(false);
            var summaryCalculator:ISummaryCalculator;
            
            while (!cursor.afterLast)
            {
                var current:Object = cursor.current;
                if (!(current is SummaryObject))
                {
                    // for all summary fields
                    var m:int = summaryFields.length;
                    var i:int = 0;
                    
                    for (i = 0; i < m; i++)
                    {
                        summaryField = summaryFields[i];
                        
                        if (!(summaryField.summaryOperation is String) &&
                            summaryField.summaryOperation is ISummaryCalculator)
                            summaryCalculator = ISummaryCalculator(summaryField.summaryOperation);
                        else
                            summaryCalculator = defaultSummaryCalculator;
                        
                        var summaryObject:Object = getSummary(current, summaryField);
                        
                        if (isFirst)
                        {
                            summaryMap[summaryField] = summaryCalculator.summaryOfSummaryCalculationBegin(summaryObject["summaryObject"], summaryField);
                        }
                        else
                        {
                            summaryCalculator.calculateSummaryOfSummary(summaryMap[summaryField], summaryObject["summaryObject"], summaryField);
                        }
                    }
                }
                
                isFirst = false;
                cursor.moveNext();
            }
            
            // check if there were some items
            if (!isFirst)
            {
                for (i = 0; i < m; i++)
                {
                    summaryField = summaryFields[i];
                    
                    if (!(summaryField.summaryOperation is String) &&
                        summaryField.summaryOperation is ISummaryCalculator)
                        summaryCalculator = ISummaryCalculator(summaryField.summaryOperation);
                    else
                        summaryCalculator = defaultSummaryCalculator;
                    
                    var summary:Number = summaryCalculator.returnSummaryOfSummary(summaryMap[summaryField], summaryField);
                    
                    populateSummary(node, summaryField, summaryMap[summaryField], summary);
                }
            }
        }
        
        if (depth == -1)
            insertSummaries(super.source as ICollectionView, -1, true);
        else
            insertSummaries(node, depth);
    }
    
    private function insertSummaries(node:Object, depth:int, rootSummary:Boolean = false):void
    {
        var summaries:Array = this.summaries;
        
        if (!rootSummary)
            summaries = grouping.fields[depth].summaries;
        
        if (!summaries)
            return;
        
        var summaryObj:Array = [];
        
        var n:int = summaries.length;
        for (var i:int = 0; i < n; i++)
        {
            var summaryRow:SummaryRow = summaries[i];
            summaryObj[i] = 
                summaryRow.summaryObjectFunction != null ? 
                summaryRow.summaryObjectFunction() : new SummaryObject();
            
            // for all summary fields
            var m:int = summaryRow.fields.length;
            for (var j:int = 0; j < m; j++)
            {
                var summaryField:SummaryField2 = summaryRow.fields[j];
                var summary:Number = 0.0;
                var label:String = summaryField.label ? summaryField.label : summaryField.dataField;
                
                var summaryObject:Object = getSummary(node, summaryField);
                
                if (summaryObject != null)
                {
                    summary = summaryObject["value"];
                    // populate the summary object
                    summaryObj[i][label] = summary;
                }
            }
            // populate the object summary map
            if (objectSummaryMap[UIDUtil.getUID(node)] == undefined)
                objectSummaryMap[UIDUtil.getUID(node)] = [];
            
            objectSummaryMap[UIDUtil.getUID(node)].push(summaryObj[i]);
        }
        
        // insert the summary
        if (rootSummary)
            insertRootSummary(summaryObj);
        else
            insertSummary(node, summaryObj, summaries);
        
    }
    
    /**
     *  @private
     * 
     *  initialize the variables
     * 
     */
    private function initialize():void
    {
        currentData = null;
        currentGroups = [];
    
        currentGroupLabels = [];
        currentIndices = [] ;
        
        childrenArray = null;
    }
    
    /**
     *  @private
     * 
     *  insert the root summaries
     * 
     */  
    private function insertRootSummary(summaryObj:Array):void
    {
        var coll:ICollectionView = super.source as ICollectionView;
        
        if (!(coll is IList))
            return;
        
        var n:int = summaryObj.length;
        for (var i:int = 0; i < n; i++)
        {
            var summaryRow:SummaryRow = summaries[i];
            
            if (summaryRow.summaryPlacement.indexOf("first") != -1)
            {
                IList(coll).addItemAt(summaryObj[i], 0);
            }
            
            if (summaryRow.summaryPlacement.indexOf("last") != -1)
            {
                IList(coll).addItem(summaryObj[i]);
            }
        }
    }
    
    /**
     *  @private
     *  
     *  inserts the summaries in the children collection of the parent node
     */  
    private function insertSummary(parent:Object, summaryObj:Array, summaries:Array):void
    {
        var n:int = summaries.length;
        for (var i:int = 0; i < n; i++)
        {
            var summaryRow:SummaryRow = summaries[i];
            if (summaryRow.summaryPlacement.indexOf("group") != -1)
            {
                for (var p:String in summaryObj[i])
                    parent[p] = summaryObj[i][p];
            }
            
            var children:IList;
            if (summaryRow.summaryPlacement.indexOf("first") != -1)
            {
                children = (getChildren(parent) as ArrayCollection);
                if (children)
                    children.addItemAt(summaryObj[i], 0);
            }
            
            if (summaryRow.summaryPlacement.indexOf("last") != -1)
            {
                children = (getChildren(parent) as ArrayCollection);
                if (children)
                    children.addItem(summaryObj[i]);
            }
        }
    }
    
    /**
     *  @private
     */
    private function makeGroupedCollection():Boolean
    {
        // save the sorting information of the source collection
        // sort the source collection and create a grouped collection
        // restore the sort of the original source collection
        
        var fields:Array = [];
        var n:int = grouping.fields.length;
        for (var i:int = 0; i < n; i++)
        {
            var groupingField:GroupingField = grouping.fields[i];
            var sortField:SortField = new SortField(groupingField.name, 
                        groupingField.caseInsensitive, 
                        groupingField.descending, groupingField.numeric);
            sortField.compareFunction = groupingField.compareFunction;
            fields.push(sortField);
        }
        
        oldSort = source.sort;
        source.sort = new Sort();
        
        // Set the compare function
        if (grouping.compareFunction != null)
            source.sort.compareFunction = grouping.compareFunction;
        
        source.sort.fields = fields;
        
        var refreshed:Boolean = source.refresh();
        if (!refreshed)
            return refreshed;
        
        if (async)
        {
            timer = new Timer(1);
            timer.addEventListener(Timer.TIMER, timerHandler);
            timer.start();
        }
        else
        {
            return buildGroups();
        }
        return true;
    }
    
    /**
     *  @private
     */
    private function timerHandler(event:Event):void
    {
        if (buildGroups())
        {
            timer.stop();
            timer = null;
        }
        
    }
    
    /**
     *  @private
     *  
     *  Start building the groups
     */
    private function buildGroups():Boolean
    {
        if (!prepared)
        {
            var _openItems:Object = {};
            
            // initialize the variables
            initialize();
        
            if (source == null || (source as ICollectionView).length == 0)
                return false;
            
            if (dispatchCollectionEvents)
            {
                var hierarchicalData:IHierarchicalData = new HierarchicalData(newCollection);
                HierarchicalData(hierarchicalData).childrenField = childrenField;
                
                hView = new HierarchicalCollectionView( 
                                            hierarchicalData, _openItems);
            }
    
            flatView = source as ICollectionView;
            flatCursor = flatView.createCursor();
    
            gf = grouping.fields;
            fieldCount = gf.length;
            
            if (gf)
            {
                prepared = true;
            
                if (async)
                    return false;
            }
            
            if (async)
                return true;
        }
        
        flatCursor.seek(currentPosition);
        
        while(!flatCursor.afterLast && currentPosition != CursorBookmark.LAST)
        {
            currentData = flatCursor.current;
            
            var n:int = 0;
            
            for (var i:int = 0; i < fieldCount ; ++i)
            {
                var groupingField:String = gf[i].name;
                
                var label:String = getDataLabel(currentData, gf[i]);

                if(label != currentGroupLabels[i])
                {
                    if (childrenArray && childrenArray.length)
                    {
                        ArrayCollection(currentGroups[fieldCount - 1][childrenField]).source = childrenArray;
                        childrenArray = [];
                    }
                    
                    // calculate summaries for created groups
                    if (summaryPresent)
                    {
                        for (n = currentGroups.length - 1; n >= i; n--)
                            getSummaries(currentGroups[n], n);
                    }
                    
                    currentGroupLabels.splice(i+1);
                    currentGroups.splice(i+1);
                    currentIndices.splice(i+1);
                    
                    currentGroupLabels[i] = label;
                    
                    // check for grouping Object Function
                    if (gf[i].groupingObjectFunction != null)
                        currentGroups[i] = gf[i].groupingObjectFunction(label);
                    else if (grouping.groupingObjectFunction != null)
                        currentGroups[i] = grouping.groupingObjectFunction(label);
                    else
                        currentGroups[i] = {};
                    
                    currentGroups[i][childrenField] = new ArrayCollection();
                    
                    currentGroups[i][grouping.label] = currentGroupLabels[i];
                    
                    itemIndex = currentIndices[i-1];
                    // create the group
                    if (dispatchCollectionEvents)
                    {
                        IHierarchicalCollectionView(hView).addChild(currentGroups[i-1], currentGroups[i]);
                    } else
                    {
                        if (i > 0)
                        {
                            currentGroups[i-1][childrenField].source.push(currentGroups[i]);
                        }
                        else
                        {
                            newCollection.source.push(currentGroups[i]);
                        }
                    }
                    currentIndices[i-1] = ++itemIndex;
                }
                
                // insert the node as a child of the group
                if ( i == fieldCount - 1)
                {
                    itemIndex = currentIndices[i];
                    if (!childrenArray)
                        childrenArray = [];
                    childrenArray.push(currentData);
                    currentIndices[i] = ++itemIndex;
                }
            }

            //try
            //{
                flatCursor.moveNext();
                currentPosition = flatCursor.bookmark;
                // return in case of async refresh
                if (async)
                    return false;
                /*
            }
            catch (e:ItemPendingError)
            {
                cleanUp();
                e.addResponder(new ItemResponder(
                    function(data:Object, token:Object=null):void
                    {
                        makeGroupedCollection();
                    },
                    function(info:Object, token:Object=null):void
                    {
                        //no-op
                    }));
            }*/
        }
        if (currentPosition == CursorBookmark.LAST)
        {
            if (childrenArray && childrenArray.length)
            {
                ArrayCollection(currentGroups[fieldCount - 1][childrenField]).source = childrenArray;
                
                // calculate summaries for created groups
                if (summaryPresent)
                {
                    for (n = fieldCount - 1; n >= 0; n--)
                        getSummaries(currentGroups[n], n);
                }
            }
            
            // calculate root summaries
            if (source && summaries)
            {
                if (!super.source)
                    super.source = new ArrayCollection([source]) as Object;
                
                generateRootSummaries(grouping == null);
            }
            
			// refresh the collection to reflect the changes
			// we made while grouping.
			// This is needed as we made changes directly to
			// the source of the collection when
			// dispatchCollectionEvents is false
			newCollection.refresh();
			
            // dispatch collection change event of kind refresh.
            var refreshEvent:CollectionEvent =
                    new CollectionEvent(CollectionEvent.COLLECTION_CHANGE);
            refreshEvent.kind = CollectionEventKind.REFRESH;
            dispatchEvent(refreshEvent);
            
            cleanUp();
        }
        return true;
    }
    
    /**
     *  @private
     *  Get all the summary fields and store them in an Array
     */
    private function prepareSummaryFields():void
    {
        summaryFields = [];
        
        var sr:SummaryRow
        
        // for grouping fields summaries
        if (grouping.fields != null)
        {
            for (var i:int = 0; i < grouping.fields.length; i++)
            {
                var gf:GroupingField = grouping.fields[i];
                if (gf.summaries != null)
                {
                    for (var j:int = 0; j < gf.summaries.length; j++)
                    {
                        sr = gf.summaries[j];
                        if (sr.fields != null)
                        {
                            for (var k:int = 0; k < sr.fields.length; k++)
                            {
                                summaryPresent = true;
                                summaryFields.push(sr.fields[k]);
                            }
                        }
                    }
                }
            }
        }
        
        // for root level summaries
        if (summaries != null)
        {
            for (i = 0; i < summaries.length; i++)
            {
                sr = summaries[i];
                if (sr.fields != null)
                {
                    for (j = 0; j < sr.fields.length; j++)
                    {
                        summaryPresent = true;
                        summaryFields.push(sr.fields[j]);
                    }
                }
            }
        }
    }

    /**
     *  @private
     *  
     *  Restores the original sort in the source collection
     *  and clean up all the variables.
     */
    private function cleanUp():void
    {
        source.sort = oldSort;
        source.refresh();
        
        prepared = false;
        currentPosition = CursorBookmark.FIRST;
        oldSort = null;
        flatCursor = null;
    }
    
    /**
     *  @private
     *  
     *  It will call the function func on each node of the collection.
     */  
    private function applyFunctionForParentNodes(coll:ICollectionView, func:Function, depth:int = 0):void
    {   
        if (coll.length > 0)
        {
            var masterCursor:IViewCursor = coll.createCursor();
            
            while(!masterCursor.afterLast)
            {
                var child:Object = getChildren(masterCursor.current);
                if (child is ArrayCollection)
                {
                    var childCursor:IViewCursor = ArrayCollection(child).createCursor();
                    
                    while (!childCursor.afterLast)
                    {
                        var current:Object = childCursor.current;
                        // recurse over each child
                        if (this.hasChildren(current))
                        {
                            applyFunctionForParentNodes(child as ArrayCollection, func, depth + 1);
                            break;
                        }
                        
                        childCursor.moveNext();
                    }   
                }
                
                // calculate for the parent node
                func(masterCursor.current, depth);
                masterCursor.moveNext();
            }
        }
    }
    
    /**
     *  @private
     *  
     *  removes the root summaries and
     *  generates them again.
     * 
     */  
    private function regenerateRootSummaries():void
    {
        if(!summaries)
            return;
        
        var coll:ICollectionView = super.source as ICollectionView;
        if (!grouping)
            coll = coll.createCursor().current as ICollectionView;
        
        var summaryObj:Array = objectSummaryMap[UIDUtil.getUID(coll)];
        
        // for the first time there will be no summaries
        // so, this check will fail and root summaries wont
        // be removed and regenerated again.
        // for all the other times, the root summaries will be 
        // regenerated.
        if (!summaryObj || !(coll is IList))
            return;
        
        // delete all the root level summaries
        var n:int = summaryObj.length;
        for (var i:int = 0; i < n; i++)
        {
            var index:int = IList(coll).getItemIndex(summaryObj[i]);
            if (index != -1)
                IList(coll).removeItemAt(index);
        }
        
        delete objectSummaryMap[UIDUtil.getUID(coll)];
        
        // generate the root level summaries
        generateRootSummaries(grouping == null);
    }

    /**
     *  @private
     *  
     *  removes all the summaries from the collection
     */  
    private function removeAllSummaries():void
    {
        // call generate summary with remove summary function as parameter
        applyFunctionForParentNodes(super.source as ICollectionView, removeSummary);
    }
    
    /**
     *  @private
     *  
     *  remove the summaries for an item and its parents.
     *  return the parents of the node going one level up each time.
     * 
     */  
    private function removeItemAndSummaries(coll:ICollectionView, node:Object, removeItem:Boolean = false):Array
    {
        var parentNodes:Array = [];
        var parent:Object = getParent(node);
        while (parent != null)
        {
            var index:int;
            var addParent:Boolean = true;
            var children:ICollectionView = getChildren(parent) as ArrayCollection;
            if (children)
            {
                if (children.contains(node))
                {
                    if (children is IList)
                    {
                        if (removeItem)
                        {
                            // remove the item from the group
                            index = IList(children).getItemIndex(node);
                            if (index != -1)
                            {
                                IList(children).removeItemAt(index);
                                // delete item from parent map
                                var uid:String = UIDUtil.getUID(node);
                                if (parentMap[uid])
                                    delete parentMap[uid];
                            }
                        }
                        
                        if (objectSummaryMap[UIDUtil.getUID(parent)])
                        {
                            var temp:Array = objectSummaryMap[UIDUtil.getUID(parent)];
                            var n:int = temp.length;
                            for (var i:int = 0; i < n; i++)
                            {
                                index = IList(children).getItemIndex(temp[i]);
                                if (index != -1)
                                {
                                    // remove the summary information for the group
                                    IList(children).removeItemAt(index);
                                }
                            }
                            // delete summary from parent summary map
                            delete objectSummaryMap[UIDUtil.getUID(parent)];
                        }
                        
                        if (summariesTracker != null && summariesTracker[UIDUtil.getUID(parent)])
                            summariesTracker[UIDUtil.getUID(parent)] = {}; // new Dictionary(false);
                        
                        if (removeItem)
                        {
                            // remove the group if no children is present
                            if (children.length == 0 && getParent(parent) != null)
                            {
                                addParent = false;
                            }
                            else
                                removeItem = false;
                        }
                    }
                }
                if (addParent)
                    parentNodes.push(parent);
                
                node = parent;
                
                parent  = getParent(parent);
                if (!parent)
                {
                    // remove the parent node from the collection if its the only one remaining.
                    // first check for the child collection length
                    if (parentNodes.length == 1)
                    {
                        if ((getChildren(parentNodes[0]) as ICollectionView).length == 0 && coll is IList)
                        {
                            index = IList(coll).getItemIndex(node);
                            if (index != -1)
                            {
                                IList(coll).removeItemAt(index);
                                return null;
                            }
                        }
                    }
                    return parentNodes.reverse();
                }
            }
        }
        return null;
    }
    
    /**
     *  @private
     *  
     *  removes the summaries from the parent node and all its children.
     * 
     */  
    private function removeSummary(parent:Object, depth:int):void
    {   
        var children:ICollectionView = this.getChildren(parent) as ArrayCollection;
        
        if (!children)
            return;
        
        // remove summaries from the parents of the current object
        removeItemAndSummaries(super.source as ICollectionView, children.createCursor().current);
    }
    
    /**
     *  @private
     *  
     *  updates the parent map
     */ 
    private function updateParentMap(parent:Object, node:Object):void
    {
        var uid:String = UIDUtil.getUID(node);
        parentMap[uid] = parent;
    }
    
    /**
     *  @private
     *  
     *  removes the summary information and regenrates it for a particular node
     *  and its parents.
     *  optionally removes the item from the group also.
     */  
    private function updateSummary(node:Object, removeItem:Boolean = false):void
    {       
        var coll:ICollectionView = super.source as ICollectionView;
        
        var parentNodes:Array;
        if (summaryPresent || removeItem)
            parentNodes = removeItemAndSummaries(coll, node, removeItem);
        
        if (summaryPresent && parentNodes)
        {
            var n:int = parentNodes.length;
            for (var i:int = n - 1; i >= 0; i--)
            {
                getSummaries(parentNodes[i], i);
            }
        }
    }
    
    //--------------------------------------------------------------------------
    //
    //  Event handlers
    //
    //--------------------------------------------------------------------------
    
    /**
     *  @private
     * 
     *  collection change handler.
     * 
     */  
    private function collectionChangeHandler(event:CollectionEvent):void
    {
        if (!grouping)
            return;
        
        var i:int = 0;
        var j:int = 0;
        var n:int = 0;
        var m:int = 0;
        var obj:Object;
        
        if (event.kind == CollectionEventKind.UPDATE)
        {
            n = event.items.length;
            for (i = 0; i < n; i++)
            {
                var summaryCalculated:Boolean;
                // take the source property to get the updated object
                obj = event.items[i].source;
                
                if (!obj)
                    continue;
                
                m = grouping.fields.length;
                for (j = 0; j < m; j++)
                {
                    // check if the property corresponding to the group fields changed
                    if (event.items[i].property == grouping.fields[j].name)
                    {
                        summaryCalculated = true;
                        // update summaries - first remove the item from its group
                        updateSummary(obj,true);
                        // add the item to the group
                        addItem(obj);
                        break;
                    }
                }
                // for other properties just update the summaries
                if (!summaryCalculated)
                    updateSummary(obj);
            }
        }
        
        if (event.kind == CollectionEventKind.ADD)
        {
            n = event.items.length;
            for (i = 0; i < n; i++)
            {
                obj = event.items[i];
                // add the item to the group
                addItem(obj);
            }
        }
        
        if (event.kind == CollectionEventKind.REMOVE)
        {
            n = event.items.length;
            for (i = 0; i < n; i++)
            {
                obj = event.items[i];
                // update summaries - first remove the item from its group
                updateSummary(obj,true);
            }
        }
        
        if (event.kind == CollectionEventKind.REPLACE)
        {
            n = event.items.length;
            for (i = 0; i < n; i++)
            {
                var oldValue:Object = event.items[i].oldValue;
                var newValue:Object = event.items[i].newValue;
                // update summaries - first remove the item from its group
                updateSummary(oldValue,true);
                // add the item to the group
                addItem(newValue);
            }
        }
        
        // generate the root summaries
        regenerateRootSummaries();
    }
}

}