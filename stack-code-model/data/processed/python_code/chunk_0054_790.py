package com.playfab.GroupsModels
{
    import com.playfab.PlayFabUtil;

    public class GroupInvitation
    {
        public var Expires:Date;
        public var Group:EntityKey;
        public var InvitedByEntity:EntityWithLineage;
        public var InvitedEntity:EntityWithLineage;
        public var RoleId:String;

        public function GroupInvitation(data:Object=null)
        {
            if(data == null)
                return;
            Expires = PlayFabUtil.parseDate(data.Expires);
            Group = new EntityKey(data.Group);
            InvitedByEntity = new EntityWithLineage(data.InvitedByEntity);
            InvitedEntity = new EntityWithLineage(data.InvitedEntity);
            RoleId = data.RoleId;

        }
    }
}