/*
 * =BEGIN CLOSED LICENSE
 *
 * Copyright (c) 2013-2014 Andras Csizmadia
 * http://www.vpmedia.eu
 *
 * For information about the licensing and copyright please
 * contact Andras Csizmadia at andras@vpmedia.eu
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 * =END CLOSED LICENSE
 */
package hu.vpmedia.math {
import flash.geom.Matrix;

/**
 * The MatrixData class extends Matrix and exposes its transformation
 * properties in a more familiar API. Through properties such as x, y,
 * scaleX, scaleY, skewX, skewY and rotation the Matrix can be manipulated
 * without knowledge of Matrix math. Optionally, an external Matrix instance
 * can be targeted by the MatrixData.matrix property for manipulation via
 * MatrixData API's.
 */
public class Matrix2D extends Matrix {
    /**
     * Creates a MatrixData object.
     *
     * @param    matrix        The target matrix to be wrapped by the
     *                         MatrixData object. If no Matrix is specified
     *                         the MatrixData will reflect its own values as
     *                         an identity Matrix.
     */
    public function Matrix2D(matrix:Matrix = null):void {
        this.matrix = matrix;
    }

    /**
     * The distance of the represented matrix along the x axis.
     */
    public function get x():Number {
        return _matrix.tx;
    }

    public function set x(value:Number):void {
        _matrix.tx = value;
    }

    /**
     * The distance of the represented matrix along the y axis.
     */
    public function get y():Number {
        return _matrix.ty;
    }

    public function set y(value:Number):void {
        _matrix.ty = value;
    }

    /**
     * The horizontal scale of the represented matrix.
     */
    public function get scaleX():Number {
        return Math.sqrt(_matrix.a * _matrix.a + _matrix.b * _matrix.b);
    }

    public function set scaleX(value:Number):void {
        var skewY:Number = Math.atan2(_matrix.b, _matrix.a);
        _matrix.a = value * Math.cos(skewY);
        _matrix.b = value * Math.sin(skewY);
    }

    /**
     * The vertical scale of the represented matrix.
     */
    public function get scaleY():Number {
        return Math.sqrt(_matrix.c * _matrix.c + _matrix.d * _matrix.d);
    }

    public function set scaleY(value:Number):void {
        var skewX:Number = Math.atan2(-_matrix.c, _matrix.d);
        _matrix.c = value * -Math.sin(skewX);
        _matrix.d = value * Math.cos(skewX);
    }

    /**
     * The horizontal rotation or skew of the represented matrix.
     */
    public function get skewX():Number {
        return Math.atan2(-_matrix.c, _matrix.d);
    }

    public function set skewX(value:Number):void {
        var scaleY:Number = Math.sqrt(_matrix.c * _matrix.c + _matrix.d * _matrix.d);
        _matrix.c = scaleY * -Math.sin(value);
        _matrix.d = scaleY * Math.cos(value);
    }

    /**
     * The vertical rotation or skew of the represented matrix.
     */
    public function get skewY():Number {
        return Math.atan2(_matrix.b, _matrix.a);
    }

    public function set skewY(value:Number):void {
        var scaleX:Number = Math.sqrt(_matrix.a * _matrix.a + _matrix.b * _matrix.b);
        _matrix.a = scaleX * Math.cos(value);
        _matrix.b = scaleX * Math.sin(value);
    }

    /**
     * The rotation of the represented matrix. The rotation reflects
     * the vertical skew directly, but effects both vertical and
     * horizontal skew when applied.
     */
    public function get rotation():Number {
        return skewY;
    }

    public function set rotation(value:Number):void {
        var delta:Number = value - skewY;
        skewY = value;
        skewX += delta;
    }

    /**
     * Target matrix of the MatrixData object. Because MatrixData is
     * a direct representation of a matrix, changes to the matrix are
     * immediately reflected by each MatrixData property and vice versa.
     * By default this property references to the MatrixData object itself.
     */
    public function get matrix():Matrix {
        return _matrix;
    }

    public function set matrix(value:Matrix):void {
        _matrix = value || this;
    }

    private var _matrix:Matrix;

    /**
     * Evaluates the equality of another matrix with the represented matrix.
     *
     * @return                True if all values of each matrix are equal.
     */
    public function equals(value:Matrix):Boolean {
        if (value is Matrix2D) {
            // compare apples to apples (referenced matrices in both cases)
            value = Matrix2D(value)._matrix;
        }
        if (_matrix == null || value == null) {
            return (_matrix == value);
        }
        return (_matrix.a != value.a || _matrix.b != value.b || _matrix.c != value.c || _matrix.d != value.d || _matrix.tx != value.tx || _matrix.ty != value.ty);
    }

    /**
     * Returns a new Matrix2D object that is a clone of this Matrix2D,
     * an exact copy including a clone of an externally referenced matrix.
     *
     * @return                A replicate Matrix2D instance.
     */
    override public function clone():Matrix {
        var m:Matrix2D = new Matrix2D();
        m.a = a;
        m.b = b;
        m.c = c;
        m.d = d;
        m.tx = tx;
        m.ty = ty;
        if (_matrix != this) {
            m._matrix = _matrix.clone();
        }
        return m;
    }

    public function rotateAndScaleAroundExternalPoint(m:Matrix, x:Number, y:Number, angleRadians:Number, scalex:Number, scaley:Number):void {
        _matrix.tx -= x;
        _matrix.ty -= y;
        _matrix.rotate(angleRadians);
        _matrix.scale(scalex, scaley);
        _matrix.tx += x;
        _matrix.ty += y;
    }
}
}