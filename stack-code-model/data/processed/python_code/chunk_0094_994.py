package Ed
{
	import flash.utils.Timer;
	import flash.display.MovieClip;
	import flash.events.TimerEvent;
	
	public class Lanser extends MovieClip
	{
		var stg;
		public var poeni = 8;
		public var pucanjaTajmer;
		var ubrzanjeIgre;
		var brzinaIgre;
		var brzX:Number = 3;
		var brod;
		var igra;
		public var pogodjen = false;
		var zvukPucanjaLansera = new LanserPuca;
		public var eksplozija;
		var zvukSmrtiLansera = new SmrtLansera;
		
		public function Lanser(igra):void
		{
			this.igra = igra;
			this.brzinaIgre = igra.brzinaIgre;
			this.ubrzanjeIgre = igra.ubrzanjeIgre;
			this.brod = igra.brod;
			this.stg = igra.stg;
			
			pucanjaTajmer = new Timer(Math.round(((0.5 + Math.random()) * 1000) / ubrzanjeIgre / brzinaIgre));
			pucanjaTajmer.addEventListener(TimerEvent.TIMER, puca, false, 0, true);
			pucanjaTajmer.start();
			
			// bira sa koje strane ce se pojaviti protivnik
			if (Math.random()>0.5)
			{
				this.x = 593;
			}
			else this.x = 7;
			this.y = 15;
			this.stg.addChild(this);
		}
		
		function kretji(ubrzanjeIgre):void
		{
			this.x += brzX * ubrzanjeIgre * brzinaIgre;
			if (this.x > 595)
			{
				brzX = -(Math.abs(brzX));
			}
			else if (this.x < 5)
			{
				brzX = Math.abs(brzX);
			}
		}
		
		function kretjiTeshko(ubrzanjeIgre):void
		{
			this.x += brzX * ubrzanjeIgre * brzinaIgre;
			if ((this.x > 595)||(Math.random()>0.99))
			{
				brzX = -(Math.abs(brzX));
			}
			else if ((this.x < 5||(Math.random()>0.99)))
			{
				brzX = Math.abs(brzX);
			}
		}
		
		function puca(te:TimerEvent):void
		{
			if (igra.pauza == true)
			{
				return;
			}
			zvukPucanjaLansera.play();
			new Torpedo(igra, this.x, this.y);
			pucanjaTajmer.delay = (Math.round(((0.5 + Math.random())*5000) / ubrzanjeIgre));
			pucanjaTajmer.reset();
			pucanjaTajmer.start();
		}
		
		function eksplodira():void
		{
			eksplozija = new LanserEksplozija;
			eksplozija.x = this.x;
			eksplozija.y = this.y;
			eksplozija.addEventListener("UGASIeksplozijuLANSERA", igra.ugasiEksploziju);
			stg.addChild(eksplozija);
			zvukSmrtiLansera.play();
			eksplozija.play();
		}
		
		function iskljuchi():void
		{
			pucanjaTajmer.removeEventListener(TimerEvent.TIMER, puca);
		}
	}
}