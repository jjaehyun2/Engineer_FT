package flump.export {

import flash.display.Bitmap;
import flash.display.BitmapData;
import flash.display.Sprite;
import flash.geom.Point;
import flash.geom.Rectangle;

import flump.SwfTexture;
import flump.Util;
    import flump.export.AtlasUtil;

    import flump.mold.AtlasMold;
import flump.mold.AtlasTextureMold;

public class AtlasImpl implements Atlas
{
    public var name :String;
    public var isJpg:Boolean;

    public function AtlasImpl (name :String, w :int, h :int, xBorderSize :int, yBorderSize :int, scaleFactor :int, quality :String) {
        this.name = name;
        _width = w;
        _height = h;
        _xBorderSize = xBorderSize;
        _yBorderSize = yBorderSize;
        _mask = new BitmapData(_width, _height, true, 0);
        _mask.lock();
        _scaleFactor = scaleFactor;
        _quality = quality;
    }

    public function get area () :int { return _width * _height; }

    public function get scaleFactor () :int { return _scaleFactor; }

    public function get quailty () :String { return _quality; }

    public function get filename () :String { return name + AtlasMold.scaleFactorSuffix(_scaleFactor) + (isJpg ? ".jpg" : ".png"); }

    public function get jpg():Boolean { return isJpg; }

    public function get used () :int {
        var used :int = 0;
        _nodes.forEach(function (n :Node, ..._) :void {
            used += n.paddedBounds.width * n.paddedBounds.height;
        });
        return used;
    }

    public function toMold () :AtlasMold {
        const mold :AtlasMold = new AtlasMold();
        mold.file = this.filename;
        _nodes.forEach(function (node :Node, ..._) :void {
            const tex :SwfTexture = node.texture;
            const texMold :AtlasTextureMold = new AtlasTextureMold();
            texMold.symbol = tex.symbol;
            texMold.bounds = new Rectangle(node.bounds.x, node.bounds.y, tex.w, tex.h);
            texMold.origin = new Point(tex.origin.x, tex.origin.y);
            mold.textures.push(texMold);
        });
        return mold;
    }

    public function toBitmap () :BitmapData {
        if (_bitmapData == null) {
            var constructed :Sprite = new Sprite();
            var collapsedBounds :Rectangle = new Rectangle();
            _nodes.forEach(function (node :Node, ..._) :void {
                const bm :Bitmap = new Bitmap(node.texture.toBitmapData(!hasSingleTexture ? _xBorderSize : 0, !hasSingleTexture ? _yBorderSize : 0), "auto", true);
                constructed.addChild(bm);
                bm.x = node.paddedBounds.x;
                bm.y = node.paddedBounds.y;
                collapsedBounds = collapsedBounds.union(node.paddedBounds);
            });
            _bitmapData = Util.renderToBitmapData(constructed,
                    AtlasUtil.disablePOT ? totalWidth : Util.nextPowerOfTwo(collapsedBounds.x + collapsedBounds.width),
                    AtlasUtil.disablePOT ? totalHeight : Util.nextPowerOfTwo(collapsedBounds.y + collapsedBounds.height),
                    quailty);

            trace("AtlasUtil.disablePOT " + AtlasUtil.disablePOT, totalWidth, totalHeight);
        }

        return _bitmapData;
    }


    private var totalWidth:int;
    private var totalHeight:int;
    private var hasSingleTexture:Boolean;
    // Try to place a texture in this atlas
    public function place (tex :SwfTexture, xx :uint, yy :uint) :void {
        hasSingleTexture = tex.isSingle;

        var padX:int = !tex.isSingle ? _xBorderSize : 0;
        var padY:int = !tex.isSingle ? _yBorderSize : 0;

        var w :int = tex.w + (padX * 2);
        var h :int = tex.h + (padY * 2);
        if (w > _width || h > _height) {
            throw new Error("Tried to place a texture outside of the atlas. This is a bug.");
        }
        if (isMasked(xx, yy, w, h)) {
            throw new Error("Tried to place a texture over another texture. This is a bug.");
        }
        var node :Node = new Node(xx, yy, padX, padY, tex);
        _nodes.push(node);
        setMasked(node.paddedBounds.x, node.paddedBounds.y, node.paddedBounds.width, node.paddedBounds.height);

        var newWidth:int = xx + tex.w + padX;
        var newHeight:int = yy + tex.h + padY;

        if (newWidth > totalWidth) totalWidth = newWidth;
        if (newHeight > totalHeight) totalHeight = newHeight;
    }

    protected static var _isMaskedPoint:Point = new Point();
    protected static var _isMaskedRect:Rectangle = new Rectangle();
    protected function isMasked (x :int, y :int, w :int, h :int) :Boolean {
        _isMaskedRect.setTo(x, y, w, h);
        return _mask.hitTest(_isMaskedPoint, 1, _isMaskedRect);
    }

    protected static var _setMaskedRect:Rectangle = new Rectangle();
    protected function setMasked (x :int, y :int, w: int, h :int) :void {
        _setMaskedRect.setTo(x, y, w, h);
        _mask.fillRect(_setMaskedRect, 0xffffffff);
    }

    protected var _nodes :Array = [];
    protected var _width :int;
    protected var _height :int;
    protected var _xBorderSize :int;
    protected var _yBorderSize :int;
    protected var _mask :BitmapData;
    protected var _bitmapData :BitmapData;
    protected var _scaleFactor :int;
    protected var _quality :String;
}
}

import flash.geom.Rectangle;

import flump.SwfTexture;

class Node
{
    public var bounds :Rectangle;
    public var paddedBounds :Rectangle;
    public var texture :SwfTexture;

    public function Node (x :int, y :int, xBorderSize :int, yBorderSize :int, texture :SwfTexture) {
        this.texture = texture;
        this.bounds = new Rectangle(x + xBorderSize, y + yBorderSize, texture.w, texture.h);
        this.paddedBounds = new Rectangle(x, y,
                texture.w + (xBorderSize * 2),
                texture.h + (yBorderSize * 2));
    }
}