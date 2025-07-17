//CLASSE CRÉÉE PAR: Tyler D.
package{	//Importer les classes nécessaires

	import flash.display.*;	//Ensemble des classes clés pour l'affichage visuelle en flash

	public class Ennemi extends MovieClip implements IControlable{	//Création de la classe Ennemi qui étend le MovieClip et inclut IControlable
		
		private var vitesse:int = 5;	//Création de la variable vitesse qui est un int et a une valeur initial de 5
		private var vx:int = 0;	//Création de la variable vx qui est un int et a un valeur initial de 0
		private var vy:int = 0;	//Création de la variable vy qui est un int et a un valeur initial de 0
		private var terrain:Terrain;	//Création de la variable terrain
		
		public function Ennemi(terrain:Terrain){	//Création de la fonction Ennemi
			this.terrain = terrain;	//Sauvegarder le terrain.
		}	//Fin de la fonction Ennemi
		
		public function clic(xSouris:int, ySouris:int):void{	//Création de la fonction clic
			
		}	//Fin de la fonction clic
		
		public function updatePositionX():void{	//Création de la fonction updatePositionX
			//Actualiser la position x et tester pour une collision.
			this.x += vx;
			testCollisionX();
		}	//Fin de la fonction updatePositionX
		
		public function updatePositionY():void{	//Création de la fonction updatePositionY 
			//Actualiser la position y et tester pour une collision.
			this.y += vy;
			testCollisionY();
		}	//Fin de la fonction updatePositionY
		
		public function setVitesseX(vitx:int):void{	//Création de la fonction setVitesseX
			//Modifier la vitesse.
			vx = vitx * vitesse;
		}	//Fin de la fonction setVitesseX
		
		public function setVitesseY(vity:int):void{	//Création de la fonction setVitesseY
			//Modifier la vitesse.
			vy = vity * vitesse;
		}	//Fin de la fonction setVitesseY
		
		private function testCollisionX():Boolean{	//Création de la fonction testCollisionX
			//Assurer que l'entité ne touche pas un mur.
			for(var i:uint = 0; i<terrain.murs.length; i++){
				if(hitTestObject(terrain.murs[i])){	//Si hitTestObject détecte un mur, l'énoncé if effectue:
					do{	//Fait
						if(vx > 0){	//Si vx est plus que 0, retourner vers la gauche:
							this.x--;	//
						}else{	//Si non, retourner vers la droite:
							this.x++;	//
						}	//Fin de l'énoncé if et else
					}while(hitTestObject(terrain.murs[i]));	//Continuer à retourner si il est encore dans le mur.
					return true;	//Rendre la valeur true
				}	//Fin de l'énoncé if
			}	//Fin de la boucle for
			return false;	//Rendre false
		}	//Fin de la fonction testCollisionX
		
		private function testCollisionY():Boolean{	//Création de la fonction testCollisionY
			//Assurer que l'entité ne touche pas un mur.
			for(var i:uint = 0; i<terrain.murs.length; i++){
				if(hitTestObject(terrain.murs[i])){	//Si hitTestObject detect un mur, l'énoncé if effectue:
					do{	//Fait
						if(vy > 0){	//Si vy est plus que 0, retourner vers le haut:
							this.y--;	//
						}else{	//Si non, retourner vers le bas:
							this.y++;	//
						}	//Fin de l'énoncé if et else
					}while(hitTestObject(terrain.murs[i]));	//Continuer à retourner si il est encore dans le mur.
					return true;	//Rendre la valeur true
				}	//Fin de l'énoncé if
			}	//Fin de la boucle for
			return false;	//Rendre false
		}	//Fin de la fonction testCollisionY
		
	}	//Fin de la classe Ennemi

}	//Fin du package