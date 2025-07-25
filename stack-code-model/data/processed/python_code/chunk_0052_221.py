/*
 * Copyright 2010 The Closure Compiler Authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/*
 * This file was generated from Google's Externs for the Google Maps v3.11 API.
 */
package google.maps {

/**
 * @see [google_maps_api_v3_11]
 * @constructor  */
public class Size {

    /**
     * @param width [number] 
     * @param height [number] 
     * @param opt_widthUnit [(string|undefined)] 
     * @param opt_heightUnit [(string|undefined)] 
     * @see [google_maps_api_v3_11]
     */
    public function Size(width:Number, height:Number, opt_widthUnit:String = '', opt_heightUnit:String = '') {
        super();
    }

    /**
     * @see JSType - [number] 
     * @see [google_maps_api_v3_11]
     */
    public var height:Number;

    /**
     * @see JSType - [number] 
     * @see [google_maps_api_v3_11]
     */
    public var width:Number;

    /**
     * @param other [(google.maps.Size|null)] 
     * @see [google_maps_api_v3_11]
     * @returns {boolean} 
     */
    public function equals(other:google.maps.Size):Boolean {  return null; }

    /**
     * @see [google_maps_api_v3_11]
     * @returns {string} 
     */
    public function toString():String {  return null; }

}
}