package kabam.rotmg.tooltips {
import kabam.rotmg.tooltips.view.TooltipsMediator;
import kabam.rotmg.tooltips.view.TooltipsView;

import robotlegs.bender.extensions.mediatorMap.api.IMediatorMap;
import robotlegs.bender.framework.api.IConfig;
import robotlegs.bender.framework.api.IContext;

public class TooltipsConfig implements IConfig {

    public function TooltipsConfig() {
        super();
    }
    [Inject]
    public var context:IContext;
    [Inject]
    public var mediatorMap:IMediatorMap;

    public function configure():void {
        this.mediatorMap.map(TooltipsView).toMediator(TooltipsMediator);
    }
}
}