// ActionScript file

package{
	
	/***************
	 * AllSettings contains all possible hardcoded settings for the game including all the levels. 
	 * It will store all initial settings for the game, levels, avatar, player etc.
	 * There should not be any hardcoded values anywhere in the source code except for here. 
	 * This should be tight with VillageModel
	 * Making this a singleton so I can do some stuff that apparently requires instantiation. 	
	 * @author Darian Hickman
	 * 
	 */
	
	public class AllSettings {
		public static var 	 settings:AllSettings;	
		public static const  GOATINT:Number   = 1;
		public static const  PUMPINT:Number   = 3;
		public static const  POTATOINT:Number = 2;
		public static const  DRIPINT:Number   = 4;	
		
		public static const stagewidth:Number 	= 750;
		public static const stageheight:Number	= 550;
		
		public static const EVENT_SCORE:String = "send score";
		public static const EVENT_XP_POINTS:String = "send xp points";
		public static const EVENT_GAMEEND:String = "send end";
		public static const EVENT_WIN:String = "win";
		public static const EVENT_COINS:String = "send coins";
		public static const EVENT_CASH:String = "send cash";
		public static const EVENT_OVER:String = "game over";
		public static const EVENT_INPOSITION:String = "in position";
		public static const EVENT_ARRIVED:String = "arrived";
		public static const EVENT_CURRENTFARMER:String = "current farmer";
		public static const EVENT_PLACEORDER:String = "place order";
		public static const EVENT_AT_TABLE:String = "at table";
		public static const EVENT_ORDERTAKEN:String = "order taken";
		public static const EVENT_RETRACTORDER:String = "retract order";
		public static const EVENT_LEFT_GAME:String = "left game";
		public static const EVENT_FLOAT_MESSAGE:String = "float message";
		public static const EVENT_MAKE_ANGRY:String = "angry";
		public static const EVENT_ON_PLOT_START:String = "on plot start";
		public static const EVENT_ON_LEAVE_HAPPY:String = "on leave happy";
		public static const EVENT_ON_LEAVE_ANGRY:String = "on leave angry";
		public static const EVENT_CHECK_MOVEMENT_SEQUENCER:String = "check movement sequencer";
		public static const EVENT_ORDER_COMPLETED:String = "order completed";
		public static const EVENT_AT_TRASH:String = "at trash";
		public static const EVENT_TIMEOUT:String = "event_timeout_hud"
		public static const EVENT_MUTE:String = "event_mute"
		public static const EVENT_ON_CHAR_CREATE:String = "event_character_create";
		public static const EVENT_CALL_VISITOR:String = "call visitor";
		public static const EVENT_CALL_PLAYER:String = "call player";
		
		public static const EVENT_WINDOW:String = "dispatch window event";
		public static const EVENT_WINDOWCLOSED:String = "window closed";
		public static const EVENT_CHANGE_AVATAR:String = "change avatar";
		
		public static const current_level:uint = 1;
		public static const levels:Array = [];  			// array containing all default setting at levels[0] and specific settings
															// making levels a constant because this is the only place to define levels
	
		
		public function AllSettings(pvt:PrivateClass):void{
		    if(!settings){
				settings = this;
			}else{
				throw new Error("AllSettings is a singleton");
			}
			levels[0] = new Level();
			levels[0].current_level = 0;
			levels[0].num_villagers = 5;
			levels[0].start_score  = 0;
			levels[0].innovation_name = "";
			levels[0].innovation_desc = "";
			levels[0].innovation_img = "";
			levels[0].inventory = "Goat";
			levels[0].start_time = "11:11:11";
			levels[0].win_condition = 111;
			levels[0].plot_positions = 							 // grid coords of each farmer plot
				[[8, 4], [16, 5], [3, 12], [16, 14], [16, 23]];
			levels[0].farmer_positions = 
				[[10,21], [24,22],[24,19],[24,16],[24,13],[24,10]]; // starting positions of all farmers
			levels[0].player_position = [10,21];
			levels[0].production_speed = 2;
			levels[0].avatar_speed = 2;
			levels[0].final_win_message = null;  //final_win_message should only be defined in last level. 
			levels[0].cashhash = { };			//array of cash of awarded for each event; could be negative like onLeaveAngry
			
			levels[0].cashhash[EVENT_SCORE] = 10;
			levels[0].cashhash[EVENT_INPOSITION] = 13;
			levels[0].cashhash[EVENT_ARRIVED] = 15;
			levels[0].cashhash[EVENT_CURRENTFARMER] = 1;
			levels[0].cashhash[EVENT_PLACEORDER] = 5;
			levels[0].cashhash[EVENT_AT_TABLE] = 1
			levels[0].cashhash[EVENT_ORDERTAKEN] = 5;
			levels[0].cashhash[EVENT_RETRACTORDER] = 1;
			levels[0].cashhash[EVENT_LEFT_GAME] = 1;
			levels[0].cashhash[EVENT_FLOAT_MESSAGE] = 1;
			levels[0].cashhash[EVENT_MAKE_ANGRY] = 5;
			levels[0].cashhash[EVENT_ON_PLOT_START] = 50;
			levels[0].cashhash[EVENT_ON_LEAVE_HAPPY] = 1;
			levels[0].cashhash[EVENT_ON_LEAVE_ANGRY] = 1;
			levels[0].cashhash[EVENT_CHECK_MOVEMENT_SEQUENCER] = 1;
			levels[0].cashhash[EVENT_ORDER_COMPLETED] = 60;
			
			
			levels[0].event_delays = { } ;//feed these values to timers 
			levels[0].event_delays[EVENT_SCORE] 				= 8;
			levels[0].event_delays[EVENT_XP_POINTS]				= 8;
			levels[0].event_delays[EVENT_GAMEEND] 				= 8;
			levels[0].event_delays[EVENT_WIN] 					= 8;
			levels[0].event_delays[EVENT_COINS] 				= 8;
			levels[0].event_delays[EVENT_CASH] 					= 8;
			levels[0].event_delays[EVENT_INPOSITION] 			= 5;
			levels[0].event_delays[EVENT_ARRIVED] 				= 40;
			levels[0].event_delays[EVENT_CURRENTFARMER] 		= 8;
			levels[0].event_delays[EVENT_PLACEORDER] 			= 8;
			levels[0].event_delays[EVENT_AT_TABLE] 				= 8;
			levels[0].event_delays[EVENT_ORDERTAKEN] 			= 8;
			levels[0].event_delays[EVENT_RETRACTORDER] 			= 15;
			levels[0].event_delays[EVENT_LEFT_GAME] 			= 8;
			levels[0].event_delays[EVENT_FLOAT_MESSAGE] 		= 8;
			levels[0].event_delays[EVENT_MAKE_ANGRY] 			= 10;
			levels[0].event_delays[EVENT_ON_PLOT_START] 		= 8;
			levels[0].event_delays[EVENT_ON_LEAVE_HAPPY] 		= 8;
			levels[0].event_delays[EVENT_ON_LEAVE_ANGRY] 		= 8;
			levels[0].event_delays[EVENT_CHECK_MOVEMENT_SEQUENCER] = 8;
			levels[0].event_delays[EVENT_ORDER_COMPLETED] 		= 8;
			levels[0].event_delays[EVENT_ON_CHAR_CREATE] 		= 1;
			
			levels[0].tutorial = { };
			
			// create values for level 1
			levels[1] = Level.cloneLevel(levels[0]);
			//levels[1] = new Level();
			levels[1].current_level = 1;
			levels[1].win_condition = 100;
			levels[1].innovation_name= "Goat";
			levels[1].innovation_desc= "Goats produce milk, meat, and more income for farmers";
			levels[1].innovation_img="Goat";
			levels[1].inventory = "Goat";
			levels[1].num_villagers = 1;
			levels[1].start_time = "01:10:00";
			levels[1].event_delays[EVENT_SCORE] 				= 2;
			levels[1].event_delays[EVENT_XP_POINTS]				= 3;
			levels[1].event_delays[EVENT_GAMEEND] 				= 4;
			levels[1].event_delays[EVENT_WIN] 					= 5;
			levels[1].event_delays[EVENT_COINS] 				= 6;
			levels[1].event_delays[EVENT_CASH] 					= 7;
			levels[1].event_delays[EVENT_INPOSITION] 			= 8;
			levels[1].event_delays[EVENT_ARRIVED] 				= 9;
			levels[1].event_delays[EVENT_CURRENTFARMER] 		= 10;
			levels[1].event_delays[EVENT_PLACEORDER] 			= 11;
			levels[1].event_delays[EVENT_AT_TABLE] 				= 12;
			levels[1].event_delays[EVENT_ORDERTAKEN] 			= 13;
			levels[1].event_delays[EVENT_RETRACTORDER] 			= 14;
			levels[1].event_delays[EVENT_LEFT_GAME] 			= 15;
			levels[1].event_delays[EVENT_FLOAT_MESSAGE] 		= 16;
			levels[1].event_delays[EVENT_MAKE_ANGRY] 			= 7;
			levels[1].event_delays[EVENT_ON_PLOT_START] 		= 18;
			levels[1].event_delays[EVENT_ON_LEAVE_HAPPY] 		= 19;
			levels[1].event_delays[EVENT_ON_LEAVE_ANGRY] 		= 20;
			levels[1].event_delays[EVENT_CHECK_MOVEMENT_SEQUENCER] = 8;
			levels[1].event_delays[EVENT_ORDER_COMPLETED] 		= 8;
			levels[1].event_delays[EVENT_ON_CHAR_CREATE] 		= 1;
			
			levels[1].tutorial[EVENT_ARRIVED] = "Click on the farmer and then click on the plot they should farm.";
			levels[1].tutorial[EVENT_PLACEORDER] = "Click on the farmer to get their order.";
			levels[1].tutorial[EVENT_ORDERTAKEN] = "When the order arrives by truck click it to pick it up and click the farmer to take to him";
			
			// create values for level 2
			levels[2] = Level.cloneLevel(levels[0]);
			levels[2].current_level = 2;

			levels[2].win_condition = 200;
			levels[2].inventory = "Goat, Water Pump";
			levels[2].num_villagers = 5;
			levels[2].start_time = "02:20:00";
			levels[2].innovation_name="Water Pump";
			levels[2].innovation_desc="Farmers use this to grow 10 times more food.";
			levels[2].innovation_img="WaterPump";
			
			// create values for level 3
			levels[3] = Level.cloneLevel(levels[0]);
			levels[3].current_level = 3;

			levels[3].win_condition = 700;
			levels[3].inventory = "Goat, Water Pump, Sweet Potato";
			levels[3].num_villagers = 7;
			levels[3].start_time = "02:20:00";
			levels[3].innovation_name="Sweet Potato";
			levels[3].innovation_desc="Sweet Potatoes withstand drought and provide abundant nutrients.";
			levels[3].innovation_img="Sweet Potato";
			
			// create values for level 2
			levels[4] = Level.cloneLevel(levels[0]);
			levels[4].current_level = 4;

			levels[4].win_condition = 500;
			levels[4].inventory = "Goat, Water Pump, Sweet Potato, Driptech";
			levels[4].num_villagers = 9;
			levels[4].start_time = "02:20:00";
			levels[4].innovation_name="Driptech";
			levels[4].innovation_desc="Driptech makes irrigation super efficient.";
			levels[4].innovation_img="DripTech";
			levels[4].final_win_message = "Congratulations!  You completed the game and discovered some powerful solutions to poverty!!";
		
		}
		
		public static function getInstance():AllSettings{
			if(settings == null){
				settings = new AllSettings(new PrivateClass());
			}
			return settings;
		}
	}
}
internal class PrivateClass{}