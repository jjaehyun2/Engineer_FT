package mobile {
	import com.ObjectExplainer;

	public class MobileDebuggerUtils {
		public static function explainThis(obj:Object,sep:String = ", ", pre:String = "(", post:String = ")"):String {
			var ex:ObjectExplainer = new ObjectExplainer(obj);
			return ex.explainThisWay(sep,pre,post);
		}
	}
}