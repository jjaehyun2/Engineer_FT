/**
 * Created with IntelliJ IDEA.
 * User: elf
 * Date: 19.04.14
 * Time: 16:52
 * To change this template use File | Settings | File Templates.
 */
package kitaec.common {
import mx.controls.TextInput;

import spark.components.TextInput;

import spark.events.TextOperationEvent;

public class CommonFunc {

    public static function onChangeNumberTextInput(event:TextOperationEvent, precision:uint = 2):void
    {
        var strNumber:String = "";
        if (event.currentTarget is mx.controls.TextInput)
            strNumber = (event.currentTarget as mx.controls.TextInput).text;
        else if (event.currentTarget is spark.components.TextInput)
            strNumber = (event.currentTarget as spark.components.TextInput).text;
        else
            return;

        var ind:int = strNumber.indexOf(".");
        if (ind > -1)
        {
            var decimal:String = strNumber.substring(ind + 1);
            if (decimal.indexOf(".") > -1)
                strNumber = strNumber.substring(0, ind + 1 + decimal.indexOf("."));
            if (decimal.length > precision)
                strNumber = strNumber.substring(0, ind + 1 + precision);
        }

        if (event.currentTarget is mx.controls.TextInput)
            (event.currentTarget as mx.controls.TextInput).text = strNumber;
        else if (event.currentTarget is spark.components.TextInput)
            (event.currentTarget as spark.components.TextInput).text = strNumber;
    }
}
}