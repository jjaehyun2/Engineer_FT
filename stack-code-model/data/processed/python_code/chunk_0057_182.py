package 
{
import flash.accessibility.*;
import flash.debugger.*;
import flash.display.*;
import flash.errors.*;
import flash.events.*;
import flash.external.*;
import flash.geom.*;
import flash.media.*;
import flash.net.*;
import flash.printing.*;
import flash.profiler.*;
import flash.system.*;
import flash.text.*;
import flash.ui.*;
import flash.utils.*;
import flash.xml.*;
import mx.binding.*;
import mx.core.ClassFactory;
import mx.core.DeferredInstanceFromClass;
import mx.core.DeferredInstanceFromFunction;
import mx.core.IDeferredInstance;
import mx.core.IFactory;
import mx.core.IFlexModuleFactory;
import mx.core.IPropertyChangeNotifier;
import mx.core.mx_internal;
import mx.filters.*;
import mx.styles.*;
import services.CategoryService;
import services.ProductService;
import spark.components.Application;
import spark.components.Button;
import views.ShoppingView;
import spark.components.Label;
import spark.layouts.BasicLayout;
import spark.components.Application;
import spark.layouts.HorizontalLayout;
import spark.components.List;
import spark.components.Button;

public class FlexGrocer extends spark.components.Application
{
	public function FlexGrocer() {}

	[Bindable]
	public var productService : services.ProductService;
	[Bindable]
	public var categoryService : services.CategoryService;
	[Bindable]
	public var btnCartView : spark.components.Button;
	[Bindable]
	public var btnCheckout : spark.components.Button;
	[Bindable]
	public var bodyGroup : views.ShoppingView;

	mx_internal var _bindings : Array;
	mx_internal var _watchers : Array;
	mx_internal var _bindingsByDestination : Object;
	mx_internal var _bindingsBeginWithWord : Object;

include "C:/Users/Oliver/Adobe Flash Builder 4.6/FlexGrocer/src/FlexGrocer.mxml:7,19";

}}