//0.20
//ViTO Icon
//Send server, cords and mob to chat

var ModVersion:String = "0.41";

import com.GameInterface.Tooltip.TooltipData;
import com.GameInterface.Tooltip.TooltipInterface;
import com.GameInterface.Tooltip.TooltipManager;
import com.GameInterface.DistributedValue;
import com.GameInterface.Chat
import com.GameInterface.Game.Character;
import com.GameInterface.Friends;
import com.GameInterface.WaypointInterface;

import com.GameInterface.DimensionData

//import com.GameInterface.WaypointInterface;
//import com.GameInterface.Waypoint;

var FULL_STAT:Number = 2;

var m_Character:Character;

var m_Icon:MovieClip;
var m_VTIOIsLoadedMonitor:DistributedValue;

var ShoutOutMUTarget:DistributedValue;

var m_CompassCheckTimerID:Number;
var m_CompassCheckTimerLimit:Number = 256;
var m_CompassCheckTimerCount:Number = 0;

var VTIOAddonInfo:String = "ShoutOut!|Belladawna|" + ModVersion + "||_root.shoutout_shoutout.m_Icon";


m_Character = Character.GetClientCharacter();

function OnModuleActivated()
{

	//dvMUTarget = new DistributedValue("ShoutOutMUTarget")

	//DistributedValue.SetDValue("ShoutOutMUTarget","none");
	
	//dvMUTarget.SignalChanged.Connect(SlotShoutOutMUTarget, this);
	
	if (DistributedValue.GetDValue("ShoutOutMUTarget") != "none")
	{
		//com.GameInterface.UtilsBase.PrintChatText(DistributedValue.GetDValue("ShoutOutMUTarget") + " needs removed");
		Friends.RemoveFriend(DistributedValue.GetDValue("ShoutOutMUTarget"));
		DistributedValue.SetDValue("ShoutOutMUTarget","none");
	} else {
		//com.GameInterface.UtilsBase.PrintChatText("No player to remove");
	}
	

	
}

function onLoad()
{

	dvMUTarget = new DistributedValue("ShoutOutMUTarget")

	DistributedValue.SetDValue("ShoutOutMUTarget","none");
	
	dvMUTarget.SignalChanged.Connect(SlotShoutOutMUTarget, this);
	
	Friends.SignalFriendsUpdated.Connect(SlotSignalFriendsUpdated, this);
										 
	ViTOHook();

}

function PrintCallOut()
{
	
	var dim = m_Character.GetStat(_global.Enums.Stat.e_Dimension);
	//var targetName = com.GameInterface.Game.Character.GetCharacter(m_Character.GetOffensiveTarget()).GetName());
	//var playfield = GetPlayfieldShortName();
	var playfield = com.Utils.LDBFormat.LDBGetText("Playfieldnames", m_Character.GetPlayfieldID());
	var cordx = com.Utils.Format.Printf("%.0f", m_Character.GetPosition().x);
	var cordy = com.Utils.Format.Printf("%.0f", m_Character.GetPosition().z);

	//ShoutOut! -- Zone: %zonename% -- AutoMeetup: Enable -- More Info
	
	//More Info
	//Zone
	//Target Name
	//Target HP
	
	//ShoutOut Meetup Link
	
	
	TargetID = com.GameInterface.Game.Dynel.GetDynel(m_Character.GetOffensiveTarget());
	
	TargetName = TargetID.GetName();
	
	TargetHP = TargetID.GetStat(_global.Enums.Stat.e_Life, FULL_STAT)
	
	if (TargetName != undefined)
	{
	
		TargetInfo = "Name: " + TargetName + "<br>Health: " + TargetHP + "<br><br>";
	} else {
		TargetInfo = "";
	}
	
	

	
	var Players = PlayersInArea();
	
	if (Players > 5)
	{
		
		var PlayersInfo = "Players In Area: " + Players + "<br><br>";
		
	} else {
		var PlayersInfo = "";
	}
	
	if (DistributedValue.GetDValue("AcceptAllMeetUps"))
	{
		var MeetUpInfo = "AutoMU: Enabled<br><br>";
	} else {
		var MeetUpInfo = "";
	}
	
	var ModInfo = "<font face=LARGE><font face=LARGE_BOLD>ShoutOut! " + ModVersion + "</font><br><br>";

	var ZoneInfo = "Zone: " + playfield + "<br><br>";
	
	var Disclaimer = "<br><br><br><font color=#2a6bab face=LARGE_BOLD>Belladawna's</font> <font face=LARGE_BOLD color=orange>ShoutOut!</font> needed for MeetUp Link to work.  Downlaod here: http://www.guildargo.com/public-addons/ShoutOut.zip.  AutoMeetUp can be found here: http://tsw.curseforge.com/tsw-mods/acceptallmeetups/";

	var MeetUpLink = "<br><a href='chatcmd:///option ShoutOutMUTarget &quot;" + m_Character.GetName()+ "&quot;'>Click Here to MeetUp!</a>"

	var ChatPopupContnet = ModInfo + ZoneInfo + TargetInfo + PlayersInfo + MeetUpInfo + MeetUpLink + Disclaimer;

	var ChatPopup = "<a href=\"text://" + ChatPopupContnet + "\">More Info</a>";

	Chat.SetChatInput("<font color=orange>ShoutOut!</font> -- <font face=LARGE color=yellow>Zone: " + playfield + "</font> --<font face=LARGE color=green> (" + cordx + "," + cordy + ")</font> " + ChatPopup);
}

