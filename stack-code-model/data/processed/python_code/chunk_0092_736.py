/**
 *  GODPAPER Confidential,Copyright 2012. All rights reserved.
 *
 *  Permission is hereby granted, free of charge, to any person obtaining
 *  a copy of this software and associated documentation files (the "Software"),
 *  to deal in the Software without restriction, including without limitation
 *  the rights to use, copy, modify, merge, publish, distribute, sub-license,
 *  and/or sell copies of the Software, and to permit persons to whom the
 *  Software is furnished to do so, subject to the following conditions:
 *
 *  The above copyright notice and this permission notice shall be included
 *  in all copies or substantial portions of the Software.
 *
 *  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 *  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 *  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 *  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 *  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 *  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 *  IN THE SOFTWARE.
 */
package com.godpaper.mqtt.as3.core
{
	import flash.utils.ByteArray;
	import flash.utils.IDataInput;

	//--------------------------------------------------------------------------
	//
	//  Imports
	//
	//--------------------------------------------------------------------------

	/**
	 * MQTT_Protocol.as class.
	 * @see http://public.dhe.ibm.com/software/dw/webservices/ws-mqtt/MQTT_V3.1_Protocol_Specific.pdf
	 * @author yangboz
	 * @langVersion 3.0
	 * @playerVersion 11.2+
	 * @airVersion 3.2+
	 * Created Nov 20, 2012 10:49:53 AM
	 */
	public class MQTT_Protocol extends ByteArray
	{
		//--------------------------------------------------------------------------
		//
		//  Variables
		//
		//--------------------------------------------------------------------------

		//----------------------------------
		//  CONSTANTS
		//----------------------------------
		/* For version 3 of the MQTT protocol */
		/* Mosquitto MQTT Javascript/Websocket client */
		/* Provides complete support for QoS 0.
		* Will not cause an error on QoS 1/2 packets.
		*/
		public static const PROTOCOL_NAME:String="MQIsdp";
		public static const PROTOCOL_VERSION:Number=3;

		/* Message types */
		public static const CONNECT:uint=0x10;
		public static const CONNACK:uint=0x20;
		public static const PUBLISH:uint=0x30;
		public static const PUBACK:uint=0x40;
		public static const PUBREC:uint=0x50;
		public static const PUBREL:uint=0x60;
		public static const PUBCOMP:uint=0x70;
		public static const SUBSCRIBE:uint=0x80;
		public static const SUBACK:uint=0x90;
		public static const UNSUBSCRIBE:uint=0xA0;
		public static const UNSUBACK:uint=0xB0;
		public static const PINGREQ:uint=0xC0;
		public static const PINGRESP:uint=0xD0;
		public static const DISCONNECT:uint=0xE0;
		//
		public static const CONNACK_ACCEPTED:uint=0;
		public static const CONNACK_REFUSED_PROTOCOL_VERSION:int=1;
		public static const CONNACK_REFUSED_IDENTIFIER_REJECTED:int=2;
		public static const CONNACK_REFUSED_SERVER_UNAVAILABLE:int=3;
		public static const CONNACK_REFUSED_BAD_USERNAME_PASSWORD:int=4;
		public static const CONNACK_REFUSED_NOT_AUTHORIZED:int=5;

		public static const MQTT_MAX_PAYLOAD:int=268435455;

		protected var fixHead:ByteArray;
		protected var varHead:ByteArray;
		protected var payLoad:ByteArray;
		
		protected var type:uint;
		protected var dup:uint;
		protected var qos:uint;
		protected var retain:uint;
		protected var isLength:uint;
		protected var remainingLength:uint;
		protected var remainPosition:uint;
		
		public var readCompleted:Boolean = true;
		protected var readLength:uint;
		
		//--------------------------------------------------------------------------
		//
		//  Public properties
		//
		//-------------------------------------------------------------------------- 

		//--------------------------------------------------------------------------
		//
		//  Protected properties
		//
		//-------------------------------------------------------------------------- 

		//--------------------------------------------------------------------------
		//
		//  Constructor
		//
		//--------------------------------------------------------------------------
		public function MQTT_Protocol():void
		{
			super();
		}
		//--------------------------------------------------------------------------
		//
		//  Public methods
		//
		//--------------------------------------------------------------------------
		//
		public function writeType(value:int):void
		{
			type = value;
			writeMessageType(type + (dup << 3) + (qos << 1) + retain);
		}
		
		public function writeDUP(value:int):void
		{
			dup = value;
			writeMessageType(type + (dup << 3) + (qos << 1) + retain);
		}
		
		public function writeQoS(value:int):void
		{
			qos = value;
			writeMessageType(type + (dup << 3) + (qos << 1) + retain);
		}
		
		public function writeRETAIN(value:int):void
		{
			retain = value;
			writeMessageType(type + (dup << 3) + (qos << 1) + retain);
		}
		
		public function writeRemainingLength(value:int):void
		{
			remainingLength = value;
			writeMessageType(type + (dup << 3) + (qos << 1) + retain);
		}
		
		public function readType():uint
		{
			this.position=0;
			return this.readUnsignedByte() & 0xF0;
		}
		
		public function readDUP():uint
		{
			this.position=0;
			return this.readUnsignedByte() >> 3 & 0x01;
		}
		
		public function readQoS():uint
		{
			this.position=0;
			return this.readUnsignedByte() >> 1 & 0x03;
		}
		
		public function readRETAIN():uint
		{
			this.position=0;
			return this.readUnsignedByte() & 0x01;
		}
		
		public function readRemainingLength():uint
		{
			this.position = 1;
			return this.readUnsignedByte();
		}
		
		public function writeMessageTypeLength(value:int,length:int):void
		{
			this.position = 0;
			
			if( fixHead == null )
				fixHead = new ByteArray();
			
			this.position = 0;
			this.writeByte(value);
			var le:uint = length;
			var digit:uint = 0;
			this.isLength = 0;
			do {
				digit = le % 128;
				le = le / 128;
				if(le > 0 ){
					digit = digit| 0x80;
				}
				this.isLength++;
				this.writeByte(digit);
				
			}while(le > 0);
			
			this.remainPosition = this.position;
			
			//this.writeByte(remainingLength);
			this.readBytes(fixHead);
						
			type = value & 0xF0;
			dup = (value >> 3) & 0x01;
			qos = (value >> 1) & 0x03;
			retain = value & 0x01;
		}
		
		public function writeMessageValueWithEnd(value:*):void
		{
			this.position = isLength+1;		
			this.writeBytes(value);
			this.serialize();
		}
		
		
		public function writeMessageType(value:int):void//Fix Head
		{
			this.position = 0;
			
			if( fixHead == null )
				fixHead = new ByteArray();
			
			this.position = 0;
			this.writeByte(value);
			var le:uint = remainingLength;
			var digit:uint = 0;
			this.isLength = 0;
			do {
				digit = le % 128;
				le = le / 128;
				if(le > 0 ){
					digit = digit| 0x80;
				}
				this.isLength++;
				this.writeByte(digit);

			}while(le > 0);
			
			this.remainPosition = this.position;

			//this.writeByte(remainingLength);
			this.readBytes(fixHead);
						
			type = value & 0xF0;
			dup = (value >> 3) & 0x01;
			qos = (value >> 1) & 0x03;
			retain = value & 0x01;
		}
		

		public function writeMessageValue(value:*):void//Variable Head
		{
			this.position = this.isLength + 1;
			this.writeBytes(value);
			this.serialize();
			writeMessageType( type + (dup << 3) + (qos << 1) + retain );
		}
		
		public function writeMessageFromBytes(input:IDataInput):void
		{
			if (this.readCompleted) {
				this.position = 0;
				this.writeType(input.readUnsignedByte());
				//get VarHead and Payload use RemainingLength
				
				//remainingLength = input.readUnsignedByte();
				
				//input.readBytes(this, 2, remainingLength);
				
				var multiplier :uint = 1;
				var remainLength:uint = 0;
				do 
				{
					var le:uint = input.readUnsignedByte();
					remainLength += (le & 127) * multiplier;
					multiplier *= 128;
					
				}
				while ((le & 128) != 0);

				remainingLength = remainLength;
				this.readLength = remainLength;
				writeMessageType( type + (dup << 3) + (qos << 1) + retain );
				
				if (input.bytesAvailable >= readLength) {
					this.readCompleted = true;
					input.readBytes(this,this.remainPosition,this.remainingLength);
					serialize();
					
				} else {
					this.readCompleted = false;
					this.readLength = this.readLength - input.bytesAvailable;
					input.readBytes(this,this.remainPosition,input.bytesAvailable);
				}
			} else {
				// 获取socket的字节总数
				// 如果待读取长度大于字节长度，那么要标志为多次读取
				// 如果小于，那么读取需要字节数
				// 没有读完，那么读取余下的
				if (input.bytesAvailable >= readLength) {
					this.readCompleted = true;
					input.readBytes(this,this.length,this.readLength);
					serialize();
				} else {
					this.readLength = this.readLength - input.bytesAvailable;
					input.readBytes(this,this.length,input.bytesAvailable);
				}
			}
			
		}
		
		public function readMessageType():ByteArray
		{
			return fixHead;
		}
		
		public function readMessageValue():ByteArray
		{
			return varHead;
		}
		
		public function readPayLoad():ByteArray
		{
			return payLoad;
		}
		/**
		 * @see http://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/utils/IDataInput.html
		 */		
		public function serialize():void
		{
			type 	= this.readType();
			dup 	= this.readDUP();
			qos 	= this.readQoS();
			retain	= this.readRETAIN();
			
			fixHead = new ByteArray();
			varHead = new ByteArray();
			payLoad = new ByteArray();

			this.position = 0;
			this.readBytes(fixHead, 0, this.remainPosition);
			
			this.position = this.remainPosition;
			switch( type ){
				case CONNECT://Remaining Length is the length of the variable header (12 bytes) and the length of the Payload
					this.readBytes(varHead, 0 , 12);
					this.readBytes(payLoad);
					
					remainingLength = varHead.length + payLoad.length;
					break;
				case PUBLISH://Remaining Length is the length of the variable header plus the length of the payload
					var index:int = (this.readUnsignedByte() << 8) + this.readUnsignedByte();//the length of variable header
					this.position = this.remainPosition;
					this.readBytes(varHead, 0 , index + (qos?4:2));
					this.readBytes(payLoad);	

					remainingLength = varHead.length + payLoad.length;
					break;
				case SUBSCRIBE://Remaining Length is the length of the payload
				case SUBACK://Remaining Length is the length of the payload
				case UNSUBSCRIBE://Remaining Length is the length of the payload
					this.readBytes(varHead, 0 , 2);
					this.readBytes(payLoad);
					
					remainingLength = varHead.length + payLoad.length;
					break;
				default://Remaining Length is the length of the variable header (2 bytes)
					this.readBytes(varHead);
					
					remainingLength = varHead.length;
					break;
			}
		}
		//--------------------------------------------------------------------------
		//
		//  Protected methods
		//
		//--------------------------------------------------------------------------

		//--------------------------------------------------------------------------
		//
		//  Private methods
		//
		//--------------------------------------------------------------------------
	}

}