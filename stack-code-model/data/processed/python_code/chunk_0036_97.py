//
// $Id$

package com.threerings.msoy.notify.client {
import flash.display.DisplayObject;
import flash.events.MouseEvent;
import flash.events.TextEvent;
import flash.events.TimerEvent;
import flash.geom.Point;
import flash.text.AntiAliasType;
import flash.text.TextField;
import flash.text.TextFieldAutoSize;
import flash.text.TextFormat;
import flash.utils.Timer;
import flash.utils.setTimeout;

import caurina.transitions.Tweener;

import mx.containers.Canvas;
import mx.containers.HBox;
import mx.core.ScrollPolicy;
import mx.core.UIComponent;
import mx.managers.PopUpManager;

import com.threerings.util.ClassUtil;
import com.threerings.util.Log;

import com.threerings.text.TextFieldUtil;

import com.threerings.orth.notify.client.NotificationDisplay;
import com.threerings.orth.notify.data.Notification;

import com.threerings.flex.CommandCheckBox;
import com.threerings.flex.FlexWrapper;

import com.threerings.msoy.chat.client.ChatOverlay;
import com.threerings.msoy.client.Msgs;
import com.threerings.msoy.client.MsoyContext;
import com.threerings.msoy.utils.TextUtil;

public class MsoyNotificationDisplay extends HBox
    implements NotificationDisplay
{
    public function MsoyNotificationDisplay (ctx :MsoyContext, canvasHeight :int) :void
    {
        _ctx = ctx;
        _canvasHeight = canvasHeight;
        _clearTimer.addEventListener(TimerEvent.TIMER, clearCurrentNotification);
    }

    public function clearDisplay () :void
    {
        if (_canvas.numChildren > 0) {
            // should only have one child
            var child :DisplayObject = _canvas.getChildAt(0);
            Tweener.addTween(child, {x: _canvas.width, time: 0.75, transition: "easeoutquart",
                onComplete: function () :void {
                    if (child.parent == _canvas) {
                        _canvas.removeChild(child);
                    }
                }
            });
        }

        hideNotificationHistory();
    }

    public function displayNotification (notification :Notification) :void
    {
        // TODO: this is here to allow BadgeEarnedNotification to forgo normal notification
        // display.  It would be great if we required it to display something, and then clicking
        // on the announcement caused it to show the fancy display again.
        if (notification.getAnnouncement() == null) {
            // again, this is temporary.  We should always have the notification put something in
            // the history, and probably defer this custom display until the notification's
            // priority has decreed that it get shown in the history display.  Also, all
            // notifications should be allowed to do custom shit, so this is doubly weird.
            displayCustomNotification(notification);
            return;
        }

        _pendingNotifications.push(notification);
        checkPendingNotifications();

        if (_nHistory != null) {
            _nHistory.addNotification(createDisplay(notification, true));
        }
    }

    public function sizeDidChange () :void
    {
        if (_nHistory != null) {
            // all the history text might need updating, just hide and re-show
            hideNotificationHistory();
            toggleNotificationHistory(true);
            _popupBtn.selected = true;
        }

        updateCurrentDisplay(false);
    }

    override protected function createChildren () :void
    {
        super.createChildren();
        styleName = "notificationDisplay";
        this.percentWidth = 100;

        addChild(_canvas = new Canvas());
        _canvas.styleName = "notificationCanvas";
        _canvas.percentWidth = 100;
        _canvas.height = _canvasHeight;
        _canvas.horizontalScrollPolicy = ScrollPolicy.OFF;
        _canvas.verticalScrollPolicy = ScrollPolicy.OFF;

        addChild(_popupBtn = new CommandCheckBox(null, toggleNotificationHistory));
        _popupBtn.styleName = "notificationToggle";
    }

    protected function maybeCloseHistory (event :MouseEvent) :void
    {
        // only close if they clicked outside the history
        if (!_nHistory.getBounds(_nHistory.stage).contains(event.stageX, event.stageY)) {
            hideNotificationHistory();
        }
    }

    protected function checkPendingNotifications () :void
    {
        if (_animating) {
            return;
        }
        if (_pendingNotifications.length == 0) {
            _clearTimer.start(); // in 60 seconds we'll clear this notification
            return;
        }

        _current = Notification(_pendingNotifications.shift());
        _animating = true;
        updateCurrentDisplay(true);

        // set up the min/max display times
        _clearTimer.delay = 1000 * _current.getMaxDisplayTime();
        _clearTimer.reset();
        setTimeout(function () :void {
            _animating = false;
            checkPendingNotifications();
        }, _current.getMinDisplayTime() * 1000);
    }

    protected function updateCurrentDisplay (slide :Boolean) :void
    {
        if (_current == null) {
            return;
        }

        var left :int = 5;
        var notification :UIComponent = createDisplay(_current);
        notification.y = (_canvasHeight - notification.height) / 2;
        notification.x = slide ? _canvas.width : left;
        _canvas.removeAllChildren();
        _canvas.addChild(notification);

        if (slide) {
            Tweener.addTween(notification, { x: left, time: 0.75, transition: "easeoutquart" });
        }
    }

    protected function displayCustomNotification (notification :Notification) :void
    {
        var clazz :String = notification.getDisplayClass();
        if (clazz == null) {
            return;
        }

        var thing :Object = new (ClassUtil.getClassByName(clazz))();
        thing.init(_ctx, notification);
    }

    protected function clearCurrentNotification (event :TimerEvent = null) :void
    {
        // TODO: fancy fade? that would call attention to a 60 second old notification which
        // doesn't seem like what we want
        _canvas.removeAllChildren();
        _current = null;
    }

    protected function createDisplay (
        notification :Notification, forHistory :Boolean = false) :UIComponent
    {
        var format :TextFormat = ChatOverlay.createChatFormat();
        format.size = Math.min(15, int(format.size));
        format.color = getColor(notification);
        var text :TextField = new TextField();
        TextFieldUtil.trackOnlyLinksMouseable(text);
        text.multiline = forHistory;
        text.wordWrap = forHistory;
        // I would rather not make the text selectable, but clicking on links doesn't work if it's
        // not.  wtf?
        text.selectable = true;
        text.autoSize = TextFieldAutoSize.LEFT;
        text.antiAliasType = AntiAliasType.ADVANCED;
        const announcement :String = Msgs.NOTIFY.xlate(notification.getAnnouncement());
        TextUtil.setText(text, TextUtil.parseLinks(announcement, format, true, true), format);

        // possibly set up the click tracker
        if (notification.clickTracker != null) {
            text.addEventListener(MouseEvent.CLICK, function (... ignored) :void {
                notification.clickTracker();
            });
        }

        if (forHistory) {
            // TODO: this is still cropping the text, even without the PADDING
            text.width = getHistoryWidth(false);
        } else {
            text.width = _canvas.width * 2;
            while (text.textWidth > _canvas.width && text.length > 4) {
                // as odd as this looks, it replaces the last 4 characters with "..."
                text.replaceText(text.length - 5, text.length, "...");
            }
        }

        var wrapper :FlexWrapper = new FlexWrapper(text, true);
        if (!forHistory) {
            return wrapper;
        }

        // if for history, we need to wrap it in the box that can be styled with padding, etc
        var box :HBox = new HBox();
        box.styleName = "notificationHistoryCell";
        box.addChild(wrapper);
        return box;
    }

    protected function toggleNotificationHistory (show :Boolean) :void
    {
        hideNotificationHistory();

        if (show) {
            var histWidth :int = getHistoryWidth(true);

            _nHistory = new NotificationHistoryDisplay(prepareNotifications(
                _ctx.getNotificationDirector().getCurrentNotifications()));
            _nHistory.width = histWidth;
            _nHistory.addEventListener(TextEvent.LINK, dispatchEvent);
            PopUpManager.addPopUp(_nHistory, _ctx.getTopPanel(), false);

            var canvasPos :Point = localToGlobal(new Point(_canvas.x, _canvas.y));
            var limitPos :Point = localToGlobal(new Point(this.width - histWidth, _canvas.y));
            _nHistory.x = Math.min(canvasPos.x, limitPos.x);
            _nHistory.y = canvasPos.y - _nHistory.height;

            systemManager.addEventListener(MouseEvent.CLICK, maybeCloseHistory);
        }
    }

    protected function hideNotificationHistory (...ignored) :void
    {
        if (_nHistory == null) {
            return;
        }

        PopUpManager.removePopUp(_nHistory);
        systemManager.removeEventListener(MouseEvent.CLICK, maybeCloseHistory);
        _nHistory = null;
        _popupBtn.selected = false;
    }

    protected function getHistoryWidth (pad :Boolean) :int
    {
        var histWidth :int = Math.max(200, this.width - _popupBtn.width);
        histWidth += pad ? NotificationHistoryDisplay.PADDING : 0;
        return histWidth;
    }

    protected function prepareNotifications (notifs :Array) :Array
    {
        var notifications :Array = [];
        for each (var notification :Notification in notifs) {
            // TODO: temporary work-around, as noted in displayNotification
            if (notification.getAnnouncement() == null) {
                continue;
            }
            notifications.push(createDisplay(notification, true));
        }
        return notifications;
    }

    protected function getColor (notification :Notification) :uint
    {
        switch (notification.getCategory()) {
        case Notification.SYSTEM: return 0x40b86e;
        case Notification.INVITE: return 0x0d259f;
        case Notification.PERSONAL: return 0xf17b28;
        case Notification.BUTTSCRATCHING: return 0x737373;
        case Notification.LOWEST: // fall through to default
        default: return 0xa0a0a0;
        }
    }

    protected static const log :Log = Log.getLog(MsoyNotificationDisplay);

    protected var _ctx :MsoyContext;
    protected var _canvasHeight :int;
    protected var _canvas :Canvas;
    protected var _popupBtn :CommandCheckBox;
    protected var _pendingNotifications :Array = [];
    protected var _current :Notification;
    protected var _animating :Boolean;
    protected var _nHistory :NotificationHistoryDisplay;
    protected var _clearTimer :Timer = new Timer(1, 1);
}
}