package  {
	import flash.events.NetStatusEvent;
	import flash.net.NetStream;
	import haxe.Log;
	import flash.net.NetConnection;
	import flash.display.Sprite;
	import flash.media.Video;
	import flash.Boot;
	public class VideoPlayer extends Sprite {
		public function VideoPlayer(video_url : String) : void { if( !Boot.skip_constructor ) {
			super();
			this._video = new Video();
			this._connect_nc = new NetConnection();
			this._connect_nc.connect(null);
			this._stream_ns = new NetStream(this._connect_nc);
			this._stream_ns.client = this;
			this._stream_ns.addEventListener(NetStatusEvent.NET_STATUS,this.netStatusHandler);
			this.addChild(this._video);
			this._video.attachNetStream(this._stream_ns);
			this._stream_ns.play(video_url);
		}}
		
		protected var _video : Video;
		protected var _connect_nc : NetConnection;
		protected var _stream_ns : NetStream;
		protected var _videodata : *;
		public function setDimensions(w : Number,h : Number,stretch : Boolean = false) : void {
			var aspect_ratio : Number = this._videodata.width / this._videodata.height;
			var new_w : Number = w;
			var new_h : Number = ((stretch)?h:w / aspect_ratio);
			if(new_h > this.stage.stageHeight) {
				new_w = w * (this.stage.stageHeight / new_h);
				new_h = this.stage.stageHeight;
			}
			if(new_w > this.stage.stageWidth) {
				new_h = h * (this.stage.stageWidth / new_w);
				new_w = this.stage.stageWidth;
			}
			this._video.height = new_h;
			this._video.width = new_w;
		}
		
		public function netStatusHandler(event : NetStatusEvent) : void {
			if(event.info.code == "NetStream.Play.FileStructureInvalid") {
				Log.trace("The MP4's file structure is invalid.",{ fileName : "VideoPlayer.hx", lineNumber : 46, className : "VideoPlayer", methodName : "netStatusHandler"});
			}
			else if(event.info.code == "NetStream.Play.NoSupportedTrackFound") {
				Log.trace("The MP4 doesn't contain any supported tracks",{ fileName : "VideoPlayer.hx", lineNumber : 48, className : "VideoPlayer", methodName : "netStatusHandler"});
			}
		}
		
		public function onMetaData(data : *) : void {
			this._videodata = data;
			this.setDimensions(this._videodata.width,this._videodata.height);
		}
		
	}
}