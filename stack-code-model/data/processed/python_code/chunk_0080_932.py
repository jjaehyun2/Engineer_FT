package qihoo.triplecleangame.protos {
	import com.netease.protobuf.*;
	import com.netease.protobuf.fieldDescriptors.*;
	import flash.utils.Endian;
	import flash.utils.IDataInput;
	import flash.utils.IDataOutput;
	import flash.utils.IExternalizable;
	import flash.errors.IOError;
	import qihoo.triplecleangame.protos.PBFriendList;
	// @@protoc_insertion_point(imports)

	// @@protoc_insertion_point(class_metadata)
	public dynamic final class CMsgGetFriendScoreRequest extends com.netease.protobuf.Message {
		public static const LEVEL:FieldDescriptor$TYPE_INT32 = new FieldDescriptor$TYPE_INT32("qihoo.triplecleangame.protos.CMsgGetFriendScoreRequest.level", "level", (1 << 3) | com.netease.protobuf.WireType.VARINT);

		private var level$field:int;

		private var hasField$0:uint = 0;

		public function clearLevel():void {
			hasField$0 &= 0xfffffffe;
			level$field = new int();
		}

		public function get hasLevel():Boolean {
			return (hasField$0 & 0x1) != 0;
		}

		public function set level(value:int):void {
			hasField$0 |= 0x1;
			level$field = value;
		}

		public function get level():int {
			return level$field;
		}

		public static const FRIENDQID:RepeatedFieldDescriptor$TYPE_MESSAGE = new RepeatedFieldDescriptor$TYPE_MESSAGE("qihoo.triplecleangame.protos.CMsgGetFriendScoreRequest.friendQID", "friendQID", (2 << 3) | com.netease.protobuf.WireType.LENGTH_DELIMITED, qihoo.triplecleangame.protos.PBFriendList);

		[ArrayElementType("qihoo.triplecleangame.protos.PBFriendList")]
		public var friendQID:Array = [];

		/**
		 *  @private
		 */
		override public final function writeToBuffer(output:com.netease.protobuf.WritingBuffer):void {
			if (hasLevel) {
				com.netease.protobuf.WriteUtils.writeTag(output, com.netease.protobuf.WireType.VARINT, 1);
				com.netease.protobuf.WriteUtils.write$TYPE_INT32(output, level$field);
			}
			for (var friendQID$index:uint = 0; friendQID$index < this.friendQID.length; ++friendQID$index) {
				com.netease.protobuf.WriteUtils.writeTag(output, com.netease.protobuf.WireType.LENGTH_DELIMITED, 2);
				com.netease.protobuf.WriteUtils.write$TYPE_MESSAGE(output, this.friendQID[friendQID$index]);
			}
			for (var fieldKey:* in this) {
				super.writeUnknown(output, fieldKey);
			}
		}

		/**
		 *  @private
		 */
		override public final function readFromSlice(input:flash.utils.IDataInput, bytesAfterSlice:uint):void {
			var level$count:uint = 0;
			while (input.bytesAvailable > bytesAfterSlice) {
				var tag:uint = com.netease.protobuf.ReadUtils.read$TYPE_UINT32(input);
				switch (tag >> 3) {
				case 1:
					if (level$count != 0) {
						throw new flash.errors.IOError('Bad data format: CMsgGetFriendScoreRequest.level cannot be set twice.');
					}
					++level$count;
					this.level = com.netease.protobuf.ReadUtils.read$TYPE_INT32(input);
					break;
				case 2:
					this.friendQID.push(com.netease.protobuf.ReadUtils.read$TYPE_MESSAGE(input, new qihoo.triplecleangame.protos.PBFriendList()));
					break;
				default:
					super.readUnknown(input, tag);
					break;
				}
			}
		}

	}
}