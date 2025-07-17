﻿import com.greensock.TweenNano;
import com.greensock.easing.Quad;
import com.greensock.easing.Linear;

class SnowEffect extends ParticleEmitter
{
	/* Public Variables */
	public var minWindSpeed: Number = 0;
	public var maxWindSpeed: Number = 400;
	public var initialWindSpeed: Number = 0;
	public var particleRotationFactor:Number = 1;
	
	/* Private Variables */
	//private var _initialParticleCount: Number = 0;

	private var _framesPerSpawn: Number = 5;
	
	private var _windSpeed: Number;

	private var _frameTicker: Number = 0;

	private var _windInterval: Number;
	
	public function SnowEffect()
	{
		super();

		/*
		var particleInitFn: Function = function(a_particle: MovieClip): MovieClip {
			var particle: MovieClip = a_particle;
			particle._alpha = 100;
			// Random distribution between -buffer and width+buffer
			particle._x = (Math.random()*(_effectWidth + 2*effectBuffer)) - effectBuffer;
			// Random distribution between -buffer and height+buffer 
			particle._y = (Math.random()*(_effectHeight + effectBuffer)) - effectBuffer;
			particle._xscale = particle._yscale = (Math.max(0.5, Math.random())*particleScaleFactor)*100;
			xLoop(particle);
			yLoop(particle);
			return particle;
		}

		for (var i: Number = 0; i < _initialParticleCount; i++) {
			if (addParticle(particleInitFn) == undefined) {
				break;
			}
		}
		*/
		
		_windSpeed = initialWindSpeed;
		windLoop();
		
		onEnterFrame = emitter;
	}
	
	// @Override ParticleEmitter
	private function initParticle(a_particle: MovieClip): MovieClip
	{
		var particle: MovieClip = a_particle;
		particle._alpha = 100;
		// Random distribution between -buffer and width+buffer
		particle._x = (Math.random()*(_effectWidth + 2*effectBuffer)) - effectBuffer;
		// Random distribution between -buffer and 0
		particle._y = -(Math.random()*(effectBuffer));
		particle._xscale = particle._yscale = (Math.max(0.5, Math.random())*particleScaleFactor)*100;
		xLoop(particle);
		yLoop(particle);
		return particle;
	}
	
	private function emitter(): Void
	{
		_frameTicker = (_frameTicker + 1) % _framesPerSpawn;
		// Note that, !(Number.NaN > 0) == true
		if (!(_frameTicker > 0)) {
			if (addParticle() == undefined) {
				delete onEnterFrame;
				return;
			}

			if (_particles.length % 100 == 0 && _particles.length < maxParticles)
				particleScaleFactor += 0.15; // Increase size
			if (_particles.length % 20 == 0 && _framesPerSpawn > 1)
				_framesPerSpawn--; // Speed up
		}
	}
	
	private function windLoop(): Void
	{
		var time: Number = Math.random()*3+1;
		var nextSpeed: Number = Math.random()*(2*maxWindSpeed-minWindSpeed)-(minWindSpeed+maxWindSpeed);
		var nextWind: Number = Math.random()*(2)+1;
		TweenNano.to(this, time, {_windSpeed: nextSpeed, delay: nextWind, onComplete: windLoop, onCompleteScope: this});
	}
	
	private function xLoop(a_particle: MovieClip): Void {
		if (a_particle._x > _effectWidth + effectBuffer)
			a_particle._x = Math.random() * -effectBuffer;
		else if (a_particle._x < -effectBuffer)
			a_particle._x = _effectWidth + Math.random() * effectBuffer;
		TweenNano.to(a_particle, Math.random()*2+1, {_x: a_particle._x+(Math.random()*80-40+_windSpeed)*(a_particle._xscale/100), _rotation: Math.random()*particleRotationFactor*900, onComplete: xLoop, onCompleteParams: [a_particle], onCompleteScope: this, ease: Quad.easeInOut, overwrite: 0});
	}

	private function yLoop(a_particle: MovieClip): Void {
		if (a_particle._y > _effectHeight + effectBuffer) {
			a_particle._y = Math.random() * -effectBuffer;
			if (Math.floor(4096*Math.random()) == 0 && _particles.length > 375)
				a_particle.gotoAndStop("snow2");
			else if (a_particle.frameLabel != particleFrameLabel)
				a_particle.gotoAndStop(particleFrameLabel);
		} else if (a_particle._y < -effectBuffer) {
			a_particle._y = _effectHeight + Math.random() * effectBuffer;
		}
		TweenNano.to(a_particle, Math.random()*2+1, {_y: a_particle._y+(Math.random()*60+70)*(a_particle._xscale/100)*3, onComplete: yLoop, onCompleteParams: [a_particle], onCompleteScope: this, ease: Linear.easeInOut, overwrite: 0});
	}
}