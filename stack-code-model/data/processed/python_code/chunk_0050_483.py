package
{
	import app.AppContainer;
	
	import org.hammerc.components.Button;
	import org.hammerc.components.CheckBox;
	import org.hammerc.components.Group;
	import org.hammerc.components.RadioButton;
	import org.hammerc.components.RadioButtonGroup;
	import org.hammerc.components.ToggleButton;
	import org.hammerc.layouts.HorizontalAlign;
	import org.hammerc.layouts.VerticalLayout;
	
	[SWF(width=800, height=600)]
	public class ButtonTest extends AppContainer
	{
		public function ButtonTest()
		{
			super(false);
		}
		
		override protected function createChildren():void
		{
			super.createChildren();
			
			var layout:VerticalLayout = new VerticalLayout();
			layout.gap = 5;
			layout.horizontalAlign = HorizontalAlign.CENTER;
			
			var group:Group = new Group();
			group.horizontalCenter = 0;
			group.verticalCenter = 0;
			group.layout = layout;
			addElement(group);
			
			var button:Button = new Button();
			button.label = "我是按钮";
			group.addElement(button);
			
			var toggleButton:ToggleButton = new ToggleButton();
			toggleButton.label = "我是选择按钮";
			group.addElement(toggleButton);
			
			var checkBox:CheckBox = new CheckBox();
			checkBox.label = "我是复选框";
			group.addElement(checkBox);
			
			var radioButtonGroup:RadioButtonGroup = new RadioButtonGroup();
			
			var radioButton:RadioButton = new RadioButton();
			radioButton.label = "我是单选按钮1";
			radioButton.group = radioButtonGroup;
			group.addElement(radioButton);
			
			radioButton = new RadioButton();
			radioButton.label = "我是单选按钮2";
			radioButton.group = radioButtonGroup;
			group.addElement(radioButton);
			
			radioButton = new RadioButton();
			radioButton.label = "我是单选按钮3";
			radioButton.group = radioButtonGroup;
			group.addElement(radioButton);
		}
	}
}