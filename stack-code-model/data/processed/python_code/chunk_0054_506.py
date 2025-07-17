package GMJournal_fla
{

   // =======   
   // IMPORTS
   // =======   

   import LS_Classes.textHelpers;
   import flash.display.DisplayObject;
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.external.ExternalInterface;
   import flash.geom.Point;
   import flash.text.TextField;
   
   public dynamic class MainTimeline extends MovieClip
   {
      
      // =====================
      // VARIABLE DECLARATIONS
      // =====================

      public var caption_mc:TextField;
      
      public var content_mc:MovieClip;
      public var paragraphs_mc:MovieClip;

      public var shareWithParty_mc:CheckBoxWlabel;
      public var closeButton_mc:closeButton;
      public var toggleEditButton_mc:toggleEditButton;
      
      public var EGMJournalNodeType:Object;
      public var strings:Object;
      public var editable:Boolean;
      public var entries:Array;
      public var entriesMap:Object;
      
      public var layout:String;
      public var isDragging:Boolean;
      public const CONTEXT_MENU_EVENT:String = "IE ContextMenu";
      public var events:Array;
      public var contextTarget:Number;
      
      // =============
      // MAIN TIMELINE
      // =============

      public function MainTimeline()
      {
         super();
         addFrameScript(0, this.frame1);
      }
      
      public function _mouse_press_hack_(param1:MouseEvent) : void
      {
      }
      
      public function onClose() : *
      {
         ExternalInterface.call("PlaySound","UI_Game_Journal_Close");
         //ExternalInterface.call("S7_DebugHook", "Root:onClose()", "Closing UI")
         ExternalInterface.call("S7_Journal_UI_Hide");
      }

      public function onToggleEdit() : *
      {
         //ExternalInterface.call("S7_DebugHook", "Root:onToggleEdit()", "Toggling Edit", "Root.editable", this.editable)
         this.editable = !this.editable;  // Boolean to control editable state
         if(!this.editable)
         {
            stage.focus = null;
         }
         this.content_mc.setEditControlsVisible(this.editable);
         this.paragraphs_mc.setEditable(this.editable);
      }
      
      public function HideSharedThings() : *
      {
         //ExternalInterface.call("S7_DebugHook", "Root:HideSharedThings()", "Hiding Shared Stuff")
         this.shareWithParty_mc.visible = false;
      }
      
      public function onEventInit() : *
      {
         //ExternalInterface.call("S7_DebugHook", "Root:onEventInit()", "Event Initialization")

         ExternalInterface.call("registerAnchorId", "gmjournal");
         ExternalInterface.call("setPosition", "center", "screen", "center");
         
         this.HideSharedThings();
         this.caption_mc.htmlText = this.strings.caption;

         this.toggleEditButton_mc.initialize(this.strings.editButtonCaption, this.onToggleEdit);
         this.closeButton_mc.init(this.onClose);
         
         this.content_mc.Init();
         this.paragraphs_mc.Init();
         this.shareWithParty_mc.init(this.onShareWithParty);
      }
      
      public function updateCaptions(): * {
         this.caption_mc.htmlText = this.strings.caption;
         this.toggleEditButton_mc.text_txt.htmlText = this.strings.editButtonCaption;
         this.content_mc.addCategoryButton_mc.text_txt.htmlText = this.strings.addCategory;
         this.paragraphs_mc.addParagraphButton_mc.text_txt.htmlText = this.strings.addParagraph;
         this.shareWithParty_mc.setText(this.strings.shareWithParty, -1)
      }

      //    UPDATE ENTRIES
      //    ==============

      public function updateEntries() : *
      {  
         var i:int = 0;
         var journalNodeTypeIndex:int = 0;
         var positionIndex:int = 0;
         var entriesMapIndex:Number = NaN;
         var categoryIndex:Number = NaN;
         var strContent:String = null;
         var isShared:Boolean = false;
         var entryMovieClip:* = undefined;

         while(i < this.entries.length)
         {
            journalNodeTypeIndex = this.entries[i++]; // this.entries[0] 1
            positionIndex = this.entries[i++];        // this.entries[1] 2
            entriesMapIndex = this.entries[i++];      // this.entries[2] 3
            categoryIndex = this.entries[i++];        // this.entries[3] 4
            strContent = this.entries[i++];           // this.entries[4] 5
            isShared = this.entries[i++];             // this.entries[5] 6

            //ExternalInterface.call("S7_DebugHook", "Root:updateEntries()", "Updating Entries", "journalNodeTypeIndex", journalNodeTypeIndex, "positionIndex", positionIndex, "entriesMapIndex", entriesMapIndex, "categoryMapIndex", categoryIndex, "String Content", strContent, "isShared", isShared)

            entryMovieClip = this.entriesMap[entriesMapIndex];
            
            switch(journalNodeTypeIndex)
            {
               case this.EGMJournalNodeType.EGMJournalNodeType_Unassigned:
               case this.EGMJournalNodeType.EGMJournalNodeType_Journal:
               default:
                  continue;
               case this.EGMJournalNodeType.EGMJournalNodeType_Category:
                  if(entryMovieClip == null)
                  {
                     this.createCategory(entriesMapIndex, positionIndex, strContent, isShared);
                  }
                  else
                  {
                     this.updateCategory(entryMovieClip, positionIndex, strContent, isShared);
                  }
                  continue;
               case this.EGMJournalNodeType.EGMJournalNodeType_Chapter:
                  if(entryMovieClip == null)
                  {
                     this.createChapter(entriesMapIndex, categoryIndex, positionIndex, strContent, isShared);
                  }
                  else
                  {
                     this.updateChapter(entryMovieClip, categoryIndex, positionIndex, strContent, isShared);
                  }
                  continue;
               case this.EGMJournalNodeType.EGMJournalNodeType_Paragraph:
                  if(entryMovieClip == null)
                  {
                     this.createParagraph(entriesMapIndex, categoryIndex, positionIndex, strContent, isShared);
                  }
                  else
                  {
                     this.updateParagraph(entryMovieClip, categoryIndex, positionIndex, strContent, isShared);
                  }
                  continue;
            }
         }
         this.content_mc.rebuildLayout();
         this.entries = new Array();
      }

      public function createCategory(entriesMapIndex:Number, positionIndex:int, strContent:String, isShared:Boolean) : MovieClip
      {
         //ExternalInterface.call("S7_DebugHook", "Root:createCategory()", "Creating Category")
         var catElement:* = this.content_mc.createCategory(entriesMapIndex, positionIndex, strContent, isShared);
         catElement.editableElement_mc.ownerScrollList = this.content_mc.categories;
         this.entriesMap[entriesMapIndex] = catElement;
         catElement.onDestroy = this.onCategoryDestroy;
         return catElement;
      }
      
      public function updateCategory(entryMovieClip:MovieClip, positionIndex:int, strContent:String, isShared:Boolean) : *
      {
         //ExternalInterface.call("S7_DebugHook", "Root:updateCategory()", "Updating Category")
         if(entryMovieClip.list_pos != positionIndex)
         {
            this.content_mc.categories.addElementOnPosition(entryMovieClip, positionIndex, false);
            this.content_mc.rebuildLayout();
         }
         entryMovieClip.editableElement_mc.updateText(strContent);
         entryMovieClip.editableElement_mc.setShared(isShared);
      }
      
      public function createChapter(entriesMapIndex:Number, categoryIndex:Number, positionIndex:int, strContent:String, isShared:Boolean) : MovieClip
      {
         //ExternalInterface.call("S7_DebugHook", "Root:createChapter()", "Creating Chapter")
         
         var catElement:MovieClip = this.entriesMap[categoryIndex] as MovieClip;
         if(catElement == null)
         {
            catElement = this.createCategory(categoryIndex, this.content_mc.categories.length, "", false);
         }
         var newCatElement:MovieClip = catElement.createChapter(entriesMapIndex, positionIndex, strContent, isShared);
         catElement.editableElement_mc.ownerScrollList = this.content_mc.categories;
         newCatElement.onSelect = this.onChapterSelect;
         this.entriesMap[entriesMapIndex] = newCatElement;
         newCatElement.onDestroy = this.onChapterDestroy;
         return newCatElement;
      }
      
      public function updateChapter(entriesMovieClip:MovieClip, categoryIndex:Number, positionIndex:int, strContent:String, isShared:Boolean) : *
      {
         // ExternalInterface.call("S7_DebugHook", "Root:updateChapter()", "Updating Chapter", "categoryIndex", categoryIndex, "positionIndex", positionIndex, "String Content", strContent, "isShared", isShared)
         var _loc6_:MovieClip = null;
         var _loc7_:MovieClip = null;
         var _loc8_:MovieClip = null;

         if(entriesMovieClip.parentId != categoryIndex)
         {
            _loc6_ = this.entriesMap[entriesMovieClip.parentId];
            if(_loc6_ != null)
            {
               _loc6_.removeChapter(entriesMovieClip);
            }
            _loc7_ = this.entriesMap[categoryIndex];
            if(_loc7_ != null)
            {
               _loc7_.addChapter(entriesMovieClip, positionIndex);
            }
         }
         else if(positionIndex != entriesMovieClip.list_pos)
         {
            _loc8_ = this.entriesMap[categoryIndex];
            if(_loc8_ != null)
            {
               _loc8_.addChapter(entriesMovieClip, positionIndex);
            }
         }
         entriesMovieClip.editableElement_mc.updateText(strContent);
         entriesMovieClip.editableElement_mc.setShared(isShared);
      }
      
      public function createParagraph(entriesMapIndex:Number, categoryIndex:Number, positionIndex:int, strContent:String, isShared:Boolean) : *
      {
         //ExternalInterface.call("S7_DebugHook", "Root:createParagraph()", "Creating Paragraph")
         var catElement:MovieClip = this.entriesMap[categoryIndex] as MovieClip;
         if(catElement == null)
         {
            catElement = this.createChapter(categoryIndex,-1,0,"",false);
         }
         var newCatElement:* = catElement.createParagraph(entriesMapIndex, positionIndex, strContent, isShared);
         newCatElement.editableElement_mc.ownerScrollList = this.paragraphs_mc._paragraphsList;
         this.entriesMap[entriesMapIndex] = newCatElement;
         if(catElement == this.paragraphs_mc._currentChapter)
         {
            this.paragraphs_mc.addParagraph(newCatElement,positionIndex);
         }
         newCatElement.onDestroy = this.onParagraphDestroy;
      }
      
      public function updateParagraph(entriesMovieClip:MovieClip, categoryIndex:Number, positionIndex:int, strContent:String, isShared:Boolean) : *
      {
         //ExternalInterface.call("S7_DebugHook", "Root:updateParagraph()", "Updating Paragraph", "categoryIndex", categoryIndex, "positionIndex", positionIndex, "String Content", strContent, "isShared", isShared)
         var _loc6_:MovieClip = null;
         var _loc7_:MovieClip = null;
         var _loc8_:MovieClip = null;
         if(entriesMovieClip.parentId != categoryIndex)
         {
            _loc6_ = this.entriesMap[entriesMovieClip.parentId];
            if(_loc6_ != null)
            {
               _loc6_.removeParagraph(entriesMovieClip);
               if(_loc6_ == this.paragraphs_mc._currentChapter)
               {
                  this.paragraphs_mc.removeParagraph(entriesMovieClip);
               }
            }
            _loc7_ = this.entriesMap[categoryIndex];
            if(_loc7_ != null)
            {
               _loc7_.addParagraph(entriesMovieClip,positionIndex);
               if(_loc7_ == this.paragraphs_mc._currentChapter)
               {
                  this.paragraphs_mc.addParagraph(entriesMovieClip, positionIndex);
               }
            }
         }
         else if(positionIndex != entriesMovieClip.list_pos)
         {
            _loc8_ = this.entriesMap[categoryIndex];
            if(_loc8_ != null)
            {
               _loc8_.addParagraph(entriesMovieClip,positionIndex);
               if(_loc8_ == this.paragraphs_mc._currentChapter)
               {
                  this.paragraphs_mc.addParagraph(entriesMovieClip, positionIndex);
               }
            }
         }
         entriesMovieClip.editableElement_mc.updateText(strContent);
         entriesMovieClip.editableElement_mc.setShared(isShared);
      }
      
      public function removeEntry(param1:Number) : *
      {
      }
      
      public function onChapterSelect(chapterMC:MovieClip) : *
      {
         this.paragraphs_mc.selectChapter(chapterMC);
      }
      
      public function onCategoryDestroy(categoryMC:MovieClip) : *
      {
         this.entriesMap[categoryMC.id] = undefined;

         var i:int = 0;
         while(i < categoryMC._chapters.content_array.length - 1)
         {
            this.onChapterDestroy(categoryMC._chapters.getAt(i));
            i++;
         }
      }
      
      public function onChapterDestroy(chapterMC:MovieClip) : *
      {
         this.entriesMap[chapterMC.id] = undefined;

         var i:int = 0;
         var noOfParagraphs:int = chapterMC.paragraphs.length;
         while(i < noOfParagraphs)
         {
            this.onParagraphDestroy(chapterMC.paragraphs[i]);
            i++;
         }
         if(this.paragraphs_mc._currentChapter == chapterMC)
         {
            this.paragraphs_mc.selectChapter(null);
         }
      }
      
      public function onParagraphDestroy(paragraphMC:MovieClip) : *
      {
         this.entriesMap[paragraphMC.id] = undefined;
      }
      
      public function onShareWithParty() : *
      {
         ExternalInterface.call("updateShared", 4294967295);
      }
      
      public function onEventUp(eventIndex:Number, param2:Number) : *
      {
         var _loc3_:Array = null;
         var _loc4_:int = 0;
         var _loc5_:DisplayObject = null;
         switch(this.events[eventIndex])
         {
            case this.CONTEXT_MENU_EVENT:
               if(this.editable)
               {
                  _loc3_ = stage.getObjectsUnderPoint(new Point(stage.mouseX,stage.mouseY)).reverse();
                  _loc4_ = 0;
                  while(_loc4_ < _loc3_.length)
                  {
                     _loc5_ = _loc3_[_loc4_];
                     if(_loc5_ && _loc5_.hasEventListener && _loc5_.hasEventListener(this.CONTEXT_MENU_EVENT))
                     {
                        if(_loc5_ is TextField)
                        {
                           this.contextTarget = textHelpers.getSelectionLengthOfText(_loc5_ as TextField,_loc5_.mouseX,_loc5_.mouseY);
                        }
                        _loc5_.dispatchEvent(new Event(this.CONTEXT_MENU_EVENT));
                        return true;
                     }
                     _loc4_++;
                  }
                  return true;
               }
               break;
            default:
               if(this.editable)
               {
                  _loc3_ = stage.getObjectsUnderPoint(new Point(stage.mouseX,stage.mouseY)).reverse();
                  _loc4_ = 0;
                  while(_loc4_ < _loc3_.length)
                  {
                     _loc5_ = _loc3_[_loc4_];
                     if(_loc5_ && _loc5_.hasEventListener && _loc5_.hasEventListener(this.CONTEXT_MENU_EVENT))
                     {
                        if(_loc5_ is TextField)
                        {
                           this.contextTarget = textHelpers.getSelectionLengthOfText(_loc5_ as TextField,_loc5_.mouseX,_loc5_.mouseY);
                        }
                        _loc5_.dispatchEvent(new Event(this.CONTEXT_MENU_EVENT));
                        return true;
                     }
                     _loc4_++;
                  }
                  return true;
               }
               break;
         }
         return false;
      }
      
      public function onEventDown(eventIndex:Number, param2:Number) : *
      {
         var text:TextField = null;
         switch(this.events[eventIndex])
         {
            case "IE UICopy":
               if(stage.focus && stage.focus is TextField)
               {
                  text = stage.focus as TextField;
                  ExternalInterface.call("copy", Math.abs(text.selectionEndIndex - text.selectionBeginIndex));
               }
               return true;
            case "IE UICut":
               if(stage.focus && stage.focus is TextField)
               {
                  text = stage.focus as TextField;
                  ExternalInterface.call("cut", Math.abs(text.selectionEndIndex - text.selectionBeginIndex));
               }
               return true;
            case "IE UIPaste":
               if(stage.focus && stage.focus is TextField)
               {
                  text = stage.focus as TextField;
                  if(text.selectable)
                  {
                     ExternalInterface.call("paste");
                  }
               }
               return true;
            case "IE UICancel":
               this.onClose();
               return true;
            default:
               return false;
         }
      }
      
      // ======================
      // FRAME 1 INTIIALIZATION
      // ======================

      function frame1() : *
      {
         addEventListener(MouseEvent.MOUSE_DOWN, this._mouse_press_hack_); // Dunno what this does.

         this.layout = "fixed";  // Experiment with later.
         this.isDragging = false;   // Used in scrollList.as

         // EVENTS ARRAY
         this.events = new Array("IE UICopy", "IE UICut", "IE UIPaste", this.CONTEXT_MENU_EVENT, "IE UICancel");
         
         // DYNAMIC-TEXT STRINGS OBJECT
         this.strings = {
            "caption":"",
            "editButtonCaption":"",
            "addChapter":"",
            "addCategory":"",
            "addParagraph":"",
            "shareWithParty":""
         };
         
         this.editable = false;  // isEditable toggle

         this.entries = new Array();   // entries[1 - 6]: JournalNodeType, PositionIndex, EntriesMapIndex, CategoryIndex, StringContent, isSharedBoolean
         
         // JOURNAL NODE TYPES
         this.EGMJournalNodeType = {
            "EGMJournalNodeType_Unassigned":0,
            "EGMJournalNodeType_Category":1,
            "EGMJournalNodeType_Chapter":2,
            "EGMJournalNodeType_Paragraph":3,
            "EGMJournalNodeType_Journal":4
         };
         
         this.entriesMap = new Object();  // Stores IDs and FlashObjects
      }
   }
}