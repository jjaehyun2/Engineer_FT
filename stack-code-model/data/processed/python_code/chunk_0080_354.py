 //CLASSE CRÉÉ PAR: Adrian G., Tyler D., John A.

package{
	
	import flash.display.*; //importer les classes
	import flash.events.*;
	
	public class Monde extends MovieClip{ //défini les variables
		
		public var terrain:Terrain;
		public var niveauCourant:uint = 0;
		public var joueur:Joueur;
		private var entree:Entree;
		private var ennemi:Adware;
		private var adware:IAAdware;
		private var fin:Fin;
		private var blessures:Blessures;
		private var maps:Array = new Array();
		
		public function Monde():void{ 
			//supprime les statistiques lorsqu'une nouvelle partie commence et ajoute tout les modèles dans un tableau.
			Stats.supprime(-1);
			maps.push(new map01(0, 0));
			maps.push(new map02(0, 0));
			maps.push(new map03(0, 0));
			maps.push(new map04(0, 0));
			maps.push(new map05(0, 0));
			maps.push(new map06(0, 0));
			maps.push(new map07(0, 0));
			maps.push(new map08(0, 0));
			maps.push(new map09(0, 0));
			maps.push(new map10(0, 0));
			
			var quadrants:Array = new Array(); //choisi 4 modèles aléatoirement
			for(var q:uint = 0; q < 4; q++){
				quadrants[q] = maps[int(Math.random()*10)].clone();
			}			
			niveauCourant++;
			//Créer le terrain.
			terrain = TerrainGen.creerTerrain(quadrants, this, niveauCourant);
			addChild(terrain);
			
			//Créer le joueur.
			joueur = new Joueur(this);
			joueur.x = 200;
			joueur.y = 300;
			addChild(joueur);
			terrain.joueur = joueur; //Ajouter le joueur au terrain.
			//Créer la classe d'entrée.
			entree = new Entree(joueur);
			addChild(entree);
			//Créer la classe d'affichage.
			blessures = new Blessures(this);
			blessures.x = 0;
			blessures.y = 20;
			addChild(blessures);
		}
		
		function init(){
			//Initialiser les composantes du monde.
			entree.init();
			for(var enm:uint; enm < terrain.ennemis.length; enm++){
				terrain.ennemis[enm].ia.init();
			}
			stage.addEventListener(Event.ENTER_FRAME, loop); //Ajouter un écouteur d'événement à chaque image.
		}
		
		//Fonction pour aller au prochain niveau et supprimer celui d'avant.
		private function prochainNiveau():void{
			//Supprimer le terrain.
			removeChild(terrain);
			
			var quadrants:Array = new Array(); //choisi 4 modèles aléatoirement
			for(var q:uint = 0; q < 4; q++){
				quadrants[q] = maps[int(Math.random()*10)].clone();
			}
			niveauCourant++;
			//Créer le terrain.
			terrain = TerrainGen.creerTerrain(quadrants, this, niveauCourant);
			addChild(terrain);
			terrain.joueur = joueur; //Ajouter le joueur au terrain.
			addChild(terrain);
			//Mettre le joueur par dessus le terrain.
			setChildIndex(joueur, getChildIndex(terrain));
			setChildIndex(terrain, getChildIndex(joueur)-1);
			//Initialiser les ennemis nouveaux.
			for(var enm:uint; enm < terrain.ennemis.length; enm++){
				terrain.ennemis[enm].ia.init();
			}
			
			//Ajouter un niveau complet aux statistiques.
			Stats.addition(Stats.NCOMPLETE);
		}
		
		function loop(event:Event):void{
			//Actualiser la position du joueur et afficher l'affichage.
			joueur.updatePositionX();
			joueur.updatePositionY();
			blessures.affiche();
			
			//Si la porte est active, détecter si le joueur touche la porte.
			if(terrain.porteActive){
				if(joueur.x + joueur.width/2 >= terrain.porte.x && 
				   		joueur.x + joueur.width/2 <= (terrain.porte.x + terrain.porte.width) &&
				   		joueur.y + joueur.height/2 >= terrain.porte.y && 
				   		joueur.y + joueur.height/2 <= (terrain.porte.y + terrain.porte.height)){
					prochainNiveau(); //Passer au prochain niveau si le joueur touche la porte.
				}
			}
			
			//Actualiser les ennemis.
			for(var i:uint = 0; i < terrain.ennemis.length; i++){
				terrain.ennemis[i].ia.loop();
				terrain.ennemis[i].updatePositionX();
				terrain.ennemis[i].updatePositionY();
			}
		}
		
		function mort():void{
			//Ajouter aux statistiques.
			Stats.addition(Stats.JELIM);
			
			//Tuer tous les ennemis qui restent.
			for(var i:uint = 0; i < terrain.ennemis.length; i++){
				terrain.ennemis[i].ia.mort();
			} 
			//Enlever tous les composantes du terrain.
			 removeChild(terrain);
			 removeChild(joueur);
			 entree.remove();
			 removeChild(entree);
			 removeChild(blessures);
			 //Créer l'écran de fin.
			 fin = new Fin();
			 fin.x = 192;
			 fin.y = 144;
			 stage.addChild(fin);
			 fin.btnRetourF.addEventListener(MouseEvent.CLICK, recommence);
				
		} // fin mort
		
		function recommence(event:MouseEvent):void{
			//Ajouter le score et le nom à la liste.
			var score:int = Stats.affiche(Stats.ELIM) - Stats.affiche(Stats.TIRS) + (Stats.affiche(Stats.NCOMPLETE) * 30);
			U4A3_ProjetFinal.scores.ajouterScore(score, fin.nom_txt.text);
			//Supprimer l'écran de fin et afficher le menu principal.
			stage.removeChild(fin);
			U4A3_ProjetFinal.menuP.visible = true;
		}
	}	//fin classe

} //fin paquetage