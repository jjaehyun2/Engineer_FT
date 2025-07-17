// ActionScript file
import Components.Component;
import Components.Controller;
import Components.Host;
import Components.Item_image;
import Components.Link;
import Components.Switch;

import flash.display.DisplayObject;
import flash.events.Event;
import flash.events.MouseEvent;
import flash.events.TimerEvent;
import flash.utils.Timer;

import mx.collections.ArrayCollection;
import mx.collections.ArrayList;
import mx.collections.XMLListCollection;
import mx.controls.Alert;
import mx.controls.Menu;
import mx.core.Container;
import mx.core.DragSource;
import mx.core.FlexGlobals;
import mx.core.MXMLObjectAdapter;
import mx.core.UIComponent;
import mx.events.DragEvent;
import mx.events.FlexEvent;
import mx.events.MenuEvent;
import mx.managers.CursorManager;
import mx.managers.CursorManagerPriority;
import mx.managers.DragManager;
import mx.messaging.AbstractConsumer;
import mx.rpc.events.FaultEvent;
import mx.rpc.events.ResultEvent;
import mx.utils.URLUtil;

import skins.Item_images_skin;

import spark.components.Button;

import utils.createMAC;

import view.ControllerListTitleWindow;
import view.HostListTitleWindow;
import view.LinkListTitleWindow;
import view.PortListTitleWindow;
import view.SwitchListTitleWindow;
import view.Vnet_flavorListWindow;
import view.Vnet_imageListWindow;
import view.Vnet_instanceListWindow;
import view.addControllerWindow;
import view.deleteControllerWindow;

import vo.Vnet_executor;
import vo.Vnet_usersubnet;
import vo.Vnet_vnet;


[Embed(source="assets/pen.png")]
private static const imageCursor:Class;
private var previewURL:String;
private var drag_start_obj:String;
private var isMouseDown:Boolean = false;
private var isDraw:Boolean = false;
private var fromObj:Item_image = null;
private var toObj:Item_image = null;
private var currentTarget:Item_image = null;
private var currentX:Number = 0;
private var currentY:Number = 0;
public var link_num:int = 0;

public var C_obj:ArrayCollection = new ArrayCollection();
public var H_obj:ArrayCollection = new ArrayCollection();
public  var S_obj:ArrayCollection = new ArrayCollection();

[Bindable]
public var startY:int;
[Bindable]
public var endY: int;
[Bindable]
public var startX:int;
[Bindable]
public var endX:int;


public var ac_controller:ArrayCollection=new ArrayCollection();
public var ac_switch:ArrayCollection=new ArrayCollection();
public var ac_port:ArrayCollection=new ArrayCollection();
public var ac_host:ArrayCollection=new ArrayCollection();
public var ac_link:ArrayCollection=new ArrayCollection();

public var activeItem:Item_image;
public var selectedObj:Component;
public var activeLink:Link; 
public var vnc_url:String = "";
public var vnc_iscomplete:Boolean = false;

public var parentDisplayObject:DisplayObject;

public var executor_id:int;
public var executor_name:String;
public var executor_password:String;

//true, edit usersubnet; false, add usersubnet
public var is_edit:Boolean;
public var current_index:int;

public var vnet_counter_vnet:int = 0;
public var vnet_counter:int = 0;
public var vnet_counter_ofport:int = 0;
public var vnet_counter_instance:int = 0;
public var executor:Vnet_executor;
public var vnet_vnet:Vnet_vnet;
public var vnet_counter_subnet:int = 0;
public var vnet_counter_script:int = 0;

public var vnet_controllers:ArrayCollection=new ArrayCollection();
public var vnet_switches:ArrayCollection=new ArrayCollection();
public var vnet_hosts:ArrayCollection=new ArrayCollection();
public var vnet_oflinks:ArrayCollection=new ArrayCollection();
public var vnet_links:ArrayCollection=new ArrayCollection();
public var vnet_ofports:ArrayCollection=new ArrayCollection();
public var vnet_switch_ofports:ArrayCollection=new ArrayCollection();
public var vnet_images:ArrayCollection=new ArrayCollection();
public var vnet_flavors:ArrayCollection=new ArrayCollection();
public var vnet_instances:ArrayCollection=new ArrayCollection();
public var vnet_image_instance:ArrayCollection=new ArrayCollection();
public var vnet_flavor_instance:ArrayCollection=new ArrayCollection();
public var vnet_instance_controller:ArrayCollection=new ArrayCollection();
public var vnet_instance_host:ArrayCollection=new ArrayCollection();
//public var vnet_console_url:ArrayCollection=new ArrayCollection();
public var vnet_resources:ArrayCollection=new ArrayCollection();
public var vnet_requests:ArrayCollection = new ArrayCollection();
[Bindable]
public var vnet_subnets:ArrayCollection=new ArrayCollection();
public var vnet_vnet_subnets:ArrayCollection=new ArrayCollection();
[Bindable]
public var vnet_scripts:ArrayCollection=new ArrayCollection();
public var vnet_vnet_scripts:ArrayCollection=new ArrayCollection();

public var vnet_updatelinks:ArrayCollection = new ArrayCollection();  //from,to,status,time,id
public var vnet_add_cons:ArrayCollection = new ArrayCollection();
public var vnet_del_cons:ArrayCollection = new ArrayCollection();
public var vnet_add_swis:ArrayCollection = new ArrayCollection();
public var vnet_del_swis:ArrayCollection = new ArrayCollection();
public var vnet_add_hosts:ArrayCollection = new ArrayCollection();
public var vnet_del_hosts:ArrayCollection = new ArrayCollection();