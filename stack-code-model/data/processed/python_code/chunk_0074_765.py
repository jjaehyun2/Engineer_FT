//CLASSE CRÉÉ PAR: Tyler D.

package {

	//Importer les classes nécessaires.
	import flash.display.BitmapData;

	public class TerrainGen {

		private static const GRANDEUR_CASE:int=32; //Sauvegarder la grandeur de chaque case.

		//Fonction pour créer un nouveau terrain.
		public static function creerTerrain(images:Array, monde:Monde, niveau:uint):Terrain {
			var nouvTerrain:Terrain = new Terrain(); //Initialiser le terrain.

			//Créer les murs autour du terrain.
			var murExt:Mur;
			for (var xMur:uint = 0; xMur < (images[0].width*2); xMur++) {
				murExt = new Mur();
				murExt.gotoAndStop(int(Math.random()*5)); //Choisir un image aléatoire pour changer l'apparence.
				//Placer les cases le long du haut du terrain.
				murExt.x=(xMur+1)*GRANDEUR_CASE;
				murExt.y=0;
				
				murExt.visible = false; //Le mur est invisible car c'est une plateforme flottante.
				nouvTerrain.ajouterCase(murExt, false); //Ajouter la case au terrain.
				
				//Même chose qu'en haut, sauf que le mur est visible car c'est le côté de la plateforme flottante.
				//Aussi, cette rangée de murs est le long du bas du terrain.
				murExt = new Mur(); 
				murExt.gotoAndStop(int(Math.random()*5));
				murExt.x=(xMur+1)*GRANDEUR_CASE;
				murExt.y=(images[0].height*2 + 1)*GRANDEUR_CASE;
				nouvTerrain.ajouterCase(murExt, false);
			}
			
			//Même chose qu'en haut, sauf que ceci est pour les murs verticales.
			for (var yMur:uint = 0; yMur < (images[0].height*2); yMur++) {
				murExt = new Mur();
				murExt.gotoAndStop(int(Math.random()*5));
				murExt.x=0;
				murExt.y=(yMur+1)*GRANDEUR_CASE;
				murExt.visible = false;
				nouvTerrain.ajouterCase(murExt, false);
				
				murExt = new Mur();
				murExt.gotoAndStop(int(Math.random()*5));
				murExt.x=(images[0].width*2 + 1)*GRANDEUR_CASE;
				murExt.y=(yMur+1)*GRANDEUR_CASE;
				murExt.visible = false;
				nouvTerrain.ajouterCase(murExt, false);
			}

			//Créer le terrain à partir de 4 modèles.
			for (var quad:uint = 0; quad<4; quad++) {
				//Définir le commencement de chaque quadrant.
				var xDecalage:uint = 1 + (quad % 2) * images[0].width;
				var yDecalage:uint = 1 + uint(quad/2)*images[0].height;

				//Créer une boucle pour passer à travers le modèle entier.
				for (var y:uint = yDecalage; y<(images[quad].height + yDecalage); y++) {
					for (var x:uint = xDecalage; x<(images[quad].width + xDecalage); x++) {
						//Trouver la couleur au point (x, y).
						var couleur:uint=images[quad].getPixel(x-xDecalage,y-yDecalage);
						//Créer une case à partir de la couleur au point (x, y).
						switch (couleur) {
							case 0x00FF00 : //Couleur verte
								//Créer une porte à la position (x, y).
								var nouvPorte:Porte = new Porte();
								nouvPorte.x=x*GRANDEUR_CASE;
								nouvPorte.y=y*GRANDEUR_CASE;
								nouvPorte.gotoAndStop(1); //Arrêter l'animation de la porte en position désactivée.
								nouvTerrain.addChild(nouvPorte);
								nouvTerrain.porte=nouvPorte;
								break;
							case 0xFFFF00 : //Couleur jaune
								//Créer un plancher à la position (x, y).
								var nouvPlancher:Plancher = new Plancher();
								nouvPlancher.gotoAndStop(int(Math.random()*4+1)); //Choisir un image aléatoire pour modifier la couleur.
								nouvPlancher.x=x*GRANDEUR_CASE;
								nouvPlancher.y=y*GRANDEUR_CASE;
								nouvTerrain.ajouterCase(nouvPlancher, false);
								break;
							case 0xFF0000 : //Couleur rouge
								//Créer un trou à la position (x, y).
								var nouvTrou:Mur = new Mur();
								nouvTrou.gotoAndStop(int(Math.random()*5+1)); //Choisir un image aléatoire pour changer l'apparence.
								nouvTrou.x=x*GRANDEUR_CASE;
								nouvTrou.y=y*GRANDEUR_CASE;
								nouvTerrain.ajouterCase(nouvTrou, true);
								break;
							case 0xFFFFFF : //Couleur blanche
								//Créer un mur à la position (x, y).
								var nouvMur:Mur = new Mur();
								nouvMur.gotoAndStop(6); //Choisir l'image du mur.
								nouvMur.x=x*GRANDEUR_CASE;
								nouvMur.y=y*GRANDEUR_CASE;
								nouvTerrain.ajouterCase(nouvMur, false);
								break;
						}
					}
				}
			}

			//Si une porte n'a pas été créée, choisir une position aléatoire.
			if (nouvTerrain.porte==null) {
				var porte:Porte = new Porte();
				//Si la porte est créée dans un mur, choisir une autre position aléatoire.
				var dansMur:Boolean=true;
				do {
					porte.x=int(Math.random()*(images[0].width*2-2))*GRANDEUR_CASE;
					porte.y=int(Math.random()*(images[0].height*2-2))*GRANDEUR_CASE;
					dansMur=false;
					for (var i:uint = 0; i<nouvTerrain.murs.length; i++) {
						if (porte.x==nouvTerrain.murs[i].x&&porte.y==nouvTerrain.murs[i].y) {
							dansMur=true;
						}
					}
				} while (dansMur);
				porte.gotoAndStop(1); //Arrêter l'animation de la porte en position désactivée.
				nouvTerrain.addChild(porte);
				nouvTerrain.porte=porte;
			}
			
			//Créer des ennemis pour que la quantité correspond au nombre du niveau.
			for(var enm:uint; enm < niveau; enm++){
				var nouvEnnemi:Adware=new Adware(nouvTerrain);
				//Si l'ennemi est créé dans un mur, choisir une autre position aléatoire.
				var enmDansMur:Boolean=true;
				do {
					nouvEnnemi.x=int(Math.random()*(images[0].width*2-2))*GRANDEUR_CASE;
					nouvEnnemi.y=int(Math.random()*(images[0].height*2-2))*GRANDEUR_CASE;
					enmDansMur=false;
					for (var iMur:uint = 0; iMur<nouvTerrain.murs.length; iMur++) {
						if (nouvEnnemi.x==nouvTerrain.murs[iMur].x&&nouvEnnemi.y==nouvTerrain.murs[iMur].y) {
							enmDansMur=true;
						}
					}
				} while (enmDansMur);
				//Créer le IA pour l'ennemi et l'attacher à son sujet.
				var adware:IAAdware=new IAAdware(nouvEnnemi,monde);
				nouvEnnemi.ia=adware;
				nouvTerrain.ennemis.push(nouvEnnemi);
				nouvTerrain.addChild(nouvEnnemi);
			}

			//Donner le nombre du niveau au terrain.
			nouvTerrain.niveau = niveau;
			
			//Rendre le nouveau terrain.
			return nouvTerrain;
		}

	}

}