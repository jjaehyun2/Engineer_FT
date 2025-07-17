package com.github.knose1.utils.console {
	import flash.display.Sprite;
	import flash.text.TextField;
	import flash.text.TextFormat;
	
	/**
	 * Crée une zone de text
	 * @author Knose1
	 */
	public class Console extends Sprite {
		/**
		 * Liste contenant les zones de text dans l'ordre d'apparition
		 */
		
		private var _fieldList:Vector.<TextField> = new Vector.<TextField>();
		protected function get fieldList():Vector.<TextField> {
			return _fieldList;
		}
		
		
		
		private var _container:Sprite = new Sprite();
		public function get container():Sprite {
			return _container;
		}
		
		
		
		/**
		 * Hauteur de la ligne en px
		 */
		private var _lineHeight:Number;
		public function get lineHeight():Number {
			return _lineHeight;
		}
		
		public function set lineHeight(value:Number):void {
			_lineHeight = value;
		}
		
		
		
		/**
		 * Nombre max de ligne
		 */
		private var _textSize:uint = 12;
		public function get textSize():uint {
			return _textSize;
		}
		
		public function set textSize(value:uint):void {
			_textSize = value || 1;
		}
		
		
		
		/**
		 * Nombre max de ligne
		 */
		private var _maxLineCount:uint = 25;
		public function get maxLineCount():uint {
			return _maxLineCount;
		}
		
		public function set maxLineCount(value:uint):void {
			_maxLineCount = value;
		}
		
		
		
		/**
		 * Nombre max de charactère par ligne
		 */
		private var _maxCharByLine:uint = 100;
		
		public function get maxCharByLine():uint {
			return _maxCharByLine;
		}
		
		public function set maxCharByLine(value:uint):void {
			_maxCharByLine = value;
		}
		
		
		
		/**
		 * Constructeur de la classe
		 */
		public function Console() {
			super();
			
			//Initialise la taille de la ligne
			if (!lineHeight) {
				resetLineHeight();
			}
			
			addChild(container);
			
			container.scaleX = -1;
		}
		
		public function resetLineHeight():void {
			var lText:TextField = new TextField();
			lText.text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
			
			
			var lTextFormat:TextFormat = lText.getTextFormat();
			lTextFormat.size = textSize;
			lText.setTextFormat(lTextFormat);
			
			lineHeight = lText.textHeight;
		}
		
		/**
		 * Crée un log dans la console
		 * @return Retourne le textfield crée
		 */
		public function log(pText:String, pColor:Number = 0):void {
			
			var lCutIndex:int;
			var lText:String = "";
			do {
				(lCutIndex = pText.indexOf("\n") + 1) || (lCutIndex = pText.indexOf("\r") + 1) || (lCutIndex = maxCharByLine + 1);
				
				lCutIndex--;
				
				lCutIndex = Math.min(lCutIndex, pText.length)
				
				addLine(pText.slice(0, lCutIndex), pColor);
				
				pText = pText.slice(lCutIndex).replace("\n", "").replace("\r", ""); //on retire le 1er \n ou \r
			}
			while (pText.length != 0)
			
			var lContainer:Sprite = container;
		}
		
		/**
		 * Crée une ligne dans le container
		 * @param	pText
		 * @param	pColor
		 */
		protected function addLine(pText:String, pColor:Number = 0):void {
			var lText:TextField = new TextField();
			lText.textColor = pColor;
			lText.text = pText;
			
			var lTextFormat:TextFormat = lText.getTextFormat();
			lTextFormat.size = textSize;
			lText.setTextFormat(lTextFormat);
			
			lText.scaleX = -1;
			
			fieldList.unshift(lText);
			if (fieldList.length > maxLineCount) popLine();
			
			for (var i:int = fieldList.length - 1; i >= 0; i--) {
				fieldList[i].y = lineHeight * i;
			}
			
			lText.width = 10000;
			
			container.addChild(lText);
			
		}
		
		protected function popLine():void {
			var lTextField:TextField = fieldList.pop();
			container.removeChild(lTextField);
		}
		
	}
	
}