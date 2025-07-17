package com.stuffwithstuff.bantam
{
	/**
	 * @author Simon Richardson - me@simonrichardson.info
	 */
	public final class TokenType
	{

		public static const LEFT_PAREN : TokenType = new TokenType("left_paren");

		public static const RIGHT_PAREN : TokenType = new TokenType("right_paren");

		public static const COMMA : TokenType = new TokenType("comma");

		public static const ASSIGN : TokenType = new TokenType("assign");

		public static const PLUS : TokenType = new TokenType("plus");

		public static const MINUS : TokenType = new TokenType("minus");

		public static const ASTERISK : TokenType = new TokenType("asterisk");

		public static const SLASH : TokenType = new TokenType("slash");

		public static const CARET : TokenType = new TokenType("caret");

		public static const TILDE : TokenType = new TokenType("tilde");

		public static const BANG : TokenType = new TokenType("bang");

		public static const QUESTION : TokenType = new TokenType("question");

		public static const COLON : TokenType = new TokenType("colon");

		public static const NAME : TokenType = new TokenType("name");

		public static const EOF : TokenType = new TokenType("eof");
		
		public static const values : Vector.<TokenType> = Vector.<TokenType>([LEFT_PAREN, RIGHT_PAREN, COMMA, ASSIGN, PLUS, MINUS, ASTERISK, SLASH, CARET, TILDE, BANG, QUESTION, COLON, NAME, EOF]);
		
		private var _type : String;

		public function TokenType(type : String)
		{
			_type = type;
		}

		public function get punctuator() : String
		{
			switch(this)
			{
				case LEFT_PAREN:
					return '(';
				case RIGHT_PAREN:
					return ')';
				case COMMA:
					return ',';
				case ASSIGN:
					return '=';
				case PLUS:
					return '+';
				case MINUS:
					return '-';
				case ASTERISK:
					return '*';
				case SLASH:
					return '/';
				case CARET:
					return '^';
				case TILDE:
					return '~';
				case BANG:
					return '!';
				case QUESTION:
					return '?';
				case COLON:
					return ':';
				default:
					return null;
			}
		}

		public function toString() : String
		{
			return "[TokenType (type: " + _type + ")]";
		}
	}
}