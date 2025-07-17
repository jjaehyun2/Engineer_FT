/**
 * User: booster
 * Date: 14/08/14
 * Time: 20:56
 */
package plugs {
import org.flexunit.asserts.assertEquals;
import org.flexunit.asserts.assertNotNull;
import org.flexunit.asserts.assertTrue;

import plugs.consumers.DebugConsumer;
import plugs.inputs.StringInput;
import plugs.outputs.StringOutput;
import plugs.providers.ValueProvider;

public class PullTest {
    public function PullTest() {
    }

    [Before]
    public function setUp():void {

    }

    [After]
    public function tearDown():void {

    }

    [Test]
    public function simpleTest():void {
        var provider:ValueProvider = new ValueProvider(new StringOutput("strOut"), "StringValue");
        var consumer:DebugConsumer = new DebugConsumer(new StringInput("strIn"), "DebugConsumer");

        var conn:Connection = Connection.connect(provider.output, consumer.input);

        assertNotNull(conn);

        provider.value = "Test";

        var funcCalled:Boolean = false;

        consumer.dataReceivedFunc = function(data:*, connection:Connection):void {
            assertEquals("Test", data);
            assertEquals(conn, connection);

            funcCalled = true;
        };

        consumer.pullData();

        assertTrue(funcCalled);
    }
}
}