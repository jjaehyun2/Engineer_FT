﻿/*
 * FLINT PARTICLE SYSTEM
 * .....................
 * 
 * Author: Richard Lord
 * Copyright (c) Richard Lord 2008-2011
 * http://flintparticles.org/
 * 
 * Licence Agreement
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

import org.flintparticles.common.debug.*;
import org.flintparticles.common.actions.*;
import org.flintparticles.common.counters.*;
import org.flintparticles.common.displayObjects.RadialDot;
import org.flintparticles.common.initializers.*;
import org.flintparticles.twoD.actions.*;
import org.flintparticles.twoD.emitters.Emitter2D;
import org.flintparticles.twoD.initializers.*;
import org.flintparticles.twoD.renderers.*;
import org.flintparticles.twoD.zones.*;	
import org.flintparticles.common.easing.TwoWay;

var bitmapData:BitmapData = new Logo( 265, 80 );
var bitmap:Bitmap = new Bitmap( new Logo( 265, 80 ) );
bitmap.bitmapData = bitmapData;
addChild( bitmap );
bitmap.x = 118;
bitmap.y = 70;

var emitter:Emitter2D = new Emitter2D();
emitter.counter = new Steady( 600 );

emitter.addInitializer( new Lifetime( 0.8 ) );
emitter.addInitializer( new Velocity( new DiscSectorZone( new Point( 0, 0 ), 10, 5, -Math.PI * 0.75, -Math.PI * 0.25 ) ) );
emitter.addInitializer( new Position( new BitmapDataZone( bitmapData ) ) );
emitter.addInitializer( new ImageClass( FireBlob ) );

emitter.addAction( new Age( TwoWay.quadratic ) );
emitter.addAction( new Move() );
emitter.addAction( new Accelerate( 0, -20 ) );
emitter.addAction( new ColorChange( 0xFFFF9900, 0x00FFDD66 ) );
emitter.addAction( new ScaleImage( 1.4, 2.0 ) );
emitter.addAction( new RotateToDirection() );

var renderer:BitmapRenderer = new BitmapRenderer( new Rectangle( 0, 0, 500, 200 ) );
renderer.addEmitter( emitter );
addChild( renderer );

emitter.x = 118;
emitter.y = 70;
emitter.start( );