package org.ro.core {
import org.ro.core.event.EventLog;
import org.ro.core.event.LogEntry;
import org.ro.core.model.Visible;
import org.ro.view.IDockable;
import org.ro.view.RoMenuBar;
import org.ro.view.RoView;
import org.ro.view.tab.RoTabBar;

/**
 * Single point of contact for view components:
 * @item RoView consisting of:
 * @item RoMenubar,
 * @item RoTabbar (RoTabs),
 * @item RoStatusbar,
 * @item Dock
 * etc.
 */
public class DisplayManager {
    private static var LOG:EventLog = EventLog.getInstance();

    public static function addView(viewable:Visible):void {
        var title:String = viewable.tag();
        var le:LogEntry = LOG.find(title);
        if (le == null) {
            getTabBar().addView(viewable);
            LOG.add(title);
        } else {
            le.cacheHits += 1;
            LOG.update(title);
        }
    }

    public static function removeView(title:String):void {
        LOG.close(title);
    }

    // view convenience functions
    private static function getView():RoView {
        return Globals.getInstance().getView();
    }

    private static function getMenuBar():RoMenuBar {
        return getView().getMenuBar();
    }

    private static function getTabBar():RoTabBar {
        return getView().getTabs();
    }

    // view operations
    public static function updateStatus(le:LogEntry):void {
        getView().getStatusBar().update(le);
    }

    public static function amendMenu(menu:Menu):void {
        getMenuBar().amend(menu);
    }

    public static function dockView(tab:IDockable):void {
        getView().getDock().addView(tab);
    }

    public static function getMenu():Menu {
        return getMenuBar().getMenu();
    }

    public static function setMenu(menu:Menu):void {
        getMenuBar().setMenu(menu);
    }

    // delegate to Tabs
    public static function addEventTab():void {
        var list:Vector.<LogEntry> = LOG.getEntries();
        getTabBar().addEventTab(list);
    }

    public static function addTreeTab():void {
        var list:Vector.<LogEntry> = LOG.getEntries();
        getTabBar().addTreeTab(list);
    }

    public static function toggleDock(toggle:Boolean):void {
        getView().showDock(toggle);
    }

    public static function toggleStatus(toggle:Boolean):void {
        getView().showStatus(toggle);
    }

}
}