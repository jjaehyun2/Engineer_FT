/**
 * Created by Akira on 03/03/2015.
 */
package com.bytesfromouterspace.stockbrokers.view {

    import com.bytesfromouterspace.stockbrokers.ui.components.BlockerPanel;
    import com.bytesfromouterspace.stockbrokers.ui.components.Button;

    import flash.display.Sprite;
    import flash.events.Event;
    import flash.events.MouseEvent;
    import flash.text.TextField;
    import flash.text.TextFormat;

    public class HelpView extends BlockerPanel {

        private var content:Sprite;
        private var btnClose:Button;

        public function HelpView(showStart:Boolean) {
            super();
            content = new Sprite();
            content.graphics.lineStyle(1, 0xFFFFFF);
            content.graphics.beginFill(0x121212);
            content.graphics.drawRect(0, 0, 600, 500);
            content.graphics.endFill();
            content.x = _width * 0.5 - content.width * 0.5;
            content.y = _height * 0.5 - content.height * 0.5;
            addChild(content);
            //Greedy you are, Whack a Stock you will play!
            var txt:TextField = new TextField();
            txt.x = 30;
            txt.y = 30;
            txt.width = 550;
            txt.height = 400;
            txt.wordWrap = true;
            txt.autoSize = "left";
            txt.embedFonts = true;
            var tfm:TextFormat = theme.getDefaultTextFormat();
            tfm.leading = 10;
            txt.defaultTextFormat = tfm;
            content.addChild(txt);
            txt.text = "Greedy you are, Whack a Stock you will play!\n\nWelcome to Whack a Stock!\n\nThe game objective is to make profit and gain reputation before you run out of cash or reach turn 100. Buy cheap and sell high to get max profit! When a price starts to blink, it may be better to sell that stocks!" +
                    "\n\nEach turn takes 12 seconds at least. Certain operations may increase timer and leveling up allows you to use reset button. Use resets wisely!" +
                    "\n\nAt end of each turn, interest rates are stolen from your wallet. Also, the evil market controller steals 1k per turn. They do not work for free!" +
                    "\n\nReputation is gained and lost according to your actions. \n\nYou gain reputation by buying stocks and selling with profit." +
                    "\n\nYou lose reputation by trying to buy air, selling without profit, sell what you don’t have and using monopoly money! If you don’t have enough money to buy it ask for an investor. Take care however with the interest rates! They hurt… a lot!\n\nHave fun!";
            btnClose = new Button(70, 16);
            btnClose.buttonBackgroundNormal = 0x444444;
            btnClose.buttonBorderNormal = 0x999999;
            btnClose.drawBackground();
            btnClose.setLabel("Okidoki", 10, 0xFFFFFF, "visitor1");
            btnClose.x = content.width * 0.5 - btnClose.width * 0.5;
            btnClose.y = content.height - 30;
            btnClose.addEventListener(MouseEvent.CLICK, onCloseClick);
            content.addChild(btnClose);

        }

        private function onCloseClick(event:MouseEvent):void {
            dispatchEvent(new Event(Event.CLOSE));
        }
    }
}