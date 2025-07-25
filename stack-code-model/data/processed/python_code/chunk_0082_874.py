package com.playfab.ServerModels
{
    public class GetUserInventoryResult
    {
        public var Inventory:Vector.<ItemInstance>;
        public var PlayFabId:String;
        public var VirtualCurrency:Object;
        public var VirtualCurrencyRechargeTimes:Object;

        public function GetUserInventoryResult(data:Object=null)
        {
            if(data == null)
                return;
            if(data.Inventory) { Inventory = new Vector.<ItemInstance>(); for(var Inventory_iter:int = 0; Inventory_iter < data.Inventory.length; Inventory_iter++) { Inventory[Inventory_iter] = new ItemInstance(data.Inventory[Inventory_iter]); }}
            PlayFabId = data.PlayFabId;
            VirtualCurrency = data.VirtualCurrency;
            if(data.VirtualCurrencyRechargeTimes) { VirtualCurrencyRechargeTimes = {}; for(var VirtualCurrencyRechargeTimes_iter:String in data.VirtualCurrencyRechargeTimes) { VirtualCurrencyRechargeTimes[VirtualCurrencyRechargeTimes_iter] = new VirtualCurrencyRechargeTime(data.VirtualCurrencyRechargeTimes[VirtualCurrencyRechargeTimes_iter]); }}

        }
    }
}