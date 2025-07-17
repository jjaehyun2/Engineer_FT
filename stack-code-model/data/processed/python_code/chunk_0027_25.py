//
// $Id$

package com.threerings.msoy.game.client {

import com.whirled.game.client.ThaneGameBackend;
import com.whirled.game.client.ThaneGameController;

import com.threerings.parlor.game.data.UserIdentifier;

import com.threerings.msoy.game.data.MsoyUserIdentifier;
import com.threerings.msoy.game.data.ParlorGameObject;

/** Msoy-specific game controller. */
public class MsoyThaneGameController extends ThaneGameController
{
    /** Creates a new game controller. */
    public function MsoyThaneGameController ()
    {
        super();

        // init the static identifier each time. Not sure if there's a better place for it.
        UserIdentifier.setIder(MsoyUserIdentifier.getUserId);
    }

    /** @inheritDoc */
    // from ThaneGameController
    override protected function createBackend () :ThaneGameBackend
    {
        // create the msoy-specific subclass
        return new MsoyThaneGameBackend(_ctx, _gameObj as ParlorGameObject, this);
    }
}
}