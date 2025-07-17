/*
 *      _________  __      __
 *    _/        / / /____ / /________ ____ ____  ___
 *   _/        / / __/ -_) __/ __/ _ `/ _ `/ _ \/ _ \
 *  _/________/  \__/\__/\__/_/  \_,_/\_, /\___/_//_/
 *                                   /___/
 * 
 * Tetragon : Game Engine for multi-platform ActionScript projects.
 * http://www.tetragonengine.com/ - Copyright (C) 2012 Sascha Balkau
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
package tetragon.util.obj
{
	import tetragon.debug.Log;
	import tetragon.util.reflection.describeTypeProperties;

	import flash.display.DisplayObject;
	import flash.geom.Rectangle;


	/**
	 * Creates a clone of the DisplayObject passed, similar to duplicateMovieClip in AVM1.
	 * 
	 * UNTESTED!
	 * 
	 * @param d the display object to clone.
	 * @return a duplicate instance of d.
	 */
	public function cloneDisplayObject(d:DisplayObject):DisplayObject
	{
		if (!d) return null;
		
		/* Create duplicate. */
		var clazz:Class = (d as Object)['constructor'];
		var clone:DisplayObject = new clazz();
		
		/* Duplicate properties. */
		var obj:Object = describeTypeProperties(d, true);
		for (var k:String in obj)
		{
			if (k == "scale9Grid") continue;
			if (k == "name") continue;
			clone[k] = d[k];
		}
		
		clone.transform = d.transform;
		clone.filters = d.filters;
		clone.cacheAsBitmap = d.cacheAsBitmap;
		clone.opaqueBackground = d.opaqueBackground;
		clone.x = d.x;
		clone.y = d.y;
		clone.width = d.width;
		clone.height = d.height;
		clone.rotation = d.rotation;
		
		if (d.scale9Grid)
		{
			var r:Rectangle = d.scale9Grid;
			try
			{
				clone.scale9Grid = r;
			}
			catch (err:Error)
			{
				Log.error("cloneDisplayObject: Could not clone scale9Grid - " + err.message, this);
			}
		}
		
		return clone;
	}
}