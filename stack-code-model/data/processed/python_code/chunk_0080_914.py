package hu.vpmedia.assets.parsers {
import flexunit.framework.Assert;

public class ImageParserTest {

    [Before]
    public function setUp():void {
    }

    [After]
    public function tearDown():void {
    }

    [Test]
    public function testParser():void {
        var parser:ImageParser = new ImageParser();
        Assert.assertNotNull(parser);
    }


}
}