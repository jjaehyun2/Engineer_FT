package com.stuffwithstuff.bantam.parselets
{
	import com.stuffwithstuff.bantam.Parser;
	import com.stuffwithstuff.bantam.Precedence;
	import com.stuffwithstuff.bantam.Token;
	import com.stuffwithstuff.bantam.TokenType;
	import com.stuffwithstuff.bantam.expressions.CallExpression;
	import com.stuffwithstuff.bantam.expressions.Expression;

	/**
	 * @author Simon Richardson - me@simonrichardson.info
	 */
	public final class CallParselet implements InfixParselet
	{

		public function parse(parser : Parser, left : Expression, token : Token) : Expression
		{
			// Parse the comma-separated arguments until we hit, ")".
			const args : Vector.<Expression> = new Vector.<Expression>();

			// There may be no arguments at all.
			if (!parser.match(TokenType.RIGHT_PAREN))
			{
				do
				{
					args.push(parser.parseExpression());
				}
				while (parser.match(TokenType.COMMA));
				
				parser.consumeToken(TokenType.RIGHT_PAREN);
			}

			return new CallExpression(left, args);
		}

		public function get precedence() : int
		{
			return Precedence.CALL;
		}
	}
}