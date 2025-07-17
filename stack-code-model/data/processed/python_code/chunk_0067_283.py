/**Created by the LayaAirIDE,do not modify.*/
package ui.gameCommon.shortCutChat {
	import laya.ui.*;
	import laya.display.*; 

	public class ChatPageUI extends View {
		public var touchhide:Box;
		public var chatList:List;
		public var face1:Image;
		public var face2:Image;
		public var face3:Image;
		public var face4:Image;
		public var face5:Image;
		public var face6:Image;
		public var face7:Image;
		public var face8:Image;
		public var face9:Image;
		public var face10:Image;
		public var face11:Image;
		public var face12:Image;
		public var face13:Image;
		public var face14:Image;
		public var face15:Image;
		public var face16:Image;

		public static var uiView:Object =/*[STATIC SAFE]*/{"type":"View","props":{"width":1038,"height":640},"child":[{"type":"Box","props":{"y":0,"x":0,"var":"touchhide","mouseThrough":true,"alpha":0},"child":[{"type":"Rect","props":{"y":0,"x":0,"width":1038,"lineWidth":0,"height":640,"fillColor":"#ff0000"}}]},{"type":"Image","props":{"y":85,"x":71,"width":905,"skin":"common/gameBg.png","sizeGrid":"34,32,34,34","height":470}},{"type":"List","props":{"y":119,"x":487,"width":472,"var":"chatList","height":402}},{"type":"Image","props":{"y":101,"x":475,"width":435,"skin":"common/fenge.png","rotation":90}},{"type":"Image","props":{"y":101,"x":79,"var":"face1","skin":"faceexpress/face01.png"}},{"type":"Image","props":{"y":101,"x":176,"var":"face2","skin":"faceexpress/face02.png"}},{"type":"Image","props":{"y":101,"x":273,"var":"face3","skin":"faceexpress/face03.png"}},{"type":"Image","props":{"y":101,"x":370,"var":"face4","skin":"faceexpress/face04.png"}},{"type":"Image","props":{"y":212,"x":79,"var":"face5","skin":"faceexpress/face05.png"}},{"type":"Image","props":{"y":212,"x":176,"var":"face6","skin":"faceexpress/face06.png"}},{"type":"Image","props":{"y":212,"x":273,"var":"face7","skin":"faceexpress/face07.png"}},{"type":"Image","props":{"y":212,"x":370,"var":"face8","skin":"faceexpress/face08.png"}},{"type":"Image","props":{"y":322,"x":79,"var":"face9","skin":"faceexpress/face09.png"}},{"type":"Image","props":{"y":322,"x":176,"var":"face10","skin":"faceexpress/face10.png"}},{"type":"Image","props":{"y":322,"x":273,"var":"face11","skin":"faceexpress/face11.png"}},{"type":"Image","props":{"y":322,"x":370,"var":"face12","skin":"faceexpress/face12.png"}},{"type":"Image","props":{"y":433,"x":78,"var":"face13","skin":"faceexpress/face13.png"}},{"type":"Image","props":{"y":433,"x":175,"var":"face14","skin":"faceexpress/face14.png"}},{"type":"Image","props":{"y":433,"x":272,"var":"face15","skin":"faceexpress/face15.png"}},{"type":"Image","props":{"y":433,"x":369,"var":"face16","skin":"faceexpress/face16.png"}}]};
		override protected function createChildren():void {
			super.createChildren();
			createView(uiView);

		}

	}
}