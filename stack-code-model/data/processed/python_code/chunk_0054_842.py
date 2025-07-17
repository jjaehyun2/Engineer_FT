/**
 * Created by newkrok on 09/04/16.
 */
package ageofai.building.base
{
	import ageofai.building.view.BuildProgressBarView;
	import ageofai.unit.view.LifeBarView;
	import flash.display.DisplayObject;
	import flash.display.Sprite;
	
	
	public class BaseBuildingView extends Sprite
	{
		protected var _graphicUI:DisplayObject;
		public var _lifeBar:LifeBarView;
		public var _buildProgressBar:BuildProgressBarView;
		
		public function BaseBuildingView()
		{
		}
		
		protected function createUI(uiClass:Class):void
		{
			this._graphicUI = new uiClass;
			this.addChild(this._graphicUI);
		}
		
		protected function createLifeBar():void
		{
			this._lifeBar = new LifeBarView();
			this._lifeBar.width = this._graphicUI.width;
			
			this._lifeBar.drawProcessBar( Math.random());
			
			this.addChild(this._lifeBar);
			
			this._lifeBar.hide();
		}
		
		protected function createProgressBar():void
		{
			this._buildProgressBar = new BuildProgressBarView();
			this._buildProgressBar.width = 70;
			this._buildProgressBar.x = -5;
			this._buildProgressBar.y = -20;

			this._buildProgressBar.drawProcessBar(Math.random());
			
			this.addChild( this._buildProgressBar );
			
			this._buildProgressBar.hide();
		}
	}
}