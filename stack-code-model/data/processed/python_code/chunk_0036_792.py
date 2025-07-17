/**
 * Created by matej on 2/4/15.
 */
package com432tone.demo.robotlegs2demo.config
{

    import com432tone.demo.robotlegs2demo.mediator.MainMediator;

    import robotlegs.bender.extensions.mediatorMap.api.IMediatorMap;
    import robotlegs.bender.framework.api.IConfig;

    public class MediatorConfig implements IConfig
    {
        [Inject]
        public var mediatorMap:IMediatorMap;

        public function configure():void {
            mediatorMap.map(Main).toMediator(MainMediator);
        }
    }
}