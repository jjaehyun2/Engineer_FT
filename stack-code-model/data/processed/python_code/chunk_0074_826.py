package views {
	import starling.display.Image;
	import starling.display.Quad;
	import starling.display.Sprite;
	import starling.text.TextField;
	import starling.utils.Align;
	import starling.utils.deg2rad;

	public class CircularLoader extends Sprite {
		private var mskR:Quad;

		private var mskL:Quad;
		private var lbl:TextField;

		private var imgBG:Image;
		public function CircularLoader() {
			super();
			var imgR:Image = new Image(Assets.getAtlas().getTexture("semi-circle"));
			var imgL:Image = new Image(Assets.getAtlas().getTexture("semi-circle"));
			imgBG = new Image(Assets.getAtlas().getTexture("semi-circle-bg2"));
			var w:int = imgR.width;
			
			lbl = new TextField(90,32,"");
			lbl.format.setTo("Fira Sans Semi-Bold 13",13);
			lbl.format.horizontalAlign = Align.CENTER;
			lbl.format.color = 0xD8D8D8;
			
			lbl.batchable = false;
			lbl.touchable = false;
			lbl.x = -w;
			lbl.y = 28;
			
			mskR = new Quad(w,w*2,0x000000);
			mskL = new Quad(w,w*2,0x000000);
			mskL.y = mskR.y = mskL.pivotY = mskR.pivotX = mskR.pivotY = mskR.pivotX = w;
			imgBG.touchable = false;
			imgBG.x = -w;
			imgBG.y = 0;
			imgL.scaleX = mskL.scaleX = -1;
			
			//var fltr:ColorMatrixFilter = new ColorMatrixFilter();
			//fltr.tint(0xFFFFFF);
			//imgR.filter = fltr;
			//imgL.filter = fltr;
			//imgL.alpha = imgR.alpha = 0.4;
			imgL.touchable = imgR.touchable = false;
			
			imgR.mask = mskR;
			imgL.mask = mskL;
			
			addChild(imgBG);
			addChild(imgR);
			addChild(imgL);
			addChild(lbl);
		}
		public function reset():void {
			imgBG.visible = true;
			mskL.rotation = mskR.rotation = 0;
			lbl.text = "";
		}
		public function update(value:Number):void {//percent eg 0.01
			lbl.text = (value*100).toPrecision(3)+"%";
			if(value >= 1){
				mskL.rotation = deg2rad(180);
				mskR.rotation = deg2rad(180);
				lbl.text = "100%";
				
				imgBG.visible = false;
			}else if(value < 0.5){
				mskR.rotation = deg2rad(360*value);
			}else{
				mskL.rotation = deg2rad(-(360*(value-0.5)));
				mskR.rotation = deg2rad(180);
			}
		}
		
	}
}