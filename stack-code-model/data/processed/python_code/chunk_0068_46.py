/**
 */
package away3d.filters.tasks
{
	import com.adobe.utils.*;
	
	import away3d.cameras.*;
	import away3d.core.managers.*;
	import away3d.debug.*;
	import away3d.errors.*;
	
	import flash.display3D.*;
	import flash.display3D.textures.*;
	
	public class Filter3DTaskBase
	{
		protected var _mainInputTexture:TextureBase;
		protected var _mainInputTextureContext:Context3D;
		protected var _scaledTextureWidth:int = -1;
		protected var _scaledTextureHeight:int = -1;
		protected var _textureWidth:int = -1;
		protected var _textureHeight:int = -1;
		protected var _textureDimensionsInvalid:Boolean = true;
		private var _program3DInvalid:Boolean = true;
		private var _program3D:Program3D;
		private var _program3DContext:Context3D;
		private var _target:TextureBase;
		private var _requireDepthRender:Boolean;
		protected var _textureScale:int = 0;
		
		public function Filter3DTaskBase(requireDepthRender:Boolean = false)
		{
			_requireDepthRender = requireDepthRender;
		}
		
		/**
		 * The texture scale for the input of this texture. This will define the output of the previous entry in the chain
		 */
		public function get textureScale():int
		{
			return _textureScale;
		}
		
		public function set textureScale(value:int):void
		{
			if (_textureScale == value)
				return;
			_textureScale = value;
			_scaledTextureWidth = _textureWidth >> _textureScale;
			_scaledTextureHeight = _textureHeight >> _textureScale;
			_textureDimensionsInvalid = true;
		}
		
		public function get target():TextureBase
		{
			return _target;
		}
		
		public function set target(value:TextureBase):void
		{
			_target = value;
		}
		
		public function get textureWidth():int
		{
			return _textureWidth;
		}
		
		public function set textureWidth(value:int):void
		{
			if (_textureWidth == value)
				return;
			_textureWidth = value;
			_scaledTextureWidth = _textureWidth >> _textureScale;
			if(_scaledTextureWidth < 1) _scaledTextureWidth = 1;
			_textureDimensionsInvalid = true;
		}
		
		public function get textureHeight():int
		{
			return _textureHeight;
		}
		
		public function set textureHeight(value:int):void
		{
			if (_textureHeight == value)
				return;
			_textureHeight = value;
			_scaledTextureHeight = _textureHeight >> _textureScale;
			if(_scaledTextureHeight < 1) _scaledTextureHeight = 1;
			_textureDimensionsInvalid = true;
		}
		
		public function getMainInputTexture(stage:Stage3DProxy):TextureBase
		{
			if(stage.context3D!=_mainInputTextureContext){
				_textureDimensionsInvalid = true;
			}

			if (_textureDimensionsInvalid)
				updateTextures(stage);
			
			return _mainInputTexture;
		}
		
		public function dispose():void
		{
			if (_mainInputTexture)
				_mainInputTexture.dispose();
			if (_program3D)
				_program3D.dispose();
			_program3DContext = null;
		}
		
		protected function invalidateProgram3D():void
		{
			_program3DInvalid = true;
		}
		
		protected function updateProgram3D(stage:Stage3DProxy):void
		{
			if (_program3D)
				_program3D.dispose();
			_program3DContext = stage.context3D;
			_program3D = _program3DContext.createProgram();
			_program3D.upload(new AGALMiniAssembler(Debug.active).assemble(Context3DProgramType.VERTEX, getVertexCode()),
				new AGALMiniAssembler(Debug.active).assemble(Context3DProgramType.FRAGMENT, getFragmentCode()));
			_program3DInvalid = false;
		}
		
		protected function getVertexCode():String
		{
			return "mov op, va0\n" +
				"mov v0, va1\n";
		}
		
		protected function getFragmentCode():String
		{
			throw new AbstractMethodError();
			return null;
		}
		
		protected function updateTextures(stage:Stage3DProxy):void
		{
			if (_mainInputTexture)
				_mainInputTexture.dispose();
			_mainInputTextureContext = stage.context3D;
			_mainInputTexture = _mainInputTextureContext.createTexture(_scaledTextureWidth, _scaledTextureHeight, Context3DTextureFormat.BGRA, true);
			
			_textureDimensionsInvalid = false;
		}
		
		public function getProgram3D(stage3DProxy:Stage3DProxy):Program3D
		{
			if(_program3DContext != stage3DProxy.context3D) {
				_program3DInvalid = true;
			}

			if (_program3DInvalid)
				updateProgram3D(stage3DProxy);
			return _program3D;
		}
		
		public function activate(stage3DProxy:Stage3DProxy, camera:Camera3D, depthTexture:Texture):void
		{
		}
		
		public function deactivate(stage3DProxy:Stage3DProxy):void
		{
		}
		
		public function get requireDepthRender():Boolean
		{
			return _requireDepthRender;
		}
	}
}