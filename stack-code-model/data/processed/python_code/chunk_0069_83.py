package
{
    import flash.display.Sprite;
    import flash.net.navigateToURL;
    import flash.net.URLRequest;
    import flash.net.URLVariables;

    public class ScoreUploader extends Sprite {

        public function ScoreUploader(score:int) {
            var url:String = "http://hazarddigital.com/score.php";
            var request:URLRequest = new URLRequest(url);
            var variables:URLVariables = new URLVariables();
            variables.exampleSessionId = new Date().getTime();
            variables.score = score;
            request.data = variables;
            navigateToURL(request);
        }
    }
}