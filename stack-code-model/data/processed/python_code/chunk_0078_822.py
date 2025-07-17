/*
*
* QueryChunk.as
*
* Copyright 2018 Yuichi Yoshii
*     吉井雄一 @ 吉井産業  you.65535.kir@gmail.com
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
*
*/

package infrastructure {
import flash.data.SQLResult;
import flash.data.SQLTableSchema;
import flash.errors.SQLError;

import infrastructure.grid.MutableData;
import infrastructure.list.Row;
import infrastructure.list.TableListData;

import mx.utils.ObjectUtil;
import mx.utils.StringUtil;

public class QueryChunk {
    public function QueryChunk() {
        m_password = "";
        m_a = new Accessor();
        m_tables = new TableListData();
        m_qList = new Vector.<String>();
        m_count = 0;
    }

    private var m_a:Accessor;
    private var m_tables:TableListData;
    private var m_qList:Vector.<String>;
    private var m_count:int;
    private var m_filePath:String;
    private var m_password:String;
    private var m_queryString:String;
    private var m_mutableData:MutableData;
    private var m_queryStringDelegate:Function;
    private var m_schemaResultDelegate:Function;
    private var m_mutableDataDelegate:Function;
    private var m_showStatusDelegate:Function;
    private var m_messageDelegate:Function;

    public function set filePath(value:String):void {
        m_filePath = value;
        if (m_filePath) {
            if ("" != m_filePath) {
                m_a.datasource = m_filePath;
                m_a.password = m_password;
                loadTables();
            }
        }
    }

    public function set password(value:String):void {
        m_password = value;
    }

    public function get queryString():String {
        return m_queryString;
    }

    public function set queryString(value:String):void {
        m_queryString = value;
        var t:String = "";
        var r:RegExp = new RegExp("^.+$", "gm");
        var m:Object = r.exec(value);
        while (null != m) {
            t += " " + StringUtil.trim(m[0]);
            m = r.exec(value);
        }
        m_qList = new Vector.<String>();
        t.split(";").forEach(function (arg:String, idx:int, org:Array):void {
            if ("" != StringUtil.trim(arg)) {
                m_qList.push(arg);
            }
        });
        m_queryStringDelegate();
    }

    public function get mutableData():MutableData {
        return m_mutableData;
    }

    public function set queryStringDelegate(arg:Function):void {
        m_queryStringDelegate = arg;
    }

    public function set schemaResultDelegate(arg:Function):void {
        m_schemaResultDelegate = arg;
    }

    public function set mutableDataDelegate(arg:Function):void {
        m_mutableDataDelegate = arg;
    }

    public function set showStatusDelegate(arg:Function):void {
        m_showStatusDelegate = arg;
    }

    public function set messageDelegate(arg:Function):void {
        m_messageDelegate = arg;
    }

    public function get alreadyBegun():Boolean {
        return m_a.alreadyBegun;
    }

    public function loadTables():void {
        try {
            m_tables = new TableListData();
            m_a.open();
            m_a.close();
            if (null == m_a.schemaResult) {
                return;
            }
            for (var i:int = 0; i < m_a.schemaResult.tables.length; ++i) {
                m_tables.addRow(m_a.schemaResult.tables[i].name, i);
            }
            m_tables.sortByName();
            m_schemaResultDelegate();
            m_showStatusDelegate("success");
        } catch (err:Error) {
            handleAnyError(err);
        }
    }

    public function tables(arg:String):TableListData {
        if ("" == arg) {
            return m_tables;
        }
        var ret:TableListData = new TableListData();
        for each (var r:Row in m_tables.rows) {
            if (r.name.indexOf(arg) >= 0) {
                ret.addRow(r.name, r.value);
            }
        }
        return ret;
    }

    public function begin():void {
        m_a.datasource = m_filePath;
        m_a.password = m_password;
        m_a.open();
        m_a.begin();
    }

    public function commit():void {
        m_a.commit();
        m_a.close();
    }

    public function rollback():void {
        m_a.rollback();
        m_a.close();
    }

    public function execute():void {
        var openNew:Boolean = !m_a.alreadyBegun;
        if (openNew) {
            open();
        }
        try {
            m_a.mutableDataDelegate = function (arg:SQLResult):void {
                fill(arg);
            };
            m_a.showStatusDelegate = m_showStatusDelegate;
            m_a.messageDelegate = m_messageDelegate;
            for each (var qs:String in m_qList) {
                m_a.queryString = qs;
                m_a.createStatement();
            }
            m_a.executeStatements();
            m_showStatusDelegate("success");
        } catch (sqlerr:SQLError) {
            handleSQLError(sqlerr);
        } catch (err:Error) {
            handleAnyError(err);
        }
        if (openNew) {
            close();
        }
    }

    public function queryWholeTable(i:int):void {
        var tInfo:SQLTableSchema = m_a.schemaResult.tables[i];
        var q:String = "SELECT \n";
        for (var j:int = 0; j < tInfo.columns.length; ++j) {
            if (0 < j) {
                q += "  , ";
            } else {
                q += "    ";
            }
            q += tInfo.columns[j].name + " \n";
        }
        q += "FROM \n    " + tInfo.name + " \n";
        queryString = q;
        executeQueryWholeTable(i);
    }

    private function open():void {
        m_a.datasource = m_filePath;
        m_a.password = m_password;
        m_a.open();
    }

    private function close():void {
        m_a.close();
    }

    private function fill(arg:SQLResult):void {
        if (arg && arg.data && 0 < arg.data.length && arg.data[0]) {
            ++m_count;
            m_mutableData = new MutableData();
            describe(arg.data[0]);
            pushResult(arg);
            m_mutableDataDelegate("Query " + (m_count).toString());
        } else {
            var m:Vector.<String> = new Vector.<String>();
            m.push("Query " + m_count.toString() + " has no records.");
            m_messageDelegate(m);
        }
    }

    private function describe(arg:Object):void {
        var info:Object = ObjectUtil.getClassInfo(arg);
        for (var i:int = 0; i < info.properties.length; ++i) {
            m_mutableData.addField(info.properties[i].localName);
        }
    }

    private function pushResult(arg:SQLResult):void {
        for (var r:int = 0; arg.data.length > r; ++r) {
            for each (var f:String in mutableData.fields()) {
                var v:String = arg.data[r][f];
                mutableData.addValue(v);
            }
            mutableData.addRow();
        }
    }

    private function executeQueryWholeTable(i:int):void {
        open();
        try {
            m_a.mutableDataDelegate = function (arg:SQLResult):void {
                fillWholeTable(arg, m_a.schemaResult.tables[i]);
            };
            m_a.showStatusDelegate = m_showStatusDelegate;
            m_a.messageDelegate = m_messageDelegate;
            m_a.queryString = queryString;
            m_a.createStatement();
            m_a.executeStatements();
            m_showStatusDelegate("success");
        } catch (sqlerr:SQLError) {
            handleSQLError(sqlerr);
        } catch (err:Error) {
            handleAnyError(err);
        }
        close();
    }

    private function fillWholeTable(arg:SQLResult, tInfo:SQLTableSchema):void {
        if (arg && arg.data && 0 < arg.data.length && arg.data[0]) {
            m_mutableData = new MutableData();
            describeTableSchema(tInfo);
            pushResult(arg);
            m_mutableDataDelegate(tInfo.name);
        } else {
            var m:Vector.<String> = new Vector.<String>();
            m.push(tInfo.name + " has no records.");
            m_messageDelegate(m);
        }
    }

    private function describeTableSchema(tInfo:SQLTableSchema):void {
        for (var i:int = 0; tInfo.columns.length > i; ++i) {
            m_mutableData.addField(tInfo.columns[i].name);
        }
    }

    private function handleSQLError(err:SQLError):void {
        var m:Vector.<String> = new Vector.<String>();
        m.push(err.errorID.toString());
        m.push(err.operation);
        m.push(err.message);
        m.push(err.getStackTrace());
        m_showStatusDelegate("failure");
        m_messageDelegate(m);
    }

    private function handleAnyError(err:Error):void {
        var m:Vector.<String> = new Vector.<String>();
        m.push(err.message);
        m.push(err.getStackTrace());
        m_showStatusDelegate("failure");
        m_messageDelegate(m);
    }
}
}