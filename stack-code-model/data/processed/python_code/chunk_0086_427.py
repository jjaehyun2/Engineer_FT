package net.psykosoft.psykopaint2.core.drawing.brushes
{
	import flash.display.DisplayObject;
	import flash.display3D.Context3D;
	import flash.display3D.Context3DBlendFactor;
	
	import net.psykosoft.psykopaint2.core.drawing.BrushType;
	import net.psykosoft.psykopaint2.core.drawing.brushes.shapes.AbstractBrushShape;
	import net.psykosoft.psykopaint2.core.drawing.brushes.strokes.EffectMesh;
	import net.psykosoft.psykopaint2.core.drawing.brushes.strokes.IBrushMesh;
	import net.psykosoft.psykopaint2.core.drawing.brushes.strokes.TextureSplatMesh;
	import net.psykosoft.psykopaint2.core.drawing.data.PsykoParameter;
	import net.psykosoft.psykopaint2.core.drawing.paths.SamplePoint;
	import net.psykosoft.psykopaint2.core.model.CanvasModel;
	import net.psykosoft.psykopaint2.core.model.UserPaintSettingsModel;
	import net.psykosoft.psykopaint2.core.models.PaintMode;
	import net.psykosoft.psykopaint2.core.rendering.CanvasRenderer;
	import net.psykosoft.psykopaint2.core.rendering.CopyTexture;
	import net.psykosoft.psykopaint2.core.rendering.CopyTextureWithAlpha;
	
	public class EffectBrush extends SplatBrushBase
	{
		private var _colorMatrixData:Vector.<Number> =  Vector.<Number>([1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0]);
		public function EffectBrush()
		{
			super(true);
			type = BrushType.EFFECT;
			
			param_glossiness.numberValue = .25;
			param_bumpiness.numberValue = .6;
		}

		override public function activate(view : DisplayObject, context : Context3D, canvasModel : CanvasModel, renderer:CanvasRenderer, paintSettingsModel : UserPaintSettingsModel) : void
		{
			super.activate(view, context, canvasModel, renderer, paintSettingsModel);
			if (_brushShape)
				assignBrushShape();
		}

		override protected function createBrushMesh() : IBrushMesh
		{
			return new EffectMesh();
		}

		override protected function set brushShape(brushShape : AbstractBrushShape) : void
		{
			super.brushShape = brushShape;
			if (_brushMesh)
				assignBrushShape();
			_pathManager.brushAngleRange = brushShape.rotationRange;
		}

		private function assignBrushShape() : void
		{
			EffectMesh(_brushMesh).brushTexture = _brushShape.texture;
			EffectMesh(_brushMesh).normalTexture = _brushShape.normalSpecularMap;
			EffectMesh(_brushMesh).pixelUVOffset = 0.5 / _brushShape.size;
			(_brushMesh as EffectMesh).colorMatrixData = _colorMatrixData;
			_pathManager.brushAngleRange = brushShape.rotationRange;
			
		}

		override protected function onPickColor( point : SamplePoint, pickRadius : Number, smoothFactor : Number ) : void
		{
			_appendVO.point = point;
			if ( _paintSettingsModel.colorMode == PaintMode.PHOTO_MODE )
			{
				var rsize : Number = param_sizeFactor.lowerRangeValue + param_sizeFactor.rangeValue * point.size * ( param_curvatureSizeInfluence.numberValue * (point.curvature - 1) + 1);
				if (rsize > 1) rsize = 1;
				else if (rsize < 0) rsize = 0;
				
				_appendVO.size = _maxBrushRenderSize * rsize * pickRadius;
				_colorStrategy.getColorsByVO( _appendVO, _appendVO.diagonalLength*_maxBrushRenderSize *rsize* 0.25 * smoothFactor);
			} else {
				var target:Vector.<Number> = _appendVO.point.colorsRGBA;
				target[0] = target[4] = target[8] = target[12] = _paintSettingsModel.current_r;
				target[1] = target[5] = target[9] = target[13] = _paintSettingsModel.current_g;
				target[2] = target[6] = target[10] = target[14] = _paintSettingsModel.current_b;
			}
		}

		override protected function processPoint( point : SamplePoint) : void
		{
			/*
			var minSize:Number = _maxBrushRenderSize * _sizeFactor.lowerRangeValue;
			var maxSize:Number = _maxBrushRenderSize * _sizeFactor.upperRangeValue;
			var rsize:Number = minSize + (maxSize - minSize) * point.size;
			
			if (rsize > maxSize) rsize = maxSize;
			else if (rsize < minSize) rsize = minSize;
			*/
			
				
			var rsize : Number = param_sizeFactor.lowerRangeValue + param_sizeFactor.rangeValue * point.size * ( param_curvatureSizeInfluence.numberValue * (point.curvature - 1) + 1);
			if (rsize > 1) rsize = 1;
			else if (rsize < 0) rsize = 0;
			
			_appendVO.uvBounds.x = int(Math.random() * _shapeVariations[0]) * _shapeVariations[2]; 
			_appendVO.uvBounds.y = int(Math.random() * _shapeVariations[1]) * _shapeVariations[3];
			_appendVO.size =  rsize * _maxBrushRenderSize;
			_appendVO.point = point;
			_brushMesh.append(_appendVO);
		}
		
		override protected function drawColor():void
		{
			// draw brush stroke to incremental texture
			_context.setRenderToTexture(_canvasModel.fullSizeBackBuffer, false)
			_context.clear(0, 0, 0, 0);
			_context.setBlendFactors(Context3DBlendFactor.ONE, Context3DBlendFactor.ZERO);
			CopyTexture.copy(_incrementalWorkerTexture.texture, _context);
			_context.setBlendFactors(Context3DBlendFactor.ONE, Context3DBlendFactor.ONE_MINUS_SOURCE_ALPHA);
			
			
			(_brushMesh as EffectMesh).colorTexture = _canvasModel.colorTexture;
			
			drawBrushColor();
			
			_incrementalWorkerTexture = _canvasModel.swapFullSized(_incrementalWorkerTexture);
			
			_context.setRenderToTexture(_canvasModel.colorTexture, false);
			_context.clear();
			
			_context.setBlendFactors(Context3DBlendFactor.ONE, Context3DBlendFactor.ZERO);
			
			_snapshot.drawColor();
			_context.setStencilActions();
			
			_context.setBlendFactors(param_blendModeSource.stringValue, param_blendModeTarget.stringValue);
			//_context.setBlendFactors(Context3DBlendFactor.ONE_MINUS_SOURCE_ALPHA, Context3DBlendFactor.ONE_MINUS_SOURCE_ALPHA);
			
			//CopyTexture.copy(_incrementalWorkerTexture.texture, _context, _canvasModel.usedTextureWidthRatio, _canvasModel.usedTextureHeightRatio);
			CopyTextureWithAlpha.copy(_incrementalWorkerTexture.texture, _context, param_strokeAlpha.numberValue);
			
		}
		
		public function set colorMatrixData( data:Vector.<Number> ):void
		{
			_colorMatrixData = data;
			if ( _brushMesh) (_brushMesh as EffectMesh).colorMatrixData = data;
		}
	}
}