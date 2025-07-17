package aerys.minko.render.shader.part.phong
{
	import aerys.minko.render.material.basic.BasicProperties;
	import aerys.minko.render.shader.SFloat;
	import aerys.minko.render.shader.Shader;
	import aerys.minko.type.enum.SamplerFiltering;
	import aerys.minko.type.enum.SamplerMipMapping;
	import aerys.minko.type.enum.SamplerWrapping;
	
	public class LightAwareDiffuseShaderPart extends LightAwareShaderPart
	{
		public function LightAwareDiffuseShaderPart(main:Shader)
		{
			super(main);
		}
		
		public function getDiffuseColor() : SFloat
		{
			var diffuseColor : SFloat	= null;
			
			if (meshBindings.propertyExists(BasicProperties.DIFFUSE_MAP))
			{
				var diffuseMap	: SFloat	= meshBindings.getTextureParameter(
					BasicProperties.DIFFUSE_MAP,
					meshBindings.getConstant(BasicProperties.DIFFUSE_FILTERING, SamplerFiltering.LINEAR),
					meshBindings.getConstant(BasicProperties.DIFFUSE_MIPMAPPING, SamplerMipMapping.LINEAR),
					meshBindings.getConstant(BasicProperties.DIFFUSE_WRAPPING, SamplerWrapping.REPEAT)
				);
				
				diffuseColor = sampleTexture(diffuseMap, fsUV);
			}
			else if (meshBindings.propertyExists(BasicProperties.DIFFUSE_COLOR))
			{
				diffuseColor = meshBindings.getParameter(BasicProperties.DIFFUSE_COLOR, 4);
			}
			else
			{
				diffuseColor = float4(0., 0., 0., 1.);
			}
			
			// Apply HLSA modifiers
			if (meshBindings.propertyExists(BasicProperties.DIFFUSE_TRANSFORM))
			{
				diffuseColor = multiply4x4(
					diffuseColor,
					meshBindings.getParameter(BasicProperties.DIFFUSE_TRANSFORM, 16)
				);
			}
			
			// kill transparent pixels
			if (meshBindings.propertyExists(BasicProperties.ALPHA_THRESHOLD))
			{
				var alphaThreshold : SFloat = meshBindings.getParameter(
					BasicProperties.ALPHA_THRESHOLD, 1
				);
				
				kill(subtract(0.5, lessThan(diffuseColor.w, alphaThreshold)));
			}
			
			return diffuseColor;
		}
	}
}