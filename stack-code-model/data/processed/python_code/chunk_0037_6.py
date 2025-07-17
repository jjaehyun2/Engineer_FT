package dom.tidesdk.api
{
	/**
	 * <p>Script object.</p>
	 */
	public class TScript
	{
		//
		// METHODS
		//

		/**
		 * <p> Adds a script evalutor Script evaluators are
		 * responsible for matching and evaluating custom
		 * &lt;script&gt; types, and preprocessing URLs. </p>
		 * 
		 *    <p> When a <tt>&lt;script
		 * type="text/language"&gt;</tt> tag is seen, the
		 * first evaluator that returns true to
		 * <tt>canEvaluate("text/language")</tt> will
		 * evaluate that script. </p>
		 * 
		 *    <p>When a URLRequest is received, the first
		 * evaluator that returns true to
		 * <tt>canPreprocess(URL)</tt> will preprocess that
		 * URL. Evaluators should follow this API:</p>
		 * 
		 *   <ol><li> <tt>canEvaluate(String mimeType)</tt>
		 * returns true or false. </li>
		 *  <li> <tt>canPreprocess(String mimeType)</tt>
		 * returns true or false. </li>
		 * <li> <tt>evaluate(String mimeType, String name,
		 * String sourceCode, Object scope)</tt> returns
		 * result of evaluation </li>
		 * <li> <tt>preprocess(String url, Object scope)</tt>
		 * returns preprocessed content. </li></ol>
		 * 
		 * @param evaluator  The evaluator to add. 
		 */
		public function addScriptEvaluator(evaluator:String):void {}

		/**
		 * 
		 * 
		 * @param evaluator  The mimeType to check 
		 * 
		 * @return bool   
		 */
		public function canEvaluate(evaluator:String):Boolean { return false; }

		/**
		 * 
		 * 
		 * @param url  The URL to check 
		 * 
		 * @return bool   
		 */
		public function canPreprocess(url:String):Boolean { return false; }

		/**
		 * <p>Evaluates a string of code</p>
		 * 
		 * @param mimeType  "The code's mime type (i.e. \"text/ruby\", \"text/php\")" 
		 * @param name  "The name of the code's origin (usually a filename, or URL)" 
		 * @param code  The actual code 
		 * @param scope  "global variable scope (i.e. \"window\")" 
		 * 
		 * @return Any   
		 */
		public function evaluate(mimeType:String, name:String, code:String, scope:String):* { return null; }

		/**
		 * <p>Runs an app URL through preprocessing,
		 * returning the result as a string</p>
		 * 
		 * @param URL  the URL for this resource (app, ti, and file URLs are accepted) 
		 * @param scope  global variable scope to expose into the preprocessed file 
		 * 
		 * @return String   
		 */
		public function preprocess(URL:String, scope:String):String { return ""; }

		/**
		 * <p>Removes a script evalutor</p>
		 * 
		 * @param evaluator  The evaluator to remove 
		 */
		public function removeScriptEvaluator(evaluator:String):void {}

		public function TScript() {}
	}
}