package layer.popup {
	import layer.popup.common.AlertBox;
	import com.sibirjak.asdpc.button.Button;
	import com.sibirjak.asdpc.button.ButtonEvent;
	import org.as3commons.ui.layer.PopUpManager;
	import org.as3commons.ui.layout.shortcut.hgroup;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;

	public class MultiplePopUps extends Sprite {
		private var _popUpManager : PopUpManager;
		private var _addButton : Button;
		private var _removeButton : Button;
		private var _alertId : uint;
		private var _startPosition : uint = 20;

		public function MultiplePopUps() {
			addEventListener(Event.ADDED_TO_STAGE, init);
		}

		private function init(event : Event) : void {
			removeEventListener(Event.ADDED_TO_STAGE, init);
			
			var container : Sprite = stage.addChild(new Sprite()) as Sprite;
			_popUpManager = new PopUpManager(container);

			_addButton = new Button();
			_addButton.setSize(50, 20);
			_addButton.label = "add";
			_addButton.addEventListener(ButtonEvent.CLICK, addHandler);

			_removeButton = new Button();
			_removeButton.setSize(60, 20);
			_removeButton.enabled = false;
			_removeButton.label = "remove";
			_removeButton.addEventListener(ButtonEvent.CLICK, removeHandler);

			hgroup(
				"gap", 6,
				_addButton,
				_removeButton
			).layout(this);
			
			addPopUp();
			addPopUp();
		}
		
		private function addHandler(event : ButtonEvent = null) : void {
			addPopUp();
		}

		private function removeHandler(event : ButtonEvent) : void {
			removePopUp(_popUpManager.popUpOnTop as AlertBox);
		}

		private function closeCallback(alert : AlertBox, event : String) : void {
			removePopUp(alert);
		}

		private function alertClickHandler(event : MouseEvent) : void {
			_popUpManager.bringToFront(event.currentTarget as AlertBox);
		}
		
		private function addPopUp() : void {
			_startPosition += 30;
			if (_startPosition > 140) _startPosition = 50;

			var alert : AlertBox = new AlertBox(
				"Popup " + ++_alertId,
				"This is a simple popup window. Close this window by clicking the close button or the remove button of the outher application.",
				[null, null, "Close"],
				closeCallback
			);

			alert.x = alert.y = _startPosition;
			alert.addEventListener(MouseEvent.MOUSE_DOWN, alertClickHandler);
			_popUpManager.createPopUp(alert);
			enableButtons();
		}

		private function removePopUp(alert : AlertBox) : void {
			alert.removeEventListener(MouseEvent.MOUSE_DOWN, alertClickHandler);
			_popUpManager.removePopUp(alert);
			enableButtons();
		}

		private function enableButtons() : void {
			_addButton.enabled = _popUpManager.numPopUps < 4; // max 4
			_removeButton.enabled = _popUpManager.numPopUps > 0;
		}
	}
}