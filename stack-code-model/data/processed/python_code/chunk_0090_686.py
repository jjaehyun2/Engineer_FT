/*	Programmeurs:	Tyler Dibattista, Adrian Giammaria, John Atanasov	
	Date:			1/26/2017
	File Name:		Main.as
	Flash File: 	Main.fla
	SWF File:		Main.swf
	Description:	Projet pour examen ICS4U - Jeu «Viruswave»
					style jeu d'arcade sans fin où le joueur élimine
					des viruses.*/

//  IMPORTANT!!! Plusieurs fichiers/classes existent, tous écrits par différents
// 	membres de l'équipe. Les ressources visuelles ont été crées par Adrian Giammaria.

/*Fichiers classes externes: Adware, Blessures, Ennemi, Entree, IAAdware, IATrojan
IControlable, Joueur, Laser, Monde, Porte, Score, Stats, Terrain, TerrainGen*/ 

/*Liste des modifications apportés au projet est présent au lien Github : https://github.com/tylerdibo/projet-viruswave/ 
Tous les ressources visuelles sont aussi présents sur Github.*/

//CLASSE CRÉÉ PAR: Tyler D., Adrian G., John A.

package {	//Importer les classes nécessaires																		
	
	import flash.display.*;		//Ensemble des classes clés pour l'affichage visuelle en flash						
	import flash.events.*;		//Ensemble de classes clés pour l'utilisation du souris en flash
	import flash.media.*;		//Ensemble de classes clés pour le son
	
	public class U4A3_ProjetFinal extends MovieClip{	//Création de la classe Main												
	
		static public var menuP:MenuPrinc; //Création de la variable statique menuP comme MovieClip MenuPrinc		
		private var monde:Monde; //Création de la variable monde comme MovieClip Monde 								
		static public var scores:Score;	//Création de la variable statique scores comme MovieClip Score				
		private var fin:Fin;	//Création de la variable fin comme Movieclip Fin									
		private var mus:Sound = new musique();	//Création de la variable mus pour le son
		
		public function U4A3_ProjetFinal(){	//Création de la fonction Main														
			
			mus.play();		//Joue le son
			
			//Création du menuP principal et affichage.																
			menuP = new MenuPrinc();	//La variable menuP est un nouveau MovieClip MenuPrinc			
			menuP.x = 192;
			menuP.y = 144;
			addChild(menuP);	//Ajoute le menuP au stage													
			
			//Ajouter un écouteur d'événement pour commencer le jeu, donc fait appel à la fonction partie			
			menuP.btnPartie.addEventListener(MouseEvent.CLICK, partie); 											
			scores = new Score();	//La variable scores est un nouveau MovieClip Score								
			
			//trace(stats.children());
			
		} //Fin de la fonction Main																					
		function partie (event:MouseEvent):void {	//Création de la fonction partie								
			
			//Création du monde de jeu et ajoute-le à la scène.														
			if (monde != null) {	//Si la valeur de monde n'est pas null, l'énoncé if effectue:			
				removeChild(monde);	//Enlève monde																	
			}	//Fin de l'énoncé if																				
			monde = new Monde();	//La variable monde est un nouveau Monde										
			addChild(monde);	//Ajoute le monde au stage													
			monde.init(); //Initialisation du monde																	
			
			//Cacher le menuP.			
			menuP.visible = false;																					
		}	//Fin de la fonction partie																				
		
	}	//Fin de la classe Main																						
	
}	//Fin du package