/**
 * Created by matej on 2/4/15.
 */
package com432tone.demo.robotlegs2demo.command
{

    import com432tone.demo.robotlegs2demo.model.AppModel;

    import robotlegs.bender.extensions.commandCenter.api.ICommand;

    import robotlegs.bender.framework.api.ILogger;

    public class ViewClickedCommand implements ICommand
    {

        [Inject]
        public var appModel:AppModel;
        
        [Inject]
        public var logger:ILogger;
        
        public function execute():void {
            logger.debug("Increasing count on model");
            appModel.increaseClickCount();
        }

    }
}