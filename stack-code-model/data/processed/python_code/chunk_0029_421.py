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
package google.maps.visualization {

import google.maps.Map;
import google.maps.MVCObject;
import google.maps.MVCArray;

/**
 * @see [google_maps_api_v3_11]
 * @constructor extends google.maps.MVCObject */
public class HeatmapLayer extends google.maps.MVCObject {

    /**
     * @param opt_opts [(Object<?,string>|google.maps.visualization.HeatmapLayerOptions|null|undefined)] 
     * @see [google_maps_api_v3_11]
     */
    public function HeatmapLayer(opt_opts:Object = null) {
        super();
    }

    /**
     * @see [google_maps_api_v3_11]
     * @returns {(google.maps.MVCArray|null)} 
     */
    public function getData():google.maps.MVCArray {  return null; }

    /**
     * @param data [(Array<(google.maps.LatLng|google.maps.visualization.WeightedLocation|null)>|google.maps.MVCArray|null)] 
     * @see [google_maps_api_v3_11]
     * @returns {undefined} 
     */
    public function setData(data:Object):Object /* undefined */ {  return null; }

    /**
     * @param map [(google.maps.Map|null)] 
     * @see [google_maps_api_v3_11]
     * @returns {undefined} 
     */
    public function setMap(map:google.maps.Map):Object /* undefined */ {  return null; }

    /**
     * @see [google_maps_api_v3_11]
     * @returns {(google.maps.Map|null)} 
     */
    public function getMap():google.maps.Map {  return null; }

}
}