function SlotShoutOutMUTarget()
{
	
	isFriend = false;
	MUFriendID = undefined;
	
	//com.GameInterface.UtilsBase.PrintChatText("ShoutOutMUTarget Changed");
	
	//com.GameInterface.UtilsBase.PrintChatText("Current Value: " + DistributedValue.GetDValue("ShoutOutMUTarget"))
	
	//DistributedValue.SetDValue("ShoutOutMUTarget",undefined);
	
	if (DistributedValue.GetDValue("ShoutOutMUTarget") != "none")
	{
	
		for (var key in Friends.m_Friends)
		{
			if (Friends.m_Friends[key].m_Name == DistributedValue.GetDValue("ShoutOutMUTarget"))
			{
				//com.GameInterface.UtilsBase.PrintChatText(DistributedValue.GetDValue("ShoutOutMUTarget") + " is friend");
				isFriend = true;
				MUFriendID = Friends.m_Friends[key].m_FriendID
			}
			//com.GameInterface.UtilsBase.PrintChatText(Friends.m_Friends[key].m_Name);
		}
	
		//Friends.AddFriend("Taiver"); Everyone should be friends with Taiver!
	
		if (!isFriend)
		{
			//com.GameInterface.UtilsBase.PrintChatText("Adding " + DistributedValue.GetDValue("ShoutOutMUTarget"));
			Friends.AddFriend(DistributedValue.GetDValue("ShoutOutMUTarget"));
		
			/*
			if (m_MUInt = undefined)
			{
				m_MUInt = setInterval(MUNewFriend,500);
			}
			*/
		
			//MUFriendID = GetFriendID(DistributedValue.GetDValue("ShoutOutMUTarget"));
			//com.GameInterface.UtilsBase.PrintChatText("MU On: " + MUFriendID);
		} else {
			//com.GameInterface.UtilsBase.PrintChatText("Already friend");
			
			FriendMUID = GetFriendID(DistributedValue.GetDValue("ShoutOutMUTarget"));
			//com.GameInterface.UtilsBase.PrintChatText("Slot MU On: " + FriendMUID);
			
			DistributedValue.SetDValue("ShoutOutMUTarget","none");

			Friends.MeetUp(FriendMUID);

			//MeetUp and reset DV
		}
		
	}
	
}

function SlotSignalFriendsUpdated()
{
	
	//com.GameInterface.UtilsBase.PrintChatText("Friend Added");
	FriendMUID = GetFriendID(DistributedValue.GetDValue("ShoutOutMUTarget"));
	//com.GameInterface.UtilsBase.PrintChatText("Slot MU On: " + FriendMUID);
	Friends.MeetUp(FriendMUID);
	
}

