/**
 *  Copyright 2008 Marvin Herman Froeder
 *  Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
 *  http://www.apache.org/licenses/LICENSE-2.0
 *  Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
 *
 */
package tests.funit.utils
{
	import funit.framework.*;
	
	import mx.core.Application;
	
	import sv.utils.ClassUtil;
	
	[TestFixture]
	public class GetClassTests
	{
		
		
		public function GetClassTests()
		{
			
		}
		
		
//------------------------------------------------------------------------------
		
		[Test]
		public function getClassByInstance() : void
		{
			Assert.areSame( Application, ClassUtil.getClass(new Application()) );
		}
		
//------------------------------------------------------------------------------
		
		[Test]
		public function getClassByClass() : void
		{
			Assert.areSame( Application, ClassUtil.getClass(Application));
		}

//------------------------------------------------------------------------------
		
		[Test]
		public function getClassByBaseInstance() : void
		{
			Assert.areSame( Object, ClassUtil.getClass(new Object()) );
		}
		
//------------------------------------------------------------------------------
		
		[Test]
		public function getClassByBaseClass() : void
		{
			Assert.areSame( Object, ClassUtil.getClass(Object) );
		}
		
//------------------------------------------------------------------------------		
		
		[Test]
		public function getClassByPrimitiveInstance() : void
		{
			Assert.areSame( Boolean, ClassUtil.getClass(true) );
		}
		
//------------------------------------------------------------------------------
		
		[Test]
		public function getClassByPrimitiveClass() : void
		{
			Assert.areSame( Boolean, ClassUtil.getClass(Boolean) );
		}
		
//------------------------------------------------------------------------------
		
		[Test]
		[ExpectedError("ArgumentError")]
		public function getClassFailureOnNull() : void
		{
			ClassUtil.getClass(null);
		}
		
//------------------------------------------------------------------------------
		
	}
	
}