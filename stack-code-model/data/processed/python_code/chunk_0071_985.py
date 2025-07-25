/**
 * AESKey
 * 
 * An ActionScript 3 implementation of the Advanced Encryption Standard, as
 * defined in FIPS PUB 197
 * Copyright (c) 2007 Henri Torgemane
 * 
 * Derived from:
 * 		A public domain implementation from Karl Malbrain, malbrain@yahoo.com
 * 		(http://www.geocities.com/malbrain/aestable_c.html)
 * 
 * See LICENSE.txt for full license information.
 */
package com.hurlant.crypto.symmetric
{
	import com.hurlant.crypto.prng.Random;
	import com.hurlant.util.Hex;
	import com.hurlant.util.Memory;
	
	import flash.utils.ByteArray;

	public class AESKey implements ISymmetricKey
	{
		// AES only supports Nb=4
		private static const Nb:uint = 4;    // number of columns in the state & expanded key
		
		// TODO:
		//  - move those tables in binary files, then
		//  - [Embed()] them as ByteArray directly.
		// (should result in smaller .swf, and faster initialization time.)
		
		private static const _Sbox:Array = [ // forward s-box
		0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
		0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
		0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
		0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
		0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
		0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
		0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
		0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
		0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
		0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
		0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
		0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
		0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
		0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
		0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
		0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16];
		private static const _InvSbox:Array = [ // inverse s-box
		0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
		0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
		0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
		0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
		0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
		0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
		0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
		0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
		0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
		0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
		0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
		0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
		0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
		0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
		0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
		0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d];		
		private static const _Xtime2Sbox:Array = [ // combined Xtimes2[Sbox[]]
		0xc6, 0xf8, 0xee, 0xf6, 0xff, 0xd6, 0xde, 0x91, 0x60, 0x02, 0xce, 0x56, 0xe7, 0xb5, 0x4d, 0xec, 
		0x8f, 0x1f, 0x89, 0xfa, 0xef, 0xb2, 0x8e, 0xfb, 0x41, 0xb3, 0x5f, 0x45, 0x23, 0x53, 0xe4, 0x9b, 
		0x75, 0xe1, 0x3d, 0x4c, 0x6c, 0x7e, 0xf5, 0x83, 0x68, 0x51, 0xd1, 0xf9, 0xe2, 0xab, 0x62, 0x2a, 
		0x08, 0x95, 0x46, 0x9d, 0x30, 0x37, 0x0a, 0x2f, 0x0e, 0x24, 0x1b, 0xdf, 0xcd, 0x4e, 0x7f, 0xea, 
		0x12, 0x1d, 0x58, 0x34, 0x36, 0xdc, 0xb4, 0x5b, 0xa4, 0x76, 0xb7, 0x7d, 0x52, 0xdd, 0x5e, 0x13, 
		0xa6, 0xb9, 0x00, 0xc1, 0x40, 0xe3, 0x79, 0xb6, 0xd4, 0x8d, 0x67, 0x72, 0x94, 0x98, 0xb0, 0x85, 
		0xbb, 0xc5, 0x4f, 0xed, 0x86, 0x9a, 0x66, 0x11, 0x8a, 0xe9, 0x04, 0xfe, 0xa0, 0x78, 0x25, 0x4b, 
		0xa2, 0x5d, 0x80, 0x05, 0x3f, 0x21, 0x70, 0xf1, 0x63, 0x77, 0xaf, 0x42, 0x20, 0xe5, 0xfd, 0xbf, 
		0x81, 0x18, 0x26, 0xc3, 0xbe, 0x35, 0x88, 0x2e, 0x93, 0x55, 0xfc, 0x7a, 0xc8, 0xba, 0x32, 0xe6, 
		0xc0, 0x19, 0x9e, 0xa3, 0x44, 0x54, 0x3b, 0x0b, 0x8c, 0xc7, 0x6b, 0x28, 0xa7, 0xbc, 0x16, 0xad, 
		0xdb, 0x64, 0x74, 0x14, 0x92, 0x0c, 0x48, 0xb8, 0x9f, 0xbd, 0x43, 0xc4, 0x39, 0x31, 0xd3, 0xf2, 
		0xd5, 0x8b, 0x6e, 0xda, 0x01, 0xb1, 0x9c, 0x49, 0xd8, 0xac, 0xf3, 0xcf, 0xca, 0xf4, 0x47, 0x10, 
		0x6f, 0xf0, 0x4a, 0x5c, 0x38, 0x57, 0x73, 0x97, 0xcb, 0xa1, 0xe8, 0x3e, 0x96, 0x61, 0x0d, 0x0f, 
		0xe0, 0x7c, 0x71, 0xcc, 0x90, 0x06, 0xf7, 0x1c, 0xc2, 0x6a, 0xae, 0x69, 0x17, 0x99, 0x3a, 0x27, 
		0xd9, 0xeb, 0x2b, 0x22, 0xd2, 0xa9, 0x07, 0x33, 0x2d, 0x3c, 0x15, 0xc9, 0x87, 0xaa, 0x50, 0xa5, 
		0x03, 0x59, 0x09, 0x1a, 0x65, 0xd7, 0x84, 0xd0, 0x82, 0x29, 0x5a, 0x1e, 0x7b, 0xa8, 0x6d, 0x2c];
		private static const _Xtime3Sbox:Array = [ // combined Xtimes3[Sbox[]]
		0xa5, 0x84, 0x99, 0x8d, 0x0d, 0xbd, 0xb1, 0x54, 0x50, 0x03, 0xa9, 0x7d, 0x19, 0x62, 0xe6, 0x9a, 
		0x45, 0x9d, 0x40, 0x87, 0x15, 0xeb, 0xc9, 0x0b, 0xec, 0x67, 0xfd, 0xea, 0xbf, 0xf7, 0x96, 0x5b, 
		0xc2, 0x1c, 0xae, 0x6a, 0x5a, 0x41, 0x02, 0x4f, 0x5c, 0xf4, 0x34, 0x08, 0x93, 0x73, 0x53, 0x3f, 
		0x0c, 0x52, 0x65, 0x5e, 0x28, 0xa1, 0x0f, 0xb5, 0x09, 0x36, 0x9b, 0x3d, 0x26, 0x69, 0xcd, 0x9f, 
		0x1b, 0x9e, 0x74, 0x2e, 0x2d, 0xb2, 0xee, 0xfb, 0xf6, 0x4d, 0x61, 0xce, 0x7b, 0x3e, 0x71, 0x97, 
		0xf5, 0x68, 0x00, 0x2c, 0x60, 0x1f, 0xc8, 0xed, 0xbe, 0x46, 0xd9, 0x4b, 0xde, 0xd4, 0xe8, 0x4a, 
		0x6b, 0x2a, 0xe5, 0x16, 0xc5, 0xd7, 0x55, 0x94, 0xcf, 0x10, 0x06, 0x81, 0xf0, 0x44, 0xba, 0xe3, 
		0xf3, 0xfe, 0xc0, 0x8a, 0xad, 0xbc, 0x48, 0x04, 0xdf, 0xc1, 0x75, 0x63, 0x30, 0x1a, 0x0e, 0x6d, 
		0x4c, 0x14, 0x35, 0x2f, 0xe1, 0xa2, 0xcc, 0x39, 0x57, 0xf2, 0x82, 0x47, 0xac, 0xe7, 0x2b, 0x95, 
		0xa0, 0x98, 0xd1, 0x7f, 0x66, 0x7e, 0xab, 0x83, 0xca, 0x29, 0xd3, 0x3c, 0x79, 0xe2, 0x1d, 0x76, 
		0x3b, 0x56, 0x4e, 0x1e, 0xdb, 0x0a, 0x6c, 0xe4, 0x5d, 0x6e, 0xef, 0xa6, 0xa8, 0xa4, 0x37, 0x8b, 
		0x32, 0x43, 0x59, 0xb7, 0x8c, 0x64, 0xd2, 0xe0, 0xb4, 0xfa, 0x07, 0x25, 0xaf, 0x8e, 0xe9, 0x18, 
		0xd5, 0x88, 0x6f, 0x72, 0x24, 0xf1, 0xc7, 0x51, 0x23, 0x7c, 0x9c, 0x21, 0xdd, 0xdc, 0x86, 0x85, 
		0x90, 0x42, 0xc4, 0xaa, 0xd8, 0x05, 0x01, 0x12, 0xa3, 0x5f, 0xf9, 0xd0, 0x91, 0x58, 0x27, 0xb9, 
		0x38, 0x13, 0xb3, 0x33, 0xbb, 0x70, 0x89, 0xa7, 0xb6, 0x22, 0x92, 0x20, 0x49, 0xff, 0x78, 0x7a, 
		0x8f, 0xf8, 0x80, 0x17, 0xda, 0x31, 0xc6, 0xb8, 0xc3, 0xb0, 0x77, 0x11, 0xcb, 0xfc, 0xd6, 0x3a];
		// modular multiplication tables
		// based on:
		
		// Xtime2[x] = (x & 0x80 ? 0x1b : 0) ^ (x + x)
		// Xtime3[x] = x^Xtime2[x];
		private static const _Xtime2:Array = [ 
		0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e, 
		0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x30, 0x32, 0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e, 
		0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e, 0x50, 0x52, 0x54, 0x56, 0x58, 0x5a, 0x5c, 0x5e, 
		0x60, 0x62, 0x64, 0x66, 0x68, 0x6a, 0x6c, 0x6e, 0x70, 0x72, 0x74, 0x76, 0x78, 0x7a, 0x7c, 0x7e, 
		0x80, 0x82, 0x84, 0x86, 0x88, 0x8a, 0x8c, 0x8e, 0x90, 0x92, 0x94, 0x96, 0x98, 0x9a, 0x9c, 0x9e, 
		0xa0, 0xa2, 0xa4, 0xa6, 0xa8, 0xaa, 0xac, 0xae, 0xb0, 0xb2, 0xb4, 0xb6, 0xb8, 0xba, 0xbc, 0xbe, 
		0xc0, 0xc2, 0xc4, 0xc6, 0xc8, 0xca, 0xcc, 0xce, 0xd0, 0xd2, 0xd4, 0xd6, 0xd8, 0xda, 0xdc, 0xde, 
		0xe0, 0xe2, 0xe4, 0xe6, 0xe8, 0xea, 0xec, 0xee, 0xf0, 0xf2, 0xf4, 0xf6, 0xf8, 0xfa, 0xfc, 0xfe, 
		0x1b, 0x19, 0x1f, 0x1d, 0x13, 0x11, 0x17, 0x15, 0x0b, 0x09, 0x0f, 0x0d, 0x03, 0x01, 0x07, 0x05, 
		0x3b, 0x39, 0x3f, 0x3d, 0x33, 0x31, 0x37, 0x35, 0x2b, 0x29, 0x2f, 0x2d, 0x23, 0x21, 0x27, 0x25, 
		0x5b, 0x59, 0x5f, 0x5d, 0x53, 0x51, 0x57, 0x55, 0x4b, 0x49, 0x4f, 0x4d, 0x43, 0x41, 0x47, 0x45, 
		0x7b, 0x79, 0x7f, 0x7d, 0x73, 0x71, 0x77, 0x75, 0x6b, 0x69, 0x6f, 0x6d, 0x63, 0x61, 0x67, 0x65, 
		0x9b, 0x99, 0x9f, 0x9d, 0x93, 0x91, 0x97, 0x95, 0x8b, 0x89, 0x8f, 0x8d, 0x83, 0x81, 0x87, 0x85, 
		0xbb, 0xb9, 0xbf, 0xbd, 0xb3, 0xb1, 0xb7, 0xb5, 0xab, 0xa9, 0xaf, 0xad, 0xa3, 0xa1, 0xa7, 0xa5, 
		0xdb, 0xd9, 0xdf, 0xdd, 0xd3, 0xd1, 0xd7, 0xd5, 0xcb, 0xc9, 0xcf, 0xcd, 0xc3, 0xc1, 0xc7, 0xc5, 
		0xfb, 0xf9, 0xff, 0xfd, 0xf3, 0xf1, 0xf7, 0xf5, 0xeb, 0xe9, 0xef, 0xed, 0xe3, 0xe1, 0xe7, 0xe5]; 
		private static const _Xtime9:Array = [
		0x00, 0x09, 0x12, 0x1b, 0x24, 0x2d, 0x36, 0x3f, 0x48, 0x41, 0x5a, 0x53, 0x6c, 0x65, 0x7e, 0x77, 
		0x90, 0x99, 0x82, 0x8b, 0xb4, 0xbd, 0xa6, 0xaf, 0xd8, 0xd1, 0xca, 0xc3, 0xfc, 0xf5, 0xee, 0xe7, 
		0x3b, 0x32, 0x29, 0x20, 0x1f, 0x16, 0x0d, 0x04, 0x73, 0x7a, 0x61, 0x68, 0x57, 0x5e, 0x45, 0x4c, 
		0xab, 0xa2, 0xb9, 0xb0, 0x8f, 0x86, 0x9d, 0x94, 0xe3, 0xea, 0xf1, 0xf8, 0xc7, 0xce, 0xd5, 0xdc, 
		0x76, 0x7f, 0x64, 0x6d, 0x52, 0x5b, 0x40, 0x49, 0x3e, 0x37, 0x2c, 0x25, 0x1a, 0x13, 0x08, 0x01, 
		0xe6, 0xef, 0xf4, 0xfd, 0xc2, 0xcb, 0xd0, 0xd9, 0xae, 0xa7, 0xbc, 0xb5, 0x8a, 0x83, 0x98, 0x91, 
		0x4d, 0x44, 0x5f, 0x56, 0x69, 0x60, 0x7b, 0x72, 0x05, 0x0c, 0x17, 0x1e, 0x21, 0x28, 0x33, 0x3a, 
		0xdd, 0xd4, 0xcf, 0xc6, 0xf9, 0xf0, 0xeb, 0xe2, 0x95, 0x9c, 0x87, 0x8e, 0xb1, 0xb8, 0xa3, 0xaa, 
		0xec, 0xe5, 0xfe, 0xf7, 0xc8, 0xc1, 0xda, 0xd3, 0xa4, 0xad, 0xb6, 0xbf, 0x80, 0x89, 0x92, 0x9b, 
		0x7c, 0x75, 0x6e, 0x67, 0x58, 0x51, 0x4a, 0x43, 0x34, 0x3d, 0x26, 0x2f, 0x10, 0x19, 0x02, 0x0b, 
		0xd7, 0xde, 0xc5, 0xcc, 0xf3, 0xfa, 0xe1, 0xe8, 0x9f, 0x96, 0x8d, 0x84, 0xbb, 0xb2, 0xa9, 0xa0, 
		0x47, 0x4e, 0x55, 0x5c, 0x63, 0x6a, 0x71, 0x78, 0x0f, 0x06, 0x1d, 0x14, 0x2b, 0x22, 0x39, 0x30, 
		0x9a, 0x93, 0x88, 0x81, 0xbe, 0xb7, 0xac, 0xa5, 0xd2, 0xdb, 0xc0, 0xc9, 0xf6, 0xff, 0xe4, 0xed, 
		0x0a, 0x03, 0x18, 0x11, 0x2e, 0x27, 0x3c, 0x35, 0x42, 0x4b, 0x50, 0x59, 0x66, 0x6f, 0x74, 0x7d, 
		0xa1, 0xa8, 0xb3, 0xba, 0x85, 0x8c, 0x97, 0x9e, 0xe9, 0xe0, 0xfb, 0xf2, 0xcd, 0xc4, 0xdf, 0xd6, 
		0x31, 0x38, 0x23, 0x2a, 0x15, 0x1c, 0x07, 0x0e, 0x79, 0x70, 0x6b, 0x62, 0x5d, 0x54, 0x4f, 0x46];
		private static const _XtimeB:Array = [
		0x00, 0x0b, 0x16, 0x1d, 0x2c, 0x27, 0x3a, 0x31, 0x58, 0x53, 0x4e, 0x45, 0x74, 0x7f, 0x62, 0x69, 
		0xb0, 0xbb, 0xa6, 0xad, 0x9c, 0x97, 0x8a, 0x81, 0xe8, 0xe3, 0xfe, 0xf5, 0xc4, 0xcf, 0xd2, 0xd9, 
		0x7b, 0x70, 0x6d, 0x66, 0x57, 0x5c, 0x41, 0x4a, 0x23, 0x28, 0x35, 0x3e, 0x0f, 0x04, 0x19, 0x12, 
		0xcb, 0xc0, 0xdd, 0xd6, 0xe7, 0xec, 0xf1, 0xfa, 0x93, 0x98, 0x85, 0x8e, 0xbf, 0xb4, 0xa9, 0xa2, 
		0xf6, 0xfd, 0xe0, 0xeb, 0xda, 0xd1, 0xcc, 0xc7, 0xae, 0xa5, 0xb8, 0xb3, 0x82, 0x89, 0x94, 0x9f, 
		0x46, 0x4d, 0x50, 0x5b, 0x6a, 0x61, 0x7c, 0x77, 0x1e, 0x15, 0x08, 0x03, 0x32, 0x39, 0x24, 0x2f, 
		0x8d, 0x86, 0x9b, 0x90, 0xa1, 0xaa, 0xb7, 0xbc, 0xd5, 0xde, 0xc3, 0xc8, 0xf9, 0xf2, 0xef, 0xe4, 
		0x3d, 0x36, 0x2b, 0x20, 0x11, 0x1a, 0x07, 0x0c, 0x65, 0x6e, 0x73, 0x78, 0x49, 0x42, 0x5f, 0x54, 
		0xf7, 0xfc, 0xe1, 0xea, 0xdb, 0xd0, 0xcd, 0xc6, 0xaf, 0xa4, 0xb9, 0xb2, 0x83, 0x88, 0x95, 0x9e, 
		0x47, 0x4c, 0x51, 0x5a, 0x6b, 0x60, 0x7d, 0x76, 0x1f, 0x14, 0x09, 0x02, 0x33, 0x38, 0x25, 0x2e, 
		0x8c, 0x87, 0x9a, 0x91, 0xa0, 0xab, 0xb6, 0xbd, 0xd4, 0xdf, 0xc2, 0xc9, 0xf8, 0xf3, 0xee, 0xe5, 
		0x3c, 0x37, 0x2a, 0x21, 0x10, 0x1b, 0x06, 0x0d, 0x64, 0x6f, 0x72, 0x79, 0x48, 0x43, 0x5e, 0x55, 
		0x01, 0x0a, 0x17, 0x1c, 0x2d, 0x26, 0x3b, 0x30, 0x59, 0x52, 0x4f, 0x44, 0x75, 0x7e, 0x63, 0x68, 
		0xb1, 0xba, 0xa7, 0xac, 0x9d, 0x96, 0x8b, 0x80, 0xe9, 0xe2, 0xff, 0xf4, 0xc5, 0xce, 0xd3, 0xd8, 
		0x7a, 0x71, 0x6c, 0x67, 0x56, 0x5d, 0x40, 0x4b, 0x22, 0x29, 0x34, 0x3f, 0x0e, 0x05, 0x18, 0x13, 
		0xca, 0xc1, 0xdc, 0xd7, 0xe6, 0xed, 0xf0, 0xfb, 0x92, 0x99, 0x84, 0x8f, 0xbe, 0xb5, 0xa8, 0xa3]; 
		private static const _XtimeD:Array = [
		0x00, 0x0d, 0x1a, 0x17, 0x34, 0x39, 0x2e, 0x23, 0x68, 0x65, 0x72, 0x7f, 0x5c, 0x51, 0x46, 0x4b, 
		0xd0, 0xdd, 0xca, 0xc7, 0xe4, 0xe9, 0xfe, 0xf3, 0xb8, 0xb5, 0xa2, 0xaf, 0x8c, 0x81, 0x96, 0x9b, 
		0xbb, 0xb6, 0xa1, 0xac, 0x8f, 0x82, 0x95, 0x98, 0xd3, 0xde, 0xc9, 0xc4, 0xe7, 0xea, 0xfd, 0xf0, 
		0x6b, 0x66, 0x71, 0x7c, 0x5f, 0x52, 0x45, 0x48, 0x03, 0x0e, 0x19, 0x14, 0x37, 0x3a, 0x2d, 0x20, 
		0x6d, 0x60, 0x77, 0x7a, 0x59, 0x54, 0x43, 0x4e, 0x05, 0x08, 0x1f, 0x12, 0x31, 0x3c, 0x2b, 0x26, 
		0xbd, 0xb0, 0xa7, 0xaa, 0x89, 0x84, 0x93, 0x9e, 0xd5, 0xd8, 0xcf, 0xc2, 0xe1, 0xec, 0xfb, 0xf6, 
		0xd6, 0xdb, 0xcc, 0xc1, 0xe2, 0xef, 0xf8, 0xf5, 0xbe, 0xb3, 0xa4, 0xa9, 0x8a, 0x87, 0x90, 0x9d, 
		0x06, 0x0b, 0x1c, 0x11, 0x32, 0x3f, 0x28, 0x25, 0x6e, 0x63, 0x74, 0x79, 0x5a, 0x57, 0x40, 0x4d, 
		0xda, 0xd7, 0xc0, 0xcd, 0xee, 0xe3, 0xf4, 0xf9, 0xb2, 0xbf, 0xa8, 0xa5, 0x86, 0x8b, 0x9c, 0x91, 
		0x0a, 0x07, 0x10, 0x1d, 0x3e, 0x33, 0x24, 0x29, 0x62, 0x6f, 0x78, 0x75, 0x56, 0x5b, 0x4c, 0x41, 
		0x61, 0x6c, 0x7b, 0x76, 0x55, 0x58, 0x4f, 0x42, 0x09, 0x04, 0x13, 0x1e, 0x3d, 0x30, 0x27, 0x2a, 
		0xb1, 0xbc, 0xab, 0xa6, 0x85, 0x88, 0x9f, 0x92, 0xd9, 0xd4, 0xc3, 0xce, 0xed, 0xe0, 0xf7, 0xfa, 
		0xb7, 0xba, 0xad, 0xa0, 0x83, 0x8e, 0x99, 0x94, 0xdf, 0xd2, 0xc5, 0xc8, 0xeb, 0xe6, 0xf1, 0xfc, 
		0x67, 0x6a, 0x7d, 0x70, 0x53, 0x5e, 0x49, 0x44, 0x0f, 0x02, 0x15, 0x18, 0x3b, 0x36, 0x21, 0x2c, 
		0x0c, 0x01, 0x16, 0x1b, 0x38, 0x35, 0x22, 0x2f, 0x64, 0x69, 0x7e, 0x73, 0x50, 0x5d, 0x4a, 0x47, 
		0xdc, 0xd1, 0xc6, 0xcb, 0xe8, 0xe5, 0xf2, 0xff, 0xb4, 0xb9, 0xae, 0xa3, 0x80, 0x8d, 0x9a, 0x97];
		private static const _XtimeE:Array = [
		0x00, 0x0e, 0x1c, 0x12, 0x38, 0x36, 0x24, 0x2a, 0x70, 0x7e, 0x6c, 0x62, 0x48, 0x46, 0x54, 0x5a, 
		0xe0, 0xee, 0xfc, 0xf2, 0xd8, 0xd6, 0xc4, 0xca, 0x90, 0x9e, 0x8c, 0x82, 0xa8, 0xa6, 0xb4, 0xba, 
		0xdb, 0xd5, 0xc7, 0xc9, 0xe3, 0xed, 0xff, 0xf1, 0xab, 0xa5, 0xb7, 0xb9, 0x93, 0x9d, 0x8f, 0x81, 
		0x3b, 0x35, 0x27, 0x29, 0x03, 0x0d, 0x1f, 0x11, 0x4b, 0x45, 0x57, 0x59, 0x73, 0x7d, 0x6f, 0x61, 
		0xad, 0xa3, 0xb1, 0xbf, 0x95, 0x9b, 0x89, 0x87, 0xdd, 0xd3, 0xc1, 0xcf, 0xe5, 0xeb, 0xf9, 0xf7, 
		0x4d, 0x43, 0x51, 0x5f, 0x75, 0x7b, 0x69, 0x67, 0x3d, 0x33, 0x21, 0x2f, 0x05, 0x0b, 0x19, 0x17, 
		0x76, 0x78, 0x6a, 0x64, 0x4e, 0x40, 0x52, 0x5c, 0x06, 0x08, 0x1a, 0x14, 0x3e, 0x30, 0x22, 0x2c, 
		0x96, 0x98, 0x8a, 0x84, 0xae, 0xa0, 0xb2, 0xbc, 0xe6, 0xe8, 0xfa, 0xf4, 0xde, 0xd0, 0xc2, 0xcc, 
		0x41, 0x4f, 0x5d, 0x53, 0x79, 0x77, 0x65, 0x6b, 0x31, 0x3f, 0x2d, 0x23, 0x09, 0x07, 0x15, 0x1b, 
		0xa1, 0xaf, 0xbd, 0xb3, 0x99, 0x97, 0x85, 0x8b, 0xd1, 0xdf, 0xcd, 0xc3, 0xe9, 0xe7, 0xf5, 0xfb, 
		0x9a, 0x94, 0x86, 0x88, 0xa2, 0xac, 0xbe, 0xb0, 0xea, 0xe4, 0xf6, 0xf8, 0xd2, 0xdc, 0xce, 0xc0, 
		0x7a, 0x74, 0x66, 0x68, 0x42, 0x4c, 0x5e, 0x50, 0x0a, 0x04, 0x16, 0x18, 0x32, 0x3c, 0x2e, 0x20, 
		0xec, 0xe2, 0xf0, 0xfe, 0xd4, 0xda, 0xc8, 0xc6, 0x9c, 0x92, 0x80, 0x8e, 0xa4, 0xaa, 0xb8, 0xb6, 
		0x0c, 0x02, 0x10, 0x1e, 0x34, 0x3a, 0x28, 0x26, 0x7c, 0x72, 0x60, 0x6e, 0x44, 0x4a, 0x58, 0x56, 
		0x37, 0x39, 0x2b, 0x25, 0x0f, 0x01, 0x13, 0x1d, 0x47, 0x49, 0x5b, 0x55, 0x7f, 0x71, 0x63, 0x6d, 
		0xd7, 0xd9, 0xcb, 0xc5, 0xef, 0xe1, 0xf3, 0xfd, 0xa7, 0xa9, 0xbb, 0xb5, 0x9f, 0x91, 0x83, 0x8d]; 
		static private var _Rcon:Array = [
		0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36];
		static private var Sbox:ByteArray;
		static private var InvSbox:ByteArray;
		static private var Xtime2Sbox:ByteArray;
		static private var Xtime3Sbox:ByteArray;
		static private var Xtime2:ByteArray;
		static private var Xtime9:ByteArray;
		static private var XtimeB:ByteArray;
		static private var XtimeD:ByteArray;
		static private var XtimeE:ByteArray;
		static private var Rcon:ByteArray;
		// static initializer
		{
			//var i:uint;
			Sbox = new ByteArray;
			InvSbox = new ByteArray;
			Xtime2Sbox = new ByteArray;
			Xtime3Sbox = new ByteArray;
			Xtime2 = new ByteArray;
			Xtime9 = new ByteArray;
			XtimeB = new ByteArray;
			XtimeD = new ByteArray;
			XtimeE = new ByteArray;
            /*
			for (i=0;i<256;i++) {
				Sbox[i] = _Sbox[i];
				InvSbox[i] = _InvSbox[i];
				Xtime2Sbox[i] = _Xtime2Sbox[i];
				Xtime3Sbox[i] = _Xtime3Sbox[i];
				Xtime2[i] = _Xtime2[i];
				Xtime9[i] = _Xtime9[i];
				XtimeB[i] = _XtimeB[i];
				XtimeD[i] = _XtimeD[i];
				XtimeE[i] = _XtimeE[i];
			}
            */
            Sbox[0] = _Sbox[0];
            InvSbox[0] = _InvSbox[0];
            Xtime2Sbox[0] = _Xtime2Sbox[0];
            Xtime3Sbox[0] = _Xtime3Sbox[0];
            Xtime2[0] = _Xtime2[0];
            Xtime9[0] = _Xtime9[0];
            XtimeB[0] = _XtimeB[0];
            XtimeD[0] = _XtimeD[0];
            XtimeE[0] = _XtimeE[0];
            Sbox[1] = _Sbox[1];
            InvSbox[1] = _InvSbox[1];
            Xtime2Sbox[1] = _Xtime2Sbox[1];
            Xtime3Sbox[1] = _Xtime3Sbox[1];
            Xtime2[1] = _Xtime2[1];
            Xtime9[1] = _Xtime9[1];
            XtimeB[1] = _XtimeB[1];
            XtimeD[1] = _XtimeD[1];
            XtimeE[1] = _XtimeE[1];
            Sbox[2] = _Sbox[2];
            InvSbox[2] = _InvSbox[2];
            Xtime2Sbox[2] = _Xtime2Sbox[2];
            Xtime3Sbox[2] = _Xtime3Sbox[2];
            Xtime2[2] = _Xtime2[2];
            Xtime9[2] = _Xtime9[2];
            XtimeB[2] = _XtimeB[2];
            XtimeD[2] = _XtimeD[2];
            XtimeE[2] = _XtimeE[2];
            Sbox[3] = _Sbox[3];
            InvSbox[3] = _InvSbox[3];
            Xtime2Sbox[3] = _Xtime2Sbox[3];
            Xtime3Sbox[3] = _Xtime3Sbox[3];
            Xtime2[3] = _Xtime2[3];
            Xtime9[3] = _Xtime9[3];
            XtimeB[3] = _XtimeB[3];
            XtimeD[3] = _XtimeD[3];
            XtimeE[3] = _XtimeE[3];
            Sbox[4] = _Sbox[4];
            InvSbox[4] = _InvSbox[4];
            Xtime2Sbox[4] = _Xtime2Sbox[4];
            Xtime3Sbox[4] = _Xtime3Sbox[4];
            Xtime2[4] = _Xtime2[4];
            Xtime9[4] = _Xtime9[4];
            XtimeB[4] = _XtimeB[4];
            XtimeD[4] = _XtimeD[4];
            XtimeE[4] = _XtimeE[4];
            Sbox[5] = _Sbox[5];
            InvSbox[5] = _InvSbox[5];
            Xtime2Sbox[5] = _Xtime2Sbox[5];
            Xtime3Sbox[5] = _Xtime3Sbox[5];
            Xtime2[5] = _Xtime2[5];
            Xtime9[5] = _Xtime9[5];
            XtimeB[5] = _XtimeB[5];
            XtimeD[5] = _XtimeD[5];
            XtimeE[5] = _XtimeE[5];
            Sbox[6] = _Sbox[6];
            InvSbox[6] = _InvSbox[6];
            Xtime2Sbox[6] = _Xtime2Sbox[6];
            Xtime3Sbox[6] = _Xtime3Sbox[6];
            Xtime2[6] = _Xtime2[6];
            Xtime9[6] = _Xtime9[6];
            XtimeB[6] = _XtimeB[6];
            XtimeD[6] = _XtimeD[6];
            XtimeE[6] = _XtimeE[6];
            Sbox[7] = _Sbox[7];
            InvSbox[7] = _InvSbox[7];
            Xtime2Sbox[7] = _Xtime2Sbox[7];
            Xtime3Sbox[7] = _Xtime3Sbox[7];
            Xtime2[7] = _Xtime2[7];
            Xtime9[7] = _Xtime9[7];
            XtimeB[7] = _XtimeB[7];
            XtimeD[7] = _XtimeD[7];
            XtimeE[7] = _XtimeE[7];
            Sbox[8] = _Sbox[8];
            InvSbox[8] = _InvSbox[8];
            Xtime2Sbox[8] = _Xtime2Sbox[8];
            Xtime3Sbox[8] = _Xtime3Sbox[8];
            Xtime2[8] = _Xtime2[8];
            Xtime9[8] = _Xtime9[8];
            XtimeB[8] = _XtimeB[8];
            XtimeD[8] = _XtimeD[8];
            XtimeE[8] = _XtimeE[8];
            Sbox[9] = _Sbox[9];
            InvSbox[9] = _InvSbox[9];
            Xtime2Sbox[9] = _Xtime2Sbox[9];
            Xtime3Sbox[9] = _Xtime3Sbox[9];
            Xtime2[9] = _Xtime2[9];
            Xtime9[9] = _Xtime9[9];
            XtimeB[9] = _XtimeB[9];
            XtimeD[9] = _XtimeD[9];
            XtimeE[9] = _XtimeE[9];
            Sbox[10] = _Sbox[10];
            InvSbox[10] = _InvSbox[10];
            Xtime2Sbox[10] = _Xtime2Sbox[10];
            Xtime3Sbox[10] = _Xtime3Sbox[10];
            Xtime2[10] = _Xtime2[10];
            Xtime9[10] = _Xtime9[10];
            XtimeB[10] = _XtimeB[10];
            XtimeD[10] = _XtimeD[10];
            XtimeE[10] = _XtimeE[10];
            Sbox[11] = _Sbox[11];
            InvSbox[11] = _InvSbox[11];
            Xtime2Sbox[11] = _Xtime2Sbox[11];
            Xtime3Sbox[11] = _Xtime3Sbox[11];
            Xtime2[11] = _Xtime2[11];
            Xtime9[11] = _Xtime9[11];
            XtimeB[11] = _XtimeB[11];
            XtimeD[11] = _XtimeD[11];
            XtimeE[11] = _XtimeE[11];
            Sbox[12] = _Sbox[12];
            InvSbox[12] = _InvSbox[12];
            Xtime2Sbox[12] = _Xtime2Sbox[12];
            Xtime3Sbox[12] = _Xtime3Sbox[12];
            Xtime2[12] = _Xtime2[12];
            Xtime9[12] = _Xtime9[12];
            XtimeB[12] = _XtimeB[12];
            XtimeD[12] = _XtimeD[12];
            XtimeE[12] = _XtimeE[12];
            Sbox[13] = _Sbox[13];
            InvSbox[13] = _InvSbox[13];
            Xtime2Sbox[13] = _Xtime2Sbox[13];
            Xtime3Sbox[13] = _Xtime3Sbox[13];
            Xtime2[13] = _Xtime2[13];
            Xtime9[13] = _Xtime9[13];
            XtimeB[13] = _XtimeB[13];
            XtimeD[13] = _XtimeD[13];
            XtimeE[13] = _XtimeE[13];
            Sbox[14] = _Sbox[14];
            InvSbox[14] = _InvSbox[14];
            Xtime2Sbox[14] = _Xtime2Sbox[14];
            Xtime3Sbox[14] = _Xtime3Sbox[14];
            Xtime2[14] = _Xtime2[14];
            Xtime9[14] = _Xtime9[14];
            XtimeB[14] = _XtimeB[14];
            XtimeD[14] = _XtimeD[14];
            XtimeE[14] = _XtimeE[14];
            Sbox[15] = _Sbox[15];
            InvSbox[15] = _InvSbox[15];
            Xtime2Sbox[15] = _Xtime2Sbox[15];
            Xtime3Sbox[15] = _Xtime3Sbox[15];
            Xtime2[15] = _Xtime2[15];
            Xtime9[15] = _Xtime9[15];
            XtimeB[15] = _XtimeB[15];
            XtimeD[15] = _XtimeD[15];
            XtimeE[15] = _XtimeE[15];
            Sbox[16] = _Sbox[16];
            InvSbox[16] = _InvSbox[16];
            Xtime2Sbox[16] = _Xtime2Sbox[16];
            Xtime3Sbox[16] = _Xtime3Sbox[16];
            Xtime2[16] = _Xtime2[16];
            Xtime9[16] = _Xtime9[16];
            XtimeB[16] = _XtimeB[16];
            XtimeD[16] = _XtimeD[16];
            XtimeE[16] = _XtimeE[16];
            Sbox[17] = _Sbox[17];
            InvSbox[17] = _InvSbox[17];
            Xtime2Sbox[17] = _Xtime2Sbox[17];
            Xtime3Sbox[17] = _Xtime3Sbox[17];
            Xtime2[17] = _Xtime2[17];
            Xtime9[17] = _Xtime9[17];
            XtimeB[17] = _XtimeB[17];
            XtimeD[17] = _XtimeD[17];
            XtimeE[17] = _XtimeE[17];
            Sbox[18] = _Sbox[18];
            InvSbox[18] = _InvSbox[18];
            Xtime2Sbox[18] = _Xtime2Sbox[18];
            Xtime3Sbox[18] = _Xtime3Sbox[18];
            Xtime2[18] = _Xtime2[18];
            Xtime9[18] = _Xtime9[18];
            XtimeB[18] = _XtimeB[18];
            XtimeD[18] = _XtimeD[18];
            XtimeE[18] = _XtimeE[18];
            Sbox[19] = _Sbox[19];
            InvSbox[19] = _InvSbox[19];
            Xtime2Sbox[19] = _Xtime2Sbox[19];
            Xtime3Sbox[19] = _Xtime3Sbox[19];
            Xtime2[19] = _Xtime2[19];
            Xtime9[19] = _Xtime9[19];
            XtimeB[19] = _XtimeB[19];
            XtimeD[19] = _XtimeD[19];
            XtimeE[19] = _XtimeE[19];
            Sbox[20] = _Sbox[20];
            InvSbox[20] = _InvSbox[20];
            Xtime2Sbox[20] = _Xtime2Sbox[20];
            Xtime3Sbox[20] = _Xtime3Sbox[20];
            Xtime2[20] = _Xtime2[20];
            Xtime9[20] = _Xtime9[20];
            XtimeB[20] = _XtimeB[20];
            XtimeD[20] = _XtimeD[20];
            XtimeE[20] = _XtimeE[20];
            Sbox[21] = _Sbox[21];
            InvSbox[21] = _InvSbox[21];
            Xtime2Sbox[21] = _Xtime2Sbox[21];
            Xtime3Sbox[21] = _Xtime3Sbox[21];
            Xtime2[21] = _Xtime2[21];
            Xtime9[21] = _Xtime9[21];
            XtimeB[21] = _XtimeB[21];
            XtimeD[21] = _XtimeD[21];
            XtimeE[21] = _XtimeE[21];
            Sbox[22] = _Sbox[22];
            InvSbox[22] = _InvSbox[22];
            Xtime2Sbox[22] = _Xtime2Sbox[22];
            Xtime3Sbox[22] = _Xtime3Sbox[22];
            Xtime2[22] = _Xtime2[22];
            Xtime9[22] = _Xtime9[22];
            XtimeB[22] = _XtimeB[22];
            XtimeD[22] = _XtimeD[22];
            XtimeE[22] = _XtimeE[22];
            Sbox[23] = _Sbox[23];
            InvSbox[23] = _InvSbox[23];
            Xtime2Sbox[23] = _Xtime2Sbox[23];
            Xtime3Sbox[23] = _Xtime3Sbox[23];
            Xtime2[23] = _Xtime2[23];
            Xtime9[23] = _Xtime9[23];
            XtimeB[23] = _XtimeB[23];
            XtimeD[23] = _XtimeD[23];
            XtimeE[23] = _XtimeE[23];
            Sbox[24] = _Sbox[24];
            InvSbox[24] = _InvSbox[24];
            Xtime2Sbox[24] = _Xtime2Sbox[24];
            Xtime3Sbox[24] = _Xtime3Sbox[24];
            Xtime2[24] = _Xtime2[24];
            Xtime9[24] = _Xtime9[24];
            XtimeB[24] = _XtimeB[24];
            XtimeD[24] = _XtimeD[24];
            XtimeE[24] = _XtimeE[24];
            Sbox[25] = _Sbox[25];
            InvSbox[25] = _InvSbox[25];
            Xtime2Sbox[25] = _Xtime2Sbox[25];
            Xtime3Sbox[25] = _Xtime3Sbox[25];
            Xtime2[25] = _Xtime2[25];
            Xtime9[25] = _Xtime9[25];
            XtimeB[25] = _XtimeB[25];
            XtimeD[25] = _XtimeD[25];
            XtimeE[25] = _XtimeE[25];
            Sbox[26] = _Sbox[26];
            InvSbox[26] = _InvSbox[26];
            Xtime2Sbox[26] = _Xtime2Sbox[26];
            Xtime3Sbox[26] = _Xtime3Sbox[26];
            Xtime2[26] = _Xtime2[26];
            Xtime9[26] = _Xtime9[26];
            XtimeB[26] = _XtimeB[26];
            XtimeD[26] = _XtimeD[26];
            XtimeE[26] = _XtimeE[26];
            Sbox[27] = _Sbox[27];
            InvSbox[27] = _InvSbox[27];
            Xtime2Sbox[27] = _Xtime2Sbox[27];
            Xtime3Sbox[27] = _Xtime3Sbox[27];
            Xtime2[27] = _Xtime2[27];
            Xtime9[27] = _Xtime9[27];
            XtimeB[27] = _XtimeB[27];
            XtimeD[27] = _XtimeD[27];
            XtimeE[27] = _XtimeE[27];
            Sbox[28] = _Sbox[28];
            InvSbox[28] = _InvSbox[28];
            Xtime2Sbox[28] = _Xtime2Sbox[28];
            Xtime3Sbox[28] = _Xtime3Sbox[28];
            Xtime2[28] = _Xtime2[28];
            Xtime9[28] = _Xtime9[28];
            XtimeB[28] = _XtimeB[28];
            XtimeD[28] = _XtimeD[28];
            XtimeE[28] = _XtimeE[28];
            Sbox[29] = _Sbox[29];
            InvSbox[29] = _InvSbox[29];
            Xtime2Sbox[29] = _Xtime2Sbox[29];
            Xtime3Sbox[29] = _Xtime3Sbox[29];
            Xtime2[29] = _Xtime2[29];
            Xtime9[29] = _Xtime9[29];
            XtimeB[29] = _XtimeB[29];
            XtimeD[29] = _XtimeD[29];
            XtimeE[29] = _XtimeE[29];
            Sbox[30] = _Sbox[30];
            InvSbox[30] = _InvSbox[30];
            Xtime2Sbox[30] = _Xtime2Sbox[30];
            Xtime3Sbox[30] = _Xtime3Sbox[30];
            Xtime2[30] = _Xtime2[30];
            Xtime9[30] = _Xtime9[30];
            XtimeB[30] = _XtimeB[30];
            XtimeD[30] = _XtimeD[30];
            XtimeE[30] = _XtimeE[30];
            Sbox[31] = _Sbox[31];
            InvSbox[31] = _InvSbox[31];
            Xtime2Sbox[31] = _Xtime2Sbox[31];
            Xtime3Sbox[31] = _Xtime3Sbox[31];
            Xtime2[31] = _Xtime2[31];
            Xtime9[31] = _Xtime9[31];
            XtimeB[31] = _XtimeB[31];
            XtimeD[31] = _XtimeD[31];
            XtimeE[31] = _XtimeE[31];
            Sbox[32] = _Sbox[32];
            InvSbox[32] = _InvSbox[32];
            Xtime2Sbox[32] = _Xtime2Sbox[32];
            Xtime3Sbox[32] = _Xtime3Sbox[32];
            Xtime2[32] = _Xtime2[32];
            Xtime9[32] = _Xtime9[32];
            XtimeB[32] = _XtimeB[32];
            XtimeD[32] = _XtimeD[32];
            XtimeE[32] = _XtimeE[32];
            Sbox[33] = _Sbox[33];
            InvSbox[33] = _InvSbox[33];
            Xtime2Sbox[33] = _Xtime2Sbox[33];
            Xtime3Sbox[33] = _Xtime3Sbox[33];
            Xtime2[33] = _Xtime2[33];
            Xtime9[33] = _Xtime9[33];
            XtimeB[33] = _XtimeB[33];
            XtimeD[33] = _XtimeD[33];
            XtimeE[33] = _XtimeE[33];
            Sbox[34] = _Sbox[34];
            InvSbox[34] = _InvSbox[34];
            Xtime2Sbox[34] = _Xtime2Sbox[34];
            Xtime3Sbox[34] = _Xtime3Sbox[34];
            Xtime2[34] = _Xtime2[34];
            Xtime9[34] = _Xtime9[34];
            XtimeB[34] = _XtimeB[34];
            XtimeD[34] = _XtimeD[34];
            XtimeE[34] = _XtimeE[34];
            Sbox[35] = _Sbox[35];
            InvSbox[35] = _InvSbox[35];
            Xtime2Sbox[35] = _Xtime2Sbox[35];
            Xtime3Sbox[35] = _Xtime3Sbox[35];
            Xtime2[35] = _Xtime2[35];
            Xtime9[35] = _Xtime9[35];
            XtimeB[35] = _XtimeB[35];
            XtimeD[35] = _XtimeD[35];
            XtimeE[35] = _XtimeE[35];
            Sbox[36] = _Sbox[36];
            InvSbox[36] = _InvSbox[36];
            Xtime2Sbox[36] = _Xtime2Sbox[36];
            Xtime3Sbox[36] = _Xtime3Sbox[36];
            Xtime2[36] = _Xtime2[36];
            Xtime9[36] = _Xtime9[36];
            XtimeB[36] = _XtimeB[36];
            XtimeD[36] = _XtimeD[36];
            XtimeE[36] = _XtimeE[36];
            Sbox[37] = _Sbox[37];
            InvSbox[37] = _InvSbox[37];
            Xtime2Sbox[37] = _Xtime2Sbox[37];
            Xtime3Sbox[37] = _Xtime3Sbox[37];
            Xtime2[37] = _Xtime2[37];
            Xtime9[37] = _Xtime9[37];
            XtimeB[37] = _XtimeB[37];
            XtimeD[37] = _XtimeD[37];
            XtimeE[37] = _XtimeE[37];
            Sbox[38] = _Sbox[38];
            InvSbox[38] = _InvSbox[38];
            Xtime2Sbox[38] = _Xtime2Sbox[38];
            Xtime3Sbox[38] = _Xtime3Sbox[38];
            Xtime2[38] = _Xtime2[38];
            Xtime9[38] = _Xtime9[38];
            XtimeB[38] = _XtimeB[38];
            XtimeD[38] = _XtimeD[38];
            XtimeE[38] = _XtimeE[38];
            Sbox[39] = _Sbox[39];
            InvSbox[39] = _InvSbox[39];
            Xtime2Sbox[39] = _Xtime2Sbox[39];
            Xtime3Sbox[39] = _Xtime3Sbox[39];
            Xtime2[39] = _Xtime2[39];
            Xtime9[39] = _Xtime9[39];
            XtimeB[39] = _XtimeB[39];
            XtimeD[39] = _XtimeD[39];
            XtimeE[39] = _XtimeE[39];
            Sbox[40] = _Sbox[40];
            InvSbox[40] = _InvSbox[40];
            Xtime2Sbox[40] = _Xtime2Sbox[40];
            Xtime3Sbox[40] = _Xtime3Sbox[40];
            Xtime2[40] = _Xtime2[40];
            Xtime9[40] = _Xtime9[40];
            XtimeB[40] = _XtimeB[40];
            XtimeD[40] = _XtimeD[40];
            XtimeE[40] = _XtimeE[40];
            Sbox[41] = _Sbox[41];
            InvSbox[41] = _InvSbox[41];
            Xtime2Sbox[41] = _Xtime2Sbox[41];
            Xtime3Sbox[41] = _Xtime3Sbox[41];
            Xtime2[41] = _Xtime2[41];
            Xtime9[41] = _Xtime9[41];
            XtimeB[41] = _XtimeB[41];
            XtimeD[41] = _XtimeD[41];
            XtimeE[41] = _XtimeE[41];
            Sbox[42] = _Sbox[42];
            InvSbox[42] = _InvSbox[42];
            Xtime2Sbox[42] = _Xtime2Sbox[42];
            Xtime3Sbox[42] = _Xtime3Sbox[42];
            Xtime2[42] = _Xtime2[42];
            Xtime9[42] = _Xtime9[42];
            XtimeB[42] = _XtimeB[42];
            XtimeD[42] = _XtimeD[42];
            XtimeE[42] = _XtimeE[42];
            Sbox[43] = _Sbox[43];
            InvSbox[43] = _InvSbox[43];
            Xtime2Sbox[43] = _Xtime2Sbox[43];
            Xtime3Sbox[43] = _Xtime3Sbox[43];
            Xtime2[43] = _Xtime2[43];
            Xtime9[43] = _Xtime9[43];
            XtimeB[43] = _XtimeB[43];
            XtimeD[43] = _XtimeD[43];
            XtimeE[43] = _XtimeE[43];
            Sbox[44] = _Sbox[44];
            InvSbox[44] = _InvSbox[44];
            Xtime2Sbox[44] = _Xtime2Sbox[44];
            Xtime3Sbox[44] = _Xtime3Sbox[44];
            Xtime2[44] = _Xtime2[44];
            Xtime9[44] = _Xtime9[44];
            XtimeB[44] = _XtimeB[44];
            XtimeD[44] = _XtimeD[44];
            XtimeE[44] = _XtimeE[44];
            Sbox[45] = _Sbox[45];
            InvSbox[45] = _InvSbox[45];
            Xtime2Sbox[45] = _Xtime2Sbox[45];
            Xtime3Sbox[45] = _Xtime3Sbox[45];
            Xtime2[45] = _Xtime2[45];
            Xtime9[45] = _Xtime9[45];
            XtimeB[45] = _XtimeB[45];
            XtimeD[45] = _XtimeD[45];
            XtimeE[45] = _XtimeE[45];
            Sbox[46] = _Sbox[46];
            InvSbox[46] = _InvSbox[46];
            Xtime2Sbox[46] = _Xtime2Sbox[46];
            Xtime3Sbox[46] = _Xtime3Sbox[46];
            Xtime2[46] = _Xtime2[46];
            Xtime9[46] = _Xtime9[46];
            XtimeB[46] = _XtimeB[46];
            XtimeD[46] = _XtimeD[46];
            XtimeE[46] = _XtimeE[46];
            Sbox[47] = _Sbox[47];
            InvSbox[47] = _InvSbox[47];
            Xtime2Sbox[47] = _Xtime2Sbox[47];
            Xtime3Sbox[47] = _Xtime3Sbox[47];
            Xtime2[47] = _Xtime2[47];
            Xtime9[47] = _Xtime9[47];
            XtimeB[47] = _XtimeB[47];
            XtimeD[47] = _XtimeD[47];
            XtimeE[47] = _XtimeE[47];
            Sbox[48] = _Sbox[48];
            InvSbox[48] = _InvSbox[48];
            Xtime2Sbox[48] = _Xtime2Sbox[48];
            Xtime3Sbox[48] = _Xtime3Sbox[48];
            Xtime2[48] = _Xtime2[48];
            Xtime9[48] = _Xtime9[48];
            XtimeB[48] = _XtimeB[48];
            XtimeD[48] = _XtimeD[48];
            XtimeE[48] = _XtimeE[48];
            Sbox[49] = _Sbox[49];
            InvSbox[49] = _InvSbox[49];
            Xtime2Sbox[49] = _Xtime2Sbox[49];
            Xtime3Sbox[49] = _Xtime3Sbox[49];
            Xtime2[49] = _Xtime2[49];
            Xtime9[49] = _Xtime9[49];
            XtimeB[49] = _XtimeB[49];
            XtimeD[49] = _XtimeD[49];
            XtimeE[49] = _XtimeE[49];
            Sbox[50] = _Sbox[50];
            InvSbox[50] = _InvSbox[50];
            Xtime2Sbox[50] = _Xtime2Sbox[50];
            Xtime3Sbox[50] = _Xtime3Sbox[50];
            Xtime2[50] = _Xtime2[50];
            Xtime9[50] = _Xtime9[50];
            XtimeB[50] = _XtimeB[50];
            XtimeD[50] = _XtimeD[50];
            XtimeE[50] = _XtimeE[50];
            Sbox[51] = _Sbox[51];
            InvSbox[51] = _InvSbox[51];
            Xtime2Sbox[51] = _Xtime2Sbox[51];
            Xtime3Sbox[51] = _Xtime3Sbox[51];
            Xtime2[51] = _Xtime2[51];
            Xtime9[51] = _Xtime9[51];
            XtimeB[51] = _XtimeB[51];
            XtimeD[51] = _XtimeD[51];
            XtimeE[51] = _XtimeE[51];
            Sbox[52] = _Sbox[52];
            InvSbox[52] = _InvSbox[52];
            Xtime2Sbox[52] = _Xtime2Sbox[52];
            Xtime3Sbox[52] = _Xtime3Sbox[52];
            Xtime2[52] = _Xtime2[52];
            Xtime9[52] = _Xtime9[52];
            XtimeB[52] = _XtimeB[52];
            XtimeD[52] = _XtimeD[52];
            XtimeE[52] = _XtimeE[52];
            Sbox[53] = _Sbox[53];
            InvSbox[53] = _InvSbox[53];
            Xtime2Sbox[53] = _Xtime2Sbox[53];
            Xtime3Sbox[53] = _Xtime3Sbox[53];
            Xtime2[53] = _Xtime2[53];
            Xtime9[53] = _Xtime9[53];
            XtimeB[53] = _XtimeB[53];
            XtimeD[53] = _XtimeD[53];
            XtimeE[53] = _XtimeE[53];
            Sbox[54] = _Sbox[54];
            InvSbox[54] = _InvSbox[54];
            Xtime2Sbox[54] = _Xtime2Sbox[54];
            Xtime3Sbox[54] = _Xtime3Sbox[54];
            Xtime2[54] = _Xtime2[54];
            Xtime9[54] = _Xtime9[54];
            XtimeB[54] = _XtimeB[54];
            XtimeD[54] = _XtimeD[54];
            XtimeE[54] = _XtimeE[54];
            Sbox[55] = _Sbox[55];
            InvSbox[55] = _InvSbox[55];
            Xtime2Sbox[55] = _Xtime2Sbox[55];
            Xtime3Sbox[55] = _Xtime3Sbox[55];
            Xtime2[55] = _Xtime2[55];
            Xtime9[55] = _Xtime9[55];
            XtimeB[55] = _XtimeB[55];
            XtimeD[55] = _XtimeD[55];
            XtimeE[55] = _XtimeE[55];
            Sbox[56] = _Sbox[56];
            InvSbox[56] = _InvSbox[56];
            Xtime2Sbox[56] = _Xtime2Sbox[56];
            Xtime3Sbox[56] = _Xtime3Sbox[56];
            Xtime2[56] = _Xtime2[56];
            Xtime9[56] = _Xtime9[56];
            XtimeB[56] = _XtimeB[56];
            XtimeD[56] = _XtimeD[56];
            XtimeE[56] = _XtimeE[56];
            Sbox[57] = _Sbox[57];
            InvSbox[57] = _InvSbox[57];
            Xtime2Sbox[57] = _Xtime2Sbox[57];
            Xtime3Sbox[57] = _Xtime3Sbox[57];
            Xtime2[57] = _Xtime2[57];
            Xtime9[57] = _Xtime9[57];
            XtimeB[57] = _XtimeB[57];
            XtimeD[57] = _XtimeD[57];
            XtimeE[57] = _XtimeE[57];
            Sbox[58] = _Sbox[58];
            InvSbox[58] = _InvSbox[58];
            Xtime2Sbox[58] = _Xtime2Sbox[58];
            Xtime3Sbox[58] = _Xtime3Sbox[58];
            Xtime2[58] = _Xtime2[58];
            Xtime9[58] = _Xtime9[58];
            XtimeB[58] = _XtimeB[58];
            XtimeD[58] = _XtimeD[58];
            XtimeE[58] = _XtimeE[58];
            Sbox[59] = _Sbox[59];
            InvSbox[59] = _InvSbox[59];
            Xtime2Sbox[59] = _Xtime2Sbox[59];
            Xtime3Sbox[59] = _Xtime3Sbox[59];
            Xtime2[59] = _Xtime2[59];
            Xtime9[59] = _Xtime9[59];
            XtimeB[59] = _XtimeB[59];
            XtimeD[59] = _XtimeD[59];
            XtimeE[59] = _XtimeE[59];
            Sbox[60] = _Sbox[60];
            InvSbox[60] = _InvSbox[60];
            Xtime2Sbox[60] = _Xtime2Sbox[60];
            Xtime3Sbox[60] = _Xtime3Sbox[60];
            Xtime2[60] = _Xtime2[60];
            Xtime9[60] = _Xtime9[60];
            XtimeB[60] = _XtimeB[60];
            XtimeD[60] = _XtimeD[60];
            XtimeE[60] = _XtimeE[60];
            Sbox[61] = _Sbox[61];
            InvSbox[61] = _InvSbox[61];
            Xtime2Sbox[61] = _Xtime2Sbox[61];
            Xtime3Sbox[61] = _Xtime3Sbox[61];
            Xtime2[61] = _Xtime2[61];
            Xtime9[61] = _Xtime9[61];
            XtimeB[61] = _XtimeB[61];
            XtimeD[61] = _XtimeD[61];
            XtimeE[61] = _XtimeE[61];
            Sbox[62] = _Sbox[62];
            InvSbox[62] = _InvSbox[62];
            Xtime2Sbox[62] = _Xtime2Sbox[62];
            Xtime3Sbox[62] = _Xtime3Sbox[62];
            Xtime2[62] = _Xtime2[62];
            Xtime9[62] = _Xtime9[62];
            XtimeB[62] = _XtimeB[62];
            XtimeD[62] = _XtimeD[62];
            XtimeE[62] = _XtimeE[62];
            Sbox[63] = _Sbox[63];
            InvSbox[63] = _InvSbox[63];
            Xtime2Sbox[63] = _Xtime2Sbox[63];
            Xtime3Sbox[63] = _Xtime3Sbox[63];
            Xtime2[63] = _Xtime2[63];
            Xtime9[63] = _Xtime9[63];
            XtimeB[63] = _XtimeB[63];
            XtimeD[63] = _XtimeD[63];
            XtimeE[63] = _XtimeE[63];
            Sbox[64] = _Sbox[64];
            InvSbox[64] = _InvSbox[64];
            Xtime2Sbox[64] = _Xtime2Sbox[64];
            Xtime3Sbox[64] = _Xtime3Sbox[64];
            Xtime2[64] = _Xtime2[64];
            Xtime9[64] = _Xtime9[64];
            XtimeB[64] = _XtimeB[64];
            XtimeD[64] = _XtimeD[64];
            XtimeE[64] = _XtimeE[64];
            Sbox[65] = _Sbox[65];
            InvSbox[65] = _InvSbox[65];
            Xtime2Sbox[65] = _Xtime2Sbox[65];
            Xtime3Sbox[65] = _Xtime3Sbox[65];
            Xtime2[65] = _Xtime2[65];
            Xtime9[65] = _Xtime9[65];
            XtimeB[65] = _XtimeB[65];
            XtimeD[65] = _XtimeD[65];
            XtimeE[65] = _XtimeE[65];
            Sbox[66] = _Sbox[66];
            InvSbox[66] = _InvSbox[66];
            Xtime2Sbox[66] = _Xtime2Sbox[66];
            Xtime3Sbox[66] = _Xtime3Sbox[66];
            Xtime2[66] = _Xtime2[66];
            Xtime9[66] = _Xtime9[66];
            XtimeB[66] = _XtimeB[66];
            XtimeD[66] = _XtimeD[66];
            XtimeE[66] = _XtimeE[66];
            Sbox[67] = _Sbox[67];
            InvSbox[67] = _InvSbox[67];
            Xtime2Sbox[67] = _Xtime2Sbox[67];
            Xtime3Sbox[67] = _Xtime3Sbox[67];
            Xtime2[67] = _Xtime2[67];
            Xtime9[67] = _Xtime9[67];
            XtimeB[67] = _XtimeB[67];
            XtimeD[67] = _XtimeD[67];
            XtimeE[67] = _XtimeE[67];
            Sbox[68] = _Sbox[68];
            InvSbox[68] = _InvSbox[68];
            Xtime2Sbox[68] = _Xtime2Sbox[68];
            Xtime3Sbox[68] = _Xtime3Sbox[68];
            Xtime2[68] = _Xtime2[68];
            Xtime9[68] = _Xtime9[68];
            XtimeB[68] = _XtimeB[68];
            XtimeD[68] = _XtimeD[68];
            XtimeE[68] = _XtimeE[68];
            Sbox[69] = _Sbox[69];
            InvSbox[69] = _InvSbox[69];
            Xtime2Sbox[69] = _Xtime2Sbox[69];
            Xtime3Sbox[69] = _Xtime3Sbox[69];
            Xtime2[69] = _Xtime2[69];
            Xtime9[69] = _Xtime9[69];
            XtimeB[69] = _XtimeB[69];
            XtimeD[69] = _XtimeD[69];
            XtimeE[69] = _XtimeE[69];
            Sbox[70] = _Sbox[70];
            InvSbox[70] = _InvSbox[70];
            Xtime2Sbox[70] = _Xtime2Sbox[70];
            Xtime3Sbox[70] = _Xtime3Sbox[70];
            Xtime2[70] = _Xtime2[70];
            Xtime9[70] = _Xtime9[70];
            XtimeB[70] = _XtimeB[70];
            XtimeD[70] = _XtimeD[70];
            XtimeE[70] = _XtimeE[70];
            Sbox[71] = _Sbox[71];
            InvSbox[71] = _InvSbox[71];
            Xtime2Sbox[71] = _Xtime2Sbox[71];
            Xtime3Sbox[71] = _Xtime3Sbox[71];
            Xtime2[71] = _Xtime2[71];
            Xtime9[71] = _Xtime9[71];
            XtimeB[71] = _XtimeB[71];
            XtimeD[71] = _XtimeD[71];
            XtimeE[71] = _XtimeE[71];
            Sbox[72] = _Sbox[72];
            InvSbox[72] = _InvSbox[72];
            Xtime2Sbox[72] = _Xtime2Sbox[72];
            Xtime3Sbox[72] = _Xtime3Sbox[72];
            Xtime2[72] = _Xtime2[72];
            Xtime9[72] = _Xtime9[72];
            XtimeB[72] = _XtimeB[72];
            XtimeD[72] = _XtimeD[72];
            XtimeE[72] = _XtimeE[72];
            Sbox[73] = _Sbox[73];
            InvSbox[73] = _InvSbox[73];
            Xtime2Sbox[73] = _Xtime2Sbox[73];
            Xtime3Sbox[73] = _Xtime3Sbox[73];
            Xtime2[73] = _Xtime2[73];
            Xtime9[73] = _Xtime9[73];
            XtimeB[73] = _XtimeB[73];
            XtimeD[73] = _XtimeD[73];
            XtimeE[73] = _XtimeE[73];
            Sbox[74] = _Sbox[74];
            InvSbox[74] = _InvSbox[74];
            Xtime2Sbox[74] = _Xtime2Sbox[74];
            Xtime3Sbox[74] = _Xtime3Sbox[74];
            Xtime2[74] = _Xtime2[74];
            Xtime9[74] = _Xtime9[74];
            XtimeB[74] = _XtimeB[74];
            XtimeD[74] = _XtimeD[74];
            XtimeE[74] = _XtimeE[74];
            Sbox[75] = _Sbox[75];
            InvSbox[75] = _InvSbox[75];
            Xtime2Sbox[75] = _Xtime2Sbox[75];
            Xtime3Sbox[75] = _Xtime3Sbox[75];
            Xtime2[75] = _Xtime2[75];
            Xtime9[75] = _Xtime9[75];
            XtimeB[75] = _XtimeB[75];
            XtimeD[75] = _XtimeD[75];
            XtimeE[75] = _XtimeE[75];
            Sbox[76] = _Sbox[76];
            InvSbox[76] = _InvSbox[76];
            Xtime2Sbox[76] = _Xtime2Sbox[76];
            Xtime3Sbox[76] = _Xtime3Sbox[76];
            Xtime2[76] = _Xtime2[76];
            Xtime9[76] = _Xtime9[76];
            XtimeB[76] = _XtimeB[76];
            XtimeD[76] = _XtimeD[76];
            XtimeE[76] = _XtimeE[76];
            Sbox[77] = _Sbox[77];
            InvSbox[77] = _InvSbox[77];
            Xtime2Sbox[77] = _Xtime2Sbox[77];
            Xtime3Sbox[77] = _Xtime3Sbox[77];
            Xtime2[77] = _Xtime2[77];
            Xtime9[77] = _Xtime9[77];
            XtimeB[77] = _XtimeB[77];
            XtimeD[77] = _XtimeD[77];
            XtimeE[77] = _XtimeE[77];
            Sbox[78] = _Sbox[78];
            InvSbox[78] = _InvSbox[78];
            Xtime2Sbox[78] = _Xtime2Sbox[78];
            Xtime3Sbox[78] = _Xtime3Sbox[78];
            Xtime2[78] = _Xtime2[78];
            Xtime9[78] = _Xtime9[78];
            XtimeB[78] = _XtimeB[78];
            XtimeD[78] = _XtimeD[78];
            XtimeE[78] = _XtimeE[78];
            Sbox[79] = _Sbox[79];
            InvSbox[79] = _InvSbox[79];
            Xtime2Sbox[79] = _Xtime2Sbox[79];
            Xtime3Sbox[79] = _Xtime3Sbox[79];
            Xtime2[79] = _Xtime2[79];
            Xtime9[79] = _Xtime9[79];
            XtimeB[79] = _XtimeB[79];
            XtimeD[79] = _XtimeD[79];
            XtimeE[79] = _XtimeE[79];
            Sbox[80] = _Sbox[80];
            InvSbox[80] = _InvSbox[80];
            Xtime2Sbox[80] = _Xtime2Sbox[80];
            Xtime3Sbox[80] = _Xtime3Sbox[80];
            Xtime2[80] = _Xtime2[80];
            Xtime9[80] = _Xtime9[80];
            XtimeB[80] = _XtimeB[80];
            XtimeD[80] = _XtimeD[80];
            XtimeE[80] = _XtimeE[80];
            Sbox[81] = _Sbox[81];
            InvSbox[81] = _InvSbox[81];
            Xtime2Sbox[81] = _Xtime2Sbox[81];
            Xtime3Sbox[81] = _Xtime3Sbox[81];
            Xtime2[81] = _Xtime2[81];
            Xtime9[81] = _Xtime9[81];
            XtimeB[81] = _XtimeB[81];
            XtimeD[81] = _XtimeD[81];
            XtimeE[81] = _XtimeE[81];
            Sbox[82] = _Sbox[82];
            InvSbox[82] = _InvSbox[82];
            Xtime2Sbox[82] = _Xtime2Sbox[82];
            Xtime3Sbox[82] = _Xtime3Sbox[82];
            Xtime2[82] = _Xtime2[82];
            Xtime9[82] = _Xtime9[82];
            XtimeB[82] = _XtimeB[82];
            XtimeD[82] = _XtimeD[82];
            XtimeE[82] = _XtimeE[82];
            Sbox[83] = _Sbox[83];
            InvSbox[83] = _InvSbox[83];
            Xtime2Sbox[83] = _Xtime2Sbox[83];
            Xtime3Sbox[83] = _Xtime3Sbox[83];
            Xtime2[83] = _Xtime2[83];
            Xtime9[83] = _Xtime9[83];
            XtimeB[83] = _XtimeB[83];
            XtimeD[83] = _XtimeD[83];
            XtimeE[83] = _XtimeE[83];
            Sbox[84] = _Sbox[84];
            InvSbox[84] = _InvSbox[84];
            Xtime2Sbox[84] = _Xtime2Sbox[84];
            Xtime3Sbox[84] = _Xtime3Sbox[84];
            Xtime2[84] = _Xtime2[84];
            Xtime9[84] = _Xtime9[84];
            XtimeB[84] = _XtimeB[84];
            XtimeD[84] = _XtimeD[84];
            XtimeE[84] = _XtimeE[84];
            Sbox[85] = _Sbox[85];
            InvSbox[85] = _InvSbox[85];
            Xtime2Sbox[85] = _Xtime2Sbox[85];
            Xtime3Sbox[85] = _Xtime3Sbox[85];
            Xtime2[85] = _Xtime2[85];
            Xtime9[85] = _Xtime9[85];
            XtimeB[85] = _XtimeB[85];
            XtimeD[85] = _XtimeD[85];
            XtimeE[85] = _XtimeE[85];
            Sbox[86] = _Sbox[86];
            InvSbox[86] = _InvSbox[86];
            Xtime2Sbox[86] = _Xtime2Sbox[86];
            Xtime3Sbox[86] = _Xtime3Sbox[86];
            Xtime2[86] = _Xtime2[86];
            Xtime9[86] = _Xtime9[86];
            XtimeB[86] = _XtimeB[86];
            XtimeD[86] = _XtimeD[86];
            XtimeE[86] = _XtimeE[86];
            Sbox[87] = _Sbox[87];
            InvSbox[87] = _InvSbox[87];
            Xtime2Sbox[87] = _Xtime2Sbox[87];
            Xtime3Sbox[87] = _Xtime3Sbox[87];
            Xtime2[87] = _Xtime2[87];
            Xtime9[87] = _Xtime9[87];
            XtimeB[87] = _XtimeB[87];
            XtimeD[87] = _XtimeD[87];
            XtimeE[87] = _XtimeE[87];
            Sbox[88] = _Sbox[88];
            InvSbox[88] = _InvSbox[88];
            Xtime2Sbox[88] = _Xtime2Sbox[88];
            Xtime3Sbox[88] = _Xtime3Sbox[88];
            Xtime2[88] = _Xtime2[88];
            Xtime9[88] = _Xtime9[88];
            XtimeB[88] = _XtimeB[88];
            XtimeD[88] = _XtimeD[88];
            XtimeE[88] = _XtimeE[88];
            Sbox[89] = _Sbox[89];
            InvSbox[89] = _InvSbox[89];
            Xtime2Sbox[89] = _Xtime2Sbox[89];
            Xtime3Sbox[89] = _Xtime3Sbox[89];
            Xtime2[89] = _Xtime2[89];
            Xtime9[89] = _Xtime9[89];
            XtimeB[89] = _XtimeB[89];
            XtimeD[89] = _XtimeD[89];
            XtimeE[89] = _XtimeE[89];
            Sbox[90] = _Sbox[90];
            InvSbox[90] = _InvSbox[90];
            Xtime2Sbox[90] = _Xtime2Sbox[90];
            Xtime3Sbox[90] = _Xtime3Sbox[90];
            Xtime2[90] = _Xtime2[90];
            Xtime9[90] = _Xtime9[90];
            XtimeB[90] = _XtimeB[90];
            XtimeD[90] = _XtimeD[90];
            XtimeE[90] = _XtimeE[90];
            Sbox[91] = _Sbox[91];
            InvSbox[91] = _InvSbox[91];
            Xtime2Sbox[91] = _Xtime2Sbox[91];
            Xtime3Sbox[91] = _Xtime3Sbox[91];
            Xtime2[91] = _Xtime2[91];
            Xtime9[91] = _Xtime9[91];
            XtimeB[91] = _XtimeB[91];
            XtimeD[91] = _XtimeD[91];
            XtimeE[91] = _XtimeE[91];
            Sbox[92] = _Sbox[92];
            InvSbox[92] = _InvSbox[92];
            Xtime2Sbox[92] = _Xtime2Sbox[92];
            Xtime3Sbox[92] = _Xtime3Sbox[92];
            Xtime2[92] = _Xtime2[92];
            Xtime9[92] = _Xtime9[92];
            XtimeB[92] = _XtimeB[92];
            XtimeD[92] = _XtimeD[92];
            XtimeE[92] = _XtimeE[92];
            Sbox[93] = _Sbox[93];
            InvSbox[93] = _InvSbox[93];
            Xtime2Sbox[93] = _Xtime2Sbox[93];
            Xtime3Sbox[93] = _Xtime3Sbox[93];
            Xtime2[93] = _Xtime2[93];
            Xtime9[93] = _Xtime9[93];
            XtimeB[93] = _XtimeB[93];
            XtimeD[93] = _XtimeD[93];
            XtimeE[93] = _XtimeE[93];
            Sbox[94] = _Sbox[94];
            InvSbox[94] = _InvSbox[94];
            Xtime2Sbox[94] = _Xtime2Sbox[94];
            Xtime3Sbox[94] = _Xtime3Sbox[94];
            Xtime2[94] = _Xtime2[94];
            Xtime9[94] = _Xtime9[94];
            XtimeB[94] = _XtimeB[94];
            XtimeD[94] = _XtimeD[94];
            XtimeE[94] = _XtimeE[94];
            Sbox[95] = _Sbox[95];
            InvSbox[95] = _InvSbox[95];
            Xtime2Sbox[95] = _Xtime2Sbox[95];
            Xtime3Sbox[95] = _Xtime3Sbox[95];
            Xtime2[95] = _Xtime2[95];
            Xtime9[95] = _Xtime9[95];
            XtimeB[95] = _XtimeB[95];
            XtimeD[95] = _XtimeD[95];
            XtimeE[95] = _XtimeE[95];
            Sbox[96] = _Sbox[96];
            InvSbox[96] = _InvSbox[96];
            Xtime2Sbox[96] = _Xtime2Sbox[96];
            Xtime3Sbox[96] = _Xtime3Sbox[96];
            Xtime2[96] = _Xtime2[96];
            Xtime9[96] = _Xtime9[96];
            XtimeB[96] = _XtimeB[96];
            XtimeD[96] = _XtimeD[96];
            XtimeE[96] = _XtimeE[96];
            Sbox[97] = _Sbox[97];
            InvSbox[97] = _InvSbox[97];
            Xtime2Sbox[97] = _Xtime2Sbox[97];
            Xtime3Sbox[97] = _Xtime3Sbox[97];
            Xtime2[97] = _Xtime2[97];
            Xtime9[97] = _Xtime9[97];
            XtimeB[97] = _XtimeB[97];
            XtimeD[97] = _XtimeD[97];
            XtimeE[97] = _XtimeE[97];
            Sbox[98] = _Sbox[98];
            InvSbox[98] = _InvSbox[98];
            Xtime2Sbox[98] = _Xtime2Sbox[98];
            Xtime3Sbox[98] = _Xtime3Sbox[98];
            Xtime2[98] = _Xtime2[98];
            Xtime9[98] = _Xtime9[98];
            XtimeB[98] = _XtimeB[98];
            XtimeD[98] = _XtimeD[98];
            XtimeE[98] = _XtimeE[98];
            Sbox[99] = _Sbox[99];
            InvSbox[99] = _InvSbox[99];
            Xtime2Sbox[99] = _Xtime2Sbox[99];
            Xtime3Sbox[99] = _Xtime3Sbox[99];
            Xtime2[99] = _Xtime2[99];
            Xtime9[99] = _Xtime9[99];
            XtimeB[99] = _XtimeB[99];
            XtimeD[99] = _XtimeD[99];
            XtimeE[99] = _XtimeE[99];
            Sbox[100] = _Sbox[100];
            InvSbox[100] = _InvSbox[100];
            Xtime2Sbox[100] = _Xtime2Sbox[100];
            Xtime3Sbox[100] = _Xtime3Sbox[100];
            Xtime2[100] = _Xtime2[100];
            Xtime9[100] = _Xtime9[100];
            XtimeB[100] = _XtimeB[100];
            XtimeD[100] = _XtimeD[100];
            XtimeE[100] = _XtimeE[100];
            Sbox[101] = _Sbox[101];
            InvSbox[101] = _InvSbox[101];
            Xtime2Sbox[101] = _Xtime2Sbox[101];
            Xtime3Sbox[101] = _Xtime3Sbox[101];
            Xtime2[101] = _Xtime2[101];
            Xtime9[101] = _Xtime9[101];
            XtimeB[101] = _XtimeB[101];
            XtimeD[101] = _XtimeD[101];
            XtimeE[101] = _XtimeE[101];
            Sbox[102] = _Sbox[102];
            InvSbox[102] = _InvSbox[102];
            Xtime2Sbox[102] = _Xtime2Sbox[102];
            Xtime3Sbox[102] = _Xtime3Sbox[102];
            Xtime2[102] = _Xtime2[102];
            Xtime9[102] = _Xtime9[102];
            XtimeB[102] = _XtimeB[102];
            XtimeD[102] = _XtimeD[102];
            XtimeE[102] = _XtimeE[102];
            Sbox[103] = _Sbox[103];
            InvSbox[103] = _InvSbox[103];
            Xtime2Sbox[103] = _Xtime2Sbox[103];
            Xtime3Sbox[103] = _Xtime3Sbox[103];
            Xtime2[103] = _Xtime2[103];
            Xtime9[103] = _Xtime9[103];
            XtimeB[103] = _XtimeB[103];
            XtimeD[103] = _XtimeD[103];
            XtimeE[103] = _XtimeE[103];
            Sbox[104] = _Sbox[104];
            InvSbox[104] = _InvSbox[104];
            Xtime2Sbox[104] = _Xtime2Sbox[104];
            Xtime3Sbox[104] = _Xtime3Sbox[104];
            Xtime2[104] = _Xtime2[104];
            Xtime9[104] = _Xtime9[104];
            XtimeB[104] = _XtimeB[104];
            XtimeD[104] = _XtimeD[104];
            XtimeE[104] = _XtimeE[104];
            Sbox[105] = _Sbox[105];
            InvSbox[105] = _InvSbox[105];
            Xtime2Sbox[105] = _Xtime2Sbox[105];
            Xtime3Sbox[105] = _Xtime3Sbox[105];
            Xtime2[105] = _Xtime2[105];
            Xtime9[105] = _Xtime9[105];
            XtimeB[105] = _XtimeB[105];
            XtimeD[105] = _XtimeD[105];
            XtimeE[105] = _XtimeE[105];
            Sbox[106] = _Sbox[106];
            InvSbox[106] = _InvSbox[106];
            Xtime2Sbox[106] = _Xtime2Sbox[106];
            Xtime3Sbox[106] = _Xtime3Sbox[106];
            Xtime2[106] = _Xtime2[106];
            Xtime9[106] = _Xtime9[106];
            XtimeB[106] = _XtimeB[106];
            XtimeD[106] = _XtimeD[106];
            XtimeE[106] = _XtimeE[106];
            Sbox[107] = _Sbox[107];
            InvSbox[107] = _InvSbox[107];
            Xtime2Sbox[107] = _Xtime2Sbox[107];
            Xtime3Sbox[107] = _Xtime3Sbox[107];
            Xtime2[107] = _Xtime2[107];
            Xtime9[107] = _Xtime9[107];
            XtimeB[107] = _XtimeB[107];
            XtimeD[107] = _XtimeD[107];
            XtimeE[107] = _XtimeE[107];
            Sbox[108] = _Sbox[108];
            InvSbox[108] = _InvSbox[108];
            Xtime2Sbox[108] = _Xtime2Sbox[108];
            Xtime3Sbox[108] = _Xtime3Sbox[108];
            Xtime2[108] = _Xtime2[108];
            Xtime9[108] = _Xtime9[108];
            XtimeB[108] = _XtimeB[108];
            XtimeD[108] = _XtimeD[108];
            XtimeE[108] = _XtimeE[108];
            Sbox[109] = _Sbox[109];
            InvSbox[109] = _InvSbox[109];
            Xtime2Sbox[109] = _Xtime2Sbox[109];
            Xtime3Sbox[109] = _Xtime3Sbox[109];
            Xtime2[109] = _Xtime2[109];
            Xtime9[109] = _Xtime9[109];
            XtimeB[109] = _XtimeB[109];
            XtimeD[109] = _XtimeD[109];
            XtimeE[109] = _XtimeE[109];
            Sbox[110] = _Sbox[110];
            InvSbox[110] = _InvSbox[110];
            Xtime2Sbox[110] = _Xtime2Sbox[110];
            Xtime3Sbox[110] = _Xtime3Sbox[110];
            Xtime2[110] = _Xtime2[110];
            Xtime9[110] = _Xtime9[110];
            XtimeB[110] = _XtimeB[110];
            XtimeD[110] = _XtimeD[110];
            XtimeE[110] = _XtimeE[110];
            Sbox[111] = _Sbox[111];
            InvSbox[111] = _InvSbox[111];
            Xtime2Sbox[111] = _Xtime2Sbox[111];
            Xtime3Sbox[111] = _Xtime3Sbox[111];
            Xtime2[111] = _Xtime2[111];
            Xtime9[111] = _Xtime9[111];
            XtimeB[111] = _XtimeB[111];
            XtimeD[111] = _XtimeD[111];
            XtimeE[111] = _XtimeE[111];
            Sbox[112] = _Sbox[112];
            InvSbox[112] = _InvSbox[112];
            Xtime2Sbox[112] = _Xtime2Sbox[112];
            Xtime3Sbox[112] = _Xtime3Sbox[112];
            Xtime2[112] = _Xtime2[112];
            Xtime9[112] = _Xtime9[112];
            XtimeB[112] = _XtimeB[112];
            XtimeD[112] = _XtimeD[112];
            XtimeE[112] = _XtimeE[112];
            Sbox[113] = _Sbox[113];
            InvSbox[113] = _InvSbox[113];
            Xtime2Sbox[113] = _Xtime2Sbox[113];
            Xtime3Sbox[113] = _Xtime3Sbox[113];
            Xtime2[113] = _Xtime2[113];
            Xtime9[113] = _Xtime9[113];
            XtimeB[113] = _XtimeB[113];
            XtimeD[113] = _XtimeD[113];
            XtimeE[113] = _XtimeE[113];
            Sbox[114] = _Sbox[114];
            InvSbox[114] = _InvSbox[114];
            Xtime2Sbox[114] = _Xtime2Sbox[114];
            Xtime3Sbox[114] = _Xtime3Sbox[114];
            Xtime2[114] = _Xtime2[114];
            Xtime9[114] = _Xtime9[114];
            XtimeB[114] = _XtimeB[114];
            XtimeD[114] = _XtimeD[114];
            XtimeE[114] = _XtimeE[114];
            Sbox[115] = _Sbox[115];
            InvSbox[115] = _InvSbox[115];
            Xtime2Sbox[115] = _Xtime2Sbox[115];
            Xtime3Sbox[115] = _Xtime3Sbox[115];
            Xtime2[115] = _Xtime2[115];
            Xtime9[115] = _Xtime9[115];
            XtimeB[115] = _XtimeB[115];
            XtimeD[115] = _XtimeD[115];
            XtimeE[115] = _XtimeE[115];
            Sbox[116] = _Sbox[116];
            InvSbox[116] = _InvSbox[116];
            Xtime2Sbox[116] = _Xtime2Sbox[116];
            Xtime3Sbox[116] = _Xtime3Sbox[116];
            Xtime2[116] = _Xtime2[116];
            Xtime9[116] = _Xtime9[116];
            XtimeB[116] = _XtimeB[116];
            XtimeD[116] = _XtimeD[116];
            XtimeE[116] = _XtimeE[116];
            Sbox[117] = _Sbox[117];
            InvSbox[117] = _InvSbox[117];
            Xtime2Sbox[117] = _Xtime2Sbox[117];
            Xtime3Sbox[117] = _Xtime3Sbox[117];
            Xtime2[117] = _Xtime2[117];
            Xtime9[117] = _Xtime9[117];
            XtimeB[117] = _XtimeB[117];
            XtimeD[117] = _XtimeD[117];
            XtimeE[117] = _XtimeE[117];
            Sbox[118] = _Sbox[118];
            InvSbox[118] = _InvSbox[118];
            Xtime2Sbox[118] = _Xtime2Sbox[118];
            Xtime3Sbox[118] = _Xtime3Sbox[118];
            Xtime2[118] = _Xtime2[118];
            Xtime9[118] = _Xtime9[118];
            XtimeB[118] = _XtimeB[118];
            XtimeD[118] = _XtimeD[118];
            XtimeE[118] = _XtimeE[118];
            Sbox[119] = _Sbox[119];
            InvSbox[119] = _InvSbox[119];
            Xtime2Sbox[119] = _Xtime2Sbox[119];
            Xtime3Sbox[119] = _Xtime3Sbox[119];
            Xtime2[119] = _Xtime2[119];
            Xtime9[119] = _Xtime9[119];
            XtimeB[119] = _XtimeB[119];
            XtimeD[119] = _XtimeD[119];
            XtimeE[119] = _XtimeE[119];
            Sbox[120] = _Sbox[120];
            InvSbox[120] = _InvSbox[120];
            Xtime2Sbox[120] = _Xtime2Sbox[120];
            Xtime3Sbox[120] = _Xtime3Sbox[120];
            Xtime2[120] = _Xtime2[120];
            Xtime9[120] = _Xtime9[120];
            XtimeB[120] = _XtimeB[120];
            XtimeD[120] = _XtimeD[120];
            XtimeE[120] = _XtimeE[120];
            Sbox[121] = _Sbox[121];
            InvSbox[121] = _InvSbox[121];
            Xtime2Sbox[121] = _Xtime2Sbox[121];
            Xtime3Sbox[121] = _Xtime3Sbox[121];
            Xtime2[121] = _Xtime2[121];
            Xtime9[121] = _Xtime9[121];
            XtimeB[121] = _XtimeB[121];
            XtimeD[121] = _XtimeD[121];
            XtimeE[121] = _XtimeE[121];
            Sbox[122] = _Sbox[122];
            InvSbox[122] = _InvSbox[122];
            Xtime2Sbox[122] = _Xtime2Sbox[122];
            Xtime3Sbox[122] = _Xtime3Sbox[122];
            Xtime2[122] = _Xtime2[122];
            Xtime9[122] = _Xtime9[122];
            XtimeB[122] = _XtimeB[122];
            XtimeD[122] = _XtimeD[122];
            XtimeE[122] = _XtimeE[122];
            Sbox[123] = _Sbox[123];
            InvSbox[123] = _InvSbox[123];
            Xtime2Sbox[123] = _Xtime2Sbox[123];
            Xtime3Sbox[123] = _Xtime3Sbox[123];
            Xtime2[123] = _Xtime2[123];
            Xtime9[123] = _Xtime9[123];
            XtimeB[123] = _XtimeB[123];
            XtimeD[123] = _XtimeD[123];
            XtimeE[123] = _XtimeE[123];
            Sbox[124] = _Sbox[124];
            InvSbox[124] = _InvSbox[124];
            Xtime2Sbox[124] = _Xtime2Sbox[124];
            Xtime3Sbox[124] = _Xtime3Sbox[124];
            Xtime2[124] = _Xtime2[124];
            Xtime9[124] = _Xtime9[124];
            XtimeB[124] = _XtimeB[124];
            XtimeD[124] = _XtimeD[124];
            XtimeE[124] = _XtimeE[124];
            Sbox[125] = _Sbox[125];
            InvSbox[125] = _InvSbox[125];
            Xtime2Sbox[125] = _Xtime2Sbox[125];
            Xtime3Sbox[125] = _Xtime3Sbox[125];
            Xtime2[125] = _Xtime2[125];
            Xtime9[125] = _Xtime9[125];
            XtimeB[125] = _XtimeB[125];
            XtimeD[125] = _XtimeD[125];
            XtimeE[125] = _XtimeE[125];
            Sbox[126] = _Sbox[126];
            InvSbox[126] = _InvSbox[126];
            Xtime2Sbox[126] = _Xtime2Sbox[126];
            Xtime3Sbox[126] = _Xtime3Sbox[126];
            Xtime2[126] = _Xtime2[126];
            Xtime9[126] = _Xtime9[126];
            XtimeB[126] = _XtimeB[126];
            XtimeD[126] = _XtimeD[126];
            XtimeE[126] = _XtimeE[126];
            Sbox[127] = _Sbox[127];
            InvSbox[127] = _InvSbox[127];
            Xtime2Sbox[127] = _Xtime2Sbox[127];
            Xtime3Sbox[127] = _Xtime3Sbox[127];
            Xtime2[127] = _Xtime2[127];
            Xtime9[127] = _Xtime9[127];
            XtimeB[127] = _XtimeB[127];
            XtimeD[127] = _XtimeD[127];
            XtimeE[127] = _XtimeE[127];
            Sbox[128] = _Sbox[128];
            InvSbox[128] = _InvSbox[128];
            Xtime2Sbox[128] = _Xtime2Sbox[128];
            Xtime3Sbox[128] = _Xtime3Sbox[128];
            Xtime2[128] = _Xtime2[128];
            Xtime9[128] = _Xtime9[128];
            XtimeB[128] = _XtimeB[128];
            XtimeD[128] = _XtimeD[128];
            XtimeE[128] = _XtimeE[128];
            Sbox[129] = _Sbox[129];
            InvSbox[129] = _InvSbox[129];
            Xtime2Sbox[129] = _Xtime2Sbox[129];
            Xtime3Sbox[129] = _Xtime3Sbox[129];
            Xtime2[129] = _Xtime2[129];
            Xtime9[129] = _Xtime9[129];
            XtimeB[129] = _XtimeB[129];
            XtimeD[129] = _XtimeD[129];
            XtimeE[129] = _XtimeE[129];
            Sbox[130] = _Sbox[130];
            InvSbox[130] = _InvSbox[130];
            Xtime2Sbox[130] = _Xtime2Sbox[130];
            Xtime3Sbox[130] = _Xtime3Sbox[130];
            Xtime2[130] = _Xtime2[130];
            Xtime9[130] = _Xtime9[130];
            XtimeB[130] = _XtimeB[130];
            XtimeD[130] = _XtimeD[130];
            XtimeE[130] = _XtimeE[130];
            Sbox[131] = _Sbox[131];
            InvSbox[131] = _InvSbox[131];
            Xtime2Sbox[131] = _Xtime2Sbox[131];
            Xtime3Sbox[131] = _Xtime3Sbox[131];
            Xtime2[131] = _Xtime2[131];
            Xtime9[131] = _Xtime9[131];
            XtimeB[131] = _XtimeB[131];
            XtimeD[131] = _XtimeD[131];
            XtimeE[131] = _XtimeE[131];
            Sbox[132] = _Sbox[132];
            InvSbox[132] = _InvSbox[132];
            Xtime2Sbox[132] = _Xtime2Sbox[132];
            Xtime3Sbox[132] = _Xtime3Sbox[132];
            Xtime2[132] = _Xtime2[132];
            Xtime9[132] = _Xtime9[132];
            XtimeB[132] = _XtimeB[132];
            XtimeD[132] = _XtimeD[132];
            XtimeE[132] = _XtimeE[132];
            Sbox[133] = _Sbox[133];
            InvSbox[133] = _InvSbox[133];
            Xtime2Sbox[133] = _Xtime2Sbox[133];
            Xtime3Sbox[133] = _Xtime3Sbox[133];
            Xtime2[133] = _Xtime2[133];
            Xtime9[133] = _Xtime9[133];
            XtimeB[133] = _XtimeB[133];
            XtimeD[133] = _XtimeD[133];
            XtimeE[133] = _XtimeE[133];
            Sbox[134] = _Sbox[134];
            InvSbox[134] = _InvSbox[134];
            Xtime2Sbox[134] = _Xtime2Sbox[134];
            Xtime3Sbox[134] = _Xtime3Sbox[134];
            Xtime2[134] = _Xtime2[134];
            Xtime9[134] = _Xtime9[134];
            XtimeB[134] = _XtimeB[134];
            XtimeD[134] = _XtimeD[134];
            XtimeE[134] = _XtimeE[134];
            Sbox[135] = _Sbox[135];
            InvSbox[135] = _InvSbox[135];
            Xtime2Sbox[135] = _Xtime2Sbox[135];
            Xtime3Sbox[135] = _Xtime3Sbox[135];
            Xtime2[135] = _Xtime2[135];
            Xtime9[135] = _Xtime9[135];
            XtimeB[135] = _XtimeB[135];
            XtimeD[135] = _XtimeD[135];
            XtimeE[135] = _XtimeE[135];
            Sbox[136] = _Sbox[136];
            InvSbox[136] = _InvSbox[136];
            Xtime2Sbox[136] = _Xtime2Sbox[136];
            Xtime3Sbox[136] = _Xtime3Sbox[136];
            Xtime2[136] = _Xtime2[136];
            Xtime9[136] = _Xtime9[136];
            XtimeB[136] = _XtimeB[136];
            XtimeD[136] = _XtimeD[136];
            XtimeE[136] = _XtimeE[136];
            Sbox[137] = _Sbox[137];
            InvSbox[137] = _InvSbox[137];
            Xtime2Sbox[137] = _Xtime2Sbox[137];
            Xtime3Sbox[137] = _Xtime3Sbox[137];
            Xtime2[137] = _Xtime2[137];
            Xtime9[137] = _Xtime9[137];
            XtimeB[137] = _XtimeB[137];
            XtimeD[137] = _XtimeD[137];
            XtimeE[137] = _XtimeE[137];
            Sbox[138] = _Sbox[138];
            InvSbox[138] = _InvSbox[138];
            Xtime2Sbox[138] = _Xtime2Sbox[138];
            Xtime3Sbox[138] = _Xtime3Sbox[138];
            Xtime2[138] = _Xtime2[138];
            Xtime9[138] = _Xtime9[138];
            XtimeB[138] = _XtimeB[138];
            XtimeD[138] = _XtimeD[138];
            XtimeE[138] = _XtimeE[138];
            Sbox[139] = _Sbox[139];
            InvSbox[139] = _InvSbox[139];
            Xtime2Sbox[139] = _Xtime2Sbox[139];
            Xtime3Sbox[139] = _Xtime3Sbox[139];
            Xtime2[139] = _Xtime2[139];
            Xtime9[139] = _Xtime9[139];
            XtimeB[139] = _XtimeB[139];
            XtimeD[139] = _XtimeD[139];
            XtimeE[139] = _XtimeE[139];
            Sbox[140] = _Sbox[140];
            InvSbox[140] = _InvSbox[140];
            Xtime2Sbox[140] = _Xtime2Sbox[140];
            Xtime3Sbox[140] = _Xtime3Sbox[140];
            Xtime2[140] = _Xtime2[140];
            Xtime9[140] = _Xtime9[140];
            XtimeB[140] = _XtimeB[140];
            XtimeD[140] = _XtimeD[140];
            XtimeE[140] = _XtimeE[140];
            Sbox[141] = _Sbox[141];
            InvSbox[141] = _InvSbox[141];
            Xtime2Sbox[141] = _Xtime2Sbox[141];
            Xtime3Sbox[141] = _Xtime3Sbox[141];
            Xtime2[141] = _Xtime2[141];
            Xtime9[141] = _Xtime9[141];
            XtimeB[141] = _XtimeB[141];
            XtimeD[141] = _XtimeD[141];
            XtimeE[141] = _XtimeE[141];
            Sbox[142] = _Sbox[142];
            InvSbox[142] = _InvSbox[142];
            Xtime2Sbox[142] = _Xtime2Sbox[142];
            Xtime3Sbox[142] = _Xtime3Sbox[142];
            Xtime2[142] = _Xtime2[142];
            Xtime9[142] = _Xtime9[142];
            XtimeB[142] = _XtimeB[142];
            XtimeD[142] = _XtimeD[142];
            XtimeE[142] = _XtimeE[142];
            Sbox[143] = _Sbox[143];
            InvSbox[143] = _InvSbox[143];
            Xtime2Sbox[143] = _Xtime2Sbox[143];
            Xtime3Sbox[143] = _Xtime3Sbox[143];
            Xtime2[143] = _Xtime2[143];
            Xtime9[143] = _Xtime9[143];
            XtimeB[143] = _XtimeB[143];
            XtimeD[143] = _XtimeD[143];
            XtimeE[143] = _XtimeE[143];
            Sbox[144] = _Sbox[144];
            InvSbox[144] = _InvSbox[144];
            Xtime2Sbox[144] = _Xtime2Sbox[144];
            Xtime3Sbox[144] = _Xtime3Sbox[144];
            Xtime2[144] = _Xtime2[144];
            Xtime9[144] = _Xtime9[144];
            XtimeB[144] = _XtimeB[144];
            XtimeD[144] = _XtimeD[144];
            XtimeE[144] = _XtimeE[144];
            Sbox[145] = _Sbox[145];
            InvSbox[145] = _InvSbox[145];
            Xtime2Sbox[145] = _Xtime2Sbox[145];
            Xtime3Sbox[145] = _Xtime3Sbox[145];
            Xtime2[145] = _Xtime2[145];
            Xtime9[145] = _Xtime9[145];
            XtimeB[145] = _XtimeB[145];
            XtimeD[145] = _XtimeD[145];
            XtimeE[145] = _XtimeE[145];
            Sbox[146] = _Sbox[146];
            InvSbox[146] = _InvSbox[146];
            Xtime2Sbox[146] = _Xtime2Sbox[146];
            Xtime3Sbox[146] = _Xtime3Sbox[146];
            Xtime2[146] = _Xtime2[146];
            Xtime9[146] = _Xtime9[146];
            XtimeB[146] = _XtimeB[146];
            XtimeD[146] = _XtimeD[146];
            XtimeE[146] = _XtimeE[146];
            Sbox[147] = _Sbox[147];
            InvSbox[147] = _InvSbox[147];
            Xtime2Sbox[147] = _Xtime2Sbox[147];
            Xtime3Sbox[147] = _Xtime3Sbox[147];
            Xtime2[147] = _Xtime2[147];
            Xtime9[147] = _Xtime9[147];
            XtimeB[147] = _XtimeB[147];
            XtimeD[147] = _XtimeD[147];
            XtimeE[147] = _XtimeE[147];
            Sbox[148] = _Sbox[148];
            InvSbox[148] = _InvSbox[148];
            Xtime2Sbox[148] = _Xtime2Sbox[148];
            Xtime3Sbox[148] = _Xtime3Sbox[148];
            Xtime2[148] = _Xtime2[148];
            Xtime9[148] = _Xtime9[148];
            XtimeB[148] = _XtimeB[148];
            XtimeD[148] = _XtimeD[148];
            XtimeE[148] = _XtimeE[148];
            Sbox[149] = _Sbox[149];
            InvSbox[149] = _InvSbox[149];
            Xtime2Sbox[149] = _Xtime2Sbox[149];
            Xtime3Sbox[149] = _Xtime3Sbox[149];
            Xtime2[149] = _Xtime2[149];
            Xtime9[149] = _Xtime9[149];
            XtimeB[149] = _XtimeB[149];
            XtimeD[149] = _XtimeD[149];
            XtimeE[149] = _XtimeE[149];
            Sbox[150] = _Sbox[150];
            InvSbox[150] = _InvSbox[150];
            Xtime2Sbox[150] = _Xtime2Sbox[150];
            Xtime3Sbox[150] = _Xtime3Sbox[150];
            Xtime2[150] = _Xtime2[150];
            Xtime9[150] = _Xtime9[150];
            XtimeB[150] = _XtimeB[150];
            XtimeD[150] = _XtimeD[150];
            XtimeE[150] = _XtimeE[150];
            Sbox[151] = _Sbox[151];
            InvSbox[151] = _InvSbox[151];
            Xtime2Sbox[151] = _Xtime2Sbox[151];
            Xtime3Sbox[151] = _Xtime3Sbox[151];
            Xtime2[151] = _Xtime2[151];
            Xtime9[151] = _Xtime9[151];
            XtimeB[151] = _XtimeB[151];
            XtimeD[151] = _XtimeD[151];
            XtimeE[151] = _XtimeE[151];
            Sbox[152] = _Sbox[152];
            InvSbox[152] = _InvSbox[152];
            Xtime2Sbox[152] = _Xtime2Sbox[152];
            Xtime3Sbox[152] = _Xtime3Sbox[152];
            Xtime2[152] = _Xtime2[152];
            Xtime9[152] = _Xtime9[152];
            XtimeB[152] = _XtimeB[152];
            XtimeD[152] = _XtimeD[152];
            XtimeE[152] = _XtimeE[152];
            Sbox[153] = _Sbox[153];
            InvSbox[153] = _InvSbox[153];
            Xtime2Sbox[153] = _Xtime2Sbox[153];
            Xtime3Sbox[153] = _Xtime3Sbox[153];
            Xtime2[153] = _Xtime2[153];
            Xtime9[153] = _Xtime9[153];
            XtimeB[153] = _XtimeB[153];
            XtimeD[153] = _XtimeD[153];
            XtimeE[153] = _XtimeE[153];
            Sbox[154] = _Sbox[154];
            InvSbox[154] = _InvSbox[154];
            Xtime2Sbox[154] = _Xtime2Sbox[154];
            Xtime3Sbox[154] = _Xtime3Sbox[154];
            Xtime2[154] = _Xtime2[154];
            Xtime9[154] = _Xtime9[154];
            XtimeB[154] = _XtimeB[154];
            XtimeD[154] = _XtimeD[154];
            XtimeE[154] = _XtimeE[154];
            Sbox[155] = _Sbox[155];
            InvSbox[155] = _InvSbox[155];
            Xtime2Sbox[155] = _Xtime2Sbox[155];
            Xtime3Sbox[155] = _Xtime3Sbox[155];
            Xtime2[155] = _Xtime2[155];
            Xtime9[155] = _Xtime9[155];
            XtimeB[155] = _XtimeB[155];
            XtimeD[155] = _XtimeD[155];
            XtimeE[155] = _XtimeE[155];
            Sbox[156] = _Sbox[156];
            InvSbox[156] = _InvSbox[156];
            Xtime2Sbox[156] = _Xtime2Sbox[156];
            Xtime3Sbox[156] = _Xtime3Sbox[156];
            Xtime2[156] = _Xtime2[156];
            Xtime9[156] = _Xtime9[156];
            XtimeB[156] = _XtimeB[156];
            XtimeD[156] = _XtimeD[156];
            XtimeE[156] = _XtimeE[156];
            Sbox[157] = _Sbox[157];
            InvSbox[157] = _InvSbox[157];
            Xtime2Sbox[157] = _Xtime2Sbox[157];
            Xtime3Sbox[157] = _Xtime3Sbox[157];
            Xtime2[157] = _Xtime2[157];
            Xtime9[157] = _Xtime9[157];
            XtimeB[157] = _XtimeB[157];
            XtimeD[157] = _XtimeD[157];
            XtimeE[157] = _XtimeE[157];
            Sbox[158] = _Sbox[158];
            InvSbox[158] = _InvSbox[158];
            Xtime2Sbox[158] = _Xtime2Sbox[158];
            Xtime3Sbox[158] = _Xtime3Sbox[158];
            Xtime2[158] = _Xtime2[158];
            Xtime9[158] = _Xtime9[158];
            XtimeB[158] = _XtimeB[158];
            XtimeD[158] = _XtimeD[158];
            XtimeE[158] = _XtimeE[158];
            Sbox[159] = _Sbox[159];
            InvSbox[159] = _InvSbox[159];
            Xtime2Sbox[159] = _Xtime2Sbox[159];
            Xtime3Sbox[159] = _Xtime3Sbox[159];
            Xtime2[159] = _Xtime2[159];
            Xtime9[159] = _Xtime9[159];
            XtimeB[159] = _XtimeB[159];
            XtimeD[159] = _XtimeD[159];
            XtimeE[159] = _XtimeE[159];
            Sbox[160] = _Sbox[160];
            InvSbox[160] = _InvSbox[160];
            Xtime2Sbox[160] = _Xtime2Sbox[160];
            Xtime3Sbox[160] = _Xtime3Sbox[160];
            Xtime2[160] = _Xtime2[160];
            Xtime9[160] = _Xtime9[160];
            XtimeB[160] = _XtimeB[160];
            XtimeD[160] = _XtimeD[160];
            XtimeE[160] = _XtimeE[160];
            Sbox[161] = _Sbox[161];
            InvSbox[161] = _InvSbox[161];
            Xtime2Sbox[161] = _Xtime2Sbox[161];
            Xtime3Sbox[161] = _Xtime3Sbox[161];
            Xtime2[161] = _Xtime2[161];
            Xtime9[161] = _Xtime9[161];
            XtimeB[161] = _XtimeB[161];
            XtimeD[161] = _XtimeD[161];
            XtimeE[161] = _XtimeE[161];
            Sbox[162] = _Sbox[162];
            InvSbox[162] = _InvSbox[162];
            Xtime2Sbox[162] = _Xtime2Sbox[162];
            Xtime3Sbox[162] = _Xtime3Sbox[162];
            Xtime2[162] = _Xtime2[162];
            Xtime9[162] = _Xtime9[162];
            XtimeB[162] = _XtimeB[162];
            XtimeD[162] = _XtimeD[162];
            XtimeE[162] = _XtimeE[162];
            Sbox[163] = _Sbox[163];
            InvSbox[163] = _InvSbox[163];
            Xtime2Sbox[163] = _Xtime2Sbox[163];
            Xtime3Sbox[163] = _Xtime3Sbox[163];
            Xtime2[163] = _Xtime2[163];
            Xtime9[163] = _Xtime9[163];
            XtimeB[163] = _XtimeB[163];
            XtimeD[163] = _XtimeD[163];
            XtimeE[163] = _XtimeE[163];
            Sbox[164] = _Sbox[164];
            InvSbox[164] = _InvSbox[164];
            Xtime2Sbox[164] = _Xtime2Sbox[164];
            Xtime3Sbox[164] = _Xtime3Sbox[164];
            Xtime2[164] = _Xtime2[164];
            Xtime9[164] = _Xtime9[164];
            XtimeB[164] = _XtimeB[164];
            XtimeD[164] = _XtimeD[164];
            XtimeE[164] = _XtimeE[164];
            Sbox[165] = _Sbox[165];
            InvSbox[165] = _InvSbox[165];
            Xtime2Sbox[165] = _Xtime2Sbox[165];
            Xtime3Sbox[165] = _Xtime3Sbox[165];
            Xtime2[165] = _Xtime2[165];
            Xtime9[165] = _Xtime9[165];
            XtimeB[165] = _XtimeB[165];
            XtimeD[165] = _XtimeD[165];
            XtimeE[165] = _XtimeE[165];
            Sbox[166] = _Sbox[166];
            InvSbox[166] = _InvSbox[166];
            Xtime2Sbox[166] = _Xtime2Sbox[166];
            Xtime3Sbox[166] = _Xtime3Sbox[166];
            Xtime2[166] = _Xtime2[166];
            Xtime9[166] = _Xtime9[166];
            XtimeB[166] = _XtimeB[166];
            XtimeD[166] = _XtimeD[166];
            XtimeE[166] = _XtimeE[166];
            Sbox[167] = _Sbox[167];
            InvSbox[167] = _InvSbox[167];
            Xtime2Sbox[167] = _Xtime2Sbox[167];
            Xtime3Sbox[167] = _Xtime3Sbox[167];
            Xtime2[167] = _Xtime2[167];
            Xtime9[167] = _Xtime9[167];
            XtimeB[167] = _XtimeB[167];
            XtimeD[167] = _XtimeD[167];
            XtimeE[167] = _XtimeE[167];
            Sbox[168] = _Sbox[168];
            InvSbox[168] = _InvSbox[168];
            Xtime2Sbox[168] = _Xtime2Sbox[168];
            Xtime3Sbox[168] = _Xtime3Sbox[168];
            Xtime2[168] = _Xtime2[168];
            Xtime9[168] = _Xtime9[168];
            XtimeB[168] = _XtimeB[168];
            XtimeD[168] = _XtimeD[168];
            XtimeE[168] = _XtimeE[168];
            Sbox[169] = _Sbox[169];
            InvSbox[169] = _InvSbox[169];
            Xtime2Sbox[169] = _Xtime2Sbox[169];
            Xtime3Sbox[169] = _Xtime3Sbox[169];
            Xtime2[169] = _Xtime2[169];
            Xtime9[169] = _Xtime9[169];
            XtimeB[169] = _XtimeB[169];
            XtimeD[169] = _XtimeD[169];
            XtimeE[169] = _XtimeE[169];
            Sbox[170] = _Sbox[170];
            InvSbox[170] = _InvSbox[170];
            Xtime2Sbox[170] = _Xtime2Sbox[170];
            Xtime3Sbox[170] = _Xtime3Sbox[170];
            Xtime2[170] = _Xtime2[170];
            Xtime9[170] = _Xtime9[170];
            XtimeB[170] = _XtimeB[170];
            XtimeD[170] = _XtimeD[170];
            XtimeE[170] = _XtimeE[170];
            Sbox[171] = _Sbox[171];
            InvSbox[171] = _InvSbox[171];
            Xtime2Sbox[171] = _Xtime2Sbox[171];
            Xtime3Sbox[171] = _Xtime3Sbox[171];
            Xtime2[171] = _Xtime2[171];
            Xtime9[171] = _Xtime9[171];
            XtimeB[171] = _XtimeB[171];
            XtimeD[171] = _XtimeD[171];
            XtimeE[171] = _XtimeE[171];
            Sbox[172] = _Sbox[172];
            InvSbox[172] = _InvSbox[172];
            Xtime2Sbox[172] = _Xtime2Sbox[172];
            Xtime3Sbox[172] = _Xtime3Sbox[172];
            Xtime2[172] = _Xtime2[172];
            Xtime9[172] = _Xtime9[172];
            XtimeB[172] = _XtimeB[172];
            XtimeD[172] = _XtimeD[172];
            XtimeE[172] = _XtimeE[172];
            Sbox[173] = _Sbox[173];
            InvSbox[173] = _InvSbox[173];
            Xtime2Sbox[173] = _Xtime2Sbox[173];
            Xtime3Sbox[173] = _Xtime3Sbox[173];
            Xtime2[173] = _Xtime2[173];
            Xtime9[173] = _Xtime9[173];
            XtimeB[173] = _XtimeB[173];
            XtimeD[173] = _XtimeD[173];
            XtimeE[173] = _XtimeE[173];
            Sbox[174] = _Sbox[174];
            InvSbox[174] = _InvSbox[174];
            Xtime2Sbox[174] = _Xtime2Sbox[174];
            Xtime3Sbox[174] = _Xtime3Sbox[174];
            Xtime2[174] = _Xtime2[174];
            Xtime9[174] = _Xtime9[174];
            XtimeB[174] = _XtimeB[174];
            XtimeD[174] = _XtimeD[174];
            XtimeE[174] = _XtimeE[174];
            Sbox[175] = _Sbox[175];
            InvSbox[175] = _InvSbox[175];
            Xtime2Sbox[175] = _Xtime2Sbox[175];
            Xtime3Sbox[175] = _Xtime3Sbox[175];
            Xtime2[175] = _Xtime2[175];
            Xtime9[175] = _Xtime9[175];
            XtimeB[175] = _XtimeB[175];
            XtimeD[175] = _XtimeD[175];
            XtimeE[175] = _XtimeE[175];
            Sbox[176] = _Sbox[176];
            InvSbox[176] = _InvSbox[176];
            Xtime2Sbox[176] = _Xtime2Sbox[176];
            Xtime3Sbox[176] = _Xtime3Sbox[176];
            Xtime2[176] = _Xtime2[176];
            Xtime9[176] = _Xtime9[176];
            XtimeB[176] = _XtimeB[176];
            XtimeD[176] = _XtimeD[176];
            XtimeE[176] = _XtimeE[176];
            Sbox[177] = _Sbox[177];
            InvSbox[177] = _InvSbox[177];
            Xtime2Sbox[177] = _Xtime2Sbox[177];
            Xtime3Sbox[177] = _Xtime3Sbox[177];
            Xtime2[177] = _Xtime2[177];
            Xtime9[177] = _Xtime9[177];
            XtimeB[177] = _XtimeB[177];
            XtimeD[177] = _XtimeD[177];
            XtimeE[177] = _XtimeE[177];
            Sbox[178] = _Sbox[178];
            InvSbox[178] = _InvSbox[178];
            Xtime2Sbox[178] = _Xtime2Sbox[178];
            Xtime3Sbox[178] = _Xtime3Sbox[178];
            Xtime2[178] = _Xtime2[178];
            Xtime9[178] = _Xtime9[178];
            XtimeB[178] = _XtimeB[178];
            XtimeD[178] = _XtimeD[178];
            XtimeE[178] = _XtimeE[178];
            Sbox[179] = _Sbox[179];
            InvSbox[179] = _InvSbox[179];
            Xtime2Sbox[179] = _Xtime2Sbox[179];
            Xtime3Sbox[179] = _Xtime3Sbox[179];
            Xtime2[179] = _Xtime2[179];
            Xtime9[179] = _Xtime9[179];
            XtimeB[179] = _XtimeB[179];
            XtimeD[179] = _XtimeD[179];
            XtimeE[179] = _XtimeE[179];
            Sbox[180] = _Sbox[180];
            InvSbox[180] = _InvSbox[180];
            Xtime2Sbox[180] = _Xtime2Sbox[180];
            Xtime3Sbox[180] = _Xtime3Sbox[180];
            Xtime2[180] = _Xtime2[180];
            Xtime9[180] = _Xtime9[180];
            XtimeB[180] = _XtimeB[180];
            XtimeD[180] = _XtimeD[180];
            XtimeE[180] = _XtimeE[180];
            Sbox[181] = _Sbox[181];
            InvSbox[181] = _InvSbox[181];
            Xtime2Sbox[181] = _Xtime2Sbox[181];
            Xtime3Sbox[181] = _Xtime3Sbox[181];
            Xtime2[181] = _Xtime2[181];
            Xtime9[181] = _Xtime9[181];
            XtimeB[181] = _XtimeB[181];
            XtimeD[181] = _XtimeD[181];
            XtimeE[181] = _XtimeE[181];
            Sbox[182] = _Sbox[182];
            InvSbox[182] = _InvSbox[182];
            Xtime2Sbox[182] = _Xtime2Sbox[182];
            Xtime3Sbox[182] = _Xtime3Sbox[182];
            Xtime2[182] = _Xtime2[182];
            Xtime9[182] = _Xtime9[182];
            XtimeB[182] = _XtimeB[182];
            XtimeD[182] = _XtimeD[182];
            XtimeE[182] = _XtimeE[182];
            Sbox[183] = _Sbox[183];
            InvSbox[183] = _InvSbox[183];
            Xtime2Sbox[183] = _Xtime2Sbox[183];
            Xtime3Sbox[183] = _Xtime3Sbox[183];
            Xtime2[183] = _Xtime2[183];
            Xtime9[183] = _Xtime9[183];
            XtimeB[183] = _XtimeB[183];
            XtimeD[183] = _XtimeD[183];
            XtimeE[183] = _XtimeE[183];
            Sbox[184] = _Sbox[184];
            InvSbox[184] = _InvSbox[184];
            Xtime2Sbox[184] = _Xtime2Sbox[184];
            Xtime3Sbox[184] = _Xtime3Sbox[184];
            Xtime2[184] = _Xtime2[184];
            Xtime9[184] = _Xtime9[184];
            XtimeB[184] = _XtimeB[184];
            XtimeD[184] = _XtimeD[184];
            XtimeE[184] = _XtimeE[184];
            Sbox[185] = _Sbox[185];
            InvSbox[185] = _InvSbox[185];
            Xtime2Sbox[185] = _Xtime2Sbox[185];
            Xtime3Sbox[185] = _Xtime3Sbox[185];
            Xtime2[185] = _Xtime2[185];
            Xtime9[185] = _Xtime9[185];
            XtimeB[185] = _XtimeB[185];
            XtimeD[185] = _XtimeD[185];
            XtimeE[185] = _XtimeE[185];
            Sbox[186] = _Sbox[186];
            InvSbox[186] = _InvSbox[186];
            Xtime2Sbox[186] = _Xtime2Sbox[186];
            Xtime3Sbox[186] = _Xtime3Sbox[186];
            Xtime2[186] = _Xtime2[186];
            Xtime9[186] = _Xtime9[186];
            XtimeB[186] = _XtimeB[186];
            XtimeD[186] = _XtimeD[186];
            XtimeE[186] = _XtimeE[186];
            Sbox[187] = _Sbox[187];
            InvSbox[187] = _InvSbox[187];
            Xtime2Sbox[187] = _Xtime2Sbox[187];
            Xtime3Sbox[187] = _Xtime3Sbox[187];
            Xtime2[187] = _Xtime2[187];
            Xtime9[187] = _Xtime9[187];
            XtimeB[187] = _XtimeB[187];
            XtimeD[187] = _XtimeD[187];
            XtimeE[187] = _XtimeE[187];
            Sbox[188] = _Sbox[188];
            InvSbox[188] = _InvSbox[188];
            Xtime2Sbox[188] = _Xtime2Sbox[188];
            Xtime3Sbox[188] = _Xtime3Sbox[188];
            Xtime2[188] = _Xtime2[188];
            Xtime9[188] = _Xtime9[188];
            XtimeB[188] = _XtimeB[188];
            XtimeD[188] = _XtimeD[188];
            XtimeE[188] = _XtimeE[188];
            Sbox[189] = _Sbox[189];
            InvSbox[189] = _InvSbox[189];
            Xtime2Sbox[189] = _Xtime2Sbox[189];
            Xtime3Sbox[189] = _Xtime3Sbox[189];
            Xtime2[189] = _Xtime2[189];
            Xtime9[189] = _Xtime9[189];
            XtimeB[189] = _XtimeB[189];
            XtimeD[189] = _XtimeD[189];
            XtimeE[189] = _XtimeE[189];
            Sbox[190] = _Sbox[190];
            InvSbox[190] = _InvSbox[190];
            Xtime2Sbox[190] = _Xtime2Sbox[190];
            Xtime3Sbox[190] = _Xtime3Sbox[190];
            Xtime2[190] = _Xtime2[190];
            Xtime9[190] = _Xtime9[190];
            XtimeB[190] = _XtimeB[190];
            XtimeD[190] = _XtimeD[190];
            XtimeE[190] = _XtimeE[190];
            Sbox[191] = _Sbox[191];
            InvSbox[191] = _InvSbox[191];
            Xtime2Sbox[191] = _Xtime2Sbox[191];
            Xtime3Sbox[191] = _Xtime3Sbox[191];
            Xtime2[191] = _Xtime2[191];
            Xtime9[191] = _Xtime9[191];
            XtimeB[191] = _XtimeB[191];
            XtimeD[191] = _XtimeD[191];
            XtimeE[191] = _XtimeE[191];
            Sbox[192] = _Sbox[192];
            InvSbox[192] = _InvSbox[192];
            Xtime2Sbox[192] = _Xtime2Sbox[192];
            Xtime3Sbox[192] = _Xtime3Sbox[192];
            Xtime2[192] = _Xtime2[192];
            Xtime9[192] = _Xtime9[192];
            XtimeB[192] = _XtimeB[192];
            XtimeD[192] = _XtimeD[192];
            XtimeE[192] = _XtimeE[192];
            Sbox[193] = _Sbox[193];
            InvSbox[193] = _InvSbox[193];
            Xtime2Sbox[193] = _Xtime2Sbox[193];
            Xtime3Sbox[193] = _Xtime3Sbox[193];
            Xtime2[193] = _Xtime2[193];
            Xtime9[193] = _Xtime9[193];
            XtimeB[193] = _XtimeB[193];
            XtimeD[193] = _XtimeD[193];
            XtimeE[193] = _XtimeE[193];
            Sbox[194] = _Sbox[194];
            InvSbox[194] = _InvSbox[194];
            Xtime2Sbox[194] = _Xtime2Sbox[194];
            Xtime3Sbox[194] = _Xtime3Sbox[194];
            Xtime2[194] = _Xtime2[194];
            Xtime9[194] = _Xtime9[194];
            XtimeB[194] = _XtimeB[194];
            XtimeD[194] = _XtimeD[194];
            XtimeE[194] = _XtimeE[194];
            Sbox[195] = _Sbox[195];
            InvSbox[195] = _InvSbox[195];
            Xtime2Sbox[195] = _Xtime2Sbox[195];
            Xtime3Sbox[195] = _Xtime3Sbox[195];
            Xtime2[195] = _Xtime2[195];
            Xtime9[195] = _Xtime9[195];
            XtimeB[195] = _XtimeB[195];
            XtimeD[195] = _XtimeD[195];
            XtimeE[195] = _XtimeE[195];
            Sbox[196] = _Sbox[196];
            InvSbox[196] = _InvSbox[196];
            Xtime2Sbox[196] = _Xtime2Sbox[196];
            Xtime3Sbox[196] = _Xtime3Sbox[196];
            Xtime2[196] = _Xtime2[196];
            Xtime9[196] = _Xtime9[196];
            XtimeB[196] = _XtimeB[196];
            XtimeD[196] = _XtimeD[196];
            XtimeE[196] = _XtimeE[196];
            Sbox[197] = _Sbox[197];
            InvSbox[197] = _InvSbox[197];
            Xtime2Sbox[197] = _Xtime2Sbox[197];
            Xtime3Sbox[197] = _Xtime3Sbox[197];
            Xtime2[197] = _Xtime2[197];
            Xtime9[197] = _Xtime9[197];
            XtimeB[197] = _XtimeB[197];
            XtimeD[197] = _XtimeD[197];
            XtimeE[197] = _XtimeE[197];
            Sbox[198] = _Sbox[198];
            InvSbox[198] = _InvSbox[198];
            Xtime2Sbox[198] = _Xtime2Sbox[198];
            Xtime3Sbox[198] = _Xtime3Sbox[198];
            Xtime2[198] = _Xtime2[198];
            Xtime9[198] = _Xtime9[198];
            XtimeB[198] = _XtimeB[198];
            XtimeD[198] = _XtimeD[198];
            XtimeE[198] = _XtimeE[198];
            Sbox[199] = _Sbox[199];
            InvSbox[199] = _InvSbox[199];
            Xtime2Sbox[199] = _Xtime2Sbox[199];
            Xtime3Sbox[199] = _Xtime3Sbox[199];
            Xtime2[199] = _Xtime2[199];
            Xtime9[199] = _Xtime9[199];
            XtimeB[199] = _XtimeB[199];
            XtimeD[199] = _XtimeD[199];
            XtimeE[199] = _XtimeE[199];
            Sbox[200] = _Sbox[200];
            InvSbox[200] = _InvSbox[200];
            Xtime2Sbox[200] = _Xtime2Sbox[200];
            Xtime3Sbox[200] = _Xtime3Sbox[200];
            Xtime2[200] = _Xtime2[200];
            Xtime9[200] = _Xtime9[200];
            XtimeB[200] = _XtimeB[200];
            XtimeD[200] = _XtimeD[200];
            XtimeE[200] = _XtimeE[200];
            Sbox[201] = _Sbox[201];
            InvSbox[201] = _InvSbox[201];
            Xtime2Sbox[201] = _Xtime2Sbox[201];
            Xtime3Sbox[201] = _Xtime3Sbox[201];
            Xtime2[201] = _Xtime2[201];
            Xtime9[201] = _Xtime9[201];
            XtimeB[201] = _XtimeB[201];
            XtimeD[201] = _XtimeD[201];
            XtimeE[201] = _XtimeE[201];
            Sbox[202] = _Sbox[202];
            InvSbox[202] = _InvSbox[202];
            Xtime2Sbox[202] = _Xtime2Sbox[202];
            Xtime3Sbox[202] = _Xtime3Sbox[202];
            Xtime2[202] = _Xtime2[202];
            Xtime9[202] = _Xtime9[202];
            XtimeB[202] = _XtimeB[202];
            XtimeD[202] = _XtimeD[202];
            XtimeE[202] = _XtimeE[202];
            Sbox[203] = _Sbox[203];
            InvSbox[203] = _InvSbox[203];
            Xtime2Sbox[203] = _Xtime2Sbox[203];
            Xtime3Sbox[203] = _Xtime3Sbox[203];
            Xtime2[203] = _Xtime2[203];
            Xtime9[203] = _Xtime9[203];
            XtimeB[203] = _XtimeB[203];
            XtimeD[203] = _XtimeD[203];
            XtimeE[203] = _XtimeE[203];
            Sbox[204] = _Sbox[204];
            InvSbox[204] = _InvSbox[204];
            Xtime2Sbox[204] = _Xtime2Sbox[204];
            Xtime3Sbox[204] = _Xtime3Sbox[204];
            Xtime2[204] = _Xtime2[204];
            Xtime9[204] = _Xtime9[204];
            XtimeB[204] = _XtimeB[204];
            XtimeD[204] = _XtimeD[204];
            XtimeE[204] = _XtimeE[204];
            Sbox[205] = _Sbox[205];
            InvSbox[205] = _InvSbox[205];
            Xtime2Sbox[205] = _Xtime2Sbox[205];
            Xtime3Sbox[205] = _Xtime3Sbox[205];
            Xtime2[205] = _Xtime2[205];
            Xtime9[205] = _Xtime9[205];
            XtimeB[205] = _XtimeB[205];
            XtimeD[205] = _XtimeD[205];
            XtimeE[205] = _XtimeE[205];
            Sbox[206] = _Sbox[206];
            InvSbox[206] = _InvSbox[206];
            Xtime2Sbox[206] = _Xtime2Sbox[206];
            Xtime3Sbox[206] = _Xtime3Sbox[206];
            Xtime2[206] = _Xtime2[206];
            Xtime9[206] = _Xtime9[206];
            XtimeB[206] = _XtimeB[206];
            XtimeD[206] = _XtimeD[206];
            XtimeE[206] = _XtimeE[206];
            Sbox[207] = _Sbox[207];
            InvSbox[207] = _InvSbox[207];
            Xtime2Sbox[207] = _Xtime2Sbox[207];
            Xtime3Sbox[207] = _Xtime3Sbox[207];
            Xtime2[207] = _Xtime2[207];
            Xtime9[207] = _Xtime9[207];
            XtimeB[207] = _XtimeB[207];
            XtimeD[207] = _XtimeD[207];
            XtimeE[207] = _XtimeE[207];
            Sbox[208] = _Sbox[208];
            InvSbox[208] = _InvSbox[208];
            Xtime2Sbox[208] = _Xtime2Sbox[208];
            Xtime3Sbox[208] = _Xtime3Sbox[208];
            Xtime2[208] = _Xtime2[208];
            Xtime9[208] = _Xtime9[208];
            XtimeB[208] = _XtimeB[208];
            XtimeD[208] = _XtimeD[208];
            XtimeE[208] = _XtimeE[208];
            Sbox[209] = _Sbox[209];
            InvSbox[209] = _InvSbox[209];
            Xtime2Sbox[209] = _Xtime2Sbox[209];
            Xtime3Sbox[209] = _Xtime3Sbox[209];
            Xtime2[209] = _Xtime2[209];
            Xtime9[209] = _Xtime9[209];
            XtimeB[209] = _XtimeB[209];
            XtimeD[209] = _XtimeD[209];
            XtimeE[209] = _XtimeE[209];
            Sbox[210] = _Sbox[210];
            InvSbox[210] = _InvSbox[210];
            Xtime2Sbox[210] = _Xtime2Sbox[210];
            Xtime3Sbox[210] = _Xtime3Sbox[210];
            Xtime2[210] = _Xtime2[210];
            Xtime9[210] = _Xtime9[210];
            XtimeB[210] = _XtimeB[210];
            XtimeD[210] = _XtimeD[210];
            XtimeE[210] = _XtimeE[210];
            Sbox[211] = _Sbox[211];
            InvSbox[211] = _InvSbox[211];
            Xtime2Sbox[211] = _Xtime2Sbox[211];
            Xtime3Sbox[211] = _Xtime3Sbox[211];
            Xtime2[211] = _Xtime2[211];
            Xtime9[211] = _Xtime9[211];
            XtimeB[211] = _XtimeB[211];
            XtimeD[211] = _XtimeD[211];
            XtimeE[211] = _XtimeE[211];
            Sbox[212] = _Sbox[212];
            InvSbox[212] = _InvSbox[212];
            Xtime2Sbox[212] = _Xtime2Sbox[212];
            Xtime3Sbox[212] = _Xtime3Sbox[212];
            Xtime2[212] = _Xtime2[212];
            Xtime9[212] = _Xtime9[212];
            XtimeB[212] = _XtimeB[212];
            XtimeD[212] = _XtimeD[212];
            XtimeE[212] = _XtimeE[212];
            Sbox[213] = _Sbox[213];
            InvSbox[213] = _InvSbox[213];
            Xtime2Sbox[213] = _Xtime2Sbox[213];
            Xtime3Sbox[213] = _Xtime3Sbox[213];
            Xtime2[213] = _Xtime2[213];
            Xtime9[213] = _Xtime9[213];
            XtimeB[213] = _XtimeB[213];
            XtimeD[213] = _XtimeD[213];
            XtimeE[213] = _XtimeE[213];
            Sbox[214] = _Sbox[214];
            InvSbox[214] = _InvSbox[214];
            Xtime2Sbox[214] = _Xtime2Sbox[214];
            Xtime3Sbox[214] = _Xtime3Sbox[214];
            Xtime2[214] = _Xtime2[214];
            Xtime9[214] = _Xtime9[214];
            XtimeB[214] = _XtimeB[214];
            XtimeD[214] = _XtimeD[214];
            XtimeE[214] = _XtimeE[214];
            Sbox[215] = _Sbox[215];
            InvSbox[215] = _InvSbox[215];
            Xtime2Sbox[215] = _Xtime2Sbox[215];
            Xtime3Sbox[215] = _Xtime3Sbox[215];
            Xtime2[215] = _Xtime2[215];
            Xtime9[215] = _Xtime9[215];
            XtimeB[215] = _XtimeB[215];
            XtimeD[215] = _XtimeD[215];
            XtimeE[215] = _XtimeE[215];
            Sbox[216] = _Sbox[216];
            InvSbox[216] = _InvSbox[216];
            Xtime2Sbox[216] = _Xtime2Sbox[216];
            Xtime3Sbox[216] = _Xtime3Sbox[216];
            Xtime2[216] = _Xtime2[216];
            Xtime9[216] = _Xtime9[216];
            XtimeB[216] = _XtimeB[216];
            XtimeD[216] = _XtimeD[216];
            XtimeE[216] = _XtimeE[216];
            Sbox[217] = _Sbox[217];
            InvSbox[217] = _InvSbox[217];
            Xtime2Sbox[217] = _Xtime2Sbox[217];
            Xtime3Sbox[217] = _Xtime3Sbox[217];
            Xtime2[217] = _Xtime2[217];
            Xtime9[217] = _Xtime9[217];
            XtimeB[217] = _XtimeB[217];
            XtimeD[217] = _XtimeD[217];
            XtimeE[217] = _XtimeE[217];
            Sbox[218] = _Sbox[218];
            InvSbox[218] = _InvSbox[218];
            Xtime2Sbox[218] = _Xtime2Sbox[218];
            Xtime3Sbox[218] = _Xtime3Sbox[218];
            Xtime2[218] = _Xtime2[218];
            Xtime9[218] = _Xtime9[218];
            XtimeB[218] = _XtimeB[218];
            XtimeD[218] = _XtimeD[218];
            XtimeE[218] = _XtimeE[218];
            Sbox[219] = _Sbox[219];
            InvSbox[219] = _InvSbox[219];
            Xtime2Sbox[219] = _Xtime2Sbox[219];
            Xtime3Sbox[219] = _Xtime3Sbox[219];
            Xtime2[219] = _Xtime2[219];
            Xtime9[219] = _Xtime9[219];
            XtimeB[219] = _XtimeB[219];
            XtimeD[219] = _XtimeD[219];
            XtimeE[219] = _XtimeE[219];
            Sbox[220] = _Sbox[220];
            InvSbox[220] = _InvSbox[220];
            Xtime2Sbox[220] = _Xtime2Sbox[220];
            Xtime3Sbox[220] = _Xtime3Sbox[220];
            Xtime2[220] = _Xtime2[220];
            Xtime9[220] = _Xtime9[220];
            XtimeB[220] = _XtimeB[220];
            XtimeD[220] = _XtimeD[220];
            XtimeE[220] = _XtimeE[220];
            Sbox[221] = _Sbox[221];
            InvSbox[221] = _InvSbox[221];
            Xtime2Sbox[221] = _Xtime2Sbox[221];
            Xtime3Sbox[221] = _Xtime3Sbox[221];
            Xtime2[221] = _Xtime2[221];
            Xtime9[221] = _Xtime9[221];
            XtimeB[221] = _XtimeB[221];
            XtimeD[221] = _XtimeD[221];
            XtimeE[221] = _XtimeE[221];
            Sbox[222] = _Sbox[222];
            InvSbox[222] = _InvSbox[222];
            Xtime2Sbox[222] = _Xtime2Sbox[222];
            Xtime3Sbox[222] = _Xtime3Sbox[222];
            Xtime2[222] = _Xtime2[222];
            Xtime9[222] = _Xtime9[222];
            XtimeB[222] = _XtimeB[222];
            XtimeD[222] = _XtimeD[222];
            XtimeE[222] = _XtimeE[222];
            Sbox[223] = _Sbox[223];
            InvSbox[223] = _InvSbox[223];
            Xtime2Sbox[223] = _Xtime2Sbox[223];
            Xtime3Sbox[223] = _Xtime3Sbox[223];
            Xtime2[223] = _Xtime2[223];
            Xtime9[223] = _Xtime9[223];
            XtimeB[223] = _XtimeB[223];
            XtimeD[223] = _XtimeD[223];
            XtimeE[223] = _XtimeE[223];
            Sbox[224] = _Sbox[224];
            InvSbox[224] = _InvSbox[224];
            Xtime2Sbox[224] = _Xtime2Sbox[224];
            Xtime3Sbox[224] = _Xtime3Sbox[224];
            Xtime2[224] = _Xtime2[224];
            Xtime9[224] = _Xtime9[224];
            XtimeB[224] = _XtimeB[224];
            XtimeD[224] = _XtimeD[224];
            XtimeE[224] = _XtimeE[224];
            Sbox[225] = _Sbox[225];
            InvSbox[225] = _InvSbox[225];
            Xtime2Sbox[225] = _Xtime2Sbox[225];
            Xtime3Sbox[225] = _Xtime3Sbox[225];
            Xtime2[225] = _Xtime2[225];
            Xtime9[225] = _Xtime9[225];
            XtimeB[225] = _XtimeB[225];
            XtimeD[225] = _XtimeD[225];
            XtimeE[225] = _XtimeE[225];
            Sbox[226] = _Sbox[226];
            InvSbox[226] = _InvSbox[226];
            Xtime2Sbox[226] = _Xtime2Sbox[226];
            Xtime3Sbox[226] = _Xtime3Sbox[226];
            Xtime2[226] = _Xtime2[226];
            Xtime9[226] = _Xtime9[226];
            XtimeB[226] = _XtimeB[226];
            XtimeD[226] = _XtimeD[226];
            XtimeE[226] = _XtimeE[226];
            Sbox[227] = _Sbox[227];
            InvSbox[227] = _InvSbox[227];
            Xtime2Sbox[227] = _Xtime2Sbox[227];
            Xtime3Sbox[227] = _Xtime3Sbox[227];
            Xtime2[227] = _Xtime2[227];
            Xtime9[227] = _Xtime9[227];
            XtimeB[227] = _XtimeB[227];
            XtimeD[227] = _XtimeD[227];
            XtimeE[227] = _XtimeE[227];
            Sbox[228] = _Sbox[228];
            InvSbox[228] = _InvSbox[228];
            Xtime2Sbox[228] = _Xtime2Sbox[228];
            Xtime3Sbox[228] = _Xtime3Sbox[228];
            Xtime2[228] = _Xtime2[228];
            Xtime9[228] = _Xtime9[228];
            XtimeB[228] = _XtimeB[228];
            XtimeD[228] = _XtimeD[228];
            XtimeE[228] = _XtimeE[228];
            Sbox[229] = _Sbox[229];
            InvSbox[229] = _InvSbox[229];
            Xtime2Sbox[229] = _Xtime2Sbox[229];
            Xtime3Sbox[229] = _Xtime3Sbox[229];
            Xtime2[229] = _Xtime2[229];
            Xtime9[229] = _Xtime9[229];
            XtimeB[229] = _XtimeB[229];
            XtimeD[229] = _XtimeD[229];
            XtimeE[229] = _XtimeE[229];
            Sbox[230] = _Sbox[230];
            InvSbox[230] = _InvSbox[230];
            Xtime2Sbox[230] = _Xtime2Sbox[230];
            Xtime3Sbox[230] = _Xtime3Sbox[230];
            Xtime2[230] = _Xtime2[230];
            Xtime9[230] = _Xtime9[230];
            XtimeB[230] = _XtimeB[230];
            XtimeD[230] = _XtimeD[230];
            XtimeE[230] = _XtimeE[230];
            Sbox[231] = _Sbox[231];
            InvSbox[231] = _InvSbox[231];
            Xtime2Sbox[231] = _Xtime2Sbox[231];
            Xtime3Sbox[231] = _Xtime3Sbox[231];
            Xtime2[231] = _Xtime2[231];
            Xtime9[231] = _Xtime9[231];
            XtimeB[231] = _XtimeB[231];
            XtimeD[231] = _XtimeD[231];
            XtimeE[231] = _XtimeE[231];
            Sbox[232] = _Sbox[232];
            InvSbox[232] = _InvSbox[232];
            Xtime2Sbox[232] = _Xtime2Sbox[232];
            Xtime3Sbox[232] = _Xtime3Sbox[232];
            Xtime2[232] = _Xtime2[232];
            Xtime9[232] = _Xtime9[232];
            XtimeB[232] = _XtimeB[232];
            XtimeD[232] = _XtimeD[232];
            XtimeE[232] = _XtimeE[232];
            Sbox[233] = _Sbox[233];
            InvSbox[233] = _InvSbox[233];
            Xtime2Sbox[233] = _Xtime2Sbox[233];
            Xtime3Sbox[233] = _Xtime3Sbox[233];
            Xtime2[233] = _Xtime2[233];
            Xtime9[233] = _Xtime9[233];
            XtimeB[233] = _XtimeB[233];
            XtimeD[233] = _XtimeD[233];
            XtimeE[233] = _XtimeE[233];
            Sbox[234] = _Sbox[234];
            InvSbox[234] = _InvSbox[234];
            Xtime2Sbox[234] = _Xtime2Sbox[234];
            Xtime3Sbox[234] = _Xtime3Sbox[234];
            Xtime2[234] = _Xtime2[234];
            Xtime9[234] = _Xtime9[234];
            XtimeB[234] = _XtimeB[234];
            XtimeD[234] = _XtimeD[234];
            XtimeE[234] = _XtimeE[234];
            Sbox[235] = _Sbox[235];
            InvSbox[235] = _InvSbox[235];
            Xtime2Sbox[235] = _Xtime2Sbox[235];
            Xtime3Sbox[235] = _Xtime3Sbox[235];
            Xtime2[235] = _Xtime2[235];
            Xtime9[235] = _Xtime9[235];
            XtimeB[235] = _XtimeB[235];
            XtimeD[235] = _XtimeD[235];
            XtimeE[235] = _XtimeE[235];
            Sbox[236] = _Sbox[236];
            InvSbox[236] = _InvSbox[236];
            Xtime2Sbox[236] = _Xtime2Sbox[236];
            Xtime3Sbox[236] = _Xtime3Sbox[236];
            Xtime2[236] = _Xtime2[236];
            Xtime9[236] = _Xtime9[236];
            XtimeB[236] = _XtimeB[236];
            XtimeD[236] = _XtimeD[236];
            XtimeE[236] = _XtimeE[236];
            Sbox[237] = _Sbox[237];
            InvSbox[237] = _InvSbox[237];
            Xtime2Sbox[237] = _Xtime2Sbox[237];
            Xtime3Sbox[237] = _Xtime3Sbox[237];
            Xtime2[237] = _Xtime2[237];
            Xtime9[237] = _Xtime9[237];
            XtimeB[237] = _XtimeB[237];
            XtimeD[237] = _XtimeD[237];
            XtimeE[237] = _XtimeE[237];
            Sbox[238] = _Sbox[238];
            InvSbox[238] = _InvSbox[238];
            Xtime2Sbox[238] = _Xtime2Sbox[238];
            Xtime3Sbox[238] = _Xtime3Sbox[238];
            Xtime2[238] = _Xtime2[238];
            Xtime9[238] = _Xtime9[238];
            XtimeB[238] = _XtimeB[238];
            XtimeD[238] = _XtimeD[238];
            XtimeE[238] = _XtimeE[238];
            Sbox[239] = _Sbox[239];
            InvSbox[239] = _InvSbox[239];
            Xtime2Sbox[239] = _Xtime2Sbox[239];
            Xtime3Sbox[239] = _Xtime3Sbox[239];
            Xtime2[239] = _Xtime2[239];
            Xtime9[239] = _Xtime9[239];
            XtimeB[239] = _XtimeB[239];
            XtimeD[239] = _XtimeD[239];
            XtimeE[239] = _XtimeE[239];
            Sbox[240] = _Sbox[240];
            InvSbox[240] = _InvSbox[240];
            Xtime2Sbox[240] = _Xtime2Sbox[240];
            Xtime3Sbox[240] = _Xtime3Sbox[240];
            Xtime2[240] = _Xtime2[240];
            Xtime9[240] = _Xtime9[240];
            XtimeB[240] = _XtimeB[240];
            XtimeD[240] = _XtimeD[240];
            XtimeE[240] = _XtimeE[240];
            Sbox[241] = _Sbox[241];
            InvSbox[241] = _InvSbox[241];
            Xtime2Sbox[241] = _Xtime2Sbox[241];
            Xtime3Sbox[241] = _Xtime3Sbox[241];
            Xtime2[241] = _Xtime2[241];
            Xtime9[241] = _Xtime9[241];
            XtimeB[241] = _XtimeB[241];
            XtimeD[241] = _XtimeD[241];
            XtimeE[241] = _XtimeE[241];
            Sbox[242] = _Sbox[242];
            InvSbox[242] = _InvSbox[242];
            Xtime2Sbox[242] = _Xtime2Sbox[242];
            Xtime3Sbox[242] = _Xtime3Sbox[242];
            Xtime2[242] = _Xtime2[242];
            Xtime9[242] = _Xtime9[242];
            XtimeB[242] = _XtimeB[242];
            XtimeD[242] = _XtimeD[242];
            XtimeE[242] = _XtimeE[242];
            Sbox[243] = _Sbox[243];
            InvSbox[243] = _InvSbox[243];
            Xtime2Sbox[243] = _Xtime2Sbox[243];
            Xtime3Sbox[243] = _Xtime3Sbox[243];
            Xtime2[243] = _Xtime2[243];
            Xtime9[243] = _Xtime9[243];
            XtimeB[243] = _XtimeB[243];
            XtimeD[243] = _XtimeD[243];
            XtimeE[243] = _XtimeE[243];
            Sbox[244] = _Sbox[244];
            InvSbox[244] = _InvSbox[244];
            Xtime2Sbox[244] = _Xtime2Sbox[244];
            Xtime3Sbox[244] = _Xtime3Sbox[244];
            Xtime2[244] = _Xtime2[244];
            Xtime9[244] = _Xtime9[244];
            XtimeB[244] = _XtimeB[244];
            XtimeD[244] = _XtimeD[244];
            XtimeE[244] = _XtimeE[244];
            Sbox[245] = _Sbox[245];
            InvSbox[245] = _InvSbox[245];
            Xtime2Sbox[245] = _Xtime2Sbox[245];
            Xtime3Sbox[245] = _Xtime3Sbox[245];
            Xtime2[245] = _Xtime2[245];
            Xtime9[245] = _Xtime9[245];
            XtimeB[245] = _XtimeB[245];
            XtimeD[245] = _XtimeD[245];
            XtimeE[245] = _XtimeE[245];
            Sbox[246] = _Sbox[246];
            InvSbox[246] = _InvSbox[246];
            Xtime2Sbox[246] = _Xtime2Sbox[246];
            Xtime3Sbox[246] = _Xtime3Sbox[246];
            Xtime2[246] = _Xtime2[246];
            Xtime9[246] = _Xtime9[246];
            XtimeB[246] = _XtimeB[246];
            XtimeD[246] = _XtimeD[246];
            XtimeE[246] = _XtimeE[246];
            Sbox[247] = _Sbox[247];
            InvSbox[247] = _InvSbox[247];
            Xtime2Sbox[247] = _Xtime2Sbox[247];
            Xtime3Sbox[247] = _Xtime3Sbox[247];
            Xtime2[247] = _Xtime2[247];
            Xtime9[247] = _Xtime9[247];
            XtimeB[247] = _XtimeB[247];
            XtimeD[247] = _XtimeD[247];
            XtimeE[247] = _XtimeE[247];
            Sbox[248] = _Sbox[248];
            InvSbox[248] = _InvSbox[248];
            Xtime2Sbox[248] = _Xtime2Sbox[248];
            Xtime3Sbox[248] = _Xtime3Sbox[248];
            Xtime2[248] = _Xtime2[248];
            Xtime9[248] = _Xtime9[248];
            XtimeB[248] = _XtimeB[248];
            XtimeD[248] = _XtimeD[248];
            XtimeE[248] = _XtimeE[248];
            Sbox[249] = _Sbox[249];
            InvSbox[249] = _InvSbox[249];
            Xtime2Sbox[249] = _Xtime2Sbox[249];
            Xtime3Sbox[249] = _Xtime3Sbox[249];
            Xtime2[249] = _Xtime2[249];
            Xtime9[249] = _Xtime9[249];
            XtimeB[249] = _XtimeB[249];
            XtimeD[249] = _XtimeD[249];
            XtimeE[249] = _XtimeE[249];
            Sbox[250] = _Sbox[250];
            InvSbox[250] = _InvSbox[250];
            Xtime2Sbox[250] = _Xtime2Sbox[250];
            Xtime3Sbox[250] = _Xtime3Sbox[250];
            Xtime2[250] = _Xtime2[250];
            Xtime9[250] = _Xtime9[250];
            XtimeB[250] = _XtimeB[250];
            XtimeD[250] = _XtimeD[250];
            XtimeE[250] = _XtimeE[250];
            Sbox[251] = _Sbox[251];
            InvSbox[251] = _InvSbox[251];
            Xtime2Sbox[251] = _Xtime2Sbox[251];
            Xtime3Sbox[251] = _Xtime3Sbox[251];
            Xtime2[251] = _Xtime2[251];
            Xtime9[251] = _Xtime9[251];
            XtimeB[251] = _XtimeB[251];
            XtimeD[251] = _XtimeD[251];
            XtimeE[251] = _XtimeE[251];
            Sbox[252] = _Sbox[252];
            InvSbox[252] = _InvSbox[252];
            Xtime2Sbox[252] = _Xtime2Sbox[252];
            Xtime3Sbox[252] = _Xtime3Sbox[252];
            Xtime2[252] = _Xtime2[252];
            Xtime9[252] = _Xtime9[252];
            XtimeB[252] = _XtimeB[252];
            XtimeD[252] = _XtimeD[252];
            XtimeE[252] = _XtimeE[252];
            Sbox[253] = _Sbox[253];
            InvSbox[253] = _InvSbox[253];
            Xtime2Sbox[253] = _Xtime2Sbox[253];
            Xtime3Sbox[253] = _Xtime3Sbox[253];
            Xtime2[253] = _Xtime2[253];
            Xtime9[253] = _Xtime9[253];
            XtimeB[253] = _XtimeB[253];
            XtimeD[253] = _XtimeD[253];
            XtimeE[253] = _XtimeE[253];
            Sbox[254] = _Sbox[254];
            InvSbox[254] = _InvSbox[254];
            Xtime2Sbox[254] = _Xtime2Sbox[254];
            Xtime3Sbox[254] = _Xtime3Sbox[254];
            Xtime2[254] = _Xtime2[254];
            Xtime9[254] = _Xtime9[254];
            XtimeB[254] = _XtimeB[254];
            XtimeD[254] = _XtimeD[254];
            XtimeE[254] = _XtimeE[254];
            Sbox[255] = _Sbox[255];
            InvSbox[255] = _InvSbox[255];
            Xtime2Sbox[255] = _Xtime2Sbox[255];
            Xtime3Sbox[255] = _Xtime3Sbox[255];
            Xtime2[255] = _Xtime2[255];
            Xtime9[255] = _Xtime9[255];
            XtimeB[255] = _XtimeB[255];
            XtimeD[255] = _XtimeD[255];
            XtimeE[255] = _XtimeE[255];
			Rcon = new ByteArray;
            /*
			for (i=0;i<_Rcon.length;i++) {
				Rcon[i] = _Rcon[i];
			}
            */
            Rcon[0] = _Rcon[0];
            Rcon[1] = _Rcon[1];
            Rcon[2] = _Rcon[2];
            Rcon[3] = _Rcon[3];
            Rcon[4] = _Rcon[4];
            Rcon[5] = _Rcon[5];
            Rcon[6] = _Rcon[6];
            Rcon[7] = _Rcon[7];
            Rcon[8] = _Rcon[8];
            Rcon[9] = _Rcon[9];
            Rcon[10] = _Rcon[10];
            Rcon[11] = _Rcon[11];
		}
		
		private var key:ByteArray;
		private var keyLength:uint;
		private var Nr:uint;
		private var state:ByteArray;
		private var tmp:ByteArray;

		public function AESKey(key:ByteArray) {
			tmp = new ByteArray;
			state = new ByteArray;
			keyLength = key.length;
			this.key = new ByteArray;
			this.key.writeBytes(key);
			expandKey();
		}
		
		// produce Nb bytes for each round
		private function expandKey():void {
			var tmp0:uint, tmp1:uint, tmp2:uint, tmp3:uint, tmp4:uint;
			var idx:uint;
			var Nk:uint = key.length/4;
			Nr = Nk+6;
			
			for( idx = Nk; idx < Nb * (Nr + 1); idx++ ) {
				tmp0 = key[4*idx - 4];
				tmp1 = key[4*idx - 3];
				tmp2 = key[4*idx - 2];
				tmp3 = key[4*idx - 1];
				if( !(idx % Nk) ) {
					tmp4 = tmp3;
					tmp3 = Sbox[tmp0];
					tmp0 = Sbox[tmp1] ^ Rcon[idx/Nk];
					tmp1 = Sbox[tmp2];
					tmp2 = Sbox[tmp4];
				} else if( Nk > 6 && idx % Nk == 4 ) {
					tmp0 = Sbox[tmp0];
					tmp1 = Sbox[tmp1];
					tmp2 = Sbox[tmp2];
					tmp3 = Sbox[tmp3];
				}
		
				key[4*idx+0] = key[4*idx - 4*Nk + 0] ^ tmp0;
				key[4*idx+1] = key[4*idx - 4*Nk + 1] ^ tmp1;
				key[4*idx+2] = key[4*idx - 4*Nk + 2] ^ tmp2;
				key[4*idx+3] = key[4*idx - 4*Nk + 3] ^ tmp3;
			}
		}


		public function getBlockSize():uint
		{
			return 16;
		}
		
		// encrypt one 128 bit block
		public function encrypt(block:ByteArray, index:uint=0):void
		{
			var round:uint;
			state.position=0;
			state.writeBytes(block, index, Nb*4);

			addRoundKey(key, 0);
			for ( round = 1; round < Nr + 1; round++ ) {
				if (round < Nr) {
					mixSubColumns();
				} else {
					shiftRows();
				}
				addRoundKey(key, round * Nb * 4);
			}

			block.position=index;
			block.writeBytes(state);
		}
		
		public function decrypt(block:ByteArray, index:uint=0):void
		{
			var round:uint;
			state.position=0;
			state.writeBytes(block, index, Nb*4);

			addRoundKey(key, Nr*Nb*4);
			invShiftRows();
			for( round = Nr; round--; )
			{
				addRoundKey( key, round*Nb*4);
				if (round) {
					invMixSubColumns();
				}
			}
			
			block.position=index;
			block.writeBytes(state);
		}
		
		public function dispose():void {
			var i:uint;
			var r:Random = new Random;
			for (i=0;i<key.length;i++) {
				key[i] = r.nextByte();
			}
			Nr = r.nextByte();
			for (i=0;i<state.length;i++) {
				state[i] = r.nextByte();
			}
			for (i=0;i<tmp.length;i++) {
				tmp[i] = r.nextByte();
			}
			key.length=0;
			keyLength=0;
			state.length=0;
			tmp.length=0;
			key = null;
			state = null;
			tmp = null;
			Nr = 0;
			Memory.gc();
		}

		// exchanges columns in each of 4 rows
		// row0 - unchanged, row1- shifted left 1, 
		// row2 - shifted left 2 and row3 - shifted left 3
		protected function shiftRows():void
		{
			var tmp:uint;
		
			// just substitute row 0
			state[0] = Sbox[state[0]]; state[4] = Sbox[state[4]];
			state[8] = Sbox[state[8]]; state[12] = Sbox[state[12]];
		
			// rotate row 1
			tmp = Sbox[state[1]]; state[1] = Sbox[state[5]];
			state[5] = Sbox[state[9]]; state[9] = Sbox[state[13]]; state[13] = tmp;
		
			// rotate row 2
			tmp = Sbox[state[2]]; state[2] = Sbox[state[10]]; state[10] = tmp;
			tmp = Sbox[state[6]]; state[6] = Sbox[state[14]]; state[14] = tmp;
		
			// rotate row 3
			tmp = Sbox[state[15]]; state[15] = Sbox[state[11]];
			state[11] = Sbox[state[7]]; state[7] = Sbox[state[3]]; state[3] = tmp;
		}
		
		// restores columns in each of 4 rows
		// row0 - unchanged, row1- shifted right 1, 
		// row2 - shifted right 2 and row3 - shifted right 3
		protected function invShiftRows ():void
		{
			var tmp:uint;
		
			// restore row 0
			state[0] = InvSbox[state[0]]; state[4] = InvSbox[state[4]];
			state[8] = InvSbox[state[8]]; state[12] = InvSbox[state[12]];
		
			// restore row 1
			tmp = InvSbox[state[13]]; state[13] = InvSbox[state[9]];
			state[9] = InvSbox[state[5]]; state[5] = InvSbox[state[1]]; state[1] = tmp;
		
			// restore row 2
			tmp = InvSbox[state[2]]; state[2] = InvSbox[state[10]]; state[10] = tmp;
			tmp = InvSbox[state[6]]; state[6] = InvSbox[state[14]]; state[14] = tmp;
		
			// restore row 3
			tmp = InvSbox[state[3]]; state[3] = InvSbox[state[7]];
			state[7] = InvSbox[state[11]]; state[11] = InvSbox[state[15]]; state[15] = tmp;
		}
		
		// recombine and mix each row in a column
		protected function mixSubColumns ():void
		{
			tmp.length=0;
		
			// mixing column 0
			tmp[0] = Xtime2Sbox[state[0]] ^ Xtime3Sbox[state[5]] ^ Sbox[state[10]] ^ Sbox[state[15]];
			tmp[1] = Sbox[state[0]] ^ Xtime2Sbox[state[5]] ^ Xtime3Sbox[state[10]] ^ Sbox[state[15]];
			tmp[2] = Sbox[state[0]] ^ Sbox[state[5]] ^ Xtime2Sbox[state[10]] ^ Xtime3Sbox[state[15]];
			tmp[3] = Xtime3Sbox[state[0]] ^ Sbox[state[5]] ^ Sbox[state[10]] ^ Xtime2Sbox[state[15]];
		
			// mixing column 1
			tmp[4] = Xtime2Sbox[state[4]] ^ Xtime3Sbox[state[9]] ^ Sbox[state[14]] ^ Sbox[state[3]];
			tmp[5] = Sbox[state[4]] ^ Xtime2Sbox[state[9]] ^ Xtime3Sbox[state[14]] ^ Sbox[state[3]];
			tmp[6] = Sbox[state[4]] ^ Sbox[state[9]] ^ Xtime2Sbox[state[14]] ^ Xtime3Sbox[state[3]];
			tmp[7] = Xtime3Sbox[state[4]] ^ Sbox[state[9]] ^ Sbox[state[14]] ^ Xtime2Sbox[state[3]];
		
			// mixing column 2
			tmp[8] = Xtime2Sbox[state[8]] ^ Xtime3Sbox[state[13]] ^ Sbox[state[2]] ^ Sbox[state[7]];
			tmp[9] = Sbox[state[8]] ^ Xtime2Sbox[state[13]] ^ Xtime3Sbox[state[2]] ^ Sbox[state[7]];
			tmp[10]  = Sbox[state[8]] ^ Sbox[state[13]] ^ Xtime2Sbox[state[2]] ^ Xtime3Sbox[state[7]];
			tmp[11]  = Xtime3Sbox[state[8]] ^ Sbox[state[13]] ^ Sbox[state[2]] ^ Xtime2Sbox[state[7]];
		
			// mixing column 3
			tmp[12] = Xtime2Sbox[state[12]] ^ Xtime3Sbox[state[1]] ^ Sbox[state[6]] ^ Sbox[state[11]];
			tmp[13] = Sbox[state[12]] ^ Xtime2Sbox[state[1]] ^ Xtime3Sbox[state[6]] ^ Sbox[state[11]];
			tmp[14] = Sbox[state[12]] ^ Sbox[state[1]] ^ Xtime2Sbox[state[6]] ^ Xtime3Sbox[state[11]];
			tmp[15] = Xtime3Sbox[state[12]] ^ Sbox[state[1]] ^ Sbox[state[6]] ^ Xtime2Sbox[state[11]];
		
			state.position=0;
			state.writeBytes(tmp, 0, Nb*4);
		}
		
		// restore and un-mix each row in a column
		protected function invMixSubColumns ():void
		{
			tmp.length=0;
			var i:uint;
		
			// restore column 0
			tmp[0] = XtimeE[state[0]] ^ XtimeB[state[1]] ^ XtimeD[state[2]] ^ Xtime9[state[3]];
			tmp[5] = Xtime9[state[0]] ^ XtimeE[state[1]] ^ XtimeB[state[2]] ^ XtimeD[state[3]];
			tmp[10] = XtimeD[state[0]] ^ Xtime9[state[1]] ^ XtimeE[state[2]] ^ XtimeB[state[3]];
			tmp[15] = XtimeB[state[0]] ^ XtimeD[state[1]] ^ Xtime9[state[2]] ^ XtimeE[state[3]];
		
			// restore column 1
			tmp[4] = XtimeE[state[4]] ^ XtimeB[state[5]] ^ XtimeD[state[6]] ^ Xtime9[state[7]];
			tmp[9] = Xtime9[state[4]] ^ XtimeE[state[5]] ^ XtimeB[state[6]] ^ XtimeD[state[7]];
			tmp[14] = XtimeD[state[4]] ^ Xtime9[state[5]] ^ XtimeE[state[6]] ^ XtimeB[state[7]];
			tmp[3] = XtimeB[state[4]] ^ XtimeD[state[5]] ^ Xtime9[state[6]] ^ XtimeE[state[7]];
		
			// restore column 2
			tmp[8] = XtimeE[state[8]] ^ XtimeB[state[9]] ^ XtimeD[state[10]] ^ Xtime9[state[11]];
			tmp[13] = Xtime9[state[8]] ^ XtimeE[state[9]] ^ XtimeB[state[10]] ^ XtimeD[state[11]];
			tmp[2]  = XtimeD[state[8]] ^ Xtime9[state[9]] ^ XtimeE[state[10]] ^ XtimeB[state[11]];
			tmp[7]  = XtimeB[state[8]] ^ XtimeD[state[9]] ^ Xtime9[state[10]] ^ XtimeE[state[11]];
		
			// restore column 3
			tmp[12] = XtimeE[state[12]] ^ XtimeB[state[13]] ^ XtimeD[state[14]] ^ Xtime9[state[15]];
			tmp[1] = Xtime9[state[12]] ^ XtimeE[state[13]] ^ XtimeB[state[14]] ^ XtimeD[state[15]];
			tmp[6] = XtimeD[state[12]] ^ Xtime9[state[13]] ^ XtimeE[state[14]] ^ XtimeB[state[15]];
			tmp[11] = XtimeB[state[12]] ^ XtimeD[state[13]] ^ Xtime9[state[14]] ^ XtimeE[state[15]];
		
			for( i=0; i < 4 * Nb; i++ )
				state[i] = InvSbox[tmp[i]];
		}
		
		// encrypt/decrypt columns of the key
		protected function addRoundKey (key:ByteArray, offset:uint):void
		{
			var idx:uint;
		
			for( idx = 0; idx < 16; idx++ )
				state[idx] ^= key[idx+offset];
		}

		public function toString():String {
			return "aes"+(8*keyLength);
		}
	}
}