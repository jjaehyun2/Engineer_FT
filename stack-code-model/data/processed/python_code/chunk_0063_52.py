package
{
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.FocusEvent;
   import flash.events.MouseEvent;
   import flash.external.ExternalInterface;
   
   public dynamic class chapterListElement extends MovieClip
   {
       
      
      public var chapter_mc:MovieClip;
      public var editableElement_mc:MovieClip;
      public var onRemove:Function;
      public var heightOverride:Number;
      public var onSelect:Function;
      public var _id:Number;
      public var parentId:Number;
      public var paragraphs:Array;
      public var onDestroy:Function;
      
      public function chapterListElement()
      {
         super();
         addFrameScript(0,this.frame1);
      }
      
      public function Init(strContent:String, chapID:Number) : *
      {
         //ExternalInterface.call("S7_DebugHook", "chapterListElement", "Initializing chapterList", "ChapID", chapID, "String Content", strContent)
         this._id = chapID;
         this.paragraphs = new Array();
         this.editableElement_mc.Init(this.chapter_mc, strContent, 523, 27);
         
         this.editableElement_mc.onRemove = this.onChapterRemove;
         this.editableElement_mc.addEventListener("HeightChanged",this.onHeightChanged);
         this.editableElement_mc.id = chapID;
         this.updateHeight();
      }
      
      public function onHeightChanged(param1:Event) : *
      {
         this.updateHeight();
         dispatchEvent(new Event("HeightChanged"));
      }
      
      public function updateHeight() : *
      {
         this.heightOverride = this.editableElement_mc.heightOverride;
      }
      
      public function setEditable(editable:Boolean) : *
      {
         this.editableElement_mc.setEditable(editable);
         if(editable)
         {
            addEventListener(FocusEvent.FOCUS_IN,this.onFocusIn);
            removeEventListener(MouseEvent.MOUSE_UP,this.onMouseUp);
         }
         else
         {
            removeEventListener(FocusEvent.FOCUS_IN,this.onFocusIn);
            addEventListener(MouseEvent.MOUSE_UP,this.onMouseUp);
         }
      }
      
      public function selectThis() : *
      {
         if(this.onSelect != null)
         {
            this.onSelect(this);
         }
      }
      
      public function onMouseUp(param1:Event) : *
      {
         this.selectThis();
      }
      
      public function onChapterRemove() : *
      {
         if(this.onRemove != null)
         {
            this.onRemove(this.list_pos);
         }
         ExternalInterface.call("removeNode", this.id);
         if(this.onDestroy != null)
         {
            this.onDestroy(this);
         }
      }
      
      public function onFocusIn(param1:Event) : *
      {
         this.selectThis();
      }
      
      public function createParagraph(ID:Number, positionIndex:int, strContent:String, isShared:Boolean) : MovieClip
      {
         //ExternalInterface.call("S7_DebugHook", "chapterListElement", "Creating Paragraph", "ID", ID, "positionIndex", positionIndex, "String Content", strContent, "isShared", isShared)
         var paraList:* = new paragraphListElement();

         paraList.Init(strContent, ID);
         paraList.editableElement_mc.setShared(isShared);

         paraList.parentId = this._id;
         if(this.paragraphs.length <= positionIndex)
         {
            this.paragraphs[positionIndex] = paraList;
         }
         else
         {
            this.paragraphs.splice(positionIndex,0,paraList);
         }
         return paraList;
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