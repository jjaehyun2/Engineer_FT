dynamic class TransitionController extends MovieClip{
	private static var _EventDispatchingInitialized = mx.events.EventDispatcher.initialize( TransitionController.prototype );
	function dispatchEvent() {}; 
	function addEventListener() {}; 
	function removeEventListener() {};
	private var TransRoot:MovieClip;
	private var TransMask:MovieClip;
	private var TransText:MovieClip;
	
	private var aryMaskX:Array;
	private var aryMaskRot:Array;
	
	
	function TransitionController(mc:MovieClip){ TransRoot = mc; }
	
	function init(obj:Object):Void{
		//TransRoot._visible = false;
		aryMaskRot = [0, -45];
		aryMaskX = [ obj.mX, obj.mX + (obj.mW)];
		TransMask = TransRoot.attachMovie("EmptyClip", "maskAnim_mc", 1, {_x:aryMaskX[0], _y:obj.mY, _rotation:aryMaskRot[0]}); // draw mask so it will fully cover page area
		
		
		var objShape:Object = {w:obj.mW, h:obj.mH, fillColor:0x0000cc, fillAlpha:10};
		//
		var objDraw = new misc.DrawShape();
			objDraw.doDraw(objShape, TransMask);
			
		// add wait message clip
		TransText = _global.MainObj.MainContainer.attachMovie("EmptyClip", "waitText_mc", 500, {_x:25, _y:Number(_global.MainObj.siteinfo.logoarea.y)+ (Number(_global.MainObj.siteinfo.logoarea.h)/2), _alpha:0});
			var objAddText = new misc.McAddText();
			var tfFormat:TextFormat = _global.MainObj.siteinfo.text_formats[1];
			var strContentText:String = "BUILDING...";
			
			var objTxt:Object = {txtW:250, txtName:"wait"+n,  strTextValue:strContentText, txtFormat:tfFormat, embedFont:true, bolWrapText:false, bolSelectable:false, strAutoSize:"left", bolHtmlText:false, bolBorder:false, bolGround:false};
			var tmpText = objAddText.addTextField(objTxt, TransText);
		//TransRoot._width = TransRoot._height = 0;
		//TransRoot._alpha = 0;	
	}
	
	function onMenuClick(obj:Object):Void{
		hidePage();// (!obj.first)? : onTransitionComplete(true)	
	}
	
	function hidePage():Void{
		trace("[TRANSITIONAREA] hidePage()");// rotate mask up and over to right
		TransRoot._visible = true;
		var tweenCtrl = new effects.ZigoTweener();
		var mcTarget = TransMask;
		//var numTarg =  (Stage.height > Stage.width)? Stage.height : Stage.width;
			//tweenCtrl.tween(TransRoot,["_width", "_height"], [numTarg, numTarg], .45, "Quad.easeIn", 0, {func:onTransitionComplete, scope:this});
			tweenCtrl.tween(mcTarget,["_x"], [aryMaskX[1]], .85, "Quad.easeOut", 0, {func:showMessage, scope:this}, 2);
	}
	
	function showMessage():Void{
		trace("[TRANSITIONAREA] showMessage()");
		var tweenCtrl = new effects.ZigoTweener();	
		tweenCtrl.tween(TransText,["_alpha"], [100], .25, "Quad.easeOut", 0, {func:onTransitionComplete, scope:this, args:[false]});
	}
	
	function showPage(obj):Void{
		trace("[TRANSITIONAREA] showPage()");
			TransRoot._visible = true;
		var tweenCtrl = new effects.ZigoTweener();
		var mcTarget = TransMask;//_global.MainObj.PageArea.ActiveScreen
			tweenCtrl.tween(mcTarget,["_x"], [aryMaskX[0]], 1, "Quad.easeOut", 0,{func:onTransitionComplete, scope:this, args:[true]},2);
			tweenCtrl.tween(TransText,["_alpha"], [0], .25, "Quad.easeIn", 0);
	}
	
	private function onTransitionComplete(a:Boolean){
		trace("[TRANSITIONAREA] onTransitionComplete(a="+a+"), alpha ot TransText="+TransText._alpha); 
		dispatchEvent({target:this, type:'onTransitionComplete', begin:a});
	}
	
	private function onResize(){
		TransRoot._y = (Stage.height/2) - (Number(_global.MAinObj.siteinfo.maincontainer.y)/2);	
	}
}