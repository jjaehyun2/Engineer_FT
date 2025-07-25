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

import com.evernote.edam.type.Note;

  /**
   *  A small structure for returning a list of notes out of a larger set.
   * 
   * <dl>
   *  <dt>startIndex</dt>
   *    <dd>
   *    The starting index within the overall set of notes.  This
   *    is also the number of notes that are "before" this list in the set.
   *    </dd>
   * 
   *  <dt>totalNotes</dt>
   *    <dd>
   *    The number of notes in the larger set.  This can be used
   *    to calculate how many notes are "after" this note in the set.
   *    (I.e.  remaining = totalNotes - (startIndex + notes.length)  )
   *    </dd>
   * 
   *  <dt>notes</dt>
   *    <dd>
   *    The list of notes from this range.  The Notes will include all
   *    metadata (attributes, resources, etc.), but will not include the ENML
   *    content of the note or the binary contents of any resources.
   *    </dd>
   * 
   *  <dt>stoppedWords</dt>
   *    <dd>
   *    If the NoteList was produced using a text based search
   *    query that included words that are not indexed or searched by the service,
   *    this will include a list of those ignored words.
   *    </dd>
   * 
   *  <dt>searchedWords</dt>
   *    <dd>
   *    If the NoteList was produced using a text based search
   *    query that included viable search words or quoted expressions, this will
   *    include a list of those words.  Any stopped words will not be included
   *    in this list.
   *    </dd>
   * 
   *  <dt>updateCount</dt>
   *    <dd>
   *    Indicates the total number of transactions that have
   *    been committed within the account.  This reflects (for example) the
   *    number of discrete additions or modifications that have been made to
   *    the data in this account (tags, notes, resources, etc.).
   *    This number is the "high water mark" for Update Sequence Numbers (USN)
   *    within the account.
   *    </dd>
   *  </dl>
   */
  public class NoteList implements TBase   {
    private static const STRUCT_DESC:TStruct = new TStruct("NoteList");
    private static const START_INDEX_FIELD_DESC:TField = new TField("startIndex", TType.I32, 1);
    private static const TOTAL_NOTES_FIELD_DESC:TField = new TField("totalNotes", TType.I32, 2);
    private static const NOTES_FIELD_DESC:TField = new TField("notes", TType.LIST, 3);
    private static const STOPPED_WORDS_FIELD_DESC:TField = new TField("stoppedWords", TType.LIST, 4);
    private static const SEARCHED_WORDS_FIELD_DESC:TField = new TField("searchedWords", TType.LIST, 5);
    private static const UPDATE_COUNT_FIELD_DESC:TField = new TField("updateCount", TType.I32, 6);

    private var _startIndex:int;
    public static const STARTINDEX:int = 1;
    private var _totalNotes:int;
    public static const TOTALNOTES:int = 2;
    private var _notes:Array;
    public static const NOTES:int = 3;
    private var _stoppedWords:Array;
    public static const STOPPEDWORDS:int = 4;
    private var _searchedWords:Array;
    public static const SEARCHEDWORDS:int = 5;
    private var _updateCount:int;
    public static const UPDATECOUNT:int = 6;

    private var __isset_startIndex:Boolean = false;
    private var __isset_totalNotes:Boolean = false;
    private var __isset_updateCount:Boolean = false;

    public static const metaDataMap:Dictionary = new Dictionary();
    {
      metaDataMap[STARTINDEX] = new FieldMetaData("startIndex", TFieldRequirementType.REQUIRED, 
          new FieldValueMetaData(TType.I32));
      metaDataMap[TOTALNOTES] = new FieldMetaData("totalNotes", TFieldRequirementType.REQUIRED, 
          new FieldValueMetaData(TType.I32));
      metaDataMap[NOTES] = new FieldMetaData("notes", TFieldRequirementType.REQUIRED, 
          new ListMetaData(TType.LIST, 
              new StructMetaData(TType.STRUCT, Note)));
      metaDataMap[STOPPEDWORDS] = new FieldMetaData("stoppedWords", TFieldRequirementType.OPTIONAL, 
          new ListMetaData(TType.LIST, 
              new FieldValueMetaData(TType.STRING)));
      metaDataMap[SEARCHEDWORDS] = new FieldMetaData("searchedWords", TFieldRequirementType.OPTIONAL, 
          new ListMetaData(TType.LIST, 
              new FieldValueMetaData(TType.STRING)));
      metaDataMap[UPDATECOUNT] = new FieldMetaData("updateCount", TFieldRequirementType.OPTIONAL, 
          new FieldValueMetaData(TType.I32));
    }
    {
      FieldMetaData.addStructMetaDataMap(NoteList, metaDataMap);
    }

    public function NoteList() {
    }

    public function get startIndex():int {
      return this._startIndex;
    }

    public function set startIndex(startIndex:int):void {
      this._startIndex = startIndex;
      this.__isset_startIndex = true;
    }

    public function unsetStartIndex():void {
      this.__isset_startIndex = false;
    }

    // Returns true if field startIndex is set (has been assigned a value) and false otherwise
    public function isSetStartIndex():Boolean {
      return this.__isset_startIndex;
    }

    public function get totalNotes():int {
      return this._totalNotes;
    }

    public function set totalNotes(totalNotes:int):void {
      this._totalNotes = totalNotes;
      this.__isset_totalNotes = true;
    }

    public function unsetTotalNotes():void {
      this.__isset_totalNotes = false;
    }

    // Returns true if field totalNotes is set (has been assigned a value) and false otherwise
    public function isSetTotalNotes():Boolean {
      return this.__isset_totalNotes;
    }

    public function get notes():Array {
      return this._notes;
    }

    public function set notes(notes:Array):void {
      this._notes = notes;
    }

    public function unsetNotes():void {
      this.notes = null;
    }

    // Returns true if field notes is set (has been assigned a value) and false otherwise
    public function isSetNotes():Boolean {
      return this.notes != null;
    }

    public function get stoppedWords():Array {
      return this._stoppedWords;
    }

    public function set stoppedWords(stoppedWords:Array):void {
      this._stoppedWords = stoppedWords;
    }

    public function unsetStoppedWords():void {
      this.stoppedWords = null;
    }

    // Returns true if field stoppedWords is set (has been assigned a value) and false otherwise
    public function isSetStoppedWords():Boolean {
      return this.stoppedWords != null;
    }

    public function get searchedWords():Array {
      return this._searchedWords;
    }

    public function set searchedWords(searchedWords:Array):void {
      this._searchedWords = searchedWords;
    }

    public function unsetSearchedWords():void {
      this.searchedWords = null;
    }

    // Returns true if field searchedWords is set (has been assigned a value) and false otherwise
    public function isSetSearchedWords():Boolean {
      return this.searchedWords != null;
    }

    public function get updateCount():int {
      return this._updateCount;
    }

    public function set updateCount(updateCount:int):void {
      this._updateCount = updateCount;
      this.__isset_updateCount = true;
    }

    public function unsetUpdateCount():void {
      this.__isset_updateCount = false;
    }

    // Returns true if field updateCount is set (has been assigned a value) and false otherwise
    public function isSetUpdateCount():Boolean {
      return this.__isset_updateCount;
    }

    public function setFieldValue(fieldID:int, value:*):void {
      switch (fieldID) {
      case STARTINDEX:
        if (value == null) {
          unsetStartIndex();
        } else {
          this.startIndex = value;
        }
        break;

      case TOTALNOTES:
        if (value == null) {
          unsetTotalNotes();
        } else {
          this.totalNotes = value;
        }
        break;

      case NOTES:
        if (value == null) {
          unsetNotes();
        } else {
          this.notes = value;
        }
        break;

      case STOPPEDWORDS:
        if (value == null) {
          unsetStoppedWords();
        } else {
          this.stoppedWords = value;
        }
        break;

      case SEARCHEDWORDS:
        if (value == null) {
          unsetSearchedWords();
        } else {
          this.searchedWords = value;
        }
        break;

      case UPDATECOUNT:
        if (value == null) {
          unsetUpdateCount();
        } else {
          this.updateCount = value;
        }
        break;

      default:
        throw new ArgumentError("Field " + fieldID + " doesn't exist!");
      }
    }

    public function getFieldValue(fieldID:int):* {
      switch (fieldID) {
      case STARTINDEX:
        return this.startIndex;
      case TOTALNOTES:
        return this.totalNotes;
      case NOTES:
        return this.notes;
      case STOPPEDWORDS:
        return this.stoppedWords;
      case SEARCHEDWORDS:
        return this.searchedWords;
      case UPDATECOUNT:
        return this.updateCount;
      default:
        throw new ArgumentError("Field " + fieldID + " doesn't exist!");
      }
    }

    // Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise
    public function isSet(fieldID:int):Boolean {
      switch (fieldID) {
      case STARTINDEX:
        return isSetStartIndex();
      case TOTALNOTES:
        return isSetTotalNotes();
      case NOTES:
        return isSetNotes();
      case STOPPEDWORDS:
        return isSetStoppedWords();
      case SEARCHEDWORDS:
        return isSetSearchedWords();
      case UPDATECOUNT:
        return isSetUpdateCount();
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
          case STARTINDEX:
            if (field.type == TType.I32) {
              this.startIndex = iprot.readI32();
              this.__isset_startIndex = true;
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case TOTALNOTES:
            if (field.type == TType.I32) {
              this.totalNotes = iprot.readI32();
              this.__isset_totalNotes = true;
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case NOTES:
            if (field.type == TType.LIST) {
              {
                var _list93:TList = iprot.readListBegin();
                this.notes = new Array();
                for (var _i94:int = 0; _i94 < _list93.size; ++_i94)
                {
                  var _elem95:Note;
                  _elem95 = new Note();
                  _elem95.read(iprot);
                  this.notes.push(_elem95);
                }
                iprot.readListEnd();
              }
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case STOPPEDWORDS:
            if (field.type == TType.LIST) {
              {
                var _list96:TList = iprot.readListBegin();
                this.stoppedWords = new Array();
                for (var _i97:int = 0; _i97 < _list96.size; ++_i97)
                {
                  var _elem98:String;
                  _elem98 = iprot.readString();
                  this.stoppedWords.push(_elem98);
                }
                iprot.readListEnd();
              }
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case SEARCHEDWORDS:
            if (field.type == TType.LIST) {
              {
                var _list99:TList = iprot.readListBegin();
                this.searchedWords = new Array();
                for (var _i100:int = 0; _i100 < _list99.size; ++_i100)
                {
                  var _elem101:String;
                  _elem101 = iprot.readString();
                  this.searchedWords.push(_elem101);
                }
                iprot.readListEnd();
              }
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case UPDATECOUNT:
            if (field.type == TType.I32) {
              this.updateCount = iprot.readI32();
              this.__isset_updateCount = true;
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
      if (!__isset_startIndex) {
        throw new TProtocolError(TProtocolError.UNKNOWN, "Required field 'startIndex' was not found in serialized data! Struct: " + toString());
      }
      if (!__isset_totalNotes) {
        throw new TProtocolError(TProtocolError.UNKNOWN, "Required field 'totalNotes' was not found in serialized data! Struct: " + toString());
      }
      validate();
    }

    public function write(oprot:TProtocol):void {
      validate();

      oprot.writeStructBegin(STRUCT_DESC);
      oprot.writeFieldBegin(START_INDEX_FIELD_DESC);
      oprot.writeI32(this.startIndex);
      oprot.writeFieldEnd();
      oprot.writeFieldBegin(TOTAL_NOTES_FIELD_DESC);
      oprot.writeI32(this.totalNotes);
      oprot.writeFieldEnd();
      if (this.notes != null) {
        oprot.writeFieldBegin(NOTES_FIELD_DESC);
        {
          oprot.writeListBegin(new TList(TType.STRUCT, this.notes.length));
          for each (var elem102:* in this.notes)          {
            elem102.write(oprot);
          }
          oprot.writeListEnd();
        }
        oprot.writeFieldEnd();
      }
      if (this.stoppedWords != null) {
        if (isSetStoppedWords()) {
          oprot.writeFieldBegin(STOPPED_WORDS_FIELD_DESC);
          {
            oprot.writeListBegin(new TList(TType.STRING, this.stoppedWords.length));
            for each (var elem103:* in this.stoppedWords)            {
              oprot.writeString(elem103);
            }
            oprot.writeListEnd();
          }
          oprot.writeFieldEnd();
        }
      }
      if (this.searchedWords != null) {
        if (isSetSearchedWords()) {
          oprot.writeFieldBegin(SEARCHED_WORDS_FIELD_DESC);
          {
            oprot.writeListBegin(new TList(TType.STRING, this.searchedWords.length));
            for each (var elem104:* in this.searchedWords)            {
              oprot.writeString(elem104);
            }
            oprot.writeListEnd();
          }
          oprot.writeFieldEnd();
        }
      }
      if (isSetUpdateCount()) {
        oprot.writeFieldBegin(UPDATE_COUNT_FIELD_DESC);
        oprot.writeI32(this.updateCount);
        oprot.writeFieldEnd();
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

    public function toString():String {
      var ret:String = new String("NoteList(");
      var first:Boolean = true;

      ret += "startIndex:";
      ret += this.startIndex;
      first = false;
      if (!first) ret +=  ", ";
      ret += "totalNotes:";
      ret += this.totalNotes;
      first = false;
      if (!first) ret +=  ", ";
      ret += "notes:";
      if (this.notes == null) {
        ret += "null";
      } else {
        ret += this.notes;
      }
      first = false;
      if (isSetStoppedWords()) {
        if (!first) ret +=  ", ";
        ret += "stoppedWords:";
        if (this.stoppedWords == null) {
          ret += "null";
        } else {
          ret += this.stoppedWords;
        }
        first = false;
      }
      if (isSetSearchedWords()) {
        if (!first) ret +=  ", ";
        ret += "searchedWords:";
        if (this.searchedWords == null) {
          ret += "null";
        } else {
          ret += this.searchedWords;
        }
        first = false;
      }
      if (isSetUpdateCount()) {
        if (!first) ret +=  ", ";
        ret += "updateCount:";
        ret += this.updateCount;
        first = false;
      }
      ret += ")";
      return ret;
    }

    public function validate():void {
      // check for required fields
      // alas, we cannot check 'startIndex' because it's a primitive and you chose the non-beans generator.
      // alas, we cannot check 'totalNotes' because it's a primitive and you chose the non-beans generator.
      if (notes == null) {
        throw new TProtocolError(TProtocolError.UNKNOWN, "Required field 'notes' was not present! Struct: " + toString());
      }
      // check that fields of type enum have valid values
    }

  }

}