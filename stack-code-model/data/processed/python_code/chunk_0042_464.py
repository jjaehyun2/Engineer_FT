package
{
	import flash.display.DisplayObject;
	import flash.display.Sprite;
	import flash.events.*;
	
	import org.openPyro.aurora.AuroraContainerSkin;
	import org.openPyro.controls.List;
	import org.openPyro.controls.ScrollBar;
	import org.openPyro.controls.events.ListEvent;
	import org.openPyro.core.*;
	import org.openPyro.effects.Effect;
	import org.openPyro.events.PyroEvent;
	import org.openPyro.examples.DimensionMarkerSkin;
	import org.openPyro.examples.HaloTrackSkin;
	import org.openPyro.examples.SimpleButtonSkin;
	import org.openPyro.layout.*;
	import org.openPyro.painters.FillPainter;
	import org.openPyro.painters.GradientFillPainter;
	import org.openPyro.utils.GlobalTimer;
	
	[SWF(frameRate="30", backgroundColor="#8899aa")]
	public class TestList extends Sprite
	{
		
		private var list:List;
		private var container:UIContainer;
		
		public function TestList()
		{
			stage.scaleMode = "noScale"
			stage.align = "TL"
			
			//testSimpleChildren()
			//testSimpleScroll()
			testListInLayout()
			
			stage.addEventListener(Event.RESIZE, onStageResize)
			var globalTimer:GlobalTimer = new GlobalTimer(stage);
			globalTimer.start()
			
			stage.addEventListener(MouseEvent.CLICK, onStageClick);
		}
		
		private function onStageClick(event:MouseEvent):void
		{
		}
		
		private function testSimpleScroll():void{
			
			container = new UIContainer();
			container.name = "rootContainer";
			container.addEventListener(PyroEvent.UPDATE_COMPLETE,onContainerUpdate);
			container.width = stage.stageWidth/3
			container.height = stage.stageHeight/3;
			addChild(container);
			container.backgroundPainter = new FillPainter(0xcccccc)
			container.skin = new AuroraContainerSkin();
			//createScrollBarFromStyle2();	
			
			
			container.x = 100
			container.y = 100;
			
			var spacer:UIControl = new UIControl();
			spacer.size(800,400)
			spacer.backgroundPainter = new FillPainter(0xff0000);
			container.addChild(spacer);
			
		}
		
		private var uic:UIControl
		private function testSimpleChildren():void{
			uic = new UIControl()
			uic.name = "uic1"
			uic.backgroundPainter = new FillPainter(0xcdcdcd);
			this.uic.width = stage.stageWidth/4;
			this.uic.height = stage.stageHeight/4;
			addChild(uic)
			
			
			uic.x = uic.y = 100;
			
			var uic2:UIControl = new UIControl()
			uic2.name = "uic2"
			uic2.backgroundPainter = new FillPainter(0x00ff00);
			uic2.percentUnusedWidth = 50
			uic2.percentUnusedHeight = 50;
			uic.addChild(uic2)
			
			uic.addEventListener(PyroEvent.UPDATE_COMPLETE, onContainerUpdate);
		}
		
		private var s1:UIControl
		private var s2:UIControl;
		private function testListInLayout():void
		{
			createList()
			createContainer();
			
			
			container.addChild(list);
			s1 = createShape(0xff0000);
			container.addChild(s1);
			//stage.addEventListener(MouseEvent.CLICK, onMouseClick);
			
			s2 = createShape(0x00ff00);
			s2.name = "green";
			container.addChild(s2);
			
			//container.validateSize()
			container.layout = new HLayout(0);
		}
		
		private function onMouseClick(event:Event):void
		{
			stage.removeEventListener(MouseEvent.CLICK, onMouseClick);
			var s1:UIControl = new UIControl()
			s1.backgroundPainter = new GradientFillPainter([0xff0000,0x0000ff])
			s1.width = container.width+100
			s1.height = container.height+100
			s1.name = "red"
			container.addChild(s1);
			
			stage.dispatchEvent(new Event(Event.RESIZE));
		}
			
		private function createContainer():void{
			container = new UIContainer();
			container.name = "rootContainer";
			container.addEventListener(PyroEvent.UPDATE_COMPLETE,onContainerUpdate);
			container.width = stage.stageWidth/3;
			container.height = stage.stageHeight/3;
			addChild(container);
			container.backgroundPainter = new FillPainter(0xcccccc)
			container.skin = new AuroraContainerSkin();
			//createScrollBarFromStyle2();	
			
			
			container.x = 100
			container.y = 100;
			
		
			
		}
		
		private function onContainerUpdate(event:PyroEvent):void
		{
//			trace("[container]"+container.height, container.measuredHeight)
			/*
			trace("Container w/h : "+container.width, container.height)
			if(list){
				trace("list w/h: ", list.width, list.height)
			}
			if(s1){
				trace("S1 w/h: ", s1.width, s1.height)
			}
			
			if(s2){
				trace("s2 w/h: ", s2.width, s2.height)
			}
			*/
			
		}
		
		private function createShape(color:uint):UIControl
		{
			var spacer:UIControl = new UIControl();
			spacer.size("60%","100%");
			spacer.skin = new DimensionMarkerSkin();
			spacer.backgroundPainter = new FillPainter(color);
			return spacer;
		}
		
		private function createList():List{
			list = new List();
			list.addEventListener(ListEvent.ITEM_CLICK, onListClick);
			list.width = 200
			list.percentUnusedHeight = 100;
			
			var rendererFactory:ClassFactory = new ClassFactory(Renderer);
			rendererFactory.properties = {width:500, height:30}
			list.itemRenderer = rendererFactory;
			list.dataProvider = ["a", "a", "a", "a", "e", "f", "c", "b", "a"];
			
			list.skin = new AuroraContainerSkin()
			return list;
		}
		
		private function onListClick(_e:ListEvent):void
		{
			//container.horizontalScrollBar.visible = false;
			//trace('list height: '+list.height, 'list measuredht: '+list.measuredHeight, 'hScrollBar y'+list.horizontalScrollBar.y)
            trace(List(_e.target).selectedIndex+", "+List(_e.target).selectedItem);
            Effect.on(DisplayObject(_e.target)).slideDown(1);
		}
		
		public function onStageResize(event:Event):void{
			//trace(container.width, container.height)
			if(uic){
				this.uic.width = stage.stageWidth/4;
				this.uic.height = stage.stageHeight/4;
			}
			if(!container) return;
			container.width = stage.stageWidth/3;
			container.height = stage.stageHeight/3;
		}
		
		private function createScrollBarFromStyle():void
		{
			/*var vSliderSkin:SliderSkin = new SliderSkin(new SimpleButtonSkin(), new HaloTrackSkin());
			var vScrollBarSkin:ScrollBarSkin = new ScrollBarSkin(vSliderSkin, new SimpleButtonSkin(0), new SimpleButtonSkin(0));
			
			var hSliderSkin:SliderSkin =  new SliderSkin(new SimpleButtonSkin(), new HaloTrackSkin(Math.PI/2));
			var hScrollBarSkin:ScrollBarSkin = new ScrollBarSkin(hSliderSkin, new SimpleButtonSkin(0), new SimpleButtonSkin(0));
			
			var listSkin:UIContainerSkin = new UIContainerSkin(vScrollBarSkin,hScrollBarSkin);
			
			list.skin = listSkin;
			*/
		}
		
		private function createScrollBarFromStyle2():void
		{
			/*var vSliderSkin:SliderSkin = new SliderSkin(new SimpleButtonSkin(), new HaloTrackSkin());
			var vScrollBarSkin:ScrollBarSkin = new ScrollBarSkin(vSliderSkin, new SimpleButtonSkin(0), new SimpleButtonSkin(0));
			
			var hScrubberSkin:SimpleButtonSkin = new SimpleButtonSkin()
			hScrubberSkin.name = "hScrubber"
			var hSliderSkin:SliderSkin =  new SliderSkin(hScrubberSkin, new HaloTrackSkin(Math.PI/2));
			var hScrollBarSkin:ScrollBarSkin = new ScrollBarSkin(hSliderSkin, new SimpleButtonSkin(0), new SimpleButtonSkin(0));
			
			var listSkin:UIContainerSkin = new UIContainerSkin(vScrollBarSkin,hScrollBarSkin);
			
			container.skin = listSkin;
			*/ 
		}
		
		private function createVScrollBar():ScrollBar{
			
			var verticalScrollBar:ScrollBar = new ScrollBar(Direction.VERTICAL);
			verticalScrollBar.width = 15;
			verticalScrollBar.height = 300;
			addChild(verticalScrollBar);
			
			verticalScrollBar.slider.trackSkin = new HaloTrackSkin();
			verticalScrollBar.slider.thumbSkin = new SimpleButtonSkin();
			verticalScrollBar.incrementButtonSkin = new SimpleButtonSkin()
			verticalScrollBar.decrementButtonSkin = new SimpleButtonSkin();
			return verticalScrollBar;
			
		}	
	}
}