function PlayersInArea()
{
	
	var NonTeamArea:Number = 0;
	
	for(var i in _root.nametagcontroller.m_NametagArray) 
	{
		char = _root.nametagcontroller.m_NametagArray[i].m_Character;
		switch(char.GetNametagCategory()) 
		{
			case _global.Enums.NametagCategory.e_NameTagCategory_Raid:
			case _global.Enums.NametagCategory.e_NameTagCategory_Team:
				TeamArea++;
				break;
			case _global.Enums.NametagCategory.e_NameTagCategory_FriendlyPlayer:
				NonTeamArea++;
		}
	}
	
	return NonTeamArea;
	
	
}

function GetFriendID(FriendName:String)
{
	
	//com.GameInterface.UtilsBase.PrintChatText("Getting ID for: " + FriendName);
	
	for (var key in Friends.m_Friends)
	{
		if (Friends.m_Friends[key].m_Name == FriendName)
		{
			//com.GameInterface.UtilsBase.PrintChatText("GetFriendID Found Friend");
			//com.GameInterface.UtilsBase.PrintChatText("m_FriendID: " + Friends.m_Friends[key].m_FriendID);
			ID = Friends.m_Friends[key].m_FriendID;
			return ID;
		}
		//com.GameInterface.UtilsBase.PrintChatText(Friends.m_Friends[key].m_Name);
	}
	
}

function SlotPlayfieldChanged(newPlayfield:Number):Void
{
	
	
}

function DumpStats()
{
	
	com.GameInterface.UtilsBase.PrintChatText("Begin");
	
	var PlayersTest = PlayersInArea();
	
	com.GameInterface.UtilsBase.PrintChatText("Players In Area: " + PlayersTest);
	
	if (PlayersTest < 3)
	{
		com.GameInterface.UtilsBase.PrintChatText("Less then 3 players in area");
	} else {
		com.GameInterface.UtilsBase.PrintChatText("More then 3 players in area");
	}
	
	//GetFriendID("Taiver");
	
	/*
	
	for (var key in Friends.m_Friends)
	{
		if (Friends.m_Friends[key].m_Name == "Taiver")
		{
			ID = Friends.m_Friends[key].m_FriendID;
		}
		//com.GameInterface.UtilsBase.PrintChatText(Friends.m_Friends[key].m_Name);
	}
	*/
	
	
	//com.GameInterface.UtilsBase.PrintChatText("MUFriendID = " + ID);
	
	//var isFriend = false;
	
	/*
	for (var i = 0; i < 5000000; i++)
	{
		if (m_Character.GetStat(i) == 49)
		{
			com.GameInterface.UtilsBase.PrintChatText(i + " - " + m_Character.GetStat(i));
		}
	}
	*/
	
	/*
	for (var prop in com.GameInterface.DimensionData)
	{
		com.GameInterface.UtilsBase.PrintChatText(prop + " - " + m_Character[prop]);
	}
	*/
	
	/*
	for (var key in Friends.m_Friends)
	{
		for (prop in Friends.m_Friends[key])
		{
			com.GameInterface.UtilsBase.PrintChatText(prop + " - " + Friends.m_Friends[key][prop]);
		}
		
		//com.GameInterface.UtilsBase.PrintChatText(Friends.m_Friends[key].m_Name);
	}
	*/
	
	//Friends.AddFriend("Taiver");
	
	
	/*
	if (!isFriend)
	{
		com.GameInterface.UtilsBase.PrintChatText("Adding Taiver");
		Friends.AddFriend("Taiver");
	}
	*/
	com.GameInterface.UtilsBase.PrintChatText("Finish");
}


function GetPlayfieldShortName()
{
	
/*
MAPS
Kingsmouth Town = 3030
The Savage Coast = 3040
The Blue Mountain = 3050
The Scorched Desert = 3090
City Of The Sun God = 3100
The Besieged Farmlands = 3120
The Shadowy Forest = 3130
The Carpathian Fangs = 3140
*/
	
	switch(_root.waypoints.m_PlayfieldID)
	{
		case 3030: //Kingsmouth Town
			return "KM";
			break;
		case 3040: //The Savage Coast
			return "SC";
			break;
		case 3050: //The Blue Mountain
			return "BM";
			break;
		case 3090: //The Scorched Desert
			return "SD";
			break;
		case 3100: //City Of The Sun God
			return "CoTSG";
			break;
		case 3120: //The Besieged Farmlands
			return "BM";
			break;
		case 3130: //The Shadowy Forest
			return "SF";
			break;
		case 3140: //The Carpathian Fangs
			return "CF";
			break;
		case 1100: //NY
			return "NY";
			break;
		default:
			return "";
			break;
	}
	
}

