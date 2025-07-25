package org.osflash.dom.path.parser.expressions.accessors
{
	import org.osflash.dom.path.parser.expressions.DOMPathExpression;
	import org.osflash.dom.path.parser.expressions.DOMPathExpressionType;
	import org.osflash.dom.path.parser.expressions.IDOMPathDescendantsExpression;
	import org.osflash.dom.path.parser.expressions.IDOMPathExpression;
	import org.osflash.dom.path.parser.expressions.IDOMPathLeftRightNodeExpression;
	import org.osflash.stream.IStreamOutput;
	/**
	 * @author Simon Richardson - me@simonrichardson.info
	 */
	public final class DOMPathInstanceExpression extends DOMPathExpression
												 implements IDOMPathDescendantsExpression,
															IDOMPathLeftRightNodeExpression
	{
		
		/**
		 * @private
		 */
		private var _left : IDOMPathExpression;
		
		/**
		 * @private
		 */
		private var _right : IDOMPathExpression;
		
		public function DOMPathInstanceExpression(	left : IDOMPathExpression,
													right : IDOMPathExpression
													)
		{
			if(null == left) throw new ArgumentError('Given left can not be null');
			if(null == right) throw new ArgumentError('Given right can not be null');
			
			_left = left;
			_right = right;
		}
		
		/**
		 * @inheritDoc
		 */
		override public function describe(stream : IStreamOutput) : void
		{
			_left.describe(stream);
			
			stream.writeUTF(".");
			
			_right.describe(stream);
		}

		/**
		 * @inheritDoc
		 */
		override public function get type() : DOMPathExpressionType
		{
			return DOMPathExpressionType.INSTANCE;
		}

		public function get descendants() : IDOMPathExpression
		{
			return _right;
		}

		public function get left() : IDOMPathExpression
		{
			return _left;
		}

		public function get right() : IDOMPathExpression
		{
			return _right;
		}
	}
}