/*
 * Copyright (c) 2007 Derek Wischusen
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy of 
 * this software and associated documentation files (the "Software"), to deal in 
 * the Software without restriction, including without limitation the rights to 
 * use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
 * of the Software, and to permit persons to whom the Software is furnished to do
 * so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
 * SOFTWARE.
 */


package org.as3yaml {


import org.as3commons.collections.ArrayList;
import org.as3commons.collections.framework.IIterator;
import org.as3commons.collections.framework.IList;
import org.rxr.actionscript.io.StringWriter;

/**
 * 
 * This all static class provides methods for encoding and decoding YAML.  The primary methods are YAML.encode()
 * and YAML.decode().  YAML.load() and YAML.Dump() are for advanced users.
 * 
 * @author wischusen
 * 
 */
public class YAML {
    public static const DEFAULT_SCALAR_TAG : String = "tag:yaml.org,2002:str";
    public static const DEFAULT_SEQUENCE_TAG : String = "tag:yaml.org,2002:seq";
    public static const DEFAULT_MAPPING_TAG : String = "tag:yaml.org,2002:map";

    /**
     * @private
     */    
    public static var ESCAPE_REPLACEMENTS : Object = new Object();
    
    static: {
    ESCAPE_REPLACEMENTS['\x00'] = "0";
    ESCAPE_REPLACEMENTS['\u0007'] = "a";
    ESCAPE_REPLACEMENTS['\u0008'] = "b";
    ESCAPE_REPLACEMENTS['\u0009'] = "t";
    ESCAPE_REPLACEMENTS['\n'] = "n";
    ESCAPE_REPLACEMENTS['\u000B'] = "v";
    ESCAPE_REPLACEMENTS['\u000C'] = "f";
    ESCAPE_REPLACEMENTS['\r'] = "r";
    ESCAPE_REPLACEMENTS['\u001B'] = "e";
    ESCAPE_REPLACEMENTS['"'] = "\"";
    ESCAPE_REPLACEMENTS['\\'] = "\\";
    ESCAPE_REPLACEMENTS['\u0085'] = "N";
    ESCAPE_REPLACEMENTS['\u00A0'] = "_";
    }
	
	public static function encode(obj : Object) : String
	{
		var lst : IList = new ArrayList();
		lst.add(obj);
		var yamlStr : StringWriter = new StringWriter();
		YAML.dump(lst, yamlStr,	new DefaultYAMLFactory(), new DefaultYAMLConfig());
		return yamlStr.toString();
	}

    public static function decode (yaml : String) : Object
    {
    	
    	var cfg: DefaultYAMLConfig = new DefaultYAMLConfig();
		var obj : Object = YAML.load(yaml, 
									 new DefaultYAMLFactory(),
									 cfg);
		return obj;
    }

    public static function dump (data : IList, output : StringWriter, fact : YAMLFactory, cfg : YAMLConfig) : void 
    {
        var serializer : Serializer = fact.createSerializer(fact.createEmitter(output,cfg),fact.createResolver(),cfg);
        try {
            serializer.open();
            var r : Representer = fact.createRepresenter(serializer,cfg);
            for (var iter :IIterator = data.iterator(); iter.hasNext(); ) {
                r.represent(iter.next());
            }
        } catch(e : Error) {
            throw new YAMLException(e.getStackTrace());
        } finally {
            try { 
            	serializer.close(); 
            } catch(e : Error) {/*Nothing to do in this situation*/}
        }
    }

    public static function load(io : String, fact : YAMLFactory, cfg : YAMLConfig) : Object 
    {
        var ctor : Constructor = fact.createConstructor(fact.createComposer(fact.createParser(fact.createScanner(io),cfg),fact.createResolver()));
        if(ctor.checkData()) {
            return ctor.getData();
        } else {
            return null;
        }
    }
    
}
}