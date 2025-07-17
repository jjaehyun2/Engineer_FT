package com {
	import application.ApplicatonProxy;
	
	import controls.Alert.AlertPopUp;
	
	import flash.system.Capabilities;
	
	import mx.controls.TextArea;
	import mx.core.FlexGlobals;

	public class DebuggerUtils {
		private static var __use_default_trace__:Boolean = false;
		
		public static function get isDebugging():Boolean {
			return Capabilities.isDebugger;
		}
		
		public static function set __trace(message:String):void {
			if ( (FlexGlobals.topLevelApplication.appProxy is ApplicatonProxy) && (FlexGlobals.topLevelApplication.appProxy.txt_debugger is TextArea) ) {
				FlexGlobals.topLevelApplication.appProxy.txt_debugger.text += message + '\n';
			} else if (!DebuggerUtils.__use_default_trace__) {
				DebuggerUtils.__use_default_trace__ = true;
				trace(DebuggerUtils.getCallingFunctionName(new Error())+'.'+message);
				AlertPopUp.surpriseNoOkay('Cannot use that slick Debugging thing due to some kind of technical issue... Reverting to the built-in trace().','WARNING '+DebuggerUtils.getFunctionName(new Error()));
			} else {
				trace(DebuggerUtils.getCallingFunctionName(new Error())+'.'+message);
			}
		}

		public static function _trace(message:String):void {
			DebuggerUtils.__trace = message;
		}
		
		public static function explainThis(obj:Object):String {
			var ex:ObjectExplainer = new ObjectExplainer(obj);
			return ex.explainThisWay();
		}
		
		public static function assert(condition:Boolean, warning:String):int {
			DebuggerUtils.isDebugging {
				if (!condition) {
					trace("ERROR: " + warning);
					// throw if the bit is set
					throw(new Error(DebuggerUtils.getFunctionName(new Error())+"::Assert: " + warning));
					return 1;
				}
			}
			return 0;
		}

		public static function getFunctionName(e:Error):String {
			var s:String = e.getStackTrace();
			var i:int = s.indexOf("at ");
			var j:int = s.indexOf("()");
			return s.substring(i + 3, j);
		}
		
		public static function getCallingFunctionName(e:Error):String {
			var s:String = e.getStackTrace();
			var i:int = s.indexOf("at ");
			i = s.indexOf("at ", i + 3);
			if (i == -1) {
				return "caller unknown";
			}
			
			var j:int = s.indexOf("()", i + 3);
			return s.substring(i + 3, j);
		}
		
		public static function doSomething():void {
			trace(getFunctionName(new Error()));
			DebuggerUtils.doit();
		}
		
		public static function doSomethingElse():void
		{
			trace(getFunctionName(new Error()));
			DebuggerUtils.doit();
		}
		
		public static function doit():void {
			trace(getFunctionName(new Error()));
			trace("   called by", getCallingFunctionName(new Error()));
		}
	}
}