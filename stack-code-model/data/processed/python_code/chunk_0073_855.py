//CLASSE CRÉÉE PAR: Tyler D. et Adrian G.
package {

	import flash.utils.Timer;
	import flash.events.TimerEvent;
	import flash.events.Event;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Loader;

	public class IAAdware {

		//Déclarer les variables.
		private var adware:IControlable;
		private var monde:Monde;
		private var timer:Timer;
		private var bitmap:Bitmap;
		private var image:int;

		public function IAAdware(adware:IControlable, monde:Monde):void {
			//Sauvegarder les variables.
			this.adware=adware;
			this.monde=monde;

			timer=new Timer(1000);//Créer un nouveau Timer qui donne un événement à chaque seconde.
			timer.addEventListener(TimerEvent.TIMER, periodique);//Créer un écouteur d'événement pour le Timer.
		}

		public function init():void {
			timer.start();//Commencer le Timer.
		}

		function periodique(event:TimerEvent):void {
			//Arrêter l'ennemi, tirer vers le joueur, et changer de direction.
			adware.setVitesseX(0);
			adware.setVitesseY(0);
			adware.clic(monde.joueur.x + monde.joueur.width/2, monde.joueur.y + monde.joueur.height/2);
			changeDir(int(Math.random()*4));
		}

		public function loop():void {

		}

		private function changeDir(dir:int):void {
			//Choisir une direction à partir du int dir.
			switch (dir) {
				case dir = 0 :
					adware.setVitesseX(1);
					break;
				case dir = 1 :
					adware.setVitesseX(-1);
					break;
				case dir = 2 :
					adware.setVitesseY(1);
					break;
				case dir = 3 :
					adware.setVitesseY(-1);
					break;
			}
		}

		//Arrêter le Timer quand l'ennemi est mort.
		public function mort():void {
			timer.stop();
			timer.removeEventListener(TimerEvent.TIMER, periodique);
		}

	}

}