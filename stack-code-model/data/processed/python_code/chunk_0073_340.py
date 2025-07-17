package com {
	import flash.xml.XMLDocument;
	import flash.xml.XMLNode;
	
	import mx.collections.ArrayCollection;
	import mx.rpc.xml.SimpleXMLDecoder;
	import mx.rpc.xml.SimpleXMLEncoder;
	import mx.utils.ArrayUtil;

	public class XMLUtils {
		public function XMLUtils() {
		}

		public static function convertXmlToObject(file:String):Object {
			var xml:XMLDocument = new XMLDocument(file);
		
			var decoder:SimpleXMLDecoder = new SimpleXMLDecoder();
			var data:Object = decoder.decodeXML(xml);
			return data;
		}
		
		public static function objectToXML(name:String, obj:Object):XML {
			var qName:QName = new QName(((name is String) ? name : 'root'));
			var xmlDocument:XMLDocument = new XMLDocument();
			var simpleXMLEncoder:SimpleXMLEncoder = new SimpleXMLEncoder(xmlDocument);
			var xmlNode:XMLNode = simpleXMLEncoder.encodeValue(obj, qName, xmlDocument);
			var xml:XML = new XML(xmlDocument.toString());
			return xml;
		}
		
		public static function objectToXMLAsString(name:String, obj:Object):String {
			return objectToXML(name,obj).toString();
		}
		
		public static function convertXmlToArrayCollection(file:String):ArrayCollection {
			var data:Object = convertXmlToObject(file);
			var array:Array = [];
			try {
				array = ArrayUtil.toArray(data.rows.row);
			} catch (e:Error) {
				try {
					array = ArrayUtil.toArray(data);
				} catch (e:Error) {
				}
			}
		
			return new ArrayCollection(array);
		}
	}
}