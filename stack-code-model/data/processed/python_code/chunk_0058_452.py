package flatSpark.components
{

	import spark.components.Button;
	
	import flatSpark.enums.BrandColorEnum;
	
	[Style(name="iconFontFamily", type="String", format="String")]
	[Style(name="iconFontSize", type="Number", format="Number")]
	[Style(name="iconFontColor", type="uint", format="Color")]
	
	public class ButtonIcon extends spark.components.Button
	{

		[Bindable]
		public var iconFont:String;
		
		[Bindable]
		public var brand:int = BrandColorEnum.Default;
		
		public function ButtonIcon()
		{
			super();
		}

	}
}