package net.psykosoft.psykopaint2.core.drawing.brushes.strokes
{
	import away3d.core.math.PoissonLookup;

	import flash.display3D.Context3D;
	import flash.display3D.Context3DProgramType;
	import flash.display3D.Context3DVertexBufferFormat;
	import flash.display3D.VertexBuffer3D;
	import flash.display3D.textures.TextureBase;
	import flash.geom.Rectangle;

	import net.psykosoft.psykopaint2.core.configuration.CoreSettings;
	
	import net.psykosoft.psykopaint2.core.drawing.paths.SamplePoint;
	import net.psykosoft.psykopaint2.core.model.CanvasModel;
	import net.psykosoft.psykopaint2.core.intrinsics.FastBuffer;
	

	public class TextureSplatMesh extends AbstractBrushMesh
	{
		protected static const NUM_POISSON_SAMPLES : uint = 5;
		private static const NORMAL_BLUR_SAMPLE_RANGE : uint = 3;

		protected var _normalSpecularFragmentData : Vector.<Number>;
		protected var _normalSpecularVertexData : Vector.<Number>;
		protected var _numFragmentRegisters : Number;

		protected static var _tmpData:Vector.<Number>;

		public function TextureSplatMesh()
		{
			super();

			_normalSpecularFragmentData = new <Number>[.5, 1/(NUM_POISSON_SAMPLES + 1), 50, (NUM_POISSON_SAMPLES+1) *.5 ];
			_normalSpecularVertexData = new <Number>[0, 0, 0, 1, .5, -.5, 0, 1, 0, 0, 0, 0 ,0,0,0,0];

			if (!_tmpData )
			{
				_tmpData = new Vector.<Number>(32,true);
			}

			initPoisson();
		}

		private function initPoisson() : void
		{
			var fragmentIndex : uint = 4;
			var points : Vector.<Number> = PoissonLookup.getDistribution(NUM_POISSON_SAMPLES);
			var pointIndex : int = 0;
			var rangeX : Number = NORMAL_BLUR_SAMPLE_RANGE/CoreSettings.STAGE_WIDTH;
			var rangeY : Number = NORMAL_BLUR_SAMPLE_RANGE/CoreSettings.STAGE_HEIGHT;
			for (var i : int = 0; i < NUM_POISSON_SAMPLES; ++i) {
				_normalSpecularFragmentData[fragmentIndex] = points[pointIndex] * rangeX;
				_normalSpecularFragmentData[fragmentIndex + 1] = points[pointIndex + 1] * rangeY;
				fragmentIndex += 2;
				pointIndex += 2;
			}
			_numFragmentRegisters = Math.ceil(fragmentIndex/4);
			// expand if necessary
			_normalSpecularFragmentData.length = _numFragmentRegisters * 4;
		}

		
		/**
		 * The append() method is responsible for adding the actual textured triangles
		 * that will be rendered on the GPU. In the case of the TextureSplatMesh
		 * we are adding scaled and rotated Quads, meaning 2 triangles are added
		 * each time. 
		 */
		override public function append( appendVO:StrokeAppendVO ):void
		{
			//check for maximum vertex count
			if ( _numVertices >= 65531 ) return;
			
			// The following 3 values tell us which part of the AbstractBrushShape's texture should be used:
			
			// uvBounds contains the uv coordinates of the table cell that is being drawn
			var uvBounds:Rectangle = appendVO.uvBounds;
			
			// baseAngle is the diagonal angle of the cell, this is required to calculate 
			// the 4 corner points of the quad
			var baseAngle:Number = appendVO.diagonalAngle; //Math.atan2(uvBounds.height,uvBounds.width);
			
			// halfSize is the distance of the center of the cell to the corners, again
			// this value is required for the calculation of the 4 corners of the quad
			var halfSize : Number = appendVO.size * appendVO.diagonalLength * 0.5;//appendVO.size * Math.SQRT1_2;
			
			// angle is the rotation value of the SamplePoint 
			var angle : Number = appendVO.point.angle;
			
			// 4 intermediate values required for the corner calculation:
			var cos1 : Number = halfSize * Math.cos(  baseAngle + angle);
			var sin1 : Number = halfSize * Math.sin(  baseAngle + angle);
			var cos2 : Number = halfSize * Math.cos( -baseAngle + angle);
			var sin2 : Number = halfSize * Math.sin( -baseAngle + angle);


			var point:SamplePoint = appendVO.point;
			var pnx:Number = point.x;
			var pny:Number = point.y;
			var bumpFactors : Vector.<Number> = point.bumpFactors;

			var diffX : Number;
			var diffU : Number;

			// data will accumulate all the vertex data that is sent to the GPU
			// for performance reasons we reuse the same Vector each time
			var data:Vector.<Number> = _tmpData;

			var ox:Number = appendVO.quadOffsetRatio * (-cos1 - cos2);
			var oy:Number = appendVO.quadOffsetRatio * (-sin1 - sin2);
			
			var ndcScaleX:Number = 2/CoreSettings.STAGE_WIDTH;
			var ndcScaleY:Number = 2/CoreSettings.STAGE_HEIGHT;

			// Calculating the upper left corner of the quad:
			var vx : Number = (pnx - cos1 + ox) * ndcScaleX - 1.0;
			var vy : Number = -((pny - sin1 + oy) * ndcScaleY - 1.0);

			/*
			if (vx < _minX) _minX = vx;
			if (vx > _maxX) _maxX = vx;
			if (vy < _minY) _minY = vy;
			if (vy > _maxY) _maxY = vy;
			*/
			
			data[0] = vx;
			data[1] = vy;

			diffX = vx;

			// Calculating the upper right corner of the quad:
			vx = (pnx + cos2 + ox) * ndcScaleX - 1.0;
			vy = -((pny + sin2 + oy) * ndcScaleY - 1.0);

			/*
			if (vx < _minX) _minX = vx;
			if (vx > _maxX) _maxX = vx;
			if (vy < _minY) _minY = vy;
			if (vy > _maxY) _maxY = vy;
			*/
			diffX -= vx;

			data[8] = vx;
			data[9] = vy;

			// Calculating the lower right corner of the quad:
			vx = (pnx + cos1 + ox) * ndcScaleX - 1.0;
			vy = -((pny + sin1 + oy) * ndcScaleY - 1.0);
			/*
			if (vx < _minX) _minX = vx;
			if (vx > _maxX) _maxX = vx;
			if (vy < _minY) _minY = vy;
			if (vy > _maxY) _maxY = vy;
			*/
			data[16] = vx;
			data[17] = vy;

			// Calculating the lower left corner of the quad:
			vx = (pnx - cos2 + ox) * ndcScaleX - 1.0;
			vy = -((pny - sin2 + oy) * ndcScaleY - 1.0);

			/*
			if (vx < _minX) _minX = vx;
			if (vx > _maxX) _maxX = vx;
			if (vy < _minY) _minY = vy;
			if (vy > _maxY) _maxY = vy;
			*/
			data[24] = vx;
			data[25] = vy;
			
			// The uv coordinates for the 4 corners:
			data[2]  = data[26] = uvBounds.left;
			data[3]  = data[11] = uvBounds.top;
			data[10] = data[18] = uvBounds.right;
			data[19] = data[27] = uvBounds.bottom;

			diffU = uvBounds.left - uvBounds.right;
			
			//used by bump map:
			var rotCos : Number = Math.cos(angle);
			var rotSin : Number = Math.sin(angle);
			data[4] = data[12] = data[20] = data[28] = rotCos;
			data[5] = data[13] = data[21] = data[29] =-rotSin;
			data[6] = data[14] = data[22] = data[30] = rotSin;
			data[7] = data[15] = data[23] = data[31] = rotCos;

			// this is a scaling factor for neighbor sampling, trying to match the chosen mip maps (so we can sample neighbouring pixels correctly)
			bumpFactors[2] = bumpFactors[6] = bumpFactors[10] = bumpFactors[14] = Math.abs(diffX / diffU * .5);
			
			// _fastBuffer accumulates all the required vertex data before sending them to the GPU
			// we are using DomainMemory here for maximum performance:
			_fastBuffer.addInterleavedFloatsToVertices( data,_vIndex,8,8);
			_fastBuffer.addInterleavedFloatsToVertices( point.colorsRGBA,_vIndex+32,4,12);
			_fastBuffer.addInterleavedFloatsToVertices( bumpFactors,_vIndex+48,4,12);
			
			// each Quad uses 256 bytes of memory - calculated as numElementsPerVertex * 16
			_vIndex += 256;
			
			// each Quad uses 4 vertices (4 corner points):
			_numVertices += 4;
			
			// each Quad uses 6 indices (2 triangles a 3 indices):
			_numIndices += 6;

			invalidateBuffers();
			//invalidateBounds();
		}

		override public function drawColor(context3d : Context3D, canvas : CanvasModel, source : TextureBase = null) : void
		{
			var vertexBuffer : VertexBuffer3D = getVertexBuffer(context3d);

			context3d.setProgram(getColorProgram(context3d));
			
			//Vertex coordinate
			context3d.setVertexBufferAt(0, vertexBuffer, 0, Context3DVertexBufferFormat.FLOAT_2);
			//uv coordinate
			context3d.setVertexBufferAt(1, vertexBuffer, 2, Context3DVertexBufferFormat.FLOAT_2);
			//color value
			context3d.setVertexBufferAt(2, vertexBuffer, 8, Context3DVertexBufferFormat.FLOAT_4);
			
			context3d.setTextureAt(0, _brushTexture);
			context3d.drawTriangles(getIndexBuffer(context3d), 0, _numIndices/3);

			context3d.setTextureAt(0, null);

			context3d.setVertexBufferAt(0, null);
			context3d.setVertexBufferAt(1, null);
			context3d.setVertexBufferAt(2, null);
			
		}


		/**
		 * The uv coordinates are passed via v0 to the fragment shader
		 * The color data is passed via v1 to the fragment shader
		 */
		override protected function getColorVertexCode() : String
		{
			return "mov v0, va1\n"+
				   "mov v1, va2\n" +
				   "mov op, va0\n";
		}

		/**
		 * reads the red channel of the color texture and multiplies it with the color data
		 * the 3 vertices of a triangle can contain different colors and the resulting
		 * color used is the result of an interpolation between the 3 at the pixel location
		 */
		override protected function getColorFragmentCode() : String
		{
			return "tex ft0, v0, fs0 <2d, clamp, linear, miplinear >\n" +
				   "mul oc, v1, ft0.x\n";
		}

		override protected function get numElementsPerVertex() : int
		{
			return 16;
		}

		override protected function get topologyIndexType() : int
		{
			return FastBuffer.INDEX_MODE_QUADS;
		}


		override public function drawNormalsAndSpecular(context3d : Context3D, canvas : CanvasModel, glossiness : Number, bumpiness : Number, influence : Number) : void
		{
			var vertexBuffer : VertexBuffer3D = getVertexBuffer(context3d);

			context3d.setProgram(getNormalSpecularProgram(context3d));
			context3d.setVertexBufferAt(0, vertexBuffer, 0, Context3DVertexBufferFormat.FLOAT_2);
			context3d.setVertexBufferAt(1, vertexBuffer, 2, Context3DVertexBufferFormat.FLOAT_2);
			context3d.setVertexBufferAt(2, vertexBuffer, 4, Context3DVertexBufferFormat.FLOAT_4);
			context3d.setVertexBufferAt(3, vertexBuffer, 12, Context3DVertexBufferFormat.FLOAT_4);

			context3d.setTextureAt(0, _normalTexture);
			context3d.setTextureAt(1, canvas.normalSpecularMap);
			_normalSpecularVertexData[0] = 1/512;	// scale with diff_x / diff_u ( in pixel space ? )
			_normalSpecularVertexData[1] = 1/512;

			_normalSpecularVertexData[8] = 1/canvas.width;
			_normalSpecularVertexData[9] = 1/canvas.height;

			_normalSpecularVertexData[12] = glossiness;
			_normalSpecularVertexData[13] = bumpiness;
			_normalSpecularVertexData[15] = influence;

			context3d.setProgramConstantsFromVector(Context3DProgramType.VERTEX, 0, _normalSpecularVertexData, 4);
			context3d.setProgramConstantsFromVector(Context3DProgramType.FRAGMENT, 0, _normalSpecularFragmentData, _numFragmentRegisters);
			context3d.drawTriangles(getIndexBuffer(context3d), 0, _numIndices/3);
			context3d.setTextureAt(0, null);
			context3d.setTextureAt(1, null);

			context3d.setVertexBufferAt(0, null);
			context3d.setVertexBufferAt(1, null);
			context3d.setVertexBufferAt(2, null);
			context3d.setVertexBufferAt(3, null);
		}

		override protected function getNormalSpecularVertexCode() : String
		{
			return 	"mov op, va0\n" +

				// brushmap coords
					"mov v0, va1\n" +
					"mul vt0, va2.xyxy, vc0.xyzz\n" +
					"add v1, va1, vt0\n" +
					"mul vt0, va2.zwzw, vc0.xyzz\n" +
					"add v2, va1, vt0\n" +

				// canvas uvs
					"mul vt0, va0, vc1.xyww\n" +
					// make sure we've got the right mip neighbour
					"mul vt0, vt0, va3.z\n" +
					"add vt0, vt0, vc1.xxzz\n" +
					"mov v3, vt0\n" +

				// do not write to w to preserve linear (non-perspective) interpolation
					"mul v4.xyz, va3.xyw, vc3.xyw\n" +
					"mov v4.w, vc0.w";
		}

		// default code expects a height map + alpha map
		// texture input is:
		// R = height
		// G = gloss modulation
		// output should be (normalX, normalY, gloss, influence (alpha))
		// analytical solutions may be more optimal if possible
		override protected function getNormalSpecularFragmentCode() : String
		{
			var registers : Vector.<String> = new Vector.<String>();
			var i : uint;
			for (i = 1; i < _numFragmentRegisters; ++i) {
				registers.push("fc" + i + ".xy");
				registers.push("fc" + i + ".zw");
			}

			var code : String = "tex ft1, v0, fs0 <2d, clamp, linear, miplinear >\n" +
					"tex ft2, v1, fs0 <2d, clamp, linear, miplinear >\n" +
					"tex ft3, v2, fs0 <2d, clamp, linear, miplinear >\n" +
					"sub ft0.x, ft1.x, ft2.x\n" +
					"sub ft0.y, ft1.x, ft3.x\n" +

					"mul ft0.xy, ft0.xy, v4.y\n"; 	// bumpiness
			// ft0.xy contains bumpiness from brush

			// store original to blend against later
			code += "tex ft6, v3, fs1 <2d, clamp, linear, nomip>\n" +
					"sub ft6.xy, ft6.xy, fc0.x\n" +	// - .5
					"mul ft6.xy, ft6.xy, v4.z\n" +	// v4.z contains the amount of flattening of the original
					"add ft6.xy, ft6.xy, fc0.x\n";	// + .5

			for (i = 0; i < NUM_POISSON_SAMPLES; ++i) {
				code += "mul ft5.xy, " + registers[i] + ", ft1.x\n" +
						"add ft7, v3, ft5.xy\n" +
						"tex ft7, ft7, fs1 <2d, clamp, linear, nomip>\n";

				if (i == 0)
					code += "add ft3, ft6, ft7\n";
				else
					code += "add ft3, ft3, ft7\n";
			}
			// instead of doing - .5 for every sample, do it once for the total
			code += "sub ft3.xy, ft3.xy, fc0.w\n";	// - (NUM_POISSON_SAMPLES+1) *.5

			code += "mul ft3, ft3, fc0.y\n" +		// 1/(NUM_POISSON_SAMPLES + 1) -> average out
					"add ft0.xy, ft0.xy, ft3.xy\n" +
					"add ft0.xy, ft0.xy, fc0.x\n";	// + .5

			// ft0.xy now contains blurred map + new map

			// set glossiness, scaled by texture
			code +=	"mul ft0.z, ft1.y, v4.x\n" +

				// lerp based on height, not really robust
					"mul ft0.w, ft1.x, fc0.z\n" +	// brush height as alpha * 50
					"mov oc, ft0";

			return code;
		}
	}
}