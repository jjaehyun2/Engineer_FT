//
// $Id$

package com.threerings.msoy.world.client {
import flash.events.MouseEvent;
import flash.filters.ColorMatrixFilter;
import flash.geom.Rectangle;

import mx.containers.Canvas;
import mx.containers.Tile;
import mx.controls.Text;
import mx.core.UIComponent;

import com.threerings.io.TypedArray;

import com.threerings.util.Log;

import com.threerings.display.GraphicsUtil;

import com.threerings.orth.ui.MediaWrapper;
import com.threerings.orth.ui.ScalingMediaDescContainer;

import com.threerings.flex.CommandCheckBox;

import com.threerings.msoy.badge.data.all.BadgeCodes;
import com.threerings.msoy.badge.data.all.InProgressBadge;
import com.threerings.msoy.client.Msgs;
import com.threerings.msoy.client.Prefs;
import com.threerings.msoy.data.AVRGameNavItemData;
import com.threerings.msoy.data.BasicNavItemData;
import com.threerings.msoy.data.GwtPageNavItemData;
import com.threerings.msoy.data.HomePageItem;
import com.threerings.msoy.item.data.all.Item;
import com.threerings.msoy.ui.FlyingPanel;

/**
 * The "My Whirled Places" 3x3 grid of recent games and rooms you have visited, plus stamps and
 * special actions like the Whirled Tour.  Displayed when landing in your home room.
 */
public class HomePageDialog extends FlyingPanel
{
    public static var log :Log = Log.getLog(HomePageDialog);

    public function HomePageDialog (ctx :WorldContext)
    {
        super(ctx);
        _wctx = ctx;

        title = Msgs.HOME_PAGE_GRID.get("t.home_page");
        showCloseButton = true;
        setStyle("paddingTop", EDGE_MARGIN);
        setStyle("paddingLeft", EDGE_MARGIN);
        setStyle("paddingRight", EDGE_MARGIN);
        setStyle("paddingBottom", 2);
        setStyle("verticalGap", 0);
        setStyle("horizontalAlign", "left");

        // Set up the tile container for the items
        _grid = new Tile();
        _grid.tileWidth = IMAGE_WIDTH;
        _grid.tileHeight = IMAGE_HEIGHT + LABEL_HEIGHT;
        _grid.setStyle("horizontalGap", CELL_HSPACING);
        _grid.setStyle("verticalGap", CELL_VSPACING);
        addChild(_grid);

        var autoshow :CommandCheckBox = new CommandCheckBox(
            Msgs.HOME_PAGE_GRID.get("b.autoshow"), function (show :Boolean) :void {
                Prefs.setAutoshow("grid", show);
            });
        autoshow.selected = Prefs.getAutoshow("grid");
        addChild(autoshow);

        // Fill it with empty components just to force the layout
        gotItems(TypedArray.create(HomePageItem));

        open();
    }

    override public function stylesInitialized () :void
    {
        super.stylesInitialized();

        // Draw some dashed lines between the cells
        var color :int = getStyle("borderColor") as int;
        _grid.graphics.lineStyle(0.5, color, 1.0);
        for (var row :int = 1; row < ROWS; ++row) {
            var y :Number = row * (CELL_HEIGHT + CELL_VSPACING) - CELL_VSPACING / 2;
            var x1 :Number = CELL_WIDTH * COLUMNS + CELL_HSPACING * (COLUMNS - 1);
            GraphicsUtil.dashTo(_grid.graphics, 0, y, x1, y, 3, 3);
        }
        for (var col :int = 1; col < COLUMNS; ++col) {
            var x :Number = col * (CELL_WIDTH + CELL_HSPACING) - CELL_HSPACING / 2;
            var y1 :Number = CELL_HEIGHT * ROWS + CELL_VSPACING * (ROWS - 1);
            GraphicsUtil.dashTo(_grid.graphics, x, 0, x, y1, 3, 3);
        }
    }

    public function refresh () :void
    {
        var svc :WorldService = _ctx.getClient().requireService(WorldService) as WorldService;
        svc.getHomePageGridItems(_ctx.resultListener(gotItems));
    }

    protected function gotItems (items :TypedArray) :void
    {
        _grid.removeAllChildren();
        var numCells :int = ROWS * COLUMNS;
        for (var ii :int = 0; ii < numCells; ii++) {
            var disp :UIComponent = null;
            if (ii < items.length) {
                disp = createItem(HomePageItem(items[ii]));
            }
            if (disp == null) {
                disp = new UIComponent();
            }
            _grid.addChild(disp);
        }
    }

    protected function createItem (item :HomePageItem) :UIComponent
    {
        // Not filled in... bail
        if (item.getAction() == HomePageItem.ACTION_NONE) {
            return null;
        }

        // Create the image
        var view :ScalingMediaDescContainer = new ScalingMediaDescContainer(IMAGE_WIDTH, IMAGE_HEIGHT);
        view.setMediaDesc(item.getImage());
        var image :UIComponent = new MediaWrapper(view, IMAGE_WIDTH, IMAGE_HEIGHT, true);

        // create the label
        var label :Text = new Text();
        label.width = IMAGE_WIDTH;
        label.height = LABEL_HEIGHT;
        label.text = resolveItemText(item);
        label.truncateToFit = true;
        label.setStyle("textAlign", "center");
        label.setStyle("verticalAlign", "middle");
        label.setStyle("fontFamily", "Arial");
        label.setStyle("fontSize", "11");
        label.y = IMAGE_HEIGHT;

        // create the cell box
        var cell :Canvas = new Canvas();
        cell.addChild(image);
        cell.addChild(label);
        cell.width = CELL_WIDTH;
        cell.height = CELL_HEIGHT;
        cell.useHandCursor = true;
        cell.buttonMode = true;
        cell.mouseChildren = false;

        cell.addEventListener(MouseEvent.CLICK, function (evt :MouseEvent) :void {
            itemClicked(item);
            // TODO: figure out which HP items make sense to close and which don't
            // for now, leave open only for gwt page views
            if (item.getAction() != HomePageItem.ACTION_GWT_PAGE) {
                close();
            }
        });

        cell.addEventListener(MouseEvent.ROLL_OVER, function (evt :MouseEvent) :void {
            label.setStyle("textDecoration", "underline");
            image.filters = [BRIGHTEN_FILTER];
        });

        cell.addEventListener(MouseEvent.ROLL_OUT, function (evt :MouseEvent) :void {
            label.setStyle("textDecoration", "none");
            image.filters = [];
        });

        return cell;
    }

    protected function resolveItemText (item :HomePageItem) :String
    {
        var basicData :BasicNavItemData = item.getNavItemData() as BasicNavItemData;
        var name :String = basicData != null ? basicData.getName() : "?";

        switch (item.getAction()) {
        case HomePageItem.ACTION_BADGE:
            var badge :InProgressBadge = InProgressBadge(item.getNavItemData());
            var level :String = badge.levelName;
            var badgeName :String = Msgs.PASSPORT.get(badge.nameProp, level);
            var badgeDesc :String;
            if (Msgs.PASSPORT.exists(badge.descProp)) {
                badgeDesc = Msgs.PASSPORT.get(badge.descProp);
            } else {
                badgeDesc = Msgs.PASSPORT.get(badge.descPropGeneric, String(badge.levelUnits));
            }
            return Msgs.HOME_PAGE_GRID.get("b.earn_badge", badgeName, badgeDesc);

        case HomePageItem.ACTION_ROOM:
            return Msgs.HOME_PAGE_GRID.get("b.visit_room", name);

        case HomePageItem.ACTION_GROUP:
            return Msgs.HOME_PAGE_GRID.get("b.visit_group", name);

        case HomePageItem.ACTION_GAME:
        case HomePageItem.ACTION_AVR_GAME:
            return Msgs.HOME_PAGE_GRID.get("b.play_game", name);

        case HomePageItem.ACTION_EXPLORE:
            return Msgs.HOME_PAGE_GRID.get("b.whirled_tour");

        case HomePageItem.ACTION_GWT_PAGE:
            return GwtPageNavItemData(item.getNavItemData()).getName();

        default:
            return name;
        }
    }

    override protected function didOpen () :void
    {
        // Vertical center in place view, and against right edge with padding
        var placeBounds :Rectangle = _wctx.getTopPanel().getPlaceViewBounds();
        y = placeBounds.y + (placeBounds.height - height) / 2;
        x = placeBounds.right - width - PADDING;

        super.didOpen();

        refresh();
    }

    protected function itemClicked (item :HomePageItem) :void
    {
        // TODO: what's this for? looks important
        var trackingDetails :String;
        switch (item.getAction()) {

        case HomePageItem.ACTION_GAME:
            trackingDetails = "game_" + BasicNavItemData(item.getNavItemData()).getId();
            _wctx.getWorldController().handlePlayGame(
                BasicNavItemData(item.getNavItemData()).getId());
            break;

        case HomePageItem.ACTION_AVR_GAME:
            trackingDetails = "avrgame_" + BasicNavItemData(item.getNavItemData()).getId();
            _wctx.getWorldController().handleGoGroupHome(
                AVRGameNavItemData(item.getNavItemData()).getGroupId());
            break;

        case HomePageItem.ACTION_BADGE:
            trackingDetails = "badge_" + InProgressBadge(item.getNavItemData()).badgeCode;
            badgeClicked(InProgressBadge(item.getNavItemData()).badgeCode);
            break;

        case HomePageItem.ACTION_GROUP:
            trackingDetails = "group_" + BasicNavItemData(item.getNavItemData()).getId();
            _wctx.getWorldController().handleGoGroupHome(
                BasicNavItemData(item.getNavItemData()).getId());
            break;

        case HomePageItem.ACTION_ROOM:
            trackingDetails = "room_" + BasicNavItemData(item.getNavItemData()).getId();
            _wctx.getWorldController().handleGoScene(
                BasicNavItemData(item.getNavItemData()).getId());
            break;

        case HomePageItem.ACTION_EXPLORE:
            trackingDetails = "tour"
            startTour();
            break;

        case HomePageItem.ACTION_GWT_PAGE:
            var pageItemData :GwtPageNavItemData = GwtPageNavItemData(item.getNavItemData());
            _wctx.getWorldController().displayPage(pageItemData.getPage(), pageItemData.getArgs());

        default:
            trackingDetails = "UNKNOWN"
            log.info("No action for " + item);
            break;
        }
    }

    protected function badgeClicked (code :int) :void
    {
        var ctrl :WorldController = _wctx.getWorldController();
        switch (uint(code)) {
        case BadgeCodes.FRIENDLY:
        case BadgeCodes.FIXTURE:
            ctrl.displayPage("whirleds", "");
            break;

        case BadgeCodes.EXPLORER:
            startTour();
            break;

        case BadgeCodes.MAGNET:
            ctrl.displayPage("people", "invites");
            break;

        case BadgeCodes.GAMER:
        case BadgeCodes.CONTENDER:
        case BadgeCodes.COLLECTOR:
            ctrl.displayPage("games", "");
            break;

        case BadgeCodes.CHARACTER_DESIGNER:
            ctrl.displayPage("stuff", "" + Item.AVATAR);
            break;

        case BadgeCodes.FURNITURE_BUILDER:
            ctrl.displayPage("stuff", "" + Item.FURNITURE);
            break;

        case BadgeCodes.LANDSCAPE_PAINTER:
            ctrl.displayPage("stuff", "" + Item.DECOR);
            break;

        case BadgeCodes.PROFESSIONAL:
        case BadgeCodes.ARTISAN:
        case BadgeCodes.SHOPPER:
        case BadgeCodes.JUDGE:
        case BadgeCodes.OUTSPOKEN:
            ctrl.displayPage("shop", "");
            break;
        }
    }

    protected function startTour () :void
    {
        _wctx.getTourDirector().startTour();
    }

    protected var _grid :Tile;
    protected var _wctx :WorldContext;

    protected static const ROWS :int = 3;
    protected static const COLUMNS :int = 3;
    protected static const IMAGE_WIDTH :int = 100;
    protected static const IMAGE_HEIGHT :int = 75;
    protected static const LABEL_HEIGHT :int = 40;
    protected static const CELL_WIDTH :int = IMAGE_WIDTH;
    protected static const CELL_HEIGHT :int = IMAGE_HEIGHT + LABEL_HEIGHT;
    protected static const CELL_HSPACING :int = 30;
    protected static const CELL_VSPACING :int = 15;
    protected static const EDGE_MARGIN :int = 20;
    protected static const WIDTH :int =
        EDGE_MARGIN * 2 + IMAGE_WIDTH * COLUMNS + CELL_HSPACING * (COLUMNS - 1);
    protected static const HEIGHT :int =
        EDGE_MARGIN * 2 + (IMAGE_HEIGHT + LABEL_HEIGHT) * ROWS + CELL_VSPACING * (ROWS - 1);
    protected static const BRIGHTEN_DELTA :Number = 40;
    protected static const BRIGHTEN_FILTER :ColorMatrixFilter = new ColorMatrixFilter([
        1, 0, 0, 0, BRIGHTEN_DELTA,
        0, 1, 0, 0, BRIGHTEN_DELTA,
        0, 0, 1, 0, BRIGHTEN_DELTA,
        0, 0, 0, 1, 0]);
}
}