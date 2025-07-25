/*
 * Copyright 2014 Kokorin Denis
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package ru.kokorin.astream.mapper.handler {
import org.spicefactory.lib.reflect.Property;

import ru.kokorin.astream.AStreamRegistry;
import ru.kokorin.astream.converter.Converter;
import ru.kokorin.astream.ref.AStreamRef;

public class TextHandler extends BaseHandler {
    private var propertyName:String;
    private var converter:Converter;

    public function TextHandler(property:Property, registry:AStreamRegistry) {
        super("", NodeType.TEXT);
        this.propertyName = property.name;
        this.converter = registry.getConverterForProperty(property.owner, property.name);
    }

    override public function toXML(parentInstance:Object, parentXML:XML, ref:AStreamRef):void {
        const value:Object = parentInstance[propertyName];
        if (value != null && converter != null) {
            parentXML.text()[0] = converter.toString(value);
        }
    }

    override public function fromXML(parentXML:XML, parentInstance:Object, deref:AStreamRef):void {
        const textValue:XML = parentXML.text()[0];
        var value:Object = null;
        if (textValue != null && converter != null) {
            value = converter.fromString(String(textValue));
        }
        parentInstance[propertyName] = value;
    }
}
}