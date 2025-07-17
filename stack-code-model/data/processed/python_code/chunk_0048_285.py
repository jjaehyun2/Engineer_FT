package {
	import flash.filesystem.File;
	import flash.filesystem.FileStream;
	import flash.filesystem.FileMode;
	import flash.system.System;
	import fl.motion.ITween;

	public class WordXMLParser {
		var requiredChildren: Vector.<XML> ;

		public var _docml: XML
		public function WordXMLParser() {

		}
		public function ParseWordXML(doc: * ,callback:Function=null):void {

			var docStr: String = "";
			if (doc is File) {
				docStr = fileToString(doc);
			} else if (doc is String) {
				docStr = doc;
			} else {
				throw new Error("not a valid docml");
			}
			docml = trimStringToXML(docStr);
			docStr = null;
			requiredChildren = new Vector.<XML>();
			extractRequiredItem();
			var itemCounter: int = 0;
			var TotalString: String = "";
			while (itemCounter < requiredChildren.length) {
				if (requiredChildren[itemCounter].name() == "p") {
					var ptext: String = parseP(requiredChildren[itemCounter]);
					if (ptext != null) {
						if (TotalString != "") {
							TotalString += "\r\n";
						}
						TotalString += ptext;
					}

				} else if (requiredChildren[itemCounter].name() == "tbl") {
					var tblString: Array = new Array()
					parseTable(requiredChildren[itemCounter], tblString)
					TotalString += tblString.join("");
					tblString = null;
				}
				itemCounter++;
			}
			 itemCounter = 0;
			while (itemCounter < requiredChildren.length) {
				System.disposeXML(requiredChildren[itemCounter]);
				requiredChildren[itemCounter] = null;
				itemCounter++
			}
			requiredChildren = null;
			if(callback != null){
				callback(TotalString);
			}
		}
		public function extractRequiredItem() {

			var requiredItemLength: int = docml.body.children().length();
			var itemCounter: int = 0;
			while (itemCounter < requiredItemLength) {
				if (docml.body.children()[itemCounter].name() == "tbl" || docml.body.children()[itemCounter].name() == "p") {
					requiredChildren.push(docml.body.children()[itemCounter])
				}
				itemCounter++
			}
		}
		public function get docml(): XML {
			return _docml;
		}
		public function set docml(_xml: XML): void {
			_docml = _xml;
		}
		public function parseTable(tbl: XML, container: Array): void {

			var lngthss: int = tbl.tr.length();
			var trcontainer = null;
			for (var s: int = 0; s < lngthss; s++) {

				var nlnth: int = tbl.tr[s].tc.length();
				trcontainer = null
				trcontainer = new Array();

				for (var g: int = 0; g < nlnth; g++) {
					var tblLngth: int = tbl.tr[s].tc[g].tbl.length();
					var tblCounter: int = 0;
					while (tblLngth > 0 && tblCounter < tblLngth) {
						parseTable(tbl.tr[s].tc[g].tbl[tblCounter], container);
						tblCounter++;
					}

					if (tbl.tr[s].tc[g].p.length() > 0) {
						var rlenght: int = tbl.tr[s].tc[g].p.length();
						var pcounter: int = 0;
						while (pcounter < rlenght) {

							var ptext: String = parseP(tbl.tr[s].tc[g].p[pcounter])
							
							if (ptext != null) {
								trcontainer.push(ptext)
							}
							pcounter++;
						}
					}
				}
				var txt: String = trimText(trcontainer.join("\t\t"));
				if(txt != null){
					var lastIndex:int = txt.lastIndexOf("\r\n");
					if(lastIndex+2 != txt.length){
					txt = txt +"\r\n";
					}
				}
					container.push(txt);
				txt = null;
			}
		}
		public function trimText(xmls: * ): String {
			if (xmls == null) {
				return null;
			}
			var MainString: String = "";
			var sstr: String = xmls
			MainString = sstr;
			if (MainString == "" ) {
				return null;
			}
			return MainString;
		}
		public function parseP(p: XML) {
			var rtxt: String = "";
			
			if (p.r.length() > 0) {
				var rlenght: int = p.r.length();

				var tcounter: int = 0;
				if(p.pPr.jc.length() > 0){
					rtxt += "\r\n"
				}
				while (tcounter < rlenght) {
					//var tt:String = parseRow(p.r[tcounter]);
					//trace(tcounter,tt)
					rtxt += parseRow(p.r[tcounter])
					tcounter++;
				}

			}
			return trimText(rtxt);
		}
		public function parseRow(row: XML): String {
			var tcounter: int = 0;
			var ttxt: String = "";
			if (row.children().length() > 0) {
				var tlenght: int = row.children().length();

				while (tcounter < tlenght) {
					if (row.children()[tcounter].name() == "t") {
						ttxt += row.children()[tcounter].text();
					} else if (row.children()[tcounter].name() == "br" ) {
						ttxt += "\r\n"
					} else if (row.children()[tcounter].name() == "tab") {
						ttxt += "\t\t"
					}

					tcounter++;
				}
			}
			return ttxt;
		}
		public static function fileToString(FILES: File, FILESTREAMS: FileStream = null): String {
			var isStreamCreated: Boolean = false;
			if (FILESTREAMS == null) {
				isStreamCreated = true;
				FILESTREAMS = new FileStream();
			}
			FILESTREAMS.open(FILES, FileMode.READ);
			var fileContents: String = FILESTREAMS.readUTFBytes(FILESTREAMS.bytesAvailable);
			FILESTREAMS.close();
			if (isStreamCreated) {
				FILESTREAMS = null;
			}
			return fileContents;
		}
		public function trimStringToXML(string: String): XML {
			string = string.split("w:").join("");
			string = string.split("wsp:").join("");
			string = string.split("sz-cs").join("szcs");
			
			try {
				return new XML(string);
			} catch (e: Error) {
				throw new Error("not a valid docml")
			}
			return null;
		}
	}

}