package devoron.dataui.multicontainers.timeline
{
	import devoron.dataui.DataContainerForm;
	import devoron.dataui.multicontainers.table.DataContainersTableForm;
	import devoron.dataui.multicontainers.timeline.TimelineTrackForm;
	import devoron.dataui.multicontainers.timeline.TimelineModel;
	import devoron.data.core.base.ISerializeObserver;
	import devoron.dataui.multicontainers.table.IContainersControlPanel;
	import devoron.dataui.multicontainers.timeline.TimelineTrackRenderer;
	import devoron.studio.core.managers.keyboard.IKeyboardManager;
	import devoron.studio.core.managers.keyboard.IKeyboardManagerProvider;
	import devoron.components.keyboardshortcuts.KeyboardShortcut;
	import devoron.components.multicontainers.timeline.TimelineTrackRenderer;
	import devoron.data.core.base.DataStructur;
	import devoron.studio.core.workspace.components.dashboard.IDashboardComponent;
	import org.aswing.geom.IntDimension;
	import org.aswing.Icon;
	import org.aswing.JTable;
	import org.aswing.KeyboardManager;
	import org.aswing.table.DefaultTableModel;
	import org.aswing.table.GeneralTableCellFactory;
	import org.aswing.table.TableCellFactory;
	//import devoron.components.multicontainers.timeline.components.CreateLabelForm;
	//import devoron.components.multicontainers.timeline.components.TimelineLabelFactory;
	
	/**
	 * TimelinePanel.
	 * @author Devoron
	 */
	public class TimelinePanel extends DataContainersTableForm implements IDashboardComponent, IKeyboardManagerProvider, ISerializeObserver /*, IPlugin*/
	{
		private const MATERIAL_ICON:String = "../assets/icons/material_icon20.png";
		
		public function TimelinePanel(supportedTimelineLabelClasses:Array, supportedTimelineTrackClasses:Array = null, dataContainerName:String = "", dataContainerType:String = "", dataContainerIcon:Icon = null, dataCollectionMode:String = DataContainerForm.SINGLE_COMPONENT_DATA_COLLECTION, oneMinimum:Boolean = true, showTable:Boolean = false, containersPanel:IContainersControlPanel = null)
		{
			if (supportedTimelineTrackClasses)
			{
				if (supportedTimelineTrackClasses.length == 0)
					supportedTimelineTrackClasses = [TimelineTrackForm];
			}
			else
			{
				supportedTimelineTrackClasses = [TimelineTrackForm];
			}
			
			super(supportedTimelineTrackClasses, dataContainerName, dataContainerType, dataContainerIcon, dataCollectionMode, oneMinimum, showTable, containersPanel);
			
			var timelineModel:TimelineModel = new TimelineModel();
			setTimelineModel(timelineModel);
			containersTable.setTableHeader(null);
			containersTableScP.setPreferredSize(new IntDimension(950, 200));
			setTimelineTrackFactory("modifier", new GeneralTableCellFactory(TimelineTrackRenderer));
			
			containersTable.setSelectionMode(JTable.MULTIPLE_SELECTION);
		
		/*	addContainerBtnHandler(null);
		   addContainerBtnHandler(null);
		 addContainerBtnHandler(null);*/
		}
		
		public function setTimelineModel(model:DefaultTableModel):void
		{
			setModel(model);
		}
		
		public function getTimelineModel():DefaultTableModel
		{
			return getModel();
		}
		
		public function setTimelineTrackFactory(trackType:String, factory:TableCellFactory):void
		{
			containersTable.setDefaultCellFactory("TimelineTrack", factory);
		}
		
		public function getTimelineTrackFactory(trackType:String):TableCellFactory
		{
			return containersTable.getDefaultCellFactory(trackType);
		}
		
		/*public function getTimelineLabelFactory():ITimelineLabelFactory
		   {
		   //return CreateLabelForm.getInstance().getTimelineLabelFactory();
		   return null;
		   }
		
		   public function setTimelineLabelFactory(factory:ITimelineLabelFactory):void
		   {
		   //CreateLabelForm.getInstance().setTimelineLabelFactory(factory);
		 }*/
		
		/* INTERFACE devoron.studio.core.IKeyboardManagerProvider */
		
		public function setKeyboardManager(keyboardManager:IKeyboardManager):void
		{
			var containers:Array = containerForms.values();
			for each (var container:*in containers)
			{
				if (container is IKeyboardManagerProvider)
					container.setKeyboardManager(keyboardManager);
			}
		}
		
		public function keyboardManagerOn():void
		{
			var containers:Array = containerForms.values();
			for each (var container:*in containers)
			{
				if (container is IKeyboardManagerProvider)
					container.keyboardManagerOn();
			}
		}
		
		public function keyboardManagerOff():void
		{
			var containers:Array = containerForms.values();
			for each (var container:*in containers)
			{
				if (container is IKeyboardManagerProvider)
					container.keyboardManagerOff();
			}
		}
		
		public function getKeyboardShortcuts():Vector.<KeyboardShortcut>
		{
			return null;
		}
		
		/* INTERFACE devoron.data.core.ISerializeObserver */
		
		public function setSerializedData(source:DataStructur, data:String):void
		{
		/*var _modificators:Array = modificators.values();
		   for each (var modificator:*in _modificators)
		   {
		   if (modificator is ISerializeObserver)
		   modificator.setSerializedData(source, data);
		 }*/
		}
	
	}

}