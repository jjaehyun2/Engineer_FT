/*Author: Akram Taghavi-Burris
  Project: If-Else
  Created: March 1, 2013
  Updated: March 4, 2013 */

package 
{

  import flash.display.MovieClip;
	import flash.events.*;
	import flash.display.SimpleButton;

	public class MyGame extends MovieClip
	{

		/*  ======== Declaring Variables ========== */
		public var sweetie_mc:mc_sweetie = new mc_sweetie(); //new sweetie instance
		public var tiffany_mc:mc_tiffany = new mc_tiffany(); //new tiffany instance

		public var player1_btn:btn_player1 = new btn_player1(); //new player 1 button
		public var player2_btn:btn_player2 = new btn_player2(); //new player 2 button

		public var playerName:MovieClip;
		/*this variable allows us to set the name of the player, which depending on what character we choose 
		the move button will control that character */



		public function MyGame()
		{
			// constructor code

			/*  ======== Placing the Player Buttons ==========
			add instance (addChild) to stage without calling a function*/

			addChild(player1_btn);
			player1_btn.x = player1_btn.width / 2 + 100;
			/*because the object's center point it in the center the width is divided by 2 to 
			  obtain the other left edege. Then we add 100px to place it on the stage at 230*/
			player1_btn.y = 120;
			player1_btn.name = "player1_btn";


			addChild(player2_btn);
			player2_btn.x = player1_btn.width / 2 + 550;
			/*because the object's center point it in the center the width is divided by 2 to 
			  obtain the other left edege. Then we add 550px to place it on the stage at 680 */
			player2_btn.y = 120;
			player2_btn.name = "player2_btn";



			/*  ======== EVENT Listeners ========== */
			player1_btn.addEventListener(MouseEvent.CLICK,addPlayer);
			/*listens for a mouse click, then will run the function named addPlayer1*/
			player2_btn.addEventListener(MouseEvent.CLICK,addPlayer);
			/*listens for a mouse click, then will run the function named addPlayer2*/

		}//end constructor code


		/*  ======== other Functions ========== */

		/*Modular Function*/
		public function addChar(char:MovieClip,Xpos:Number,Ypos:Number):void
		{/*This modular function requires a value for the character (movieclip) and x and y 
			locations in order to run. By adding parameters (variables) into the function we can
			ruse the same function multiple times for different values.*/
			addChild(char);
			char.x = Xpos;
			char.y = Ypos;
		}//end addChar


		public function addBtn(btn:SimpleButton,Xpos:Number,Ypos:Number):void
		{/*This modular function requires a value for the character (movieclip) and x and y 
			locations in order to run. By adding parameters (variables) into the function we can
			ruse the same function multiple times for different values.*/

			addChild(btn);
			btn.x = Xpos;
			btn.y = Ypos;
		}//end addBtn()


		/*  Add Player functions */

		public function addPlayer(e:MouseEvent):void
		{

			var btnName = e.target.name;

			player1_btn.removeEventListener(MouseEvent.CLICK,addPlayer); /*removes the listener so another player can not be added*/
			player2_btn.removeEventListener(MouseEvent.CLICK,addPlayer); /*removes the listener so another player can not be added*/

			removeChild(player1_btn);
			removeChild(player2_btn);

			/* Check this condition, to add player */

			if ((btnName == "player1_btn"))
			{

				playerName = sweetie_mc; /*sets the variable for the playerName*/
				addChar(playerName,100,200); /*runs the addObj function */

			}
			else
			{
				playerName = tiffany_mc; /*sets the variable for the playerName*/
				addChar(playerName,100,200); /*runs the addObj function */
			}//end if-else


		}//end addPlayer()



	}//end class

}//end package