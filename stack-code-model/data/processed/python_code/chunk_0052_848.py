package devoron.components.multicontainers.timeline.components 
{
	import org.aswing.layout.BorderLayout;
	import devoron.studio.core.Settings;
	import devoron.studio.core.resources.PackagesBackGroudDecorator;
	import devoron.studio.modificators.ModifiersPlugin;
	import devoron.studio.modificators.timeline.ITimelineLabelContainer;
	import devoron.studio.modificators.timeline.TimelineLabel;
	import devoron.studio.modificators.timeline.Track;
	import flash.events.Event;
	import flash.events.FocusEvent;
	import flash.events.MouseEvent;
	import org.aswing.ASColor;
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
	public class RemoveLabelForm extends JFrame
	{
		private var timelineLabelContainer:ITimelineLabelContainer;
		protected var form:Form;
		protected var widthST:JNumberStepper;
		protected var removeBtn:JButton;
		
		private static var instance:RemoveLabelForm;
		private static var label:TimelineLabel;
		private static var track:Track;
		
		public function RemoveLabelForm(timelineLabelContainer:ITimelineLabelContainer) 
		{
			super.setTitleBar(null);
			this.timelineLabelContainer = timelineLabelContainer;
			getBackgroundChild().alpha = 0;
			resizable = false;
			setBackground(new ASColor(0X0E1012, 0.3));
			setBackgroundChild(null);
			setBackgroundDecorator(new PackagesBackGroudDecorator());
			//Settings.put("main.colors.dialogBackgroundColor", super.setBackground);
			setSize(new IntDimension(100, 34));
			setPreferredSize(new IntDimension(100, 34));
			setMaximumSize(new IntDimension(100, 34));
			setMinimumSize(new IntDimension(100, 34));
			removeBtn = new JButton("Remove label");
			removeBtn.buttonMode = true;
			removeBtn.setForeground(new ASColor(0xFFFFFF, 0.5));
			removeBtn.setMaximumHeight(16);
			removeBtn.addActionListener(removeBtnHandler);
			
			var panePanel:JPanel = new JPanel();
			panePanel.setLayout(new BorderLayout(10, 0));
			panePanel.setSizeWH(100, 32);
			setContentPane(panePanel);
			
			form = new Form();
			form.setSizeWH(100, 32);
			form.setVisible(true);
			form.setAlignmentY(0.5);
			panePanel.append(form);
			form.addLeftHoldRow(0, [0,2]);
			form.addLeftHoldRow(0, 4, removeBtn);
			
			addEventListener(PopupEvent.POPUP_OPENED, onPopupOpened);
			addEventListener(AWEvent.HIDDEN, onHidden);
		}
		
		public static function init(timelineLabelContainer:ITimelineLabelContainer):void {
			if (!instance) {
				instance = new RemoveLabelForm(timelineLabelContainer);
			}
		}
		
		public static function showForm(label:TimelineLabel, track:Track, x:Number = 0, y:Number = 0):void {
			RemoveLabelForm.label = label;
			RemoveLabelForm.track = track;
			instance.setLocationXY(x, y);
			instance.show();
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
		
		
		private function onClick(e:MouseEvent):void 
		{
			if (!super.getBounds(stage).contains(e.stageX, e.stageY))
			hide();
		}
		
		
		private function removeBtnHandler(e:AWEvent):void 
		{
			timelineLabelContainer.removeTimelineLabel(RemoveLabelForm.label, RemoveLabelForm.track);
			super.hide();
		}
		
	}

}