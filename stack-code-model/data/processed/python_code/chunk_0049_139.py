package aerys.minko.render.effect.wireframe
{
	import aerys.minko.render.geometry.stream.format.VertexComponent;
	import aerys.minko.render.geometry.stream.format.VertexComponentType;
	import aerys.minko.render.shader.SFloat;
	import aerys.minko.render.shader.Shader;
	import aerys.minko.render.shader.part.ShaderPart;

	public class WireframeShaderPart extends ShaderPart
	{
		private const LINE_THICKNESS_COEFF	: Number	= 1000.;
		
		protected function get vertexW() : SFloat
		{
			return getVertexAttribute(
				VertexComponent.create(['w1', 'w2', 'w3'], VertexComponentType.FLOAT_3)
			);
		}
		
		protected function get wireThickness() : SFloat
		{
			var coeff	: SFloat	= meshBindings.getParameter(WireframeProperties.THICKNESS, 1);
			
			coeff = subtract(2000, multiply(coeff, 50));
			
			return coeff;
		}
		
		public function WireframeShaderPart(main : Shader)
		{
			super(main);
		}
		
		/**
		 * The weight of the current vertex for the wireframe effect. 
		 * @return 
		 * 
		 */
		public function getVertexWeight(wireThickness : Object = null) : SFloat
		{
			wireThickness ||= this.wireThickness;
			
			var cameraDistance 	: SFloat	= length(subtract(cameraPosition, localToWorld(vertexXYZ)));
			var scale 			: SFloat 	= length(multiply3x3(float3(1., 0., 0.), localToWorldMatrix));
			var w				: SFloat	= vertexW;
			
			// original weight is the distance from the vertex to the opposite
			// side of the triangle, due to the abscence of geometry shader, this
			// is done in the WireframeMeshModifer.
			// It is then modified by its distance to the
			// camera and the scale of the mesh.
			
			w = multiply(w, wireThickness);
			w = divide(w, cameraDistance);
			w = multiply(w, scale);
			
			return w;
		}
		
		public function getWireFactor(interpolatedVertexWeights : SFloat) : SFloat
		{
			// only the shortest distance is used to compute the color of the fragment
			var d 	: SFloat 	= min(
				interpolatedVertexWeights.x,
				interpolatedVertexWeights.y,
				interpolatedVertexWeights.z
			);
			
			// e is strictly negative and closer to 0 the closer the fragment
			// is to a side of the triangle
			var e : SFloat 	= multiply(-2., power(d, 6));
			
			// the result is between 1 (when e = 0, i.e. when the fragment is on a 
			// triangle edge and rapidly approaches 0 when e decreases (when
			// the fragment gets further from an edge)			
			return power(2., e);
		}
		
		public function applyWireframe(diffuseColor : SFloat, weight : SFloat = null) : SFloat
		{
			weight ||= interpolate(getVertexWeight());
			
			var wireColor 		: SFloat	= meshBindings.getParameter(
				WireframeProperties.COLOR, 4, 0x000000ff
			);
			
			// the interpolated weight is a vector of dimension 3 containing
			// values representing the distance of the fragment to each side
			// of the triangle
			var wireFactor		: SFloat	= getWireFactor(weight);
			
			// the final color of the pixel is l * line_color + (1 - l) * surface_color
			diffuseColor = mix(diffuseColor, wireColor, wireFactor);
			
			kill(multiply(lessThan(diffuseColor.a, .001), -1));
			
			return diffuseColor;
		}
	}
}