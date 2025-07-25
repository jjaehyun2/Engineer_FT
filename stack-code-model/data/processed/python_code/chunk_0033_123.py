package net.psykosoft.psykopaint2.core.drawing.brushes.shapes
{
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.GradientType;
	import flash.display.Shape;
	import flash.display3D.Context3D;
	import flash.display3D.textures.Texture;
	import flash.filters.ColorMatrixFilter;
	import flash.geom.Matrix;
	import flash.geom.Point;
	
	import net.psykosoft.psykopaint2.base.utils.misc.TrackedBitmapData;
	import net.psykosoft.psykopaint2.core.configuration.CoreSettings;

	public class NoisyBrushShape extends AbstractBrushShape
	{
		private var _alphaContrast : ColorMatrixFilter;
		private var _brushMap : BitmapData;
		private var _alphaMask:BitmapData;
		private const origin:Point = new Point();
		
		public function NoisyBrushShape(context3D : Context3D)
		{
			super(context3D, "noise", 1,256,2,2);
			_alphaContrast = new ColorMatrixFilter([255, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 2, -255]);
		}

		override protected function uploadBrushTexture(texture : Texture) : void
		{
			var size : Number = _textureSize;
			
			var alphaMask:Shape = new Shape();
			var m:Matrix = new Matrix();
			m.createGradientBox( size* _variationFactors[2], size * _variationFactors[3]);
			_alphaMask = new TrackedBitmapData(size, size, true, 0);
			alphaMask.graphics.beginGradientFill(GradientType.RADIAL,[0x7f7f00,0x7f7f00],[1,0],[0,255],m);
			alphaMask.graphics.drawRect(0,0,size * _variationFactors[2], size* _variationFactors[3]);
			alphaMask.graphics.endFill();
			
			m.identity();
			for ( var y:int = 0; y < _variationFactors[1]; y++ )
			{
				m.ty = y * size * _variationFactors[3];
				for ( var x:int = 0; x < _variationFactors[0]; x++ )
				{
					m.tx = x * size * _variationFactors[2];
					_alphaMask.draw(alphaMask,m);
				}
			}
			if (_brushMap) _brushMap.dispose();
			_brushMap = new TrackedBitmapData(size, size, true, 0xFF000000);
			_brushMap.perlinNoise(3, 3, 3, Math.random() * 0xffffff, false, true, 15, true);
			
			_brushMap.applyFilter(_brushMap, _brushMap.rect, origin, _alphaContrast);
			_brushMap.copyChannel(_alphaMask,_brushMap.rect,origin,8,8);
		
			//TEST: 
			CoreSettings.STAGE.addChild(new Bitmap(_brushMap));
			
			uploadMips(_textureSize, _brushMap, texture);
		}

		override protected function updateTexture(texture : Texture, automatic:Boolean = true) : void
		{
			_brushMap.perlinNoise(3, 3, 3, Math.random() * 0xffffff, false, true, 15, true);
			_brushMap.applyFilter(_brushMap, _brushMap.rect,origin, _alphaContrast);
			_brushMap.copyChannel(_alphaMask,_alphaMask.rect,origin,8,8);
			uploadMips(_textureSize, _brushMap, texture);
		}
		
		override protected function uploadNormalSpecularMap(texture : Texture) : void
		{
			_brushMap.perlinNoise(3, 3, 3, Math.random() * 0xffffff, false, true, 15, true);
			trace("uploadNormalSpecularMap");
			
			var alphaMask:Shape = new Shape();
			var m:Matrix = new Matrix();
			
			m.createGradientBox( size* _variationFactors[2], size * _variationFactors[3]);
			alphaMask.graphics.beginGradientFill(GradientType.RADIAL,[0x7f7f00,0x7f7f00],[0,1],[0,255],m);
			//alphaMask.graphics.drawRect(0,0,size * _variationFactors[2], size* _variationFactors[3]);
			alphaMask.graphics.drawCircle(size * _variationFactors[2]/2,size * _variationFactors[3]/2,Math.min(size * _variationFactors[2],size * _variationFactors[3]));
			alphaMask.graphics.endFill();
			
			
			m.identity();
			//DRAW FOR ALL VARIATIONS
			for ( var y:int = 0; y < _variationFactors[1]; y++ )
			{
				m.ty = y * size * _variationFactors[3];
				for ( var x:int = 0; x < _variationFactors[0]; x++ )
				{
					m.tx = x * size * _variationFactors[2];
					//_brushMap.floodFill(size,size,0);
					_brushMap.draw(alphaMask,m);
				}
			}
			
			//_brushMap.floodFill(size,size,0x000000);
			_brushMap.draw(alphaMask);
			
			/*TEST:
			var maskBm:Bitmap = new Bitmap(_brushMap);
			maskBm.x = 500;
			CoreSettings.STAGE.addChild(maskBm);*/
			
			
			uploadMips(_textureSize, _brushMap, texture);
		}
	}
}