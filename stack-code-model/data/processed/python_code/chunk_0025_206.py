package kitaec.common {
import mx.collections.ArrayCollection;
import mx.collections.IList;
import mx.utils.ObjectUtil;

public class ObjectUtil {

    public static function convertResultObject(target:Object, type:*, setofAdditionalProperties:Object = null):*
    {
        var def:* = new type();
        var props:Array = properties(target);
        for each(var property:String in props)
        {
            var camelCasedProp = property.replace(/_([a-z0-9])/g, function (g) { return g.substr(1,1).toUpperCase(); });

            try{// if readonly
                if(def[camelCasedProp] is ArrayCollection)
                {
                    continue;
                }
                def[camelCasedProp] = target[property];
            }catch(e:Error)
            {
                trace(e.getStackTrace());
            }
        }

        for (var prop:String in setofAdditionalProperties)
        {
            if(def.hasOwnProperty(prop))
            {
                try{// if readonly
                    def[prop] = setofAdditionalProperties[prop];
                }catch(e:Error)
                {
                    trace(e.getStackTrace());
                }
            }
        }
        return def;

    }

    public static function convertResultList(inList:IList, clazz:Class, setofAdditionalProperties:Object = null):ArrayCollection
    {
        var convertedList:ArrayCollection = new ArrayCollection();
        for each(var item:Object in inList)
        {
            var resultObject:Object = convertResultObject(item, clazz, setofAdditionalProperties);
            convertedList.addItem(resultObject);
        }
        return convertedList;
    }

    public static function convertRequestObject(target:Object, setofAdditionalProperties:Object = null):Object
    {
        var def:Object = new Object();
        var props:Array = properties(target);
        for each(var property:String in props)
        {
            var camelCasedProp:String = property.replace(/[A-Z0-9]/g, function (g) { return "_" + g.substr(0,1).toLowerCase(); });

            try{// if readonly
                if(def[camelCasedProp] is ArrayCollection)
                {
                    continue;
                }
                def[camelCasedProp] = target[property];
            }catch(e:Error)
            {
                trace(e.getStackTrace());
            }
        }

        for (var prop:String in setofAdditionalProperties)
        {
            try{// if readonly
                def[prop] = setofAdditionalProperties[prop];
            }catch(e:Error)
            {
                trace(e.getStackTrace());
            }
        }
        return def;
    }

    public static function convertRequestList(inList:IList, setofAdditionalProperties:Object = null):Array
    {
        var convertedList:Array = new Array();
        for each(var item:Object in inList)
        {
            var resultObject:Object = convertRequestObject(item, setofAdditionalProperties);
            convertedList.push(resultObject);
        }
        return convertedList;
    }


    public static function properties(instance:*):Array
    {
        var result:Array = [];
        var info:* = mx.utils.ObjectUtil.getClassInfo(instance);
        if ((info as Object).hasOwnProperty("properties"))
        {
            var properties:Array = info.properties;
            for each(var prop:QName in properties)
            {
                var property:String = prop.localName;
                result.push(property);
            }
        }
        return result;
    }

    public static function checkUniq(list:IList, item:Object, field:String):Boolean {
        var count:int = 0;
        var listItem:Object;
        for each(listItem in list) {
            if(listItem[field] == item[field] && listItem != item) {
                count++;
            }
        }
        return count < 1;
    }
}
}