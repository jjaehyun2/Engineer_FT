package edu.isi.bmkeg.kefed.editor.bin
{	
	import edu.isi.bmkeg.kefed.editor.KefedDataEditorModule;
		
	import flash.display.DisplayObjectContainer;
	
	import org.robotlegs.core.IInjector;
	
	import org.robotlegs.utilities.modular.mvcs.ModuleContext;
	
	public class kefedDataEditorContext extends ModuleContext
	{

		override public function startup():void
		{
			viewMap.mapType(KefedDataEditorModule);		
		}
		
	}
	
}