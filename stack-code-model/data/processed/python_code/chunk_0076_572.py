package com.tourism_in_lviv.air.view.ui.component
{
	
	import flash.system.Capabilities;
	
	import spark.components.BorderContainer;
	import spark.components.Image;
	import spark.components.Label;
	import spark.components.supportClasses.SkinnableComponent;
	
	
	
	/**
	 * 
	 * @author Ihor Khomiak
	 */
	public class ComponentDescriptionInfo extends SkinnableComponent
	{
		
		[SkinPart( required = "true" )]
		/**
		 * 
		 * @default 
		 */
		public var img:Image;
		
		[SkinPart( required = "true" )]
		/**
		 * 
		 * @default 
		 */
		public var imgContainer:BorderContainer;

		[SkinPart( required = "true" )]
		/**
		 * 
		 * @default 
		 */
		public var lblTitle:Label;

		[SkinPart( required = "true" )]
		/**
		 * 
		 * @default 
		 */
		public var lblDescription:Label;
		
		[SkinPart( required = "true" )]
		/**
		 * 
		 * @default 
		 */
		public var lblAddressLabel:Label;

		[SkinPart( required = "true" )]
		/**
		 * 
		 * @default 
		 */
		public var lblAddressValue:Label;
		
		/**
		 * 
		 */
		public function ComponentDescriptionInfo()
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
			
			switch(instance)
			{
				case img:
					if( Capabilities.screenResolutionX >= 520 )
						img.width = 480;
					break;
				
				case imgContainer:
					if( Capabilities.screenResolutionX >= 520 )
						imgContainer.width = 480;
					break;
			}
		}
		
		override protected function partRemoved(partName:String, instance:Object) : void
		{
			super.partRemoved(partName, instance);
		}
		
	}
}