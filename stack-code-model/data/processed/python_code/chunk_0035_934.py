package devoron.components.multicontainers.timeline.components 
{
	import devoron.studio.modificators.timeline.ITimelineLabelContainer;
	import devoron.studio.modificators.timeline.TimelineLabel;
	import org.aswing.layout.BorderLayout;
	//import devoron.studio.core.Settings;
	import devoron.studio.core.resources.PackagesBackGroudDecorator;
	import devoron.studio.modificators.ModifiersPlugin;
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
	import org.aswing.JStepper;
	import org.aswing.JTextField;
	import org.aswing.JWindow;
	/**
	 * ...
	 * @author ...
	 */
	public class TrackSettingsForm extends JFrame
	{
		protected var form:Form;
		protected var nameTF:JTextField;
		protected var durationST:JStepper;
		protected var acceptBtn:JButton;
		
		private static var instance:TrackSettingsForm;
		private static var _track:Track;
		
		public function TrackSettingsForm() 
		{
			super.setTitleBar(null);
			getBackgroundChild().alpha = 0;
			resizable = false;
			setBackground(new ASColor(0X0E1012, 0.3));
			setBackgroundChild(null);
			setBackgroundDecorator(new PackagesBackGroudDecorator());
			//Settings.put("main.colors.dialogBackgroundColor", super.setBackground);
			setSize(new IntDimension(420, 38));
			setPreferredSize(new IntDimension(420, 38));
			setMaximumSize(new IntDimension(420, 38));
			setMinimumSize(new IntDimension(420, 38));
			
			nameTF = new JTextField();
			nameTF.setPreferredWidth(250);
			
			durationST = new JStepper(1000, 0, int.MAX_VALUE);
			durationST.setPreferredWidth(68);
			
			acceptBtn = new JButton("Accept");
			acceptBtn.setPreferredWidth(65);
			acceptBtn.buttonMode = true;
			acceptBtn.setForeground(new ASColor(0xFFFFFF, 0.5));
			acceptBtn.setMaximumHeight(16);
			acceptBtn.addActionListener(acceptBtnHandler);
			
			var panePanel:JPanel = new JPanel();
			panePanel.setLayout(new BorderLayout(10, 0));
			panePanel.setSizeWH(420, 38);
			setContentPane(panePanel);
			
			form = new Form();
			form.setSizeWH(420, 38);
			form.setVisible(true);
			form.setAlignmentY(0.5);
			panePanel.append(form);
			form.addLeftHoldRow(0, [0,2]);
			form.addLeftHoldRow(0, 6, nameTF, 5, durationST, 3, acceptBtn);
			
			addEventListener(PopupEvent.POPUP_OPENED, onPopupOpened);
			addEventListener(AWEvent.HIDDEN, onHidden);
		}
		
		public static function init():void {
			if (!instance) {
				instance = new TrackSettingsForm();
			}
		}
		
		public static function showForm(track:Track, x:Number = 0, y:Number = 0):void {
			TrackSettingsForm.track = track;
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
		
		override public function show():void 
		{
			super.show();
		}
		
		private function onClick(e:MouseEvent):void 
		{
			if (!super.getBounds(stage).contains(e.stageX, e.stageY))
			hide();
		}
		
		private function acceptBtnHandler(e:AWEvent):void 
		{
			// применить новое имя и длину
			_track.trackName = nameTF.getText();
			_track.duration = durationST.getValue();
			_track.dispatchEvent(new AWEvent(AWEvent.ACT));
			super.hide();
		}
		
		static public function get track():Track 
		{
			return _track;
		}
		
		static public function set track(value:Track):void 
		{
			_track = value;
			instance.nameTF.setText(value.trackName);
			instance.durationST.setValue(value.duration);
		}
		
	}

}