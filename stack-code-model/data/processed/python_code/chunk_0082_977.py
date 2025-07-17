/**
 *  Copyright 2008 Marvin Herman Froeder
 *  Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
 *  http://www.apache.org/licenses/LICENSE-2.0
 *  Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
 *
 */
package org.sonatype.flexmojos.test.report
{

    import mx.collections.ArrayCollection;

    import org.sonatype.flexmojos.coverage.CoverageDataCollector;

    public class TestCaseReport extends TestCaseReportBase
    {

        public function TestCaseReport()
        {
            methods = new ArrayCollection();
        }

        /*
         * Return the method Object from the internal TestSuite model for the
         * currently executing method on a Test.
         * @param test the Test.
         * @return the method Object.
         */
        public function getMethod( methodName:String ):TestMethodReport
        {
            var method:TestMethodReport;
            for each ( method in methods )
            {
                if ( method.name == methodName )
                {
                    return method;
                }
            }

            method = new TestMethodReport();
            method.name = methodName;
            method.time = 0;

            methods.addItem( method );

            return method;
        }

        /*
           <?xml version="1.0" encoding="UTF-8" ?>
           <testsuite errors="0" skipped="0" tests="1" time="0.312" failures="0" name="com.Test">
           <testcase classname="flex.Test" time="0.297" name="testExecute"/>
           <testcase classname="flex.Test" time="0.297" name="testExecute"/>
           <testcase time="3.125" name="removeAllSnapshots">
           <failure message="All artifacts should be deleted by SnapshotRemoverTask." type="junit.framework.AssertionFailedError">
           junit.framework.AssertionFailedError: All artifacts should be deleted by SnapshotRemoverTask. Found: [H:\home_hudson\.hudson\workspace\Nexus\jdk\1.6\label\windows\trunk\nexus\nexus-test-harness\nexus-test-harness-launcher\target\bundle\nexus-webapp-1.2.0-SNAPSHOT\runtime\work\storage\nexus-test-harness-snapshot-repo\nexus634\artifact\1.0-SNAPSHOT\artifact-1.0-20010101.184024-1.jar, H:\home_hudson\.hudson\workspace\Nexus\jdk\1.6\label\windows\trunk\nexus\nexus-test-harness\nexus-test-harness-launcher\target\bundle\nexus-webapp-1.2.0-SNAPSHOT\runtime\work\storage\nexus-test-harness-snapshot-repo\nexus634\artifact\1.0-SNAPSHOT\artifact-1.0-SNAPSHOT.jar]
           at junit.framework.Assert.fail(Assert.java:47)
           at junit.framework.Assert.assertTrue(Assert.java:20)
           </failure>
           <system-out>[INFO] Nexus configuration validated succesfully.
           </system-out>
           </testcase>
           </testsuite>
         */
        public function toXml():String
        {
            var genxml:String = "<testsuite errors='"+ errors +  
                    "' failures='"+failures+
                    "' name='" + name.replace( "::", "." ) +
                    "' tests='"+tests +
                    "' time='"+ time + "' >";

            for each ( var methodReport:TestMethodReport in methods )
            {
                genxml +=  methodReport.toXml().toXMLString();
            }

            var data:Object = CoverageDataCollector.extractCoverageResult();
            for ( var cls:String in data )
            {
                genxml +=  TestCoverageReport(data[cls]).toXml() ;
            }
            
            genxml += "</testsuite>"
            return genxml;
        }

    }
}