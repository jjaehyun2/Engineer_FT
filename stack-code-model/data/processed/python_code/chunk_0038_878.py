package io.decagames.rotmg.shop {
    import com.company.assembleegameclient.parameters.Parameters;
    import com.company.assembleegameclient.ui.tooltip.TextToolTip;
    import com.greensock.TweenMax;
    
    import flash.events.TimerEvent;
    import flash.utils.Timer;
    
    import io.decagames.rotmg.shop.genericBox.GenericBoxTile;
    import io.decagames.rotmg.shop.genericBox.data.GenericBoxInfo;
    import io.decagames.rotmg.shop.mysteryBox.MysteryBoxTile;
    import io.decagames.rotmg.shop.packages.PackageBoxTile;
    import io.decagames.rotmg.supportCampaign.data.SupporterCampaignModel;
    import io.decagames.rotmg.supportCampaign.tab.SupporterShopTabView;
    import io.decagames.rotmg.ui.buttons.BaseButton;
    import io.decagames.rotmg.ui.buttons.SliceScalingButton;
    import io.decagames.rotmg.ui.defaults.DefaultLabelFormat;
    import io.decagames.rotmg.ui.gird.UIGrid;
    import io.decagames.rotmg.ui.labels.UILabel;
    import io.decagames.rotmg.ui.popups.signals.ClosePopupSignal;
    import io.decagames.rotmg.ui.tabs.TabButton;
    import io.decagames.rotmg.ui.tabs.UITab;
    import io.decagames.rotmg.ui.tabs.UITabs;
    import io.decagames.rotmg.ui.texture.TextureParser;
    
    import kabam.rotmg.account.core.signals.OpenMoneyWindowSignal;
    import kabam.rotmg.application.DynamicSettings;
    import kabam.rotmg.core.signals.HideTooltipsSignal;
    import kabam.rotmg.core.signals.ShowTooltipSignal;
    import kabam.rotmg.game.model.GameModel;
    import kabam.rotmg.mysterybox.model.MysteryBoxInfo;
    import kabam.rotmg.mysterybox.services.GetMysteryBoxesTask;
    import kabam.rotmg.mysterybox.services.MysteryBoxModel;
    import kabam.rotmg.packages.model.PackageInfo;
    import kabam.rotmg.packages.services.GetPackagesTask;
    import kabam.rotmg.packages.services.PackageModel;
    import kabam.rotmg.tooltips.HoverTooltipDelegate;
    
    import robotlegs.bender.bundles.mvcs.Mediator;
    
    public class ShopPopupMediator extends Mediator {
        
        
        public function ShopPopupMediator() {
            super();
        }
        
        [Inject]
        public var view: ShopPopupView;
        [Inject]
        public var mysteryBoxModel: MysteryBoxModel;
        [Inject]
        public var packageBoxModel: PackageModel;
        [Inject]
        public var gameModel: GameModel;
        [Inject]
        public var openMoneyWindow: OpenMoneyWindowSignal;
        [Inject]
        public var closePopupSignal: ClosePopupSignal;
        [Inject]
        public var showTooltipSignal: ShowTooltipSignal;
        [Inject]
        public var hideTooltipSignal: HideTooltipsSignal;
        [Inject]
        public var supporterModel: SupporterCampaignModel;
        [Inject]
        public var getMysteryBoxesTask: GetMysteryBoxesTask;
        [Inject]
        public var getPackagesTask: GetPackagesTask;
        private var closeButton: SliceScalingButton;
        private var addButton: SliceScalingButton;
        private var mysteryBoxesGrid: UIGrid;
        private var packageBoxesGrid: UIGrid;
        private var toolTip: TextToolTip = null;
        private var hoverTooltipDelegate: HoverTooltipDelegate;
        private var tabs: UITabs;
        private var packageTab: TabButton;
        private var updateLabel: UILabel;
        private var updateTimer: Timer;
        
        private function get updateInterval(): int {
            if (DynamicSettings.settingExists("MysteryBoxRefresh")) {
                return DynamicSettings.getSettingValue("MysteryBoxRefresh") * 1000;
            }
            return 50 * 60 * 60;
        }
        
        override public function initialize(): void {
            var _local3: * = null;
            var _local1: Boolean = false;
            this.closeButton = new SliceScalingButton(TextureParser.instance.getSliceScalingBitmap("UI", "close_button"));
            this.addButton = new SliceScalingButton(TextureParser.instance.getSliceScalingBitmap("UI", "add_button"));
            this.tabs = new UITabs(590);
            if (this.supporterModel.hasValidData) {
                this.tabs.addTab(new SupporterShopTabView(this.supporterModel.campaignTitle, this.supporterModel.campaignDescription), true);
            }
            this.tabs.addTab(this.createMysteryBoxTab(), !this.supporterModel.hasValidData);
            this.tabs.addTab(this.createPackageBoxTab());
            this.tabs.y = 115;
            this.tabs.x = 3;
            this.view.header.setTitle("Shop", 319, DefaultLabelFormat.defaultPopupTitle);
            this.view.header.showCoins(132).coinsAmount = this.gameModel.player.credits_;
            this.view.header.showFame(132).fameAmount = this.gameModel.player.fame_;
            this.closeButton.clickSignal.addOnce(this.onClose);
            this.view.header.addButton(this.closeButton, "right_button");
            this.addButton.clickSignal.add(this.onAdd);
            this.view.header.addButton(this.addButton, "left_button");
            this.view.addChild(this.tabs);
            this.updateLabel = new UILabel();
            this.updateLabel.defaultTextFormat = DefaultLabelFormat.createTextFormat(12, 0xfff000, "left", true);
            this.updateLabel.text = "Updating shop...";
            this.updateLabel.x = 15;
            this.updateLabel.y = 582;
            this.updateLabel.alpha = 0;
            this.view.addChild(this.updateLabel);
            var _local4: Vector.<PackageInfo> = this.packageBoxModel.getTargetingBoxesForGrid().concat(this.packageBoxModel.getBoxesForGrid());
            var _local2: Date = new Date();
            _local2.setTime(Parameters.data["packages_indicator"]);
            var _local6: int = 0;
            var _local5: * = _local4;
            for each(_local3 in _local4) {
                if (_local3 != null && (!_local3.endTime || _local3.getSecondsToEnd() > 0)) {
                    if (_local3.isNew() && (_local3.startTime.getTime() > _local2.getTime() || !Parameters.data["packages_indicator"])) {
                        _local1 = true;
                    }
                }
            }
            this.packageTab = this.tabs.getTabButtonByLabel("Packages");
            if (this.packageTab) {
                this.packageTab.showIndicator = _local1;
                this.packageTab.clickSignal.add(this.onPackageClick);
            }
            this.gameModel.player.creditsWereChanged.add(this.refreshCoins);
            this.gameModel.player.fameWasChanged.add(this.refreshFame);
            this.toolTip = new TextToolTip(0x363636, 0x9b9b9b, "Buy Gold", "Click to buy more Realm Gold!", 200);
            this.hoverTooltipDelegate = new HoverTooltipDelegate();
            this.hoverTooltipDelegate.setShowToolTipSignal(this.showTooltipSignal);
            this.hoverTooltipDelegate.setHideToolTipsSignal(this.hideTooltipSignal);
            this.hoverTooltipDelegate.setDisplayObject(this.addButton);
            this.hoverTooltipDelegate.tooltip = this.toolTip;
            this.updateTimer = new Timer(this.updateInterval);
            this.updateTimer.addEventListener("timer", this.updateShop);
            this.tabs.tabSelectedSignal.add(this.onTabChange);
            if (!this.supporterModel.hasValidData) {
                this.updateShop(null);
            }
        }
        
        override public function destroy(): void {
            this.updateTimer.stop();
            this.updateTimer.removeEventListener("timer", this.tryUpdateMysteryBoxes);
            this.mysteryBoxModel.updateSignal.remove(this.onBoxUpdate);
            this.packageBoxModel.updateSignal.remove(this.onPackageUpdate);
            this.view.dispose();
            this.closeButton.dispose();
            this.addButton.dispose();
            this.gameModel.player.creditsWereChanged.remove(this.refreshCoins);
            this.gameModel.player.fameWasChanged.remove(this.refreshFame);
            this.tabs.dispose();
            this.mysteryBoxesGrid.dispose();
            this.packageBoxesGrid.dispose();
            this.toolTip = null;
            this.hoverTooltipDelegate.removeDisplayObject();
            this.hoverTooltipDelegate = null;
            if (this.packageTab) {
                this.packageTab.clickSignal.remove(this.onPackageClick);
            }
        }
        
        private function createPackageBoxTab(): UITab {
            var _local1: * = null;
            _local1 = new UITab("Packages");
            this.packageBoxesGrid = new UIGrid(550, 2, 6, 384, 3, _local1);
            this.packageBoxesGrid.x = 10;
            this.packageBoxesGrid.decorBitmap = "tabs_tile_decor";
            this.updatePackages();
            _local1.addContent(this.packageBoxesGrid);
            return _local1;
        }
        
        private function createMysteryBoxTab(): UITab {
            var _local1: UITab = new UITab("Mystery Boxes", true);
            this.mysteryBoxesGrid = new UIGrid(550, 3, 6, 384, 3, _local1);
            this.mysteryBoxesGrid.decorBitmap = "tabs_tile_decor";
            this.mysteryBoxesGrid.x = 10;
            this.updateMysteryBoxes();
            _local1.addContent(this.mysteryBoxesGrid);
            return _local1;
        }
        
        private function updateMysteryBoxes(): void {
            var _local2: * = null;
            var _local1: * = null;
            this.mysteryBoxesGrid.clearGrid();
            var _local3: Vector.<MysteryBoxInfo> = this.mysteryBoxModel.getBoxesForGrid();
            var _local5: int = 0;
            var _local4: * = _local3;
            for each(_local2 in _local3) {
                if (_local2 != null && (!_local2.endTime || _local2.getSecondsToEnd() > 0)) {
                    _local1 = this.createBoxTile(_local2, MysteryBoxTile);
                    _local1.selfRemoveSignal.add(this.updateMysteryBoxes);
                    this.mysteryBoxesGrid.addGridElement(_local1);
                }
            }
        }
        
        private function updatePackages(): void {
            var _local2: * = null;
            var _local1: * = null;
            this.packageBoxesGrid.clearGrid();
            var _local3: Vector.<PackageInfo> = this.packageBoxModel.getTargetingBoxesForGrid().concat(this.packageBoxModel.getBoxesForGrid());
            var _local5: int = 0;
            var _local4: * = _local3;
            for each(_local2 in _local3) {
                if (_local2 != null && (!_local2.endTime || _local2.getSecondsToEnd() > 0)) {
                    _local1 = this.createBoxTile(_local2, PackageBoxTile);
                    _local1.selfRemoveSignal.add(this.updatePackages);
                    this.packageBoxesGrid.addGridElement(_local1);
                }
            }
        }
        
        private function createBoxTile(_arg_1: GenericBoxInfo, _arg_2: Class): GenericBoxTile {
            return new _arg_2(_arg_1);
        }
        
        private function onTabChange(_arg_1: String): void {
            if (this.updateTimer) {
                this.updateTimer.reset();
            }
            if (_arg_1 != "Campaign") {
                this.updateShop(null);
            } else {
                TweenMax.killTweensOf(this.updateLabel);
                this.updateLabel.alpha = 0;
            }
        }
        
        private function tryUpdateMysteryBoxes(): void {
            TweenMax.killTweensOf(this.updateLabel);
            this.updateLabel.alpha = 1;
            this.mysteryBoxModel.updateSignal.add(this.onBoxUpdate);
            this.getMysteryBoxesTask.start();
            TweenMax.to(this.updateLabel, 0.6, {
                "alpha": 0,
                "yoyo": true,
                "repeat": -1
            });
        }
        
        private function tryUpdatePackages(): void {
            TweenMax.killTweensOf(this.updateLabel);
            this.updateLabel.alpha = 1;
            this.packageBoxModel.updateSignal.add(this.onPackageUpdate);
            this.getPackagesTask.start();
            TweenMax.to(this.updateLabel, 0.6, {
                "alpha": 0,
                "yoyo": true,
                "repeat": -1
            });
        }
        
        private function onBoxUpdate(): void {
            this.mysteryBoxModel.updateSignal.remove(this.onBoxUpdate);
            this.updateMysteryBoxes();
            TweenMax.killTweensOf(this.updateLabel);
            this.updateLabel.alpha = 0;
        }
        
        private function onPackageUpdate(): void {
            this.packageBoxModel.updateSignal.remove(this.onPackageUpdate);
            this.updatePackages();
            TweenMax.killTweensOf(this.updateLabel);
            this.updateLabel.alpha = 0;
        }
        
        private function onPackageClick(_arg_1: BaseButton): void {
            if (TabButton(_arg_1).hasIndicator) {
                Parameters.data["packages_indicator"] = new Date().getTime();
                TabButton(_arg_1).showIndicator = false;
            }
        }
        
        private function refreshCoins(): void {
            this.view.header.showCoins(132).coinsAmount = this.gameModel.player.credits_;
        }
        
        private function refreshFame(): void {
            this.view.header.showFame(132).fameAmount = this.gameModel.player.fame_;
        }
        
        private function onAdd(_arg_1: BaseButton): void {
            this.openMoneyWindow.dispatch();
        }
        
        private function onClose(_arg_1: BaseButton): void {
            this.closePopupSignal.dispatch(this.view);
        }
        
        private function updateShop(_arg_1: TimerEvent): void {
            var _local2: * = this.tabs.currentTabLabel;
            switch (_local2) {
            case "Mystery Boxes":
                this.tryUpdateMysteryBoxes();
                return;
            case "Packages":
                this.tryUpdatePackages();
                return;
            default:
                return;
            }
        }
    }
}