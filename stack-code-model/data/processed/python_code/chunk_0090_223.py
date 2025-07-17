package com.qcenzo.apps.album
{
	import com.adobe.utils.AGALMiniAssembler;
	
	import flash.display3D.Context3D;
	import flash.display3D.Context3DBlendFactor;
	import flash.display3D.Context3DProgramType;
	import flash.display3D.Context3DVertexBufferFormat;
	import flash.display3D.IndexBuffer3D;
	import flash.display3D.Program3D;
	import flash.display3D.VertexBuffer3D;
	import flash.display3D.textures.VideoTexture;
	import flash.events.AsyncErrorEvent;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.events.NetStatusEvent;
	import flash.net.NetConnection;
	import flash.net.NetStream;
	import flash.utils.ByteArray;

	public class BackgroundVideo
	{
		private const COMPLETE:String = "NetStream.Play.Complete";
		
		private var _url:String;
		private var _oncomp:Function;
		private var _ns:NetStream;
		private var _nc:NetConnection;
		private var _tex:VideoTexture;
		private var _ready:Boolean;
		private var _cont:Context3D;
		private var _ixb:IndexBuffer3D;
		private var _vxb:VertexBuffer3D;
		private var _shd:Program3D;

		public function BackgroundVideo()
		{
			_nc = new NetConnection();
			_nc.connect(null);
			
			_ns = new NetStream(_nc);
			_ns.addEventListener(IOErrorEvent.IO_ERROR, onIOError);
			_ns.addEventListener(AsyncErrorEvent.ASYNC_ERROR, onAError);
			_ns.addEventListener(NetStatusEvent.NET_STATUS, onStat);
			_ns.client = {};
		}
		
		public function setup(context:Context3D):void
		{
			_cont = context;
			
			var agal:AGALMiniAssembler = new AGALMiniAssembler();
			var v:ByteArray = agal.assemble(Context3DProgramType.VERTEX,
				"mov op, va0\n" +
				"mov v0, va1");
			var f:ByteArray = agal.assemble(Context3DProgramType.FRAGMENT, 
				"tex oc, v0, fs0<2d,linear,nomip>");
			_shd = _cont.createProgram();
			_shd.upload(v, f);
			
			_vxb = _cont.createVertexBuffer(4, 4);
			_vxb.uploadFromVector(Vector.<Number>([-1, 1, 0, 0, 1, 1, 1, 0, -1, -1, 0, 1, 1, -1, 1, 1]), 0, 4);
			
			_ixb = _cont.createIndexBuffer(6);
			_ixb.uploadFromVector(Vector.<uint>([0, 1, 2, 2, 1, 3]), 0, 6);
			
			_tex = _cont.createVideoTexture();
			_tex.addEventListener(Event.TEXTURE_READY, onReady); 
			_tex.attachNetStream(_ns);
			
			if (_url != null)
				_ns.play(_url);
		}
		
		public function play(url:String, onComplete:Function):void
		{
			_oncomp = onComplete;
			
			if (_tex == null)
				_url = url;
			else
			{
				_ready = false;
				_tex.addEventListener(Event.TEXTURE_READY, onReady); 
				_ns.play(url);
			}
		}
		
		public function render():void
		{
			if (_ready)
			{
				_cont.setBlendFactors(Context3DBlendFactor.ONE, Context3DBlendFactor.ZERO);
				_cont.setVertexBufferAt(0, _vxb, 0, Context3DVertexBufferFormat.FLOAT_2);
				_cont.setVertexBufferAt(1, _vxb, 2, Context3DVertexBufferFormat.FLOAT_2);
				_cont.setVertexBufferAt(2, null);
				_cont.setVertexBufferAt(3, null);
				_cont.setProgram(_shd);
				_cont.setTextureAt(0, _tex);
				_cont.drawTriangles(_ixb);
			}
		}
		
		public function onPlayStatus(data:Object):void
		{
			if (data.code == COMPLETE && _oncomp != null)
				_oncomp();
		}
		
		private function onReady(event:Event):void
		{
			_tex.removeEventListener(Event.TEXTURE_READY, onReady);
			_ready = true;
		}
		
		private function onStat(event:NetStatusEvent):void 
		{
		}
		
		private function onIOError(event:IOErrorEvent):void 
		{
		}
		
		private function onAError(event:AsyncErrorEvent):void
		{
		}
	}
}