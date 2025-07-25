// These Codes are generated by kakaTools ProtocolGenerater v1.3
// ------------------------------------------------------------------
//
// Copyright (c) 2015 linchen.
// All rights reserved.
//
// Email: superkaka.org@gmail.com
//
// ------------------------------------------------------------------

package protocol
{
	import protocol.vo.*;
	import org.superkaka.KLib.net.protocol.*;
	
    public class MessageRegister
    {
        
        static public function getTranslator():PackageTranslator
        {
            var translator:PackageTranslator = new PackageTranslator();
            register(translator);
            return translator;
        }
        
        static public function register(target:PackageTranslator):void
        {
            
            target.RegisterMessage(Protocol.sendLogin, Create_sendLoginVO);
        
            target.RegisterMessage(Protocol.testCommonStruct, Create_testCommonStructVO);
        
            target.RegisterMessage(Protocol.sendString, Create_sendStringVO);
        
        }
        
        
        static public function Create_sendLoginVO():BaseVO
        {
            return new sendLoginVO();
        }
        
        static public function Create_testCommonStructVO():BaseVO
        {
            return new testCommonStructVO();
        }
        
        static public function Create_sendStringVO():BaseVO
        {
            return new sendStringVO();
        }
        
		
    }
}