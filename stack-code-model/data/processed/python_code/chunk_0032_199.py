/**
 * Created by hyh on 9/14/15.
 */
package starlingbuilder.util.ui.inspector
{
    import feathers.controls.Check;

    import starling.events.Event;

    public class CheckPropertyComponent extends BasePropertyComponent
    {
        protected var _check:Check;

        public function CheckPropertyComponent(propertyRetriever:IPropertyRetriever, param:Object, customParam:Object = null, setting:Object = null)
        {
            super(propertyRetriever, param, customParam, setting);

            _check = new Check();
            applySetting(_check, UIPropertyComponentFactory.CHECK);
            addChild(_check);

            update();
            _check.addEventListener(Event.CHANGE, onCheck);
        }

        private function onCheck(event:Event):void
        {
            _oldValue = _propertyRetriever.get(_param.name);
            _propertyRetriever.set(_param.name, _check.isSelected);

            setChanged();
        }

        override public function update():void
        {
            _check.isSelected = _propertyRetriever.get(_param.name);
        }
    }
}