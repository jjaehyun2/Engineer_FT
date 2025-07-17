package flatSpark.components
{
	
	import spark.components.Panel;
	import spark.core.IDisplayText;
	
	
	public class PanelWithSub extends Panel
	{
		
		public function PanelWithSub()
		{
			super();
		}
		
		
		//----------------------------------
		//  titleField
		//---------------------------------- 
		
		[SkinPart(required="false")]
		public var subTitleDisplay:IDisplayText;
		
		//----------------------------------
		//  subTitle
		//----------------------------------
		
		/**
		 *  @private
		 */
		private var _subTitle:String = "";
		
		/**
		 *  @private
		 */
		private var subTitleChanged:Boolean;
		
		[Bindable]
		[Inspectable(category="General", defaultValue="")]
		
		public function get subTitle():String 
		{
			return _subTitle;
		}
		
		/**
		 *  @private
		 */
		public function set subTitle(value:String):void 
		{
			_subTitle = value;
			
			if (subTitleDisplay)
				subTitleDisplay.text = subTitle;
		}
		
		override protected function getCurrentSkinState():String
		{
			return super.getCurrentSkinState();
		} 
		
		override protected function partAdded(partName:String, instance:Object) : void
		{
			super.partAdded(partName, instance);
			if (instance == subTitleDisplay)
			{
				subTitleDisplay.text = subTitle;
			}
		}
		
		override protected function partRemoved(partName:String, instance:Object) : void
		{
			super.partRemoved(partName, instance);
		}
		
	}
}