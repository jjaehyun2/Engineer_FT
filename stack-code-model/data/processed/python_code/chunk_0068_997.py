/*
	Adobe Systems Incorporated(r) Source Code License Agreement
	Copyright(c) 2005 Adobe Systems Incorporated. All rights reserved.
	
	Please read this Source Code License Agreement carefully before using
	the source code.
	
	Adobe Systems Incorporated grants to you a perpetual, worldwide, non-exclusive, 
	no-charge, royalty-free, irrevocable copyright license, to reproduce,
	prepare derivative works of, publicly display, publicly perform, and
	distribute this source code and such derivative works in source or 
	object code form without any attribution requirements.  
	
	The name "Adobe Systems Incorporated" must not be used to endorse or promote products
	derived from the source code without prior written permission.
	
	You agree to indemnify, hold harmless and defend Adobe Systems Incorporated from and
	against any loss, damage, claims or lawsuits, including attorney's 
	fees that arise or result from your use or distribution of the source 
	code.
	
	THIS SOURCE CODE IS PROVIDED "AS IS" AND "WITH ALL FAULTS", WITHOUT 
	ANY TECHNICAL SUPPORT OR ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING,
	BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
	FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  ALSO, THERE IS NO WARRANTY OF 
	NON-INFRINGEMENT, TITLE OR QUIET ENJOYMENT.  IN NO EVENT SHALL MACROMEDIA
	OR ITS SUPPLIERS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
	EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
	PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
	OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
	WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
	OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOURCE CODE, EVEN IF
	ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

package mx.collaboration.xmpp.protocol.tests
{
	import flash.events.Event;
	import flash.utils.*;
	
	import flexunit.framework.TestCase;
	
	import mx.collaboration.xmpp.protocol.*;
	import mx.collaboration.xmpp.protocol.authenticators.*;
	import mx.collaboration.xmpp.protocol.channels.*;
	import mx.collaboration.xmpp.protocol.channels.httpbinding.*;
	import mx.collaboration.xmpp.protocol.events.*;
	import mx.collaboration.xmpp.protocol.tests.authenticators.*;;
    
    public class TestNonSASLAuthenticator extends TestCase
    {

        public function testBaseAuthenticator():void
        {
            var stream:XMPPStream = new XMPPStream();
            
            stream.userJID = new JID( TestConfig.GOOD_USER );
            stream.channel = new SocketChannel( TestConfig.GOOD_SERVER, TestConfig.GOOD_SERVER, TestConfig.GOOD_PORT );
            stream.authenticator = new PassAuthenticator();          
            stream.addEventListener( XMPPStreamEvent.CONNECT,
            						 addAsync( checkAuthenticateSuccessThenClose, TestConfig.DEFAULT_TIMEOUT ) );            
            stream.connect();
        }

        public function testDigestAuthenticationSocketChannel():void
        {
            var stream:XMPPStream = new XMPPStream();
            
            stream.userJID = new JID( TestConfig.GOOD_USER );
            stream.channel = new SocketChannel( TestConfig.GOOD_SERVER, TestConfig.GOOD_SERVER, TestConfig.GOOD_PORT );
            stream.authenticator = new NonSASLAuthenticator( TestConfig.GOOD_PASS, 
                                                             NonSASLAuthenticator.DIGEST );          
            stream.addEventListener( XMPPStreamEvent.CONNECT, 
                                     addAsync( checkAuthenticateSuccessThenClose, TestConfig.DEFAULT_TIMEOUT) );            
            stream.connect();
        }

        public function testDigestAuthenticationHTTPBindingChannel():void
        {
            var stream:XMPPStream = new XMPPStream();
            
            stream.userJID = new JID( TestConfig.GOOD_USER );
            stream.channel = new HTTPBindingChannel( TestConfig.GOOD_SERVER, TestConfig.GOOD_PORT, TestConfig.BINDING_URI );
            stream.authenticator = new NonSASLAuthenticator( TestConfig.GOOD_PASS, 
                                                             NonSASLAuthenticator.DIGEST );          
            stream.addEventListener( XMPPStreamEvent.CONNECT, 
                                     addAsync( checkAuthenticateSuccessThenClose, TestConfig.DEFAULT_TIMEOUT) );            
            stream.connect();
        }

 
        public function testPlaintextAuthentication():void
        {
            var stream:XMPPStream = new XMPPStream();
            
            stream.userJID = new JID( TestConfig.GOOD_USER );
            stream.channel = new SocketChannel( TestConfig.GOOD_SERVER, TestConfig.GOOD_SERVER, TestConfig.GOOD_PORT );
            stream.authenticator = new NonSASLAuthenticator( TestConfig.GOOD_PASS, 
                                                             NonSASLAuthenticator.PLAINTEXT );          
            stream.addEventListener( XMPPStreamEvent.CONNECT, 
                                     addAsync( checkAuthenticateSuccessThenClose, TestConfig.DEFAULT_TIMEOUT) );
            
            stream.connect();
        }        
        
        public function checkAuthenticateSuccessThenClose( e:Event ):void
        {
            assertTrue( e.target.isConnected() );            
            
            e.target.disconnect();
        }

    }
    
}