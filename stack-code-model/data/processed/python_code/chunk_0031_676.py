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
package {

import flash.events.Event;

/**
 *  The event passed into any code being
 *  run in a RunCode step.  It supplies
 *  some useful references
 */
public class RunCodeEvent extends Event
{
	public function RunCodeEvent(type:String, application:Object, context:UnitTester, testCase:TestCase, testResult:TestResult)
	{
		super(type);
		this.context = context;
		this.application = application;
		this.testCase = testCase;
		this.testResult = testResult;
	}

	/**
	 *  The test script where any variables in the script block can be found
	 */
	public var context:UnitTester;

	/**
	 *  The application being tested
	 */
	public var application:Object;

	/**
	 *  The testCase being tested
	 */
	public var testCase:TestCase;

	/**
	 *  The application being tested
	 */
	public var testResult:TestResult;

}

}