package com.illuzor.thegame.editor.panels {
	
	import com.bit101.components.Label;
	import com.bit101.components.PushButton;
	import com.bit101.components.Text;
	import flash.display.Sprite;
	
	/**
	 * ...
	 * @author illuzor // illuzor.com // illuzor@gmail.com
	 */
	public class SelectedItemPanel extends Sprite {
		
		private var yText:Text;
		private var xText:Text;
		public var removeButton:PushButton;
		public var applyCoordinatesBut:PushButton;
		
		public function SelectedItemPanel() {
			var title:Label = new Label(this, 10, 10, "SELECTED ITEM MENU");
			var xLabel:Label = new Label(this, 10, 30, "X:");
			var yLabel:Label = new Label(this, 10, 50, "Y:");
			
			xText = new Text(this, 30, 30);
			xText.textField.maxChars = 3;
			xText.textField.restrict = "0-9";
			xText.width = 30;
			xText.height = 18;
			
			yText = new Text(this, 30, 50);
			yText.textField.maxChars = 3;
			yText.textField.restrict = "0-9";
			yText.width = 30;
			yText.height = 18;
			
			applyCoordinatesBut = new PushButton(this, 70, 40, "APPLY");
			applyCoordinatesBut.width = 40;
			
			removeButton = new PushButton(this, 10, 80, "REMOVE");
			removeButton.width = 50;
		}
		
		public function setText(xt:uint, yt:uint):void {
			xText.text = String(xt);
			yText.text = String(yt);
		}
		
		public function getText():Object {
			return { x:uint(xText.text), y:uint(yText.text) };
		}
		
	}
}