package goplayer
{
  public class Dimensions
  {
    public var _width : Number
    public var _height : Number

    public function Dimensions(width : Number, height : Number)
    { _width = width, _height = height }

    public function get width() : Number
    { return _width }

    public function get height() : Number
    { return _height }

    public function get doubled() : Dimensions
    { return scaledBy(2) }

    public function get halved() : Dimensions
    { return scaledBy(.5) }
    
    public function get quarter() : Dimensions
    { return scaledBy(.25) }

    public function scaledBy(scalar : Number) : Dimensions
    { return new Dimensions(width * scalar, height * scalar) }

    public function get center() : Position
    { return halved.asPosition }

    public function get asPosition() : Position
    { return new Position(width, height) }

    public function plus(other : Dimensions) : Dimensions
    { return new Dimensions(width + other.width, height + other.height) }

    public function minus(other : Dimensions) : Dimensions
    { return new Dimensions(width - other.width, height - other.height) }

    public function get aspectRatio() : Number
    { return width / height }

    public function get innerSquare() : Dimensions
    { return Dimensions.square(Math.min(width, height)) }

    public function getInnerDimensions
      (innerAspectRatio : Number) : Dimensions
    {
      if (innerAspectRatio > aspectRatio)
        return new Dimensions(width, width / innerAspectRatio)
      else
        return new Dimensions(height * innerAspectRatio, height)
    }

    public function isGreaterThan(other : Dimensions) : Boolean
    { return width > other.width && height > other.height }

    public function toString() : String
    { return width + "×" + height }

    public static function equals(a : Dimensions, b : Dimensions) : Boolean
    {
      return a == null ? b == null
        : b != null && a.width == b.width && a.height == b.height
    }

    public static function square(size : Number) : Dimensions
    { return new Dimensions(size, size) }

    public static const ZERO : Dimensions = new Dimensions(0, 0)
  }
}