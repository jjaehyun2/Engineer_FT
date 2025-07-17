package devoron.dataui.propertiescontainer
{
	import devoron.dataui.DataContainerForm;
	import devoron.studio.guidesinger.TextIcon;
	import devoron.aswing.ASWingUtils;
	import devoron.components.tables.icons.IconsTable;
	import devoron.components.buttons.DSButton;
	import devoron.components.checkboxes.DSCheckBox;
	import devoron.components.icons.WatchingIcon;
	import devoron.components.labels.DSLabel;
	import devoron.components.tables.TableControlPanel;
	import devoron.components.values.color.ColorTableCellEditor;
	import devoron.components.values.color.ColorTableCellRenderer;
	import devoron.studio.core.workspace.IPropertiesPanelComponent;
	import devoron.components.tables.colors.ColorsTable;
	import org.aswing.ASColor;
	import org.aswing.border.DecorateBorder;
	import org.aswing.Component;
	import org.aswing.event.AWEvent;
	import org.aswing.geom.IntDimension;
	import org.aswing.Icon;
	import org.aswing.Insets;
	import org.aswing.JButton;
	import org.aswing.JPanel;
	import org.aswing.JScrollPane;
	import org.aswing.JToggleButton;
	import org.aswing.layout.FlowLayout;
	import org.aswing.skinbuilder.SkinToggleButtonBackground;
	import org.aswing.table.GeneralTableCellFactory;
	
	/**
	 * AbstractLAFForm
	 * @author Devoron
	 */
	public class DefaultComponentsPropertiesShema extends DataContainerForm implements IPropertiesPanelComponent
	{
		
		public function DefaultComponentsPropertiesShema(dataContainerName:String = "", dataContainerType:String = "", dataContainerIcon:Icon = null, dataCollectionMode:String = DataContainerForm.SINGLE_COMPONENT_DATA_COLLECTION, dataLiveMode:Boolean = false)
		{
			super(dataContainerName, dataContainerType, dataContainerIcon, dataCollectionMode, dataLiveMode);
			super.setPreferredWidth(580);
			super.setTextRenderer(DSLabel);
			
			//var labels:Arr
			var names:Array = ["bool", "int", "color", "image", "insets"];
			var buttons:Array = [];
			var keyValueBtn:DSButton;
			var btnsPanel:JPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
			for (var i:int = 0; i < names.length; i++)
			{
				keyValueBtn = new DSButton(names[i]);
				keyValueBtn.setPreferredSize(new IntDimension(70, 24));
				buttons.push(keyValueBtn);
				btnsPanel.append(keyValueBtn);
				keyValueBtn.addActionListener(keyValueBtnHandler);
			}
		
		/*var ico:WatchingIcon = new WatchingIcon("F:\Projects\projects\flash\studio\Studio\assets\icons\TableControlPanel\Frame_maximizeIcon_disabledImage.png", 16, 16);
		   var btn:JButton = new JButton("", ico);
		 */
		
			//var 
			//addCenterHoldRow(0, btn);
		
		}
		
		private function keyValueBtnHandler(e:AWEvent):void
		{
		
		}
		
		public function addBooleanField(key:String, defaultValue:Boolean):void
		{
			var ChB:DSCheckBox = new DSCheckBox(key);
			ChB.setSelected(defaultValue);
			super.addLeftHoldRow(0, ChB);
			var obj:Object = new Object();
			obj[key] = ChB;
			super.setDataContainerChangeComponents(obj);
		}
		
		public function addImageField(key:String, pathToImage:String):void
		{
			if (!iconsTable)
			{
				createIconsTable();
			}
			
			var images:Array = iconsTable.getIcons();
			images.push(pathToImage);
			iconsTable.setIcons(images);
		}
		
		public function addASColorUIResourceField(key:String, defaultValue:ASColor):void
		{
			//super.addLeftHoldRow(0, new Colo);
			if (!colorsTable)
			{
				createColorsTable();
			}
			
			var colors:Array = colorsTable.getColors();
			colors.push({name: key, value: defaultValue});
			colorsTable.setColors(colors);
		}
		
		public function addDecorateBorderField(key:String, skinEmptyBorder:DecorateBorder):void
		{
			//gtrace("2:" + key + "пустое место");
		}
		
		public function addDefaultsDecoratorBaseField(key:String, defaultValue:Class):void
		{
			//gtrace("2:" + key + "пустое место");
		}
		
		public function addInsetsUIResourceField(key:String, defaultValue:Insets):void
		{
			//gtrace("2:" + key + "пустое место");
		}
		
		public function addIntField(key:String, defaultValue:int):void
		{
			gtrace(key);
		}
		
		protected function createColorsTable():void
		{
			colorsTable = new ColorsTable();
			colorsTable.setDefaultEditor("Color", new ColorTableCellEditor());
			colorsTable.setDefaultCellFactory("Color", new GeneralTableCellFactory(ColorTableCellRenderer));
			colorsTableScP = ASWingUtils.supportedWithScrollPane(colorsTable, 580, 180);
			super.addLeftHoldRow(0, colorsTableScP);
			
			var colorsTableTCP:TableControlPanel = new TableControlPanel(colorsTable);
			super.addRightHoldRow(0, colorsTableTCP);
			
			super.setDataContainerChangeComponents({color: colorsTable});
		
		}
		
		protected function createIconsTable():void
		{
			iconsTable = new IconsTable();
			iconsTableScP = ASWingUtils.supportedWithScrollPane(iconsTable, 580, 180);
			super.addLeftHoldRow(0, iconsTableScP);
			super.setDataContainerChangeComponents({icons: iconsTable});
			
			var iconsTableTCP:TableControlPanel = new TableControlPanel(iconsTable);
			super.addRightHoldRow(0, iconsTableTCP);
		}
		
		protected function createSkinForm():void
		{
		
		}
		
		protected function createInsetsForm():void
		{
		
		}
		
		/* INTERFACE devoron.studio.core.IPropertiesPanelComponent */
		
		public function getDashboardComponent():Component
		{
			return this;
		}
		
		public function getDashboardMinimalComponent():Component
		{
			return new JToggleButton("dfs");
		}
	
	}

}