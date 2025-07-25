/**
 * Created by max.rozdobudko@gmail.com on 7/30/17.
 */
package feathersx.mvvc {
import feathers.core.FeathersControl;
import feathers.data.IListCollection;

import skein.utils.ArrayUtil;
import skein.utils.VectorUtil;

import starling.display.DisplayObject;

public class NavigationItem {

    //--------------------------------------------------------------------------
    //
    //  Constructor
    //
    //--------------------------------------------------------------------------

    public function NavigationItem(identifier: String) {
        super();
        _identifier = identifier
    }

    public function dispose(): void {
        trace("dispose", this);
        if (isViewLoaded) {
            this.view.removeFromParent(true);
        }
    }

    //--------------------------------------------------------------------------
    //
    //  Identifier
    //
    //--------------------------------------------------------------------------

    private var _identifier:String;
    public function get identifier(): String {
        return _identifier;
    }

    //--------------------------------------------------------------------------
    //
    //  Delegate
    //
    //--------------------------------------------------------------------------

    //------------------------------------
    //  delegate
    //------------------------------------

    private var _callback: Function;
    internal function setChangeCallback(callback: Function): void {
        _callback = callback;
    }

    protected function notifyChange(animated: Boolean): void {
        if (_callback != null) {
            _callback(animated);
        }
    }

    //--------------------------------------------------------------------------
    //
    //  View
    //
    //--------------------------------------------------------------------------

    public function get isViewLoaded(): Boolean {
        return _view != null;
    }

    public function get viewIfLoaded(): DisplayObject {
        return _view;
    }

    private var _view: DisplayObject;
    public function get view(): DisplayObject {
        if (_view == null) {
            _view = new NavigationBarContent(this);
        }
        return _view;
    }

    //--------------------------------------------------------------------------
    //
    //  Title
    //
    //--------------------------------------------------------------------------

    private var _title: String;
    public function get title(): String {
        return _title;
    }
    public function set title(value: String): void {
        setTitle(value, false);
    }

    public function setTitle(value: String, animated: Boolean): void {
        if (value == _title) return;
        _title = value;
        notifyChange(animated);
    }

    private var _titleView: FeathersControl;
    public function get titleView(): FeathersControl {
        return _titleView;
    }
    public function set titleView(value: FeathersControl): void {
        _titleView = value;
    }

    //--------------------------------------------------------------------------
    //
    //  Back Button
    //
    //--------------------------------------------------------------------------

    //-------------------------------------
    //  hidesBackButton
    //-------------------------------------

    private var _hidesBackButton: Boolean = false;
    public function get hidesBackButton():Boolean {
        return _hidesBackButton;
    }
    public function set hidesBackButton(value:Boolean):void {
        _hidesBackButton = value;
    }

    //-------------------------------------
    //  backBarButtonItem
    //-------------------------------------

    private var _backBarButtonItem: BarButtonItem;
    public function get backBarButtonItem(): BarButtonItem {
        return _backBarButtonItem;
    }
    public function set backBarButtonItem(value: BarButtonItem): void {
        _backBarButtonItem = value;
    }

    //-------------------------------------
    //  leftItemsSupplementBackButton
    //-------------------------------------

    private var _leftItemsSupplementBackButton: Boolean;
    public function get leftItemsSupplementBackButton(): Boolean {
        return _leftItemsSupplementBackButton;
    }
    public function set leftItemsSupplementBackButton(value: Boolean): void {
        _leftItemsSupplementBackButton = value;
    }

    //--------------------------------------------------------------------------
    //
    //  Left Items
    //
    //--------------------------------------------------------------------------

    private var _leftItems:Vector.<BarButtonItem>;
    public function get leftItems(): Vector.<BarButtonItem> {
        return _leftItems;
    }
    public function set leftItems(value: Vector.<BarButtonItem>): void {
        setLeftItems(value, false);
    }
    public function setLeftItems(items: Vector.<BarButtonItem>, animated: Boolean): void {
        if (VectorUtil.equals(items, _leftItems)) return;
        _leftItems = items;
        notifyChange(animated);
    }

    //--------------------------------------------------------------------------
    //
    //  Right Items
    //
    //--------------------------------------------------------------------------

    private var _rightItems:Vector.<BarButtonItem>;
    public function get rightItems(): Vector.<BarButtonItem> {
        return _rightItems;
    }
    public function set rightItems(value: Vector.<BarButtonItem>): void {
        setRightItems(value, false);
    }
    public function setRightItems(items: Vector.<BarButtonItem>, animated: Boolean): void {
        if (VectorUtil.equals(items, _rightItems)) return;
        _rightItems = items;
        notifyChange(animated);
    }

    //--------------------------------------------------------------------------
    //
    //  Search Controller
    //
    //--------------------------------------------------------------------------

    private var _searchController: SearchController;
    public function get searchController(): SearchController {
        return _searchController;
    }
    public function set searchController(value: SearchController): void {
        if (value == _searchController) return;
        _searchController = value;
        notifyChange(false);
    }

    //--------------------------------------------------------------------------
    //
    //  Transitions
    //
    //--------------------------------------------------------------------------

    private var _pushTransition: Function;
    public function get pushTransition(): Function {
        return _pushTransition;
    }
    public function set pushTransition(value: Function): void {
        _pushTransition = value;
    }

    private var _popTransition: Function;
    public function get popTransition(): Function {
        return _popTransition;
    }
    public function set popTransition(value: Function): void {
        _popTransition = value;
    }

    //--------------------------------------------------------------------------
    //
    //  Description
    //
    //--------------------------------------------------------------------------

    public function toString(): String {
        return "[NavigationItem("+identifier+")]";
    }
}
}