package
{
	import flash.events.Event;
	import flash.geom.Rectangle;
	
	import app.AppContainer;
	
	import org.hammerc.archer.ds.QuadTree;
	import org.hammerc.core.UIComponent;
	import org.hammerc.debug.Stats;
	
	[SWF(width=600, height=500, frameRate=60)]
	public class QuadTreeTest extends AppContainer
	{
		private var canvas:UIComponent = new UIComponent();
		
		private var spArr:Array = [];
		
		private var quad:QuadTree;
		
		public function QuadTreeTest()
		{
			super();
		}
		
		override protected function createChildren():void
		{
			super.createChildren();
			
			stage.addChild(new Stats());
			
			addElement(canvas);
			
			initSprites();
			
			quad = new QuadTree(new Rectangle(0,0,stage.stageWidth,stage.stageHeight), 3);
			
			addEventListener(Event.ENTER_FRAME, onEnterFrame);
		}
		
		private function initSprites():void
		{
			for(var i:int = 0 ; i< 500 ;  i++ )
			{
				var sp:RectSprite = new RectSprite(Math.random() * stage.stageWidth,Math.random() * stage.stageHeight,5+10 * Math.random(),5+10 * Math.random(),Math.random()*4-2,Math.random()*4-2);
				spArr.push(sp)
				this.canvas.addChild(sp);
			}
		}
		
		private function onEnterFrame(event:Event):void
		{
//			arrayTest();
			qtTest();
		}
		
		private function arrayTest():void
		{
			for each(var a:RectSprite in this.spArr)
			{
				a.update();
				for each (var i:RectSprite in this.spArr)
				{
					if(a==i)continue;
					if(a.isCollid && i.isCollid)continue
					if(a.hitTestObject( i))
					{ 
						if(!a.isCollid)
						{
							a.collid(true)
						}
						if(!i.isCollid)
						{
							i.collid(true);
						}
					}
				}
			}
		}
		
		private function qtTest():void
		{
			this.quad.clear();
			for each ( var s:RectSprite in this.spArr)
			{
				s.update();
				quad.insert(s);
			}
			for each(var a:RectSprite in this.spArr)
			{
				var arr:Array = this.quad.retrieve(a);
				for each (var i:RectSprite in arr)
				{
					if(a==i)continue;
					if(a.isCollid && i.isCollid)continue;
					if(a.hitTestObject( i))
					{
						a.collid(true);
						i.collid(true);
					}
				}
			}
		}
	}
}

import flash.display.Sprite;

class RectSprite extends Sprite
{
	private var _vx:Number;
	private var _vy:Number;
	private var _width:Number
	private var _height:Number
	public function RectSprite(px:Number,py:Number,p_width:Number,p_height:Number,p_vx:Number,p_vy:Number)
	{
		super();
		this.mouseChildren = this.mouseEnabled = false
		this._vx = p_vx;
		this._vy = p_vy;
		this.x = px
		this.y = py
		
		this.graphics.beginFill(0xffff0000)
		this.graphics.drawRect(0,0,p_width,p_height);
		this.graphics.endFill();
		this._width = p_width
		this._height = p_height
	}
	public var isCollid:Boolean = false
	public function update():void
	{
		if(this.x > stage.stageWidth)this.x = 0
		if(this.x<0)this.x = stage.stageWidth;
		if(this.y > stage.stageHeight)this.y = 0
		if(this.y<0)this.y = stage.stageHeight;
		this.x+=this._vx
		this.y+=this._vy
		
		this.collid(false)
	}
	
	public function collid(p:Boolean):void
	{
		this.isCollid = p
		
		if( p){
			this.graphics.clear()
			this.graphics.beginFill(0xff0000ff)
			this.graphics.drawRect(0,0,this._width,this._height);
			this.graphics.endFill(); 
		}else
		{
			this.graphics.clear()
			this.graphics.beginFill(0xffff0000)
			this.graphics.drawRect(0,0,this._width,this._height);
			this.graphics.endFill();
		}
	}
	
}