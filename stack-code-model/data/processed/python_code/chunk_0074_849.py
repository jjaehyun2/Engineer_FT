package com.playfab.ClientModels
{
    public class LoginWithAppleRequest
    {
        public var CreateAccount:*;
        public var EncryptedRequest:String;
        public var IdentityToken:String;
        public var InfoRequestParameters:GetPlayerCombinedInfoRequestParams;
        public var PlayerSecret:String;
        public var TitleId:String;

        public function LoginWithAppleRequest(data:Object=null)
        {
            if(data == null)
                return;
            CreateAccount = data.CreateAccount;
            EncryptedRequest = data.EncryptedRequest;
            IdentityToken = data.IdentityToken;
            InfoRequestParameters = new GetPlayerCombinedInfoRequestParams(data.InfoRequestParameters);
            PlayerSecret = data.PlayerSecret;
            TitleId = data.TitleId;

        }
    }
}