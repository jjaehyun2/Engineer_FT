package com.stuffwithstuff.bantam
{
	import flash.utils.Dictionary;

	/**
	 * @author Simon Richardson - me@simonrichardson.info
	 */
	public final class Lexer implements Iterator
	{

		private const _punctuators : Dictionary = new Dictionary();

		private var _text : String;

		private var _index : int = 0;

		/**
		 * Creates a new Lexer to tokenize the given string.
		 * @param text String to tokenize.
		 */
		public function Lexer(text : String)
		{
			_index = 0;
			_text = text;

			// Register all of the TokenTypes that are explicit punctuators.
			const total : int = TokenType.values.length;
			for(var i : int = 0; i<total; i++)
			{
				const type : TokenType = TokenType.values[i];
				var punctuator : String = type.punctuator;
				if (punctuator != null)
				{
					_punctuators[punctuator] = type;
				}
			}
		}

		public function hasNext() : Boolean
		{
			return true;
		}

		public function get next() : Token
		{
			while (_index < _text.length)
			{
				var c : String = _text.charAt(_index++);
				var chr : int = c.charCodeAt(0);
				
				if (_punctuators[c])
				{
					// Handle punctuation.
					return new Token(_punctuators[c], c);
				}
				else if (chr >= 97 && chr <= 122)
				{
					// Handle names.
					var start : int = _index - 1;
					while (_index < _text.length)
					{
						c = _text.charAt(_index);
						chr = c.charCodeAt(0);
						if (!(chr >= 97 && chr <= 122)) break;
						_index++;
					}

					const name : String = _text.substring(start, _index);
					return new Token(TokenType.NAME, name);
				}
				else
				{
					// Ignore all other characters (whitespace, etc.)
				}
			}
			
			// Once we've reached the end of the string, just return EOF tokens. We'll
			// just keeping returning them as many times as we're asked so that the
			// parser's lookahead doesn't have to worry about running out of tokens.
			return new Token(TokenType.EOF, "");
		}
	}
}