import flash.display.Sprite;
import flash.display.Graphics;
import flash.geom.ColorTransform;
import org.openPyro.core.UIControl;
import flash.text.TextField;
import flash.events.MouseEvent;	
import org.openPyro.controls.listClasses.IListDataRenderer;
import org.openPyro.controls.listClasses.BaseListData;

internal class Renderer extends UIControl implements IListDataRenderer{
	
	private var txt:TextField;
    private var m_selected:Boolean;
    private var m_bld:BaseListData
	
	public function Renderer(){
		
		txt = new TextField()
		//txt.border=true;
		addChild(txt);
		txt.autoSize = "left";
		txt.wordWrap=true;
		txt.selectable=false;
		//this.addEventListener(MouseEvent.CLICK, onMouseClick)
		//this.height = 30;
	}
	
	
	private var addHt:Number = 0
	private function onMouseClick(event:MouseEvent):void{
		addHt = 100;
		this.invalidateSize();
	}
	
	public function set data(d:Object):void{
        _data = d;
		this.txt.text = String(d);
		invalidateSize();
	}
	
	private var _data:Object;
	public function set label(s:String):void{
		_data = s;
		this.txt.text = s;
		this.invalidateSize();
	}
	
	override public function measure():void{
		super.measure()
		
		//if(this.txt.text == "1"){
			//trace(this.txt.text + ':measuring height: '+ _measuredHeight);
		//}
		//this.invalidateDisplayList()
		//trace('[ ROOT set height ]'+_measuredHeight)
	}
	
	public function get data():Object
	{
		return _data;
	}
	
	override public function updateDisplayList(unscaledWidth:Number, unscaledHeight:Number):void{
		if(this.txt.text == "1"){
			//trace('updating dl: '+unscaledHeight);
		}
		super.updateDisplayList(unscaledWidth, unscaledHeight);
		
		txt.width = unscaledWidth-20
		txt.x = 10
		txt.y = 10
		txt.height = 20
		
		var gr:Graphics = this.graphics;
		gr.clear()
		gr.lineStyle(1, 0x6ab0f7)
		gr.beginFill(0xcccccc)
		gr.drawRect(0,0,unscaledWidth,unscaledHeight);
		gr.endFill();
	}

    public function  get selected():Boolean {
        return m_selected;
    }

    public function  set selected(_selected:Boolean):void {
        //var e:Error = new Error();
        //trace(e.getStackTrace());
        m_selected = _selected;
        if(m_selected) {
            this.transform.colorTransform = new ColorTransform(1.1, 1.1, 1.1);
        } else {
            this.transform.colorTransform = new ColorTransform(1.0, 1.0, 1.0);
        }
    }

    public function  set baseListData(_bld:BaseListData):void {
        m_bld = _bld;
    }
}