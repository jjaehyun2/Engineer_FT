import flash.desktop.NativeApplication;
import flash.events.Event;

import mx.events.FlexEvent;

import radiko.Radiko;

[Embed(source='radiko/images/radiko16.png')]
private var IconImage16:Class;
[Embed(source='radiko/images/radiko128.png')]
private var IconImage128:Class;

private function initApp(event:FlexEvent):void {
  // メモリ使用量軽減対策
  (event.target as Application).removeEventListener(FlexEvent.APPLICATION_COMPLETE, initApp);

  if (NativeApplication.supportsSystemTrayIcon || NativeApplication.supportsDockIcon) {
    var menu:NativeMenu = Radiko.iconMenu;

    // システムトレイ・ドックアイコンを登録
    var icon:InteractiveIcon;
    if (NativeApplication.supportsSystemTrayIcon) {
      var stIcon:SystemTrayIcon = (NativeApplication.nativeApplication.icon as SystemTrayIcon);
      icon = stIcon;
      stIcon.menu = menu;
      var appInfo:Object = Radiko.appInfo;
      stIcon.tooltip = appInfo.name + ' ' + appInfo.version;
      icon.addEventListener(MouseEvent.CLICK, function (event:MouseEvent):void {
        Radiko.togglePlayerWindow(Radiko.WINDOW_TOGGLE_SHOW);
      });
    } else if (NativeApplication.supportsDockIcon) {
      var dIcon:DockIcon = (NativeApplication.nativeApplication.icon as DockIcon);
      icon = dIcon;
      dIcon.menu = menu;
    } else {
      trace('Icon is not supported.');
      // 操作不能回避のため、アイコンが登録できなければ終了
      NativeApplication.nativeApplication.exit();
    }

    // アイコン画像
    var iconImage16:Bitmap  = (new IconImage16() as Bitmap);
    var iconImage128:Bitmap = (new IconImage128() as Bitmap);
    icon.bitmaps = [iconImage16, iconImage128];

    // メニュー - 表示
    var showWindowItem:NativeMenuItem = new NativeMenuItem('radikoを表示');
    menu.addItem(showWindowItem);
    showWindowItem.name = Radiko.MENU_SHOW_WINDOW;
    showWindowItem.addEventListener(Event.SELECT, function (event:Event):void {
      Radiko.togglePlayerWindow();
    });

    // メニュー - 終了
    var exitItem:NativeMenuItem = new NativeMenuItem('radikoを終了');
    menu.addItem(exitItem);
    exitItem.addEventListener(Event.SELECT, function (event:Event):void {
      NativeApplication.nativeApplication.exit();
    });

    // Windowsは起動時のみ、Macはドックアイコンをクリック時にも起きる
    NativeApplication.nativeApplication.addEventListener(InvokeEvent.INVOKE, function (event:InvokeEvent):void {
      Radiko.togglePlayerWindow(Radiko.WINDOW_TOGGLE_SHOW);
    });

    // 終了時に、他のイベントで終了中を検知するためフラグを立てる
    NativeApplication.nativeApplication.addEventListener(Event.EXITING, function (event:Event):void {
      Radiko.exiting = true;
    });

    // アップデート確認
    Radiko.checkUpdate();
  } else {
    trace('Icon is not supported.');
    // 操作不能回避のため、アイコンが登録できなければ終了
    NativeApplication.nativeApplication.exit();
  }
}