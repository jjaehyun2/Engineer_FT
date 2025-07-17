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
public class _components_ProductItemWatcherSetupUtil
    implements mx.binding.IWatcherSetupUtil2
{
    public function _components_ProductItemWatcherSetupUtil()
    {
        super();
    }

    public static function init(fbs:IFlexModuleFactory):void
    {
        import components.ProductItem;
        (components.ProductItem).watcherSetupUtil = new _components_ProductItemWatcherSetupUtil();
    }

    public function setup(target:Object,
                          propertyGetter:Function,
                          staticPropertyGetter:Function,
                          bindings:Array,
                          watchers:Array):void
    {
        import mx.core.DeferredInstanceFromClass;
        import __AS3__.vec.Vector;
        import mx.binding.IBindingClient;
        import flash.events.MouseEvent;
        import mx.core.ClassFactory;
        import mx.states.AddItems;
        import mx.core.IFactory;
        import mx.core.DeferredInstanceFromFunction;
        import flash.events.EventDispatcher;
        import spark.components.Image;
        import mx.states.State;
        import spark.components.Button;
        import mx.core.IFlexModuleFactory;
        import mx.binding.BindingManager;
        import cart.ShoppingCart;
        import spark.components.RichText;
        import mx.core.IDeferredInstance;
        import spark.components.Group;
        import mx.core.IPropertyChangeNotifier;
        import flash.events.IEventDispatcher;
        import mx.core.IStateClient2;
        import spark.components.Label;
        import cart.ShoppingCartItem;
        import mx.core.mx_internal;
        import spark.components.VGroup;
        import spark.layouts.HorizontalLayout;
        import valueObjects.Product;
        import flash.events.Event;

        // writeWatcher id=0 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher shouldWriteChildren=true
        watchers[0] = new mx.binding.PropertyWatcher("product",
                                                                             {
                propertyChange: true
            }
,
                                                                         // writeWatcherListeners id=0 size=6
        [
        bindings[0],
        bindings[1],
        bindings[2],
        bindings[3],
        bindings[4],
        bindings[5]
        ]
,
                                                                 propertyGetter
);

        // writeWatcher id=1 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher shouldWriteChildren=true
        watchers[1] = new mx.binding.PropertyWatcher("prodName",
                                                                             {
                propertyChange: true
            }
,
                                                                         // writeWatcherListeners id=1 size=1
        [
        bindings[0]
        ]
,
                                                                 null
);

        // writeWatcher id=3 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher shouldWriteChildren=true
        watchers[3] = new mx.binding.PropertyWatcher("listPrice",
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

        // writeWatcher id=2 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher shouldWriteChildren=true
        watchers[2] = new mx.binding.PropertyWatcher("imageName",
                                                                             {
                propertyChange: true
            }
,
                                                                         // writeWatcherListeners id=2 size=1
        [
        bindings[1]
        ]
,
                                                                 null
);

        // writeWatcher id=4 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher shouldWriteChildren=true
        watchers[4] = new mx.binding.PropertyWatcher("description",
                                                                             {
                propertyChange: true
            }
,
                                                                         // writeWatcherListeners id=4 size=1
        [
        bindings[3]
        ]
,
                                                                 null
);

        // writeWatcher id=5 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher shouldWriteChildren=true
        watchers[5] = new mx.binding.PropertyWatcher("isOrganic",
                                                                             {
                propertyChange: true
            }
,
                                                                         // writeWatcherListeners id=5 size=1
        [
        bindings[4]
        ]
,
                                                                 null
);

        // writeWatcher id=6 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher shouldWriteChildren=true
        watchers[6] = new mx.binding.PropertyWatcher("isLowFat",
                                                                             {
                propertyChange: true
            }
,
                                                                         // writeWatcherListeners id=6 size=1
        [
        bindings[5]
        ]
,
                                                                 null
);


        // writeWatcherBottom id=0 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher
        watchers[0].updateParent(target);

 





        // writeWatcherBottom id=1 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher
        watchers[0].addChild(watchers[1]);

 





        // writeWatcherBottom id=3 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher
        watchers[0].addChild(watchers[3]);

 





        // writeWatcherBottom id=2 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher
        watchers[0].addChild(watchers[2]);

 





        // writeWatcherBottom id=4 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher
        watchers[0].addChild(watchers[4]);

 





        // writeWatcherBottom id=5 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher
        watchers[0].addChild(watchers[5]);

 





        // writeWatcherBottom id=6 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher
        watchers[0].addChild(watchers[6]);

 





    }
}

}