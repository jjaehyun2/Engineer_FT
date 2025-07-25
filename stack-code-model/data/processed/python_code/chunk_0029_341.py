////////////////////////////////////////////////////////////////////////////////
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
// http://www.apache.org/licenses/LICENSE-2.0 
// 
// Unless required by applicable law or agreed to in writing, software 
// distributed under the License is distributed on an "AS IS" BASIS, 
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and 
// limitations under the License
// 
// No warranty of merchantability or fitness of any kind. 
// Use this software at your own risk.
// 
////////////////////////////////////////////////////////////////////////////////
package actionScripts.plugin.syntax
{
    import flash.text.engine.ElementFormat;
    import flash.text.engine.FontDescription;
    
    import actionScripts.events.EditorPluginEvent;
    import actionScripts.plugin.IEditorPlugin;
    import actionScripts.plugin.PluginBase;
    import actionScripts.ui.parser.PythonLineParser;
    import actionScripts.valueObjects.ConstantsCoreVO;
    import actionScripts.valueObjects.Settings;
	
	public class PythonSyntaxPlugin extends PluginBase implements IEditorPlugin
	{
		private var formats:Object = {};
		
		override public function get name():String 			{return "Python Syntax Plugin";}
		override public function get author():String 		{return ConstantsCoreVO.MOONSHINE_IDE_LABEL +" Project Team";}
		override public function get description():String 	{return "Provides highlighting for Python.";}
		
		override public function activate():void
		{ 
			super.activate();
			init();
		}
		
		private function init():void
		{
			var fontDescription:FontDescription = Settings.font.defaultFontDescription;
			var fontSize:Number = Settings.font.defaultFontSize;
			
			formats[0] = /* default, parser fault */			new ElementFormat(fontDescription, fontSize, 0xFF0000);
			formats[PythonLineParser.PY_CODE] =					new ElementFormat(fontDescription, fontSize, 0x101010);
			formats[PythonLineParser.PY_STRING1] = 				
			formats[PythonLineParser.PY_STRING2] = 				new ElementFormat(fontDescription, fontSize, 0xca2323);
			formats[PythonLineParser.PY_COMMENT] =					 
			formats[PythonLineParser.PY_MULTILINE_COMMENT] = 	new ElementFormat(fontDescription, fontSize, 0x39c02f);
			formats[PythonLineParser.PY_KEYWORD] = 				new ElementFormat(fontDescription, fontSize, 0x0082cd);
			formats[PythonLineParser.PY_FUNCTION_KEYWORD] =		new ElementFormat(fontDescription, fontSize, 0x3382dd);
			formats[PythonLineParser.PY_PACKAGE_CLASS_KEYWORDS] = 	new ElementFormat(fontDescription, fontSize, 0xa848da);
			formats['lineNumber'] =								new ElementFormat(fontDescription, fontSize, 0x888888);
			formats['breakPointLineNumber'] =					new ElementFormat(fontDescription, fontSize, 0xffffff);
			formats['breakPointBackground'] =					0xdea5dd;
			formats['tracingLineColor']=						0xc6dbae;
			
			dispatcher.addEventListener(EditorPluginEvent.EVENT_EDITOR_OPEN, handleEditorOpen);
		}
		
		private function handleEditorOpen(event:EditorPluginEvent):void
		{
			if (event.fileExtension == "py")
			{
				event.editor.setParserAndStyles(new PythonLineParser(), formats);
			}
		}
		
	}
	
}