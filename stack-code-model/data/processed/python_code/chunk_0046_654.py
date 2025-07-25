﻿// Decompiled by AS3 Sorcerer 6.08
// www.as3sorcerer.com

//kabam.rotmg.core.commands.SetupDomainSecurityCommand

package kabam.rotmg.core.commands
{
    import kabam.rotmg.application.model.PlatformModel;
    import kabam.rotmg.application.model.DomainModel;

    public class SetupDomainSecurityCommand 
    {

        [Inject]
        public var client:PlatformModel;
        [Inject]
        public var domains:DomainModel;


        public function execute():void
        {
            if (this.client.isWeb())
            {
                this.domains.applyDomainSecurity();
            }
        }


    }
}//package kabam.rotmg.core.commands