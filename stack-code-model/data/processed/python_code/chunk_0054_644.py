package
{
import mx.core.IFlexModuleFactory;
import mx.binding.ArrayElementWatcher;
import mx.binding.FunctionReturnWatcher;
import mx.binding.IWatcherSetupUtil2;
import mx.binding.PropertyWatcher;
import mx.binding.RepeaterComponentWatcher;
import mx.binding.RepeaterItemWatcher;
import mx.binding.StaticPropertyWatcher;
import mx.binding.XMLWatcher;
import mx.binding.Watcher;

[ExcludeClass]
public class _views_ShoppingViewWatcherSetupUtil
    implements mx.binding.IWatcherSetupUtil2
{
    public function _views_ShoppingViewWatcherSetupUtil()
    {
        super();
    }

    public static function init(fbs:IFlexModuleFactory):void
    {
        import views.ShoppingView;
        (views.ShoppingView).watcherSetupUtil = new _views_ShoppingViewWatcherSetupUtil();
    }

    public function setup(target:Object,
                          propertyGetter:Function,
                          staticPropertyGetter:Function,
                          bindings:Array,
                          watchers:Array):void
    {
        import mx.core.DeferredInstanceFromClass;
        import mx.collections.ArrayCollection;
        import __AS3__.vec.Vector;
        import mx.collections.ArrayList;
        import mx.binding.IBindingClient;
        import flash.events.MouseEvent;
        import mx.core.ClassFactory;
        import mx.states.AddItems;
        import mx.core.IFactory;
        import mx.collections.IList;
        import mx.core.DeferredInstanceFromFunction;
        import flash.events.EventDispatcher;
        import mx.states.State;
        import spark.components.List;
        import spark.components.Button;
        import components.ProductItem;
        import mx.core.IFlexModuleFactory;
        import mx.binding.BindingManager;
        import cart.ShoppingCart;
        import spark.components.Group;
        import mx.core.IDeferredInstance;
        import spark.components.gridClasses.GridColumn;
        import mx.core.IPropertyChangeNotifier;
        import flash.events.IEventDispatcher;
        import mx.core.IStateClient2;
        import spark.components.Label;
        import mx.states.SetProperty;
        import cart.ShoppingCartItem;
        import mx.core.mx_internal;
        import spark.components.VGroup;
        import valueObjects.Product;
        import spark.layouts.HorizontalLayout;
        import flash.events.Event;
        import spark.components.DataGrid;

        // writeWatcher id=0 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher shouldWriteChildren=true
        watchers[0] = new mx.binding.PropertyWatcher("shoppingCart",
                                                                             {
                propertyChange: true
            }
,
                                                                         // writeWatcherListeners id=0 size=2
        [
        bindings[0],
        bindings[2]
        ]
,
                                                                 propertyGetter
);

        // writeWatcher id=3 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher shouldWriteChildren=true
        watchers[3] = new mx.binding.PropertyWatcher("items",
                                                                             {
                propertyChange: true
            }
,
                                                                         // writeWatcherListeners id=3 size=1
        [
        bindings[2]
        ]
,
                                                                 null
);

        // writeWatcher id=1 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher shouldWriteChildren=true
        watchers[1] = new mx.binding.PropertyWatcher("groceryInventory",
                                                                             {
                propertyChange: true
            }
,
                                                                         // writeWatcherListeners id=1 size=1
        [
        bindings[1]
        ]
,
                                                                 propertyGetter
);

        // writeWatcher id=2 shouldWriteSelf=true class=flex2.compiler.as3.binding.FunctionReturnWatcher shouldWriteChildren=true
        watchers[2] = new mx.binding.FunctionReturnWatcher("getItemAt",
                                                                     target,
                                                                     function():Array { return [ 0 ]; },
                                                                                 {
                collectionChange: true
            }
,
                                                                     [bindings[1]],
                                                                     null
);


        // writeWatcherBottom id=0 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher
        watchers[0].updateParent(target);

 





        // writeWatcherBottom id=3 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher
        watchers[0].addChild(watchers[3]);

 





        // writeWatcherBottom id=1 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher
        watchers[1].updateParent(target);

 





        // writeWatcherBottom id=2 shouldWriteSelf=true class=flex2.compiler.as3.binding.FunctionReturnWatcher
        // writeEvaluationWatcherPart 2 1 parentWatcher
        watchers[2].parentWatcher = watchers[1];
        watchers[1].addChild(watchers[2]);

 





    }
}

}