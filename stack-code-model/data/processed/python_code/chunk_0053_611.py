/**
 * Created by Akira on 05/03/2015.
 */
package com.bytesfromouterspace.stockbrokers.model {
    import com.bytesfromouterspace.stockbrokers.ui.StringUtils;

    import flash.utils.Dictionary;

    public class GameStatsSessionModel {

        public var data:Object;

        public function GameStatsSessionModel(jsonData:String = null) {
            data = {
                stamp: new Date().toString(),
                user: "n/a",
                ip: "n/a",
                score: 0
            };
            if(jsonData != null) {
                data = JSON.parse(jsonData).data;
            }
        }

        public function agregateStats(groupName:String, stats:Dictionary):void {
            var key:String;
            var prefix:String = groupName + "_";
            if(stats) {
                for(key in stats) {
                    data[prefix + key] = stats[key];
                }
            }
        }

        public function statValueAsInt(key:String):String {
            if((key != null) && (data != null) && data.hasOwnProperty(key)) {
                return Number(data[key]).toFixed(0);
            }
            return "N/A";
        }

        public function statValue(key:String):Number {
            if((key != null) && (data != null) && data.hasOwnProperty(key)) {
                return Number(data[key]);
            }
            return 0;
        }

        public function statValueAsCurrency(key:String):String {
            if((key != null) && (data != null) && data.hasOwnProperty(key)) {
                var value:Number = data[key];
                if(!isNaN(value)) {
                    return StringUtils.formatCurrency(data[key]);
                } else {
                    return "---";
                }
            }
            return "N/A";
        }

    }
}