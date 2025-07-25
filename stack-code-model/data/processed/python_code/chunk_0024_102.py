package io.decagames.rotmg.social.model {
    import com.company.assembleegameclient.objects.Player;
    
    public class GuildMemberVO {
        
        
        public function GuildMemberVO() {
            super();
        }
        
        private var _name: String;
        
        public function get name(): String {
            return this._name;
        }
        
        public function set name(_arg_1: String): void {
            this._name = _arg_1;
        }
        
        private var _rank: int;
        
        public function get rank(): int {
            return this._rank;
        }
        
        public function set rank(_arg_1: int): void {
            this._rank = _arg_1;
        }
        
        private var _fame: int;
        
        public function get fame(): int {
            return this._fame;
        }
        
        public function set fame(_arg_1: int): void {
            this._fame = _arg_1;
        }
        
        private var _player: Player;
        
        public function get player(): Player {
            return this._player;
        }
        
        public function set player(_arg_1: Player): void {
            this._player = _arg_1;
        }
        
        private var _serverName: String;
        
        public function get serverName(): String {
            return this._serverName;
        }
        
        public function set serverName(_arg_1: String): void {
            this._serverName = _arg_1;
        }
        
        private var _serverAddress: String;
        
        public function get serverAddress(): String {
            return this._serverAddress;
        }
        
        public function set serverAddress(_arg_1: String): void {
            this._serverAddress = _arg_1;
        }
        
        private var _isOnline: Boolean;
        
        public function get isOnline(): Boolean {
            return this._isOnline;
        }
        
        public function set isOnline(_arg_1: Boolean): void {
            this._isOnline = _arg_1;
        }
        
        private var _isMe: Boolean;
        
        public function get isMe(): Boolean {
            return this._isMe;
        }
        
        public function set isMe(_arg_1: Boolean): void {
            this._isMe = _arg_1;
        }
        
        private var _lastLogin: Number;
        
        public function get lastLogin(): Number {
            return this._lastLogin;
        }
        
        public function set lastLogin(_arg_1: Number): void {
            this._lastLogin = _arg_1;
        }
    }
}