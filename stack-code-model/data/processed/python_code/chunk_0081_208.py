package com.grantech.controls.displays
{
	import com.grantech.models.LayerDataModel;
	import com.grantech.models.ParticleDataModel;

	import flash.display3D.Context3DBlendFactor;

	import starling.extensions.ColorArgb;
	import starling.extensions.PDParticleSystem;
	import starling.utils.deg2rad;
	import starling.utils.rad2deg;

	public class SceneParticleSystem extends PDParticleSystem implements ISceneObject
	{
		public function SceneParticleSystem(layer:LayerDataModel, config:Object)
		{
			super(null, ParticleDataModel(layer).texture);
			this.layer = layer;
		}
		
		private var _layer:LayerDataModel;
		public function get layer():LayerDataModel { return this._layer; }
		public function set layer(value:LayerDataModel):void
		{
			this._layer = value;
			for(var key:String in layer.properties)
				if( this.hasOwnProperty(key))
					this[key] = layer.properties[key];
			this.updateEmissionRate();
		}
		public function hasOwnProperty(V:*):Boolean { return super.hasOwnProperty(V); }

		public function getBlendCode(value:String):int
		{
			switch (value)
			{
				case Context3DBlendFactor.ZERO: return 0;
				case Context3DBlendFactor.ONE: return 1;
				case Context3DBlendFactor.SOURCE_COLOR: return 0x300;
				case Context3DBlendFactor.ONE_MINUS_SOURCE_COLOR: return 0x301;
				case Context3DBlendFactor.SOURCE_ALPHA: return 0x302;
				case Context3DBlendFactor.ONE_MINUS_SOURCE_ALPHA: return 0x303;
				case Context3DBlendFactor.DESTINATION_ALPHA: return 0x304;
				case Context3DBlendFactor.ONE_MINUS_DESTINATION_ALPHA: return 0x305;
				case Context3DBlendFactor.DESTINATION_COLOR: return 0x306;
				case Context3DBlendFactor.ONE_MINUS_DESTINATION_COLOR: return 0x307;
				default:    throw new ArgumentError("unsupported blending function: " + value);
			}
		}

		public function getBlendFunc(value:int):String
		{
			switch (value)
			{
				case 0:     return Context3DBlendFactor.ZERO;
				case 1:     return Context3DBlendFactor.ONE;
				case 0x300: return Context3DBlendFactor.SOURCE_COLOR;
				case 0x301: return Context3DBlendFactor.ONE_MINUS_SOURCE_COLOR;
				case 0x302: return Context3DBlendFactor.SOURCE_ALPHA;
				case 0x303: return Context3DBlendFactor.ONE_MINUS_SOURCE_ALPHA;
				case 0x304: return Context3DBlendFactor.DESTINATION_ALPHA;
				case 0x305: return Context3DBlendFactor.ONE_MINUS_DESTINATION_ALPHA;
				case 0x306: return Context3DBlendFactor.DESTINATION_COLOR;
				case 0x307: return Context3DBlendFactor.ONE_MINUS_DESTINATION_COLOR;
				default:    throw new ArgumentError("unsupported blending function: " + value);
			}
		}

		public function get sourcePositionVariancex():Number { return emitterXVariance; }
		public function set sourcePositionVariancex(value:Number):void { emitterXVariance = value; }

		public function get sourcePositionVariancey():Number { return emitterYVariance; }
		public function set sourcePositionVariancey(value:Number):void { emitterYVariance = value; }

		public function get duration():Number { return defaultDuration; }
		public function set duration(value:Number):void { defaultDuration = value; }

		public function set maxParticles(value:int):void { capacity = value; }
		public function get maxParticles():int { return capacity; }

		public function get particleLifespan():Number { return lifespan; }
		public function set particleLifespan(value:Number):void { lifespan = value; }

		public function get particleLifespanVariance():Number { return lifespanVariance; }
		public function set particleLifespanVariance(value:Number):void { lifespanVariance = value; }
		
		public function get startParticleSize():Number { return startSize; }
		public function set startParticleSize(value:Number):void { startSize = value; }

		public function get startParticleSizeVariance():Number { return startSizeVariance; }
		public function set startParticleSizeVariance(value:Number):void { startSizeVariance = value; }

		public function get finishParticleSize():Number { return endSize; }
		public function set finishParticleSize(value:Number):void { endSize = value; }

		public function get finishParticleSizeVariance():Number { return endSizeVariance; }
		public function set finishParticleSizeVariance(value:Number):void { endSizeVariance = value; }

		public function get angle():Number { return rad2deg(emitAngle); }
		public function set angle(value:Number):void { emitAngle = deg2rad(value); }

		public function get angleVariance():Number { return rad2deg(emitAngleVariance); }
		public function set angleVariance(value:Number):void { emitAngleVariance = deg2rad(value); }

		public function get rotationStart():Number { return rad2deg(startRotation); }
		public function set rotationStart(value:Number):void { startRotation = deg2rad(value); }

		public function get rotationStartVariance():Number { return rad2deg(startRotationVariance); }
		public function set rotationStartVariance(value:Number):void { startRotationVariance = deg2rad(value); }

		public function get rotationEnd():Number { return rad2deg(endRotation); }
		public function set rotationEnd(value:Number):void { endRotation = deg2rad(value); }

		public function get rotationEndVariance():Number { return rad2deg(endRotationVariance); }
		public function set rotationEndVariance(value:Number):void { endRotationVariance = deg2rad(value); }

		public function get gravityx():Number { return gravityX; }
		public function set gravityx(value:Number):void { gravityX = value; }

		public function get gravityy():Number { return gravityY; }
		public function set gravityy(value:Number):void { gravityY = value; }

		public function get radialAccelVariance():Number { return radialAccelerationVariance; }
		public function set radialAccelVariance(value:Number):void { radialAccelerationVariance = value; }

		public function get tangentialAccelVariance():Number { return tangentialAccelerationVariance; }
		public function set tangentialAccelVariance(value:Number):void { tangentialAccelerationVariance = value; }

		public function get finishColor():ColorArgb { return endColor; }
		public function set finishColor(value:ColorArgb):void { endColor = value; }

		public function get finishColorVariance():ColorArgb { return endColorVariance; }
		public function set finishColorVariance(value:ColorArgb):void { endColorVariance = value; }

		public function get blendFuncSource():int { return getBlendCode(blendFactorSource); }
		public function set blendFuncSource(value:int):void { blendFactorSource = getBlendFunc(value) }

		public function get blendFuncDestination():int { return getBlendCode(blendFactorDestination); }
		public function set blendFuncDestination(value:int):void { blendFactorDestination = getBlendFunc(value) }
	}
}