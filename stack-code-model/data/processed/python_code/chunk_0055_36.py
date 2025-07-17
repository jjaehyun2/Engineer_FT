package MitchMovie 
{
	import flash.display.*;
	import flash.events.*;
	import flash.geom.*;
	import flash.ui.MouseCursor;
	import flash.ui.Mouse;
	import gfw.Interface.IByteArrayAssetProvider;
	import mx.core.UIComponent;
	import flash.utils.ByteArray;
	import gfw.graphic.NetStreamLoader;
	import mx.collections.*;
	import spark.utils.TextFlowUtil;
	import spark.components.RichText;
	import gfw.core.GameObject;
	import gfw.core.Game;
	import gfw.core.GameObjectManager
	import gfw.core.Button;
	import gfw.core.Level;
	import gfw.components.TextWindow;
	import gfw.core.ToggleButton;
	import animation.MoveThis;
	import gfw.graphic.GraphicsResource;
	/**
	 * ...
	 * @author jk
	 */

	public class MitchLevel extends Level implements IByteArrayAssetProvider
	{
		
	public function MitchLevel(Controller:Game) {
		super(Controller);
		this._videoAssets = new Array();
		this._videoIndex = 0;
		this._nextVideoIndex = 0;
	}
	private var _videoAssets:Array;
	private var _videoIndex:int;
	private var _nextVideoIndex:int;
	
	//this is called by Netstreamloader whenever the actual flv finishs
	public function GetNextAsset():ByteArray {
		var _prevVideo:int = _videoIndex;
		if (_videoAssets[_videoIndex].playOnce && _nextVideoIndex == _videoIndex) {
			//autoprogress to next
			_videoIndex = Math.min(_videoIndex + 1, _videoAssets.length - 1);
			_nextVideoIndex = _videoIndex;
		}
		else
		{
			_videoIndex = _nextVideoIndex;
		}
		if (_prevVideo == _videoIndex) {	//enable progress after anim played once
			m_BtRight.Enable(true);
		}
		return _videoAssets[_videoIndex].video as ByteArray;
	}
	private function InitPic( gr:GraphicsResource):Picture {
		var Obj:Picture = new Picture();
		Obj.Startup();
		Obj.SetGraphic(CreateButtonGraphic(gr));
		m_Controller.GetView().addElement(Obj);
		GameObjectManager.Instance.addBaseObject(Obj);
		return Obj;
	}
	
	override public function Startup():void {
		
		//load the embeded flvs
		var videoElement:Object = new Object(); 
		videoElement.video = new Resources.Idle1ClipData();
		videoElement.playOnce = false;
		_videoAssets.push(videoElement);
		
		videoElement = new Object(); 
		videoElement.video = new Resources.ApproachClipData();
		videoElement.playOnce = true;
		_videoAssets.push(videoElement);
		
		videoElement = new Object(); 
		videoElement.video = new Resources.PlugEnterClipData();
		videoElement.playOnce = true;
		_videoAssets.push(videoElement);
		
		videoElement = new Object(); 
		videoElement.video = new Resources.PlugPumpClipData();
		videoElement.playOnce = false;
		_videoAssets.push(videoElement);
				
		videoElement = new Object(); 
		videoElement.video = new Resources.DildoProbeClipData();
		videoElement.playOnce = false;
		_videoAssets.push(videoElement);
		
		videoElement = new Object(); 
		videoElement.video = new Resources.DildoPumpData();
		videoElement.playOnce = false;
		_videoAssets.push(videoElement);
		
		videoElement = new Object(); 
		videoElement.video = new Resources.PlugRemoveClipData();
		videoElement.playOnce = true;
		_videoAssets.push(videoElement);
		
		
		videoElement = new Object(); 
		videoElement.video = new Resources.PostClipData();
		videoElement.playOnce = false;
		_videoAssets.push(videoElement);
		
		//we will stream the flvs by using this:
		var ns:NetStreamLoader = new NetStreamLoader(this);
		
		var UIComp:UIComponent = new UIComponent();
		UIComp.addChild(ns.video);
		m_Controller.GetView().addElement(UIComp);		
		
		m_BtRight = new Button();
		m_BtRight.Startup();
		m_BtRight.SetGraphic(CreateButtonGraphic(Resources.BtArrowRightGraphics));
		m_BtRight.Enable(false);
		m_Controller.GetView().addElement(m_BtRight);
		m_BtRight.x = 10;
		m_BtRight.y = 10;
		m_BtRight.addEventListener(MouseEvent.CLICK, Right);
		m_BtRight.addEventListener(MouseEvent.MOUSE_OVER, changeCursor);
		m_BtRight.addEventListener(MouseEvent.MOUSE_OUT, resetCursor);
		
		m_BtRestart = new Button();
		m_BtRestart.Startup();
		m_BtRestart.SetGraphic(CreateButtonGraphic(Resources.BtArrowLeftGraphics));
		m_Controller.GetView().addElement(m_BtRestart);
		m_BtRestart.x = 10;
		m_BtRestart.y =  m_BtRight.y+ m_BtRight.height + 10;
		m_BtRestart.addEventListener(MouseEvent.CLICK, Restart);
		m_BtRestart.addEventListener(MouseEvent.MOUSE_OVER, changeCursor);
		m_BtRestart.addEventListener(MouseEvent.MOUSE_OUT, resetCursor);
		
		GameObjectManager.Instance.addBaseObject(m_BtRight);
		GameObjectManager.Instance.addBaseObject(m_BtRestart);	
		
			
		m_Controller.PauseGame(false);
		ns.connect();
	}
	private function CreateButtonGraphic(singleBitmap:GraphicsResource):GraphicsResource {
		var Gr:GraphicsResource = null; 
		var h:int = singleBitmap.drawRect.height;
		var w:int = singleBitmap.drawRect.width;
		var square:Shape = new Shape(); 
		
		var bitmap:BitmapData;
		bitmap = singleBitmap.bitmap.clone();
		bitmap.colorTransform(singleBitmap.bitmap.rect, new ColorTransform(1, 1, 1, 1, 100, 100, 100));
		square.graphics.beginBitmapFill(bitmap);
		square.graphics.drawRect(0, 0, w , h); 
		square.graphics.endFill();
		
		bitmap = singleBitmap.bitmap.clone();
		square.graphics.beginBitmapFill(bitmap);
		square.graphics.drawRect(w, 0, w , h); 
		square.graphics.endFill();
		
		bitmap = singleBitmap.bitmap.clone();
		//bitmap.colorTransform(singleBitmap.bitmap.rect, new ColorTransform(1, 1, 1, 1, 100, 100, 100));
		square.graphics.beginBitmapFill(bitmap);
		square.graphics.drawRect(w*2, 0, w , h); 
		square.graphics.endFill();
		
		bitmap = singleBitmap.bitmap.clone();
		//bitmap.colorTransform(singleBitmap.bitmap.rect, new ColorTransform(1, 1, 1, 1, 100, 100, 100));
		square.graphics.beginBitmapFill(bitmap);
		square.graphics.drawRect(w*3, 0, w , h); 
		square.graphics.endFill();
		
		Gr = new GraphicsResource(square,1,-1,new Rectangle(0,0,singleBitmap.drawRect.width,singleBitmap.drawRect.height));
		return Gr;
	}
	override public function Shutdown(): void {
		m_Controller.PauseGame(true);
		m_BtDown = null;
		m_BtLeft = null;
		m_BtRight = null;
		m_BtUp = null;
		m_BtRestart = null;
		GameObjectManager.Instance.shutdown();
	}
	override public function Tick(dt:Number):void {
		var cursor:IViewCursor= GameObjectManager.Instance.CreateCursor();
		while (cursor.current != null) {
			cursor.current.Tick(dt);
			cursor.moveNext();
		}
		cursor = null;
		GameObjectManager.Instance.enterFrame();
	}
	override public function IsLevelFinished():Boolean 	{
		return false;
	}
	private function changeCursor(e:MouseEvent)
	{
		var _target:Button = e.currentTarget as Button;
		if (_target != null && _target.IsEnabled())
		{
			Mouse.cursor = MouseCursor.BUTTON;
		}
		else
		{
			Mouse.cursor = MouseCursor.ARROW;
		}
	}
	 
	private function resetCursor(e:MouseEvent)
	{
		Mouse.cursor = MouseCursor.ARROW;
	}
	private function UpdateScore():void {
	}
	public function Up(e:Event):void {
		
	}
	public function Down(e:Event):void {

	}
	public function Left(e:Event):void {

	}
	public function Right(e:Event):void {
		m_BtRight.Enable(false);
		_nextVideoIndex = Math.min(_nextVideoIndex + 1, _videoAssets.length-1);
	}
	public function Restart(e:Event):void {
		_nextVideoIndex = 0;
		//Shutdown();
		//Startup();
	}
	private var m_Movie:MovieClip = null;
	private var m_BtLeft:Button = null;
	private var m_BtRight:Button = null;
	private var m_BtDown:Button = null;
	private var m_BtUp:Button = null;
	private var m_BtRestart:Button = null;
	
	protected var m_Idle:Picture = null;

	}
}