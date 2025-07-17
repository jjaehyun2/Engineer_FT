package com.base.module
{
	import com.base.events.DispImpl;
	import com.base.module.events.ModuleEvent;
	import com.base.module.interfaces.IBlock;
	import com.base.module.interfaces.IModule;
	
	import utils.struct.MYHashMap;
	
	/**
	 * 模块模型基类实现
	 * @author movinliao
	 * 
	 */
	public class ModuleBase extends DispImpl implements IModule
	{
		private var _blocks: MYHashMap = new MYHashMap();
		protected var _api: * = null;
		protected var _inited: Boolean = false;
		
		public function ModuleBase(key:String)
		{
			super(key);
		}
		
		public function init(api:*):void
		{
			_api = api;
			
			var thisObj: IModule = this;
			_blocks.eachValue(function(item: IBlock): Boolean{
				item.init(thisObj);
				return false;
			});
			
			_inited = true;
			
			dispatchEvent(ModuleEvent.INIT);
		}
		
		public function destroy():void
		{
			dispatchEvent(ModuleEvent.DESTROY);
			
			_blocks.eachValue(function(item: IBlock): Boolean{
				item.destroy();
				return false;
			}, false);
			_blocks.clear();
			
			_api = null;
			_blocks = null;
		}
		
		public function addBlock(key:String, item:IBlock):void
		{
			if(!item || _blocks.containsKey(key))
			{
				return;
			}
			
			if(_inited)
			{
				item.init(this);
			}
			
			_blocks.put(key, item);
			dispatchEvent(ModuleEvent.ADD, key);
		}
		
		public function removeBlock(key:String):void
		{
			dispatchEvent(ModuleEvent.REMOVE, key);
			
			if(!_blocks.containsKey(key))
			{
				return;
			}
			var item: IBlock = _blocks.remove(key);
			item.destroy();
		}
		
		public function block(key:String):IBlock
		{
			return _blocks.getValue(key);
		}
		
		public function hasBlock(key:String):Boolean
		{
			return _blocks.containsKey(key);
		}
		
		public function start():void
		{
			super.paused = false;
			_blocks.eachValue(function(item: IBlock): Boolean{
				item.start();
				return false;
			});
			
			dispatchEvent(ModuleEvent.START);
		}
		
		public function stop():void
		{
			dispatchEvent(ModuleEvent.STOP);
			
			super.paused = true;
			_blocks.eachValue(function(item: IBlock): Boolean{
				item.stop();
				return false;
			}, false);
		}
		
		public function get api():*
		{
			return _api;
		}
		
		public function get keys():Array
		{
			return _blocks.keys();
		}
		
		public function addBlockListener(blockKey:String, key:String, 
		   listener:Function, priority:int=0):void
		{
			if(block(blockKey))
			{
				block(blockKey).addListener(key, listener, priority);
			}
		}
		
		public function removeBlockListener(blockKey:String, key:String, 
		  listener:Function, priority:int=0):void
		{
			if(block(blockKey))
			{
				block(blockKey).removeListener(key, listener, priority);
			}
		}
		
		public function get inited():Boolean
		{
			return _inited;
		}
		
		public function log(content:String, priority:*):void
		{
		}
		/////////////////////////////////////////////////////
		protected function dispatchEvent(key: String, data: * = null, priority: * = 0): void
		{
			var event: ModuleEvent = new ModuleEvent(key);
			event.eventData = data;
			event.priority = priority;
			dispatch(key, event);
		}
	}
}