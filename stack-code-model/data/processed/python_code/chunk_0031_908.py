package org.avManager.model.data
{
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Loader;
	import flash.display.LoaderInfo;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.net.URLRequest;
	
	import mx.collections.ArrayCollection;
	import mx.controls.Alert;
	
	import org.avManager.model.ActressManager;
	import org.avManager.model.ClassificationManager;
	import org.libra.log4a.Logger;

	public final class VideoData extends SQLData
	{
		
		private var _videoID:String;
		
		private var _date:Date;
		
		private var _cover:BitmapData;
		
		private var _coverSub:BitmapData;
		
		private var _classificationList:Vector.<ClassificationData> = new Vector.<ClassificationData>();
		
		private var _classification:Array = [];
		
		private var _torrent:String = null;
		
		private var _actress:String = null;
		
		private var _initActress:Boolean = false;
		
		[Bindable]
		private var _actressDataList:ArrayCollection = new ArrayCollection;
		
		[Bindable]
		private var _torrentList:ArrayCollection = new ArrayCollection();
		
		public function VideoData(id:int)
		{
			super(id);
		}
		
		public function setCoverURL(url:String):void{
			var loader:Loader = new Loader();
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE, onLoadCoverCompleted);
			loader.contentLoaderInfo.addEventListener(IOErrorEvent.IO_ERROR, onLoadIOError);
			loader.load(new URLRequest(url));
			
			var urlSmall:String = url.replace("l.jpg","s.jpg");
			var loader1:Loader = new Loader();
			loader1.contentLoaderInfo.addEventListener(Event.COMPLETE, onLoadCoverSubCompleted);
			loader1.contentLoaderInfo.addEventListener(IOErrorEvent.IO_ERROR, onLoadIOError);
			loader1.load(new URLRequest(urlSmall));
		}
		
		private function onLoadIOError(event:IOErrorEvent):void
		{
			var loaderInfo:LoaderInfo = event.target as LoaderInfo;
			loaderInfo.removeEventListener(IOErrorEvent.IO_ERROR, onLoadIOError);
			loaderInfo.removeEventListener(Event.COMPLETE, onLoadCoverCompleted);
			Logger.error(event.text);
			Alert.show(event.text);
		}
		
		private function onLoadCoverCompleted(event:Event):void
		{
			var loaderInfo:LoaderInfo = event.target as LoaderInfo;
			loaderInfo.removeEventListener(IOErrorEvent.IO_ERROR, onLoadIOError);
			loaderInfo.removeEventListener(Event.COMPLETE, onLoadCoverCompleted);
			
			this.cover = (loaderInfo.content as Bitmap).bitmapData;
			Logger.info(this._videoID + "的封面下好了");
		}
		
		private function onLoadCoverSubCompleted(event:Event):void
		{
			var loaderInfo:LoaderInfo = event.target as LoaderInfo;
			loaderInfo.removeEventListener(IOErrorEvent.IO_ERROR, onLoadIOError);
			loaderInfo.removeEventListener(Event.COMPLETE, onLoadCoverSubCompleted);
			
			this.coverSub = (loaderInfo.content as Bitmap).bitmapData;
			Logger.info(this._videoID + "的子封面下好了");
		}
		
		public function addClassification(classification:ClassificationData):void{
			for each(var c:ClassificationData in this._classificationList){
				if(c == classification) return;
			}
			_classificationList.push(classification);
			this._classification.push(classification.id);
		}
		
		public function getClassificationStr():String{
			var s:String = "";
			for(var i:int = 0;i < _classificationList.length; i++){
				s += s ? " " + _classificationList[i].name : _classificationList[i].name; 
			}
			return s;
		}
		
		public function hasClassification(classificationName:String):Boolean{
			for(var i:int = 0;i < _classificationList.length; i++){
				if(_classificationList[i].name == classificationName) return true; 
			}
			return false;
		}
		
		public function initActress():void{
			if(!this._initActress){
				if(_actress){
					_initActress = true;
					var a:Array = _actress.split(" ");
					var actressData:ActressData = null;
					for(var i:int = 0; i < a.length; i++){
						actressData = ActressManager.instance.getActressByName(a[i]);
						if(actressData){
							_actressDataList.addItem(actressData);					
						}
					}
				}
			}
		}
		
		[SQLData(cloName="VIDEO_ID")]
		public function get videoID():String
		{
			return _videoID;
		}

		[Bindable]
		public function set videoID(value:String):void
		{
			_videoID = value;
			this.needUpdate = true;
		}

		[SQLData(cloName="DATE")]
		public function get date():Date
		{
			return _date;
		}
		
		[Bindable]
		public function set date(value:Date):void
		{
			_date = value;
			this.needUpdate = true;
		}

		[SQLData(type="BitmapData",cloName="COVER")]
		public function get cover():BitmapData
		{
			return _cover;
		}
		
		[Bindable]
		public function set cover(value:BitmapData):void
		{
			_cover = value;
			this.needUpdate = true;
		}

		[SQLData(type="BitmapData",cloName="COVER_SUB")]
		public function get coverSub():BitmapData
		{
			return _coverSub;
		}
		
		[Bindable]
		public function set coverSub(value:BitmapData):void
		{
			_coverSub = value;
			this.needUpdate = true;
		}

		[SQLData(type="Array",cloName="CLASSIFICATION")]
		public function get classification():Array
		{
			return _classification;
		}

		public function set classification(value:Array):void
		{
			_classification = value;
			_classificationList.length = 0;
			for each(var i:int in _classification){
				_classificationList.push(ClassificationManager.instance.getClassificationByID(i));
			}
			this.needUpdate = true;
		}
	
		[SQLData(cloName="TORRENT")]
		public function get torrent():String
		{
			return _torrent;
		}

		public function set torrent(value:String):void
		{
			_torrent = value;
			_torrentList.source = _torrent ? _torrent.split(" ") : [];
			this.needUpdate = true;
		}

		public function get torrentList():ArrayCollection
		{
			return _torrentList;
		}
		
		[Bindable]
		public function set torrentList(value:ArrayCollection):void
		{
//			_torrentList = value;
		}

		[SQLData(cloName="ACTRESS")]
		public function get actress():String
		{
			return _actress;
		}
	
		[Bindable]
		public function set actress(value:String):void
		{			
			_actress = value ? value : '';
			var a:Array = _actress.split(" ");
			var l:int = a.length;
			while(--l > -1){
				if(a[l] == ""){
					a.splice(l, 1);
				}
			}
			_actress = a.join(" ");
			this.needUpdate = true;
			_actressDataList.removeAll();
		}

		public function get actressDataList():ArrayCollection
		{
			return _actressDataList;
		}

		[Bindable]
		public function set actressDataList(value:ArrayCollection):void
		{
//			return _actressDataList;
		}

	}
}