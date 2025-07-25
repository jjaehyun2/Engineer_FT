package kabam.rotmg.core.model {
import com.company.assembleegameclient.appengine.SavedCharacter;
import com.company.assembleegameclient.appengine.SavedCharactersList;
import com.company.assembleegameclient.appengine.SavedNewsItem;
import com.company.assembleegameclient.parameters.Parameters;

import kabam.rotmg.account.core.Account;
import kabam.rotmg.servers.api.LatLong;

import org.osflash.signals.Signal;

public class PlayerModel {

    public static const CHARACTER_SLOT_PRICES:Array = [10 * 60, 800, 1000];


    public const creditsChanged:Signal = new Signal(int);

    public const fameChanged:Signal = new Signal(int);

    public const tokensChanged:Signal = new Signal(int);

    public var lockList:Vector.<String>;

    public var ignoreList:Vector.<String>;

    public function PlayerModel() {
        lockList = new Vector.<String>(0);
        ignoreList = new Vector.<String>(0);
        super();
        this.isInvalidated = true;
    }
    public var charList:SavedCharactersList;
    public var isInvalidated:Boolean;
    [Inject]
    public var account:Account;
    private var isAgeVerified:Boolean;

    private var _currentCharId:int;

    public function get currentCharId():int {
        return this._currentCharId;
    }

    public function set currentCharId(_arg_1:int):void {
        this._currentCharId = _arg_1;
    }

    private var _isLogOutLogIn:Boolean;

    public function get isLogOutLogIn():Boolean {
        return this._isLogOutLogIn;
    }

    public function set isLogOutLogIn(_arg_1:Boolean):void {
        this._isLogOutLogIn = _arg_1;
    }

    private var _hasShownUnitySignUp:Boolean;

    public function get hasShownUnitySignUp():Boolean {
        return this._hasShownUnitySignUp;
    }

    public function set hasShownUnitySignUp(_arg_1:Boolean):void {
        this._hasShownUnitySignUp = _arg_1;
    }

    private var _isNameChosen:Boolean;

    public function get isNameChosen():Boolean {
        return this._isNameChosen;
    }

    public function set isNameChosen(_arg_1:Boolean):void {
        this._isNameChosen = _arg_1;
    }

    public function getHasPlayerDied():Boolean {
        return this.charList.hasPlayerDied;
    }

    public function setHasPlayerDied(_arg_1:Boolean):void {
        this.charList.hasPlayerDied = _arg_1;
    }

    public function getIsAgeVerified():Boolean {
        return this.isAgeVerified || this.charList.isAgeVerified;
    }

    public function setIsAgeVerified(_arg_1:Boolean):void {
        this.isAgeVerified = true;
    }

    public function isNewPlayer():Boolean {
        return Parameters.data.needsTutorial && this.charList.nextCharId_ == 1;
    }

    public function getMaxCharacters():int {
        return this.charList.maxNumChars_;
    }

    public function setMaxCharacters(_arg_1:int):void {
        this.charList.maxNumChars_ = _arg_1;
    }

    public function getCredits():int {
        return this.charList.credits_;
    }

    public function getSalesForceData():String {
        return this.charList.salesForceData_;
    }

    public function changeCredits(_arg_1:int):void {
        this.charList.credits_ = this.charList.credits_ + _arg_1;
        this.creditsChanged.dispatch(this.charList.credits_);
    }

    public function setCredits(_arg_1:int):void {
        if (this.charList.credits_ != _arg_1) {
            this.charList.credits_ = _arg_1;
            this.creditsChanged.dispatch(_arg_1);
        }
    }

    public function getFame():int {
        return this.charList.fame_;
    }

    public function setFame(_arg_1:int):void {
        if (this.charList.fame_ != _arg_1) {
            this.charList.fame_ = _arg_1;
            this.fameChanged.dispatch(_arg_1);
        }
    }

    public function getTokens():int {
        return this.charList.tokens_;
    }

    public function setTokens(_arg_1:int):void {
        if (this.charList.tokens_ != _arg_1) {
            this.charList.tokens_ = _arg_1;
            this.tokensChanged.dispatch(_arg_1);
        }
    }

    public function getCharacterCount():int {
        return this.charList.numChars_;
    }

    public function getCharById(_arg_1:int):SavedCharacter {
        return this.charList.getCharById(_arg_1);
    }

    public function deleteCharacter(_arg_1:int):void {
        var _local2:SavedCharacter = this.charList.getCharById(_arg_1);
        var _local3:int = this.charList.savedChars_.indexOf(_local2);
        if (_local3 != -1) {
            this.charList.savedChars_.splice(_local3, 1);
            this.charList.numChars_--;
        }
    }

    public function getAccountId():String {
        return this.charList.accountId_;
    }

    public function hasAccount():Boolean {
        return this.charList.accountId_ != "";
    }

    public function getNumStars():int {
        return this.charList.numStars_;
    }

    public function getGuildName():String {
        return this.charList.guildName_;
    }

    public function getGuildRank():int {
        return this.charList.guildRank_;
    }

    public function getNextCharSlotPrice():int {
        var _local1:int = Math.min(CHARACTER_SLOT_PRICES.length - 1, this.charList.maxNumChars_ - 1);
        return CHARACTER_SLOT_PRICES[_local1];
    }

    public function getTotalFame():int {
        return this.charList.totalFame_;
    }

    public function getNextCharId():int {
        return this.charList.nextCharId_;
    }

    public function getCharacterById(_arg_1:int):SavedCharacter {
        for each(var _local2:SavedCharacter in this.charList.savedChars_) {
            if (_local2.charId() == _arg_1) {
                return _local2;
            }
        }
        return null;
    }

    public function getCharacterByIndex(_arg_1:int):SavedCharacter {
        return this.charList.savedChars_[_arg_1];
    }

    public function isAdmin():Boolean {
        return this.charList.isAdmin_;
    }

    public function mapEditor():Boolean {
        return this.charList.canMapEdit_;
    }

    public function getNews():Vector.<SavedNewsItem> {
        return this.charList.news_;
    }

    public function getMyPos():LatLong {
        return this.charList.myPos_;
    }

    public function setClassAvailability(_arg_1:int, _arg_2:String):void {
        this.charList.classAvailability[_arg_1] = _arg_2;
    }

    public function getName():String {
        return this.charList.name_;
    }

    public function getConverted():Boolean {
        return this.charList.converted_;
    }

    public function setName(_arg_1:String):void {
        this.charList.name_ = _arg_1;
    }

    public function getNewUnlocks(_arg_1:int, _arg_2:int):Array {
        return this.charList.newUnlocks(_arg_1, _arg_2);
    }

    public function hasAvailableCharSlot():Boolean {
        return this.charList.hasAvailableCharSlot();
    }

    public function getAvailableCharSlots():int {
        return this.charList.availableCharSlots();
    }

    public function getSavedCharacters():Vector.<SavedCharacter> {
        return this.charList.savedChars_;
    }

    public function getCharStats():Object {
        return this.charList.charStats_;
    }

    public function isClassAvailability(_arg_1:String, _arg_2:String):Boolean {
        var _local3:String = this.charList.classAvailability[_arg_1];
        return _local3 == _arg_2;
    }

    public function isLevelRequirementsMet(_arg_1:int):Boolean {
        return this.charList.levelRequirementsMet(_arg_1);
    }

    public function getBestFame(_arg_1:int):int {
        return this.charList.bestFame(_arg_1);
    }

    public function getBestLevel(_arg_1:int):int {
        return this.charList.bestLevel(_arg_1);
    }

    public function getBestCharFame():int {
        return this.charList.bestCharFame_;
    }

    public function isNewToEditing():Boolean {
        return this.charList && !this.charList.isFirstTimeLogin();
    }

    public function getVaults():Vector.<Vector.<int>> {
        return this.charList.vaultItems;
    }

    public function name():void {
    }

    public function setCharacterList(_arg_1:SavedCharactersList):void {
        if (this.charList) {
            charList.dispose();
        }
        this.charList = _arg_1;
        this._isNameChosen = this.charList.nameChosen_;
    }
}
}