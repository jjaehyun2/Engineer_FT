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
   * a problem that a caller may be able to resolve.  For example, if the user
   * attempts to add a note to their account which would exceed their storage
   * quota, this type of exception may be thrown to indicate the source of the
   * error so that they can choose an alternate action.
   * 
   * This exception would not be used for internal system errors that do not
   * reflect user actions, but rather reflect a problem within the service that
   * the user cannot resolve.
   * 
   * errorCode:  The numeric code indicating the type of error that occurred.
   *   must be one of the values of EDAMErrorCode.
   * 
   * parameter:  If the error applied to a particular input parameter, this will
   *   indicate which parameter.
   */
  public class EDAMUserException implements TBase   {
    private static const STRUCT_DESC:TStruct = new TStruct("EDAMUserException");
    private static const ERROR_CODE_FIELD_DESC:TField = new TField("errorCode", TType.I32, 1);
    private static const PARAMETER_FIELD_DESC:TField = new TField("parameter", TType.STRING, 2);

    private var _errorCode:int;
    public static const ERRORCODE:int = 1;
    private var _parameter:String;
    public static const PARAMETER:int = 2;

    private var __isset_errorCode:Boolean = false;

    public static const metaDataMap:Dictionary = new Dictionary();
    {
      metaDataMap[ERRORCODE] = new FieldMetaData("errorCode", TFieldRequirementType.REQUIRED, 
          new FieldValueMetaData(TType.I32));
      metaDataMap[PARAMETER] = new FieldMetaData("parameter", TFieldRequirementType.OPTIONAL, 
          new FieldValueMetaData(TType.STRING));
    }
    {
      FieldMetaData.addStructMetaDataMap(EDAMUserException, metaDataMap);
    }

    public function EDAMUserException() {
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

    public function get parameter():String {
      return this._parameter;
    }

    public function set parameter(parameter:String):void {
      this._parameter = parameter;
    }

    public function unsetParameter():void {
      this.parameter = null;
    }

    // Returns true if field parameter is set (has been assigned a value) and false otherwise
    public function isSetParameter():Boolean {
      return this.parameter != null;
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

      case PARAMETER:
        if (value == null) {
          unsetParameter();
        } else {
          this.parameter = value;
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
      case PARAMETER:
        return this.parameter;
      default:
        throw new ArgumentError("Field " + fieldID + " doesn't exist!");
      }
    }

    // Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise
    public function isSet(fieldID:int):Boolean {
      switch (fieldID) {
      case ERRORCODE:
        return isSetErrorCode();
      case PARAMETER:
        return isSetParameter();
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
          case PARAMETER:
            if (field.type == TType.STRING) {
              this.parameter = iprot.readString();
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
      if (this.parameter != null) {
        if (isSetParameter()) {
          oprot.writeFieldBegin(PARAMETER_FIELD_DESC);
          oprot.writeString(this.parameter);
          oprot.writeFieldEnd();
        }
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

    public function toString():String {
      var ret:String = new String("EDAMUserException(");
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
      if (isSetParameter()) {
        if (!first) ret +=  ", ";
        ret += "parameter:";
        if (this.parameter == null) {
          ret += "null";
        } else {
          ret += this.parameter;
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