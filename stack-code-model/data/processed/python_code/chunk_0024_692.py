﻿package com.company.assembleegameclient.map {
import com.company.assembleegameclient.objects.TextureData;
import com.company.assembleegameclient.objects.TextureDataConcrete;
import com.company.util.BitmapUtil;

import flash.display.BitmapData;

public class GroundProperties {

    public var type_:int;
    public var id_:String;
    public var noWalk_:Boolean = true;
    public var minDamage_:int = 0;
    public var maxDamage_:int = 0;
    public var animate_:AnimateProperties;
    public var blendPriority_:int = -1;
    public var compositePriority_:int = 0;
    public var speed_:Number = 1;
    public var xOffset_:Number = 0;
    public var yOffset_:Number = 0;
    public var slideAmount_:Number = 0;
    public var push_:Boolean = false;
    public var sink_:Boolean = false;
    public var sinking_:Boolean = false;
    public var randomOffset_:Boolean = false;
    public var hasEdge_:Boolean = false;
    private var edgeTD_:TextureData = null;
    private var cornerTD_:TextureData = null;
    private var innerCornerTD_:TextureData = null;
    private var edges_:Vector.<BitmapData> = null;
    private var innerCorners_:Vector.<BitmapData> = null;
    public var sameTypeEdgeMode_:Boolean = false;
    public var topTD_:TextureData = null;
    public var topAnimate_:AnimateProperties = null;

    public function GroundProperties(_arg1:XML) {
        this.animate_ = new AnimateProperties();
        super();
        this.type_ = int(_arg1.@type);
        this.id_ = String(_arg1.@id);
        this.noWalk_ = _arg1.hasOwnProperty("NoWalk");
        if (_arg1.hasOwnProperty("MinDamage")) {
            this.minDamage_ = int(_arg1.MinDamage);
        }
        if (_arg1.hasOwnProperty("MaxDamage")) {
            this.maxDamage_ = int(_arg1.MaxDamage);
        }
        this.push_ = _arg1.hasOwnProperty("Push");
        if (_arg1.hasOwnProperty("Animate")) {
            this.animate_.parseXML(XML(_arg1.Animate));
        }
        if (_arg1.hasOwnProperty("BlendPriority")) {
            this.blendPriority_ = int(_arg1.BlendPriority);
        }
        if (_arg1.hasOwnProperty("CompositePriority")) {
            this.compositePriority_ = int(_arg1.CompositePriority);
        }
        if (_arg1.hasOwnProperty("Speed")) {
            this.speed_ = Number(_arg1.Speed);
        }
        if (_arg1.hasOwnProperty("SlideAmount")) {
            this.slideAmount_ = Number(_arg1.SlideAmount);
        }
        this.xOffset_ = ((_arg1.hasOwnProperty("XOffset")) ? Number(_arg1.XOffset) : 0);
        this.yOffset_ = ((_arg1.hasOwnProperty("YOffset")) ? Number(_arg1.YOffset) : 0);
        this.push_ = _arg1.hasOwnProperty("Push");
        this.sink_ = _arg1.hasOwnProperty("Sink");
        this.sinking_ = _arg1.hasOwnProperty("Sinking");
        this.randomOffset_ = _arg1.hasOwnProperty("RandomOffset");
        if (_arg1.hasOwnProperty("Edge")) {
            this.hasEdge_ = true;
            this.edgeTD_ = new TextureDataConcrete(XML(_arg1.Edge));
            if (_arg1.hasOwnProperty("Corner")) {
                this.cornerTD_ = new TextureDataConcrete(XML(_arg1.Corner));
            }
            if (_arg1.hasOwnProperty("InnerCorner")) {
                this.innerCornerTD_ = new TextureDataConcrete(XML(_arg1.InnerCorner));
            }
        }
        this.sameTypeEdgeMode_ = _arg1.hasOwnProperty("SameTypeEdgeMode");
        if (_arg1.hasOwnProperty("Top")) {
            this.topTD_ = new TextureDataConcrete(XML(_arg1.Top));
            this.topAnimate_ = new AnimateProperties();
            if (_arg1.hasOwnProperty("TopAnimate")) {
                this.topAnimate_.parseXML(XML(_arg1.TopAnimate));
            }
        }
    }

    public function getEdges():Vector.<BitmapData> {
        if (((!(this.hasEdge_)) || (!((this.edges_ == null))))) {
            return (this.edges_);
        }
        this.edges_ = new Vector.<BitmapData>(9);
        this.edges_[3] = this.edgeTD_.getTexture(0);
        this.edges_[1] = BitmapUtil.rotateBitmapData(this.edges_[3], 1);
        this.edges_[5] = BitmapUtil.rotateBitmapData(this.edges_[3], 2);
        this.edges_[7] = BitmapUtil.rotateBitmapData(this.edges_[3], 3);
        if (this.cornerTD_ != null) {
            this.edges_[0] = this.cornerTD_.getTexture(0);
            this.edges_[2] = BitmapUtil.rotateBitmapData(this.edges_[0], 1);
            this.edges_[8] = BitmapUtil.rotateBitmapData(this.edges_[0], 2);
            this.edges_[6] = BitmapUtil.rotateBitmapData(this.edges_[0], 3);
        }
        return (this.edges_);
    }

    public function getInnerCorners():Vector.<BitmapData> {
        if ((((this.innerCornerTD_ == null)) || (!((this.innerCorners_ == null))))) {
            return (this.innerCorners_);
        }
        this.innerCorners_ = this.edges_.concat();
        this.innerCorners_[0] = this.innerCornerTD_.getTexture(0);
        this.innerCorners_[2] = BitmapUtil.rotateBitmapData(this.innerCorners_[0], 1);
        this.innerCorners_[8] = BitmapUtil.rotateBitmapData(this.innerCorners_[0], 2);
        this.innerCorners_[6] = BitmapUtil.rotateBitmapData(this.innerCorners_[0], 3);
        return (this.innerCorners_);
    }


}
}