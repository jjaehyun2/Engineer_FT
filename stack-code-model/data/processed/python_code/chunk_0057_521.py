package away3d.core.render
{
	import away3d.core.base.IRenderable;
	import away3d.core.data.RenderableListItem;
	import away3d.core.math.Matrix3DUtils;
	import away3d.core.traverse.EntityCollector;

	import com.adobe.utils.AGALMiniAssembler2;
	import com.assukar.airong.utils.Debug;

	import flash.display3D.Context3D;
	import flash.display3D.Context3DBlendFactor;
	import flash.display3D.Context3DCompareMode;
	import flash.display3D.Context3DProgramType;
	import flash.display3D.Program3D;
	import flash.display3D.textures.TextureBase;
	import flash.geom.Matrix3D;
	
	/**
	 * The PositionRenderer renders normalized position coordinates.
	 */
	public class PositionRenderer extends RendererBase
	{
		private var _program3D:Program3D;
		private var _renderBlended:Boolean;
		
		/**
		 * Creates a PositionRenderer object.
		 * @param renderBlended Indicates whether semi-transparent objects should be rendered.
		 * @param antiAlias The amount of anti-aliasing to be used
		 * @param renderMode The render mode to be used.
		 */
		public function PositionRenderer(renderBlended:Boolean = false)
		{
			// todo: request context in here
			_renderBlended = renderBlended;
			super();
		}
		
		/**
		 * @inheritDoc
		 */
		override protected function draw(entityCollector:EntityCollector, target:TextureBase):void
		{
			var item:RenderableListItem;
			var renderable:IRenderable;
			var matrix:Matrix3D = Matrix3DUtils.CALCULATION_MATRIX;
			var viewProjection:Matrix3D = entityCollector.camera.viewProjection;
			
			_context.setDepthTest(true, Context3DCompareMode.LESS);
			_context.setBlendFactors(Context3DBlendFactor.ONE, Context3DBlendFactor.ZERO);
			
			if (!_program3D)
				initProgram3D(_context);
			_context.setProgram(_program3D);
			
			item = entityCollector.opaqueRenderableHead;
			while (item) {
				renderable = item.renderable;
				renderable.activateVertexBuffer(0, _stage3DProxy);
				matrix.copyFrom(item.renderSceneTransform);
				matrix.append(viewProjection);
				_context.setProgramConstantsFromMatrix(Context3DProgramType.VERTEX, 0, viewProjection, true);
				_context.drawTriangles(renderable.getIndexBuffer(_stage3DProxy), 0, renderable.numTriangles);
				item = item.next;
			}
			
			if (!_renderBlended)
				return;
			
			item = entityCollector.blendedRenderableHead;
			while (item) {
				renderable = item.renderable;
				renderable.activateVertexBuffer(0, _stage3DProxy);
				matrix.copyFrom(item.renderSceneTransform);
				matrix.append(viewProjection);
				_context.setProgramConstantsFromMatrix(Context3DProgramType.VERTEX, 0, matrix, true);
				_context.drawTriangles(renderable.getIndexBuffer(_stage3DProxy), 0, renderable.numTriangles);
				item = item.next;
			}
		}
		
		/**
		 * Creates the depth rendering Program3D.
		 * @param context The Context3D object for which the Program3D needs to be created.
		 */
		private function initProgram3D(context:Context3D):void
		{
			var vertexCode:String;
			var fragmentCode:String;
			
			_program3D = context.createProgram();
			
			vertexCode = "m44 vt0, va0, vc0	\n" +
				"mov op, vt0		\n" +
				"rcp vt1.x, vt0.w	\n" +
				"mul v0, vt0, vt1.x	\n";
			fragmentCode = "mov oc, v0\n";
			
			_program3D.upload(new AGALMiniAssembler2(Debug.active).assemble(Context3DProgramType.VERTEX, vertexCode),
				new AGALMiniAssembler2(Debug.active).assemble(Context3DProgramType.FRAGMENT, fragmentCode));
		}
	}
}