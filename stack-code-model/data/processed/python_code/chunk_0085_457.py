/*
* Tencent is pleased to support the open source community by making Fanvas available.
* Copyright (C) 2015 THL A29 Limited, a Tencent company. All rights reserved.
*
* Licensed under the MIT License (the "License"); you may not use this file except in compliance with the 
* License. You may obtain a copy of the License at
* http://opensource.org/licenses/MIT
*
* Unless required by applicable law or agreed to in writing, software distributed under the License is 
* distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or 
* implied. See the License for the specific language governing permissions and limitations under the 
* License.
*/
package model {
	
	import flash.geom.ColorTransform;
	import flash.geom.Matrix;
	
	public class InstanceData {
		
		public var isPlaceElement : Boolean;//是添加新元件帧，区别于移动元件
		public var startFrame : int;//实例的起始帧
		public var definitionID : int;//库ID
		public var defIndex : int;//库Index，简化JS库中定义的搜索方式
		public var type : String;//Shape MovieClip 
		public var InstanceID : String;
		public var depth : int;
		public var x : Number;
		public var y : Number;
		public var matrix : Matrix;
		public var skewX : Number;
		public var skewY : Number;
		public var alpha : Number;
		public var scaleX : Number;
		public var scaleY : Number;
		public var maskDepth : int;
		public var clipDepth : int;
		public var filters : Array;
		public var cacheAsBitmap : Boolean;
		public var colorTransform : ColorTransform;
		
		public function InstanceData() {
		}
	}
}