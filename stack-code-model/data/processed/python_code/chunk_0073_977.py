package com.company.assembleegameclient.account.ui {
   import com.company.assembleegameclient.account.ui.components.BackgroundBox;
   import com.company.assembleegameclient.account.ui.components.Selectable;
   import com.company.assembleegameclient.util.TextureRedrawer;
   import com.company.assembleegameclient.util.offer.Offer;
   import com.company.util.AssetLibrary;
   import com.company.util.BitmapUtil;
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.Sprite;
   import flash.events.MouseEvent;
   import flash.filters.DropShadowFilter;
   import kabam.rotmg.account.core.model.MoneyConfig;
   import kabam.rotmg.text.view.TextFieldDisplayConcrete;
   import kabam.rotmg.text.view.stringBuilder.LineBuilder;
   import kabam.rotmg.ui.view.SignalWaiter;
   import kabam.rotmg.util.components.RadioButton;
   
   public class OfferRadioButton extends Sprite implements Selectable {
      
      private static const SELECTED_COLOR:int = 7829367;
      
      private static const OVER_COLOR:int = 5987163;
      
      private static const DEFAULT_COLOR:int = 4539717;
       
      
      private const waiter:SignalWaiter = new SignalWaiter();
      
      public var offer:Offer;
      
      private var config:MoneyConfig;
      
      private var background:BackgroundBox;
      
      private var container:Sprite;
      
      private var toggle:RadioButton;
      
      private var coinBitmap:BitmapData;
      
      private var goldText:TextFieldDisplayConcrete;
      
      private var costText:TextFieldDisplayConcrete;
      
      private var bonusText:TextFieldDisplayConcrete;
      
      private var taglineText:TextFieldDisplayConcrete;
      
      private var isSelected:Boolean;
      
      private var isOver:Boolean;
      
      public function OfferRadioButton(param1:Offer, param2:MoneyConfig) {
         super();
         this.offer = param1;
         this.config = param2;
         this.makeBackgroundBox();
         this.makeContainer();
         this.makeSelectToggle();
         this.makeCoinImage();
         this.makeGoldText();
         this.makeCostText();
         this.makeBonusText();
         this.makeTaglineTextIfApplicable();
         addEventListener("mouseOver",this.onMouseOver);
         addEventListener("rollOut",this.onRollOut);
         this.waiter.complete.add(this.alignUI);
      }
      
      public function getValue() : String {
         return this.offer.realmGold_.toString();
      }
      
      public function setOver(param1:Boolean) : void {
         this.isOver = param1;
         this.updateBackgroundColor();
      }
      
      public function setSelected(param1:Boolean) : void {
         this.isSelected = param1;
         this.toggle.setSelected(param1);
         this.updateBackgroundColor();
      }
      
      public function showBonus(param1:Boolean) : void {
         if(this.bonusText) {
            this.bonusText.visible = param1;
         }
      }
      
      private function makeBackgroundBox() : void {
         this.background = new BackgroundBox();
         this.background.setSize(520,36);
         this.updateBackgroundColor();
         addChild(this.background);
      }
      
      private function makeContainer() : void {
         this.container = new Sprite();
         this.container.y = 3;
         this.container.x = 3;
         addChild(this.container);
      }
      
      private function makeSelectToggle() : void {
         this.toggle = new RadioButton();
         this.toggle.x = 3;
         this.container.addChild(this.toggle);
      }
      
      private function makeCoinImage() : void {
         this.coinBitmap = AssetLibrary.getImageFromSet("lofiObj3",225);
         this.coinBitmap = TextureRedrawer.redraw(this.coinBitmap,50,true,0,false);
         this.coinBitmap = BitmapUtil.cropToBitmapData(this.coinBitmap,8,8,this.coinBitmap.width - 16,this.coinBitmap.height - 16);
         var _loc1_:Bitmap = new Bitmap(this.coinBitmap);
         _loc1_.x = this.toggle.x + 35;
         this.container.addChild(_loc1_);
      }
      
      private function makeGoldText() : void {
         this.goldText = new TextFieldDisplayConcrete().setSize(18).setColor(16777215).setBold(true);
         this.goldText.setStringBuilder(new LineBuilder().setParams("Payments.GoldAmount",{"amount":this.offer.realmGold_}));
         this.goldText.filters = [new DropShadowFilter(0,0,0)];
         this.waiter.push(this.goldText.textChanged);
         this.container.addChild(this.goldText);
      }
      
      private function makeCostText() : void {
         this.costText = new TextFieldDisplayConcrete().setSize(18).setColor(16777215).setBold(true);
         this.costText.setStringBuilder(this.config.parseOfferPrice(this.offer));
         this.costText.filters = [new DropShadowFilter(0,0,0)];
         this.waiter.push(this.costText.textChanged);
         this.container.addChild(this.costText);
      }
      
      private function makeBonusText() : void {
         if(!this.hasBonus()) {
            return;
         }
         this.bonusText = new TextFieldDisplayConcrete().setSize(18).setColor(16777215).setBold(true);
         this.bonusText.setStringBuilder(new LineBuilder().setParams("Payments.GoldBonus",{"percent":this.offer.bonus}));
         this.bonusText.filters = [new DropShadowFilter(0,0,0)];
         this.waiter.push(this.bonusText.textChanged);
         this.container.addChild(this.bonusText);
      }
      
      private function makeTaglineTextIfApplicable() : void {
         if(this.hasTagline()) {
            this.makeTaglineText();
         }
      }
      
      private function makeTaglineText() : void {
         this.taglineText = new TextFieldDisplayConcrete().setSize(18).setColor(8891485);
         this.taglineText.setStringBuilder(new LineBuilder().setParams(this.offer.tagline));
         this.taglineText.filters = [new DropShadowFilter(0,0,0)];
         this.waiter.push(this.taglineText.textChanged);
         this.container.addChild(this.taglineText);
      }
      
      private function hasTagline() : Boolean {
         return this.offer.tagline != null;
      }
      
      private function hasBonus() : Boolean {
         return this.offer != null && this.offer.bonus != 0;
      }
      
      private function alignUI() : void {
         this.goldText.x = this.toggle.x + 70;
         this.goldText.y = this.coinBitmap.height * 0.5 - this.goldText.height / 2;
         this.costText.x = 200;
         this.costText.y = this.coinBitmap.height / 2 - this.costText.height / 2;
         if(this.hasBonus() && this.bonusText != null) {
            this.bonusText.x = 280;
            this.bonusText.y = this.coinBitmap.height / 2 - this.bonusText.height / 2;
         }
         if(this.hasTagline() && this.taglineText != null) {
            this.taglineText.x = 400;
            this.taglineText.y = this.coinBitmap.height / 2 - this.taglineText.height / 2;
         }
      }
      
      private function updateBackgroundColor() : void {
         var _loc1_:int = !!this.isSelected?7829367:Number(!!this.isOver?5987163:4539717);
         this.background.setColor(_loc1_);
      }
      
      private function onMouseOver(param1:MouseEvent) : void {
         this.setOver(true);
      }
      
      private function onRollOut(param1:MouseEvent) : void {
         this.setOver(false);
      }
   }
}