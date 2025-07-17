/**
 * Created by matej on 2/4/15.
 */
package com432tone.demo.robotlegs2demo.config
{

    import com432tone.demo.robotlegs2demo.model.AppModel;

    import robotlegs.bender.framework.api.IConfig;

    import robotlegs.bender.framework.api.IInjector;

    public class ModelConfig implements IConfig
    {
        
//        This is the hearth of robotlegs2, it is SwiftSuspenders DependencyInjection Library.
//        If you pass Inject tag before public variable, it will populate that variable with rule that is mapped to the 
//        injector. While installing MVCSBundle, some rules are allready there so we can use them allready, but for 
//        anything else, we have to map it.
        [Inject]
        public var injector:IInjector;

        public function configure():void {

//            Mapping AppModel as singleton will return to us the same instance of AppModel every time we write 
            /*
            [Inject]
            public var model:AppModel;
             */
//            So it is handy to get model data, anywhere we need it.
            injector.map(AppModel).asSingleton();
        }
    }
}