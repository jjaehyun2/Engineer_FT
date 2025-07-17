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

import flash.utils.Dictionary;

import org.as3yaml.nodes.*;

public class Resolver {
    private static var yamlImplicitResolvers : Dictionary = new Dictionary();
    private static var yamlPathResolvers : Dictionary = new Dictionary();

    private var resolverExactPaths : Array = new Array();
    private var resolverPrefixPaths : Array = new Array();

	public function Resolver() { }
    public static function addImplicitResolver(tag : String, regexp : RegExp, first : String) : void {
        var firstVal : String = (null == first)?"":first;
        for(var i:int=0,j:int=firstVal.length;i<j;i++) {
            var theC : String = firstVal.charAt(i);
            var curr : Array = yamlImplicitResolvers[theC] as Array;
            if(curr == null) {
                curr = new Array();
                yamlImplicitResolvers[theC] = curr;
            }
            curr.push([tag,regexp]);
        }
    }
    public function descendResolver(currentNode : Node, currentIndex : Object) : void {
        var exactPaths : Dictionary = new Dictionary();
        var prefixPaths : Array = new Array();
		var path : Array 
        if(null != currentNode) {
            var depth : int = resolverPrefixPaths.length;
            for(var xi:int=0; xi < resolverPrefixPaths[0].length; xi++) {
                var obj : Array = resolverPrefixPaths[0][xi] as Array;
                path = obj[0] as Array;
                if(checkResolverPrefix(depth,path, obj[1],currentNode,currentIndex)) {
                    if(path.size() > depth) {
                        prefixPaths.push([path,obj[1]]);
                    } else {
                        var resPath : Array = new Array();
                        resPath.push(path);
                        resPath.push(obj[1]);
                        exactPaths[obj[1]] = yamlPathResolvers[resPath];
                    }
                }
            }
        } else {
            for(var keyObj : Object in yamlPathResolvers) {
                var key : Array = keyObj as Array;
                path = key[0] as Array;
                var kind : Class = key[1] as Class;
                if(null == path) {
                    exactPaths[kind] = yamlPathResolvers[key];
                } else {
                    prefixPaths.push(key);
                }
            }
        }
        resolverExactPaths.unshift(exactPaths);
        resolverPrefixPaths.unshift(prefixPaths);
    }

    public function ascendResolver() : void {
        resolverExactPaths.shift();
        resolverPrefixPaths.shift();
    }

    public function checkResolverPrefix(depth : int, path : Array, kind : Class, currentNode : Node, currentIndex : Object) : Boolean {
        var check : Array = path[depth-1];
        var nodeCheck : Object = check[0];
        var indexCheck : Object = check[1];
        if(nodeCheck is String) {
            if(!currentNode.getTag() == (nodeCheck)) {
                return false;
            }
        } else if(null != nodeCheck) {
            if(!(nodeCheck).isInstance(currentNode)) {
                return false;
            }
        }
        if(indexCheck == true && currentIndex != null) {
            return false;
        }
        if(indexCheck == true && currentIndex == null) {
            return false;
        }
        if(indexCheck is String) {
            if(!(currentIndex is ScalarNode && indexCheck == ((ScalarNode(currentIndex)).getValue()))) {
                return false;
            }
        } else if(indexCheck is int) {
            if(!currentIndex == (indexCheck)) {
                return false;
            }
        }
        return true;
    }
    
    public function resolve(kind : Class, value : String, implicit : Array) : String {
        var resolvers : Array = null;
        if(kind == ScalarNode && implicit[0]) {
            if("" == (value)) {
                resolvers = yamlImplicitResolvers[""] as Array;
            } else {
                resolvers = yamlImplicitResolvers[value.charAt(0)] as Array;
            }
            if(resolvers == null) {
                resolvers = new Array();
            }
            if(yamlImplicitResolvers[null]) {
                resolvers.concat(yamlImplicitResolvers[null]);
            }
            for(var xi:int=0; xi < resolvers.length; xi++) {
                var val : Array = resolvers[xi];
                if((RegExp(val[1])).exec(value)) {
                    return val[0] as String;
                }
            }
        }
        var exactPaths : Dictionary = resolverExactPaths[0] as Dictionary;
        if(exactPaths[kind]) {
            return exactPaths[kind] as String;
        }
        if(exactPaths[null]) {
            return exactPaths[null] as String;
        }
        if(kind == ScalarNode) {
            return YAML.DEFAULT_SCALAR_TAG;
        } else if(kind == SequenceNode) {
            return YAML.DEFAULT_SEQUENCE_TAG;
        } else if(kind == MappingNode) {
            return YAML.DEFAULT_MAPPING_TAG;
        }
        return null;
    } 

    static: {
        addImplicitResolver("tag:yaml.org,2002:bool",new RegExp("^(?:yes|Yes|YES|no|No|NO|true|True|TRUE|false|False|FALSE|on|On|ON|off|Off|OFF)$"),"yYnNtTfFoO");
        addImplicitResolver("tag:yaml.org,2002:float",new RegExp("^(?:[-+]?(?:[0-9][0-9_]*)\\.[0-9_]*(?:[eE][-+][0-9]+)?|[-+]?(?:[0-9][0-9_]*)?\\.[0-9_]+(?:[eE][-+][0-9]+)?|[-+]?[0-9][0-9_]*(?::[0-5]?[0-9])+\\.[0-9_]*|[-+]?\\.(?:inf|Inf|INF)|\\.(?:nan|NaN|NAN))$"),"-+0123456789.");
        addImplicitResolver("tag:yaml.org,2002:int",new RegExp("^(?:[-+]?0b[0-1_]+|[-+]?0[0-7_]+|[-+]?(?:0|[1-9][0-9_]*)|[-+]?0x[0-9a-fA-F_]+|[-+]?[1-9][0-9_]*(?::[0-5]?[0-9])+)$"),"-+0123456789");
        addImplicitResolver("tag:yaml.org,2002:merge",new RegExp("^(?:<<)$"),"<");
        addImplicitResolver("tag:yaml.org,2002:null",new RegExp("^(?:~|null|Null|NULL| )$"),"~nN\x00");
        addImplicitResolver("tag:yaml.org,2002:timestamp",new RegExp("^(?:[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]|[0-9][0-9][0-9][0-9]-[0-9][0-9]?-[0-9][0-9]?(?:[Tt]|[ \t]+)[0-9][0-9]?:[0-9][0-9]:[0-9][0-9](?:\\.[0-9]*)?(?:[ \t]*(?:Z|[-+][0-9][0-9]?(?::[0-9][0-9])?))?)$"),"0123456789");
        addImplicitResolver("tag:yaml.org,2002:value",new RegExp("^(?:=)$"),"=");
      // The following implicit resolver is only for documentation purposes. It cannot work
      // because plain scalars cannot start with '!', '&', or '*'.
        addImplicitResolver("tag:yaml.org,2002:yaml",new RegExp("^(?:!|&|\\*)$"),"!&*");
    }
}
}