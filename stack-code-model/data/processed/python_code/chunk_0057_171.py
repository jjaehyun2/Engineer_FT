package TowerOfHanoi 
{
	import flash.display.*;
	import flash.events.*;
	import flash.geom.*;
	import gfw.physics.HitTester;
	import mx.collections.*;
	import spark.utils.TextFlowUtil;
	import spark.components.RichText;
	import gfw.core.GameObject;
	import gfw.core.Game;
	import gfw.core.GameObjectManager
	import gfw.core.Level;
	import gfw.core.Button;
	import animation.MoveThis;
	import gfw.graphic.GraphicsResource;
	import gfw.input.Input;
	/**
	 * ...
	 * @author jk
	 * enthält alle Level-Objekte und -zustände
	 */
	public class HanoiLevel extends Level
	{
		
	public function HanoiLevel(Controller:Game) {
		super(Controller);
	}
	override public function Startup():void {
		m_Tower1 = new Tower();
		m_Tower2 = new Tower();
		m_Tower3 = new Tower();
		m_MoveTower = m_Tower1;
		m_MoveBlock = null;
		m_Tower1.x = 200;
		m_Tower1.y = 350;
		m_Controller.GetView().addElement(m_Tower1);
		m_Tower1.Startup();
		m_Tower1.SetText("Source");
		m_Tower2.x = 350;
		m_Tower2.y = m_Tower1.y;
		m_Controller.GetView().addElement(m_Tower2);
		m_Tower2.Startup();
		m_Tower3.x = 500;
		m_Tower3.y = m_Tower1.y;
		m_Controller.GetView().addElement(m_Tower3);
		m_Tower3.Startup();
		m_Tower3.SetText("Destination");
		var block:Block;
		for (var i:int = m_MaxBlocks; i >= 1; i-- ) {
			block = new  Block();
			m_Controller.GetView().addElement(block);
			block.Startup();
			block.SetSize(i);
			m_MoveTower.PushBlockOnTower(block);
			GameObjectManager.Instance.addBaseObject(block);
		}

		m_BtUp = new Button();
		m_BtUp.Startup();
		m_BtUp.SetGraphic(CreateButtonGraphic(Resources.BtArrowUpGraphics));
		m_Controller.GetView().addElement(m_BtUp);
		m_BtUp.x = 10;
		m_BtUp.y = 10;
		m_BtUp.addEventListener(MouseEvent.CLICK, Up);
		
		m_BtDown = new Button();
		m_BtDown.Startup();
		m_BtDown.SetGraphic(CreateButtonGraphic(Resources.BtArrowDownGraphics));
		m_Controller.GetView().addElement(m_BtDown);
		m_BtDown.x = 10;
		m_BtDown.y = m_BtUp.y+ m_BtUp.height + 10;
		m_BtDown.addEventListener(MouseEvent.CLICK, Down);
		
		m_BtLeft = new Button();
		m_BtLeft.Startup();
		m_BtLeft.SetGraphic(CreateButtonGraphic(Resources.BtArrowLeftGraphics));
		m_Controller.GetView().addElement(m_BtLeft);
		m_BtLeft.x = 10;
		m_BtLeft.y = m_BtDown.y+ m_BtDown.height + 10;
		m_BtLeft.addEventListener(MouseEvent.CLICK, Left);
		
		m_BtRight = new Button();
		m_BtRight.Startup();
		m_BtRight.SetGraphic(CreateButtonGraphic(Resources.BtArrowRightGraphics));
		m_Controller.GetView().addElement(m_BtRight);
		m_BtRight.x = 10;
		m_BtRight.y =  m_BtLeft.y+ m_BtLeft.height + 10;
		m_BtRight.addEventListener(MouseEvent.CLICK, Right);
		
		m_BtRestart = new Button();
		m_BtRestart.Startup();
		m_BtRestart.SetGraphic(CreateButtonGraphic(Resources.BtRestartGraphics));
		m_Controller.GetView().addElement(m_BtRestart);
		m_BtRestart.x = 10;
		m_BtRestart.y =  m_BtRight.y+ m_BtRight.height + 10;
		m_BtRestart.addEventListener(MouseEvent.CLICK, Restart);
		
		m_Score = 0;
		m_ScoreText = new RichText();
		m_ScoreText.x = 10;
		m_ScoreText.y = m_BtRestart.y + m_BtRestart.height + 50;
		m_ScoreText.setStyle("fontSize", 14);
		m_Controller.GetView().addElement(m_ScoreText);
		
		GameObjectManager.Instance.addBaseObject(m_BtDown);
		GameObjectManager.Instance.addBaseObject(m_BtUp);
		GameObjectManager.Instance.addBaseObject(m_BtLeft);
		GameObjectManager.Instance.addBaseObject(m_BtRight);
		GameObjectManager.Instance.addBaseObject(m_BtRestart);
		GameObjectManager.Instance.addBaseObject(m_Tower1);
		GameObjectManager.Instance.addBaseObject(m_Tower2);
		GameObjectManager.Instance.addBaseObject(m_Tower3);
		
		UpdateBlocks();
		m_Controller.PauseGame(false);
	}
	private function CreateButtonGraphic(singleBitmap:GraphicsResource):GraphicsResource {
		var Gr:GraphicsResource = null; 
		var h:int = singleBitmap.drawRect.height;
		var w:int = singleBitmap.drawRect.width;
		var square:Shape = new Shape(); 
		
		var bitmap:BitmapData;
		bitmap = singleBitmap.bitmap.clone();
		//bitmap = new BitmapData(singleBitmap.bitmap.rect.width, singleBitmap.bitmap.rect.height, true, 0);
		//bitmap.copyPixels(singleBitmap.bitmap,singleBitmap.drawRect,new Point(0,0),singleBitmap.bitmapAlpha,new Point(0,0),true)
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
		m_MoveBlock = null;
		m_MoveTower = null;
		m_Tower1 = null;
		m_Tower2 = null;
		m_Tower3 = null;
		m_BtDown = null;
		m_BtLeft = null;
		m_BtRight = null;
		m_BtUp = null;
		m_BtRestart = null;
		GameObjectManager.Instance.shutdown();
		
		m_Controller.GetView().removeElement(m_ScoreText);
		m_ScoreText = null;
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
	override public function IsLevelFinished():Boolean 
	{
		if (m_Tower3.m_Blocks.length == m_MaxBlocks) return true;
		return false;
	}
	private function UpdateScore():void {
		var text:String = new String("<p><span fontWeight=\"bold\">Moves used: "+m_Score.toString()+"</span></p>");
		m_ScoreText.textFlow = TextFlowUtil.importFromString(text);
	}
	private function UpdateBlocks():void  {
		var block:Block;
		var tower:Tower;
		for (var k:int = 1; k <= 3; k++ ) {
			switch(k) {
				case 1: tower = m_Tower1;
				break;
				case 2: tower = m_Tower2;
				break;
				default: tower = m_Tower3;
				break;
			}
			for (var i:int = tower.m_Blocks.length ; i > 0; i-- ) {
				block = tower.m_Blocks[i - 1] as Block;
				block.x = tower.x+tower.width/2-block.width/2;
				block.y = tower.y- i*35;
			}
		}
		
		m_BtDown.Enable(CanPushBlockOnTower());
		m_BtUp.Enable(CanPopBlockFromTower());
		if (m_MoveBlock != null) {
			m_MoveBlock.x = m_MoveTower.x+m_MoveTower.width/2-m_MoveBlock.width/2;
		}
		m_Tower1.SelectAsTarget(m_MoveTower==m_Tower1);
		m_Tower2.SelectAsTarget(m_MoveTower==m_Tower2);
		m_Tower3.SelectAsTarget(m_MoveTower==m_Tower3);

	}
	private function CanPushBlockOnTower():Boolean {
		if (m_MoveBlock == null || m_MoveTower == null ) return false;
			
		return m_MoveTower.CanPushBlockOnTower(m_MoveBlock);
	}
	private function CanPopBlockFromTower():Boolean {
		if (m_MoveBlock != null || m_MoveTower == null ) return false;
			
		return m_MoveTower.CanPopBlockFromTower();
	}
	public function MouseDrag():void {
		if (Input.mousePressed ) {
			//??HitTester.realHitTest(m_Tower1,new Point(Input.mouseX,Input.mouseY));
		}
	}
	public function Up(e:Event):void {
		if (CanPopBlockFromTower()) {
			m_MoveBlock = m_MoveTower.PopBlockFromTower();
			m_MoveBlock.y = 20;
			UpdateBlocks();
			m_Controller.GetSoundMngr().PlaySound("HIT", false, 1, 0, 1.0);
		}
	}
	public function Down(e:Event):void {
		if (CanPushBlockOnTower()) {
			m_MoveTower.PushBlockOnTower(m_MoveBlock);
			m_MoveBlock = null;
			m_Score++;
			m_Controller.GetSoundMngr().PlaySound("BUMP", false, 1, 0, 1.0);
			UpdateScore();
			UpdateBlocks();
		}
	}
	public function Left(e:Event):void {
		if (m_MoveTower == null) {
			m_MoveTower = m_Tower3;
		} else if(m_MoveTower== m_Tower1) {
			m_MoveTower = m_Tower1;
		} else if(m_MoveTower== m_Tower2) {
			m_MoveTower = m_Tower1;
		} else if(m_MoveTower== m_Tower3) {
			m_MoveTower = m_Tower2;
		}
		UpdateBlocks();
	}
	public function Right(e:Event):void {
		if (m_MoveTower == null) {
			m_MoveTower = m_Tower1;
		} else if(m_MoveTower== m_Tower3) {
			m_MoveTower = m_Tower3;
		} else if(m_MoveTower== m_Tower2) {
			m_MoveTower = m_Tower3;
		} else if(m_MoveTower== m_Tower1) {
			m_MoveTower = m_Tower2;
		}
		UpdateBlocks();
	}
	public function Restart(e:Event):void {
		Shutdown();
		Startup();
	}
	public function GetScore():int {
		return m_Score;
	}
	private function Start(e:Event):void {
		//MoveThis.startTween(bt, { x:+30, y: + 30 }, 30,{easing:"Reverse.easeInOut", loop:true }); 
		//bt2.Enable(false);
	}
	
	private var m_MoveBlock:Block = null;
	private var m_MoveTower:Tower = null;
	private var m_Tower1:Tower = null;
	private var m_Tower2:Tower = null;
	private var m_Tower3:Tower = null;
	private var m_BtLeft:Button = null;
	private var m_BtRight:Button = null;
	private var m_BtDown:Button = null;
	private var m_BtUp:Button = null;
	private var m_BtRestart:Button = null;
	
	private var m_ScoreText:RichText = null;
	private var m_Score:int = 0;
	private var m_MaxBlocks:int = 5;
	}
}