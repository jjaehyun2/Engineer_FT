package kabam.rotmg.game.focus {
import com.company.assembleegameclient.game.GameSprite;

import kabam.rotmg.game.focus.control.SetGameFocusSignal;
import kabam.rotmg.game.focus.view.GameFocusMediator;

import org.swiftsuspenders.Injector;

import robotlegs.bender.extensions.mediatorMap.api.IMediatorMap;
import robotlegs.bender.extensions.signalCommandMap.api.ISignalCommandMap;
import robotlegs.bender.framework.api.IConfig;
import robotlegs.bender.framework.api.IContext;

public class GameFocusConfig implements IConfig {


    public function GameFocusConfig() {
        super();
    }
    [Inject]
    public var context:IContext;
    [Inject]
    public var injector:Injector;
    [Inject]
    public var commandMap:ISignalCommandMap;
    [Inject]
    public var mediatorMap:IMediatorMap;

    public function configure():void {
        this.injector.map(SetGameFocusSignal).asSingleton();
        this.mediatorMap.map(GameSprite).toMediator(GameFocusMediator);
    }
}
}