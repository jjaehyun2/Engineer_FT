﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//kabam.rotmg.minimap.MiniMapConfig

package kabam.rotmg.minimap
{
    import robotlegs.bender.framework.api.IConfig;
    import robotlegs.bender.framework.api.IContext;
    import org.swiftsuspenders.Injector;
    import robotlegs.bender.extensions.mediatorMap.api.IMediatorMap;
    import kabam.rotmg.minimap.control.MiniMapZoomSignal;
    import kabam.rotmg.minimap.control.SetMiniMapMapSignal;
    import kabam.rotmg.minimap.control.UpdateGameObjectTileSignal;
    import kabam.rotmg.minimap.control.UpdateGroundTileSignal;
    import io.decagames.rotmg.classes.NewClassUnlockSignal;
    import kabam.rotmg.minimap.view.MiniMap;
    import kabam.rotmg.minimap.view.MiniMapMediator;
    import io.decagames.rotmg.classes.NewClassUnlockNotification;
    import io.decagames.rotmg.classes.NewClassUnlockNotificationMediator;

    public class MiniMapConfig implements IConfig 
    {

        [Inject]
        public var context:IContext;
        [Inject]
        public var injector:Injector;
        [Inject]
        public var mediatorMap:IMediatorMap;


        public function configure():void
        {
            this.injector.map(MiniMapZoomSignal).asSingleton();
            this.injector.map(SetMiniMapMapSignal).asSingleton();
            this.injector.map(UpdateGameObjectTileSignal).asSingleton();
            this.injector.map(UpdateGroundTileSignal).asSingleton();
            this.injector.map(NewClassUnlockSignal).asSingleton();
            this.mediatorMap.map(MiniMap).toMediator(MiniMapMediator);
            this.mediatorMap.map(NewClassUnlockNotification).toMediator(NewClassUnlockNotificationMediator);
        }


    }
}//package kabam.rotmg.minimap