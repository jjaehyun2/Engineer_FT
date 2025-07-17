//
// $Id$

package com.threerings.msoy.ui {

import flash.display.Sprite;
import flash.text.TextField;
import flash.text.TextFieldAutoSize;
import flash.text.TextFormat;

import com.threerings.crowd.data.OccupantInfo;

import com.threerings.text.TextFieldUtil;

import com.threerings.msoy.client.MsoyController;
import com.threerings.msoy.data.MsoyUserOccupantInfo;
import com.threerings.msoy.room.data.MemberInfo;
import com.threerings.msoy.room.data.PuppetName;
import com.threerings.msoy.data.MsoyTokenRing;

public class MsoyNameLabel extends Sprite
{
    public function MsoyNameLabel (ignoreStatus :Boolean = false)
    {
        _ignoreStatus = ignoreStatus;

        // TODO: the outline trick just barely works here, perhaps it is time to consider a
        // different solution, including using different code for avatars and occupant list
        // NOTE: the look of this text field must match the labels in MsoyGamePlayerList
        _label = TextFieldUtil.createField("",
            { textColor: 0xFFFFFF, selectable: false, autoSize :TextFieldAutoSize.LEFT,
            outlineColor: 0x000000, outlineWidth: 5, outlineStrength: 12 });

        // It's ok that we modify this later, as it gets cloned anyway when assigned to the field.
        _label.defaultTextFormat = FORMAT;
        _label.x = 0;
        addChild(_label);
    }

    /**
     * Update the name based on an OccupantInfo.
     */
    public function update (info :OccupantInfo) :void
    {
        setName(info.username.toString());
        setSubscriber((info is MsoyUserOccupantInfo) && MsoyUserOccupantInfo(info).isSubscriber());
        setStaff((info is MsoyUserOccupantInfo) && MsoyUserOccupantInfo(info).isSupport());
        setStatus(info.status, (info is MemberInfo) && MemberInfo(info).isAway(), false,
            (info.username is PuppetName));
    }

    /**
     * Set the displayed name.
     */
    public function setName (name :String) :void
    {
        TextFieldUtil.updateText(_label, name);
    }

    /**
     * Set whether we're displaying a subscriber.
     */
    public function setSubscriber (subscriber :Boolean) :void
    {
        if (subscriber == (_subscriberIcon == null)) {
            if (subscriber) {
                _subscriberIcon = new GlowSprite();
                _subscriberIcon.addChild(new SUBSCRIBER());
                _subscriberIcon.init(0xFFFFFF, MsoyController.SUBSCRIBE);
                addChild(_subscriberIcon);
                _label.x = _subscriberIcon.width;

            } else {
                removeChild(_subscriberIcon);
                _subscriberIcon = null;
                _label.x = 0;
            }
        }
    }
     /**
     * Set whether we're displaying a staff member
     */
    public function setStaff (staff :Boolean) :void
    {
        if (staff == (_staffIcon == null)) {
            if (staff) {
                _staffIcon = new GlowSprite();
                _staffIcon.addChild(new STAFF());
                _staffIcon.init(0xFFFFFF, MsoyController.STAFF);
                addChild(_staffIcon);
                _label.x = _staffIcon.width;

            } else {
                removeChild(_staffIcon);
                _staffIcon = null;
                _label.x = 0;
            }
        }
    }
    
    /**
     * Updates our member's status (idle, disconnected, etc.).
     */
    public function setStatus (
        status :int, away :Boolean, italicize :Boolean, isPuppet :Boolean = false) :void
    {
        if (_ignoreStatus) {
            return;
        }

        if (away) {
            _label.textColor = 0xFFFF77;
        } else if (status == OccupantInfo.IDLE) {
            _label.textColor = 0x777777;
        } else if (status == OccupantInfo.DISCONNECTED) {
            _label.textColor = 0x80803C;
        } else if (isPuppet) {
            _label.textColor = 0xFFBF99;
        } else {
            _label.textColor = 0x99BFFF;
        }

        // turn on or off italicizing.
        TextFieldUtil.updateFormat(_label, { italic: italicize });
    }

    protected var _ignoreStatus :Boolean;

    protected var _label :TextField;

    protected var _subscriberIcon :GlowSprite;
    protected var _staffIcon :GlowSprite;

    protected static const FORMAT :TextFormat =
        TextFieldUtil.createFormat({ font: "_sans", size: 12, letterSpacing: .6 });

    [Embed(source="../../../../../../pages/images/ui/clubwhirled.png")]
    protected static const SUBSCRIBER :Class;
    
    [Embed(source="../../../../../../pages/images/ui/virtuedev.png")]
    protected static const STAFF :Class;
    
}
}