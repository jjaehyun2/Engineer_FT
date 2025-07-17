package devoron.dataui.bindings 
{
	import devoron.data.core.base.DataObject;
	import devoron.data.core.base.DataStructurObject;
	import devoron.data.core.base.IDataContainer;
	import devoron.dataui.multicontainers.table.DataContainersTable;
	import flash.utils.Dictionary;
	import org.aswing.Icon;
	import org.aswing.util.HashMap;
	/**
	 * DataUIModel
	 * @author Devoron
	 */
	public class DataUIModel implements IDataContainer
	{
		private var _dataContainerName:String;
		private var _dataContainerType:String;
		public var dataChangeComponents:Array;
		protected var _active:Boolean = false;
		public var propsAndComps:Object;
		public var compsAndProps:Dictionary;
		public var lastActiveComp:*;
		
		public var getValueFunctions:HashMap;
		public var setValueFunctions:HashMap;
		
		public var dataChangeParams:Object;
		private var _dataCollectionMode:String;
		private var _dataLiveMode:Boolean;
		private var _dataContainerIcon:Icon;
		
		public function DataUIModel(name:String, type:String, icon:Icon, liveMode:Boolean=false) 
		{
			_dataContainerName = name;
			_dataContainerType = type;
			_dataContainerIcon = icon;
			_dataLiveMode = liveMode;
			propsAndComps = new Object;
			getValueFunctions =  new HashMap;
			setValueFunctions =  new HashMap;
			compsAndProps = new Dictionary;
		}
		
		public function setDataToContainer(data:Object):void
		{
			//_active = false;
			
			//if(
			for (var prop:String in data)
			{
				if (prop == "liveSerialize")
					continue;
				var comp:* = propsAndComps[prop];
				try
				{
					var value:* = (setValueFunctions.get(comp) as Function).call(null, data[prop]);
				}
				catch (e:Error)
				{
					//Main_PRICE2000.tracer(comp);	
				}
			}
			
			dataChangeParams = data;
			//_active = true;
		}
		
		public function collectDataFromContainer(data:Object = null):Object
		{
			data = data == null ? new DataStructurObject() : data;
			data.dataName = _dataContainerName;
			data.dataType = _dataContainerType;
			data.dataLiveMode = _dataLiveMode;
			
			//dataStructurObject.active = _active;
			//dataStructurObject.useUrls = _useUrls;
			
			for (var prop:String in propsAndComps)
			{
				var comp:* = propsAndComps[prop];
				try
				{
					var value:* = (getValueFunctions.get(comp) as Function).call()
					data[prop] = value;
				}
				catch (e:Error)
				{
				}
			}
			
			//super.dispatchEvent(new Event(Event.CHANGE));
			
			return data;
		}
		
		public function collectDataFromContainerExtended(data:Object):void
		{
			if (lastActiveComp is DataContainersTable)
			{
				data[compsAndProps[lastActiveComp]] = (lastActiveComp as DataContainersTable).getData();
			}
			else
			{
				data[compsAndProps[lastActiveComp]] = (getValueFunctions.get(lastActiveComp) as Function).call();
			}
		
			//super.dispatchEvent(new Event(Event.CHANGE));
			//Main_PRICE2000.tracer("компонент " + lastActiveComp + " значение " + (getValueFunctions.get(lastActiveComp) as Function).call());
		}
		
		public function addDataComponents(comps:Array):void 
		{
			
		}
		
		public function addDataComponent(comp:*):void 
		{
			
		}
		
		/*public function get active():Boolean 
		{
			
		}
		
		public function set active(b:Boolean):Boolean 
		{
			
		}*//*public function get active():Boolean 
		{
			
		}
		
		public function set active(b:Boolean):Boolean 
		{
			
		}*/		
		/* INTERFACE devoron.data.core.base.IDataContainer */
		
		public function get dataContainerName():String 
		{
			return _dataContainerName;
		}
		
		public function get dataContainerType():String 
		{
			return _dataContainerType;
		}
		
		public function set dataContainerName(value:String):void 
		{
			_dataContainerName = value;
		}
		
		public function set dataContainerType(value:String):void 
		{
			_dataContainerType = value;
		}
		
		public function get dataContainerIcon():Icon 
		{
			return _dataContainerIcon;
		}
		
		public function set dataContainerIcon(value:Icon):void 
		{
			_dataContainerIcon = value;
		}
		
		public function get dataLiveMode():Boolean 
		{
			return _dataLiveMode;
		}
		
		public function set dataLiveMode(value:Boolean):void 
		{
			_dataLiveMode = value;
		}
		
		public function get dataCollectionMode():String 
		{
			return _dataCollectionMode;
		}
		
		public function set dataCollectionMode(value:String):void 
		{
			_dataCollectionMode = value;
		}
		
		
	}

}