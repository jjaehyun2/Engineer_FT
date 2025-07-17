/*
 * Class: MenuPositioning_View
 * @author Ryan C. Knaggs
 * @since 1.0
 * @version 1.2 - RCK
 * @date 09/09/2009
 * @description: This class file will handle
 * the positioning of the main category menu and sub-menus
 *
 * @see mxml.MenuController.as
 */

package views
{
	import flash.geom.Point;
	
	import libs.vo.GlobalsVO;
	
	import mx.controls.Image;
	
	import mxml.*;
	import mxml.header.LoginState;
	
	
	
	public class PositionMenu_View
	{
		
		private const CATEGORY_MENU:int = 1;
		private const SUBMENU:int = 2;
		private const RIGHT:String = "right";
		private const TOP:String = "top";
		
		
		
		/**
		 * Constructor
		 */
		 
		public function PositionMenu_View() {
		}
		
				
		
		

		/**
		 * Position the category menu
		 * @param menu:Menu - The current menu to position
		 * @param target:Object - The target is the location
		 * of the main menubar's current selected category item
		 */	
		 
		public function positionDownMenu(menu:*,target:Object,img:Image=null):void {
			
			// Interceptor If logged In menu state and user selects the Login feature
			if((menu is Menu) && (menu.parentRef is LoginState) ) {
				menu.hOrientation = "left";
			}
			
			/* Position the category menu 
			 * based on the meta data hOrientation */
			if (menu is Menu) {
				if (img is Image) {
					menu.hOrientation == RIGHT ? 
					img.x = menu.parentRef.imgHighlight.contentToGlobal(new Point(0,0)).x :
					img.x = menu.parentRef.imgHighlight.contentToGlobal(new Point(0,0)).x - 
							 menu.containerWidth + menu.parentRef.imgHighlight.width;
				} else {
					menu.hOrientation == RIGHT ? 
					menu.x = menu.parentRef.imgHighlight.contentToGlobal(new Point(0,0)).x :
					menu.x = menu.parentRef.imgHighlight.contentToGlobal(new Point(0,0)).x - 
							 menu.containerWidth + menu.parentRef.imgHighlight.width;
				}
	
				var menuContainerOffset:Number = 0;
				if (GlobalsVO.ISLoggedOut == false) {
					menuContainerOffset = Number(GlobalsVO.getCSSProperty("menuContainerOffsetY"));
				}
				
				if (img is Image) {
					img.y = GlobalsVO.getGlobal("MenuBarContainer").contentToGlobal(new Point(0,0)).y + Number(GlobalsVO.getCSSProperty("menuBarHeight"))+Number(GlobalsVO.getCSSProperty("categoryMenuOffsetY"));
				} else {
					menu.y = GlobalsVO.getGlobal("MenuBarContainer").contentToGlobal(new Point(0,0)).y + Number(GlobalsVO.getCSSProperty("menuBarHeight"))+Number(GlobalsVO.getCSSProperty("categoryMenuOffsetY"));

			       	// Set menu Effect Type
			       	menu.effectType = 0;	// Fade in only effect
				}
			}
			if (img is Image) {
				//trace('### img.x/y='+img.x,img.y);
			} else {
				//trace('### menu.x/y='+menu.x,menu.y);
			}

		}
		
		
		
		
		
		/**
		 * Position the side menu 
		 * @param menu
		 * @param target
		 */
		 		
		public function positionSideMenu(menu:Menu,target:Object):void {
			
			if(menu.parentRef.hOrientation == RIGHT) {
				menu.x = menu.parentRef.x + menu.parentRef.width;
				menu.effectType = CATEGORY_MENU;
			} else {
				menu.x = menu.parentRef.x - menu.parentRef.width;
				menu.effectType = SUBMENU;
			}
			
			var vorien:String = menu.parentRef.selectedMenuItem.vOrientation;
			menu.parentRef.selectedMenuItem.vOrientation == TOP ?
			menu.y = menu.parentRef.y :
			menu.y = menu.parentRef.selectedMenuItem.contentToGlobal(new Point(0,0)).y;
		}
	}
}