/**
 * Copyright (C) 2008 Darshan Sawardekar.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.puremvc.as3.multicore.utilities.fabrication.routing.firewall.test {
    import org.puremvc.as3.multicore.utilities.fabrication.addons.BaseTestCase;
    import org.puremvc.as3.multicore.utilities.fabrication.addons.mock.EventListenerMock;
    import org.puremvc.as3.multicore.utilities.fabrication.events.RouterFirewallEvent;
    import org.puremvc.as3.multicore.utilities.fabrication.interfaces.IDisposable;
    import org.puremvc.as3.multicore.utilities.fabrication.interfaces.IFirewallRule;
    import org.puremvc.as3.multicore.utilities.fabrication.interfaces.IRouterFirewall;
    import org.puremvc.as3.multicore.utilities.fabrication.interfaces.IRouterMessage;
    import org.puremvc.as3.multicore.utilities.fabrication.patterns.observer.TransportNotification;
    import org.puremvc.as3.multicore.utilities.fabrication.routing.RouterMessage;
    import org.puremvc.as3.multicore.utilities.fabrication.routing.firewall.*;
    import org.puremvc.as3.multicore.utilities.fabrication.routing.firewall.mock.FirewallRuleMock;
    import org.puremvc.as3.multicore.utilities.pipes.messages.Message;

    /**
     * @author Darshan Sawardekar
     */
    public class MultiRuleFirewallTest extends BaseTestCase {

        private var firewall:MultiRuleFirewall = null;


        [Before]
        public function setUp():void
        {
            firewall = new MultiRuleFirewall();
        }

        [After]
        public function tearDown():void
        {
            firewall.dispose();
            firewall = null;
        }

        [Test]
        public function testMultiRuleFirewallHasValidType():void
        {
            assertType(MultiRuleFirewall, firewall);
            assertType(IRouterFirewall, firewall);
            assertType(IDisposable, firewall);
        }

        [Test]
        public function testMultiRuleFirewallAllowsAddingRules():void
        {
            firewall.addRule(new FirewallRuleMock());
            firewall.addRule(new FirewallRuleMock());
            firewall.addRule(new FirewallRuleMock());
        }

        [Test]
        public function testMultiRuleFirewallAllowsRemovingRules():void
        {
            var sampleSize:int = 25;
            var rule:IFirewallRule;
            var rulesAdded:Array = new Array();
            var i:int = 0;

            for (i = 0; i < sampleSize; i++) {
                rule = new FirewallRuleMock();
                rulesAdded.push(rule);
                firewall.addRule(rule);
            }

            for (i = 0; i < sampleSize; i++) {
                rule = rulesAdded[i];
                assertTrue(firewall.hasRule(rule));
                firewall.removeRule(rule);
                assertFalse(firewall.hasRule(rule));
            }
        }

        [Test]
        public function testMultiRuleFirewallExecutesRules():void
        {
            var sampleSize:int = 25;
            var rule:FirewallRuleMock;
            var message:IRouterMessage = new RouterMessage(
                    Message.NORMAL, null, "A/A0/OUTPUT", "B/B0/INPUT",
                    new TransportNotification("note", "body", "type")
                    );
            var rulesAdded:Array = new Array();
            var i:int = 0;

            for (i = 0; i < sampleSize; i++) {
                rule = new FirewallRuleMock();
                rulesAdded.push(rule);
                rule.mock.method("process").withArgs(String, String, String, IRouterMessage).once;

                firewall.addRule(rule);
            }

            firewall.process(message);

            for each (rule in rulesAdded) {
                verifyMock(rule.mock);
            }
        }

        [Test]
        public function testMultiRuleFirewallObeysRules():void
        {
            var message:IRouterMessage = new RouterMessage(
                    Message.NORMAL, null, "A/A0/OUTPUT", "B/B0/INPUT",
                    new TransportNotification("note", "body", "type")
                    );
            var rule:FirewallRuleMock = new FirewallRuleMock();
            rule.mock.method("process").withArgs(String, String, String, IRouterMessage).returns(true);

            firewall.addRule(rule);

            assertTrue(firewall.process(message));

            firewall.removeRule(rule);

            rule = new FirewallRuleMock();
            rule.mock.method("process").withArgs(String, String, String, IRouterMessage).returns(false);
            firewall.addRule(rule);

            assertFalse(firewall.process(message));
        }

        [Test]
        public function testMultiRuleFirewallReturnsFalseIfAnyRuleFails():void
        {
            var message:IRouterMessage = new RouterMessage(
                    Message.NORMAL, null, "A/A0/OUTPUT", "B/B0/INPUT",
                    new TransportNotification("note", "body", "type")
                    );
            var rule:FirewallRuleMock;
            var sampleSize:int = 25;
            var i:int = 0;

            for (i = 0; i < sampleSize; i++) {
                rule = new FirewallRuleMock();
                rule.mock.method("process").withArgs(String, String, String, IRouterMessage).returns(true);
                firewall.addRule(rule);
            }

            rule = new FirewallRuleMock();
            rule.mock.method("process").withArgs(String, String, String, IRouterMessage).returns(false);
            firewall.addRule(rule);

            assertFalse(firewall.process(message));
        }

        [Test]
        public function testMultiRuleFirewallSendsAllowedEventWhenMessageRuleIsTrue():void
        {
            var message:IRouterMessage = new RouterMessage(
                    Message.NORMAL, null, "A/A0/OUTPUT", "B/B0/INPUT",
                    new TransportNotification("note", "body", "type")
                    );
            var rule:FirewallRuleMock;
            var sampleSize:int = 25;
            var eventListener:EventListenerMock;
            var i:int = 0;

            for (i = 0; i < sampleSize; i++) {
                rule = new FirewallRuleMock();
                rule.mock.method("process").withArgs(String, String, String, IRouterMessage).returns(true);
                firewall.addRule(rule);
            }

            eventListener = new EventListenerMock(firewall, RouterFirewallEvent.ALLOWED_MESSAGE);
            eventListener.mock.method("handle").withArgs(RouterFirewallEvent).once;

            firewall.process(message);

            verifyMock(eventListener.mock);
        }

        [Test]
        public function testMultiRuleFirewallSendsBlockedEventWhenMessageRuleIsFalse():void
        {
            var message:IRouterMessage = new RouterMessage(
                    Message.NORMAL, null, "A/A0/OUTPUT", "B/B0/INPUT",
                    new TransportNotification("note", "body", "type")
                    );
            var rule:FirewallRuleMock;
            var sampleSize:int = 25;
            var eventListener:EventListenerMock;
            var i:int = 0;

            for (i = 0; i < sampleSize; i++) {
                rule = new FirewallRuleMock();
                rule.mock.method("process").withArgs(String, String, String, IRouterMessage).returns(false);
                firewall.addRule(rule);
            }

            eventListener = new EventListenerMock(firewall, RouterFirewallEvent.BLOCKED_MESSAGE);
            eventListener.mock.method("handle").withArgs(RouterFirewallEvent).once;

            firewall.process(message);

            verifyMock(eventListener.mock);
        }

        [Test(expects="Error")]
        public function testMultiRuleFirewallResetsAfterDisposal():void
        {
            var firewall:MultiRuleFirewall = new MultiRuleFirewall();
            firewall.dispose();

            firewall.hasRule(new FirewallRuleMock());
        }
    }
}