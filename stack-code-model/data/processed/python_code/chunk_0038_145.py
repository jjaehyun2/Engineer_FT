package flash.display {
    import org.apache.royale.display.Graphics;
    import org.apache.royale.display.UIGraphicsBase;
    import org.apache.royale.geom.Matrix;
    import org.apache.royale.display.IGraphicsTarget;

    public final class Graphics {
        public function Graphics() {
            if (__locked) {
                throw new Error("Graphics can not be instanced");
            }

            _renderTarget = new UIGraphicsBase();
            _relatedG = org.apache.royale.display.Graphics.getInstanceFor(_renderTarget);
        }

        private var _renderTarget:IGraphicsTarget;

        internal function get renderTarget():IGraphicsTarget {
            return _renderTarget;
        }

        private var _relatedG:org.apache.royale.display.Graphics = null;

        private static var __locked:Boolean = true;

        internal static function createGraphics():flash.display.Graphics {
            __locked = false;
            var g:flash.display.Graphics = new flash.display.Graphics();
            __locked = true;
            return g;
        }

        public function drawRoundRect(x:Number, y:Number, width:Number, height:Number, ellipseWidth:Number, ellipseHeight:Number = NaN):void {
            _relatedG.drawRoundRect(x, y, width, height, ellipseWidth, ellipseHeight);
        }

        public function lineBitmapStyle(bitmap:org.apache.royale.display.BitmapData, matrix:org.apache.royale.geom.Matrix = null, repeat:Boolean = true, smooth:Boolean = false):void {
            _relatedG.lineBitmapStyle(bitmap, matrix, repeat, smooth);
        }

        public function beginGradientFill(type:String, colors:Array, alphas:Array, ratios:Array, matrix:org.apache.royale.geom.Matrix = null, spreadMethod:String = "pad", interpolationMethod:String = "rgb", focalPointRatio:Number = 0):void {
            _relatedG.beginGradientFill(type, colors, alphas, ratios, matrix, spreadMethod, interpolationMethod, focalPointRatio);
        }

        public function cubicCurveTo(controlX1:Number, controlY1:Number, controlX2:Number, controlY2:Number, anchorX:Number, anchorY:Number):void {
            _relatedG.cubicCurveTo(controlX1, controlY1, controlX2, controlY2, anchorX, anchorY);
        }

        public function lineTo(x:Number, y:Number):void {
            _relatedG.lineTo(x, y);
        }

        public function beginFill(color:uint, alpha:Number = 1.0):void {
            _relatedG.beginFill(color, alpha);
        }

        public function endFill():void {
            _relatedG.endFill();
        }

        public function lineStyle(thickness:Number = NaN, color:uint = 0, alpha:Number = 1.0, pixelHinting:Boolean = false, scaleMode:String = "normal", caps:String = null, joints:String = null, miterLimit:Number = 3):void {
            _relatedG.lineStyle(thickness, color, alpha, pixelHinting, scaleMode, caps, joints, miterLimit);
        }

        public function drawEllipse(x:Number, y:Number, width:Number, height:Number):void {
            _relatedG.drawEllipse(x, y, width, height);
        }

        public function beginBitmapFill(bitmap:org.apache.royale.display.BitmapData, matrix:org.apache.royale.geom.Matrix = null, repeat:Boolean = true, smooth:Boolean = false):void {
            _relatedG.beginBitmapFill(bitmap, matrix, repeat, smooth);
        }

        public function drawCircle(x:Number, y:Number, radius:Number):void {
            _relatedG.drawCircle(x, y, radius);
        }

        public function curveTo(controlX:Number, controlY:Number, anchorX:Number, anchorY:Number):void {
            _relatedG.curveTo(controlX, controlY, anchorX, anchorY);
        }

        public function clear():void {
            _relatedG.clear();
        }

        public function lineGradientStyle(type:String, colors:Array, alphas:Array, ratios:Array, matrix:org.apache.royale.geom.Matrix = null, spreadMethod:String = "pad", interpolationMethod:String = "rgb", focalPointRatio:Number = 0):void {
            _relatedG.lineGradientStyle(type, colors, alphas, ratios, matrix, spreadMethod, interpolationMethod, focalPointRatio);
        }

        public function drawRoundRectComplex(x:Number, y:Number, width:Number, height:Number, topLeftRadius:Number, topRightRadius:Number, bottomLeftRadius:Number, bottomRightRadius:Number):void {
            _relatedG.drawRoundRectComplex(x, y, width, height, topLeftRadius, topRightRadius, bottomLeftRadius, bottomRightRadius);
        }

        public function drawRect(x:Number, y:Number, width:Number, height:Number):void {
            _relatedG.drawRect(x, y, width, height);
        }

        public function moveTo(x:Number, y:Number):void {
            _relatedG.moveTo(x, y);
        }
    }
}