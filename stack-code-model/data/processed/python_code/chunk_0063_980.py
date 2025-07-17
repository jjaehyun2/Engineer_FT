package
{
	import app.AppContainer;
	
	import org.hammerc.components.Button;
	import org.hammerc.components.Panel;
	
	[SWF(width=800, height=600)]
	public class PanelTest extends AppContainer
	{
		public function PanelTest()
		{
			super(false);
		}
		
		override protected function createChildren():void
		{
			super.createChildren();
			
			var panel:Panel = new Panel();
			panel.title = "我是面板";
			panel.horizontalCenter = 0;
			panel.verticalCenter = 0;
			panel.width = 300;
			panel.height = 300;
			addElement(panel);
			
			var btn:Button = new Button();
			btn.top = 20;
			btn.horizontalCenter = 0;
			btn.label = "测试";
			panel.addElement(btn);
		}
	}
}