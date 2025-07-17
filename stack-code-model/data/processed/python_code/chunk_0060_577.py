///////////////////////////////////////////////////////////////////////////
// Copyright (c) 2012 Esri. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
///////////////////////////////////////////////////////////////////////////
package cn.seisys.TGISViewer.utils
{

import com.esri.ags.Graphic;
import com.esri.ags.geometry.Geometry;
import com.esri.ags.geometry.MapPoint;
import com.esri.ags.geometry.Multipoint;
import com.esri.ags.geometry.Polygon;
import com.esri.ags.geometry.Polyline;
import com.esri.ags.layers.GraphicsLayer;
import com.esri.ags.layers.supportClasses.LayerInfo;

import flash.events.TimerEvent;
import flash.utils.Timer;

public class MapServiceUtil
{
    public static function getVisibleSubLayers(layerInfos:Array, layerIds:Array = null):Array
    {
        var result:Array = [];

        layerIds = layerIds ? layerIds.concat() : null;

        var layerInfo:LayerInfo;
        var layerIdIndex:int;

        if (layerIds)
        {
            // replace group layers with their sub layers
            for each (layerInfo in layerInfos)
            {
                layerIdIndex = layerIds.indexOf(layerInfo.layerId);
                if (layerInfo.subLayerIds && layerIdIndex != -1)
                {
                    layerIds.splice(layerIdIndex, 1); // remove the group layer id
                    for each (var subLayerId:Number in layerInfo.subLayerIds)
                    {
                        layerIds.push(subLayerId); // add subLayerId
                    }
                }
            }
            result = layerIds;
        }
        else
        {
            result = getDefaultVisibleLayers(layerInfos);
        }

        // remove group layers
        for each (layerInfo in layerInfos)
        {
            if (layerInfo.subLayerIds)
            {
                layerIdIndex = result.indexOf(layerInfo.layerId);
                if (layerIdIndex != -1)
                {
                    result.splice(layerIdIndex, 1);
                }
            }
        }

        return result;
    }

    private static function getDefaultVisibleLayers(layerInfos:Array):Array
    {
        var result:Array = [];

        for each (var layerInfo:LayerInfo in layerInfos)
        {
            if (layerInfo.parentLayerId >= 0 && result.indexOf(layerInfo.parentLayerId) == -1)
            {
                // layer is not visible if it's parent is not visible
                continue;
            }
            if (layerInfo.defaultVisibility)
            {
                result.push(layerInfo.layerId);
            }
        }

        return result;
    }
	
	//get geom center
	public static function getGeomCenter(gra:Graphic):MapPoint 
	{
		if ( !gra.geometry )
			return null;
		
		var pt:MapPoint;
		switch (gra.geometry.type) 
		{
			case Geometry.MAPPOINT: 
			{
				pt = gra.geometry as MapPoint;
				break;
			}
			case Geometry.MULTIPOINT: 
			{
				const multipoint:Multipoint = gra.geometry as Multipoint;
				pt = multipoint.points && multipoint.points.length > 0 ? multipoint.points[0] as MapPoint : null;
				break;
			}
			case Geometry.POLYLINE: 
			{
				const pl:Polyline = gra.geometry as Polyline;
				const pathCount:Number = pl.paths.length;
				const pathIndex:int = pathCount % 2 == 0 || pathCount == 1 ? pathCount / 2 : pathCount / 2 + 1;
				const midPath:Array = pl.paths[pathIndex];
				const ptCount:Number = midPath.length;
				const ptIndex:int = ptCount % 2 == 0 || ptCount == 1 ? ptCount / 2 : ptCount / 2 + 1;
				pt = pl.getPoint(pathIndex, ptIndex);
				break;
			}
			case Geometry.POLYGON: 
			{
				const poly:Polygon = gra.geometry as Polygon;
				pt = poly.extent.center;
				break;
			}
		}
		return pt;
	}
	
	public static function flashGraphic( graphic:Graphic, graphicLayer:GraphicsLayer, delay:Number, repeatCount:int = 0 ):Timer
	{
		var timer:Timer = new Timer( delay, repeatCount * 2 );
		timer.addEventListener(TimerEvent.TIMER, flashTimer_timerEvnetHandler );
		timer.start();
		return timer;
		
		function flashTimer_timerEvnetHandler( event:TimerEvent ):void
		{
			graphic.visible = !graphic.visible;
			graphicLayer.refresh();
		}
	}
	
	public static function stopFlashGrahpic( timer:Timer, graphic:Graphic, graphicLayer:GraphicsLayer ):void
	{
		timer.stop();
		graphic.visible = true;
		graphicLayer.refresh();
	}
}

}