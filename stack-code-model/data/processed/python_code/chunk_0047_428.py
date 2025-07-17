package  {
	import flash.display.Bitmap;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	public class ImageFactory {
		
		/*[Embed(source = "../_assets/01.jpg")] private static const Img01:Class;
		[Embed(source = "../_assets/02.jpg")] private static const Img02:Class;
		[Embed(source = "../_assets/03.jpg")] private static const Img03:Class;
		[Embed(source = "../_assets/04.jpg")] private static const Img04:Class;
		[Embed(source = "../_assets/05.jpg")] private static const Img05:Class;*/
		
		public static function getImages():Vector.<Bitmap> {
			var vector:Vector.<Bitmap> = new Vector.<Bitmap>();
			vector.push(new Bitmap(new Img01));
			vector.push(new Bitmap(new Img02));
			vector.push(new Bitmap(new Img03));
			vector.push(new Bitmap(new Img04));
			vector.push(new Bitmap(new Img05));
			
			for (var i:int = 0; i <vector.length ; i++) {
				vector[i].smoothing = true;
			}
			return vector;
		}
		
	}
}