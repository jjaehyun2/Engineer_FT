package com.unhurdle
{
	import flash.filesystem.File;

	public class PropertyWriter
	{
		public function PropertyWriter()
		{
		}
		static public function writeToBuffer(property:OMVProperty,buffer:Array):void{
			//TODO: need to add comments
			buffer.push("		");
			if(property.static){
				buffer.push("static ");
			}
			if(property.readOnly){
				buffer.push("public const ");
			} else {
				buffer.push("public var ");
			}
			buffer.push(property.name);
			buffer.push(":");
			buffer.push(property.type);
			if(property.readOnly){
				var val:String = property.value;
				buffer.push("=");
				if(property.type == "String"){
					buffer.push('"');
				} else if(!val){
					if(property.type == "Number" || property.type == "int"){
						val = "0";
					} else if(property.type == "Boolean"){
						val = "false";
					} else {
						val = "null";
					}
				}
				buffer.push(val);
				if(property.type == "String"){
					buffer.push('"');
				}
			}
			buffer.push(";");
			buffer.push(File.lineEnding);
			
		}
	}
}