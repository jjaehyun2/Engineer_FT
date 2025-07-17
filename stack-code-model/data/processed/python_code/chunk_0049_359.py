package
{
	import app.AppContainer;
	
	import org.hammerc.collections.ArrayCollection;
	import org.hammerc.components.ItemRenderer;
	import org.hammerc.components.List;
	
	[SWF(width=800, height=600)]
	public class ListTest extends AppContainer
	{
		public function ListTest()
		{
			super(false);
		}
		
		override protected function createChildren():void
		{
			super.createChildren();
			
			var source:Array = [];
			for (var i:int = 0; i < 20; i++) 
			{
				source.push({text:"数据 " + i});
			}
			
			var ac:ArrayCollection = new ArrayCollection(source);
			
			var list:List = new List();
			list.itemRenderer = ItemRenderer;
			list.labelField = "text";
			list.useVirtualLayout = true;
			list.horizontalCenter = list.verticalCenter = 0;
			list.width = 150;
			list.height = 200;
			addElement(list);
			
			list.dataProvider = ac;
		}
	}
}