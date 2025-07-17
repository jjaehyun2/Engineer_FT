package cn.geckos.shuttle.controllers
{
import cn.geckos.shuttle.managers.AccountsManager;

import org.puremvc.as3.interfaces.INotification;
import org.puremvc.as3.patterns.command.SimpleCommand;

public class AddAccountCommand extends SimpleCommand
{
    override public function execute(notification:INotification):void
    {
        var data:Object = notification.getBody();
        AccountsManager.getInstance().addAccount(data.id, data.service);
    }
        
}
}