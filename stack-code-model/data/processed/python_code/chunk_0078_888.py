//CLASSE CRÉÉ PAR: Adrian G.

package{
	import flash.events.Event; //importer les classes nécessaires
	import flash.display.*;
	import flash.text.*;
	import flash.events.MouseEvent;
	
	public class MenuAide extends MovieClip{
			
			var affichage:String=""; //défini variable affichage comme une chaîne vide
			
		public function MenuAide() {
			var monMessage:TextField = new TextField(); //défini variable monMessage comme champ de text
			monMessage.x = 200; //position x du champ de text
			monMessage.y = 50; //position y du champ de text
			monMessage.autoSize = TextFieldAutoSize.CENTER; //centrer le text dans monMessage
			monMessage.textColor = 0xffffff; //définir le couleur du text dans monMessage 
			
			affichage = "Utilisez les touches fléchées pour bouger.\n"  //définir le text contenu dans affichage
			+ "Pour tirer, dirigez la souris sur le point où tu veux tirer et cliquez.\n"
			+ "Lorsque tous les ennemis sur l'écran sont élimines, vous pouvez continuer\nau prochain niveau en passant par la porte.\n"
			+ "Si vous êtes attaqués 3 fois il faut recommencer.\n"; 
			monMessage.text = affichage; //le contenu de affichage serais mis dans le champ de text
			addChild(monMessage); //ajoute monMessage sur le scène
		} // fin constructeur
		
		
	} // fin classe
} // fin paquetage