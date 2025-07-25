/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 */
package com.evernote.edam.type {

import org.apache.thrift.Set;
import org.apache.thrift.type.BigInteger;
import flash.utils.ByteArray;
import flash.utils.Dictionary;

import org.apache.thrift.*;
import org.apache.thrift.meta_data.*;
import org.apache.thrift.protocol.*;

import com.evernote.edam.type.SponsoredGroupRole;

  /**
   *  This structure is used to provide information about a user's Premium account.
   * <dl>
   *  <dt>currentTime</dt>
   *    <dd>
   *    The server-side date and time when this data was generated.
   *    </dd>
   *  <dt>premium</dt>
   *    <dd>
   *    True if the user's account is Premium.
   *    </dd>
   *  <dt>premiumRecurring</dt>
   *    <dd>
   *    True if the user's account is Premium and has a recurring payment method.
   *    </dd>
   *  <dt>premiumExpirationDate</dt>
   *    <dd>
   *    The date when the user's Premium account expires, or the date when the
   *    user's account will be charged if it has a recurring payment method.
   *    </dd>
   *  <dt>premiumExtendable</dt>
   *    <dd>
   *    True if the user is eligible for purchasing Premium account extensions.
   *    </dd>
   *  <dt>premiumPending</dt>
   *    <dd>
   *    True if the user's Premium account is pending payment confirmation
   *    </dd>
   *  <dt>premiumCancellationPending</dt>
   *    <dd>
   *    True if the user has requested that no further charges to be made; the
   *    Premium account will remain active until it expires.
   *    </dd>
   *  <dt>canPurchaseUploadAllowance</dt>
   *    <dd>
   *    True if the user is eligible for purchasing additional upload allowance.
   *    </dd>
   *  <dt>sponsoredGroupName</dt>
   *    <dd>
   *    The name of the sponsored group that the user is part of.
   *    </dd>
   *  <dt>sponsoredGroupRole</dt>
   *    <dd>
   *    DEPRECATED - will be removed in a future update.
   *    </dd>
   *  </dl>
   */
  public class PremiumInfo implements TBase   {
    private static const STRUCT_DESC:TStruct = new TStruct("PremiumInfo");
    private static const CURRENT_TIME_FIELD_DESC:TField = new TField("currentTime", TType.I64, 1);
    private static const PREMIUM_FIELD_DESC:TField = new TField("premium", TType.BOOL, 2);
    private static const PREMIUM_RECURRING_FIELD_DESC:TField = new TField("premiumRecurring", TType.BOOL, 3);
    private static const PREMIUM_EXPIRATION_DATE_FIELD_DESC:TField = new TField("premiumExpirationDate", TType.I64, 4);
    private static const PREMIUM_EXTENDABLE_FIELD_DESC:TField = new TField("premiumExtendable", TType.BOOL, 5);
    private static const PREMIUM_PENDING_FIELD_DESC:TField = new TField("premiumPending", TType.BOOL, 6);
    private static const PREMIUM_CANCELLATION_PENDING_FIELD_DESC:TField = new TField("premiumCancellationPending", TType.BOOL, 7);
    private static const CAN_PURCHASE_UPLOAD_ALLOWANCE_FIELD_DESC:TField = new TField("canPurchaseUploadAllowance", TType.BOOL, 8);
    private static const SPONSORED_GROUP_NAME_FIELD_DESC:TField = new TField("sponsoredGroupName", TType.STRING, 9);
    private static const SPONSORED_GROUP_ROLE_FIELD_DESC:TField = new TField("sponsoredGroupRole", TType.I32, 10);

    private var _currentTime:BigInteger;
    public static const CURRENTTIME:int = 1;
    private var _premium:Boolean;
    public static const PREMIUM:int = 2;
    private var _premiumRecurring:Boolean;
    public static const PREMIUMRECURRING:int = 3;
    private var _premiumExpirationDate:BigInteger;
    public static const PREMIUMEXPIRATIONDATE:int = 4;
    private var _premiumExtendable:Boolean;
    public static const PREMIUMEXTENDABLE:int = 5;
    private var _premiumPending:Boolean;
    public static const PREMIUMPENDING:int = 6;
    private var _premiumCancellationPending:Boolean;
    public static const PREMIUMCANCELLATIONPENDING:int = 7;
    private var _canPurchaseUploadAllowance:Boolean;
    public static const CANPURCHASEUPLOADALLOWANCE:int = 8;
    private var _sponsoredGroupName:String;
    public static const SPONSOREDGROUPNAME:int = 9;
    private var _sponsoredGroupRole:int;
    public static const SPONSOREDGROUPROLE:int = 10;

    private var __isset_currentTime:Boolean = false;
    private var __isset_premium:Boolean = false;
    private var __isset_premiumRecurring:Boolean = false;
    private var __isset_premiumExpirationDate:Boolean = false;
    private var __isset_premiumExtendable:Boolean = false;
    private var __isset_premiumPending:Boolean = false;
    private var __isset_premiumCancellationPending:Boolean = false;
    private var __isset_canPurchaseUploadAllowance:Boolean = false;
    private var __isset_sponsoredGroupRole:Boolean = false;

    public static const metaDataMap:Dictionary = new Dictionary();
    {
      metaDataMap[CURRENTTIME] = new FieldMetaData("currentTime", TFieldRequirementType.REQUIRED, 
          new FieldValueMetaData(TType.I64));
      metaDataMap[PREMIUM] = new FieldMetaData("premium", TFieldRequirementType.REQUIRED, 
          new FieldValueMetaData(TType.BOOL));
      metaDataMap[PREMIUMRECURRING] = new FieldMetaData("premiumRecurring", TFieldRequirementType.REQUIRED, 
          new FieldValueMetaData(TType.BOOL));
      metaDataMap[PREMIUMEXPIRATIONDATE] = new FieldMetaData("premiumExpirationDate", TFieldRequirementType.OPTIONAL, 
          new FieldValueMetaData(TType.I64));
      metaDataMap[PREMIUMEXTENDABLE] = new FieldMetaData("premiumExtendable", TFieldRequirementType.REQUIRED, 
          new FieldValueMetaData(TType.BOOL));
      metaDataMap[PREMIUMPENDING] = new FieldMetaData("premiumPending", TFieldRequirementType.REQUIRED, 
          new FieldValueMetaData(TType.BOOL));
      metaDataMap[PREMIUMCANCELLATIONPENDING] = new FieldMetaData("premiumCancellationPending", TFieldRequirementType.REQUIRED, 
          new FieldValueMetaData(TType.BOOL));
      metaDataMap[CANPURCHASEUPLOADALLOWANCE] = new FieldMetaData("canPurchaseUploadAllowance", TFieldRequirementType.REQUIRED, 
          new FieldValueMetaData(TType.BOOL));
      metaDataMap[SPONSOREDGROUPNAME] = new FieldMetaData("sponsoredGroupName", TFieldRequirementType.OPTIONAL, 
          new FieldValueMetaData(TType.STRING));
      metaDataMap[SPONSOREDGROUPROLE] = new FieldMetaData("sponsoredGroupRole", TFieldRequirementType.OPTIONAL, 
          new FieldValueMetaData(TType.I32));
    }
    {
      FieldMetaData.addStructMetaDataMap(PremiumInfo, metaDataMap);
    }

    public function PremiumInfo() {
    }

    public function get currentTime():BigInteger {
      return this._currentTime;
    }

    public function set currentTime(currentTime:BigInteger):void {
      this._currentTime = currentTime;
      this.__isset_currentTime = true;
    }

    public function unsetCurrentTime():void {
      this.__isset_currentTime = false;
    }

    // Returns true if field currentTime is set (has been assigned a value) and false otherwise
    public function isSetCurrentTime():Boolean {
      return this.__isset_currentTime;
    }

    public function get premium():Boolean {
      return this._premium;
    }

    public function set premium(premium:Boolean):void {
      this._premium = premium;
      this.__isset_premium = true;
    }

    public function unsetPremium():void {
      this.__isset_premium = false;
    }

    // Returns true if field premium is set (has been assigned a value) and false otherwise
    public function isSetPremium():Boolean {
      return this.__isset_premium;
    }

    public function get premiumRecurring():Boolean {
      return this._premiumRecurring;
    }

    public function set premiumRecurring(premiumRecurring:Boolean):void {
      this._premiumRecurring = premiumRecurring;
      this.__isset_premiumRecurring = true;
    }

    public function unsetPremiumRecurring():void {
      this.__isset_premiumRecurring = false;
    }

    // Returns true if field premiumRecurring is set (has been assigned a value) and false otherwise
    public function isSetPremiumRecurring():Boolean {
      return this.__isset_premiumRecurring;
    }

    public function get premiumExpirationDate():BigInteger {
      return this._premiumExpirationDate;
    }

    public function set premiumExpirationDate(premiumExpirationDate:BigInteger):void {
      this._premiumExpirationDate = premiumExpirationDate;
      this.__isset_premiumExpirationDate = true;
    }

    public function unsetPremiumExpirationDate():void {
      this.__isset_premiumExpirationDate = false;
    }

    // Returns true if field premiumExpirationDate is set (has been assigned a value) and false otherwise
    public function isSetPremiumExpirationDate():Boolean {
      return this.__isset_premiumExpirationDate;
    }

    public function get premiumExtendable():Boolean {
      return this._premiumExtendable;
    }

    public function set premiumExtendable(premiumExtendable:Boolean):void {
      this._premiumExtendable = premiumExtendable;
      this.__isset_premiumExtendable = true;
    }

    public function unsetPremiumExtendable():void {
      this.__isset_premiumExtendable = false;
    }

    // Returns true if field premiumExtendable is set (has been assigned a value) and false otherwise
    public function isSetPremiumExtendable():Boolean {
      return this.__isset_premiumExtendable;
    }

    public function get premiumPending():Boolean {
      return this._premiumPending;
    }

    public function set premiumPending(premiumPending:Boolean):void {
      this._premiumPending = premiumPending;
      this.__isset_premiumPending = true;
    }

    public function unsetPremiumPending():void {
      this.__isset_premiumPending = false;
    }

    // Returns true if field premiumPending is set (has been assigned a value) and false otherwise
    public function isSetPremiumPending():Boolean {
      return this.__isset_premiumPending;
    }

    public function get premiumCancellationPending():Boolean {
      return this._premiumCancellationPending;
    }

    public function set premiumCancellationPending(premiumCancellationPending:Boolean):void {
      this._premiumCancellationPending = premiumCancellationPending;
      this.__isset_premiumCancellationPending = true;
    }

    public function unsetPremiumCancellationPending():void {
      this.__isset_premiumCancellationPending = false;
    }

    // Returns true if field premiumCancellationPending is set (has been assigned a value) and false otherwise
    public function isSetPremiumCancellationPending():Boolean {
      return this.__isset_premiumCancellationPending;
    }

    public function get canPurchaseUploadAllowance():Boolean {
      return this._canPurchaseUploadAllowance;
    }

    public function set canPurchaseUploadAllowance(canPurchaseUploadAllowance:Boolean):void {
      this._canPurchaseUploadAllowance = canPurchaseUploadAllowance;
      this.__isset_canPurchaseUploadAllowance = true;
    }

    public function unsetCanPurchaseUploadAllowance():void {
      this.__isset_canPurchaseUploadAllowance = false;
    }

    // Returns true if field canPurchaseUploadAllowance is set (has been assigned a value) and false otherwise
    public function isSetCanPurchaseUploadAllowance():Boolean {
      return this.__isset_canPurchaseUploadAllowance;
    }

    public function get sponsoredGroupName():String {
      return this._sponsoredGroupName;
    }

    public function set sponsoredGroupName(sponsoredGroupName:String):void {
      this._sponsoredGroupName = sponsoredGroupName;
    }

    public function unsetSponsoredGroupName():void {
      this.sponsoredGroupName = null;
    }

    // Returns true if field sponsoredGroupName is set (has been assigned a value) and false otherwise
    public function isSetSponsoredGroupName():Boolean {
      return this.sponsoredGroupName != null;
    }

    public function get sponsoredGroupRole():int {
      return this._sponsoredGroupRole;
    }

    public function set sponsoredGroupRole(sponsoredGroupRole:int):void {
      this._sponsoredGroupRole = sponsoredGroupRole;
      this.__isset_sponsoredGroupRole = true;
    }

    public function unsetSponsoredGroupRole():void {
      this.__isset_sponsoredGroupRole = false;
    }

    // Returns true if field sponsoredGroupRole is set (has been assigned a value) and false otherwise
    public function isSetSponsoredGroupRole():Boolean {
      return this.__isset_sponsoredGroupRole;
    }

    public function setFieldValue(fieldID:int, value:*):void {
      switch (fieldID) {
      case CURRENTTIME:
        if (value == null) {
          unsetCurrentTime();
        } else {
          this.currentTime = value;
        }
        break;

      case PREMIUM:
        if (value == null) {
          unsetPremium();
        } else {
          this.premium = value;
        }
        break;

      case PREMIUMRECURRING:
        if (value == null) {
          unsetPremiumRecurring();
        } else {
          this.premiumRecurring = value;
        }
        break;

      case PREMIUMEXPIRATIONDATE:
        if (value == null) {
          unsetPremiumExpirationDate();
        } else {
          this.premiumExpirationDate = value;
        }
        break;

      case PREMIUMEXTENDABLE:
        if (value == null) {
          unsetPremiumExtendable();
        } else {
          this.premiumExtendable = value;
        }
        break;

      case PREMIUMPENDING:
        if (value == null) {
          unsetPremiumPending();
        } else {
          this.premiumPending = value;
        }
        break;

      case PREMIUMCANCELLATIONPENDING:
        if (value == null) {
          unsetPremiumCancellationPending();
        } else {
          this.premiumCancellationPending = value;
        }
        break;

      case CANPURCHASEUPLOADALLOWANCE:
        if (value == null) {
          unsetCanPurchaseUploadAllowance();
        } else {
          this.canPurchaseUploadAllowance = value;
        }
        break;

      case SPONSOREDGROUPNAME:
        if (value == null) {
          unsetSponsoredGroupName();
        } else {
          this.sponsoredGroupName = value;
        }
        break;

      case SPONSOREDGROUPROLE:
        if (value == null) {
          unsetSponsoredGroupRole();
        } else {
          this.sponsoredGroupRole = value;
        }
        break;

      default:
        throw new ArgumentError("Field " + fieldID + " doesn't exist!");
      }
    }

    public function getFieldValue(fieldID:int):* {
      switch (fieldID) {
      case CURRENTTIME:
        return this.currentTime;
      case PREMIUM:
        return this.premium;
      case PREMIUMRECURRING:
        return this.premiumRecurring;
      case PREMIUMEXPIRATIONDATE:
        return this.premiumExpirationDate;
      case PREMIUMEXTENDABLE:
        return this.premiumExtendable;
      case PREMIUMPENDING:
        return this.premiumPending;
      case PREMIUMCANCELLATIONPENDING:
        return this.premiumCancellationPending;
      case CANPURCHASEUPLOADALLOWANCE:
        return this.canPurchaseUploadAllowance;
      case SPONSOREDGROUPNAME:
        return this.sponsoredGroupName;
      case SPONSOREDGROUPROLE:
        return this.sponsoredGroupRole;
      default:
        throw new ArgumentError("Field " + fieldID + " doesn't exist!");
      }
    }

    // Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise
    public function isSet(fieldID:int):Boolean {
      switch (fieldID) {
      case CURRENTTIME:
        return isSetCurrentTime();
      case PREMIUM:
        return isSetPremium();
      case PREMIUMRECURRING:
        return isSetPremiumRecurring();
      case PREMIUMEXPIRATIONDATE:
        return isSetPremiumExpirationDate();
      case PREMIUMEXTENDABLE:
        return isSetPremiumExtendable();
      case PREMIUMPENDING:
        return isSetPremiumPending();
      case PREMIUMCANCELLATIONPENDING:
        return isSetPremiumCancellationPending();
      case CANPURCHASEUPLOADALLOWANCE:
        return isSetCanPurchaseUploadAllowance();
      case SPONSOREDGROUPNAME:
        return isSetSponsoredGroupName();
      case SPONSOREDGROUPROLE:
        return isSetSponsoredGroupRole();
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
          case CURRENTTIME:
            if (field.type == TType.I64) {
              this.currentTime = iprot.readI64();
              this.__isset_currentTime = true;
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case PREMIUM:
            if (field.type == TType.BOOL) {
              this.premium = iprot.readBool();
              this.__isset_premium = true;
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case PREMIUMRECURRING:
            if (field.type == TType.BOOL) {
              this.premiumRecurring = iprot.readBool();
              this.__isset_premiumRecurring = true;
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case PREMIUMEXPIRATIONDATE:
            if (field.type == TType.I64) {
              this.premiumExpirationDate = iprot.readI64();
              this.__isset_premiumExpirationDate = true;
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case PREMIUMEXTENDABLE:
            if (field.type == TType.BOOL) {
              this.premiumExtendable = iprot.readBool();
              this.__isset_premiumExtendable = true;
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case PREMIUMPENDING:
            if (field.type == TType.BOOL) {
              this.premiumPending = iprot.readBool();
              this.__isset_premiumPending = true;
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case PREMIUMCANCELLATIONPENDING:
            if (field.type == TType.BOOL) {
              this.premiumCancellationPending = iprot.readBool();
              this.__isset_premiumCancellationPending = true;
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case CANPURCHASEUPLOADALLOWANCE:
            if (field.type == TType.BOOL) {
              this.canPurchaseUploadAllowance = iprot.readBool();
              this.__isset_canPurchaseUploadAllowance = true;
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case SPONSOREDGROUPNAME:
            if (field.type == TType.STRING) {
              this.sponsoredGroupName = iprot.readString();
            } else { 
              TProtocolUtil.skip(iprot, field.type);
            }
            break;
          case SPONSOREDGROUPROLE:
            if (field.type == TType.I32) {
              this.sponsoredGroupRole = iprot.readI32();
              this.__isset_sponsoredGroupRole = true;
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
      if (!__isset_currentTime) {
        throw new TProtocolError(TProtocolError.UNKNOWN, "Required field 'currentTime' was not found in serialized data! Struct: " + toString());
      }
      if (!__isset_premium) {
        throw new TProtocolError(TProtocolError.UNKNOWN, "Required field 'premium' was not found in serialized data! Struct: " + toString());
      }
      if (!__isset_premiumRecurring) {
        throw new TProtocolError(TProtocolError.UNKNOWN, "Required field 'premiumRecurring' was not found in serialized data! Struct: " + toString());
      }
      if (!__isset_premiumExtendable) {
        throw new TProtocolError(TProtocolError.UNKNOWN, "Required field 'premiumExtendable' was not found in serialized data! Struct: " + toString());
      }
      if (!__isset_premiumPending) {
        throw new TProtocolError(TProtocolError.UNKNOWN, "Required field 'premiumPending' was not found in serialized data! Struct: " + toString());
      }
      if (!__isset_premiumCancellationPending) {
        throw new TProtocolError(TProtocolError.UNKNOWN, "Required field 'premiumCancellationPending' was not found in serialized data! Struct: " + toString());
      }
      if (!__isset_canPurchaseUploadAllowance) {
        throw new TProtocolError(TProtocolError.UNKNOWN, "Required field 'canPurchaseUploadAllowance' was not found in serialized data! Struct: " + toString());
      }
      validate();
    }

    public function write(oprot:TProtocol):void {
      validate();

      oprot.writeStructBegin(STRUCT_DESC);
      oprot.writeFieldBegin(CURRENT_TIME_FIELD_DESC);
      oprot.writeI64(this.currentTime);
      oprot.writeFieldEnd();
      oprot.writeFieldBegin(PREMIUM_FIELD_DESC);
      oprot.writeBool(this.premium);
      oprot.writeFieldEnd();
      oprot.writeFieldBegin(PREMIUM_RECURRING_FIELD_DESC);
      oprot.writeBool(this.premiumRecurring);
      oprot.writeFieldEnd();
      if (isSetPremiumExpirationDate()) {
        oprot.writeFieldBegin(PREMIUM_EXPIRATION_DATE_FIELD_DESC);
        oprot.writeI64(this.premiumExpirationDate);
        oprot.writeFieldEnd();
      }
      oprot.writeFieldBegin(PREMIUM_EXTENDABLE_FIELD_DESC);
      oprot.writeBool(this.premiumExtendable);
      oprot.writeFieldEnd();
      oprot.writeFieldBegin(PREMIUM_PENDING_FIELD_DESC);
      oprot.writeBool(this.premiumPending);
      oprot.writeFieldEnd();
      oprot.writeFieldBegin(PREMIUM_CANCELLATION_PENDING_FIELD_DESC);
      oprot.writeBool(this.premiumCancellationPending);
      oprot.writeFieldEnd();
      oprot.writeFieldBegin(CAN_PURCHASE_UPLOAD_ALLOWANCE_FIELD_DESC);
      oprot.writeBool(this.canPurchaseUploadAllowance);
      oprot.writeFieldEnd();
      if (this.sponsoredGroupName != null) {
        if (isSetSponsoredGroupName()) {
          oprot.writeFieldBegin(SPONSORED_GROUP_NAME_FIELD_DESC);
          oprot.writeString(this.sponsoredGroupName);
          oprot.writeFieldEnd();
        }
      }
      if (isSetSponsoredGroupRole()) {
        oprot.writeFieldBegin(SPONSORED_GROUP_ROLE_FIELD_DESC);
        oprot.writeI32(this.sponsoredGroupRole);
        oprot.writeFieldEnd();
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

    public function toString():String {
      var ret:String = new String("PremiumInfo(");
      var first:Boolean = true;

      ret += "currentTime:";
      ret += this.currentTime;
      first = false;
      if (!first) ret +=  ", ";
      ret += "premium:";
      ret += this.premium;
      first = false;
      if (!first) ret +=  ", ";
      ret += "premiumRecurring:";
      ret += this.premiumRecurring;
      first = false;
      if (isSetPremiumExpirationDate()) {
        if (!first) ret +=  ", ";
        ret += "premiumExpirationDate:";
        ret += this.premiumExpirationDate;
        first = false;
      }
      if (!first) ret +=  ", ";
      ret += "premiumExtendable:";
      ret += this.premiumExtendable;
      first = false;
      if (!first) ret +=  ", ";
      ret += "premiumPending:";
      ret += this.premiumPending;
      first = false;
      if (!first) ret +=  ", ";
      ret += "premiumCancellationPending:";
      ret += this.premiumCancellationPending;
      first = false;
      if (!first) ret +=  ", ";
      ret += "canPurchaseUploadAllowance:";
      ret += this.canPurchaseUploadAllowance;
      first = false;
      if (isSetSponsoredGroupName()) {
        if (!first) ret +=  ", ";
        ret += "sponsoredGroupName:";
        if (this.sponsoredGroupName == null) {
          ret += "null";
        } else {
          ret += this.sponsoredGroupName;
        }
        first = false;
      }
      if (isSetSponsoredGroupRole()) {
        if (!first) ret +=  ", ";
        ret += "sponsoredGroupRole:";
        var sponsoredGroupRole_name:String = SponsoredGroupRole.VALUES_TO_NAMES[this.sponsoredGroupRole];
        if (sponsoredGroupRole_name != null) {
          ret += sponsoredGroupRole_name;
          ret += " (";
        }
        ret += this.sponsoredGroupRole;
        if (sponsoredGroupRole_name != null) {
          ret += ")";
        }
        first = false;
      }
      ret += ")";
      return ret;
    }

    public function validate():void {
      // check for required fields
      // alas, we cannot check 'currentTime' because it's a primitive and you chose the non-beans generator.
      // alas, we cannot check 'premium' because it's a primitive and you chose the non-beans generator.
      // alas, we cannot check 'premiumRecurring' because it's a primitive and you chose the non-beans generator.
      // alas, we cannot check 'premiumExtendable' because it's a primitive and you chose the non-beans generator.
      // alas, we cannot check 'premiumPending' because it's a primitive and you chose the non-beans generator.
      // alas, we cannot check 'premiumCancellationPending' because it's a primitive and you chose the non-beans generator.
      // alas, we cannot check 'canPurchaseUploadAllowance' because it's a primitive and you chose the non-beans generator.
      // check that fields of type enum have valid values
      if (isSetSponsoredGroupRole() && !SponsoredGroupRole.VALID_VALUES.contains(sponsoredGroupRole)){
        throw new TProtocolError(TProtocolError.UNKNOWN, "The field 'sponsoredGroupRole' has been assigned the invalid value " + sponsoredGroupRole);
      }
    }

  }

}