/*
Copyright (c) 2007 salesforce.com, inc.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. The name of the author may not be used to endorse or promote products
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR "AS IS" AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
package com.salesforce.results
{
    import mx.utils.ObjectProxy;
    import mx.collections.ArrayCollection;

  /**
   * Returned in the response to describeSObject(), contains detailed information on the custom or standard object
   *
   * @see http://www.salesforce.com/us/developer/docs/api/Content/sforce_api_calls_describesobjects_describesobjectresult.htm Apex Developer Guide
   *
   * @author rhess
   *
   */
    public dynamic class DescribeSObjectResult
    {
        public var activateable:Boolean;
        public var childRelationships:Array;
        public var createable:Boolean;
        public var custom:Boolean;
        public var deletable:Boolean;
        public var fields:Array;
        public var keyPrefix:String;
        public var layoutable:Boolean;
        public var label:String;
        public var labelPlural:String;
        public var mergeable:Boolean;
        public var name:String;
        public var queryable:Boolean;
        public var recordTypeInfos:Array;
        public var replicateable:Boolean;
        public var retrieveable:Boolean;
        public var searchable:Boolean;
        public var undeletable:Boolean;
        public var updateable:Boolean;
        public var urlDetail:String;
        public var urlEdit:String;
        public var urlNew:String;

        public function DescribeSObjectResult(obj:ObjectProxy=null) {
          if (obj != null)
          {
            for (var key:String in obj) {
                var val:Object = obj[key];
                if (val is ArrayCollection || val is ObjectProxy) {
                    if (key == "fields") {
                        var fieldArray:Array = new Array();
                        for (var i:int = 0;i<(val as ArrayCollection).length;i++) {
                            var field:Field = new Field((val as ArrayCollection)[i]);
                            fieldArray[field.name] = field;
                            fieldArray.length++;
                        }
                        this[key] = fieldArray;
                    } else if (key == "childRelationships") {
                        var crArray:Array = new Array();
                        var cr:ChildRelationship;

                        if ( val is ObjectProxy ) {
                            cr = new ChildRelationship(val as ObjectProxy);
                            crArray[cr.relationshipName] = cr;
                            crArray.length++;
                        } else {
                            for (var i2:int = 0;i2<(val as ArrayCollection).length;i2++) {
                                cr = new ChildRelationship((val as ArrayCollection)[i2]);
                                crArray[cr.relationshipName] = cr;
                                crArray.length++;
                            }
                        }
                        this[key] = crArray;
                    } else if (key == "recordTypeInfos") {
                        var rtArray:Array = new Array();
                        var rt:RecordTypeInfo;

                        if ( val is ObjectProxy ) {
                            rt = new RecordTypeInfo(val as ObjectProxy);
                            rtArray[rt.name] = rt;
                            rtArray.length++;
                        } else {
                            for (var i3:int=0;i3<(val as ArrayCollection).length;i3++) {
                                rt = new RecordTypeInfo((val as ArrayCollection)[i3]);
                                rtArray[rt.name] = rt;
                                rtArray.length++;
                            }
                        }
                        this[key] = rtArray;
                    }
                } else {
                    this[key] = obj[key]
                }
            }
        }
      }
    }
}