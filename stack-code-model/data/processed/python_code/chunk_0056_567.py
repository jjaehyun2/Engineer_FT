package parser
{
	public class JspParser extends SyntaxParserBase
	{
		public function JspParser(editor:TextFieldBase, baseIndex:uint = 0, length:int = -1)
		{
			super(editor, baseIndex, length);
		}
		
		public override function process() : void{
			var array:Array = null;
			var regex:RegExp = null;
			var beginIndex : int = 0;
			var endIndex : int = 0;
			var i : uint;
			var text : String = null;
			var attributes : String = null;
			
			super.setColor( 0x000000, 0, super.getLength());			
			
			// normal tags
			regex = /\<(\s?)((\w|\/)+\s.*?([^\%]>))|(\<(\s?)(\w|\/)+([^\%]>))/sm;
			array = super.search(regex);
			for( i = 0; i < array.length; i++){
				beginIndex = array[i].beginIndex;
				endIndex = array[i].endIndex;

				super.setColor( 0x000080, beginIndex, endIndex);
			}
			
			// tag with prefix
			regex = /\<(\s?)((\w|\/)+\:\w.*?([^\%]>))/sm;
			array = super.search(regex);
			for( i = 0; i < array.length; i++){
				beginIndex = array[i].beginIndex;
				endIndex = array[i].endIndex;
				
				super.setColor( 0xCE6500, beginIndex, endIndex);
			}
			
			// server tag <%@ %>
			regex = /(\<\%\@(.*?)\%\>)/sm;
			array = super.search(regex);
			for( i = 0; i < array.length; i++){
				beginIndex = array[i].beginIndex;
				endIndex = array[i].endIndex;
				
				super.setColor( 0x800000, beginIndex+3, endIndex-2);
				
				super.setColor( 0xFF0000, beginIndex, beginIndex+3);
				super.setColor( 0xFF0000, endIndex-2, endIndex);		
			}
			
			// styles
			regex = /(\<(\s*)style.*?\<(\s*)\/(\s*)style(\s*)\>)/sm;
			array = super.search(regex);
			for( i = 0; i < array.length; i++){
				beginIndex = array[i].beginIndex;
				endIndex = array[i].endIndex;
				super.setColor( 0x900090, beginIndex, endIndex);
				text = super.getString();
				beginIndex = text.indexOf('>', beginIndex) + 1;
				while( text.charAt(--endIndex) != '<' );
				
				attributes = text.substring(  array[i].beginIndex, beginIndex).toLowerCase();
				
				var cssParser : CssParser = new CssParser( super.m_Editor, beginIndex, endIndex-beginIndex);
				cssParser.process();
			}
			
			// scripts
			regex = /(\<(\s*)script.*?\<(\s*)\/(\s*)script(\s*)\>)/sm;
			array = super.search(regex);
			for( i = 0; i < array.length; i++){
				beginIndex = array[i].beginIndex;
				endIndex = array[i].endIndex;
				super.setColor( 0x840000, beginIndex, endIndex);
				text = super.getString();
				beginIndex = text.indexOf('>', beginIndex) + 1;
				while( text.charAt(--endIndex) != '<' );
				
				attributes = text.substring(  array[i].beginIndex, beginIndex).toLowerCase();
				
				var subParser : SyntaxParserBase = null;
				var regExp : RegExp = /\blanguage\=(?<quote>\"|\')(?<language>.*?)(\k<quote>)/smi;
				var results : Array = regExp.exec(attributes);
				if( results != null && results.length > 3 ){
					switch(results[2].toString().toLowerCase()){
						case "javascript":
						case "jscript":
							subParser = new JavascriptParser( super.m_Editor, beginIndex, endIndex-beginIndex);
							break;
						case "vbscript":
							subParser = new VbscriptParser( super.m_Editor, beginIndex, endIndex-beginIndex);
							break;
					}
				}
				
				
				if( subParser == null ){
					regExp = /\btype\=(?<quote>\"|\')(?<type>.*?)(\k<quote>)/smi;
					results = regExp.exec(attributes);
					if( results != null && results.length > 3 ){
						switch(results[2].toString().toLowerCase()){
							case "text/javascript":
							case "text/jscript":
								subParser = new JavascriptParser( super.m_Editor, beginIndex, endIndex-beginIndex);
								break;
							case "text/c#":
								subParser = new CSharpParser( super.m_Editor, beginIndex, endIndex-beginIndex);
								break;
						}
					}
				}
				
				if( subParser == null ){
					subParser = new JavascriptParser( super.m_Editor, beginIndex, endIndex-beginIndex);				
				}
				
				subParser.process();
			}
					
			// atributes double quote
			regex = /\=(\"[^\r|\n|\"]*\")/sm;
			array = super.search(regex);
			for( i = 0; i < array.length; i++){
				beginIndex = array[i].beginIndex;
				endIndex = array[i].endIndex;
				super.setColor( 0x0000FF, beginIndex, endIndex);
			}
			
			// atributes single quote
			regex = /\=(\'[^\r|\n|\']*\')/sm;
			array = super.search(regex);
			for( i = 0; i < array.length; i++){
				beginIndex = array[i].beginIndex;
				endIndex = array[i].endIndex;
				super.setColor( 0x0000FF, beginIndex, endIndex);
			}	

			// html comments <!-- -->
			regex = /(\<\!\-\-.*?\-\-\>)/sm;
			array = super.search(regex);
			for( i = 0; i < array.length; i++){
				beginIndex = array[i].beginIndex;
				endIndex = array[i].endIndex;
				super.setColor( 0x666666, beginIndex, endIndex);
			}
			
			// html doctype <!DOCTYPE >
			regex = /(\<\!\DOCTYPE.*?\>)/smi;
			array = super.search(regex);
			for( i = 0; i < array.length; i++){
				beginIndex = array[i].beginIndex;
				endIndex = array[i].endIndex;
				super.setColor( 0x666666, beginIndex, endIndex);
			}	

			
			// server tag <%! %> <%= %> <% %>
			regex = /(\<\%[^\@](.*?)\%\>)/sm;
			array = super.search(regex);
			for( i = 0; i < array.length; i++){
				beginIndex = array[i].beginIndex;
				endIndex = array[i].endIndex;
								
				super.setColor( 0xFF0000, beginIndex, endIndex);
				
				text = super.getString();
				var code : String = text.substring(beginIndex, endIndex);
				if( code.search( /^\<\%(\!|\=)/s ) == 0 )
					beginIndex = beginIndex+3;
				else
					beginIndex = beginIndex+2;
				while( text.charAt(--endIndex) != '%' );
				
				new JavaParser( super.m_Editor, beginIndex, endIndex-beginIndex).process();
			}
			
			// server comments <%-- --%>
			regex = /(\<\%\-\-.*?\-\-\%\>)/sm;
			array = super.search(regex);
			for( i = 0; i < array.length; i++){
				beginIndex = array[i].beginIndex;
				endIndex = array[i].endIndex;
				super.setColor(0x006600, beginIndex, endIndex);
			}
		}
	}
}