//
// $Id$

package com.threerings.msoy.world.tour.client {

import mx.core.UIComponent;

import com.threerings.util.Log;

import com.threerings.presents.client.BasicDirector;
import com.threerings.presents.client.Client;
import com.threerings.presents.dobj.AttributeChangeAdapter;
import com.threerings.presents.dobj.AttributeChangedEvent;

import com.threerings.msoy.data.MemberObject;
import com.threerings.msoy.data.MsoyCodes;
import com.threerings.msoy.room.client.RoomObjectView;
import com.threerings.msoy.world.client.WorldClient;
import com.threerings.msoy.world.client.WorldContext;
import com.threerings.msoy.world.tour.data.TourMarshaller;

public class TourDirector extends BasicDirector
{
    public const log :Log = Log.getLog(this);

    // reference the TourMarshaller class
    TourMarshaller;

    public function TourDirector (ctx :WorldContext)
    {
        super(ctx);
        _wctx = ctx;
    }

    public function isOnTour () :Boolean
    {
        const mobj :MemberObject = _wctx.getMemberObject();
        return (mobj != null && mobj.onTour);
    }

    public function startTour () :void
    {
        if (isOnTour()) {
            _wctx.displayFeedback(MsoyCodes.WORLD_MSGS, "e.already_touring");

        } else {
            nextRoom();
        }
    }

    public function nextRoom (button :UIComponent = null) :void
    {
        const roomView :RoomObjectView = _wctx.getPlaceView() as RoomObjectView;
        const loadingDone :Boolean = (roomView != null) && roomView.loadingDone();
        _tsvc.nextRoom(loadingDone,
            _wctx.resultListener(handleNextRoomResult, MsoyCodes.WORLD_MSGS, null, button));
    }

    public function endTour () :void
    {
        if (_tourDialog != null) {
            closeTourDialog(); // will end up calling back to endTour()

        } else if (isOnTour()) {
            _tsvc.endTour();
        }
    }

    protected function handleNextRoomResult (sceneId :int) :void
    {
        _wctx.getSceneDirector().moveTo(sceneId);
        _tourDialog.setRating(0);
    }

    /**
     * Called when attributes change on our client object.
     */
    protected function cliObjAttrChanged (event :AttributeChangedEvent) :void
    {
        if (event.getName() == MemberObject.ON_TOUR) {
            checkTouringStatus();
        }
    }

    protected function checkTouringStatus () :void
    {
        if (isOnTour()) {
            if (_tourDialog == null) {
                _tourDialog = new TourDialog(_wctx);
                _tourDialog.addCloseCallback(dialogWasClosed);
                _tourDialog.open();
            }
        } else {
            // TEMP: debugging TODO
            if (_tourDialog != null) {
                log.warning("Did we fall out of the tour?", new Error());
            }
            // END: TEMP

            // TEMP more: for now, let's just not close it: leave it up until the user kills it
            //closeTourDialog();
            // END
            // if we keep this off, we can refactor/cleanup a bit...
        }
    }

    protected function closeTourDialog () :void
    {
        if (_tourDialog != null) {
            _tourDialog.close();
        }
    }

    protected function dialogWasClosed () :void
    {
        _tourDialog = null;
        endTour();
    }

    // from BasicDirector
    override protected function clientObjectUpdated (client :Client) :void
    {
        super.clientObjectUpdated(client);

        WorldClient(client).bodyOf().addListener(new AttributeChangeAdapter(cliObjAttrChanged));
        checkTouringStatus();
    }

    // from BasicDirector
    override protected function registerServices (client :Client) :void
    {
        super.registerServices(client);

        client.addServiceGroup(MsoyCodes.WORLD_GROUP);
    }

    // from BasicDirector
    override protected function fetchServices (client :Client) :void
    {
        super.fetchServices(client);

        _tsvc = (client.requireService(TourService) as TourService);
    }

    protected var _wctx :WorldContext;

    protected var _tsvc :TourService;

    protected var _tourDialog :TourDialog;
}
}