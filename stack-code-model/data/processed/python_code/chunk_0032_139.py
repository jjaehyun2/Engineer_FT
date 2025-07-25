/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 */
package com.evernote.edam.notestore {

import org.apache.thrift.Set;
import org.apache.thrift.type.BigInteger;
import flash.utils.ByteArray;
import flash.utils.Dictionary;

import org.apache.thrift.*;
import org.apache.thrift.meta_data.*;
import org.apache.thrift.protocol.*;


  /**
   * Identifying information about previous versions of a note that are backed up
   * within Evernote's servers.  Used in the return value of the listNoteVersions
   * call.
   * 
   * <dl>
   *  <dt>updateSequenceNum</dt>
   *  <dd>
   *    The update sequence number for the Note when it last had this content.
   *    This serves to uniquely identify each version of the note, since USN
   *    values are unique within an account for each update.
   *  </dd>
   *  <dt>updated</dt>
   *  <dd>
   *    The 'updated' time that was set on the Note when it had this version
   *    of the content.  This is the user-modifiable modification time on the
   *    note, so it's not reliable for guaranteeing the order of various
   *    versions.  (E.g. if someone modifies the note, then changes this time
   *    manually into the past and then updates the note again.)
   *  </dd>
   *  <dt>saved</dt>
   *  <dd>
   *    A timestamp that holds the date and time when this version of the note
   *    was backed up by Evernote's servers.  This
   *  </dd>
   *  <dt>title</dt>
   *  <dd>
   *    The title of the note when this particular version was saved.  (The
   *    current title of the note may differ from this value.)
   *  </dd>
   * </dl>
   */
  public class NoteVersionId implements TBase   {
    private static const STRUCT_DESC:TStruct = new TStruct("NoteVersionId");
    private static const UPDATE_SEQUENCE_NUM_FIELD_DESC:TField = new TField("updateSequenceNum", TType.I32, 1);
    private static const UPDATED_FIELD_DESC:TField = new TField("updated", TType.I64, 2);
    private static const SAVED_FIELD_DESC:TField = new TField("saved", TType.I64, 3);
    private static const TITLE_FIELD_DESC:TField = new TField("title", TType.STRING, 4);

    private var _updateSequenceNum:int;
    public static const UPDATESEQUENCENUM:int = 1;
    private var _updated:BigInteger;
    public static const UPDATED:int = 2;
    private var _saved:BigInteger;
    public static const SAVED:int = 3;
    private var _title:String;
    public static const TITLE:int = 4;

    private var __isset_updateSequenceNum:Boolean = false;
    private var __isset_updated:Boolean = false;
    private var __isset_saved:Boolean = false;

    public static const metaDataMap:Dictionary = new Dictionary();
    {
      metaDataMap[UPDATESEQUENCENUM] = new FieldMetaData("updateSequenceNum", TFieldRequirementType.REQUIRED, 
          new FieldValueMetaData(TType.I32));
      metaDataMap[UPDATED] = new FieldMetaData("updated", TFieldRequirementType.REQUIRED, 
          new FieldValueMetaData(TType.I64));
      metaDataMap[SAVED] = new FieldMetaData("saved", TFieldRequirementType.REQUIRED, 
          new FieldValueMetaData(TType.I64));
      metaDataMap[TITLE] = new FieldMetaData("title", TFieldRequirementType.REQUIRED, 
          new FieldValueMetaData(TType.STRING));
    }
    {
      FieldMetaData.addStructMetaDataMap(NoteVersionId, metaDataMap);
    }

    public function NoteVersionId() {
    }

    public function get updateSequenceNum():int {
      return this._updateSequenceNum;
    }

    public function set updateSequenceNum(updateSequenceNum:int):void {
      this._updateSequenceNum = updateSequenceNum;
      this.__isset_updateSequenceNum = true;
    }

    public function unsetUpdateSequenceNum():void {
      this.__isset_updateSequenceNum = false;
    }

    // Returns true if field updateSequenceNum is set (has been assigned a value) and false otherwise
    public function isSetUpdateSequenceNum():Boolean {
      return this.__isset_updateSequenceNum;
    }

    public function get updated():BigInteger {
      return this._updated;
    }

    public function set updated(updated:BigInteger):void {
      this._updated = updated;
      this.__isset_updated = true;
    }

    public function unsetUpdated():void {
      this.__isset_updated = false;
    }

    // Returns true if field updated is set (has been assigned a value) and false otherwise
    public function isSetUpdated():Boolean {
      return this.__isset_updated;
    }

    public function get saved():BigInteger {
      return this._saved;
    }

    public function set saved(saved:BigInteger):void {
      this._saved = saved;
      this.__isset_saved = true;
    }

    public function unsetSaved():void {
      this.__isset_saved = false;
    }

    // Returns true if field saved is set (has been assigned a value) and false otherwise
    public function isSetSaved():Boolean {
      return this.__isset_saved;
    }

    public function get title():String {
      return this._title;
    }

    public function set title(title:String):void {
      this._title = title;
    }

    public function unsetTitle():void {
      this.title = null;
    }

    // Returns true if field title is set (has been assigned a value) and false otherwise
    public function isSetTitle():Boolean {
      return this.title != null;
    }

    public function setFieldValue(fieldID:int, value:*):void {
      switch (fieldID) {
      case UPDATESEQUENCENUM:
        if (value == null) {
          unsetUpdateSequenceNum();
        } else {
          this.updateSequenceNum = value;
        }
        break;

      case UPDATED:
        if (value == null) {
          unsetUpdated();
        } else {
          this.updated = value;
        }
        break;

      case SAVED:
        if (value == null) {
          unsetSaved();
        } else {
          this.saved = value;
        }
        break;

      case TITLE:
        if (value == null) {
          unsetTitle();
        } else {
          this.title = value;
        }
        break;

      default:
        throw new ArgumentError("Field " + fieldID + " doesn't exist!");
      }
    }

    public function getFieldValue(fieldID:int):* {
      switch (fieldID) {
      case UPDATESEQUENCENUM:
        return this.updateSequenceNum;
      case UPDATED:
        return this.updated;
      case SAVED:
        return this.saved;
      case TITLE:
        return this.title;
      default:
        throw new ArgumentError("Field " + fieldID + " doesn't exist!");
      }
    }

    // Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise
    public function isSet(fieldID:int):Boolean {
      switch (fieldID) {
      case UPDATESEQUENCENUM:
        return isSetUpdateSequenceNum();
      case UPDATED:
        return isSetUpdated();
      case SAVED:
        return isSetSaved();
      case TITLE:
        return isSetTitle();
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
          case UPDATESEQUENCENUM:
            if (field.type == TType.I32) {
              this.updateSequenceNum = iprot.readI32();
              this.__isset_updateSequenceNum = true;
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case UPDATED:
            if (field.type == TType.I64) {
              this.updated = iprot.readI64();
              this.__isset_updated = true;
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case SAVED:
            if (field.type == TType.I64) {
              this.saved = iprot.readI64();
              this.__isset_saved = true;
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case TITLE:
            if (field.type == TType.STRING) {
              this.title = iprot.readString();
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
      if (!__isset_updateSequenceNum) {
        throw new TProtocolError(TProtocolError.UNKNOWN, "Required field 'updateSequenceNum' was not found in serialized data! Struct: " + toString());
      }
      if (!__isset_updated) {
        throw new TProtocolError(TProtocolError.UNKNOWN, "Required field 'updated' was not found in serialized data! Struct: " + toString());
      }
      if (!__isset_saved) {
        throw new TProtocolError(TProtocolError.UNKNOWN, "Required field 'saved' was not found in serialized data! Struct: " + toString());
      }
      validate();
    }

    public function write(oprot:TProtocol):void {
      validate();

      oprot.writeStructBegin(STRUCT_DESC);
      oprot.writeFieldBegin(UPDATE_SEQUENCE_NUM_FIELD_DESC);
      oprot.writeI32(this.updateSequenceNum);
      oprot.writeFieldEnd();
      oprot.writeFieldBegin(UPDATED_FIELD_DESC);
      oprot.writeI64(this.updated);
      oprot.writeFieldEnd();
      oprot.writeFieldBegin(SAVED_FIELD_DESC);
      oprot.writeI64(this.saved);
      oprot.writeFieldEnd();
      if (this.title != null) {
        oprot.writeFieldBegin(TITLE_FIELD_DESC);
        oprot.writeString(this.title);
        oprot.writeFieldEnd();
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

    public function toString():String {
      var ret:String = new String("NoteVersionId(");
      var first:Boolean = true;

      ret += "updateSequenceNum:";
      ret += this.updateSequenceNum;
      first = false;
      if (!first) ret +=  ", ";
      ret += "updated:";
      ret += this.updated;
      first = false;
      if (!first) ret +=  ", ";
      ret += "saved:";
      ret += this.saved;
      first = false;
      if (!first) ret +=  ", ";
      ret += "title:";
      if (this.title == null) {
        ret += "null";
      } else {
        ret += this.title;
      }
      first = false;
      ret += ")";
      return ret;
    }

    public function validate():void {
      // check for required fields
      // alas, we cannot check 'updateSequenceNum' because it's a primitive and you chose the non-beans generator.
      // alas, we cannot check 'updated' because it's a primitive and you chose the non-beans generator.
      // alas, we cannot check 'saved' because it's a primitive and you chose the non-beans generator.
      if (title == null) {
        throw new TProtocolError(TProtocolError.UNKNOWN, "Required field 'title' was not present! Struct: " + toString());
      }
      // check that fields of type enum have valid values
    }

  }

}