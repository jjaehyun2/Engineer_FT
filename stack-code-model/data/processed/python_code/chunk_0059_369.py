/**
 * Created by max.rozdobudko@gmail.com on 12/3/17.
 */
package com.github.airext.notifications {
public class NotificationContent {

    public function NotificationContent() {
        super();
    }

    public var title: String;
    public var body: String;
    public var sound: NotificationSound;
    public var color: int;
    public var userInfo: Object;

    public function userInfoAsJSON(): String {
        return JSON.stringify(userInfo);
    }

    public function toString(): String {
        return '[NotificationContent(title="'+title+'", body="'+body+'", sound="'+sound+'", color="'+color+'", userInfo="'+userInfo+'")]';
    }
}
}