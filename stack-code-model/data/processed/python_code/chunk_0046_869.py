package devoron.dataui.multicontainers.ddb
{
	import com.adobe.utils.ArrayUtil;
	import devoron.components.buttons.DropDownButton;
	import devoron.components.buttons.DropDownButtonGroup;
	import devoron.components.comboboxes.DSComboBox;
	import devoron.dataui.DataContainerForm;
	import devoron.data.core.base.DataStructurObject;
	import devoron.data.core.base.DefaultDataFactory;
	import devoron.studio.core.workspace.components.dashboard.IDashboardComponent;
	import flash.events.Event;
	import org.aswing.AbstractButton;
	import org.aswing.ButtonGroup;
	import org.aswing.Component;
	import org.aswing.EmptyIcon;
	import org.aswing.event.AWEvent;
	import org.aswing.geom.IntDimension;
	import org.aswing.Icon;
	import org.aswing.JCheckBox;
	import org.aswing.JPanel;
	import org.aswing.JToggleButton;
	import org.aswing.layout.GridLayout;
	import org.aswing.util.HashMap;
	import org.aswing.VectorListModel;
	
	/**
	 * Множественный Drop-Down-Button контейнер данных.
	 * @author Devoron
	 */
	public class DataContainersDDBButtonGroupForm extends DataContainerForm implements IDashboardComponent
	{
		private const BEHAVIOR_ICON:String = "../assets/icons/behavior_icon20.png";
		private var defaultDataFactory:DefaultDataFactory;
		private var containersButtonsPanel:JPanel;
		private var containersButtonGroup:ButtonGroup;
		protected var supportedContainerFormClasses:Array;
		protected var containersCB:DSComboBox;
		protected var containersCBModel:VectorListModel;
		protected var containersDDBGroup:DropDownButtonGroup;
		protected var containerNames:Array;
		protected var containersModel:Array;
		
		public function DataContainersDDBButtonGroupForm(supportedContainerFormClasses:Array, dataContainerName:String = "", dataContainerType:String = "", dataContainerIcon:Icon = null, dataCollectionMode:String = DataContainerForm.SINGLE_COMPONENT_DATA_COLLECTION)
		{
			super(dataContainerName, dataContainerType, dataContainerIcon, dataCollectionMode);
			this.supportedContainerFormClasses = supportedContainerFormClasses;
			
			defaultDataFactory = new DefaultDataFactory();
			containersCBModel = new VectorListModel();
			containerNames = new Array();
			containersModel = new Array();
			
			/*containersCB = new GrayCB();
			   containersCB.setModel(containersCBModel);
			   containersCB.setPreferredSize(new IntDimension(164, 24));
			   containersCB.addActionListener(behaviorsCBHandler);
			 super.addLeftHoldRow(0, containersCB);*/
			
			containersButtonsPanel = new JPanel(new GridLayout(2, 6, 3, 2));
			super.addLeftHoldRow(0, containersButtonsPanel);
			containersButtonGroup = new ButtonGroup(false, 0, true);
			
			super.addLeftHoldRow(0, [0, 5]);
			
			containersDDBGroup = new DropDownButtonGroup();
			super.addLeftHoldRow(0, containersDDBGroup);
			
			
			
			createDataContainerForms();
			
			// установить имена контейнеров в модель и сделать первый контейнер (TimeBehavior) активным
			containersCBModel.appendAll(ArrayUtil.createUniqueCopy(containerNames));
			//containersCB.setSelectedIndex(0);
			
			var comps:Object = new Object();
			comps[dataContainerType] = this;
			super.setDataContainerChangeComponents(comps);
		}
		
		public function getData():Array
		{
			var data:Array = new Array();
			var dataNames:Array = containerForms.keys();
			var container:DataContainerForm;
			for each (var dataName:String in dataNames)
			{
				container = containerForms.get(dataName);
				data.push({id: container.dataContainerName, data: container.collectDataFromContainer()});
			}
			return data;
		}
		
		public function setData(data:Object):void
		{
			var container:DataContainerForm;
			for each (var dataObject:*in data)
			{
				container = containerForms.get(dataObject.id);
				container.setDataToContainer(dataObject.data);
			}
		}
		
		public function addActionListener(listener:Function, useCapture:Boolean = false, priority:int = 0, useWeakReference:Boolean = false):void
		{
			super.addEventListener(AWEvent.ACT, listener, useCapture, priority, useWeakReference);
		}
		
		public function removeActionListener(listener:Function):void
		{
			super.removeEventListener(AWEvent.ACT, listener);
		}
		
		/* INTERFACE devoron.gameeditor.core.IDashboardComponent */
		
		public function getDashboardComponent():Component
		{
			return this;
		}
		
		public function getDashboardMinimalComponent():Component
		{
			return new JToggleButton("sh");
		}
		
		// нужно обозначить функции получения и установки значения для нестандартного компонента - SegmentedColorMiddlePointsComponent
		
		override protected function getGetValueFunction(comp:*):Function
		{
			// отдать массив данных из контейнеров
			if (comp is DataContainersDDBButtonGroupForm)
				return comp.getData;
			return super.getGetValueFunction(comp);
		}
		
		override protected function getSetValueFunction(comp:*):Function
		{
			if (comp is DataContainersDDBButtonGroupForm)
				return comp.setData;
			return super.getSetValueFunction(comp);
		}
		
		//**************************************************** ♪ ОБРАБОТЧИКИ СОБЫТИЙ ***************************************
		
		/**
		 * Обработчик выбора в комбобоксе поведения (behaviorsCB).
		 * Делает видимой разворачивающуюся кнопку данного поведения.
		 * Добавляет выбранное поведение.
		 * @param	e
		 */
		protected function behaviorButtonHandler(e:AWEvent):void
		{
			var btn:AbstractButton = e.currentTarget as AbstractButton;
			var containerName:String = btn.name;
			if (btn.isSelected())
				containersDDBGroup.showContainer(containerName);
			else
				containersDDBGroup.hideContainer(containerName);
		
			//containersDDBGroup.hideCo(containerName);
			//containersCBModel.remove(containerName);
		}
		
		/**
		 * Обработчик смены состояния чекбокса разворачивающейся кнопки поведения.
		 * @param	e
		 */
		protected function containerStateChangeHandler(e:Event):void
		{
			var behaviorName:String = (e.currentTarget.parent as DropDownButton).getText();
			if (!(e.currentTarget as JCheckBox).isSelected())
				containersCBModel.append(behaviorName);
		}
		
		/**
		 * * Обработчик нажатия кнопки закрытия разворачивающейся кнопки поведения.
		 * @param	e
		 */
		protected function behaviorRemovingHandler(e:Event):void
		{
			//var behaviorDDB:DropDownButton = (e.currentTarget.parent as DropDownButton);
			//behaviorDDB.getParent().getParent().setVisible(false);
			//behaviorDDB.hideRelatedFormRow();
			//removeBehavior(behaviorDDB.getText());
		}
		
		/**
		 * Обработчик изменения настроек выбранного материала.
		 * @param	obj
		 */
		private function containerDataChangeHandler(obj:DataStructurObject):void
		{
			/*var dataObject:Object = containersTable.getData()[containersTable.getSelectedRow()];
			   currentContainerForm.collectDataFromContainer(dataObject.data.data);
			 containersTable.dispatchEvent(new AWEvent(AWEvent.ACT));*/
			 //var dataObject:Object = dataObjects[selId];
			//currentContainerForm.collectDataFromContainer(dataObject.data.data);
			//gtrace("изменились данные в конейтенерe");
			super.dispatchEvent(new AWEvent(AWEvent.ACT));
		}
		
		//**************************************************** ☼ СОЗДАНИЕ КОМПОНЕНТОВ ***************************************	
		
		protected function createDataContainerForms(visible:Boolean = false):void
		{
			// заполнение комбобокса типами материалов, сбор дефолтных данных, создание форм-контейнеров
			var data:DataStructurObject;
			var containerForm:DataContainerForm;
			for each (var containerClass:Class in supportedContainerFormClasses)
			{
				containerForm = new containerClass();
				data = containerForm.collectDataFromContainer() as DataStructurObject;
				data.dataName = containerForm.dataContainerName;
				data.dataType = containerForm.dataContainerType;
				
				containersDDBGroup.appendButton(containerForm.dataContainerName, containerForm);
				containerNames.push(containerForm.dataContainerName);
				defaultDataFactory.registerDataStructurObject(containerForm.dataContainerName, data);
				
				containerForm.addDataChangeListener(containerDataChangeHandler, null);
				containerForms.put(containerForm.dataContainerName, containerForm);
				
				var btn:JToggleButton = createContainerButton(containerForm.dataContainerName, containerForm.dataContainerIcon);
				containersButtonsPanel.append(btn);
					//containersButtonGroup.append(btn);
			}
		}
		
		private var containerForms:HashMap = new HashMap();
		
		protected function createContainerButton(dataContainerName:String, icon:Icon = null):JToggleButton
		{
			var btn:JToggleButton = new JToggleButton("", icon ? icon : new EmptyIcon(20, 20));
			btn.setPreferredSize(new IntDimension(26, 26));
			//btn.setPreferredWidth(40);
			btn.setToolTipText(dataContainerName);
			btn.addActionListener(behaviorButtonHandler);
			btn.name = dataContainerName;
			return btn;
		}
	
	}

}