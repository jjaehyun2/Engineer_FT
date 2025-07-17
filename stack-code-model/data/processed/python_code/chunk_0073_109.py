/**
 * Created by Akira on 02/03/2015.
 */
package com.bytesfromouterspace.stockbrokers.model {
    import flash.events.IEventDispatcher;

    public interface IHistoryModel extends IEventDispatcher {
        function get history():Vector.<Number>;
        function addToHistory(value:Number):void;
        function dispatchHistoryChange():void;
        function set focus(value:Boolean):void;
        function get name():String;
    }
}