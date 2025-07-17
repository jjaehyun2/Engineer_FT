package com.fp.templates.base
{
	import com.engine.templates.ITemplate;
	import com.engine.utils.CSVParser;
	import com.fp.templates.HeroTemplate;
	import com.fp.utils.AssetsUtil;
	
	import flash.events.Event;
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	import flash.utils.Dictionary;
	
	import starling.core.Starling;
	import starling.events.Event;
	
	public class Template implements ITemplate
	{
		public static var allData:Dictionary = new Dictionary();// 所有的模板数据
		public static var allTemps:Dictionary = new Dictionary();// 所有的模板类
		
		protected var _templateIds:Array = [];// 模板的id列表，用来指示位置用，id是唯一的找寻模板的key
		protected var _templateList:Array = [];// 模板的数据列表
		protected var _hasInit:Boolean = false;// 模板数据是否初始化过
		protected var _crtIdx:int = 0;// 模板数据当前的指针位置，默认为0
		
		protected var _id:Number;
		
		protected var _name:String;
		
		public function Template()
		{
		}
		
		private static function regTemps():void
		{
//			allTemps[BattleMapTemplate.TYPE] = new BattleMapTemplate();
			allTemps[HeroTemplate.TYPE] = new HeroTemplate();
		}
		
		public static function init():void
		{
			regTemps();
			
			var tempList:Array = AssetsUtil.tempsAppDirFile;
			var len:int = tempList.length;
			var idx:int = 0;
			var fs:FileStream = new FileStream();
			var file:File;
			
			loadFile();
			
			function loadFile():void
			{
				if(idx >= len)
				{
					fs = null;
					Starling.current.dispatchEvent(new starling.events.Event("templateInited"));
					return;
				}
				file = tempList[idx] as File;
				fs.addEventListener(flash.events.Event.COMPLETE, onOpenedFile);
				fs.openAsync(file,FileMode.READ);
			}
			
			function onOpenedFile(e:flash.events.Event):void
			{
				parserCvs();
				//				parserTempFile();
				
				fs.close();
				idx++;
				loadFile();
			}
			
			function parserCvs():void
			{
				var str:String = fs.readMultiByte(fs.bytesAvailable, File.systemCharset);
				//				trace("====\n"+str+"");
				var list:Array = CSVParser.parserToList(str);
				var tempName:String = file.name.split(".")[0];
				allData[tempName] = list;
			}
			
			function parserTempFile():void
			{
				// 这里是以后解析正式包的方法，正式包以 *.temp 为格式
			}
		}
		
		public static function getTemp(name:String):ITemplate
		{
			var temp:ITemplate = allTemps[name];
			temp.initTemps(name);
			return temp;
		}
		
		protected function get crtData():Object
		{
			return _templateList[_crtIdx];
		}
		
		public function initTemps(name:String):void
		{
			if(_hasInit)
				return;
			_templateList = Template.allData[name];
			var len:int = _templateList.length;
			for(var i:int = 0; i < len; i++)
			{
				_templateIds.push(Number(_templateList[i].id));
			}
		}
		
		public function getTempById(id:Number):ITemplate
		{
			_crtIdx = _templateIds.indexOf(id);
			_crtIdx = _crtIdx < 0 ? 0 : _crtIdx;
			return this;
		}
		
		public function getProp(id:Number, propname:String):*
		{
			_crtIdx = _templateIds.indexOf(id);
			_crtIdx = _crtIdx < 0 ? 0 : _crtIdx;
			var obj:Object = crtData;
			return obj[propname];
		}
		
		public function getCrtProp(propname:String):*
		{
			var obj:Object = crtData;
			return obj[propname];
		}
		
		public function get id():Number
		{
			return Number(crtData["id"]);
		}
		
		public function get name():String
		{
			return crtData["name"];
		}
		
		public function get hasNext():Boolean
		{
			return _crtIdx + 1 <= _templateList.length - 1;
		}
		
		public function get hasPrev():Boolean
		{
			return _crtIdx - 1 >= 0;
		}
		
		public function get nextTemp():ITemplate
		{
			if(hasNext)
				_crtIdx++;
			return this;
		}
		
		public function get prevTemp():ITemplate
		{
			if(hasPrev)
				_crtIdx--;
			return this;
		}
		
		public function get firstTemp():ITemplate
		{
			_crtIdx = 0;
			return this;
		}
		
		public function get lastTemp():ITemplate
		{
			_crtIdx = _templateList.length - 1;
			return this;
		}
		
	}
}