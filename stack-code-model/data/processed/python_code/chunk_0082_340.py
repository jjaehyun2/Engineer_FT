﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//io.decagames.rotmg.tos.config.ToSConfig

package io.decagames.rotmg.tos.config
{
    import robotlegs.bender.framework.api.IConfig;
    import robotlegs.bender.extensions.mediatorMap.api.IMediatorMap;
    import io.decagames.rotmg.tos.popups.buttons.RefuseButton;
    import io.decagames.rotmg.tos.popups.buttons.RefuseButtonMediator;
    import io.decagames.rotmg.tos.popups.buttons.GoBackButton;
    import io.decagames.rotmg.tos.popups.buttons.GoBackButtonMediator;
    import io.decagames.rotmg.tos.popups.buttons.AcceptButton;
    import io.decagames.rotmg.tos.popups.buttons.AcceptButtonMediator;

    public class ToSConfig implements IConfig 
    {

        [Inject]
        public var mediatorMap:IMediatorMap;


        public function configure():void
        {
            this.mediatorMap.map(RefuseButton).toMediator(RefuseButtonMediator);
            this.mediatorMap.map(GoBackButton).toMediator(GoBackButtonMediator);
            this.mediatorMap.map(AcceptButton).toMediator(AcceptButtonMediator);
        }


    }
}//package io.decagames.rotmg.tos.config