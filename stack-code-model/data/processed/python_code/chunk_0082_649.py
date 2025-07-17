//
// $Id$

package com.threerings.msoy.game.client {

import com.threerings.presents.client.InvocationService;
import com.threerings.presents.client.InvocationService_ConfirmListener;
import com.threerings.presents.client.InvocationService_ResultListener;

/**
 * An ActionScript version of the Java GameGameService interface.
 */
public interface GameGameService extends InvocationService
{
    // from Java interface GameGameService
    function complainPlayer (arg1 :int, arg2 :String) :void;

    // from Java interface GameGameService
    function getTrophies (arg1 :int, arg2 :InvocationService_ResultListener) :void;

    // from Java interface GameGameService
    function removeDevelopmentTrophies (arg1 :int, arg2 :InvocationService_ConfirmListener) :void;
}
}