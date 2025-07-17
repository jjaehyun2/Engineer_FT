package com.qcenzo.apps.album
{
	import com.adobe.utils.AGALMiniAssembler;
	import com.qcenzo.apps.album.effects.Effect;
	
	import flash.display.BitmapData;
	import flash.display3D.Context3D;
	import flash.display3D.Context3DBlendFactor;
	import flash.display3D.Context3DProgramType;
	import flash.display3D.Context3DTextureFormat;
	import flash.display3D.Context3DVertexBufferFormat;
	import flash.display3D.Program3D;
	import flash.display3D.textures.Texture;
	import flash.utils.ByteArray;

	public class Atlas
	{
		private var _cont:Context3D;
		private var _shd:Program3D;
		private var _eff:Effector;
		private var _bitmapData:BitmapData;
		private var _tex:Texture;
		private var _num:int;
		
		public function Atlas(w:int, h:int)
		{ 
			_eff = new Effector(w, h);
		}

		public function addEffect(e:Effect):void
		{
			_eff.addEffect(e);
		}
		
		public function prevEffect():void
		{
			_eff.prevEffect();
		}
		
		public function nextEffect():void
		{
			_eff.nextEffect();
		}
		
		public function add(bitmapData:BitmapData, numIcons:int):void
		{
			_bitmapData = bitmapData;
			_num = numIcons; 
		}
		
		public function setup(context:Context3D):void
		{
			_cont = context; 
			
			var agal:AGALMiniAssembler = new AGALMiniAssembler();
			var v:ByteArray = agal.assemble(Context3DProgramType.VERTEX,
				"mov vt0, vc0.y\n" +
				"ife vt0.w, vc0.z\n" +
					"mov, vt1, va1\n" +
				"els\n" +
					"ifl vc0.y, va3.x\n" +
						"mov vt1, va0\n" +
					"els\n" +
						"sub vt0.x, vc0.y, va3.x\n" +
						"ifg vt0.x, vc0.w\n" +
							"mov vt1, va1\n" +
						"els\n" +
							"div vt0.x, vt0.x, vc0.w\n" +
							"sub vt0.y, vc0.z, vt0.x\n" +
							"mul vt2, va1, vt0.x\n" +
							"mul vt1, va0, vt0.y\n" +
							"add vt1, vt1, vt2\n" +
						"eif\n" +
					"eif\n" +
				"eif\n" +
				"m44 op, vt1, vc1\n" +
				"mov v0, va2", 2);
			var f:ByteArray = agal.assemble(Context3DProgramType.FRAGMENT, 
				"tex oc, v0, fs0<2d,linear,nomip>", 2);
			_shd = _cont.createProgram();
			_shd.upload(v, f);
			
			_tex = _cont.createTexture(_bitmapData.width, _bitmapData.height, Context3DTextureFormat.BGRA_PACKED, false);
			_tex.uploadFromBitmapData(_bitmapData);
			
			_eff.setup(_cont, _num);
		}
		 
		public function render():void
		{
			_cont.setBlendFactors(Context3DBlendFactor.SOURCE_ALPHA, Context3DBlendFactor.ONE_MINUS_SOURCE_ALPHA);
			_cont.setVertexBufferAt(0, _eff.vxb0, 0, Context3DVertexBufferFormat.FLOAT_3);
			_cont.setVertexBufferAt(1, _eff.vxb1, 0, Context3DVertexBufferFormat.FLOAT_3);
			_cont.setVertexBufferAt(2, _eff.uvb, 0, Context3DVertexBufferFormat.FLOAT_2);
			_cont.setVertexBufferAt(3, _eff.vxb0, 3, Context3DVertexBufferFormat.FLOAT_1);
			_cont.setProgramConstantsFromVector(Context3DProgramType.VERTEX, 0, _eff.vector);
			_cont.setProgramConstantsFromMatrix(Context3DProgramType.VERTEX, 1, _eff.matrix, true);
			_cont.setProgram(_shd);
			_cont.setTextureAt(0, _tex);
			_cont.drawTriangles(_eff.ixb);
		}
	}
}