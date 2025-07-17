package aerys.minko.render.shader.part.environment
{
	import aerys.minko.render.material.environment.EnvironmentMappingProperties;
	import aerys.minko.render.shader.SFloat;
	import aerys.minko.render.shader.Shader;
	import aerys.minko.render.shader.part.BlendingShaderPart;
	import aerys.minko.render.shader.part.phong.LightAwareShaderPart;
	import aerys.minko.render.shader.part.projection.BlinnNewellProjectionShaderPart;
	import aerys.minko.render.shader.part.projection.ProbeProjectionShaderPart;
	import aerys.minko.type.enum.Blending;
	import aerys.minko.type.enum.EnvironmentMappingType;
	import aerys.minko.type.enum.SamplerDimension;
	import aerys.minko.type.enum.SamplerFiltering;
	import aerys.minko.type.enum.SamplerMipMapping;
	import aerys.minko.type.enum.SamplerWrapping;
	
	import flash.geom.Rectangle;
	
	public class EnvironmentMappingShaderPart extends LightAwareShaderPart
	{
		private var _blinnNewellProjectionPart	: BlinnNewellProjectionShaderPart;
		private var _probeProjectionPart		: ProbeProjectionShaderPart;
		private var _blending					: BlendingShaderPart;
		
		public function EnvironmentMappingShaderPart(main : Shader)
		{
			super(main);
			
			_blinnNewellProjectionPart	= new BlinnNewellProjectionShaderPart(main);
			_probeProjectionPart		= new ProbeProjectionShaderPart(main);
			_blending					= new BlendingShaderPart(main);
		}
		
		public function getEnvironmentColor() : SFloat
		{
			// compute reflected vector
			var cWorldCameraPosition	: SFloat = this.cameraPosition;
			var vsWorldVertexToCamera	: SFloat = normalize(subtract(cWorldCameraPosition, vsWorldPosition));
			var reflected				: SFloat = normalize(interpolate(reflect(vsWorldVertexToCamera.xyzz, vsWorldNormal.xyzz)));
			var reflectionType 			: int	 = meshBindings.getConstant(
				EnvironmentMappingProperties.ENVIRONMENT_MAPPING_TYPE
			);
			
			// retrieve reflection color from reflection map
			var reflectionMap			: SFloat;
			var reflectionMapUV			: SFloat;
			var reflectionColor			: SFloat;
			
			switch (reflectionType)
			{
				case EnvironmentMappingType.NONE:
					reflectionColor = float4(0, 0, 0, 0);
					break;
				
				case EnvironmentMappingType.PROBE:
					reflectionMap	= meshBindings.getTextureParameter(EnvironmentMappingProperties.ENVIRONMENT_MAP);
					reflectionMapUV = _probeProjectionPart.projectVector(reflected, new Rectangle(0, 0, 1, 1));
					reflectionColor = sampleTexture(reflectionMap, reflectionMapUV);
					break;
				
				case EnvironmentMappingType.BLINN_NEWELL:
					reflectionMap	= meshBindings.getTextureParameter(EnvironmentMappingProperties.ENVIRONMENT_MAP);
					reflectionMapUV = _blinnNewellProjectionPart.projectVector(reflected, new Rectangle(0, 0, 1, 1));
					reflectionColor = sampleTexture(reflectionMap, reflectionMapUV);
					break;
				
				case EnvironmentMappingType.CUBE:
					reflectionMap	= meshBindings.getTextureParameter(
						EnvironmentMappingProperties.ENVIRONMENT_MAP, 
						SamplerFiltering.NEAREST, SamplerMipMapping.DISABLE, SamplerWrapping.CLAMP, SamplerDimension.CUBE
					);
					reflectionColor = sampleTexture(reflectionMap, reflected);
					break
				
				default:
					throw new Error('Unsupported reflection type');
			}
			
			// modifify alpha color
			if (meshBindings.propertyExists(EnvironmentMappingProperties.REFLECTIVITY))
			{
				var reflectivity : SFloat = meshBindings.getParameter(
					EnvironmentMappingProperties.REFLECTIVITY, 1
				);
				
				reflectionColor = float4(reflectionColor.xyz, multiply(reflectionColor.w, reflectivity));
			}
			
			return reflectionColor;
		}
		
		public function applyEnvironmentMapping(diffuse : SFloat) : SFloat
		{
			if (!meshBindings.propertyExists(EnvironmentMappingProperties.ENVIRONMENT_MAPPING_TYPE))
				return diffuse;
			
			return _blending.blend(
				getEnvironmentColor(),
				diffuse,
				meshBindings.getConstant(EnvironmentMappingProperties.ENVIRONMENT_BLENDING, Blending.ALPHA)
			);
		}
	}
}