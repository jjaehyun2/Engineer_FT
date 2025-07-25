package org.osflash.dom.path.parser.parselets.types
{
	import org.osflash.dom.path.parser.IDOMPathParser;
	import org.osflash.dom.path.parser.expressions.IDOMPathExpression;
	import org.osflash.dom.path.parser.expressions.types.DOMPathStringExpression;
	import org.osflash.dom.path.parser.parselets.IDOMPathPrefixParselet;
	import org.osflash.dom.path.parser.tokens.DOMPathToken;
	/**
	 * @author Simon Richardson - me@simonrichardson.info
	 */
	public final class DOMPathStringParselet implements IDOMPathPrefixParselet
	{
		/**
		 * @inheritDoc
		 */
		public function parse(parser : IDOMPathParser, token : DOMPathToken) : IDOMPathExpression
		{
			return new DOMPathStringExpression(token.buffer);
		}
	}
}