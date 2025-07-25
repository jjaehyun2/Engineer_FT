/*******************************************************************************
 * PushButton Engine
 * Copyright (C) 2009 PushButton Labs, LLC
 * For more information see http://www.pushbuttonengine.com
 * 
 * This file is licensed under the terms of the MIT license, which is included
 * in the License.html file at the root directory of this SDK.
 ******************************************************************************/
package com.pblabs.rendering2D.spritesheet
{
    import com.pblabs.engine.entity.EntityComponent;
    import com.pblabs.rendering2D.modifier.Modifier;
    
    import flash.display.BitmapData;
    import flash.geom.Point;
    
    /**
     * An abstract class to allow access to a set of sprites.
     * This needs to be inherited to be of any use.
     * @see SpriteSheetComponent
     * @see SWFSpriteSheetComponent
     */
    public class SpriteContainerComponent extends EntityComponent
    {
		/**
		 * Array with BitmapData modifiers that will be pre-rendered 
		 */
		public function get modifiers():Array
		{
			return _modifiers;
		}
		
		public function set modifiers(value:Array):void
		{
			_modifiers = value;
			buildFrames();
		}
       /**
         * Subclasses must override this method and return an
         * array of BitmapData objects.
         */
        protected function getSourceFrames():Array
        {
            throw new Error("Not Implemented");
        }
        
        /**
         * Deletes the frames so this class can be re-used with a new set of frames.
         */
        protected function deleteFrames():void
        {
            frames = null;
        }
        
        /**
         * True if the frames associated with this sprite container have been loaded.
         */
        public function get isLoaded():Boolean
        {
            return frames != null;
        }
        
        /**
         * Specifies an offset so the sprite is centered correctly. If it is not
         * set, the sprite is centered.
         */
        public function get center():Point
        {
            if(!_center)
                return new Point();
            
            return _center;
        }
		
        public function set center(v:Point):void
        {
            _center = v;
            _defaultCenter = false;
        }

		/**
		 * Indicates that the spriteSheet has a centered alignment.
		 */
		public function get centered():Boolean
		{
			return _defaultCenter;
		}
		
        /**
         * The number of directions per frame.
         */
        [EditorData(defaultValue="1")]
        public var directionsPerFrame:Number = 1;
        
        /**
         * The number of degrees separating each direction.
         */
        public function get degreesPerDirection():Number
        {
            return 360 / directionsPerFrame;
        }
        
        /**
         * The total number of frames the sprite container has. This counts each
         * direction separately.
         */
        public function get rawFrameCount():int
        {
            if (!frames)
                buildFrames();
            
            return frames ? frames.length : 0;
        }
        
        /**
         * The number of frames the sprite container has. This counts each set of
         * directions as one frame.
         */
        public function get frameCount():int
        {
            return rawFrameCount / directionsPerFrame;
        }

		public function set frameCount(value:int):void
		{
			if (!frames)
			{
				// frames where not loaded yet so cap them as soon as 
				// the divider provides the frames
				frameCountCap = value;
			}
			else
			{
				// frame where loaded so splice the array
				if (frames.length>value)
					frames.splice(value,frames.length-value);
			}
		}
		
        /**
         * Gets the bitmap data for a frame at the specified index.
         * 
         * @param index The index of the frame to retrieve.
         * @param direction The direction of the frame to retrieve in degrees. This
         *                  can be ignored if there is only 1 direction per frame.
         * 
         * @return The bitmap data for the specified frame, or null if it doesn't exist.
         */
        public function getFrame(index:int, direction:Number=0.0):BitmapData
        {
            if(!isLoaded)
                return null;
            
            // Make sure direction is in 0..360.
            while (direction < 0)
                direction += 360;
            
            while (direction > 360)
                direction -= 360;
            
            // Easy case if we only have one direction per frame.
            if (directionsPerFrame == 1)
                return getRawFrame(index);
            
            // Otherwise we have to do a search.
            
            // Make sure we have data to fulfill our requests from.
            if (frameNotes == null)
                generateFrameNotes();
            
            // Look for best match.
            var bestMatchIndex:int = -1;
            var bestMatchDirectionDistance:Number = Number.POSITIVE_INFINITY;
            
            for (var i:int = 0; i < frameNotes.length; i++)
            {
                var note:FrameNote = frameNotes[i];
                if (note.Frame != index)
                    continue;
                
					 var distance:Number = Math.min(Math.abs(note.Direction - direction), note.Direction + 360 - direction);
                if (distance < bestMatchDirectionDistance)
                {
                    // This one is better on both frame and heading.
                    bestMatchDirectionDistance = distance;
                    bestMatchIndex = note.RawFrame;
                }
            }
            
            // Return the bitmap.
            if (bestMatchIndex >= 0)
                return getRawFrame(bestMatchIndex);
            
            return null;
        }
        
        protected function buildFrames():void
        {
            frames = getSourceFrames();
            
            // not loaded, can't do anything yet
            if (frames == null)
                return;
            
            if (frames.length == 0)
                throw new Error("No frames loaded");
            					
			// BitmapData modification implementation
			if (frames!=null && modifiers.length>0)
			{
				// loop all frames
				for (var f:int = 0; f<frames.length; f++)
				{
					// get frame
					var frame:BitmapData = (frames[f] as BitmapData).clone();						
					// apply BitmapData modifiers
					for (var m:int = 0; m<modifiers.length; m++)
						frame = (modifiers[m] as Modifier).modify(frame,f, frames.length);	
					// assign modified frame
					frames[f] = frame;
				}
								
			}

			if (frameCountCap>0)
			{
				// this frames array has to be capped because the frameCount was set manually to override	
				frames.splice(frameCountCap,frames.length-frameCountCap);
			}
			
			if (_defaultCenter)
				_center = new Point(BitmapData(frames[0]).width * 0.5, BitmapData(frames[0]).height * 0.5);
			
        }
        
        /**
         * Gets the frame at the specified index. This does not take direction into
         * account.
         */
        protected function getRawFrame(index:int):BitmapData
        {
            if (frames == null)
                buildFrames();
            
            if (frames == null)
                return null;
            
            if ((index < 0) || (index >= rawFrameCount))
                return null;
            
            return frames[index];  
        }
        
        private function generateFrameNotes():void
        {
            frameNotes = new Array();
            
            var totalStates:int = frameCount / degreesPerDirection;
            
            for (var direction:int = 0; direction < directionsPerFrame; direction++)
            {
                for (var frame:int = 0; frame < frameCount; frame++)
                {
                    var note:FrameNote = new FrameNote();
                    note.Frame = frame;
                    note.Direction = direction * degreesPerDirection;
                    note.RawFrame = (direction * frameCount) + frame;
                    
                    frameNotes.push(note);
                }
            }
        }
        
        private var frameNotes:Array;
        protected var frames:Array = null;
		private var _modifiers:Array = new Array();
        private var _center:Point = new Point(0, 0);
        private var _defaultCenter:Boolean = true;
		private var frameCountCap:int = 0;
    }
}

final class FrameNote
{
    public var Frame:int;
    public var Direction:Number;
    public var RawFrame:int;
}