package org.osflash.dom.path.parser.expressions
{
	/**
	 * @author Simon Richardson - simon@ustwo.co.uk
	 */
	public final class DOMPathExpressionType
	{

		public static const WILDCARD : DOMPathExpressionType = new DOMPathExpressionType(0x01);

		public static const ALL_DESCENDANTS : DOMPathExpressionType = new DOMPathExpressionType(0x02);

		public static const DESCENDANTS : DOMPathExpressionType = new DOMPathExpressionType(0x03);

		public static const NAME_DESCENDANTS : DOMPathExpressionType = new DOMPathExpressionType(0x04);

		public static const STRING : DOMPathExpressionType = new DOMPathExpressionType(0x05);

		public static const NAME : DOMPathExpressionType = new DOMPathExpressionType(0x06);

		public static const INDEX_ACCESS : DOMPathExpressionType = new DOMPathExpressionType(0x07);

		public static const INTEGER : DOMPathExpressionType = new DOMPathExpressionType(0x08);

		public static const NUMBER : DOMPathExpressionType = new DOMPathExpressionType(0x09);

		public static const UNSIGNED_INTEGER : DOMPathExpressionType = new DOMPathExpressionType(0x10);

		public static const INFIX_ATTRIBUTE : DOMPathExpressionType = new DOMPathExpressionType(0x11);

		public static const CALL_METHOD : DOMPathExpressionType = new DOMPathExpressionType(0x12);

		public static const GROUP : DOMPathExpressionType = new DOMPathExpressionType(0x13);

		public static const INSTANCE : DOMPathExpressionType = new DOMPathExpressionType(0x14);

		public static const INDEX_ACCESS_DESCENDANTS : DOMPathExpressionType = new DOMPathExpressionType(0x15);

		public static const ATTRIBUTE : DOMPathExpressionType = new DOMPathExpressionType(0x16);

		public static const EQUALITY : DOMPathExpressionType = new DOMPathExpressionType(0x17);

		public static const INEQUALITY : DOMPathExpressionType = new DOMPathExpressionType(0x18);

		public static const LOGICAL_AND : DOMPathExpressionType = new DOMPathExpressionType(0x19);

		public static const LOGICAL_OR : DOMPathExpressionType = new DOMPathExpressionType(0x20);

		public static const BOOLEAN : DOMPathExpressionType = new DOMPathExpressionType(0x21);

		public static const NULL : DOMPathExpressionType = new DOMPathExpressionType(0x22);

		public static const UNDEFINED : DOMPathExpressionType = new DOMPathExpressionType(0x23);

		public static const LESS_THAN : DOMPathExpressionType = new DOMPathExpressionType(0x24);

		public static const GREATER_THAN : DOMPathExpressionType = new DOMPathExpressionType(0x25);

		public static const LESS_THAN_OR_EQUAL_TO : DOMPathExpressionType = new DOMPathExpressionType(0x26);
		
		public static const GREATER_THAN_OR_EQUAL_TO : DOMPathExpressionType = new DOMPathExpressionType(0x27);

		/**
		 * @private
		 */
		private var _type : int;

		/**
		 * 
		 */
		public function DOMPathExpressionType(type : int)
		{
			_type = type;
		}

		public static function getType(type : int) : String
		{
			switch(type)
			{
				case WILDCARD.type:
					return 'wildcard';
				case ALL_DESCENDANTS.type:
					return 'allDescendants';
				case DESCENDANTS.type:
					return 'descendants';
				case NAME_DESCENDANTS.type:
					return 'nameDiscendants';
				case STRING.type:
					return 'string';
				case NAME.type:
					return 'name';
				case INDEX_ACCESS.type:
					return 'indexAccess';
				case INTEGER.type:
					return 'integer';
				case NUMBER.type:
					return 'number';
				case UNSIGNED_INTEGER.type:
					return 'unsignedInteger';
				case INFIX_ATTRIBUTE.type:
					return 'infixAttribute';
				case CALL_METHOD.type:
					return 'callMethod';
				case GROUP.type:
					return 'group';
				case INSTANCE.type:
					return 'instance';
				case INDEX_ACCESS_DESCENDANTS.type:
					return 'indexAccessDescendants';
				case ATTRIBUTE.type:
					return 'attribute';
				case EQUALITY.type:
					return 'equality';
				case INEQUALITY.type:
					return 'inequality';
				case LOGICAL_AND.type:
					return 'logicalAnd';
				case LOGICAL_OR.type:
					return 'logicalOr';
				case BOOLEAN.type:
					return 'boolean';
				case NULL.type:
					return 'null';
				case UNDEFINED.type:
					return 'undefined';
				case LESS_THAN.type:
					return 'lessThan';
				case GREATER_THAN.type:
					return 'greaterThan';
				case LESS_THAN_OR_EQUAL_TO.type:
					return 'lessThanOrEqualTo';
				case GREATER_THAN_OR_EQUAL_TO.type:
					return 'greaterThanOrEqualTo';
				default:
					throw new ArgumentError('Given argument is Unknown');
			}
		}

		/**
		 * 
		 */
		public function get type() : int
		{
			return _type;
		}
	}
}