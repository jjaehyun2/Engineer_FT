stop();

//--------------------------------------
// BASIC IMPORTS REQUIRED 
//--------------------------------------
import fl.transitions.*;
import fl.transitions.easing.*;

import classes.scrollingpanel.events.NpScrollingPanelEvent;
import classes.scrollingpanel.ui.NpScrollingPanel;

//helper class for loading XML
import classes.net.LoadXml;

//tweenMax imports
import gs.*;
import gs.easing.*;




//--------------------------------------
// STREAM BACKGROUND MUSIC
//--------------------------------------

import flash.media.Sound;
import flash.media.SoundLoaderContext;
import flash.net.URLRequest;

var s:Sound = new Sound();
var req:URLRequest = new URLRequest("sound/bg_music.mp3");
var context:SoundLoaderContext = new SoundLoaderContext(8000, true);
s.load(req, context);
s.play();

var soundCHNL:SoundChannel = new SoundChannel(); 
soundCHNL = s.play(); 
 
var soundTrans:SoundTransform = new SoundTransform(); 
 
soundTrans.volume = .5; 
soundCHNL.soundTransform = soundTrans;




//--------------------------------------
//INIT VARIABLES
//--------------------------------------

var myLoader:Loader = new Loader();
var myLoader2:Loader = new Loader();

var myTransitionManagerThumbs:TransitionManager = new TransitionManager(thumbsContainer_mc);
var myTransitionManagerArrows:TransitionManager = new TransitionManager(arrows_mc);
var myTransitionManagerBottom:TransitionManager = new TransitionManager(fotoInferior_mc);
var myTransitionManagerTop:TransitionManager = new TransitionManager(fotoSuperior_mc);
var myTransitionManagerNew:TransitionManager = new TransitionManager(fotoSuperior_mc);

var _gallery:String;
var flag:Number = 0;

//INITIALIZE COUNTER AND TOTAL PHOTOS
var _bottomPhoto:Number;
var _totalPhotos:Number; 
var _background:Number = 1;

homeFullscreen_mc.buttonMode = true;
arrows_mc.visible = false;
backButton_btn.visible = false;
navigationBar_mc.visible = false;
footer_mc.visible = false;
title_mc.visible = false;
Title_Home_mc.visible = false;
form_mc.visible = false;
contactForm_mc.visible = false;
esc_mc.visible = false;	
formBackground_mc.visible = false;	
thumbsContainer_mc.visible = false;
preloaderContainer_mc.visible = false;
instructions_mc.visible = false;

var toggleThumbs:Boolean = false;  
var _intructions:Boolean = false;
	
	
	
//--------------------------------------
// SET STAGE
//--------------------------------------
stage.align = StageAlign.TOP_LEFT;
stage.scaleMode = StageScaleMode.NO_SCALE;




//--------------------------------------
// SETUP THE HORIZONTAL SCROLLER
//--------------------------------------

var thumbsContainer:NpScrollingPanel = new NpScrollingPanel("horizontal");
thumbsContainer.y = 25;
thumbsContainer.x = 25;

thumbsContainer.mouseScrolling = true;
thumbsContainer.panelEdgeScrolling = false;
thumbsContainer.panelScrollBlur = false;
thumbsContainer.scrollSpeed = 30;

thumbsContainer.resizePanelMaskToStage = false;
thumbsContainer.panelMaskWidth = 550;
thumbsContainer.panelMaskHeight = 150;
thumbsContainer.panelReflection = false;
thumbsContainer.contentButtonMode = true;
thumbsContainer.panelBgAlpha = 0;
thumbsContainer.panelBgColour = 0x000000;
thumbsContainer.contentY_position = 0;
thumbsContainer.contentX_position = 0;
thumbsContainer.contentPadding = 10;

thumbsContainer_mc.addChild(thumbsContainer);


	

//--------------------------------------
//RE-ARRANGE ELEMENTS ON RESIZE
//--------------------------------------

stage.addEventListener( Event.RESIZE, onResize );

