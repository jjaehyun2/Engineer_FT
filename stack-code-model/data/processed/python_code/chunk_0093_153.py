package com.tourism_in_lviv.air.view.ui.component
{
	
	import spark.components.supportClasses.SkinnableComponent;
	
	/**
	 * 
	 * @author Ihor Khomiak
	 */
	public class ComponentHomeView extends SkinnableComponent
	{
		/**
		 * 
		 */
		public function ComponentHomeView()
		{
			super();
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