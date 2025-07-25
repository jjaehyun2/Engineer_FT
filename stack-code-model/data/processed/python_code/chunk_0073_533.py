// vim: tabstop=4 shiftwidth=4

// Copyright (c) 2011 , Yang Bo All rights reserved.
//
// Author: Yang Bo (pop.atry@gmail.com)
//
// Use, modification and distribution are subject to the "New BSD License"
// as listed at <url: http://www.opensource.org/licenses/bsd-license.php >.

package com.netease.protobuf.fieldDescriptors {
	import com.netease.protobuf.*
	import flash.utils.*
	/**
	 * @private
	 */
	public final class FieldDescriptor$TYPE_ENUM extends
			FieldDescriptor {
		public var enumType:Class
		public function FieldDescriptor$TYPE_ENUM(
				fullName:String, name:String, tag:uint, enumType:Class) {
			this.fullName = fullName
			this._name = name
			this.tag = tag
			this.enumType = enumType
		}
		override public function get type():Class {
			return int
		}
		override public function readSingleField(input:IDataInput):* {
			return ReadUtils.read$TYPE_ENUM(input)
		}
		override public function writeSingleField(output:WritingBuffer,
				value:*):void {
			WriteUtils.write$TYPE_ENUM(output, value)
		}
	}
}