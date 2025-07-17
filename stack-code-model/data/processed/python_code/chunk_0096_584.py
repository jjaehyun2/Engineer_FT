package
{
	/**
	 * uint 类提供使用表示 32 位无符号整数的数据类型的方法。因为无符号整数只能为正，所以其最大值是 int 类最大值的两倍。
	 * <p class="- topic/p ">由 uint 类表示的值的范围介于 0 到 4,294,967,295 (2^32-1) 之间。</p><p class="- topic/p ">可以通过声明 uint 类型的变量并为变量赋予文本值来创建 uint 对象。uint 类型变量的默认值为 <codeph class="+ topic/ph pr-d/codeph ">0</codeph>。</p><p class="- topic/p ">uint 类主要用于像素颜色值（ARGB 和 RGBA）和 int 数据类型无法正常运行的其它情况。例如，数字 0xFFFFFFFF 表示 Alpha 值为 255 的白色颜色值，它无法用 int 数据类型表示，因为它不在有效的 int 值范围内。</p><p class="- topic/p ">下例将创建一个 uint 对象并调用 <codeph class="+ topic/ph pr-d/codeph "> toString()</codeph> 方法：</p><pre xml:space="preserve" class="- topic/pre ">
	 * var myuint:uint = 1234;
	 * trace(myuint.toString()); // 1234
	 * </pre><p class="- topic/p ">下面的示例在不使用构造函数的情况下，将 <codeph class="+ topic/ph pr-d/codeph ">MIN_VALUE</codeph> 属性的值赋予一个变量：</p><pre xml:space="preserve" class="- topic/pre ">
	 * var smallest:uint = uint.MIN_VALUE;
	 * trace(smallest.toString()); // 0
	 * </pre>
	 * 
	 *   EXAMPLE:
	 * 
	 *   下面的示例声明 uint <codeph class="+ topic/ph pr-d/codeph ">i</codeph>（在 <codeph class="+ topic/ph pr-d/codeph ">for</codeph> 循环内），这将输出介于 0 和 9 之间的数字（因为 uint 默认为 0）。
	 * <codeblock xml:space="preserve" class="+ topic/pre pr-d/codeblock ">
	 * 
	 *   package {
	 * import flash.display.Sprite;
	 * 
	 *   public class UintExample extends Sprite {
	 * public function UintExample() {
	 * for(var i:uint; i &lt; 10; i++) {
	 * trace(i);
	 * }
	 * }
	 * }
	 * }
	 * </codeblock>
	 * @langversion	3.0
	 * @playerversion	Flash 9
	 * @playerversion	Lite 4
	 */
	public final class uint
	{
		
		/**
		 * 可表示的最大 32 位无符号整数为 4,294,967,295。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 */
		public static const MAX_VALUE : uint = 4294967295;

		/**
		 * 可表示的最小无符号整数为 0。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 */
		public static const MIN_VALUE : uint = 0;

		/**
		 * 返回数字的字符串表示形式（采用指数表示法）。字符串在小数点前面包含一位，在小数点后面最多包含 20 位（在 fractionDigits 参数中指定）。
		 * @param	fractionDigits	介于 0 和 20（含）之间的整数，表示所需的小数位数。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	AIR 1.0
		 * @playerversion	Lite 4
		 * @throws	RangeError 如果 fractionDigits 参数不在 0 到 20 的范围内，则会引发异常。
		 */
		public function toExponential (p:int = 0) : String { return null; }

		/**
		 * 返回数字的字符串表示形式（采用定点表示法）。定点表示法是指字符串的小数点后面包含特定的位数（在 fractionDigits 参数中指定）。fractionDigits 参数的有效范围为 0 到 20。如果指定的值在此范围外，则会引发异常。
		 * @param	fractionDigits	介于 0 和 20（含）之间的整数，表示所需的小数位数。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	AIR 1.0
		 * @playerversion	Lite 4
		 * @throws	RangeError 如果 fractionDigits 参数不在 0 到 20 的范围内，则会引发异常。
		 */
		public function toFixed (p:int=0) : String{ return null; }

		/**
		 * 返回数字的字符串表示形式（采用指数表示法或定点表示法）。字符串将包含 precision 参数中指定的位数。
		 * @param	precision	介于 1 和 21（含）之间的整数，表示结果字符串中所需的位数。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	AIR 1.0
		 * @playerversion	Lite 4
		 * @throws	RangeError 如果 precision 参数不在 1 到 21 的范围内，则会引发异常。
		 */
		public function toPrecision (p:int=0) : String{ return null; }

		/**
		 * 返回 uint 对象的字符串表示形式。
		 * @param	radix	指定要用于数字到字符串的转换的基数（从 2 到 36）。如果未指定 radix 参数，则默认值为 10。
		 * @return	uint 对象的字符串表达式。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 */
		public function toString (radix:int=10) : String{ return null; }


		
		/**
		 * 创建新的 uint 对象。可以创建一个 uint 类型的变量并赋予其文本值。new uint() 构造函数主要用作占位符。uint 对象与  uint() 函数不同，后者会将参数转换为原始值。
		 * @param	num	要创建的 uint 对象的数值，或者要转换为数字的值。如果未提供 num，则默认值为 0。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 */
		public function uint (value:*=0){ }

		/**
		 * 返回指定 uint 对象的原始 uint 类型值。
		 * @return	此 uint 对象的原始 uint 类型值。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 */
		public function valueOf () : uint{ return 0; }
	}
}