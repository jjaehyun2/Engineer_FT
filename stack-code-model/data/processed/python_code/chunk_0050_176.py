/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.zzznake.Highscore.View
{
	import flash.text.AntiAliasType;
	import flash.text.StyleSheet;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	
	import flash.display.Sprite;
	
	import de.p3337.zzznake.Main.Zzznake;

	/**
	 * The HighscoreRow creates a row for the HighscoreRankingView with three TextFields as columns.
	 */
	public class HighscoreRow extends Sprite {
		private const _FIELD_HEIGHT:uint = Zzznake.ZZZNAKE_PADDING;
		
		private var styleSheet:StyleSheet;
		
		private var leftColumn:TextField;
		private var middleColumn:TextField;
		private var rightColumn:TextField;
		
		/**
		 * Creates a new HighscoreRow.
		 * 
		 * @param leftColumnText The position number of this ranking.
		 * @param middleColumnText The username.
		 * @param rightColumnText The score value.
		 * @param fontWeight The font weight. Default is "normal".
		 */
		public function HighscoreRow(leftColumnText:String, middleColumnText:String, rightColumnText:String, fontWeight:String = "normal") {
			super();
			
			mouseEnabled = false;
			mouseChildren = false;
			
			styleSheet = new StyleSheet();
			styleSheet.setStyle(".label", {
				color:'#000000',
				fontWeight:fontWeight,
				fontSize:'16',
				fontFamily:'Courier New'
			});
			
			addLeftColumn(leftColumnText);
			addMiddleColumn(middleColumnText);
			addRightColumn(rightColumnText);
		}
		
		private function addLeftColumn(text:String):void {
			leftColumn = new TextField();
			leftColumn.styleSheet = styleSheet;
			leftColumn.htmlText = "<span class='label'>" + text + "</span>";
			leftColumn.width = Zzznake.ZZZNAKE_PADDING;
			leftColumn.height = Zzznake.ZZZNAKE_PADDING;
			leftColumn.antiAliasType = AntiAliasType.ADVANCED;
			leftColumn.autoSize = TextFieldAutoSize.RIGHT;
			leftColumn.mouseEnabled = false;
			addChild(leftColumn);
		}
		
		private function addMiddleColumn(text:String):void {
			middleColumn = new TextField();
			middleColumn.styleSheet = styleSheet;
			middleColumn.htmlText = "<span class='label'>" + text + "</span>";
			middleColumn.width = ((Zzznake.ZZZNAKE_WIDTH - (Zzznake.ZZZNAKE_PADDING * 2)) / 2) - Zzznake.ZZZNAKE_PADDING;
			middleColumn.height = Zzznake.ZZZNAKE_PADDING;
			middleColumn.x = Zzznake.ZZZNAKE_PADDING;
			middleColumn.antiAliasType = AntiAliasType.ADVANCED;
			middleColumn.autoSize = TextFieldAutoSize.RIGHT;
			middleColumn.mouseEnabled = false;
			addChild(middleColumn);
		}
		
		private function addRightColumn(text:String):void {
			rightColumn = new TextField();
			rightColumn.styleSheet = styleSheet;
			rightColumn.htmlText = "<span class='label'>" + text + "</span>";
			rightColumn.width = (Zzznake.ZZZNAKE_WIDTH - (Zzznake.ZZZNAKE_PADDING * 2)) / 2;
			rightColumn.x = (Zzznake.ZZZNAKE_WIDTH - (Zzznake.ZZZNAKE_PADDING * 2)) / 2;
			rightColumn.height = FIELD_HEIGHT;
			rightColumn.antiAliasType = AntiAliasType.ADVANCED;
			rightColumn.autoSize = TextFieldAutoSize.RIGHT;
			rightColumn.mouseEnabled = false;
			addChild(rightColumn);
		}
		
		
		/**
		 * Updates the position value of this row.
		 * 
		 * @param text The new position.
		 */
		public function setLeftColumnText(text:String):void {
			leftColumn.htmlText = "<span class='label'>" + text + "</span>";
		}
		
		/**
		 * Updates the username of this row.
		 * 
		 * @param text The new username.
		 */
		public function setMiddleColumnText(text:String):void {
			middleColumn.htmlText = "<span class='label'>" + text + "</span>";
		}
		
		/**
		 * Updates the score value.
		 * 
		 * @param text The new score value.
		 */
		public function setRightColumnText(text:String):void {
			rightColumn.htmlText = "<span class='label'>" + text + "</span>";
		}

		public function get FIELD_HEIGHT():uint {
			return _FIELD_HEIGHT;
		}

	}
}