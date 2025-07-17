package com.stuffwithstuff.bantam.parselets
{
	import com.stuffwithstuff.bantam.ParseException;
	import com.stuffwithstuff.bantam.Parser;
	import com.stuffwithstuff.bantam.Precedence;
	import com.stuffwithstuff.bantam.Token;
	import com.stuffwithstuff.bantam.expressions.AssignExpression;
	import com.stuffwithstuff.bantam.expressions.Expression;
	import com.stuffwithstuff.bantam.expressions.NameExpression;

	/**
	 * @author Simon Richardson - me@simonrichardson.info
	 */
	public final class AssignParselet  implements InfixParselet
	{

		public function parse(parser : Parser, left : Expression, token : Token) : Expression
		{
			const right : Expression = parser.parseExpressionBy(Precedence.ASSIGNMENT - 1);

			if (!(left is NameExpression)) 
				throw new ParseException("The left-hand side of an assignment must be a name.");

			const name : String = NameExpression(left).name;
			return new AssignExpression(name, right);
		}

		public function get precedence() : int
		{
			return Precedence.ASSIGNMENT;
		}
	}
}