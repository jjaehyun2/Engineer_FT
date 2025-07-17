//
// $Id$

package {

import avmplus.System;

import com.whirled.thane.HttpUserCodeLoader;

import com.threerings.util.Log;

import com.threerings.msoy.bureau.client.MsoyBureauClient;

public class MsoyThaneClient
{
    Log.setLevels(":debug");
    MsoyBureauClient.main(System.argv, new HttpUserCodeLoader(), cleanup);

    protected static function cleanup (client :MsoyBureauClient) :void
    {
        trace("Exiting bureau");
        System.exit(0);
    }
}
}