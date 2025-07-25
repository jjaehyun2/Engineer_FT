package com.playfab.ClientModels
{
    public class OpenTradeRequest
    {
        public var AllowedPlayerIds:Vector.<String>;
        public var OfferedInventoryInstanceIds:Vector.<String>;
        public var RequestedCatalogItemIds:Vector.<String>;

        public function OpenTradeRequest(data:Object=null)
        {
            if(data == null)
                return;
            AllowedPlayerIds = data.AllowedPlayerIds ? Vector.<String>(data.AllowedPlayerIds) : null;
            OfferedInventoryInstanceIds = data.OfferedInventoryInstanceIds ? Vector.<String>(data.OfferedInventoryInstanceIds) : null;
            RequestedCatalogItemIds = data.RequestedCatalogItemIds ? Vector.<String>(data.RequestedCatalogItemIds) : null;

        }
    }
}