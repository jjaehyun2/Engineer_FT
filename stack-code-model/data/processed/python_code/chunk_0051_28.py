package {
  import flash.display.Sprite; 
  import com.dayvson.lib.Sample;
  import flash.text.TextField;
  [SWF(width=640, height=360, background=0x000000)]
  
  public class VersionAppUsingExternalSWC extends Sprite {
    public function VersionAppUsingExternalSWC() {
      var sample:Sample = new Sample();
      var txt:TextField = new TextField();
      txt.text = sample.getVersion();
      trace("VersionAppUsingExternalSWC #@@#@#@ -=> ");
      txt.x = 100;
      txt.y = 100;
      addChild(txt);
    }
  }
}