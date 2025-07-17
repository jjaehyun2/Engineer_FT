package com.qcenzo.apps.album
{
	import com.qcenzo.apps.album.effects.Effect;
	
	import flash.display.BitmapData;
	import flash.display.Stage;
	import flash.display.Stage3D;
	import flash.display3D.Context3D;
	import flash.display3D.Context3DCompareMode;
	import flash.display3D.Context3DProfile;
	import flash.display3D.Context3DRenderMode;
	import flash.events.ErrorEvent;
	import flash.events.Event;

	public class Album
	{
		private var _stage:Stage;
		private var _antia:int;
		private var _cont:Context3D;
		private var _bgv:BackgroundVideo;
		private var _atl:Atlas;

		public function Album(stage:Stage, antialias:int = 0)
		{
			_stage = stage;
			_antia = antialias;
			
			_bgv = new BackgroundVideo();
			_atl = new Atlas(stage.stageWidth, stage.stageHeight);
			
			_stage.stage3Ds[0].addEventListener(Event.CONTEXT3D_CREATE, onCreate);
			_stage.stage3Ds[0].addEventListener(ErrorEvent.ERROR, onError);
			_stage.stage3Ds[0].requestContext3D(Context3DRenderMode.AUTO, Context3DProfile.STANDARD_CONSTRAINED);
		}
		
		public function addTexture(bitmapData:BitmapData, numIcons:int):void
		{
			_atl.add(bitmapData, numIcons);
		}
		
		public function playVideo(url:String, onComplete:Function):void
		{
			_bgv.play(url, onComplete);
		}
		
		public function addEffect(e:Effect):void
		{
			_atl.addEffect(e);
		}
		
		public function prevEffect():void
		{
			_atl.prevEffect();
		}
		
		public function nextEffect():void
		{
			_atl.nextEffect();
		}
		
		private function onCreate(event:Event):void
		{
			var c:Context3D = _cont;
			 
			_cont = (event.target as Stage3D).context3D;
			_cont.configureBackBuffer(_stage.stageWidth, _stage.stageHeight, _antia);
			_cont.setDepthTest(true, Context3DCompareMode.ALWAYS);
			
			if (c == null)
			{
				_bgv.setup(_cont);
				_atl.setup(_cont);
				
				_stage.addEventListener(Event.ENTER_FRAME, onFrames);
				_stage.addEventListener(Event.RESIZE, onResize);
			}
		}
		
		private function onFrames(event:Event):void
		{
			if (_cont == null || _cont.driverInfo == "Disposed")
				return;
			_cont.clear();
			_bgv.render();
			_atl.render();
			_cont.present();
		}
		
		private function onResize(event:Event):void
		{
			if (_cont == null || _cont.driverInfo == "Disposed")
				return;
			_cont.configureBackBuffer(_stage.stageWidth, _stage.stageHeight, _antia);
		}
		
		private function onError(event:ErrorEvent):void
		{
		}
	}
}