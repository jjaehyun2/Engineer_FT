package  
{
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.events.IEventDispatcher;
	import flash.events.IOErrorEvent;
	import flash.events.MouseEvent;
	import flash.net.FileFilter;
	import flash.net.FileReference;
	/**
	 * 维吉尼亚文本加密
	 * @author qzd
	 */
	public class main extends MovieClip
	{
		var fr:FileReference;
		var act:String = "";
		var textTypeFilter:FileFilter = new FileFilter("Text Files (*.txt)", "*.txt");
		public function main() 
		{
			fr = new FileReference();
			key_t.restrict = "A-Z 0-9a-z";
			configureListeners(fr);
			openBtn.addEventListener(MouseEvent.CLICK, btnClick);
			saveBtn.addEventListener(MouseEvent.CLICK, btnClick);
			enBtn.addEventListener(MouseEvent.CLICK, btnClick);
			deBtn.addEventListener(MouseEvent.CLICK, btnClick);
			alertBox.visible = false;
		}
		private function configureListeners(dispatcher:IEventDispatcher):void {
            dispatcher.addEventListener(Event.COMPLETE, completeHandler);
            dispatcher.addEventListener(IOErrorEvent.IO_ERROR, ioErrorHandler);
			dispatcher.addEventListener(Event.SELECT, selectHandler);
        }
		private function ioErrorHandler(e:IOErrorEvent):void {
			switch(act) {
				case "load":
					showAlert("加载失败");
					break;
				case "save":
					showAlert("保存失败");
					break;
			}
		}
		private function selectHandler(e:Event) {
			switch(act) {
				case "load":
					fr.load();
					break;
				default:
					break;
			}
		}
		private function completeHandler(e:Event) {
			switch(act) {
				case "load":
					txt_t.text = String(fr.data);
					break;
				case "save":
					showAlert("保存成功");
					break;
				default:
					break;
			}
		}
		private function btnClick(e:MouseEvent):void {
			switch(e.target.name) {
				case "openBtn":
					openFile();
					break;
				case "saveBtn":
					saveFile();
					break;
				case "enBtn":
					encrypt();
					break;
				case "deBtn":
					decrypt();
					break;
				default:
					break;
			}
		}
		private function openFile() {
			fr.browse([textTypeFilter]);
			act = "load";
		}
		private function saveFile() {
			fr.save(txt_t.text, "pw.txt");
			act = "save";
		}
		private function encrypt() {
			var key:String = key_t.text;
			if (key.length > 0) {
				var keyIndex:int = 0;
				if (txt_t.text.length > 0) {
					var txt:String = txt_t.text;
					var enTxt:String = "";
					for (var i:int = 0; i < txt.length; i++) {
						enTxt += String.fromCharCode(txt.charCodeAt(i) + key.charCodeAt(keyIndex));
						keyIndex++;
						if (keyIndex == key.length) {
							keyIndex = 0;
						}
					}
					txt_t.text = enTxt;
				}else {
					showAlert("请先加载文档");
				}
			}else {
				showAlert("请输入口令");
			}
		}
		private function decrypt() {
			var key:String = key_t.text;
			if (key.length > 0) {
				var keyIndex:int = 0;
				if (txt_t.text.length > 0) {
					var deTxt:String = "";
					var txt:String = txt_t.text;
					for (var i:int = 0; i < txt.length; i++) {
						deTxt += String.fromCharCode(txt.charCodeAt(i) - key.charCodeAt(keyIndex));
						keyIndex++;
						if (keyIndex == key.length) {
							keyIndex = 0
						}
					}
					txt_t.text = deTxt;
				}else {
					showAlert("请先加载文档");
				}
			}else {
				showAlert("请输入口令");
			}
		}
		private function showAlert(msg:String) {
			alertBox.visible = true;
			alertBox.msg_t.text = msg;
			alertBox.closeBtn.addEventListener(MouseEvent.CLICK, hideAlert);
		}
		private function hideAlert(e:MouseEvent) {
			alertBox.visible = false;
			alertBox.closeBtn.removeEventListener(MouseEvent.CLICK, hideAlert);
		}
	}
}