function onResize ( e : Event = null ) : void
{	
	
	//--------------------------------------
	//RE-SIZE BACKGROUND
	//--------------------------------------

	// set image dimensions to match stage;
	backgroundContainer_mc.width = stage.stageWidth;
	backgroundContainer_mc.height = stage.stageHeight;
		
	backgroundContainer_mc.smoothing = true;
	backgroundContainer_mc.smoothing = true;
				
	// adjust proportionally to fill stage;
	( backgroundContainer_mc.scaleX > backgroundContainer_mc.scaleY ) ? backgroundContainer_mc.scaleY = backgroundContainer_mc.scaleX : backgroundContainer_mc.scaleX = backgroundContainer_mc.scaleY;
				
	// control shrinkage;
	if ( backgroundContainer_mc == null ) if ( backgroundContainer_mc.scaleX < 1 || backgroundContainer_mc.scaleY < 1 ) backgroundContainer_mc.scaleX = backgroundContainer_mc.scaleY = 1;		
				
	// center image;
	backgroundContainer_mc.x = stage.stageWidth * .5 - backgroundContainer_mc.width * .5;
	backgroundContainer_mc.y = stage.stageHeight * .5 - backgroundContainer_mc.height * .5;
					
	
	//--------------------------------------
	//RE-SIZE TOP PHOTO
	//--------------------------------------
	
	// set image dimensions to match stage;
	fotoSuperior_mc.width = stage.stageWidth;
	fotoSuperior_mc.height = stage.stageHeight;
		
	fotoSuperior_mc.smoothing = true;
	fotoSuperior_mc.smoothing = true;
				
	// adjust proportionally to fill stage;
	( fotoSuperior_mc.scaleX > fotoSuperior_mc.scaleY ) ? fotoSuperior_mc.scaleY = fotoSuperior_mc.scaleX : fotoSuperior_mc.scaleX = fotoSuperior_mc.scaleY;
				
	// control shrinkage;
	if ( fotoSuperior_mc == null ) if ( fotoSuperior_mc.scaleX < 1 || fotoSuperior_mc.scaleY < 1 ) fotoSuperior_mc.scaleX = fotoSuperior_mc.scaleY = 1;		
				
	// center image;
	fotoSuperior_mc.x = stage.stageWidth * .5 - fotoSuperior_mc.width * .5;
	fotoSuperior_mc.y = stage.stageHeight * .5 - fotoSuperior_mc.height * .5;
	
	
	//--------------------------------------
	//RE-SIZE BOTTOM PHOTO
	//--------------------------------------
	
	// set image dimensions to match stage;
	fotoInferior_mc.width = stage.stageWidth;
	fotoInferior_mc.height = stage.stageHeight;
		
	fotoInferior_mc.smoothing = true;
	fotoInferior_mc.smoothing = true;
				
	// adjust proportionally to fill stage;
	( fotoInferior_mc.scaleX > fotoInferior_mc.scaleY ) ? fotoInferior_mc.scaleY = fotoInferior_mc.scaleX : fotoInferior_mc.scaleX = fotoInferior_mc.scaleY;
				
	// control shrinkage;
	if ( fotoInferior_mc == null ) if ( fotoInferior_mc.scaleX < 1 || fotoInferior_mc.scaleY < 1 ) fotoInferior_mc.scaleX = fotoInferior_mc.scaleY = 1;		
				
	// center image;
	fotoInferior_mc.x = stage.stageWidth * .5 - fotoInferior_mc.width * .5;
	fotoInferior_mc.y = stage.stageHeight * .5 - fotoInferior_mc.height * .5;
		
		
	//--------------------------------------
	//SET ELEMENTS TO STAGE
	//--------------------------------------
	
	arrows_mc.next_btn.x = stage.stageWidth - 72;
	arrows_mc.y = (stage.stageHeight * 0.5);
	
	
	thumbsContainer_mc.y = stage.stageHeight - 185;
	
	backButton_btn.x = stage.stageWidth - 52;
	backButton_btn.y = 74;
	
	navigationBar_mc.background_mc.width = stage.stageWidth;   
	navigationBar_mc.y = stage.stageHeight - 60;
	
	footer_mc.y = stage.stageHeight - 60;
	
	form_mc.x = (stage.stageWidth/2) - 175;
	form_mc.y = (stage.stageHeight/2) - 75;
	
	contactForm_mc.x = (stage.stageWidth/2) - 182;
	contactForm_mc.y = (stage.stageHeight/2) - 125;
	
	instructions_mc.x = (stage.stageWidth/2) - 182;
	instructions_mc.y = (stage.stageHeight/2) - 125;
	
	esc_mc.width = stage.stageWidth;
	esc_mc.height = stage.stageHeight;
	
	formBackground_mc.width = stage.stageWidth;
	formBackground_mc.height = stage.stageHeight;
	
	preloaderContainer_mc.x = (stage.stageWidth/2) - 34;
	preloaderContainer_mc.y = (stage.stageHeight/2) - 12;
	
	if(stage.stageWidth > 1280)
	{
		
		footer_mc.scaleX = 1.3;
		footer_mc.scaleY = 1.3;
		
		navigationBar_mc.scaleX = 1.3;
		navigationBar_mc.scaleY = 1.3;
	
		footer_mc.x = stage.stageWidth - 424;
		
	}else{
		
		footer_mc.scaleX = 1;
		footer_mc.scaleY = 1;
		
		navigationBar_mc.scaleX = 1;
		navigationBar_mc.scaleY = 1;
	
		footer_mc.x = stage.stageWidth - 340;
		
	}
	
}





