package tests.flocking 
{
 import alternativa.engine3d.animation.AnimationClip;
    import alternativa.engine3d.animation.keys.Track;
    import alternativa.engine3d.core.Object3D;
    import alternativa.engine3d.loaders.ParserA3D;
    import alternativa.engine3d.materials.FillMaterial;
    import alternativa.engine3d.materials.StandardMaterial;
    import alternativa.engine3d.materials.TextureMaterial;
    import alternativa.engine3d.objects.Joint;
    import alternativa.engine3d.objects.Skin;
	import alternativa.engine3d.objects.SkinClone;
	import alternativa.engine3d.objects.SkinClonesContainer;
    import alternativa.engine3d.primitives.Plane;
	import alternativa.engine3d.RenderingSystem;
    import alternativa.engine3d.resources.BitmapTextureResource;
	import alternativa.engine3d.Template;
	import alternativa.stances.MechStance;
	import ash.core.Engine;
	import ash.core.Entity;
	import ash.tick.FrameTickProvider;
    import com.greensock.events.LoaderEvent;
    import com.greensock.loading.BinaryDataLoader;
    import com.greensock.loading.ImageLoader;
    import com.greensock.loading.LoaderMax;
	import components.flocking.Flocking;
	import components.flocking.FlockSettings;
	import components.Pos;
	import components.Rot;
	import components.Vel;
    import flash.display.Bitmap;
    import flash.display.BitmapData;
    import flash.display.Loader;
    import flash.events.IEventDispatcher;
    import flash.events.KeyboardEvent;
    import flash.events.MouseEvent;
    import flash.net.URLRequest;
    import flash.system.ApplicationDomain;
    import flash.system.LoaderContext;
    import flash.system.Security;
    import flash.system.SecurityDomain;
    import flash.text.TextField;
    import flash.ui.Keyboard;
    import flash.utils.ByteArray;
    import flash.utils.Dictionary;
	import systems.animation.AnimationSystem;
	import systems.animation.IAnimatable;
	import systems.movement.FlockingSystem;
	import systems.player.a3d.AnimationManager;




    import flash.display.DisplayObject;    
    import flash.display.MovieClip;
    import flash.display.Sprite;
    import flash.events.Event;
    import flash.geom.Vector3D;
    
    import alternativa.engine3d.alternativa3d;
    use namespace alternativa3d;

    /**
     * ...
     * @author Glenn Ko
     */
    [SWF(frameRate="60", backgroundColor="0xddddff")]
    public class TestFlocking3D extends MovieClip
    {
        public var engine:Engine;
        public var ticker:FrameTickProvider;
        
        public static const WORLD_SCALE:Number = 2;
        public static const TEST_FLOCKING:Boolean = true;
        public static const G_WORLD_SIZE_MULT:Number = 1;
                
        private  var WORLD_WIDTH:Number = 1200*WORLD_SCALE*G_WORLD_SIZE_MULT;
        private  var WORLD_HEIGHT:Number = 800 * WORLD_SCALE*G_WORLD_SIZE_MULT;
        
        
        
        private static const NUMBOIDS:int = 100   * 3 * G_WORLD_SIZE_MULT;
        static public const MIN_SPEED:Number = 24*WORLD_SCALE;
        static public const MAX_SPEED:Number = 66*WORLD_SCALE;
        static public const TURN_RATIO:Number = 0.9;
        static public const MIN_DIST:Number = 65*WORLD_SCALE;
        static public const SENSE_DIST:Number = 200*WORLD_SCALE;
        static public const DEFAULT_ROT_X:Number = Math.PI * .5; // for boid

        
        private var _skin:Skin;
        private var _animManager:AnimationManager;
        private var rootContainer:Object3D = new Object3D();
        public var myAssets:Assets;
        
        private var loadingField:TextField;
        
        
        public function TestFlocking3D() 
        {
            super();
            // Wonderfl.disable_capture();
             

             
            
         
            
            
            myAssets = new Assets();
            if (myAssets.MECH_SKIN != null) {
                init();
            }
            else {
                
                
            //    myAssets.addEventListener(Event.COMPLETE, init);
            
                var domain:SecurityDomain = loaderInfo.url.indexOf("file://") >= 0 ? null : SecurityDomain.currentDomain;
                if (domain != null) {
                    Security.loadPolicyFile("http://glidias.github.io/crossdomain.xml");    
                
                }
                
                myAssets.addEventListener(Event.COMPLETE, loadQueueComplete);
                 myAssets.load("http://glidias.github.io/Asharena/assets/skins/mech/bundle.swf", "tests.flocking", new LoaderContext(true, null, domain));
             
                
                loadingField = new TextField();
                
                addChild(loadingField);
              //  loadingField.text = "LOADING...";
                /*
                 LoaderMax.defaultContext = new LoaderContext(true, null, domain);
                var loadQueue:LoaderMax = new LoaderMax();
                
                loadQueue.addEventListener(LoaderEvent.SECURITY_ERROR, onError);
                loadQueue.addEventListener(LoaderEvent.ERROR, onError);
                loadQueue.addEventListener(LoaderEvent.IO_ERROR, onError);
               loadQueue.addEventListener(LoaderEvent.COMPLETE, loadQueueComplete);
                loadQueue.append( new BinaryDataLoader("http://glidias.github.io/Asharena/assets/skins/gladiator/animations.ani", {  name:"anim" } ));
                loadQueue.append( skinbmpLoader=new ImageLoader("http://glidias.github.io/Asharena/assets/skins/gladiator/samnite/samnite_skin.png",{ name:"skinbmp" } ));
                loadQueue.append( new BinaryDataLoader("http://glidias.github.io/Asharena/assets/skins/gladiator/samnite/samnite_lowpolyanim.a3d", {  name:"skin" } ));
                loadQueue.load();
            //    */
                

            }
            
        }
        
        private function onError(e:LoaderEvent):void 
        {
            throw new Error(e + ", "+e.data);
        }
        
        
        
        private function loadTest():void {
            var loader:Loader = new Loader();
            loader.contentLoaderInfo.addEventListener(Event.COMPLETE, onLoadComplete);
            loader.load( new URLRequest("http://glidias.github.io/Asharena/assets/skins/gladiator/samnite/samnite_skin.png"), LoaderMax.defaultContext);
            // new ImageLoader("http://glidias.github.io/Asharena/assets/skins/gladiator/samnite/samnite_skin.png", { name:"skinbmp", onComplete:function(e:Event):void { throw new Error("LOAD DOE:"+e.target.rawContent.content);  }  } ).load();
        
            
        }
        
        private function onLoadComplete(e:Event):void 
        {
            throw new Error(e.currentTarget.content);
        }
        
        private function loadQueueComplete(e:Event):void 
        {
            removeChild(loadingField);
            //loadTest();

            init();
    //        onReady3D( null, LoaderMax.getLoader("skin").content,  LoaderMax.getLoader("skinbmp").rawContent.bitmapData,  LoaderMax.getLoader("anim").content);
            
        }
        
        
        
        
        
        private function init(e:Event=null):void {
            
            engine = new Engine();
            
            if (TEST_FLOCKING) engine.addSystem( new FlockingSystem(), 0 );
            engine.addSystem( new AnimationSystem(), 1 );
            //engine.addSystem( new DisplayObjectRenderingSystem(this), 1);
            
            ticker = new FrameTickProvider(stage);
            ticker.add(tick);
            
            stage.addEventListener(KeyboardEvent.KEY_DOWN, onKeyDown);
            
            MechStance.RANGE = 1 / MAX_SPEED;
            addChild( _template3d = new Template());
            _template3d.settings.cameraSpeed *= 4;
            _template3d.settings.viewBackgroundColor = 0xBBBBBB;
            _template3d.settings.cameraSpeedMultiplier *= 2;
             _template3d.addEventListener(Template.VIEW_CREATE, onReady3D);
    
        
        }
        
    
        private var _template3d:Template;
        private function onReady3D(e:Event, skinData:ByteArray=null, skinBmpData:BitmapData=null, animData:ByteArray=null):void 
        {
                    
            if (e != null) (e.currentTarget as IEventDispatcher).removeEventListener(e.type, onReady3D);
            
            if (loadingField) {
                if (LoaderMax.getLoader("skin")) {
                    skinData = LoaderMax.getLoader("skin").content;
                    var skinBmpDataRawContent:* = skinbmpLoader.rawContent;
                    if (skinBmpDataRawContent == null) throw new Error("Failed to load skinbmp:"+LoaderMax.getLoader("skinbmp") + ", "+skinData + ", "+animData );
                    skinBmpData = skinBmpDataRawContent.bitmapData;
                    animData = LoaderMax.getLoader("anim").content
                }
            }
            
            engine.addSystem( new RenderingSystem(rootContainer), 2 );
            
            
            var child:Object3D = _template3d.scene.addChild( new Plane( 1e4, 1e4, 1, 1, false, false, null, new FillMaterial(0x445544, 1) ) );
            child.x += WORLD_WIDTH * .5;
            child.y += WORLD_HEIGHT * .5;
            child.z -= 72*.5;
            //rootContainer.rotationZ = Math.PI;
          
            var parser:ParserA3D = new ParserA3D();
            parser.parse(skinData || new myAssets.MECH_KAYRATH());
            var skin:Skin = findSkin(parser.objects);
            skin.divide(1000);
        //    skin.calculateBindingMatrices();
            //throw new Error(skin.surfaceJoints.length + "::: " + skin.surfaceJoints[0].length);
            skin.renderedJoints = skin.surfaceJoints[0];
            
        
            
        
            var standardMaterial:StandardMaterial = new StandardMaterial( new BitmapTextureResource(skinBmpData || (new myAssets.MECH_SKIN().bitmapData)), _template3d.normalResource);
            skin.geometry.calculateNormals();
            skin.geometry.calculateTangents(0);
            skin.rotationX = Math.PI * .5;
            skin.rotationZ = Math.PI*.5;
            
            standardMaterial.specularPower = 0;
            skin.boundBox = null;
            skin.setMaterialToAllSurfaces(standardMaterial);
            //_template3d.scene.addChild(skin); 
            _skin = skin;
            
            
            
            skinClonesCont = new SkinClonesContainer(skin, 0, SkinClone);
            rootContainer.addChild(skinClonesCont);
            
            _animManager = new AnimationManager();
            
            var animBytes:ByteArray =  animData || new myAssets.MECH_ANIMS();
            animBytes.uncompress();
            _animManager.readExternal(animBytes );
            
            postProcessAnimManager();
            
            _template3d.cameraController.setObjectPos(new Vector3D(WORLD_WIDTH * .5, WORLD_HEIGHT * .5, 100));
            //_template3d.camera.transformChanged = true;
            //_template3d.cameraController.update();
            //throw new Error(_animManager.animClips[0].name);
            
            _template3d.scene.addChild(rootContainer);
            _template3d.uploadResources(_template3d.scene.getResources(true));
            _template3d.uploadResources(skin.getResources());
            
            
            startGame();
            
        }
        
        private function postProcessAnimManager():void {
            /*
            var len:int = _animManager.animClips.length;
            for (var i:int = 0; i < len; i++) {
                removeAnimationTrack(_animManager, _animManager.animClips[i].name ,"Bip01");
            }
            */
            removeAnimationTrack(_animManager, "jog" ,"Bip01");
            //
        }
        private function removeAnimationTrack(animManager:AnimationManager, animName:String, boneName:String):void 
        {
            var anim:AnimationClip = animManager.getAnimationByName(animName);
            
            var len:int = anim.numTracks;
            for (var i:int = 0; i < len ; i++) {
                var t:Track = anim.getTrackAt(i);
                if (t.object === boneName) {
                    anim.removeTrack(t);
                    
                    return;
                }
            }
            
        }
        
        private function startGame():void 
        {
            createBoids();
            ticker.start();
        }
        private function findSkin(objects:Vector.<Object3D>):Skin {
            for each(var obj:Object3D in objects) {
                if (obj is Skin) return obj as Skin;
            }
            throw new Error("Could not find skin:");
            return null;
        }
        
        
        private var playing:Boolean = true;
        
        private function onKeyDown(e:KeyboardEvent):void 
        {
            var kc:uint = e.keyCode;
            if (kc === Keyboard.P) {
                playing = !playing;
                if (playing) ticker.start()
                else ticker.stop();
            }
            else if (kc === Keyboard.F6) {
                _template3d.takeScreenshot(screenieMethod);
            }
            else if (kc === Keyboard.F7) {
                _scrnie=_template3d.takeScreenshot(screenieMethod2);
            }
        }
        
          private function screenieMethod():Boolean 
        {
           
            return true;
        
        }
        
         private function screenieMethod2():Boolean 
        {
            stage.addEventListener(MouseEvent.CLICK, removeScreenie);
            return false;
        }
        private var _scrnie:Bitmap;
        private var skinClonesCont:SkinClonesContainer;
        private var skinbmpLoader:ImageLoader;
          private function removeScreenie(e:Event=null):void {
            if (_scrnie == null) return;
            stage.removeEventListener(MouseEvent.CLICK, removeScreenie);
            _scrnie.parent.removeChild(_scrnie);
            _scrnie = null;
        }
        
        
        private function tick(time:Number):void 
        {
            engine.update(time);
            
            _template3d.cameraController.update(time);
            _template3d.camera.render(_template3d.stage3D); // onRenderTick();
        }
        
        
        private function createBoids():void 
        {
            
             var tmp:Number = 2.0 * Math.PI / NUMBOIDS;
             
                var tmpw:int = WORLD_WIDTH / 2 , tmph:int = WORLD_HEIGHT / 2;
                var flockSettings:FlockSettings = Flocking.createFlockSettings(MIN_DIST,SENSE_DIST,0,0,tmpw*2, tmph*2, MIN_SPEED, MAX_SPEED, TURN_RATIO);
              
            for (var i:int = 0; i < NUMBOIDS; ++i) {
                 const ph:Number = i * tmp;
                var pos:Pos = new Pos(  tmpw + ((i % 4) * 0.2 + 0.3) * tmpw * Math.cos(ph), tmph + ((i % 4) * 0.2 + 0.3) * tmph * Math.sin(ph));
                
                
                var vel:Vel = new Vel( ((i%4)*(-4) + 16) * Math.cos(ph + Math.PI / 6 * (1+i%4) * (Math.random() - 0.5)),  ((i%4)*(-4) + 16) * Math.sin(ph + Math.PI / 6 * (1+i%4) * (Math.random() - 0.5)));
                
                var rot:Rot = new Rot(0, 0, Math.random() * 2 * Math.PI);
                

                
                var entity:Entity = new Entity().add(pos).add(rot).add(vel).add( new Flocking().setup(flockSettings )) ;
                
                //entity.add( new BoidGraphic(), DisplayObject);
                ///*
                var obj:Object3D;// = new Object3D();
                var skinClone:SkinClone  =  skinClonesCont.createClone();
                var skin:Object3D =skinClone.root ;// _skin.clone() as Skin;
                //obj.addChild(skin);
                obj = skin;
                
                skinClonesCont.addClone(skinClone);
                entity.add( new MechStance( _animManager.cloneFor(skin.childrenList), vel, skinClone.renderedJoints, !TEST_FLOCKING ), IAnimatable).add(obj, Object3D);
                //*/
                
                /*
                var obj:Object3D= new Object3D();
                var skin:Object3D =_skin.clone() as Skin;
                obj.addChild(skin);
                
                
            
                
                //obj = skin;
                rootContainer.addChild(obj);

                entity.add( new MechStance( _animManager.cloneFor(skin), vel, (skin as Skin).renderedJoints ), IAnimatable).add(obj, Object3D);
                */
                
                engine.addEntity(entity);
            }
        }
        
        
        
    
    }
		

}