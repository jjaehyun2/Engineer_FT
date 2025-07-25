// =================================================================================================
//
//	Starling Framework
//	Copyright 2012 Gamua OG. All Rights Reserved.
//
//	This program is free software. You can redistribute and/or modify it
//	in accordance with the terms of the accompanying license agreement.
//
// =================================================================================================

package starling.textures
{

	import flash.display3D.Context3DTextureFormat;
	import flash.utils.ByteArray;

	/** A parser for the ATF data format. */
    internal class AtfData
    {
        private var mFormat:String;
        private var mWidth:int;
        private var mHeight:int;
        private var mNumTextures:int;
        private var mData:ByteArray;
        
        /** Create a new instance by parsing the given byte array. */
        public function AtfData(data:ByteArray)
        {
            var signature:String = String.fromCharCode(data[0], data[1], data[2]);
            if (signature != "ATF") throw new ArgumentError("Invalid ATF data");
            
            switch (data[6])
            {
                case 0:
                case 1: mFormat = Context3DTextureFormat.BGRA; break;
                case 2:
                case 3: mFormat = Context3DTextureFormat.COMPRESSED; break;
                case 4:
                case 5: mFormat = "compressedAlpha"; break; // explicit string to stay compatible 
                                                            // with older versions
                default: throw new Error("Invalid ATF format");
            }
            
            mWidth = Math.pow(2, data[7]); 
            mHeight = Math.pow(2, data[8]);
            mNumTextures = data[9];
            mData = data;
        }
        
        public function get format():String { return mFormat; }
        public function get width():int { return mWidth; }
        public function get height():int { return mHeight; }
        public function get numTextures():int { return mNumTextures; }
        public function get data():ByteArray { return mData; }
    }
}