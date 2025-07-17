package x3dom.shaders
{
	import x3dom.*;
	
	import com.adobe.utils.AGALMiniAssembler;
	
	import flash.display3D.Context3D;
	import flash.display3D.Context3DProgramType;
	import flash.display3D.Program3D;
	
	public class LPPDebugShader
	{
		/**
		 * Holds our 3D context
		 */
		private var _context3D:Context3D;
		
		/**
		 * Program3D for the LPPDebugShader
		 */
		private var _program3D:Program3D;
		
		/**
		 * Generate the final Program3D for the DepthShader
		 */
		public function LPPDebugShader()
		{
			//Get 3D Context
			this._context3D = FlashBackend.getContext();
			
			//Generate Program3D 
			this._program3D = this._context3D.createProgram();
			
			//Generate vertex shader
			var vertexShader:AGALMiniAssembler = generateVertexShader();
			
			//Generate fragment shader
			var fragmentShader:AGALMiniAssembler = generateFragmentShader();
			
			//Upload shaders to Program3D
			this._program3D.upload( vertexShader.agalcode, fragmentShader.agalcode);
		}
		
		/**
		 * Generate the vertex shader
		 */
		private function generateVertexShader() : AGALMiniAssembler
		{
			//Init shader string
			var shader:String = "";
			
			//Build shader
			shader += "m44 op, va0, vc0\n";	//Position*MP-Matrix -> (op)
			shader += "mov v0, va1\n";	//Texcoords -> (v0)
			
			//Generate AGALMiniAssembler from generated Shader
			var vertexShader:AGALMiniAssembler = new AGALMiniAssembler();
			vertexShader.assemble( Context3DProgramType.VERTEX, shader );
			
			//Return AGALMiniAssembler
			return vertexShader;
		}
		
		/**
		 * Generate the fragment shader
		 */
		private function generateFragmentShader() : AGALMiniAssembler
		{
			//Init shader string
			var shader:String = "";
			
			shader += "tex oc, v0, fs0 <2d, wrap, linear>\n";	//Sample Texture(ft0)
			
			//Generate AGALMiniAssembler from generated Shader
			var fragmentShader:AGALMiniAssembler = new AGALMiniAssembler();
			fragmentShader.assemble( Context3DProgramType.FRAGMENT, shader );
			
			//Return AGALMiniAssembler
			return fragmentShader;
		}
		
		/**
		 * Return the generated Program3D
		 */ 
		public function get program3D() : Program3D
		{
			return this._program3D;
		}
	}
}