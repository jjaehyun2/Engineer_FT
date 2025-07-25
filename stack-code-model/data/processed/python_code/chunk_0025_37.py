package org.osflash.html.builders.elements.common
{
	import org.osflash.html.element.IHTMLNode;
	/**
	 * @author Simon Richardson - simon@ustwo.co.uk
	 */
	public interface IHTMLRawTextNode extends IHTMLNode
	{
		
		function get text() : String;
		function set text(value : String) : void;
	}
}