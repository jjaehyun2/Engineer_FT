/**
 * @author Peter Hansen
 * @copyright p3337.de All rights reserved.
 */
package de.p3337.straightouttaspace.Views.Screens.HUD
{
	import flash.display.Sprite;
	import flash.display.Stage;
	import flash.text.AntiAliasType;
	import flash.text.StyleSheet;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	
	public class HighscoreView extends Sprite
	{
		private var stageRef:Stage;
		
		private var myScoreField:TextField;
		private var highScoreField:TextField;
		
		public function HighscoreView(stageRef:Stage)
		{
			super();
			
			this.stageRef = stageRef;
			
			graphics.beginFill(0xFF0000, 0);
			graphics.drawRect(0, 0, this.stageRef.stageWidth, 50);
			graphics.endFill();
			
			var myScoreLabelSheet:StyleSheet = new StyleSheet();
			myScoreLabelSheet.setStyle(".label", {color:'#FFFFFF', fontWeight:'bold', fontSize:'16', fontFamily:'Courier New'});
			
			var myScoreLabel:TextField = new TextField();
			myScoreLabel.styleSheet = myScoreLabelSheet;
			myScoreLabel.htmlText = "<span class='label'>MY SCORE</span>";
			myScoreLabel.width = 25;
			myScoreLabel.height = 25;
			myScoreLabel.x = 5;
			myScoreLabel.antiAliasType = AntiAliasType.ADVANCED;
			myScoreLabel.autoSize = TextFieldAutoSize.LEFT;
			myScoreLabel.mouseEnabled = false;
			addChild(myScoreLabel);
			
			
			var myScoreFieldSheet:StyleSheet = new StyleSheet();
			myScoreFieldSheet.setStyle(".label", {color:'#FFFFFF', fontWeight:'normal', fontSize:'16', fontFamily:'Courier New'});
			
			myScoreField = new TextField();
			myScoreField.styleSheet = myScoreFieldSheet;
			myScoreField.htmlText = "<span class='label'>0</span>";
			myScoreField.width = 85;
			myScoreField.height = 25;
			myScoreField.x = 5;
			myScoreField.y = myScoreLabel.height;
			myScoreField.antiAliasType = AntiAliasType.ADVANCED;
			myScoreField.autoSize = TextFieldAutoSize.RIGHT;
			myScoreField.mouseEnabled = false;
			addChild(myScoreField);
			
			
			var styleSheet2:StyleSheet = new StyleSheet();
			styleSheet2.setStyle(".label", {color:'#00FFFF', fontWeight:'bold', fontSize:'20', fontFamily:'Courier New'});
			
			var highScoreLabel:TextField = new TextField();
			highScoreLabel.styleSheet = styleSheet2;
			highScoreLabel.htmlText = "<span class='label'>HIGH SCORE</span>";
			highScoreLabel.width = 25;
			highScoreLabel.height = 30;
			highScoreLabel.x = this.stageRef.stageWidth / 2 - highScoreLabel.width;
			highScoreLabel.antiAliasType = AntiAliasType.ADVANCED;
			highScoreLabel.autoSize = TextFieldAutoSize.CENTER;
			highScoreLabel.mouseEnabled = false;
			addChild(highScoreLabel);
			
			
			highScoreField = new TextField();
			highScoreField.styleSheet = myScoreFieldSheet;
			highScoreField.htmlText = "<span class='label'>0</span>";
			highScoreField.width = 95;
			highScoreField.height = 25;
			highScoreField.x = this.stageRef.stageWidth / 2 - highScoreField.width / 2;
			highScoreField.y = highScoreLabel.height;
			highScoreField.antiAliasType = AntiAliasType.ADVANCED;
			highScoreField.autoSize = TextFieldAutoSize.RIGHT;
			highScoreField.mouseEnabled = false;
			addChild(highScoreField);
		}
		
		public function updateMyScore(value:uint):void
		{
			this.myScoreField.htmlText = "<span class='label'>"+ value +"</span>";
		}
		
		public function updateHighScore(value:uint):void
		{
			this.highScoreField.htmlText = "<span class='label'>"+ value +"</span>";
		}
		
		public function destroy():void
		{
			this.stageRef = null;
			this.myScoreField = null;
			this.highScoreField = null;
			removeChildren();
		}
	}
}