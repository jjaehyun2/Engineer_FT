/**
 * Created by hyh on 5/17/16.
 */
package starlingbuilder.util.ui.inspector
{
    import starling.events.Event;

    public class TextAreaStringPropertyComponent extends TextAreaPropertyComponent
    {
        public function TextAreaStringPropertyComponent(propertyRetriever:IPropertyRetriever, param:Object, customParam:Object = null, setting:Object = null)
        {
            super(propertyRetriever, param, customParam, setting);

            _textArea.height = 100;
        }

        override protected function onTextInput(event:Event):void
        {
            var value:Object = _textArea.text;
            _oldValue = _propertyRetriever.get(_param.name);
            _propertyRetriever.set(_param.name, value);
            setChanged();
        }
    }
}