//--------------------------------------
//LOAD BACKGROUND
//--------------------------------------

var myBackgroundLoder:Loader = new Loader();

myBackgroundLoder.load(new URLRequest("images/background/bg"+_background+".jpg"));
myBackgroundLoder.contentLoaderInfo.addEventListener(Event.COMPLETE, addBackgroundToStage);
backgroundContainer_mc.addChild(myBackgroundLoder);


//SHOW PRELOADER
Mouse.hide();
preloader_mc.startDrag(true);
preloader_mc.visible = true;
		

function addBackgroundToStage(event:Event)
{
	
	myBackgroundLoder.contentLoaderInfo.removeEventListener(Event.COMPLETE, addBackgroundToStage);
	onResize();
	
	//REMOVE PRELOADER
	Mouse.show();
	preloader_mc.stopDrag();
	preloader_mc.visible = false;
	
	backgroundContainer_mc.alpha = 0;
	TweenMax.to(backgroundContainer_mc, 3, {alpha:1, ease:Quart.easeIn, onComplete:goHome});

	function goHome():void
	{		
	
		gotoAndStop("HOME");
		
	}
	
}





//--------------------------------------
//TOGGLE FULLSCREEN
//--------------------------------------

footer_mc.fullscreenButton_mc.buttonMode = true;
footer_mc.fullscreenButton_mc.addEventListener(MouseEvent.CLICK,toggleFullScreen);
                
        
    function toggleFullScreen(event:MouseEvent):void
	{
            switch(stage.displayState) 
			{
                case "normal":
                    stage.displayState = "fullScreen";    
                    break;
                case "fullScreen":
                default:
                    stage.displayState = "normal";    
                    break;
            }
    }    
	






//--------------------------------------
//NAVIGATION ACCORDIAN
//--------------------------------------

//import tweenlite classes
import gs.TweenLite;
import gs.easing.*;




////////////////////////////
//LISTENERS

navigationBar_mc.blackAndWhite_mc.buttonMode = true;
navigationBar_mc.blackAndWhite_mc.addEventListener(MouseEvent.MOUSE_OVER, prepareMove);
navigationBar_mc.blackAndWhite_mc.addEventListener(MouseEvent.MOUSE_OUT, prepareMoveBack);

navigationBar_mc.nature_mc.buttonMode = true;
navigationBar_mc.nature_mc.addEventListener(MouseEvent.MOUSE_OVER, prepareMove);
navigationBar_mc.nature_mc.addEventListener(MouseEvent.MOUSE_OUT, prepareMoveBack);

navigationBar_mc.fashion_mc.buttonMode = true;
navigationBar_mc.fashion_mc.addEventListener(MouseEvent.MOUSE_OVER, prepareMove);
navigationBar_mc.fashion_mc.addEventListener(MouseEvent.MOUSE_OUT, prepareMoveBack);

navigationBar_mc.nudes_mc.buttonMode = true;
navigationBar_mc.nudes_mc.addEventListener(MouseEvent.MOUSE_OVER, prepareMove);
navigationBar_mc.nudes_mc.addEventListener(MouseEvent.MOUSE_OUT, prepareMoveBack);

navigationBar_mc.contact_mc.flickr_mc.buttonMode = true;
navigationBar_mc.contact_mc.contact.buttonMode = true;



///////////////////////////
//FUNCTIONS


