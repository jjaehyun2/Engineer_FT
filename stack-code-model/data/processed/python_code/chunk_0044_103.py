package com.playfab.GroupsModels
{
    public class RemoveGroupInvitationRequest
    {
        public var Entity:EntityKey;
        public var Group:EntityKey;

        public function RemoveGroupInvitationRequest(data:Object=null)
        {
            if(data == null)
                return;
            Entity = new EntityKey(data.Entity);
            Group = new EntityKey(data.Group);

        }
    }
}