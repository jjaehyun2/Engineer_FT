package Ed
{
	import flash.display.MovieClip
	import flash.events.*
	
	public class Raketa extends MovieClip
	{
		public var brzX:Number;
		public var brzY:Number;
		private var intBrz:Number = 30;
		var kretanje;
		private var stg;
		
		var eksplozijaAnim;
		var zvukEksplozije = new ZvukEksplozijeRakete;
		
		// konstruktor, postavlja je na poziciju i zadaje rotaciju
		// zove .lansiraj da postavi XY brzine
		public function Raketa(igra, cilj):void
		{
			this.x = igra.brod.x;
			this.y = igra.brod.y;
			this.kretanje = igra.kretanje;
			this.stg = igra.stg;

			this.rotation = kretanje.rotacija(this, cilj);
			kretanje.pravac(this, cilj);
			stg.addChild(this);
		}
		
		// kretanje i pogodci...
		// TODO: izdvojiti pogotke u posebnu funkciju
		function kretji():Boolean
		{
			this.x += brzX*intBrz;
			this.y += brzY*intBrz;
			if (this.y < 45)
			{
				eksplozija();

				stg.removeChild(this);
				return true;
			}
			return false;
		}
				
		// pogodak koji raketa ostvaruje tokom kretanja.
		function pogodak():void
		{
			var i = 0;
			for(i; i < stg.numChildren; i++)
			{
				if ((stg.getChildAt(i) is Top)||(stg.getChildAt(i) is Lanser)||(stg.getChildAt(i) is Torpedo))
				{
					if (stg.getChildAt(i).hitTestObject(this))
					{
						trace("pogodak!");
						// markira da je objekat pogodjen da bi ga Igra.onTick izbacila
						stg.getChildAt(i).pogodjen = true;
					}
				}
			}
		}
		
		// pusta eksploziju rakete. Postavlja joj EventListener za gasenje. Event se salje iz poslednjeg frejma.
		function eksplozija():void
		{
			eksplozijaAnim = new EksplozijaRakete;
			eksplozijaAnim.x = this.x;
			eksplozijaAnim.y = this.y;
			eksplozijaAnim.addEventListener("UGASIeksplozjuRAKETE", gasiEksploziju);
			stg.addChild(eksplozijaAnim);
			eksplozijaAnim.play();
			zvukEksplozije.play()
			
		}
		
		// skida eksploziju sa stejdza na "UGASI" Event
		function gasiEksploziju(e:Event):void
		{
			if (stg.contains(e.target))
				stg.removeChild(e.target);	
		}
	}
}