/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.flexunit.internals.runners.statements.cases
{
	import org.flexunit.Assert;
	import org.flexunit.internals.runners.statements.RunBeforesClass;
	import org.flexunit.runners.model.mocks.FrameworkMethodMock;
	import org.flexunit.token.ChildResult;
	import org.flexunit.token.mocks.AsyncTestTokenMock;

	public class RunBeforesClassCase
	{
		//TODO: Ensure that these tests and this test case are properly designed
		
		protected var runBeforesClass:RunBeforesClass;
		protected var frameworkMethodMock:FrameworkMethodMock;
		protected var befores:Array;
		protected var target:Object;
		
		[Before(description="Create an instance of the RunBeforesClass class")]
		public function createRunBeforesClass():void {
			frameworkMethodMock = new FrameworkMethodMock();
			befores = [frameworkMethodMock];
			target = new Object();
			runBeforesClass = new RunBeforesClass(befores, target);
		}
		
		[After(description="Remove the reference to the instance of the RunBeforesClass class")]
		public function destroyRunBeforesClass():void {
			runBeforesClass = null;
			frameworkMethodMock = null;
			befores = null;
			target = null;
		}
		
		//TODO: It currently is hard to determine which IAsyncStatement is being returned with the withPotentialAsync function
		[Test(description="Ensure that the overridden withPotentialAsync function returns the correct instance of an IAsyncStatement when the metadata does not have a 'BeforeClass'")]
		public function withPotentialAsyncNoBeforeClassTest():void {
			frameworkMethodMock.mock.method("getSpecificMetaDataArg").withArgs("BeforeClass", "async").once.returns("notTrue");
			
			runBeforesClass.handleChildExecuteComplete(new ChildResult(new AsyncTestTokenMock()));
			
			frameworkMethodMock.mock.verify();
		}
		
		[Test(description="Ensure that the overridden withPotentialAsync function returns the correct instance of an IAsyncStatement when the metadata has a 'BeforeClass'")]
		public function withPotentialAsyncHasBeforeClassTest():void {
			frameworkMethodMock.mock.method("getSpecificMetaDataArg").withArgs("BeforeClass", "async").once.returns("true");
			
			runBeforesClass.handleChildExecuteComplete(new ChildResult(new AsyncTestTokenMock()));
			
			frameworkMethodMock.mock.verify();
		}
		
		[Test(description="Ensure that the toString function returns the correct string value")]
		public function toStringTest():void {
			Assert.assertEquals( "RunBeforesClass", runBeforesClass.toString() );
		}
	}
}