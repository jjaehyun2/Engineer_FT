package roshan.buffer {
	import com.netease.protobuf.*;
	use namespace com.netease.protobuf.used_by_generated_code;
	import com.netease.protobuf.fieldDescriptors.*;
	import flash.utils.Endian;
	import flash.utils.IDataInput;
	import flash.utils.IDataOutput;
	import flash.utils.IExternalizable;
	import flash.errors.IOError;
	import roshan.buffer.ACTION;
	import roshan.buffer.CHARACTER_TYPE;
	// @@protoc_insertion_point(imports)

	// @@protoc_insertion_point(class_metadata)
	public dynamic final class CharacterAction extends com.netease.protobuf.Message {
		/**
		 *  @private
		 */
		public static const ID:FieldDescriptor_TYPE_UINT32 = new FieldDescriptor_TYPE_UINT32("roshan.buffer.CharacterAction.id", "id", (1 << 3) | com.netease.protobuf.WireType.VARINT);

		public var id:uint;

		/**
		 *  @private
		 */
		public static const X:FieldDescriptor_TYPE_SINT32 = new FieldDescriptor_TYPE_SINT32("roshan.buffer.CharacterAction.x", "x", (2 << 3) | com.netease.protobuf.WireType.VARINT);

		private var x$field:int;

		private var hasField$0:uint = 0;

		public function clearX():void {
			hasField$0 &= 0xfffffffe;
			x$field = new int();
		}

		public function get hasX():Boolean {
			return (hasField$0 & 0x1) != 0;
		}

		public function set x(value:int):void {
			hasField$0 |= 0x1;
			x$field = value;
		}

		public function get x():int {
			return x$field;
		}

		/**
		 *  @private
		 */
		public static const Y:FieldDescriptor_TYPE_SINT32 = new FieldDescriptor_TYPE_SINT32("roshan.buffer.CharacterAction.y", "y", (3 << 3) | com.netease.protobuf.WireType.VARINT);

		private var y$field:int;

		public function clearY():void {
			hasField$0 &= 0xfffffffd;
			y$field = new int();
		}

		public function get hasY():Boolean {
			return (hasField$0 & 0x2) != 0;
		}

		public function set y(value:int):void {
			hasField$0 |= 0x2;
			y$field = value;
		}

		public function get y():int {
			return y$field;
		}

		/**
		 *  @private
		 */
		public static const SAY:FieldDescriptor_TYPE_STRING = new FieldDescriptor_TYPE_STRING("roshan.buffer.CharacterAction.say", "say", (4 << 3) | com.netease.protobuf.WireType.LENGTH_DELIMITED);

		private var say$field:String;

		public function clearSay():void {
			say$field = null;
		}

		public function get hasSay():Boolean {
			return say$field != null;
		}

		public function set say(value:String):void {
			say$field = value;
		}

		public function get say():String {
			return say$field;
		}

		/**
		 *  @private
		 */
		public static const WALK:FieldDescriptor_TYPE_BOOL = new FieldDescriptor_TYPE_BOOL("roshan.buffer.CharacterAction.walk", "walk", (7 << 3) | com.netease.protobuf.WireType.VARINT);

		private var walk$field:Boolean;

		public function clearWalk():void {
			hasField$0 &= 0xfffffffb;
			walk$field = new Boolean();
		}

		public function get hasWalk():Boolean {
			return (hasField$0 & 0x4) != 0;
		}

		public function set walk(value:Boolean):void {
			hasField$0 |= 0x4;
			walk$field = value;
		}

		public function get walk():Boolean {
			return walk$field;
		}

		/**
		 *  @private
		 */
		public static const DIRECTION:FieldDescriptor_TYPE_UINT32 = new FieldDescriptor_TYPE_UINT32("roshan.buffer.CharacterAction.direction", "direction", (8 << 3) | com.netease.protobuf.WireType.VARINT);

		private var direction$field:uint;

		public function clearDirection():void {
			hasField$0 &= 0xfffffff7;
			direction$field = new uint();
		}

		public function get hasDirection():Boolean {
			return (hasField$0 & 0x8) != 0;
		}

		public function set direction(value:uint):void {
			hasField$0 |= 0x8;
			direction$field = value;
		}

		public function get direction():uint {
			return direction$field;
		}

		/**
		 *  @private
		 */
		public static const ACTION:FieldDescriptor_TYPE_ENUM = new FieldDescriptor_TYPE_ENUM("roshan.buffer.CharacterAction.action", "action", (9 << 3) | com.netease.protobuf.WireType.VARINT, roshan.buffer.ACTION);

		private var action$field:int;

		public function clearAction():void {
			hasField$0 &= 0xffffffef;
			action$field = new int();
		}

		public function get hasAction():Boolean {
			return (hasField$0 & 0x10) != 0;
		}

		public function set action(value:int):void {
			hasField$0 |= 0x10;
			action$field = value;
		}

		public function get action():int {
			return action$field;
		}

		/**
		 *  @private
		 */
		public static const ISYOU:FieldDescriptor_TYPE_BOOL = new FieldDescriptor_TYPE_BOOL("roshan.buffer.CharacterAction.isYou", "isYou", (11 << 3) | com.netease.protobuf.WireType.VARINT);

		private var isYou$field:Boolean;

		public function clearIsYou():void {
			hasField$0 &= 0xffffffdf;
			isYou$field = new Boolean();
		}

		public function get hasIsYou():Boolean {
			return (hasField$0 & 0x20) != 0;
		}

		public function set isYou(value:Boolean):void {
			hasField$0 |= 0x20;
			isYou$field = value;
		}

		public function get isYou():Boolean {
			return isYou$field;
		}

		/**
		 *  @private
		 */
		public static const GONE:FieldDescriptor_TYPE_BOOL = new FieldDescriptor_TYPE_BOOL("roshan.buffer.CharacterAction.gone", "gone", (12 << 3) | com.netease.protobuf.WireType.VARINT);

		private var gone$field:Boolean;

		public function clearGone():void {
			hasField$0 &= 0xffffffbf;
			gone$field = new Boolean();
		}

		public function get hasGone():Boolean {
			return (hasField$0 & 0x40) != 0;
		}

		public function set gone(value:Boolean):void {
			hasField$0 |= 0x40;
			gone$field = value;
		}

		public function get gone():Boolean {
			return gone$field;
		}

		/**
		 *  @private
		 */
		public static const CHARACTERTYPE:FieldDescriptor_TYPE_ENUM = new FieldDescriptor_TYPE_ENUM("roshan.buffer.CharacterAction.characterType", "characterType", (13 << 3) | com.netease.protobuf.WireType.VARINT, roshan.buffer.CHARACTER_TYPE);

		private var characterType$field:int;

		public function clearCharacterType():void {
			hasField$0 &= 0xffffff7f;
			characterType$field = new int();
		}

		public function get hasCharacterType():Boolean {
			return (hasField$0 & 0x80) != 0;
		}

		public function set characterType(value:int):void {
			hasField$0 |= 0x80;
			characterType$field = value;
		}

		public function get characterType():int {
			return characterType$field;
		}

		/**
		 *  @private
		 */
		override com.netease.protobuf.used_by_generated_code final function writeToBuffer(output:com.netease.protobuf.WritingBuffer):void {
			com.netease.protobuf.WriteUtils.writeTag(output, com.netease.protobuf.WireType.VARINT, 1);
			com.netease.protobuf.WriteUtils.write_TYPE_UINT32(output, this.id);
			if (hasX) {
				com.netease.protobuf.WriteUtils.writeTag(output, com.netease.protobuf.WireType.VARINT, 2);
				com.netease.protobuf.WriteUtils.write_TYPE_SINT32(output, x$field);
			}
			if (hasY) {
				com.netease.protobuf.WriteUtils.writeTag(output, com.netease.protobuf.WireType.VARINT, 3);
				com.netease.protobuf.WriteUtils.write_TYPE_SINT32(output, y$field);
			}
			if (hasSay) {
				com.netease.protobuf.WriteUtils.writeTag(output, com.netease.protobuf.WireType.LENGTH_DELIMITED, 4);
				com.netease.protobuf.WriteUtils.write_TYPE_STRING(output, say$field);
			}
			if (hasWalk) {
				com.netease.protobuf.WriteUtils.writeTag(output, com.netease.protobuf.WireType.VARINT, 7);
				com.netease.protobuf.WriteUtils.write_TYPE_BOOL(output, walk$field);
			}
			if (hasDirection) {
				com.netease.protobuf.WriteUtils.writeTag(output, com.netease.protobuf.WireType.VARINT, 8);
				com.netease.protobuf.WriteUtils.write_TYPE_UINT32(output, direction$field);
			}
			if (hasAction) {
				com.netease.protobuf.WriteUtils.writeTag(output, com.netease.protobuf.WireType.VARINT, 9);
				com.netease.protobuf.WriteUtils.write_TYPE_ENUM(output, action$field);
			}
			if (hasIsYou) {
				com.netease.protobuf.WriteUtils.writeTag(output, com.netease.protobuf.WireType.VARINT, 11);
				com.netease.protobuf.WriteUtils.write_TYPE_BOOL(output, isYou$field);
			}
			if (hasGone) {
				com.netease.protobuf.WriteUtils.writeTag(output, com.netease.protobuf.WireType.VARINT, 12);
				com.netease.protobuf.WriteUtils.write_TYPE_BOOL(output, gone$field);
			}
			if (hasCharacterType) {
				com.netease.protobuf.WriteUtils.writeTag(output, com.netease.protobuf.WireType.VARINT, 13);
				com.netease.protobuf.WriteUtils.write_TYPE_ENUM(output, characterType$field);
			}
			for (var fieldKey:* in this) {
				super.writeUnknown(output, fieldKey);
			}
		}

		/**
		 *  @private
		 */
		override com.netease.protobuf.used_by_generated_code final function readFromSlice(input:flash.utils.IDataInput, bytesAfterSlice:uint):void {
			var id$count:uint = 0;
			var x$count:uint = 0;
			var y$count:uint = 0;
			var say$count:uint = 0;
			var walk$count:uint = 0;
			var direction$count:uint = 0;
			var action$count:uint = 0;
			var isYou$count:uint = 0;
			var gone$count:uint = 0;
			var characterType$count:uint = 0;
			while (input.bytesAvailable > bytesAfterSlice) {
				var tag:uint = com.netease.protobuf.ReadUtils.read_TYPE_UINT32(input);
				switch (tag >> 3) {
				case 1:
					if (id$count != 0) {
						throw new flash.errors.IOError('Bad data format: CharacterAction.id cannot be set twice.');
					}
					++id$count;
					this.id = com.netease.protobuf.ReadUtils.read_TYPE_UINT32(input);
					break;
				case 2:
					if (x$count != 0) {
						throw new flash.errors.IOError('Bad data format: CharacterAction.x cannot be set twice.');
					}
					++x$count;
					this.x = com.netease.protobuf.ReadUtils.read_TYPE_SINT32(input);
					break;
				case 3:
					if (y$count != 0) {
						throw new flash.errors.IOError('Bad data format: CharacterAction.y cannot be set twice.');
					}
					++y$count;
					this.y = com.netease.protobuf.ReadUtils.read_TYPE_SINT32(input);
					break;
				case 4:
					if (say$count != 0) {
						throw new flash.errors.IOError('Bad data format: CharacterAction.say cannot be set twice.');
					}
					++say$count;
					this.say = com.netease.protobuf.ReadUtils.read_TYPE_STRING(input);
					break;
				case 7:
					if (walk$count != 0) {
						throw new flash.errors.IOError('Bad data format: CharacterAction.walk cannot be set twice.');
					}
					++walk$count;
					this.walk = com.netease.protobuf.ReadUtils.read_TYPE_BOOL(input);
					break;
				case 8:
					if (direction$count != 0) {
						throw new flash.errors.IOError('Bad data format: CharacterAction.direction cannot be set twice.');
					}
					++direction$count;
					this.direction = com.netease.protobuf.ReadUtils.read_TYPE_UINT32(input);
					break;
				case 9:
					if (action$count != 0) {
						throw new flash.errors.IOError('Bad data format: CharacterAction.action cannot be set twice.');
					}
					++action$count;
					this.action = com.netease.protobuf.ReadUtils.read_TYPE_ENUM(input);
					break;
				case 11:
					if (isYou$count != 0) {
						throw new flash.errors.IOError('Bad data format: CharacterAction.isYou cannot be set twice.');
					}
					++isYou$count;
					this.isYou = com.netease.protobuf.ReadUtils.read_TYPE_BOOL(input);
					break;
				case 12:
					if (gone$count != 0) {
						throw new flash.errors.IOError('Bad data format: CharacterAction.gone cannot be set twice.');
					}
					++gone$count;
					this.gone = com.netease.protobuf.ReadUtils.read_TYPE_BOOL(input);
					break;
				case 13:
					if (characterType$count != 0) {
						throw new flash.errors.IOError('Bad data format: CharacterAction.characterType cannot be set twice.');
					}
					++characterType$count;
					this.characterType = com.netease.protobuf.ReadUtils.read_TYPE_ENUM(input);
					break;
				default:
					super.readUnknown(input, tag);
					break;
				}
			}
		}

	}
}