﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//com.company.assembleegameclient.objects.particles.StreamEffect

package com.company.assembleegameclient.objects.particles
{
    import flash.geom.Point;
    import kabam.rotmg.messaging.impl.data.WorldPosData;

    public class StreamEffect extends ParticleEffect 
    {

        public var start_:Point;
        public var end_:Point;
        public var color_:int;

        public function StreamEffect(_arg_1:WorldPosData, _arg_2:WorldPosData, _arg_3:int)
        {
            this.start_ = new Point(_arg_1.x_, _arg_1.y_);
            this.end_ = new Point(_arg_2.x_, _arg_2.y_);
            this.color_ = _arg_3;
        }

        override public function update(_arg_1:int, _arg_2:int):Boolean
        {
            var _local_5:int;
            var _local_6:StreamParticle;
            x_ = this.start_.x;
            y_ = this.start_.y;
            var _local_3:int = 5;
            var _local_4:int;
            while (_local_4 < _local_3)
            {
                _local_5 = ((3 + int((Math.random() * 5))) * 20);
                _local_6 = new StreamParticle(1.85, _local_5, this.color_, (1500 + (Math.random() * 3000)), (0.1 + (Math.random() * 0.1)), this.start_, this.end_);
                map_.addObj(_local_6, x_, y_);
                _local_4++;
            }
            return (false);
        }


    }
}//package com.company.assembleegameclient.objects.particles

import com.company.assembleegameclient.objects.particles.Particle;
import flash.geom.Vector3D;
import flash.geom.Point;

class StreamParticle extends Particle 
{

    public var timeLeft_:int;
    protected var moveVec_:Vector3D = new Vector3D();
    public var start_:Point;
    public var end_:Point;
    public var dx_:Number;
    public var dy_:Number;
    public var pathX_:Number;
    public var pathY_:Number;
    public var xDeflect_:Number;
    public var yDeflect_:Number;
    public var period_:Number;

    public function StreamParticle(_arg_1:Number, _arg_2:int, _arg_3:int, _arg_4:int, _arg_5:Number, _arg_6:Point, _arg_7:Point)
    {
        super(_arg_3, _arg_1, _arg_2);
        this.moveVec_.z = _arg_5;
        this.timeLeft_ = _arg_4;
        this.start_ = _arg_6;
        this.end_ = _arg_7;
        this.dx_ = ((this.end_.x - this.start_.x) / this.timeLeft_);
        this.dy_ = ((this.end_.y - this.start_.y) / this.timeLeft_);
        var _local_8:Number = (Point.distance(_arg_6, _arg_7) / this.timeLeft_);
        var _local_9:Number = 0.25;
        this.xDeflect_ = ((this.dy_ / _local_8) * _local_9);
        this.yDeflect_ = ((-(this.dx_) / _local_8) * _local_9);
        this.pathX_ = (x_ = this.start_.x);
        this.pathY_ = (y_ = this.start_.y);
        this.period_ = (0.25 + (Math.random() * 0.5));
    }

    override public function update(_arg_1:int, _arg_2:int):Boolean
    {
        this.timeLeft_ = (this.timeLeft_ - _arg_2);
        if (this.timeLeft_ <= 0)
        {
            return (false);
        }
        this.pathX_ = (this.pathX_ + (this.dx_ * _arg_2));
        this.pathY_ = (this.pathY_ + (this.dy_ * _arg_2));
        var _local_3:Number = Math.sin(((this.timeLeft_ / 1000) / this.period_));
        moveTo((this.pathX_ + (this.xDeflect_ * _local_3)), (this.pathY_ + (this.yDeflect_ * _local_3)));
        return (true);
    }


}