package com {
	import flash.display.DisplayObject;
	
	import mx.collections.ArrayCollection;

	public class Generator {
		public var parent:*;
		public var dataSource:*;
		public var children:Array = [];
		
		private var _callback:Function;
		
		public function Generator(datasource:*,callback:Function=null,doIterate:Boolean=true) {
			var _this:* = this;
			this.children = [];
			this.parent = parent;
			this.dataSource = datasource;
			this._callback = callback;
			
			var gen:Generator;
			
			function iterate_over_array(ar:Array):void {
				if (doIterate) {
					for (i in ar) {
						anItem = ar[i];
						//trace(DebuggerUtils.getFunctionName(new Error())+'.1 --> ('+i+') of ('+ar.length+') anItem='+anItem.toString());
						if (_this._callback is Function) {
							try { _this._callback(_this,anItem) } catch (err:Error) {
								//trace(DebuggerUtils.getFunctionName(new Error())+'.ERROR.1 '+err.toString()+', '+err.getStackTrace());
							}
						}
						gen = new Generator(anItem,_this._callback);
						gen.parent = _this;
						_this.children.push(gen);
					}
				} else {
					if (_this._callback is Function) {
						try { _this._callback(_this,ar) } catch (err:Error) {
							//trace(DebuggerUtils.getFunctionName(new Error())+'.ERROR.2 '+err.toString()+', '+err.getStackTrace());
						}
					}
				}
			}
			
			var i:String;
			if (this.dataSource is Array) {
				iterate_over_array(this.dataSource);
			} else if (this.dataSource is ArrayCollection) {
				iterate_over_array(this.dataSource.source);
			} else if (this.dataSource is DisplayObject) {
				iterate_over_array(ObjectUtils.getChildren(this.dataSource));
			} else if (this.dataSource is String) {
				// Do Nothing - this is a leaf node.
			} else { // Walk the object...
				var keys:Array = [];
				try { keys = ObjectUtils.keys(this.dataSource); }
					catch (err:Error) {}
				if (keys.length > 0) {
					var anItem:*;
					if ( (doIterate) && (this._callback is Function) ) {
						try { this._callback(this,this.dataSource) } catch (err:Error) {
							//trace(DebuggerUtils.getFunctionName(new Error())+'.ERROR.3 '+err.toString());
						}
					}
					var dp:* = this.dataSource;
					if (this.dataSource['children']) {
						dp = this.dataSource['children'];
						if ( (!doIterate) && (dp is Array) && (this._callback is Function) ) {
							try { this._callback(this,dp) } catch (err:Error) {
								//trace(DebuggerUtils.getFunctionName(new Error())+'.ERROR.4 '+err.toString());
							}
						}
					}
					for (i in dp) {
						anItem = dp[i];
						if ( (doIterate) && (this._callback is Function) ) {
							try { this._callback(this,anItem) } catch (err:Error) {
								//trace(DebuggerUtils.getFunctionName(new Error())+'.ERROR.5 '+err.toString());
							}
						}
						gen = new Generator(anItem,this._callback,doIterate);
						gen.parent = this;
						this.children.push(gen);
					}
				}
			}
		}
		
		public function walk(callback:Function=null):void {
			if (callback is Function) {
				try { callback(this) } catch (err:Error) {
					//trace(DebuggerUtils.getFunctionName(new Error())+'.ERROR.1 '+err.toString());
				}
			}
			if (this.children is Array) {
				for (var i:int = 0; i < this.children.length; i++) {
					this.children[i].walk(callback);
				}
			}
		}
	}
}