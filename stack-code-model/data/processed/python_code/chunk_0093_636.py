package org.ro.view {
import mx.collections.XMLListCollection;
import mx.events.MenuEvent;

import org.ro.core.DisplayManager;
import org.ro.core.Globals;
import org.ro.core.Menu;
import org.ro.core.MenuEntry;
import org.ro.to.Invokeable;
import org.ro.to.Link;
import org.ro.to.Member;

public class RoMenuBar extends MenuBarAdapter {

    private var menu:Menu;

    public function RoMenuBar() {
        dataProvider = getDefaultMenuItems();
        labelField = "@label";
        iconField = "@icon";
        setMarginWidth(0);
        percentWidth = 100;
        addEventListener(MenuEvent.ITEM_CLICK, itemClickHandler);
        toolTip = "Click icon to select server (populates menu), configure, etc.."
    }

    protected function itemClickHandler(event:MenuEvent):void {
        var id:String = event.item.@id;
        if (id == "play") {
            handleHostSelection(event);
        } else if (id == "next") {
            new KitchenSink("Next");
        } else if (id == "dock") {
            toggleDock(event);
        } else if (id == "status") {
            toggleStatus(event);
        } else {
            handleActionSelection(event);
        }
    }

    private static function toggleDock(event:MenuEvent):void {
        var toggle:Boolean = event.item.@toggled;
        DisplayManager.toggleDock(toggle);
    }

    private static function toggleStatus(event:MenuEvent):void {
        var toggle:Boolean = event.item.@status;
        DisplayManager.toggleStatus(toggle);
    }

    private function handleActionSelection(event:MenuEvent):void {
        var action:Member = menu.findAction(event.item.@url);
        action.invoke();
    }

    private static function handleHostSelection(event:MenuEvent):void {
        var user:String = event.item.@user;
        var url:String = event.item.@url;
        var pw:String = event.item.@password;
        var path:String = event.item.@path;

        Globals.session.login(url, user, pw);

        var link:Link = new Link();
        link.setHref(url + path);
        link.setMethod(Invokeable.GET);
        link.invoke();
    }

    //TODO Multiple Services under the same title need to be grouped and separated
    public function amend(menu:Menu):void {
        this.menu = menu;
        var oldItems:XMLListCollection = dataProvider as XMLListCollection;
        var newMenuItems:XMLListCollection = XMLListCollection(oldItems);
        var addedTopMenus:Array = this.menu.uniqueMenuTitles();
        for each (var tm:String in addedTopMenus) {
            var newItem:String = '<topmenu label="' + tm + '">';
            //TODO iterate over 'subs' - account for multiple 'children'
            var subItems:Array = this.menu.findEntriesByTitle(tm);
            for each (var sm:MenuEntry in subItems) {
                newItem = newItem + '<submenu label="' + sm.itemTitle + '" url="' + sm.itemId + '"/>';
            }
            newItem = newItem + '</topmenu>';
            newMenuItems.addItem(new XML(newItem));
//            newMenuItems.addItem(new XML('<submenu type="separator"/>'));
        }
//        newMenuItems.removeItemAt(newMenuItems.length - 1);
        dataProvider = newMenuItems;
    }

    //DEPRECATED use FileReader.loadMenu("menu.xml")
    public static function getDefaultMenuItems():XML {
        //TODO store encoded with master pw in sqllite, add dialog for appending more entries and input of master pw
        var menuItems:XML =
                <topmenu label="" icon="MenuIcon">
                    <submenu id="play" label="SimpleApp (localhost:8080)"
                             url="http://localhost:8080"
                             path="/restful/services/"
                             user="sven"
                             password="pass"/>
                    <submenu id="play" label="ToDoApp (localhost:8080)"
                             url="http://localhost:8080"
                             path="/restful/services/"
                             user="todoapp-admin"
                             password="pass"/>
                    <submenu type="separator"/>
                    <submenu id="play"
                             label="SEMAT (http://semat-semat.193b.starter-ca-central-1.openshiftapps.com/:80)"
                             url="http://semat-semat.193b.starter-ca-central-1.openshiftapps.com"
                             path="/restful/services/"
                             user="user"
                             password="user"/>
                    <submenu type="separator"/>
                    <submenu id="play" label="KNIfe (localhost:8080)"
                             url="http://localhost:8080"
                             path="/restful/services/"
                             user="sven"
                             password="pass"/>
                    <submenu type="separator"/>
                    <submenu id="config" label="Settings">
                        <submenu id="dock" label="Dock" type="check" toggled="true"/>
                        <submenu id="status" label="Status Line" type="check" toggled="true"/>
                    </submenu>
                    <submenu id="next" label="KitchenSink"/>
                </topmenu>;
        return menuItems
    }

    public function getMenu():Menu {
        return menu;
    }

    public function setMenu(menu:Menu):void {
        this.menu = menu;
    }

}
}