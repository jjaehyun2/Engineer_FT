package view {
	import config.ConfigUtil;
	import events.LayoutEvent;
	import flash.accessibility.Accessibility;
	import flash.display.Graphics;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.external.ExternalInterface;
	import flash.net.FileReference;
	import flash.system.System;
	import flash.system.fscommand;
	import flash.text.TextField;
	import model.YuanJian;
	import model.YuanJianManager;
	
	/**
	 * ...
	 * @author hongjie
	 */
	public final class KongZhiQu extends Sprite {
		
		public function KongZhiQu(width:int, height:int) {
			super();
			
			const g:Graphics = this.graphics;
			g.beginFill(0, 0);
			g.drawRect(0, 0, width, height);
			g.endFill();
			
			if (ExternalInterface.available) {
				ExternalInterface.addCallback("importXML", this._onImportXML);
				ExternalInterface.addCallback("deleteYuJian", this._onDeleteYuanJian);
				//ExternalInterface.addCallback("saveXML", this._onSaveXML);
				ExternalInterface.addCallback("exportXML", this._onExportXML);
			} else {
				var btn:Sprite = _createBtn('载入元件');
				btn.x = 20;
				btn.addEventListener(MouseEvent.CLICK, _onImportXML);
				addChild(btn);
				
				btn = _createBtn('剔除元件');
				btn.x = 100;
				btn.addEventListener(MouseEvent.CLICK, _onDeleteYuanJian);
				addChild(btn);
				
				btn = _createBtn('保存布局');
				btn.x = 180;
				btn.addEventListener(MouseEvent.CLICK, _onSaveXML);
				addChild(btn);
				
				btn = _createBtn('导出布局');
				btn.x = 260;
				btn.addEventListener(MouseEvent.CLICK, _onExportXML);
				addChild(btn);
			}
			
			btn = YuanJianQu.createBtn('垂直线槽', 0x5b9bd5);
			btn.x = 20;
			btn.y = (height - 30) >> 1;
			btn.addEventListener(MouseEvent.MOUSE_DOWN, _onStartDragVXianCao);
			addChild(btn);
			
			btn = YuanJianQu.createBtn('水平线槽', 0x5b9bd5);
			btn.x = 90;
			btn.y = (height - 30) >> 1;
			btn.addEventListener(MouseEvent.MOUSE_DOWN, _onStartDragHXianCao);
			addChild(btn);
			
			btn = YuanJianQu.createBtn('轨道', 0xffc000, 30);
			btn.x = 160;
			btn.y = (height - 30) >> 1;
			btn.addEventListener(MouseEvent.MOUSE_DOWN, _onStartDragGuiDao);
			addChild(btn);
			
			btn = YuanJianQu.createBtn('虚拟轨道', 0xffc000);
			btn.x = 200;
			btn.y = (height - 30) >> 1;
			btn.addEventListener(MouseEvent.MOUSE_DOWN, _onStartDragJiaGuiDao);
			addChild(btn);
			
			btn = YuanJianQu.createBtn('卡扣', 0x00b050, 30);
			btn.x = 270;
			btn.y = (height - 30) >> 1;
			btn.addEventListener(MouseEvent.MOUSE_DOWN, _onStartDragKaKou);
			addChild(btn);
		}
		
		private function _onStartDragVXianCao(e:MouseEvent):void {
			dispatchEvent(new LayoutEvent(LayoutEvent.START_TO_DTAG_V_XIAN_CAO));
		}
		
		private function _onStartDragHXianCao(e:MouseEvent):void {
			dispatchEvent(new LayoutEvent(LayoutEvent.START_TO_DTAG_H_XIAN_CAO));
		}
		
		private function _onStartDragGuiDao(e:MouseEvent):void {
			dispatchEvent(new LayoutEvent(LayoutEvent.START_TO_DTAG_GUI_DAO));
		}
		
		private function _onStartDragJiaGuiDao(e:MouseEvent):void {
			dispatchEvent(new LayoutEvent(LayoutEvent.START_TO_DTAG_JIA_GUI_DAO));
		}
		
		private function _onStartDragKaKou(e:MouseEvent):void {
			dispatchEvent(new LayoutEvent(LayoutEvent.START_TO_DTAG_KA_KOU));
		}
		
		private function _onDeleteYuanJian(e:MouseEvent = null):void {
			const xml:XML = ConfigUtil.instance.xml;
			const layoutXML:XML = ConfigUtil.instance.layoutXML;
			var yuanJian:YuanJian;
			if (layoutXML) {
				var itemName:String, itemCode:String;
				for each (var item:* in layoutXML.items.item) {
					itemName = item.@name;
					itemCode = item.@code;
					if (itemName == 'kaKou') {
						continue;
					}
					for each (var item1:* in xml.items.item) {
						if (itemName == item1.@name) {
							itemName = null;
							break;
						}
					}
					if (itemName) {
						yuanJian = YuanJianManager.instance.getYuanJian(itemName, itemCode);
						if (yuanJian.guiDao)
							yuanJian.guiDao.removeYuanJian(yuanJian);
						else
							yuanJian.parent.removeChild(yuanJian);
					}
					itemName = item.@topItem;
					itemCode = item.@topItemCode;
					for each (item1 in xml.items.item) {
						if (itemName == item1.@name) {
							itemName = null;
							break;
						}
					}
					if (itemName) {
						yuanJian = YuanJianManager.instance.getYuanJian(itemName, itemCode);
						if (yuanJian.guiDao)
							yuanJian.guiDao.removeYuanJian(yuanJian);
						else {
							if (yuanJian.parent) {
								yuanJian.parent.removeChild(yuanJian);
							}
						}
					}
					
					itemName = item.@bottomItem;
					itemCode = item.@bottomItemCode;
					for each (item1 in xml.items.item) {
						if (itemName == item1.@name) {
							itemName = null;
							break;
						}
					}
					if (itemName) {
						yuanJian = YuanJianManager.instance.getYuanJian(itemName, itemCode);
						if (yuanJian.guiDao)
							yuanJian.guiDao.removeYuanJian(yuanJian);
						else {
							if (yuanJian.parent) {
								yuanJian.parent.removeChild(yuanJian);
							}
						}
					}
				}
			}
		}
		
		private function _onSaveXML(e:MouseEvent = null):void {
			const xmlStr:String = _getXML();
			var fileRef:FileReference = new FileReference();
			fileRef.save(xmlStr, ConfigUtil.instance.layoutName + '.xml');
			fileRef.addEventListener(Event.COMPLETE, _onSaved);
		}
		
		private function _onSaved(e:Event):void {
			const fileRef:FileReference = e.currentTarget as FileReference;
			fileRef.removeEventListener(Event.COMPLETE, _onSaved);
			new Alert("保存布局成功！").show(this.stage);
		}
		
		//private function _onAddJiaGuiDao(e:MouseEvent):void {
		//dispatchEvent(new LayoutEvent(LayoutEvent.ADD_JIA_GUI_DAO));
		//}
		
		//private function _onAddGuiDao(e:MouseEvent):void {
		//dispatchEvent(new LayoutEvent(LayoutEvent.ADD_GUI_DAO));
		//}
		
		//private function _onAddXianCao(e:MouseEvent):void {
		//dispatchEvent(new LayoutEvent(LayoutEvent.ADD_XIAN_CAO));
		//}
		
		private function _onExportXML(e:MouseEvent = null):String {
			const xmlStr:String = _getXML();
			return xmlStr;
			//System.setClipboard(xmlStr);
		
			//var fileRef:FileReference = new FileReference();
			//fileRef.save(xmlStr, '.xml');
			//fileRef.addEventListener(Event.COMPLETE, _onExported);
		
			//fscommand(
		}
		
		private function _onExported(e:Event):void {
			const fileRef:FileReference = e.currentTarget as FileReference;
			fileRef.removeEventListener(Event.COMPLETE, _onExported);
			ConfigUtil.instance.layoutName = fileRef.name.split('.')[0];
			new Alert("导出布局成功！").show(this.stage);
		}
		
		private function _getXML():String {
			var bujuQu:BuJuQu = Main.mainScene.buJuQu;
			var xmlStr:String = '<?xml version="1.0" encoding="UTF-8"?>\n<data>\n\t<layout>\n';
			xmlStr += bujuQu.exportXianCao() + bujuQu.exportGuiDao() + '\n\t</layout>';
			xmlStr += '\n\t<items>' + bujuQu.exportYuanJian() + '\n\t</items>';
			xmlStr += '\n</data>';
			return xmlStr;
		}
		
		private function _onImportXML(e:MouseEvent = null):void {
			ConfigUtil.instance.addEventListener(LayoutEvent.IMPORT_XML_OK, _onReset);
			this.dispatchEvent(new LayoutEvent(LayoutEvent.IMPORT_XML));
		}
		
		private function _onReset(evt:LayoutEvent):void {
			// 检测一下在布局区是否有需要被剔除的元件
			if (_hasYuanJianNeededToBeDeleted()) {
				new Alert("检测到可剔除元件！").show(this.stage);
			}
			//new AlertPanel("sdfdsfds").show(this.stage);
		}
		
		private function _hasYuanJianNeededToBeDeleted():Boolean {
			var result:Boolean = false;
			const xml:XML = ConfigUtil.instance.xml;
			const layoutXML:XML = ConfigUtil.instance.layoutXML;
			if (layoutXML) {
				var itemName:String, itemCode:String;
				for each (var item:* in layoutXML.items.item) {
					itemName = item.@name;
					itemCode = item.@code;
					if (itemName == 'kaKou') {
						continue;
					}
					for each (var item1:* in xml.items.item) {
						if (itemName == item1.@name) {
							itemName = null;
							break;
						}
					}
					if (itemName) {
						result = true;
						YuanJianManager.instance.getYuanJian(itemName, itemCode).isRedundant = true;
					}
					itemName = item.@topItem;
					itemCode = item.@topItemCode;
					for each (item1 in xml.items.item) {
						if (itemName == item1.@name) {
							itemName = null;
							break;
						}
					}
					if (itemName) {
						result = true;
						YuanJianManager.instance.getYuanJian(itemName, itemCode).isRedundant = true;
					}
					
					itemName = item.@bottomItem;
					itemCode = item.@bottomItemCode;
					for each (item1 in xml.items.item) {
						if (itemName == item1.@name) {
							itemName = null;
							break;
						}
					}
					if (itemName) {
						result = true;
						YuanJianManager.instance.getYuanJian(itemName, itemCode).isRedundant = true;
					}
				}
			}
			return result;
		}
		
		private function _createBtn(name:String, bgColor:int = 0x9dc3e6, w:int = 60):Sprite {
			var btn:Sprite = new Sprite();
			const g:Graphics = btn.graphics;
			g.beginFill(bgColor);
			g.drawRect(0, 0, w, 30);
			g.endFill();
			var tf:TextField = new TextField();
			tf.mouseEnabled = false;
			tf.text = name;
			tf.textColor = 0xffffff;
			tf.x = (w - tf.textWidth) >> 1;
			tf.y = (30 - tf.textHeight) >> 1;
			tf.width = w;
			tf.height = 30;
			btn.addChild(tf);
			return btn;
		}
	
	}

}