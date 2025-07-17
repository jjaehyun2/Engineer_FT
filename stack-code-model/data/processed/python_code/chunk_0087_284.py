package com.lowoui_as
{
	import com.greensock.easing.*;
	import com.lowoui_as.Global;
	import com.lowoui_as.component.LoaderSWF;
	import com.lowoui_as.config.ConfigAsset;
	import com.lowoui_as.core.UIDialog;
	import flash.display.MovieClip;
	import flash.display.Sprite;

	public class WidgetManager extends Sprite
	{
		private static var _ins:WidgetManager = null;

		public static function get ins():WidgetManager {
			if (_ins == null)
				_ins = new WidgetManager();

			return _ins;
		}

		public static var container:Object = null;
		public static var widgetsArr:Array = [];

		private var yesnoDialog:LoaderSWF = null;
		private var yesDialog:LoaderSWF = null;
		private var noticeDialog:LoaderSWF = null;

		public function WidgetManager() {}

		public function loadWidgets(arr:Array) : void
		{
			for (var i:int = 0; i < arr.length; i++)
			{ LoadWidget(arr[i][0], arr[i][1]); }
		}

		public function SceneMovieOut(sName:String):void
		{
			for (var i:int = 0; i < widgetsArr.length; i++)
			{
				if (widgetsArr[i].visible && widgetsArr[i].contentCon.beMovieView)
				{ widgetsArr[i].contentCon.closeView(); }
			}
		}

		public function LoadWidget(wName:String,depth:int) : void
		{
			if (Global.hudManager != null)
				Global.hudManager.UpdateChatMsg("widget name:"+wName);

			for (var i:int = 0; i < widgetsArr.length; i++)
			{
				if (widgetsArr[i].name == wName)
				{
					trace("load widget exsit!");
					widgetsArr[i].contentCon.openView();

					return;
				}
			}

			var widgetCon:LoaderSWF = new LoaderSWF();
			widgetCon.name = wName;
			widgetCon.loadSWF(ConfigAsset.swfURL(wName));
			container.addChild(widgetCon);

			//set widget weight
			widgetCon.widgetWeight = depth;

			widgetsArr.push(widgetCon);
		}

		public function CloseWidget(wName:String) : void
		{
			if (widgetsArr.length == 0) { return; }

			for (var i:int = 0; i < widgetsArr.length; i++)
			{
				if (widgetsArr[i].name == wName)
				{
					widgetsArr[i].contentCon.closeView();
				}
			}
		}

		public function CloseCurrSceneWidgets()
		{
			if (widgetsArr.length == 0) { return; }

			for (var i:int = 0; i < widgetsArr.length; i++)
			{
				widgetsArr[i].contentCon.closeView();
			}
		}

		public function UnloadWidget(wName:String) : void
		{
			if (widgetsArr.length == 0) { return; }

			for (var i:int = 0; i < widgetsArr.length; i++)
			{
				if (widgetsArr[i].name == wName)
				{
					widgetsArr[i].unloadSWF();
					container.removeChild(widgetsArr[i]);
					widgetsArr[i] = null;

					widgetsArr.splice(i, 1);
				}
			}
		}

		public function UnloadAllWidget()
		{
			if (widgetsArr.length == 0) { return; }

			for (var i:int = 0; i < widgetsArr.length; i++)
			{
				widgetsArr[i].unloadSWF();

				container.removeChild(widgetsArr[i]);
				widgetsArr[i] = null;
			}
			widgetsArr = [];
		}

		public function SetWidgetVisible(wName:String,visible:Boolean) : void
		{
		}

		public function SetWidgetSize(wName:String, width:uint, height:uint) : void
		{
		}

		/**
		 * Dialog
		 */
		public function OpenDialogYesNo(title:String, info:String, yesCallFun:String, noCallFun:String) : void
		{
			UIDialog.dialogTitle     = title;
			UIDialog.dialogInfo      = info;
			UIDialog.dialogBtnYesFun = yesCallFun;
			UIDialog.dialogBtnNoFun  = noCallFun;

			openDialogToStage(yesnoDialog,"YesNoDialog");
		}

		public function OpenDialogYes(title:String, info:String, yesCallFun:String) : void
		{
			trace("yesCallFun:"+yesCallFun);
			UIDialog.dialogTitle     = title;
			UIDialog.dialogInfo      = info;
			UIDialog.dialogBtnYesFun = yesCallFun;

			openDialogToStage(yesDialog,"YesDialog");
		}

		public function OpenDialogNotice(title:String, info:String, time:Number) : void
		{
			UIDialog.dialogTitle        = title;
			UIDialog.dialogInfo         = info;
			UIDialog.dialogDurationTime = time;

			openDialogToStage(noticeDialog, "NoticeDialog");
		}

		public function CloseDialog(dialogName:String) : void
		{
			var dialog:Object = null;

			switch (dialogName)
			{
				case "YesNoDialog":
					dialog = yesnoDialog.contentCon["dialog"];
					break;
				case "YesDialog":
					dialog = yesDialog.contentCon["dialog"];
					break;
				case "NoticeDialog":
					dialog = yesDialog.contentCon["dialog"];
					break;
				default:
			}

			if(dialog != null)
				dialog.closeDialog();
		}

		private function openDialogToStage(dialogLoader:LoaderSWF, dialogLoaderName:String) : void
		{
			if (dialogLoader == null)
			{
				dialogLoader = new LoaderSWF();
				dialogLoader.name = dialogLoaderName;
				dialogLoader.loadSWF(ConfigAsset.swfURL(dialogLoaderName));
				container.addChild(dialogLoader);
			}
			else
			{
				dialogLoader.contentCon["dialog"].openAndUpdate();
			}
			//set dialog to max depth
			container.setChildIndex(dialogLoader, container.numChildren - 1);
		}

		public static function callFunction(wName:String,arr:Array/*fName:String,param1,param2...*/) : void
		{
			trace("callFunction" + arr[0]);

			var ff:String = arr[0];
			var _widget:Object = getWidgetByName(wName);
			if (_widget != null)
			{ _widget[ff](); }
		}

		/**
		 * when dialog pop up
		 */
		public static function inactiveWidgetView()
		{
			trace("open dialog and inactive view.");
			for (var i:int = 0; i < widgetsArr.length; i++)
			{
				if (widgetsArr[i].contentCon.TestCall != undefined)
				{ widgetsArr[i].contentCon.TestCall(); }

				if (widgetsArr[i].name!="ESCPanel" && widgetsArr[i].contentCon.isActiveState == true)
				{ widgetsArr[i].contentCon.inactiveView(); }
			}
		}

		public static function activeWidgetView()
		{
			trace("close dialog and active view.");
			for (var i:int = 0; i < widgetsArr.length; i++)
			{
				if (widgetsArr[i].name!="ESCPanel" && widgetsArr[i].contentCon.isActiveState == false)
				{ widgetsArr[i].contentCon.activeView(); }
			}
		}

		public static function activeWidget(wName:String):void
		{
			var _widget:Object = getWidgetByName(wName);
			if (_widget != null) { _widget.activeView(); }
		}

		public static function inactiveWidget(wName:String):void
		{
			var _widget:Object = getWidgetByName(wName);
			if (_widget != null) { _widget.inactiveView(); }
		}

		public static function getWidgetByName(wName:String):Object
		{
			for each(var obj:Object in widgetsArr)
			{
				if (obj.name == wName)
				{ return obj.contentCon; }
			}

			return null;
		}

		public static function getWidgetConByName(wName:String):Object
		{
			for each(var obj:Object in widgetsArr)
			{
				if (obj.name == wName)
				{ return obj; }
			}

			return null;
		}

		public static function checkWidgetDepth(wName:String):void
		{
		}

		public static function setToTheHighestDepth(objName:String):void
		{
			var obj:MovieClip = getWidgetConByName(objName) as MovieClip;
			if (obj != null) container.setChildIndex(obj, container.numChildren - 1);
		}
	}
}