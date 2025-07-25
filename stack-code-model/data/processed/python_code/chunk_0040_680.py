///////////////////////////////////////////////////////////////////////////
// Copyright (c) 2010-2011 Esri. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and 
// limitations under the License.
///////////////////////////////////////////////////////////////////////////
package com.esri.controllers
{

import com.esri.ags.Graphic;
import com.esri.ags.Map;
import com.esri.ags.SpatialReference;
import com.esri.ags.esri_internal;
import com.esri.ags.events.LocatorEvent;
import com.esri.ags.geometry.MapPoint;
import com.esri.ags.geometry.WebMercatorMapPoint;
import com.esri.ags.symbols.Symbol;
import com.esri.ags.tasks.Locator;
import com.esri.ags.tasks.supportClasses.AddressCandidate;
import com.esri.ags.tasks.supportClasses.AddressToLocationsParameters;
import com.esri.ags.utils.WebMercatorUtil;
import com.esri.model.Model;
import com.esri.views.AddrSymbol;

import mx.rpc.events.FaultEvent;

use namespace esri_internal;

public final class LocateController
{
    [Bindable]
    /**
     * Reference to the map.
     */
    public var map:Map;

    [Bindable]
    /**
     * Reference to the model.
     */
    public var model:Model;

    public function addressToLocation(address:String, mapLevel:int = -1):void
    {
        const param:Object = {};
        param[model.locatorKey] = address;

        const addressToLocationsParameters:AddressToLocationsParameters = new AddressToLocationsParameters();
        addressToLocationsParameters.address = param;
        //addressToLocationsParameters.outFields = [ model.locatorVal ];

        const locator:Locator = new Locator(model.locatorURL);
        locator.outSpatialReference = map.spatialReference;
        locator.requestTimeout = model.requestTimeout;
        locator.showBusyCursor = true;
        locator.addEventListener(FaultEvent.FAULT, faultHandler);
        locator.addEventListener(LocatorEvent.ADDRESS_TO_LOCATIONS_COMPLETE, locator_addressToLocationsCompleteHandler);
        locator.addressToLocations(addressToLocationsParameters);

        function locator_addressToLocationsCompleteHandler(event:LocatorEvent):void
        {
            if (map.hasEventListener(event.type))
            {
                map.dispatchEvent(event);
                if (event.isDefaultPrevented())
                {
                    return;
                }
            }
            if (locator.addressToLocationsLastResult && locator.addressToLocationsLastResult.length)
            {
                const addrCand:AddressCandidate = locator.addressToLocationsLastResult[0];
                const graphic:Graphic = new Graphic(addrCand.location, null, addrCand.attributes);
                graphic.toolTip = addrCand.attributes[model.locatorVal];
                model.pointArrCol.addItem(graphic);
                if (mapLevel > -1)
                {
                    map.centerAt(addrCand.location);
                    map.level = mapLevel;
                }
            }
        }

        function faultHandler(event:FaultEvent):void
        {
            if (map.hasEventListener(event.type))
            {
                map.dispatchEvent(event);
            }
        }

    }

    public function locationToAddress(mapPoint:MapPoint, distance:Number):void
    {
        const locator:Locator = new Locator(model.locatorURL);
        locator.outSpatialReference = map.spatialReference;
        locator.requestTimeout = model.requestTimeout;
        locator.showBusyCursor = true;
        locator.addEventListener(FaultEvent.FAULT, faultHandler);
        locator.addEventListener(LocatorEvent.LOCATION_TO_ADDRESS_COMPLETE, locationToAddressCompleteHandler);
        const latlon:MapPoint = toLatLon(mapPoint);
        locator.locationToAddress(latlon, distance);

        function locationToAddressCompleteHandler(event:LocatorEvent):void
        {
            if (map.hasEventListener(event.type))
            {
                map.dispatchEvent(event);
                if (event.isDefaultPrevented())
                {
                    return;
                }
            }
            if (locator.locationToAddressLastResult)
            {
                const attributes:Object = locator.locationToAddressLastResult.address;
                const arr:Array = [];
                if (attributes.Address)
                {
                    arr.push(attributes.Address);
                }
                else
                {
                    attributes.Address = "N/A";
                }
                if (attributes.City)
                {
                    arr.push(attributes.City);
                }
                if (attributes.State)
                {
                    arr.push(attributes.State);
                }
                if (attributes.Zip)
                {
                    arr.push(attributes.Zip);
                }
                attributes.AddressFull = arr.join(' ');
                model.pointArrCol.addItem(new Graphic(mapPoint /*locator.locationToAddressLastResult.location*/, getAddrSymbol(), attributes));
            }
            else
            {
                addNoAddr();
            }
        }

        function faultHandler(event:FaultEvent):void
        {
            if (map.hasEventListener(event.type))
            {
                map.dispatchEvent(event);
                if (event.isDefaultPrevented())
                {
                    return;
                }
            }
            addNoAddr();
        }

        function addNoAddr():void
        {
            model.pointArrCol.addItem(new Graphic(mapPoint, getAddrSymbol(), { Address: 'N/A', AddressFull: 'No Address' }));
        }

    }

    private function toLatLon(mapPoint:MapPoint):MapPoint
    {
        if (mapPoint.x >= -180 && mapPoint.x <= 180 && mapPoint.y >= -90 && mapPoint.y <= 90)
        {
            return mapPoint;
        }
        return new MapPoint(WebMercatorUtil.xToLongitude(mapPoint.x), WebMercatorUtil.yToLatitude(mapPoint.y), new SpatialReference(4326));
    }

    private function toMercator(mapPoint:MapPoint):MapPoint
    {
        if (mapPoint.x >= -180 && mapPoint.x <= 180 && mapPoint.y >= -90 && mapPoint.y <= 90)
        {
            return new WebMercatorMapPoint(mapPoint.x, mapPoint.y);
        }
        return mapPoint;
    }

    private var m_addrSymbol:Symbol;

    private function getAddrSymbol():Symbol
    {
        if (m_addrSymbol === null)
        {
            m_addrSymbol = new AddrSymbol();
        }
        return m_addrSymbol;
    }
}

}