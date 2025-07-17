///////////////////////////////////////////////////////
//
// Menu Bar Decorator 
//
// Decorator pattern adapted to Flash to use
// an existing component instance on Stage.
//
// Permission to use this code for any military
// purpose is expressly denied. In all other instances
// you agree that you use this code at your own risk
// without any implied warranty.
//
// Copyright © 2003, Aral Balkan. All Rights Reserved.
// http://www.BitsAndPixels.co.uk
//
///////////////////////////////////////////////////////

import mx.controls.Menu;
import mx.controls.MenuBar;
import menuStructureXML;

class MenuBarDecorator 
{

	var menuBarRef:MenuBar;
	
	function MenuBarDecorator ( menuBarRef:MenuBar )
	{
		this.menuBarRef = menuBarRef;
	}
	
	function loadMenuStructure ( xmlFileURL:String, timeline ) 
	{
		var menuStructure:MenuStructureXML = new MenuStructureXML();
	
		menuStructure.ignoreWhite = true;
		
		// save the arguments
		menuStructure.menuBarRef = this.menuBarRef;
		menuStructure.xmlFileURL = xmlFileURL;
		// timeline can be an object or a movie clip ref
		// that holds the listeners
		menuStructure.timeline = timeline; 
		
		// onload handler
		menuStructure.onLoad = function (success) 
		{
	
			// When the data arrives, pass it to the menu
			if (success) 
			{
				// this.menu.dataProvider = this.firstChild;
				// loop through the menu tags and create a menu
				// for each one
				// var this:XML = this;
				var menus:Array = this.firstChild.childNodes;
				var numMenus:Number = menus.length;
			  
				if ( numMenus > 0 )
				{
					// holds references to the menu instances
					var menuInstances:Object = new Object();
					
					for ( var i:Number = 0; i < numMenus; i++ )
					{
						var currentMenu:XML = menus[i];
						
						var currentMenuName = currentMenu.attributes.name;
						var currentMenuInstanceName = currentMenu.attributes.instanceName;
						var currentMenuListener = currentMenu.attributes.listener;
						
						// clone the current menu so adding it to the menubar
						// does not affect the main XML object (and thus the loop)
						var currentMenuClone = currentMenu.cloneNode(true);
	
						// create the new menu as a child of the menu bar instance
						var newMenu = this.menuBarRef.addMenu ( currentMenuName, currentMenuClone );
						
						// compose reference to listener object
						var eventListener:Object = this.timeline [ currentMenuListener ];
						
						// add listener for menu
						newMenu.addEventListener ( "change", eventListener );
						
						// save reference in array to be returned later
						menuInstances [ currentMenuInstanceName ] = newMenu;
					}
					
					// return an array of references to the 
					// various menus created
					return menuInstances;
				}
				else
				{
					trace ("No menus found in menu XML.");
				}
			}
			else
			{
				trace ("There was an error loading the menu XML.");
			}
		};
		
		menuStructure.load( xmlFileURL );
	}
}