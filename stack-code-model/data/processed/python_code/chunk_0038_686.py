package
{
	import app.AppContainer;
	
	import org.hammerc.collections.ArrayCollection;
	import org.hammerc.components.ComboBox;
	import org.hammerc.components.DropDownList;
	
	[SWF(width=800, height=600)]
	public class DropDownListTest extends AppContainer
	{
		public function DropDownListTest()
		{
			super(false);
		}
		
		override protected function createChildren():void
		{
			super.createChildren();
			
			var source:Array = [];
			for (var i:int = 0; i < 40; i++) 
			{
				source.push({label:"数据 " + i});
			}
			
			var ac:ArrayCollection = new ArrayCollection(source);
			
			var dropDownList:DropDownList = new DropDownList();
			dropDownList.x = 10;
			dropDownList.y = 10;
			dropDownList.dataProvider = ac;
			addElement(dropDownList);
			
			var comboBox:ComboBox = new ComboBox();
			comboBox.x = 300;
			comboBox.y = 10;
			comboBox.dataProvider = ac;
			addElement(comboBox);
		}
	}
}