function prepareMove(evt:MouseEvent):void 
{
	
	var targetName:String = evt.currentTarget.name.toString(); //get the menuItem 
	var directionMove:String = "forward";
	moveItem(targetName, directionMove); 
	
}




function prepareMoveBack(evt:MouseEvent):void 
{
	
	var targetName:String = evt.currentTarget.name.toString(); //get the menuItem 
	var directionMove:String = "back";
	moveItem(targetName, directionMove); 

}


//////////////////////////////////////
//NAVIGATION MENU ANIMATION FUNCTION

function moveItem(target:String, directionM:String):void 
{
	
	if(directionM == "forward")
	{
		
		//Move the linkbuttons according to button pressed
		
		switch (target) 
		{
		
			case "blackAndWhite_mc" : TweenLite.to(navigationBar_mc.nature_mc, 1, {x:445, ease:Quart.easeOut});
								      TweenLite.to(navigationBar_mc.fashion_mc, 1, {x:571, ease:Quart.easeOut});
									  TweenLite.to(navigationBar_mc.nudes_mc, 1, {x:696, ease:Quart.easeOut});
									  TweenLite.to(navigationBar_mc.contact_mc, 1, {x:821, ease:Quart.easeOut});
								      break;

								
			case "nature_mc" : TweenLite.to(navigationBar_mc.fashion_mc, 1, {x:571, ease:Quart.easeOut});
							   TweenLite.to(navigationBar_mc.nudes_mc, 1, {x:696, ease:Quart.easeOut});
							   TweenLite.to(navigationBar_mc.contact_mc, 1, {x:821, ease:Quart.easeOut});
							   break;
							   
			case "fashion_mc" : TweenLite.to(navigationBar_mc.nudes_mc, 1, {x:595, ease:Quart.easeOut});
								TweenLite.to(navigationBar_mc.contact_mc, 1, {x:720, ease:Quart.easeOut});
							    break;
								
			case "nudes_mc" : TweenLite.to(navigationBar_mc.contact_mc, 1, {x:720, ease:Quart.easeOut});
							  break;
								
		
		
		}

		
	}else{
		
		//Declare all the buttons original X position
		
		TweenLite.to(navigationBar_mc.nature_mc, 1, {x:146, ease:Quart.easeOut});
		TweenLite.to(navigationBar_mc.fashion_mc, 1, {x:271, ease:Quart.easeOut});
		TweenLite.to(navigationBar_mc.nudes_mc, 1, {x:396, ease:Quart.easeOut});
		TweenLite.to(navigationBar_mc.contact_mc, 1, {x:521, ease:Quart.easeOut});
		
	}
	
}



//--------------------------------------
//CUSTOM RIGHT CLICK MENU
//--------------------------------------


//Create an instance of ContextMenu
var myMenu:ContextMenu = new ContextMenu();

//Hide the default items
myMenu.hideBuiltInItems();

//Create your custom items as a ContextMenuItem
var menuItem1:ContextMenuItem = new ContextMenuItem("All photographs ©2012 - Federico Venturino");
menuItem1.enabled = false; 


//Add an event to a custom item
var menuItem2:ContextMenuItem = new ContextMenuItem("Visit my Flickr stream");
menuItem2.separatorBefore = true;
menuItem2.addEventListener(ContextMenuEvent.MENU_ITEM_SELECT, callFlickrFromMenu);

//Add an event to a custom item
var menuItem3:ContextMenuItem = new ContextMenuItem("Toggle Fullscreen");
menuItem3.separatorBefore = true;
menuItem3.addEventListener(ContextMenuEvent.MENU_ITEM_SELECT, toggleFullScreenFromMenu);

//Add custom items to "myMenu"
myMenu.customItems.push(menuItem1, menuItem2, menuItem3);
this.contextMenu = myMenu;


function callFlickrFromMenu(e:ContextMenuEvent):void {
	var url:String = "http://www.flickr.com/photos/fed_v/";
	var request:URLRequest = new URLRequest(url);
	navigateToURL(request, '_blank')
}

 function toggleFullScreenFromMenu(e:ContextMenuEvent):void
	{
            switch(stage.displayState) 
			{
                case "normal":
                    stage.displayState = "fullScreen";    
                    break;
                case "fullScreen":
                default:
                    stage.displayState = "normal";    
                    break;
            }
    }