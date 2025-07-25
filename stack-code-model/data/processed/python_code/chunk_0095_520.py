package flashx.textLayout.operations
{
   import flashx.textLayout.edit.SelectionState;
   import flashx.textLayout.elements.FlowElement;
   import flashx.textLayout.formats.ITextLayoutFormat;
   import flashx.textLayout.formats.TextLayoutFormat;
   
   public class ApplyFormatToElementOperation extends FlowElementOperation
   {
       
      
      private var _format:ITextLayoutFormat;
      
      private var _undoStyles:TextLayoutFormat;
      
      public function ApplyFormatToElementOperation(operationState:SelectionState, targetElement:FlowElement, format:ITextLayoutFormat, relativeStart:int = 0, relativeEnd:int = -1)
      {
         super(operationState,targetElement,relativeStart,relativeEnd);
         this._format = format;
      }
      
      public function get format() : ITextLayoutFormat
      {
         return this._format;
      }
      
      public function set format(value:ITextLayoutFormat) : void
      {
         this._format = value;
      }
      
      override public function doOperation() : Boolean
      {
         var newFormat:TextLayoutFormat = null;
         var targetElement:FlowElement = getTargetElement();
         adjustForDoOperation(targetElement);
         this._undoStyles = new TextLayoutFormat(targetElement.format);
         if(this._format)
         {
            newFormat = new TextLayoutFormat(targetElement.format);
            newFormat.apply(this._format);
            targetElement.format = newFormat;
         }
         return true;
      }
      
      override public function undo() : SelectionState
      {
         var targetElement:FlowElement = getTargetElement();
         targetElement.format = new TextLayoutFormat(this._undoStyles);
         adjustForUndoOperation(targetElement);
         return originalSelectionState;
      }
   }
}