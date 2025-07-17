/**
 * Created by Alexander on 7/9/2015.
 */
package com.github.mortido.sqcity.events
{
    import com.github.mortido.sqcity.configuration.Config;
    import com.github.mortido.sqcity.models.Building;
    import com.github.mortido.sqcity.models.GameResources;

    import flash.events.Event;

    public class LoginEvent extends Event
    {
        public function LoginEvent(buildings:Vector.<Building>,
                                   username:String,
                                   resources:GameResources,
                                   config:Config,
                                   type:String,
                                   bubbles:Boolean = false,
                                   cancelable:Boolean = false)
        {
            super(type, bubbles, cancelable);
            _buildings = buildings;
            _username = username;
            _resources = resources;
            _config = config;
        }
        private var _buildings:Vector.<Building>;
        private var _username:String;
        private var _resources:GameResources;
        private var _config:Config;

        public function get buildings():Vector.<Building>
        {
            return _buildings;
        }

        public function get config():Config
        {
            return _config;
        }

        public function get username():String
        {
            return _username;
        }

        public function get resources():GameResources
        {
            return _resources;
        }
    }
}