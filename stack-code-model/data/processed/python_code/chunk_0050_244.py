/* 
 * Copyright (c) 2008 Allurent, Inc.
 *
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without restriction,
 * including without limitation the rights to use, copy, modify,
 * merge, publish, distribute, sublicense, and/or sell copies of the
 * Software, and to permit persons to whom the Software is furnished
 * to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 * IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
 * CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
 * TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
 * OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */
package
{
	import com.allurent.coverage.ControllerTest;
	import com.allurent.coverage.model.AllDomainModelTests;
	import com.allurent.coverage.service.CoverageCommunicatorTest;
	import com.allurent.coverage.view.model.AllPresentationModelTests;
	
	import flexunit.framework.TestSuite;

	public class AllTests extends TestSuite
	{
		public function AllTests(param:Object=null)
		{
			super(param);
			addTest(new AllDomainModelTests());
			addTest(new AllPresentationModelTests());
			addTest(new TestSuite(ControllerTest));
			addTest(new TestSuite(CoverageCommunicatorTest));			
		}
		
	}
}