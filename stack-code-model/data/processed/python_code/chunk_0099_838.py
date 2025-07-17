//
// C:\Users\Manju-pc\AppData\Local\FlashDevelop\Apps\ascsdk\27.0.0\frameworks\libs\air\airglobal.swc\flash\utils\IDataOutput
//
package flash.utils
{
	
	/**
	 * IDataOutput 接口提供一组用于写入二进制数据的方法。此接口是读取二进制数据的 IDataInput 接口的 I/O 对应接口。IDataOutput 接口是由 FileStream、Socket 和 ByteArray 类实现的。
	 * <p class="- topic/p ">默认情况下，所有 IDataInput 和 IDataOutput 操作均为“bigEndian”（序列中的最高有效字节存储在最低或第一个存储地址），而且都不分块。 </p><p class="- topic/p ">符号扩展名仅在读取数据时有效，写入数据时无效。因此，无需单独的写入方法就可以使用 <codeph class="+ topic/ph pr-d/codeph ">IDataInput.readUnsignedByte()</codeph> 和 <codeph class="+ topic/ph pr-d/codeph ">IDataInput.readUnsignedShort()</codeph>。换言之：</p><ul class="- topic/ul "><li class="- topic/li ">将 <codeph class="+ topic/ph pr-d/codeph ">IDataOutput.writeByte()</codeph> 与 <codeph class="+ topic/ph pr-d/codeph ">IDataInput.readUnsignedByte()</codeph> 和 <codeph class="+ topic/ph pr-d/codeph ">IDataInput.readByte()</codeph> 一起使用。</li><li class="- topic/li ">将 <codeph class="+ topic/ph pr-d/codeph ">IDataOutput.writeShort()</codeph> 与 <codeph class="+ topic/ph pr-d/codeph ">IDataInput.readUnsignedShort()</codeph> 和 <codeph class="+ topic/ph pr-d/codeph ">IDataInput.readShort()</codeph> 一起使用。</li></ul>
	 * 
	 *   EXAMPLE:
	 * 
	 *   以下示例使用 <codeph class="+ topic/ph pr-d/codeph ">DataOutputExample</codeph> 类将布尔值和 pi 的双精度浮点表示形式写入字节数组。这是使用以下步骤完成的：
	 * <ol class="- topic/ol "><li class="- topic/li ">声明新的 ByteArray 对象实例 <codeph class="+ topic/ph pr-d/codeph ">byteArr</codeph>。</li><li class="- topic/li ">写入布尔值 <codeph class="+ topic/ph pr-d/codeph ">false</codeph> 的字节等效值和数学值 pi 的双精度浮点等效值。</li><li class="- topic/li ">重新读取布尔值和双精度浮点数。</li></ol><p class="- topic/p ">注意如何在末尾添加一段代码以检查文件结尾错误，确保读取的字节流没有超出文件结尾。</p><codeblock xml:space="preserve" class="+ topic/pre pr-d/codeblock ">
	 * package {
	 * import flash.display.Sprite;
	 * import flash.utils.ByteArray;
	 * import flash.errors.EOFError;
	 * 
	 *   public class DataOutputExample extends Sprite {        
	 * public function DataOutputExample() {
	 * var byteArr:ByteArray = new ByteArray();
	 * 
	 *   byteArr.writeBoolean(false);
	 * byteArr.writeDouble(Math.PI);
	 * 
	 *   byteArr.position = 0;
	 * 
	 *   try {
	 * trace(byteArr.readBoolean()); // false
	 * } 
	 * catch(e:EOFError) {
	 * trace(e);           // EOFError: Error #2030: End of file was encountered.
	 * }
	 * 
	 *   try {
	 * trace(byteArr.readDouble());    // 3.141592653589793
	 * } 
	 * catch(e:EOFError) {
	 * trace(e);           // EOFError: Error #2030: End of file was encountered.
	 * }
	 * 
	 *   try {
	 * trace(byteArr.readDouble());
	 * } 
	 * catch(e:EOFError) {
	 * trace(e);        // EOFError: Error #2030: End of file was encountered.
	 * }
	 * }
	 * }
	 * }
	 * </codeblock>
	 * @langversion	3.0
	 * @playerversion	Flash 9
	 * @playerversion	Lite 4
	 */
	public interface IDataOutput
	{
		/**
		 * 数据的字节顺序：为 Endian 类中的 BIG_ENDIAN 或 LITTLE_ENDIAN 常量。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 */
		function get endian () : String;
		function set endian (type:String) : void;

		/**
		 * 用于确定在使用 writeObject() 方法写入或读取二进制数据时是使用 AMF3 格式还是 AMF0 格式。该值为 ObjectEncoding 类中的常数。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 */
		function get objectEncoding () : uint;
		function set objectEncoding (version:uint) : void;

		/**
		 * 写入布尔值。根据 value 参数写入单个字节。如果为 true，则写入 1，如果为 false，则写入 0。
		 * @param	value	确定写入哪个字节的布尔值。如果该参数为 true，则写入 1；如果为 false，则写入 0。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 * @internal	throws IOError An I/O error occurred?
		 */
		function writeBoolean (value:Boolean) : void;

		/**
		 * 写入一个字节。使用了该参数的低 8 位；忽略了高 24 位。
		 * @param	value	一个整型字节值。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 * @internal	throws IOError An I/O error occurred?
		 */
		function writeByte (value:int) : void;

		/**
		 * 在指定的字节数组 bytes 中，从 offset（使用从零开始的索引）指定的字节开始，向文件流、字节流或字节数组中写入一个长度由 length 指定的字节序列。
		 * 
		 *   如果省略 length 参数，则使用默认长度 0 并从 offset 开始写入整个缓冲区。如果还省略了 offset 参数，则写入整个缓冲区。 如果 offset 或 length 参数超出范围，它们将被锁定到 bytes 数组的开头和结尾。
		 * @param	bytes	要写入的字节数组。
		 * @param	offset	从零开始的索引，指定在数组中开始写入的位置。
		 * @param	length	一个无符号整数，指定在缓冲区中的写入范围。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 * @internal	throws IOError An I/O error occurred?
		 */
		function writeBytes (bytes:ByteArray, offset:uint=0, length:uint=0) : void;

		/**
		 * 写入 IEEE 754 双精度（64 位）浮点数。
		 * @param	value	双精度（64 位）浮点数。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 * @internal	throws IOError An I/O error occurred?
		 */
		function writeDouble (value:Number) : void;

		/**
		 * 写入 IEEE 754 单精度（32 位）浮点数。
		 * @param	value	单精度（32 位）浮点数。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 * @internal	throws IOError An I/O error occurred?
		 */
		function writeFloat (value:Number) : void;

		/**
		 * 写入一个带符号的 32 位整数。
		 * @param	value	一个带符号的整型字节值。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 * @internal	throws IOError An I/O error occurred?
		 */
		function writeInt (value:int) : void;

		/**
		 * 使用指定的字符集将多字节字符串写入文件流、字节流或字节数组中。
		 * @param	value	要写入的字符串值。
		 * @param	charSet	表示要使用的字符集的字符串。可能的字符集字符串包括 "shift-jis"、"cn-gb"、"iso-8859-1"”等。有关完整列表，请参阅支持的字符集。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 */
		function writeMultiByte (value:String, charSet:String) : void;

		/**
		 * 以 AMF 序列化格式将对象写入文件流、字节流或字节数组中。
		 * @param	object	要进行序列化处理的对象。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 * @internal	throws IOError An I/O error occurred?
		 */
		function writeObject (object:*) : void;

		/**
		 * 写入一个 16 位整数。使用了该参数的低 16 位；忽略了高 16 位。
		 * @param	value	一个整型字节值。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 * @internal	throws IOError An I/O error occurred?
		 */
		function writeShort (value:int) : void;

		/**
		 * 写入一个无符号的 32 位整数。
		 * @param	value	一个无符号的整型字节值。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 * @internal	throws IOError An I/O error occurred?
		 */
		function writeUnsignedInt (value:uint) : void;

		/**
		 * 将 UTF-8 字符串写入文件流、字节流或字节数组中。先写入以字节表示的 UTF-8 字符串长度（作为 16 位整数），然后写入表示字符串字符的字节。
		 * @param	value	要写入的字符串值。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 * @internal	throws IOError An I/O error occurred?
		 * @throws	RangeError 如果长度大于 65535。
		 */
		function writeUTF (value:String) : void;

		/**
		 * 写入一个 UTF-8 字符串。类似于 writeUTF()，但不使用 16 位长度的词为字符串添加前缀。
		 * @param	value	要写入的字符串值。
		 * @langversion	3.0
		 * @playerversion	Flash 9
		 * @playerversion	Lite 4
		 * @internal	throws IOError An I/O error occurred?
		 */
		function writeUTFBytes (value:String) : void;
	}
}