package widgets.PMGD.Skin
{
	
	import mx.events.FlexEvent;
	
	import spark.components.supportClasses.SkinnableComponent;
	
	
	
	public class Inicio extends SkinnableComponent
	{
		
		public function Inicio()
		{
			setStyle("skinClass", InicioSkin);
			this.addEventListener(FlexEvent.CREATION_COMPLETE,creationComplete);
			//super();
		}
		public function creationComplete(e:FlexEvent):void{
		
		}
		
		override protected function getCurrentSkinState():String
		{
			return super.getCurrentSkinState();
		} 
		
		override protected function partAdded(partName:String, instance:Object) : void
		{
			super.partAdded(partName, instance);
		}
		
		override protected function partRemoved(partName:String, instance:Object) : void
		{
			super.partRemoved(partName, instance);
		}
		
	}
}