// Copyright: Hiroshi Ichikawa <http://gimite.net/en/>
// License: New BSD License
// Reference: http://dev.w3.org/html5/websockets/
// Reference: http://tools.ietf.org/html/draft-hixie-thewebsocketprotocol-76

package net.gimite.websocket {

import flash.system.Security;

public class WebSocketMainInsecure extends WebSocketMain {

  public function WebSocketMainInsecure() {
    Security.allowDomain("*");
    super();
  }
  
}

}