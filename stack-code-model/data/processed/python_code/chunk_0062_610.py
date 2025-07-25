////////////////////////////////////////////////////////////////////////////////
//
//  Licensed to the Apache Software Foundation (ASF) under one or more
//  contributor license agreements.  See the NOTICE file distributed with
//  this work for additional information regarding copyright ownership.
//  The ASF licenses this file to You under the Apache License, Version 2.0
//  (the "License"); you may not use this file except in compliance with
//  the License.  You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
//
////////////////////////////////////////////////////////////////////////////////
package flashx.textLayout.events
{
	
	/** ModelChange values.  These are various types of model change. @private */
	public final class ModelChange
	{
		public static const ELEMENT_ADDED:String    = "elementAdded";
		public static const ELEMENT_REMOVAL:String  = "elementRemoval";
		public static const ELEMENT_MODIFIED:String = "elementModified";		
		
		public static const TEXTLAYOUT_FORMAT_CHANGED:String = "formatChanged";
		
		public static const TEXT_INSERTED:String = "textInserted";
		public static const TEXT_DELETED:String  = "textDeleted";
		
		public static const STYLE_SELECTOR_CHANGED:String = "styleSelectorChanged";
		
		public static const USER_STYLE_CHANGED:String = "userStyleChanged";
	}
}