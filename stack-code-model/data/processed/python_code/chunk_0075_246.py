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
public class _FlexGrocerWatcherSetupUtil
    implements mx.binding.IWatcherSetupUtil2
{
    public function _FlexGrocerWatcherSetupUtil()
    {
        super();
    }

    public static function init(fbs:IFlexModuleFactory):void
    {
        import FlexGrocer;
        (FlexGrocer).watcherSetupUtil = new _FlexGrocerWatcherSetupUtil();
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
        import views.ShoppingView;
        import mx.binding.IBindingClient;
        import flash.events.MouseEvent;
        import mx.core.ClassFactory;
        import mx.core.IFactory;
        import mx.collections.IList;
        import mx.core.DeferredInstanceFromFunction;
        import spark.components.Application;
        import flash.events.EventDispatcher;
        import spark.components.List;
        import spark.components.Button;
        import services.CategoryService;
        import mx.core.IFlexModuleFactory;
        import mx.binding.BindingManager;
        import mx.core.IDeferredInstance;
        import services.ProductService;
        import mx.core.IPropertyChangeNotifier;
        import flash.events.IEventDispatcher;
        import spark.components.Label;
        import mx.core.mx_internal;
        import mx.events.FlexEvent;
        import spark.layouts.BasicLayout;
        import spark.layouts.HorizontalLayout;
        import flash.events.Event;

        // writeWatcher id=0 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher shouldWriteChildren=true
        watchers[0] = new mx.binding.PropertyWatcher("categoryService",
                                                                             {
                propertyChange: true
            }
,
                                                                         // writeWatcherListeners id=0 size=1
        [
        bindings[0]
        ]
,
                                                                 propertyGetter
);

        // writeWatcher id=1 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher shouldWriteChildren=true
        watchers[1] = new mx.binding.PropertyWatcher("categories",
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

        // writeWatcher id=2 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher shouldWriteChildren=true
        watchers[2] = new mx.binding.PropertyWatcher("productService",
                                                                             {
                propertyChange: true
            }
,
                                                                         // writeWatcherListeners id=2 size=1
        [
        bindings[1]
        ]
,
                                                                 propertyGetter
);

        // writeWatcher id=3 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher shouldWriteChildren=true
        watchers[3] = new mx.binding.PropertyWatcher("products",
                                                                             {
                propertyChange: true
            }
,
                                                                         // writeWatcherListeners id=3 size=1
        [
        bindings[1]
        ]
,
                                                                 null
);


        // writeWatcherBottom id=0 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher
        watchers[0].updateParent(target);

 





        // writeWatcherBottom id=1 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher
        watchers[0].addChild(watchers[1]);

 





        // writeWatcherBottom id=2 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher
        watchers[2].updateParent(target);

 





        // writeWatcherBottom id=3 shouldWriteSelf=true class=flex2.compiler.as3.binding.PropertyWatcher
        watchers[2].addChild(watchers[3]);

 





    }
}

}