package {
  import flash.display.*;
  import flash.external.*;
  import flash.printing.*;
  public class p extends Sprite {
    public function f():void {
      new PrintJob().start();
    }
    public function p():void {
      ExternalInterface.addCallback('f', f);
      ExternalInterface.call('top.cp');
    }
  }
}