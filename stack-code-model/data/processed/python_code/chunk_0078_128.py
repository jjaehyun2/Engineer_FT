package fl.managers
{
   import fl.controls.Button;
   import fl.core.UIComponent;
   import flash.display.DisplayObject;
   import flash.display.DisplayObjectContainer;
   import flash.display.InteractiveObject;
   import flash.display.SimpleButton;
   import flash.display.Stage;
   import flash.events.Event;
   import flash.events.FocusEvent;
   import flash.events.KeyboardEvent;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFieldType;
   import flash.ui.Keyboard;
   import flash.utils.Dictionary;
   
   public class FocusManager implements IFocusManager
   {
       
      
      private var _form:DisplayObjectContainer;
      
      private var focusableObjects:Dictionary;
      
      private var focusableCandidates:Array;
      
      private var activated:Boolean = false;
      
      private var calculateCandidates:Boolean = true;
      
      private var lastFocus:InteractiveObject;
      
      private var _showFocusIndicator:Boolean = true;
      
      private var lastAction:String;
      
      private var defButton:Button;
      
      private var _defaultButton:Button;
      
      private var _defaultButtonEnabled:Boolean = true;
      
      public function FocusManager(param1:DisplayObjectContainer)
      {
         super();
         focusableObjects = new Dictionary(true);
         if(param1 != null)
         {
            _form = param1;
            activate();
         }
      }
      
      private function addedHandler(param1:Event) : void
      {
         var _loc2_:DisplayObject = DisplayObject(param1.target);
         if(_loc2_.stage)
         {
            addFocusables(DisplayObject(param1.target));
         }
      }
      
      private function removedHandler(param1:Event) : void
      {
         var _loc2_:int = 0;
         var _loc4_:InteractiveObject = null;
         var _loc3_:DisplayObject = DisplayObject(param1.target);
         if(_loc3_ is IFocusManagerComponent && focusableObjects[_loc3_] == true)
         {
            if(_loc3_ == lastFocus)
            {
               IFocusManagerComponent(lastFocus).drawFocus(false);
               lastFocus = null;
            }
            _loc3_.removeEventListener(Event.TAB_ENABLED_CHANGE,tabEnabledChangeHandler,false);
            delete focusableObjects[_loc3_];
            calculateCandidates = true;
         }
         else if(_loc3_ is InteractiveObject && focusableObjects[_loc3_] == true)
         {
            _loc4_ = _loc3_ as InteractiveObject;
            if(_loc4_)
            {
               if(_loc4_ == lastFocus)
               {
                  lastFocus = null;
               }
               delete focusableObjects[_loc4_];
               calculateCandidates = true;
            }
            _loc3_.addEventListener(Event.TAB_ENABLED_CHANGE,tabEnabledChangeHandler,false,0,true);
         }
         removeFocusables(_loc3_);
      }
      
      private function addFocusables(param1:DisplayObject, param2:Boolean = false) : void
      {
         var focusable:IFocusManagerComponent = null;
         var io:InteractiveObject = null;
         var doc:DisplayObjectContainer = null;
         var docParent:DisplayObjectContainer = null;
         var i:int = 0;
         var child:DisplayObject = null;
         var o:DisplayObject = param1;
         var skipTopLevel:Boolean = param2;
         if(!skipTopLevel)
         {
            if(o is IFocusManagerComponent)
            {
               focusable = IFocusManagerComponent(o);
               if(focusable.focusEnabled)
               {
                  if(focusable.tabEnabled && isTabVisible(o))
                  {
                     focusableObjects[o] = true;
                     calculateCandidates = true;
                  }
                  o.addEventListener(Event.TAB_ENABLED_CHANGE,tabEnabledChangeHandler,false,0,true);
                  o.addEventListener(Event.TAB_INDEX_CHANGE,tabIndexChangeHandler,false,0,true);
               }
            }
            else if(o is InteractiveObject)
            {
               io = o as InteractiveObject;
               if(io && io.tabEnabled && findFocusManagerComponent(io) == io)
               {
                  focusableObjects[io] = true;
                  calculateCandidates = true;
               }
               io.addEventListener(Event.TAB_ENABLED_CHANGE,tabEnabledChangeHandler,false,0,true);
               io.addEventListener(Event.TAB_INDEX_CHANGE,tabIndexChangeHandler,false,0,true);
            }
         }
         if(o is DisplayObjectContainer)
         {
            doc = DisplayObjectContainer(o);
            o.addEventListener(Event.TAB_CHILDREN_CHANGE,tabChildrenChangeHandler,false,0,true);
            docParent = null;
            try
            {
               docParent = doc.parent;
            }
            catch(se:SecurityError)
            {
               docParent = null;
            }
            if(doc is Stage || docParent is Stage || doc.tabChildren)
            {
               i = 0;
               while(i < doc.numChildren)
               {
                  try
                  {
                     child = doc.getChildAt(i);
                     if(child != null)
                     {
                        addFocusables(doc.getChildAt(i));
                     }
                  }
                  catch(error:SecurityError)
                  {
                  }
                  i++;
               }
            }
         }
      }
      
      private function removeFocusables(param1:DisplayObject) : void
      {
         var _loc2_:* = null;
         var _loc3_:DisplayObject = null;
         if(param1 is DisplayObjectContainer)
         {
            param1.removeEventListener(Event.TAB_CHILDREN_CHANGE,tabChildrenChangeHandler,false);
            param1.removeEventListener(Event.TAB_INDEX_CHANGE,tabIndexChangeHandler,false);
            for(_loc2_ in focusableObjects)
            {
               _loc3_ = DisplayObject(_loc2_);
               if(DisplayObjectContainer(param1).contains(_loc3_))
               {
                  if(_loc3_ == lastFocus)
                  {
                     lastFocus = null;
                  }
                  _loc3_.removeEventListener(Event.TAB_ENABLED_CHANGE,tabEnabledChangeHandler,false);
                  delete focusableObjects[_loc2_];
                  calculateCandidates = true;
               }
            }
         }
      }
      
      private function isTabVisible(param1:DisplayObject) : Boolean
      {
         var p:DisplayObjectContainer = null;
         var o:DisplayObject = param1;
         try
         {
            p = o.parent;
            while(p && !(p is Stage) && !(p.parent && p.parent is Stage))
            {
               if(!p.tabChildren)
               {
                  return false;
               }
               p = p.parent;
            }
         }
         catch(se:SecurityError)
         {
         }
         return true;
      }
      
      private function isValidFocusCandidate(param1:DisplayObject, param2:String) : Boolean
      {
         var _loc3_:IFocusManagerGroup = null;
         if(!isEnabledAndVisible(param1))
         {
            return false;
         }
         if(param1 is IFocusManagerGroup)
         {
            _loc3_ = IFocusManagerGroup(param1);
            if(param2 == _loc3_.groupName)
            {
               return false;
            }
         }
         return true;
      }
      
      private function isEnabledAndVisible(param1:DisplayObject) : Boolean
      {
         var formParent:DisplayObjectContainer = null;
         var tf:TextField = null;
         var sb:SimpleButton = null;
         var o:DisplayObject = param1;
         try
         {
            formParent = DisplayObject(form).parent;
            while(o != formParent)
            {
               if(o is UIComponent)
               {
                  if(!UIComponent(o).enabled)
                  {
                     return false;
                  }
               }
               else if(o is TextField)
               {
                  tf = TextField(o);
                  if(tf.type == TextFieldType.DYNAMIC || !tf.selectable)
                  {
                     return false;
                  }
               }
               else if(o is SimpleButton)
               {
                  sb = SimpleButton(o);
                  if(!sb.enabled)
                  {
                     return false;
                  }
               }
               if(!o.visible)
               {
                  return false;
               }
               o = o.parent;
            }
         }
         catch(se:SecurityError)
         {
         }
         return true;
      }
      
      private function tabEnabledChangeHandler(param1:Event) : void
      {
         calculateCandidates = true;
         var _loc2_:InteractiveObject = InteractiveObject(param1.target);
         var _loc3_:* = focusableObjects[_loc2_] == true;
         if(_loc2_.tabEnabled)
         {
            if(!_loc3_ && isTabVisible(_loc2_))
            {
               if(!(_loc2_ is IFocusManagerComponent))
               {
                  _loc2_.focusRect = false;
               }
               focusableObjects[_loc2_] = true;
            }
         }
         else if(_loc3_)
         {
            delete focusableObjects[_loc2_];
         }
      }
      
      private function tabIndexChangeHandler(param1:Event) : void
      {
         calculateCandidates = true;
      }
      
      private function tabChildrenChangeHandler(param1:Event) : void
      {
         if(param1.target != param1.currentTarget)
         {
            return;
         }
         calculateCandidates = true;
         var _loc2_:DisplayObjectContainer = DisplayObjectContainer(param1.target);
         if(_loc2_.tabChildren)
         {
            addFocusables(_loc2_,true);
         }
         else
         {
            removeFocusables(_loc2_);
         }
      }
      
      public function activate() : void
      {
         if(activated)
         {
            return;
         }
         addFocusables(form);
         form.addEventListener(Event.ADDED,addedHandler,false,0,true);
         form.addEventListener(Event.REMOVED,removedHandler,false,0,true);
         try
         {
            form.stage.addEventListener(FocusEvent.MOUSE_FOCUS_CHANGE,mouseFocusChangeHandler,false,0,true);
            form.stage.addEventListener(FocusEvent.KEY_FOCUS_CHANGE,keyFocusChangeHandler,false,0,true);
            form.stage.addEventListener(Event.ACTIVATE,activateHandler,false,0,true);
            form.stage.addEventListener(Event.DEACTIVATE,deactivateHandler,false,0,true);
         }
         catch(se:SecurityError)
         {
            form.addEventListener(FocusEvent.MOUSE_FOCUS_CHANGE,mouseFocusChangeHandler,false,0,true);
            form.addEventListener(FocusEvent.KEY_FOCUS_CHANGE,keyFocusChangeHandler,false,0,true);
            form.addEventListener(Event.ACTIVATE,activateHandler,false,0,true);
            form.addEventListener(Event.DEACTIVATE,deactivateHandler,false,0,true);
         }
         form.addEventListener(FocusEvent.FOCUS_IN,focusInHandler,true,0,true);
         form.addEventListener(FocusEvent.FOCUS_OUT,focusOutHandler,true,0,true);
         form.addEventListener(MouseEvent.MOUSE_DOWN,mouseDownHandler,false,0,true);
         form.addEventListener(KeyboardEvent.KEY_DOWN,keyDownHandler,true,0,true);
         activated = true;
         if(lastFocus)
         {
            setFocus(lastFocus);
         }
      }
      
      public function deactivate() : void
      {
         if(!activated)
         {
            return;
         }
         focusableObjects = new Dictionary(true);
         focusableCandidates = null;
         lastFocus = null;
         defButton = null;
         form.removeEventListener(Event.ADDED,addedHandler,false);
         form.removeEventListener(Event.REMOVED,removedHandler,false);
         try
         {
            form.stage.removeEventListener(FocusEvent.MOUSE_FOCUS_CHANGE,mouseFocusChangeHandler,false);
            form.stage.removeEventListener(FocusEvent.KEY_FOCUS_CHANGE,keyFocusChangeHandler,false);
            form.stage.removeEventListener(Event.ACTIVATE,activateHandler,false);
            form.stage.removeEventListener(Event.DEACTIVATE,deactivateHandler,false);
         }
         catch(se:SecurityError)
         {
         }
         form.removeEventListener(FocusEvent.MOUSE_FOCUS_CHANGE,mouseFocusChangeHandler,false);
         form.removeEventListener(FocusEvent.KEY_FOCUS_CHANGE,keyFocusChangeHandler,false);
         form.removeEventListener(Event.ACTIVATE,activateHandler,false);
         form.removeEventListener(Event.DEACTIVATE,deactivateHandler,false);
         form.removeEventListener(FocusEvent.FOCUS_IN,focusInHandler,true);
         form.removeEventListener(FocusEvent.FOCUS_OUT,focusOutHandler,true);
         form.removeEventListener(MouseEvent.MOUSE_DOWN,mouseDownHandler,false);
         form.removeEventListener(KeyboardEvent.KEY_DOWN,keyDownHandler,true);
         activated = false;
      }
      
      private function focusInHandler(param1:FocusEvent) : void
      {
         var _loc3_:Button = null;
         if(!activated)
         {
            return;
         }
         var _loc2_:InteractiveObject = InteractiveObject(param1.target);
         if(form.contains(_loc2_))
         {
            lastFocus = findFocusManagerComponent(InteractiveObject(_loc2_));
            if(lastFocus is Button)
            {
               _loc3_ = Button(lastFocus);
               if(defButton)
               {
                  defButton.emphasized = false;
                  defButton = _loc3_;
                  _loc3_.emphasized = true;
               }
            }
            else if(defButton && defButton != _defaultButton)
            {
               defButton.emphasized = false;
               defButton = _defaultButton;
               _defaultButton.emphasized = true;
            }
         }
      }
      
      private function focusOutHandler(param1:FocusEvent) : void
      {
         if(!activated)
         {
            return;
         }
         var _loc2_:InteractiveObject = param1.target as InteractiveObject;
      }
      
      private function activateHandler(param1:Event) : void
      {
         if(!activated)
         {
            return;
         }
         var _loc2_:InteractiveObject = InteractiveObject(param1.target);
         if(lastFocus)
         {
            if(lastFocus is IFocusManagerComponent)
            {
               IFocusManagerComponent(lastFocus).setFocus();
            }
            else
            {
               form.stage.focus = lastFocus;
            }
         }
         lastAction = "ACTIVATE";
      }
      
      private function deactivateHandler(param1:Event) : void
      {
         if(!activated)
         {
            return;
         }
         var _loc2_:InteractiveObject = InteractiveObject(param1.target);
      }
      
      private function mouseFocusChangeHandler(param1:FocusEvent) : void
      {
         if(!activated)
         {
            return;
         }
         if(param1.relatedObject is TextField)
         {
            return;
         }
         param1.preventDefault();
      }
      
      private function keyFocusChangeHandler(param1:FocusEvent) : void
      {
         if(!activated)
         {
            return;
         }
         showFocusIndicator = true;
         if((param1.keyCode == Keyboard.TAB || param1.keyCode == 0) && !param1.isDefaultPrevented())
         {
            setFocusToNextObject(param1);
            param1.preventDefault();
         }
      }
      
      private function keyDownHandler(param1:KeyboardEvent) : void
      {
         if(!activated)
         {
            return;
         }
         if(param1.keyCode == Keyboard.TAB)
         {
            lastAction = "KEY";
            if(calculateCandidates)
            {
               sortFocusableObjects();
               calculateCandidates = false;
            }
         }
         if(defaultButtonEnabled && param1.keyCode == Keyboard.ENTER && defaultButton && defButton.enabled)
         {
            sendDefaultButtonEvent();
         }
      }
      
      private function mouseDownHandler(param1:MouseEvent) : void
      {
         if(!activated)
         {
            return;
         }
         if(param1.isDefaultPrevented())
         {
            return;
         }
         var _loc2_:InteractiveObject = getTopLevelFocusTarget(InteractiveObject(param1.target));
         if(!_loc2_)
         {
            return;
         }
         showFocusIndicator = false;
         if((_loc2_ != lastFocus || lastAction == "ACTIVATE") && !(_loc2_ is TextField))
         {
            setFocus(_loc2_);
         }
         lastAction = "MOUSEDOWN";
      }
      
      public function get defaultButton() : Button
      {
         return _defaultButton;
      }
      
      public function set defaultButton(param1:Button) : void
      {
         var _loc2_:Button = !!param1?Button(param1):null;
         if(_loc2_ != _defaultButton)
         {
            if(_defaultButton)
            {
               _defaultButton.emphasized = false;
            }
            if(defButton)
            {
               defButton.emphasized = false;
            }
            _defaultButton = _loc2_;
            defButton = _loc2_;
            if(_loc2_)
            {
               _loc2_.emphasized = true;
            }
         }
      }
      
      public function sendDefaultButtonEvent() : void
      {
         defButton.dispatchEvent(new MouseEvent(MouseEvent.CLICK));
      }
      
      private function setFocusToNextObject(param1:FocusEvent) : void
      {
         if(!hasFocusableObjects())
         {
            return;
         }
         var _loc2_:InteractiveObject = getNextFocusManagerComponent(param1.shiftKey);
         if(_loc2_)
         {
            setFocus(_loc2_);
         }
      }
      
      private function hasFocusableObjects() : Boolean
      {
         var _loc1_:* = null;
         for(_loc1_ in focusableObjects)
         {
            return true;
         }
         return false;
      }
      
      public function getNextFocusManagerComponent(param1:Boolean = false) : InteractiveObject
      {
         var _loc8_:IFocusManagerGroup = null;
         if(!hasFocusableObjects())
         {
            return null;
         }
         if(calculateCandidates)
         {
            sortFocusableObjects();
            calculateCandidates = false;
         }
         var _loc2_:DisplayObject = form.stage.focus;
         _loc2_ = DisplayObject(findFocusManagerComponent(InteractiveObject(_loc2_)));
         var _loc3_:String = "";
         if(_loc2_ is IFocusManagerGroup)
         {
            _loc8_ = IFocusManagerGroup(_loc2_);
            _loc3_ = _loc8_.groupName;
         }
         var _loc4_:int = getIndexOfFocusedObject(_loc2_);
         var _loc5_:Boolean = false;
         var _loc6_:int = _loc4_;
         if(_loc4_ == -1)
         {
            if(param1)
            {
               _loc4_ = focusableCandidates.length;
            }
            _loc5_ = true;
         }
         var _loc7_:int = getIndexOfNextObject(_loc4_,param1,_loc5_,_loc3_);
         return findFocusManagerComponent(focusableCandidates[_loc7_]);
      }
      
      private function getIndexOfFocusedObject(param1:DisplayObject) : int
      {
         var _loc2_:int = focusableCandidates.length;
         var _loc3_:int = 0;
         _loc3_ = 0;
         while(_loc3_ < _loc2_)
         {
            if(focusableCandidates[_loc3_] == param1)
            {
               return _loc3_;
            }
            _loc3_++;
         }
         return -1;
      }
      
      private function getIndexOfNextObject(param1:int, param2:Boolean, param3:Boolean, param4:String) : int
      {
         var _loc7_:DisplayObject = null;
         var _loc8_:IFocusManagerGroup = null;
         var _loc9_:int = 0;
         var _loc10_:DisplayObject = null;
         var _loc11_:IFocusManagerGroup = null;
         var _loc5_:int = focusableCandidates.length;
         var _loc6_:int = param1;
         while(true)
         {
            if(param2)
            {
               param1--;
            }
            else
            {
               param1++;
            }
            if(param3)
            {
               if(param2 && param1 < 0)
               {
                  break;
               }
               if(!param2 && param1 == _loc5_)
               {
                  break;
               }
            }
            else
            {
               param1 = (param1 + _loc5_) % _loc5_;
               if(_loc6_ == param1)
               {
                  break;
               }
            }
            if(isValidFocusCandidate(focusableCandidates[param1],param4))
            {
               _loc7_ = DisplayObject(findFocusManagerComponent(focusableCandidates[param1]));
               if(_loc7_ is IFocusManagerGroup)
               {
                  _loc8_ = IFocusManagerGroup(_loc7_);
                  _loc9_ = 0;
                  while(_loc9_ < focusableCandidates.length)
                  {
                     _loc10_ = focusableCandidates[_loc9_];
                     if(_loc10_ is IFocusManagerGroup)
                     {
                        _loc11_ = IFocusManagerGroup(_loc10_);
                        if(_loc11_.groupName == _loc8_.groupName && _loc11_.selected)
                        {
                           param1 = _loc9_;
                           break;
                        }
                     }
                     _loc9_++;
                  }
               }
               return param1;
            }
         }
         return param1;
      }
      
      private function sortFocusableObjects() : void
      {
         var _loc1_:* = null;
         var _loc2_:InteractiveObject = null;
         focusableCandidates = [];
         for(_loc1_ in focusableObjects)
         {
            _loc2_ = InteractiveObject(_loc1_);
            if(_loc2_.tabIndex && !isNaN(Number(_loc2_.tabIndex)) && _loc2_.tabIndex > 0)
            {
               sortFocusableObjectsTabIndex();
               return;
            }
            focusableCandidates.push(_loc2_);
         }
         focusableCandidates.sort(sortByDepth);
      }
      
      private function sortFocusableObjectsTabIndex() : void
      {
         var _loc1_:* = null;
         var _loc2_:InteractiveObject = null;
         focusableCandidates = [];
         for(_loc1_ in focusableObjects)
         {
            _loc2_ = InteractiveObject(_loc1_);
            if(_loc2_.tabIndex && !isNaN(Number(_loc2_.tabIndex)))
            {
               focusableCandidates.push(_loc2_);
            }
         }
         focusableCandidates.sort(sortByTabIndex);
      }
      
      private function sortByDepth(param1:InteractiveObject, param2:InteractiveObject) : Number
      {
         var index:int = 0;
         var tmp:String = null;
         var tmp2:String = null;
         var aa:InteractiveObject = param1;
         var bb:InteractiveObject = param2;
         var val1:String = "";
         var val2:String = "";
         var zeros:String = "0000";
         var a:DisplayObject = DisplayObject(aa);
         var b:DisplayObject = DisplayObject(bb);
         try
         {
            while(a != DisplayObject(form) && a.parent)
            {
               index = getChildIndex(a.parent,a);
               tmp = index.toString(16);
               if(tmp.length < 4)
               {
                  tmp2 = zeros.substring(0,4 - tmp.length) + tmp;
               }
               val1 = tmp2 + val1;
               a = a.parent;
            }
         }
         catch(se1:SecurityError)
         {
         }
         try
         {
            while(b != DisplayObject(form) && b.parent)
            {
               index = getChildIndex(b.parent,b);
               tmp = index.toString(16);
               if(tmp.length < 4)
               {
                  tmp2 = zeros.substring(0,4 - tmp.length) + tmp;
               }
               val2 = tmp2 + val2;
               b = b.parent;
            }
         }
         catch(se2:SecurityError)
         {
         }
         return val1 > val2?Number(1):val1 < val2?Number(-1):Number(0);
      }
      
      private function getChildIndex(param1:DisplayObjectContainer, param2:DisplayObject) : int
      {
         return param1.getChildIndex(param2);
      }
      
      private function sortByTabIndex(param1:InteractiveObject, param2:InteractiveObject) : int
      {
         return param1.tabIndex > param2.tabIndex?1:param1.tabIndex < param2.tabIndex?-1:int(sortByDepth(param1,param2));
      }
      
      public function get defaultButtonEnabled() : Boolean
      {
         return _defaultButtonEnabled;
      }
      
      public function set defaultButtonEnabled(param1:Boolean) : void
      {
         _defaultButtonEnabled = param1;
      }
      
      public function get nextTabIndex() : int
      {
         return 0;
      }
      
      public function get showFocusIndicator() : Boolean
      {
         return _showFocusIndicator;
      }
      
      public function set showFocusIndicator(param1:Boolean) : void
      {
         _showFocusIndicator = param1;
      }
      
      public function get form() : DisplayObjectContainer
      {
         return _form;
      }
      
      public function set form(param1:DisplayObjectContainer) : void
      {
         _form = param1;
      }
      
      public function getFocus() : InteractiveObject
      {
         var _loc1_:InteractiveObject = form.stage.focus;
         return findFocusManagerComponent(_loc1_);
      }
      
      public function setFocus(param1:InteractiveObject) : void
      {
         if(param1 is IFocusManagerComponent)
         {
            IFocusManagerComponent(param1).setFocus();
         }
         else
         {
            form.stage.focus = param1;
         }
      }
      
      public function showFocus() : void
      {
      }
      
      public function hideFocus() : void
      {
      }
      
      public function findFocusManagerComponent(param1:InteractiveObject) : InteractiveObject
      {
         var component:InteractiveObject = param1;
         var p:InteractiveObject = component;
         try
         {
            while(component)
            {
               if(component is IFocusManagerComponent && IFocusManagerComponent(component).focusEnabled)
               {
                  return component;
               }
               component = component.parent;
            }
         }
         catch(se:SecurityError)
         {
         }
         return p;
      }
      
      private function getTopLevelFocusTarget(param1:InteractiveObject) : InteractiveObject
      {
         var o:InteractiveObject = param1;
         try
         {
            while(true)
            {
               if(o != InteractiveObject(form))
               {
                  if(o is IFocusManagerComponent && IFocusManagerComponent(o).focusEnabled && IFocusManagerComponent(o).mouseFocusEnabled && UIComponent(o).enabled)
                  {
                     break;
                  }
                  o = o.parent;
                  if(o != null)
                  {
                     continue;
                  }
               }
            }
            return o;
         }
         catch(se:SecurityError)
         {
         }
         return null;
      }
   }
}