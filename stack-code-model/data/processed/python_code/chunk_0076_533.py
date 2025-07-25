package kabam.rotmg.servers.model {
import com.company.assembleegameclient.parameters.Parameters;

import kabam.rotmg.servers.api.Server;
import kabam.rotmg.servers.api.ServerModel;

public class LocalhostServerModel implements ServerModel {


    public function LocalhostServerModel() {
        super();
        this.localhost = new Server().setName("localhost").setAddress("localhost").setPort(Parameters.PORT);
    }
    private var localhost:Server;

    public function getServers():Vector.<Server> {
        return new <Server>[this.localhost];
    }

    public function getServer():Server {
        return this.localhost;
    }

    public function isServerAvailable():Boolean {
        return true;
    }

    public function setServers(servers:Vector.<Server>):void {
    }
}
}