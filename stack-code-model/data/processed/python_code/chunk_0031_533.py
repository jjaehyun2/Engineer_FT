/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 */
package com.evernote.edam.error {

import org.apache.thrift.Set;
import org.apache.thrift.type.BigInteger;
import flash.utils.ByteArray;
import flash.utils.Dictionary;

import org.apache.thrift.*;
import org.apache.thrift.meta_data.*;
import org.apache.thrift.protocol.*;

import com.evernote.edam.error.EDAMErrorCode;

  /**
   * This exception is thrown by EDAM procedures when a call fails as a result of
   * a problem in the service that could not be changed through caller action.
   * 
   * errorCode:  The numeric code indicating the type of error that occurred.
   *   must be one of the values of EDAMErrorCode.
   * 
   * message:  This may contain additional information about the error
   */
  public class EDAMSystemException implements TBase   {
    private static const STRUCT_DESC:TStruct = new TStruct("EDAMSystemException");
    private static const ERROR_CODE_FIELD_DESC:TField = new TField("errorCode", TType.I32, 1);
    private static const MESSAGE_FIELD_DESC:TField = new TField("message", TType.STRING, 2);

    private var _errorCode:int;
    public static const ERRORCODE:int = 1;
    private var _message:String;
    public static const MESSAGE:int = 2;

    private var __isset_errorCode:Boolean = false;

    public static const metaDataMap:Dictionary = new Dictionary();
    {
      metaDataMap[ERRORCODE] = new FieldMetaData("errorCode", TFieldRequirementType.REQUIRED, 
          new FieldValueMetaData(TType.I32));
      metaDataMap[MESSAGE] = new FieldMetaData("message", TFieldRequirementType.OPTIONAL, 
          new FieldValueMetaData(TType.STRING));
    }
    {
      FieldMetaData.addStructMetaDataMap(EDAMSystemException, metaDataMap);
    }

    public function EDAMSystemException() {
    }

    public function get errorCode():int {
      return this._errorCode;
    }

    public function set errorCode(errorCode:int):void {
      this._errorCode = errorCode;
      this.__isset_errorCode = true;
    }

    public function unsetErrorCode():void {
      this.__isset_errorCode = false;
    }

    // Returns true if field errorCode is set (has been assigned a value) and false otherwise
    public function isSetErrorCode():Boolean {
      return this.__isset_errorCode;
    }

    public function get message():String {
      return this._message;
    }

    public function set message(message:String):void {
      this._message = message;
    }

    public function unsetMessage():void {
      this.message = null;
    }

    // Returns true if field message is set (has been assigned a value) and false otherwise
    public function isSetMessage():Boolean {
      return this.message != null;
    }

    public function setFieldValue(fieldID:int, value:*):void {
      switch (fieldID) {
      case ERRORCODE:
        if (value == null) {
          unsetErrorCode();
        } else {
          this.errorCode = value;
        }
        break;

      case MESSAGE:
        if (value == null) {
          unsetMessage();
        } else {
          this.message = value;
        }
        break;

      default:
        throw new ArgumentError("Field " + fieldID + " doesn't exist!");
      }
    }

    public function getFieldValue(fieldID:int):* {
      switch (fieldID) {
      case ERRORCODE:
        return this.errorCode;
      case MESSAGE:
        return this.message;
      default:
        throw new ArgumentError("Field " + fieldID + " doesn't exist!");
      }
    }

    // Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise
    public function isSet(fieldID:int):Boolean {
      switch (fieldID) {
      case ERRORCODE:
        return isSetErrorCode();
      case MESSAGE:
        return isSetMessage();
      default:
        throw new ArgumentError("Field " + fieldID + " doesn't exist!");
      }
    }

    public function read(iprot:TProtocol):void {
      var field:TField;
      iprot.readStructBegin();
      while (true)
      {
        field = iprot.readFieldBegin();
        if (field.type == TType.STOP) { 
          break;
        }
        switch (field.id)
        {
          case ERRORCODE:
            if (field.type == TType.I32) {
              this.errorCode = iprot.readI32();
              this.__isset_errorCode = true;
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case MESSAGE:
            if (field.type == TType.STRING) {
              this.message = iprot.readString();
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          default:
            TProtocolUtil.skip(iprot, field.type);
            break;
        }
        iprot.readFieldEnd();
      }
      iprot.readStructEnd();


      // check for required fields of primitive type, which can't be checked in the validate method
      if (!__isset_errorCode) {
        throw new TProtocolError(TProtocolError.UNKNOWN, "Required field 'errorCode' was not found in serialized data! Struct: " + toString());
      }
      validate();
    }

    public function write(oprot:TProtocol):void {
      validate();

      oprot.writeStructBegin(STRUCT_DESC);
      oprot.writeFieldBegin(ERROR_CODE_FIELD_DESC);
      oprot.writeI32(this.errorCode);
      oprot.writeFieldEnd();
      if (this.message != null) {
        if (isSetMessage()) {
          oprot.writeFieldBegin(MESSAGE_FIELD_DESC);
          oprot.writeString(this.message);
          oprot.writeFieldEnd();
        }
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

    public function toString():String {
      var ret:String = new String("EDAMSystemException(");
      var first:Boolean = true;

      ret += "errorCode:";
      var errorCode_name:String = EDAMErrorCode.VALUES_TO_NAMES[this.errorCode];
      if (errorCode_name != null) {
        ret += errorCode_name;
        ret += " (";
      }
      ret += this.errorCode;
      if (errorCode_name != null) {
        ret += ")";
      }
      first = false;
      if (isSetMessage()) {
        if (!first) ret +=  ", ";
        ret += "message:";
        if (this.message == null) {
          ret += "null";
        } else {
          ret += this.message;
        }
        first = false;
      }
      ret += ")";
      return ret;
    }

    public function validate():void {
      // check for required fields
      // alas, we cannot check 'errorCode' because it's a primitive and you chose the non-beans generator.
      // check that fields of type enum have valid values
      if (isSetErrorCode() && !EDAMErrorCode.VALID_VALUES.contains(errorCode)){
        throw new TProtocolError(TProtocolError.UNKNOWN, "The field 'errorCode' has been assigned the invalid value " + errorCode);
      }
    }

  }

}