function ViTOHook()
{
	
	
	///////////////////////////////////////////
	////Crap for Viper's Bar
	///////////////////////////////////////////
	
	
	//Crap for Viper's Bar
	
	// Setting up the VTIO loaded monitor.
	m_VTIOIsLoadedMonitor = DistributedValue.Create("VTIO_IsLoaded");
	m_VTIOIsLoadedMonitor.SignalChanged.Connect(SlotCheckVTIOIsLoaded, this);
	
	
	// Setting up the monitor for your option window state.
	//m_OptionWindowState = DistributedValue.Create("AEGISHelper_OptionWindowOpen");
	//m_OptionWindowState.SignalChanged.Connect(SlotOptionWindowState, this);
	
	// Make sure the game doesn't think the window is open if the game was reloaded with it open. Can also be placed in OnModuleDeactivated() if that's used.
	//DistributedValue.SetDValue("AEGISHelper_OptionWindowOpen", false);

	// Setting up your icon.
	m_Icon = attachMovie("Icon", "m_Icon", getNextHighestDepth());
	m_Icon._width = 18;
	m_Icon._height = 18;
	m_Icon.onMousePress = function(buttonID) {
		if (buttonID == 1) {
			//Left Button Stuff
			PrintCallOut();
		} else if (buttonID == 2) {
			//DumpStats();
			// Do right mouse button stuff..
		}
	}

	m_Icon.onRollOver = function() {
		if (m_Tooltip != undefined) m_Tooltip.Close();
        var tooltipData:TooltipData = new TooltipData();
		tooltipData.AddAttribute("", "<font face='_StandardFont' size='13' color='#FF8000'><b>ShoutOut! " + ModVersion + " by Belladawna</b></font>");
        tooltipData.AddAttributeSplitter();
        tooltipData.AddAttribute("", "");
        tooltipData.AddAttribute("", "<font face='_StandardFont' size='12' color='#FFFFFF'>Left click to put announcement in chat</font>");
        tooltipData.m_Padding = 4;
        tooltipData.m_MaxWidth = 210;
		m_Tooltip = TooltipManager.GetInstance().ShowTooltip(undefined, TooltipInterface.e_OrientationVertical, 0, tooltipData);
	}
	m_Icon.onRollOut = function() {
		if (m_Tooltip != undefined)	m_Tooltip.Close();
	}

	// Start the compass check.
	m_CompassCheckTimerID = setInterval(PositionIcon, 100);
	PositionIcon();

	// Check if VTIO is loaded (if it loaded before this add-on was).
	SlotCheckVTIOIsLoaded();
	
	
	//////////////////////////////////////////////////
	//////End Crap for Viper's Bar
	//////////////////////////////////////////////////


	
}

///////////////////////////
//Functions for Viper's Bar
///////////////////////////


// The compass check function.
function PositionIcon() {
	m_CompassCheckTimerCount++;
	if (m_CompassCheckTimerCount > m_CompassCheckTimerLimit) clearInterval(m_CompassCheckTimerID);
	if (_root.compass._x > 0) {
		clearInterval(m_CompassCheckTimerID);
		m_Icon._x = _root.compass._x - 154;
		m_Icon._y = _root.compass._y + 0;
	}
}

// The function that checks if VTIO is actually loaded and if it is sends the add-on information defined earlier.
// This function will also get called if VTIO loads after your add-on. Make sure not to remove the check for seeing if the value is actually true.
function SlotCheckVTIOIsLoaded() {
	if (DistributedValue.GetDValue("VTIO_IsLoaded")) DistributedValue.SetDValue("VTIO_RegisterAddon", VTIOAddonInfo);
}