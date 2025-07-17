package com.stuffwithstuff.bantam.parselets
{
	import com.stuffwithstuff.bantam.Parser;
	import com.stuffwithstuff.bantam.Token;
	import com.stuffwithstuff.bantam.expressions.Expression;
	import com.stuffwithstuff.bantam.expressions.NameExpression;

	/**
	 * @author Simon Richardson - me@simonrichardson.info
	 */
	public final class NameParselet implements PrefixParselet
	{

		public function parse(parser : Parser, token : Token) : Expression
		{
			return new NameExpression(token.text);
		}
	}
}