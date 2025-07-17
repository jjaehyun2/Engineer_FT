package
{
   // =======
   // IMPORTS
   // =======

   import LS_Classes.listDisplay;
   import flash.display.DisplayObjectContainer;
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.external.ExternalInterface;
   
   public dynamic class categoryListElement extends MovieClip
   {
       
      // =====================
      // VARIABLE DECLARATIONS
      // =====================
      
      public var addChapterButton_mc:addChapterButton;
      public var category_mc:MovieClip;
      public var chaptersHolder_mc:MovieClip;
      public var editableElement_mc:MovieClip;
      public var _id:Number;
      public var _chapters:listDisplay;
      public var heightOverride:Number;
      public var _editable:Boolean;
      public const captionBottomMargin:Number = 3;
      public var onDestroy:Function;
      
      public function categoryListElement()
      {
         super();
         addFrameScript(0,this.frame1);
      }
      
      public function Init(entriesMapIndex:Number, strContent:String) : *
      {
         //ExternalInterface.call("S7_DebugHook", "categoryListElement", "Initializing new categoryListElement", "entriesMapIndex", entriesMapIndex, "String Content", strContent)
         this._id = entriesMapIndex;   // Maps to FlashObject
         
         this.addChapterButton_mc.initialize((root as MovieClip).strings.addChapter, this.onAddChapter);
         this.addChapterButton_mc.heightOverride = 27;
         
         this.category_mc.Init();
         this.category_mc.addEventListener("HeightChanged",this.onHeightChanged);
         
         this.editableElement_mc.Init(this.category_mc, strContent,523,27);
         this.editableElement_mc.onRemove = this.onRemove;
         this.editableElement_mc.addEventListener("HeightChanged",this.onHeightChanged);
         this.editableElement_mc.id = this._id;
         
         this._chapters = new listDisplay();
         this.chaptersHolder_mc.addChild(this._chapters);
         this.category_mc.attachList(this._chapters);
         this._chapters.elementSpacing = 3;
         this._chapters.addElement(this.addChapterButton_mc, false);
         this._chapters.canPositionInvisibleElements = false;
         this._chapters.positionElements();
         this.updateHeight();
      }
      
      public function setEditable(editable:Boolean) : *
      {
         var chapterElement:* = undefined;
         this._editable = editable;
         this.editableElement_mc.setEditable(editable);
         this.addChapterButton_mc.visible = editable;
         var i:int = 0;
         while(i < this._chapters.length)
         {
            chapterElement = this._chapters.getAt(i);
            if(chapterElement != null && chapterElement.setEditable != undefined)
            {
               chapterElement.setEditable(editable);
            }
            i++;
         }
         this._chapters.positionElements();
         this.onHeightChanged(null);
      }
      
      public function onRemove(param1:MovieClip) : *
      {
         (root as MovieClip).content_mc.categories.removeElement(this.list_pos);
         ExternalInterface.call("removeNode",this._id);
         if(this.onDestroy != null)
         {
            this.onDestroy(this);
         }
      }
      
      public function onHeightChanged(param1:Event) : *
      {
         this.chaptersHolder_mc.y = this.editableElement_mc.heightOverride + this.captionBottomMargin;
         this.updateHeight();
         dispatchEvent(new Event("HeightChanged"));
      }
      
      public function updateHeight() : *
      {
         var heightChange:* = !!this._chapters.visible?this._chapters.visibleHeight:0;
         if(heightChange > 0)
         {
            heightChange = heightChange + this.captionBottomMargin;
         }
         this.heightOverride = this.editableElement_mc.heightOverride + heightChange;
      }
      
      public function onAddChapter() : *
      {
         ExternalInterface.call("addChapter", this._id);
      }
      
      public function createChapter(entriesMapIndex:Number, positionIndex:int, strContent:String, isShared:Boolean) : MovieClip
      {
         //ExternalInterface.call("S7_DebugHook", "categoryListElement", "Creating Chapter", "entriesMapIndex", entriesMapIndex, "positionIndex", positionIndex, "String Content", strContent)
         var chapterElement:* = new chapterListElement();
         this._chapters.addElementOnPosition(chapterElement, positionIndex, false);
         chapterElement.onRemove = this.onChapterRemove;
         chapterElement.Init(strContent, entriesMapIndex);
         chapterElement.setEditable(this._editable);
         chapterElement.addEventListener("HeightChanged",this.onChapterHeightChanged);
         chapterElement.editableElement_mc.setShared(isShared);
         chapterElement.parentId = this._id;
         var displayContainer:DisplayObjectContainer = this.addChapterButton_mc.parent;
         displayContainer.setChildIndex(this.addChapterButton_mc,displayContainer.numChildren - 1);
         this._chapters.positionElements();
         this.onHeightChanged(null);
         return chapterElement;
      }
      
      public function onChapterRemove(param1:int) : *
      {
         this._chapters.removeElement(param1);
         this.onHeightChanged(null);
      }
      
      public function onChapterHeightChanged(param1:Event) : *
      {
         this._chapters.positionElements();
         this.onHeightChanged(param1);
      }
      
      public function get id() : Number
      {
         return this._id;
      }
      
      function frame1() : *
      {
      }
   }
}