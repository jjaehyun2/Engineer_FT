﻿/**************************************************************************
 * LOGOSWARE Class Library.
 *
 * Copyright 2009 (c) LOGOSWARE (http://www.logosware.com) All rights reserved.
 *
 *
 * This program is free software; you can redistribute it and/or modify it under
 * the terms of the GNU General Public License as published by the Free Software
 * Foundation; either version 2 of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along with
 * this program; if not, write to the Free Software Foundation, Inc., 59 Temple
 * Place, Suite 330, Boston, MA 02111-1307 USA
 *
 **************************************************************************/
package com.logosware.qr {
import flash.display.BitmapData;
import flash.filters.ColorMatrixFilter;
import flash.filters.ConvolutionFilter;
import flash.geom.Point;
import flash.geom.Rectangle;
import flash.utils.ByteArray;

/**
 * QRImage Class recognizes QR Code from image.
 *
 * A class for cutting out the QR code image from the camera mainly.
 * Returns a formatted in a two-dimensional array of 0 and 1 the QR Code Version 1 ~ 10 in the image on
 *
 * @author Kenichi UENO
 * @contributor Andras Csizmadia - www.vpmedia.eu
 **/
public class QRImage {

    /**
     * @private
     * Minimum version that supports
     **/
    private var _minVersion:uint = 1;

    /**
     * @private
     * Highest version that supports
     **/
    private var _maxVersion:uint = 10;

    /**
     * @private
     **/
    private var _resultImage:BitmapData = new BitmapData(1, 1);

    /**
     * @private
     **/
    private var _resultArray:Array = [];

    /**
     * @private
     **/
    private var _results:Array = [
        _resultImage,
        _resultArray
    ];

    /**
     * @private
     **/
    private const _origin:Point = new Point(0, 0);

    //----------------------------------
    //  Constructor
    //----------------------------------

    /**
     * Constructor.
     **/
    public function QRImage() {
    }

    //----------------------------------
    //  API
    //----------------------------------

    /**
     * Run the reading
     * @return the result array
     */
    public function process(QRCodes:Array):Array {
        const n:uint = QRCodes ? QRCodes.length : 0;
        if (!n)
            return null;
        for (var i:int = 0; i < n; i++) {
            var bmpData:BitmapData = QRCodes[i].image;
            var colors:Array = QRCodes[i].borderColors;
            // Get the version
            var qrInfo:Object = _getVersion(bmpData, colors[0], colors[1], colors[2]);
            if (qrInfo.version > 0) {
                // Get the results of the grid
                _results = _getGrid(bmpData, qrInfo);
                _resultImage = _results[0];
                _resultArray = _results[1];

                // Marker also confirmed grid
                var checkBmp:BitmapData = new BitmapData(_resultImage.width, _resultImage.height);
                checkBmp.applyFilter(_resultImage, _resultImage.rect, _origin, new ConvolutionFilter(7, 7, [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], 33));
                if ((checkBmp.getPixel(7, 7) == 0) && (checkBmp.getPixel(checkBmp.width - 8, 7) == 0) && (checkBmp.getPixel(7, checkBmp.height - 8) == 0)) {
                    return _resultArray;
                }
            }
        }
        // process end
        return null;
    }

    //----------------------------------
    //  Private methods
    //----------------------------------

    /**
     * I will be a two-dimensional array of bits of information QR code
     * @param bmpData
     * @param qrInfo QR code information object
     * @return bit pattern array
     */
    private function _getGrid(bmpData:BitmapData, qrInfo:Object):Array {
        var __resultBmp:BitmapData = new BitmapData(8 + qrInfo.version * 4 + 17, 8 + qrInfo.version * 4 + 17);
        var __resultArray:Array = new Array(qrInfo.version * 4 + 17);
        var __i:uint;
        var __thisColor:uint;
        var __tlCenter:Object = { x: qrInfo.topLeftRect.topLeft.x + 0.5 * ( qrInfo.topLeftRect.width ), y: qrInfo.topLeftRect.topLeft.y + 0.5 * ( qrInfo.topLeftRect.height ) };
        var __trCenter:Object = { x: qrInfo.topRightRect.topLeft.x + 0.5 * ( qrInfo.topRightRect.width ), y: qrInfo.topRightRect.topLeft.y + 0.5 * ( qrInfo.topRightRect.height ) };
        var __blCenter:Object = { x: qrInfo.bottomLeftRect.topLeft.x + 0.5 * ( qrInfo.bottomLeftRect.width ), y: qrInfo.bottomLeftRect.topLeft.y + 0.5 * ( qrInfo.bottomLeftRect.height ) };
        for (__i = 0; __i < (qrInfo.version * 4 + 17); __i++) {
            __resultArray[__i] = new Array(qrInfo.version * 4 + 17);
        }
        __i = 0;
        __thisColor = 0;
        while (__thisColor != 0xFFFFFF) {
            __i++;
            __thisColor = bmpData.getPixel(qrInfo.topRightRect.topLeft.x + __i, qrInfo.bottomLeftRect.topLeft.y + __i);
        }
        bmpData.floodFill(qrInfo.topRightRect.topLeft.x + __i, qrInfo.bottomLeftRect.topLeft.y + __i, 0xFFCCFFFF);

        var __bottomRightRect:Rectangle = bmpData.getColorBoundsRect(0xFFFFFFFF, 0xFFCCFFFF);
        bmpData.floodFill(qrInfo.topRightRect.topLeft.x + __i, qrInfo.bottomLeftRect.topLeft.y + __i, 0xFFFFFFFF);
        var __brCenter:Object = { x: __bottomRightRect.topLeft.x + 0.5 * ( __bottomRightRect.width ), y: __bottomRightRect.topLeft.y + 0.5 * ( __bottomRightRect.height ) };

        if (qrInfo.version == 1) {
            __brCenter.x = __blCenter.x + (__trCenter.x - __tlCenter.x) * 11.0 / 14.0;
            __brCenter.y = __trCenter.y + (__blCenter.y - __tlCenter.y) * 11.0 / 14.0;
        }

        var __tempNum1:Number = ( qrInfo.version * 4.0 + 17 - 10 ); //QRコード上の、左上マーカー中心から右「下」マーカー中心までのｘ座標の差 (ver5なら27)
        var __tempNum2:Number = ( qrInfo.version * 4.0 + 17 - 7 ); //QRコード上の、左上マーカー中心から右「上」マーカー中心までのｘ座標の差 (ver5なら30)

        var __blTop:Object = { x: qrInfo.bottomLeftRect.topLeft.x + qrInfo.bottomLeftRect.width * 0.5, y: qrInfo.bottomLeftRect.topLeft.y + qrInfo.bottomLeftRect.height / 14.0 };
        var __trLeft:Object = { x: qrInfo.topRightRect.topLeft.x + qrInfo.topRightRect.width / 14.0, y: qrInfo.topRightRect.topLeft.y + qrInfo.topRightRect.height * 0.5 };

        var __sum:Number = 0.0;
        var __num:Number = 0.0;

        for (__i = __blTop.y - qrInfo.cellSize; __i <= __blTop.y + qrInfo.cellSize; __i++) {
            if (bmpData.getPixel(__blTop.x, __i) != 0xFFFFFF) {
                __sum += __i;
                __num++;
            }
        }
        __blTop.y = 0.5 * (__blTop.y + __sum / __num);

        var __a3:Number = ( __tlCenter.y - __trLeft.y) / ( __tlCenter.x - __trLeft.x);
        var __a30:Number = ( __blTop.y - __brCenter.y) / ( __blTop.x - __brCenter.x);
        var __b3:Number = __trLeft.y - __a3 * __trLeft.x;
        var __b30:Number = __brCenter.y - __a30 * __brCenter.x;
        var __startX3:Number = __tlCenter.x + ( __trLeft.x - __tlCenter.x ) * ( -3.0 / __tempNum1 );
        var __startX30:Number = __blTop.x + ( __brCenter.x - __blTop.x ) * ( -3.0 / __tempNum1 );
        var __startY3:Number = __tlCenter.y + ( __trLeft.y - __tlCenter.y ) * ( -3.0 / __tempNum1 );
        var __startY30:Number = __blTop.y + ( __brCenter.y - __blTop.y ) * ( -3.0 / __tempNum1 );
        var __end3:Number = __trLeft.x + ( __trLeft.x - __tlCenter.x ) * ( 6.0 / __tempNum1 );
        var __end30:Number = __brCenter.x + ( __brCenter.x - __blTop.x ) * ( 6.0 / __tempNum1 );
        var __loopConst:uint = (__resultBmp.width - 8 );
        var __loopConst2:uint = __loopConst - 1;
        var __a:Array = new Array(__loopConst);
        var __b:Array = new Array(__loopConst);
        var __startX:Array = new Array(__loopConst);
        var __startY:Array = new Array(__loopConst);
        var __endX:Array = new Array(__loopConst);

        for (__i = 0; __i < __loopConst; __i++) {
            __a[__i] = (( __a30 - __a3 ) / __tempNum1) * ( __i - 3 ) + __a3;
            __startX[__i] = (( __startX30 - __startX3 ) / __tempNum1) * ( __i - 3 ) + __startX3;
            __startY[__i] = (( __startY30 - __startY3 ) / __tempNum1) * ( __i - 3 ) + __startY3;
            __endX[__i] = (( __end30 - __end3 ) / __tempNum1) * ( __i - 3 ) + __end3;
            __b[__i] = __startY[__i] - __a[__i] * __startX[__i];
        }
        for (var __y:Number = 0; __y < __loopConst; __y++) {
            var __y2:Number = __y - 3;
            for (var __x:Number = 0; __x < __loopConst; __x++) {
                var __x2:Number = __x - 3;
                if ((bmpData.getPixel(__startX[__y] + ( __endX[__y] - __startX[__y] ) * ( __x / __loopConst2 ), __a[__y] * (__startX[__y] + ( __endX[__y] - __startX[__y] ) * ( __x / __loopConst2 )) + __b[__y]) & 0xFF0000) < 0xFF0000) {
                    __resultBmp.setPixel(4 + __x, 4 + __y, 0);
                    __resultArray[__y][__x] = 1;
                }
            }
        }
        return [__resultBmp, __resultArray];
    }

    /**
     * I determine which version of the QR code
     * @param bmp source image
     * @param tlColor
     * @param trColor
     * @param blColor
     * @return QR code info object
     */
    private function _getVersion(bmp:BitmapData, tlColor:uint, trColor:uint, blColor:uint):Object {
        var i:uint;
        var thisColor:uint;
        bmp.lock();
        var topLeftRect:Rectangle = bmp.getColorBoundsRect(0xFFFFFFFF, tlColor);
        var topRightRect:Rectangle = bmp.getColorBoundsRect(0xFFFFFFFF, trColor);
        var bottomLeftRect:Rectangle = bmp.getColorBoundsRect(0xFFFFFFFF, blColor);
        var startTopLeft:Point = new Point(26, topLeftRect.topLeft.y + topLeftRect.height);
        var numX:uint = 0;
        var tempX:uint;
        var oldP:uint;
        var whiteNum:uint = 0;
        for (var j:int = -8; j <= 0; j++) {
            tempX = 0;
            var whiteArray:Array = [];
            var tempArray:ByteArray = bmp.getPixels(new Rectangle(startTopLeft.x, startTopLeft.y + j, bmp.width - 52, 1));
            var startColor:uint = tempArray[1];
            var endColor:uint = tempArray[4 * (bmp.width - 26 - 1) + 1];
            if (( startColor != 0xFF ) && ( endColor != 0xFF )) {
                oldP = startColor;
                for (i = 1; i < (bmp.width - 24); i++) {
                    var tempColor:uint = tempArray[4 * i + 1];
                    if (tempColor != oldP) {
                        tempX++;
                        oldP = tempColor;
                    }
                    if (tempColor == 0xFF) {
                        whiteNum++;
                    } else {
                        if (whiteNum > 0) {
                            whiteArray.push([whiteNum]);
                            whiteNum = 0;
                        }
                    }
                }
                var sum:Number = 0;
                // White mass check of validity is OK when you were about the same size all
                for (var k:uint = 0; k < whiteArray.length; k++) {
                    sum += Number(whiteArray[k]);
                }
                var average:Number = sum / whiteArray.length;
                var error:uint = 0;
                for (k = 0; k < whiteArray.length; k++) {
                    if (!((whiteArray[k] > (average * 0.5)) && (whiteArray[k] < (average * 1.5)) )) {
                        error++;
                    }
                }
                if ((numX < tempX) && (error == 0)) {
                    numX = tempX;
                }
            }
        }
        numX = Math.floor(( ( numX - 3 ) - 6  ) * 0.25) + 1;
        startTopLeft = new Point(topLeftRect.topLeft.x + topLeftRect.width, 26);
        var numY:uint = 0;
        whiteNum = 0;
        for (j = -8; j <= 0; j++) {
            tempX = 0;
            whiteArray = [];
            tempArray = bmp.getPixels(new Rectangle(startTopLeft.x + j, startTopLeft.y, 1, bmp.height - 52));
            startColor = tempArray[1];
            endColor = tempArray[4 * (bmp.height - 26 - 1) + 1];
            if (( startColor != 0xFF ) && ( endColor != 0xFF )) {
                oldP = startColor;
                for (i = 1; i < (bmp.height - 24); i++) {
                    tempColor = tempArray[4 * i + 1];
                    if (tempColor != oldP) {
                        tempX++;
                        oldP = tempColor;
                    }
                    if (tempColor == 0xFF) {
                        whiteNum++;
                    } else {
                        if (whiteNum > 0) {
                            whiteArray.push([whiteNum]);
                            whiteNum = 0;
                        }
                    }
                }
                sum = 0;
                // White mass check of validity is OK when you were about the same size all
                for (k = 0; k < whiteArray.length; k++) {
                    sum += Number(whiteArray[k]);
                }
                average = sum / whiteArray.length;
                error = 0;
                for (k = 0; k < whiteArray.length; k++) {
                    if (!((whiteArray[k] > (average * 0.5)) && (whiteArray[k] < (average * 1.5)) )) {
                        error++;
                    }
                }
                if ((numY < tempX) && (error == 0)) {
                    numY = tempX;
                }
            }
        }
        numY = Math.floor(( ( numY - 3 ) - 6  ) * 0.25) + 1;

        if ((numX == numY) && (numX >= _minVersion) && (numX <= _maxVersion )) {
//				trace("numX");
        } else {
            numX = 0;
        }
        bmp.unlock();
        return {cellSize: (topRightRect.x + topRightRect.width - topLeftRect.x) / (numX * 4 + 17), version: numX, topLeftRect: topLeftRect, topRightRect: topRightRect, bottomLeftRect: bottomLeftRect};
    }

    /**
     * Calculating the threshold of black and white using the brightness of the image near the center
     * @param bmp TBD
     * @return TBD
     */
    private function _getThreshold(bmp:BitmapData):uint {
        var rect:Rectangle = new Rectangle(bmp.width * 0.5, 0, 1, bmp.height);
        var bmp_check:BitmapData = new BitmapData(1, bmp.height);
        bmp_check.copyPixels(bmp, rect, new Point(0, 0));
        bmp_check.lock();
        var tempArray:ByteArray = bmp_check.getPixels(bmp_check.rect);
        var sum:Number = 0.0;
        for (var i:uint = 0; i < bmp.height; i++) {
            sum += tempArray[4 * i + 3]; // TBD
        }
        sum /= bmp.height;

        return uint(0xFF000000 + 0x00010101 * Math.round(sum));
    }

    /**
     * I want to gray scale of the image
     * @param bmp_src TBD
     * @param bmp_dst TBD
     * @param rect TBD
     * @param point TBD
     * @param constnum TBD
     **/
    private function _toGray(bmp_src:BitmapData, bmp_dst:BitmapData, rect:Rectangle, point:Point, constnum:Number = 2.5):void {
        var conGray:Array = [constnum * 0.3, constnum * 0.59, constnum * 0.11];
        var cmfGray:ColorMatrixFilter = new ColorMatrixFilter(
                [conGray[0], conGray[1], conGray[2], 0, 0,
                    conGray[0], conGray[1], conGray[2], 0, 0,
                    conGray[0], conGray[1], conGray[2], 0, 0,
                    0, 0, 0, 0, 255]
        );
        bmp_dst.applyFilter(bmp_src, rect, point, cmfGray);
    }

    /**
     * I binarized image
     * @param bmp TBD
     * @param threshold TBD
     **/
    private function _binalization(bmp:BitmapData, threshold:uint = 0xFFFFFFFF):void {
        bmp.threshold(bmp, bmp.rect, new Point(0, 0), "<", threshold, 0xFF000000, 0xFFFFFFFF);
        bmp.threshold(bmp, bmp.rect, new Point(0, 0), ">=", threshold, 0xFFFFFFFF, 0xFFFFFFFF);
    }

    /**
     * I want to pick up a point on the boundary
     * @param bmp TBD
     * @param rect TBD
     * @param color TBD
     * @param devide TBD
     * @return TBD
     **/
    private function _getBorderPoints(bmp:BitmapData, rect:Rectangle, color:uint, divide:uint):Array {
        var tempX:uint;
        var tempY:uint;
        var tempBmpX:BitmapData = new BitmapData(rect.width, 1);
        var tempBmpY:BitmapData = new BitmapData(1, rect.height);
        var tempRect2:Rectangle;
        var tempPoint:Point;
        const loopCount:uint = divide;
        var borderPoints:Array = new Array();
        for (var j:uint = 0; j <= loopCount; j++) {
            tempX = ( (rect.width - 1) * j ) / loopCount + rect.topLeft.x;
            tempY = ( (rect.height - 1) * j ) / loopCount + rect.topLeft.y;
            tempBmpX.copyPixels(bmp, new Rectangle(rect.topLeft.x, tempY, rect.width, 1), new Point(0, 0));
            tempBmpY.copyPixels(bmp, new Rectangle(tempX, rect.topLeft.y, 1, rect.height), new Point(0, 0));
            // Horizontal line scan
            tempRect2 = tempBmpY.getColorBoundsRect(0xFFFFFFFF, color);
            tempPoint = new Point(
                    tempX + tempRect2.topLeft.x,
                    rect.topLeft.y + tempRect2.topLeft.y
            );
            borderPoints.push(tempPoint);
            tempPoint = new Point(
                    tempX + tempRect2.topLeft.x + tempRect2.width,
                    rect.topLeft.y + tempRect2.topLeft.y + tempRect2.height);
            borderPoints.push(tempPoint);
            // Vertical line scan
            tempRect2 = tempBmpX.getColorBoundsRect(0xFFFFFFFF, color);
            tempPoint = new Point(
                    rect.topLeft.x + tempRect2.topLeft.x,
                    tempY + tempRect2.topLeft.y
            );
            borderPoints.push(tempPoint);
            tempPoint = new Point(
                    rect.topLeft.x + tempRect2.topLeft.x + tempRect2.width,
                    tempY + tempRect2.topLeft.y + tempRect2.height
            );
            borderPoints.push(tempPoint);
        }
        return borderPoints;
    }
}
}