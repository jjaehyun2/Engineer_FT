package org.osflash.css.geom
{
	import org.osflash.css.data.CSSConvertableValue;
	import org.osflash.stream.IStreamOutput;
	import org.osflash.stream.IStreamWriter;
	/**
	 * @author Simon Richardson - simon@ustwo.co.uk
	 */
	public class CSSPoint implements IStreamWriter
	{
		/**
		 * @private
		 */
		private var _x : CSSConvertableValue;
		
		/**
		 * @private
		 */
		private var _y : CSSConvertableValue;
		
		public function CSSPoint()
		{
			_x = new CSSConvertableValue();
			_y = new CSSConvertableValue();
		}
		
		public function setValues(...rest) : void
		{
			const total : int = rest.length;
			if(total == 1)
			{
				x = rest[0];
				y = rest[0];
			}
			else if(total == 2)
			{
				x = rest[0];
				y = rest[1];
			}
			else throw new ArgumentError('Invalid number of arguments sent');
		}
		
		/**
		 * @inheritDoc
		 */
		public function write(stream : IStreamOutput) : void
		{
			stream.writeUTF(x + ' ' + y);
		}
		
		public function hasValidProperties() : Boolean
		{
			return null != x || null != y;
		}
		
		public function get value() : String { return x + ' ' + y; }
		public function set value(arg : String) : void { setValues.apply(null, arg.split(' ')); }
				
		public function get x() : * { return _x.value; }
		public function set x(value : *) : void { _x.value = value; }

		public function get y() : * { return _y.value; }
		public function set y(value : *) : void { _y.value = value; }
		
	}
}