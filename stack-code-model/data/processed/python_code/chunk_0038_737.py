package devoron.components.multicontainers.timeline.components
{
	import devoron.studio.modificators.timeline2.ITimelineLabelContainer;
	import org.aswing.layout.BorderLayout;
	import devoron.components.multicontainers.timeline.components.TimelineLabelFactory;
	import devoron.studio.modificators.timeline.DefaultTimelineLabelFactory;
	import devoron.studio.core.resources.PackagesBackGroudDecorator;
	import devoron.studio.core.Settings;
	import devoron.studio.modificators.ModifiersPlugin;
	import devoron.studio.modificators.timeline.ITimelineLabelContainer;
	import devoron.studio.modificators.timeline.TimelineLabel;
	import devoron.studio.modificators.timeline.Track;
	import devoron.studio.modificators.timeline.ITimelineLabelContainer;
	import flash.events.Event;
	import flash.events.FocusEvent;
	import flash.events.MouseEvent;
	import org.aswing.ASColor;
	import org.aswing.decorators.ColorDecorator;
	import org.aswing.event.AWEvent;
	import org.aswing.event.PopupEvent;
	import org.aswing.ext.Form;
	import org.aswing.geom.IntDimension;
	import org.aswing.JButton;
	import org.aswing.JFrame;
	import org.aswing.JNumberStepper;
	import org.aswing.JPanel;
	import org.aswing.JWindow;
	
	/**
	 * ...
	 * @author ...
	 */
	public class CreateLabelForm2 extends JFrame
	{
		private var timelineLabelContainer:ITimelineLabelContainer;
		protected var form:Form;
		protected var widthST:JNumberStepper;
		protected var acceptBtn:JButton;
		
		private static var instance:CreateLabelForm;
		private static var label:TimelineLabel;
		private static var track:Track;
		private var labelFactory:TimelineLabelFactory;
		
		public function CreateLabelForm(timelineLabelContainer:ITimelineLabelContainer = null, labelFactory:TimelineLabelFactory = null)
		{
			if (instance != null)
			{
				throw new Error("CreateLabelForm can only be accessed through CreateLabelForm.instance");
			}
			
			this.name = "CreateLabelForm";
			super.setTitleBar(null);
			this.timelineLabelContainer = timelineLabelContainer;
			setResizable(false);
			setBackground(new ASColor(0X0E1012, 0.3));
			setBackgroundChild(null);
			setBackgroundDecorator(new ColorDecorator(new ASColor(0x262F2B, 1), new ASColor(0xFFFFFF, 0.4)));
			//Settings.put("main.colors.dialogBackgroundColor", super.setBackground);
			setSize(new IntDimension(163, 34));
			setPreferredSize(new IntDimension(163, 34));
			setMaximumSize(new IntDimension(163, 34));
			setMinimumSize(new IntDimension(163, 34));
			widthST = new JNumberStepper(0, 0, 100);
			widthST.setPreferredWidth(70);
			acceptBtn = new JButton("Create label");
			acceptBtn.buttonMode = true;
			acceptBtn.setForeground(new ASColor(0xFFFFFF, 0.5));
			acceptBtn.setMaximumHeight(16);
			acceptBtn.addActionListener(acceptBtnHandler);
			
			form = new Form();
			form.setSizeWH(163, 32);
			form.setVisible(true);
			form.setAlignmentY(0.5);
			form.addLeftHoldRow(0, [0, 2]);
			form.addLeftHoldRow(0, widthST, 2, acceptBtn);
			
			setContentPane(form);
			
			addEventListener(PopupEvent.POPUP_OPENED, onPopupOpened);
			addEventListener(AWEvent.HIDDEN, onHidden);
			
			if (labelFactory == null)
			{
				labelFactory = new DefaultTimelineLabelFactory();
			}
			this.labelFactory = labelFactory;
			
			instance = this;
		
		}
		
		public function setTimelineLabelFactory(factory:TimelineLabelFactory):void
		{
			labelFactory = factory;
		}
		
		public function getTimelineLabelFactory():TimelineLabelFactory
		{
			return labelFactory;
		}
		
		public function setTimelineLabelContainer(container:ITimelineLabelContainer):void
		{
			timelineLabelContainer = container;
		}
		
		public function getTimelineLabelContainer():ITimelineLabelContainer
		{
			return timelineLabelContainer;
		}
		
		/*public static function init(timelineLabelContainer:ITimelineLabelContainer):CreateLabelForm {
		   if (!instance) {
		   instance = new CreateLabelForm(timelineLabelContainer);
		   }
		 }*/
		
		public static function getInstance():CreateLabelForm
		{
			//if (instance == null)
			//new CreateLabelForm();
			return instance;
		}
		
		public static function showForm(track:*, freeSpace:Number, x:Number = 0, y:Number = 0):void
		{
			/*CreateLabelForm.track = track;
			instance.setLocationXY(x, y);
			instance.setFreeSpace(freeSpace);
			instance.show();*/
		}
		
		private function onHidden(e:AWEvent):void
		{
			stage.removeEventListener(MouseEvent.CLICK, onClick);
			stage.removeEventListener(MouseEvent.MOUSE_DOWN, onClick);
			stage.removeEventListener(MouseEvent.RIGHT_CLICK, onClick);
		}
		
		private function onPopupOpened(e:Event):void
		{
			stage.addEventListener(MouseEvent.CLICK, onClick);
			stage.addEventListener(MouseEvent.MOUSE_DOWN, onClick);
			stage.addEventListener(MouseEvent.RIGHT_CLICK, onClick);
		}
		
		override public function show():void
		{
			super.show();
		}
		
		private function onClick(e:MouseEvent):void
		{
			if (!super.getBounds(stage).contains(e.stageX, e.stageY))
				hide();
		}
		
		public function setFreeSpace(freeSpace:Number):void
		{
			widthST.setMaximum(freeSpace);
			widthST.setValue(freeSpace);
		}
		
		private function acceptBtnHandler(e:AWEvent):void
		{
			var timelineLabel:TimelineLabel = labelFactory.createNewTimelineLabel();
			timelineLabel.setOwnerTrack(CreateLabelForm.track);
			var position:Number =super.getGlobalLocation().x/* super.getBounds(stage).x*/;
			//gtrace("position " + position);
			timelineLabelContainer.addTimelineLabel(timelineLabel, CreateLabelForm.track, position, widthST.getValue());
			super.hide();
		}
	
	}

}