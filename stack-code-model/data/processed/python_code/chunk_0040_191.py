package com.playfab.ClientModels
{
    public class FriendInfo
    {
        public var FacebookInfo:UserFacebookInfo;
        public var FriendPlayFabId:String;
        public var GameCenterInfo:UserGameCenterInfo;
        public var Profile:PlayerProfileModel;
        public var PSNInfo:UserPsnInfo;
        public var SteamInfo:UserSteamInfo;
        public var Tags:Vector.<String>;
        public var TitleDisplayName:String;
        public var Username:String;
        public var XboxInfo:UserXboxInfo;

        public function FriendInfo(data:Object=null)
        {
            if(data == null)
                return;
            FacebookInfo = new UserFacebookInfo(data.FacebookInfo);
            FriendPlayFabId = data.FriendPlayFabId;
            GameCenterInfo = new UserGameCenterInfo(data.GameCenterInfo);
            Profile = new PlayerProfileModel(data.Profile);
            PSNInfo = new UserPsnInfo(data.PSNInfo);
            SteamInfo = new UserSteamInfo(data.SteamInfo);
            Tags = data.Tags ? Vector.<String>(data.Tags) : null;
            TitleDisplayName = data.TitleDisplayName;
            Username = data.Username;
            XboxInfo = new UserXboxInfo(data.XboxInfo);

        }
    }
}