package com.sixfootsoftware.engine {

import flash.utils.getTimer;
import org.flixel.FlxGroup;

    public class SplashScreen extends FlxGroup {

        private var previousLogo:SplashScreenLogo;
        //noinspection JSFieldCanBeLocal
        private var logo:SplashScreenLogo;
        private var timer:Number = -1;
        private var logoTimer:Number = -1;
        private var total:Number = -1;
        private var firstLogo:Boolean = true;

        public function SplashScreen( totalDuration:Number ) {
            timer = getTimer();
            logoTimer = timer;
            total = totalDuration * 1000;
        }

        public function addLogo( logo:SplashScreenLogo ):void {
            previousLogo = LinkedListBuilder.addToLinkedList( previousLogo, logo ) as SplashScreenLogo;
            this.add( logo.getSprite() );
        }

        override public function preUpdate():void {
            if ( firstLogo ) {
                firstLogo  = false;
                logo = LinkedListBuilder.retrieveFirstItem( previousLogo ) as SplashScreenLogo;
                logo.showLogo();
            }
            if ( getTimer() > ( timer + total ) ) {
                this.kill();
            }
            if ( logo.getNext() && getTimer() > ( logoTimer + logo.getDuration() ) ) {
                logo.hideLogo();
                logoTimer += logo.getDuration();
                logo = logo.getNext() as SplashScreenLogo;
                logo.showLogo();
            }
        }
    }
}