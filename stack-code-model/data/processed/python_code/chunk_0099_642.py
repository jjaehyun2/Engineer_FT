package com.core 
{
		 import as3isolib.core.ClassFactory;
        import as3isolib.core.IFactory;
		 import as3isolib.display.IsoView;
         import as3isolib.display.renderers.DefaultShadowRenderer;
		 import as3isolib.display.scene.IsoGridSprite;
		 import as3isolib.geom.IsoMath;
		 import as3isolib.geom.Pt;
		 import com.baseoneonline.flash.astar.AStar;
		 import com.baseoneonline.flash.astar.AStarNode;
		 import com.baseoneonline.flash.astar.IAStarSearchable;
		 import eDpLib.events.ProxyEvent;
		 import flash.events.MouseEvent;
		 import gs.TweenLite;

        import as3isolib.display.IsoSprite;
        import as3isolib.display.primitive.IsoBox;
		import as3isolib.display.renderers.DefaultShadowRenderer;
        import as3isolib.display.scene.IsoGrid;
        import as3isolib.display.scene.IsoScene;
        
        import flash.display.Loader;
        import flash.display.Sprite;
        import flash.events.Event;
        import flash.net.URLRequest;
        
        public class IsoApplication extends Sprite
        {
                private var scene:IsoScene;
                private var assets:Object;
                private var character:IsoSprite
                private var loader:Loader
                
                private function loadAssets ():void
                {
                        loader = new Loader();
                        loader.contentLoaderInfo.addEventListener(Event.INIT, loader_initHandler);
                        loader.load(new URLRequest("./assets/assets.swf"));
                        
                }
                
                private function loader_initHandler (evt:Event):void
                {
                        buildScene();
                }
                
                private function buildScene ():void
                {
					var view:IsoView = new IsoView();
                        view.clipContent = false
                        view.showBorder=false
                        view.setSize(750, 200);
                        //view.y=-300
						
                        scene = new IsoScene();
						
                        view.addScene(scene) //it is recommended to use an IsoView
                       
                        var villager:Class = loader.contentLoaderInfo.applicationDomain.getDefinition("villagertest") as Class;
                        var treeLeavesClass:Class = loader.contentLoaderInfo.applicationDomain.getDefinition("tree") as Class;
                        
                        var grid:IsoGridSprite = new IsoGridSprite();
						grid.setGridSize(20,20,20)
						grid.cellSize = 50
						grid.moveTo(0, 0, 0);
                       // grid.showOrigin = true
						grid.addEventListener(MouseEvent.CLICK, grid_mouseHandler);
                       
                        scene.addChild(grid);
						/*
                       var box3:IsoBox = new IsoBox();
						 box3.setSize(90, 90, 10);
						 box3.moveTo(250, 190, -10);
						 scene.addChild(box3);
						 */
						
                        var box4:IsoBox = new IsoBox();
						 box4.setSize(50, 50, 50);
						 box4.moveTo(300,150,0);
						 scene.addChild(box4);  
                        //
						var box5:IsoBox = new IsoBox();
						 box5.setSize(50, 50, 50);
						 box5.moveTo(50,200,0);
						 scene.addChild(box5);  
						 //
						
                        var s1:IsoSprite = new IsoSprite();
                        s1.setSize(1, 1, 100);
						
                        s1.moveTo(200, 200, 0);
                        s1.sprites = [treeLeavesClass];
						
                        scene.addChild(s1);
						
                        //
						character = new IsoSprite();
                        character.setSize(1,1, 100);
                        character.moveTo(0,0,0)
                        character.sprites = [villager];
                      
						//
						/*
						var s2:IsoSprite = new IsoSprite();
                        s2.setSize(50, 50, 50);
                        s2.moveTo(36, 250, 0);
                        s2.sprites = [treeLeavesClass];
                        scene.addChild(s2);
						*/
						  scene.addChild(character);
                        addChild(view)
						
						
						
						
                }
                
                public function IsoApplication ()
                {
                        loadAssets();
						addEventListener(Event.ENTER_FRAME, drv);
                }
				 private function grid_mouseHandler (evt:ProxyEvent):void
                {
					
                        var mEvt:MouseEvent = MouseEvent(evt.targetEvent);
                        var pt:Pt = new Pt(mEvt.localX, mEvt.localY);
					      IsoMath.screenToIso(pt);
						  //trace("activity" + pt + " " + character)
						  //var from:AStarNode=new AStarNode(character.x,character.y)
						  //var to:AStarNode = new AStarNode(pt.x, pt.y)
						
						//  trace("astar"+AStar.distEuclidian(from,to).toString())
						//TweenLite.to(character,1,{x:pt.x,y:pt.y,onCompleteParams:[character]})
				}
				private function drv(event:Event):void {
					if(scene){
					scene.render()};
				}

        }
}