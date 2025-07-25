package kabam.rotmg.account.web.view {
import com.company.assembleegameclient.account.ui.Frame;
import com.company.assembleegameclient.ui.DeprecatedClickableText;

import flash.events.MouseEvent;
import flash.filters.DropShadowFilter;

import kabam.rotmg.text.view.TextFieldDisplayConcrete;
import kabam.rotmg.text.view.stringBuilder.LineBuilder;

import org.osflash.signals.Signal;

public class WebVerifyEmailDialog extends Frame {

    public static const TITLE:String = "Please verify your Email in order to play";

    public function WebVerifyEmailDialog() {
        super("Please verify your Email in order to play", "", "");
        this.verify = new Signal();
        h_ = 150;
        w_ = 310;
        this.logout = new Signal();
    }
    public var verify:Signal;
    public var refresh:Signal;
    public var logout:Signal;
    private var verifyTitle:TextFieldDisplayConcrete;
    private var verifySubtitle:TextFieldDisplayConcrete;
    private var verifyEmail:DeprecatedClickableText;
    private var logoutText:DeprecatedClickableText;

    public function setUserInfo(_arg_1:String, _arg_2:Boolean):void {
        if (!_arg_2) {
            this.makeVerifyEmailText(_arg_1);
        }
        this.makeLogoutText();
    }

    private function makeVerifyEmailText(_arg_1:String):void {
        if (this.verifyEmail != null) {
            removeChild(this.verifyEmail);
            removeChild(this.verifyTitle);
            removeChild(this.verifySubtitle);
        }
        this.verifyTitle = new TextFieldDisplayConcrete().setSize(18).setColor(0xff00);
        this.verifyTitle.setBold(true);
        this.verifyTitle.setStringBuilder(new LineBuilder().setParams("Account created"));
        this.verifyTitle.filters = [new DropShadowFilter(0, 0, 0)];
        this.verifyTitle.x = 17;
        this.verifyTitle.y = 38;
        addChild(this.verifyTitle);
        this.verifySubtitle = new TextFieldDisplayConcrete().setSize(14).setColor(0xb3b3b3);
        this.verifySubtitle.setStringBuilder(new LineBuilder().setParams("Check your Inbox and verify your Email we\njust sent to " + _arg_1 + ".\nEmails can arrive delayed in some cases,\nplease also check your spam folder.\n\n"));
        this.verifySubtitle.filters = [new DropShadowFilter(0, 0, 0)];
        this.verifySubtitle.x = 17;
        this.verifySubtitle.y = this.verifyTitle.y + this.verifyTitle.height;
        addChild(this.verifySubtitle);
        this.verifyEmail = new DeprecatedClickableText(14, false, "Resend Email");
        addNavigationText(this.verifyEmail);
        this.verifyEmail.y = this.verifySubtitle.y + this.verifySubtitle.height;
        this.verifyEmail.addEventListener("click", this.onVerifyEmail);
    }

    private function makeLogoutText():void {
        if (this.logoutText != null) {
            removeChild(this.logoutText);
        }
        this.logoutText = new DeprecatedClickableText(14, false, "Log out");
        this.logoutText.addEventListener("click", this.onLogout);
        addNavigationText(this.logoutText);
        this.logoutText.y = this.verifyEmail.y + this.verifyEmail.height;
    }

    private function onVerifyEmail(_arg_1:MouseEvent):void {
        this.verify.dispatch();
        this.verifyEmail.makeStatic("WebAccountDetailDialog.sent");
    }

    private function onLogout(_arg_1:MouseEvent):void {
        this.logout.dispatch();
    }
}
}