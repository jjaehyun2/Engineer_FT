package com.playfab.ClientModels
{
    public class UserCustomIdInfo
    {
        public var CustomId:String;

        public function UserCustomIdInfo(data:Object=null)
        {
            if(data == null)
                return;
            CustomId = data.CustomId;

        }
    }
}