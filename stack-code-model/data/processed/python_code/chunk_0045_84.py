﻿package com.company.assembleegameclient.objects.particles {
import flash.geom.Point;

import kabam.rotmg.messaging.impl.data.WorldPosData;

public class ConfettiEffect extends ParticleEffect {

    public var start_:Point;
    public var end_:Point;
    public var color_:int;
    public var lifetime_:int;
    public var confettiColor_:Boolean = false;

    public function ConfettiEffect(_arg1:WorldPosData, _arg2:WorldPosData, _arg3:int, _arg4:int, _arg5:Boolean = false) {
        this.start_ = new Point(_arg1.x_, _arg1.y_);
        this.end_ = new Point(_arg2.x_, _arg2.y_);
        this.color_ = _arg3;
        this.lifetime_ = _arg4;
        this.confettiColor_ = _arg5;
    }

    override public function update(_arg1:int, _arg2:int):Boolean {
        var _local4:int;
        var _local7:int;
        var _local8:ConfettiParticle;
        x_ = this.start_.x;
        y_ = this.start_.y;
        var _local3:int = 5;
        var _local5:Array = [0xFFFF, 0xFF00FF, 0xFFFF00, 0xFFFFFF];
        var _local6:int;
        while (_local6 < _local3) {
            if (this.confettiColor_) {
                _local4 = _local5[int(Math.floor((Math.random() * (_local5.length + 1))))];
            }
            else {
                _local4 = this.color_;
            }
            _local7 = ((3 + int((Math.random() * 5))) * 20);
            _local8 = new ConfettiParticle(1.85, _local7, _local4, ((500 * this.lifetime_) + ((Math.random() * 500) * this.lifetime_)), (0.1 + (Math.random() * 0.1)), this.start_, this.end_);
            map_.addObj(_local8, x_, y_);
            _local6++;
        }
        return (false);
    }


}
}

import com.company.assembleegameclient.objects.particles.Particle;

import flash.geom.Point;
import flash.geom.Vector3D;

class ConfettiParticle extends Particle {

    public var timeLeft_:int;
    protected var moveVec_:Vector3D;
    public var start_:Point;
    public var end_:Point;
    public var dx_:Number;
    public var dy_:Number;
    public var pathX_:Number;
    public var pathY_:Number;
    public var xDeflect_:Number;
    public var yDeflect_:Number;
    public var period_:Number;

    public function ConfettiParticle(_arg1:Number, _arg2:int, _arg3:int, _arg4:int, _arg5:Number, _arg6:Point, _arg7:Point) {
        this.moveVec_ = new Vector3D();
        super(_arg3, _arg1, _arg2);
        this.moveVec_.z = _arg5;
        this.timeLeft_ = _arg4;
        this.start_ = _arg6;
        this.end_ = _arg7;
        this.dx_ = ((this.end_.x - this.start_.x) / this.timeLeft_);
        this.dy_ = ((this.end_.y - this.start_.y) / this.timeLeft_);
        var _local8:Number = (Point.distance(_arg6, _arg7) / this.timeLeft_);
        var _local9:Number = 0.25;
        this.xDeflect_ = ((this.dy_ / _local8) * _local9);
        this.yDeflect_ = ((-(this.dx_) / _local8) * _local9);
        this.pathX_ = (x_ = this.start_.x);
        this.pathY_ = (y_ = this.start_.y);
        this.period_ = (0.25 + (Math.random() * 0.5));
    }

    override public function update(_arg1:int, _arg2:int):Boolean {
        this.timeLeft_ = (this.timeLeft_ - _arg2);
        if (this.timeLeft_ <= 0) {
            return (false);
        }
        this.pathX_ = (this.pathX_ + (this.dx_ * _arg2));
        this.pathY_ = (this.pathY_ + (this.dy_ * _arg2));
        var _local3:Number = Math.sin(((this.timeLeft_ / 1000) / this.period_));
        moveToInModal((this.pathX_ + (this.xDeflect_ * _local3)), (this.pathY_ + (this.yDeflect_ * _local3)));
        return (true);
    }


}