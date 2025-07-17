//CLASSE CRÉÉ PAR: Adrian G.
package{
	
	public class Stats { //défini stats comme classe publique
		private static var nTemps:int; //défini variable nTemps comme entier
		public static const TEMPS:int = 0; //défini constant TEMPS comme entier égale à 0 pour l'identifier
		
		private static var nComplete:int;
		public static const NCOMPLETE:int = 1;
		
		private static var nElim:int;
		public static const ELIM:int = 2;
		
		private static var nJElim:int;
		public static const JELIM:int = 3;
		
		private static var nTirs:int;
		public static const TIRS:int = 4;
		
		private static var nTirsR:int;
		public static const TIRSR:int = 5;
		
	public function Stats() {
			nTemps = 0; //entier nTemps est égale à 0
			nComplete = 0;
			nElim = 0;
			nJElim = 0;
			nTirs = 0;
			nTirsR = 0;
		} //fin constructeur
		
	static function addition(variable:int):void { //fonction pour additionner aux statistiques
		switch(variable) 
			{ // switch 
			case TEMPS: 
				nTemps++; //ajoute 1 au temps joué
				break;
			case NCOMPLETE:
				nComplete++; //ajoute 1 au nombre de niveaux complèté
				break;
			case ELIM: 
				nElim++; //ajoute 1 au nombre d'ennemis éliminé
				break;
			case JELIM:
				nJElim++; //ajoute 1 au nombre de fois le joueur est éliminé
				break;
			case TIRS:
				nTirs++; //ajout 1 au nombre de fois le joueur a tiré
				break;
			case TIRSR:
				nTirsR++; //ajout 1 au nombre de fois le joueur a réussi a frapper un ennemi
				break;
			} //fin switch
	} // fin fonction addition
	
	
	static function supprime(variable:int):void {
		switch(variable)
			{ // switch 
			case TEMPS:
				nTemps = 0; //remet la variable nTemps à 0
				break;
			case NCOMPLETE:
				nComplete = 0;
				break;
			case ELIM:
				nElim = 0;
				break;
			case JELIM:
				nJElim = 0;
				break;
			case TIRS:
				nTirs = 0;
				break;
			case TIRSR:
				nTirsR = 0;
				break;
			default: //remet tout les valeurs à 0
				nTemps = 0;
				nComplete = 0;
				nElim = 0;
				nJElim = 0;
				nTirs = 0;
				nTirsR = 0;
				break;
			} //fin switch
	} //fin fonction supprime
	
	public static function affiche(variable:int):int { //fonction affiche retourne un entier
		switch(variable) 
			{ //switch
		case TEMPS:
			return nTemps; //retourne valeur contenu dans le variable nTemps
			break;
		case NCOMPLETE:
			return nComplete;
			break;
		case ELIM:
			return nElim;
			break;
		case JELIM:
			return nJElim;
			break;
		case TIRS:
			return nTirs;
			break;
		case TIRSR:
			return nTirsR;
			break;
		}
		return 0; //assure que la fonction peut retourner une valeur pour éviter un erreur 
	}
	
		
	} //fin classe publique
}//fin paquetage