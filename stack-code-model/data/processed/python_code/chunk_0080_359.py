package com.codeazur.as3swf.data.abc.bytecode
{
	import com.codeazur.as3swf.SWFData;
	import com.codeazur.as3swf.data.abc.ABCData;
	import com.codeazur.as3swf.data.abc.ABCSet;
	import com.codeazur.as3swf.data.abc.io.ABCScanner;
	import com.codeazur.utils.StringUtils;
	/**
	 * @author Simon Richardson - stickupkid@gmail.com
	 */
	public class ABCInstanceInfoSet extends ABCSet {
		
		public var instanceInfos:Vector.<ABCInstanceInfo>;
		
		public function ABCInstanceInfoSet(abcData:ABCData) {
			super(abcData);
			
			instanceInfos = new Vector.<ABCInstanceInfo>();
		}
		
		public function merge(instanceInfoSet:ABCInstanceInfoSet):void {
			instanceInfoSet.abcData = abcData;
			
			const total:uint = instanceInfoSet.instanceInfos.length;
			for(var i:uint=0; i<total; i++) {
				const info:ABCInstanceInfo = instanceInfoSet.instanceInfos[i];
				info.abcData = abcData;
				
				instanceInfos.push(info);
			}
		}
		
		public function read(data:SWFData, scanner:ABCScanner):void {
			const position:uint = scanner.getInstanceInfo();
			if(data.position != position) {
				throw new Error('Invalid position (Expected: ' + data.position + ', Recieved: ' + position + ')');
			}
			
			data.position = position;
			
			const total:uint = data.readEncodedU30();
			for(var i:uint=0; i<total; i++) {
				data.position = scanner.getInstanceInfoAtIndex(i);
				
				const mnameIndex:uint = data.readEncodedU30();
				const mname:IABCMultiname = getMultinameByIndex(mnameIndex);
				
				const superMNameIndex:uint = data.readEncodedU30();
				const superMName:IABCMultiname = getMultinameByIndex(superMNameIndex);
				
				const flags:uint = data.readUI8();
				
				const instanceInfo:ABCInstanceInfo = ABCInstanceInfo.create(abcData, mname, superMName, flags);
				const instanceTraitPositions:Vector.<uint> = scanner.getInstanceTraitInfoAtIndex(i);
				instanceInfo.read(data, scanner, instanceTraitPositions);
				
				instanceInfos.push(instanceInfo);
			}
		}
		
		public function write(bytes:SWFData):void {
			const total:uint = instanceInfos.length;
			bytes.writeEncodedU32(total);
			
			for(var i:uint=0; i<total; i++) {
				const instanceInfo:ABCInstanceInfo = instanceInfos[i];
				
				bytes.writeEncodedU32(getMultinameIndex(instanceInfo.multiname));
				bytes.writeEncodedU32(getMultinameIndex(instanceInfo.superMultiname));
				
				bytes.writeUI8(instanceInfo.flags);
				
				instanceInfo.write(bytes);
			}
		}
		
		public function getAt(index:uint):ABCInstanceInfo {
			return instanceInfos[index];
		}
		
		public function getByMultiname(multiname:IABCMultiname):ABCInstanceInfo {
			var result:ABCInstanceInfo;
			
			const total:uint = instanceInfos.length;
			for(var i:uint=0; i<total; i++) {
				const instanceInfo:ABCInstanceInfo = instanceInfos[i];
				if(instanceInfo.multiname.equals(multiname)) {
					result = instanceInfo;
					break;
				}
			}
			
			return result;
		}
		
		override public function get name() : String { return "ABCInstanceInfoSet"; }
		override public function get length():uint { return instanceInfos.length; }
		
		override public function toString(indent : uint = 0) : String {
			var str:String = super.toString(indent);
			
			str += "\n" + StringUtils.repeat(indent + 2) + "Number InstanceInfo: ";
			str += instanceInfos.length;
			
			if(instanceInfos.length > 0) {
				for(var i:uint=0; i<instanceInfos.length; i++) {
					str += "\n" + instanceInfos[i].toString(indent + 4);
				}
			}
			
			return str;
		}
	}
}