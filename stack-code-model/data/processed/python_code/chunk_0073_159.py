package uieditor.editor.ui.tabpanel
{
	import flash.utils.Dictionary;

	import feathers.controls.Alert;
	import feathers.controls.Button;
	import feathers.controls.ButtonGroup;
	import feathers.controls.LayoutGroup;
	import feathers.controls.List;
	import feathers.controls.renderers.IListItemRenderer;
	import feathers.data.ListCollection;
	import feathers.layout.AnchorLayout;
	import feathers.layout.AnchorLayoutData;
	import feathers.layout.VerticalLayout;

	import starling.display.Canvas;
	import starling.display.DisplayObject;
	import starling.display.Image;
	import starling.display.Sprite;
	import starling.events.Event;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	import starling.textures.TextureAtlas;

	import uieditor.editor.UIEditorApp;
	import uieditor.editor.controller.DocumentEditor;
	import uieditor.editor.controller.LibraryDocumentEditor;
	import uieditor.editor.data.EmbedAsset;
	import uieditor.editor.events.DocumentEventType;
	import uieditor.editor.feathers.popup.MsgBox;
	import uieditor.editor.model.LibrarySetting;
	import uieditor.editor.ui.itemrenderer.LibraryItemRenderer;
	import uieditor.editor.ui.popup.CloneLibraryItemPopUp;
	import uieditor.editor.ui.popup.NewLibraryItemPopup;
	import uieditor.editor.util.ObjectUtil;

	public class LibraryTab extends LayoutGroup
	{
		private var _preview : DisplayObject;

		private var _previewLayer : LayoutGroup;

		private var _background : Canvas;

		private var _list : List;

		private var _buttonGroup : ButtonGroup;

		private var _libraryCollection : ListCollection;

		private var _libraryDocumentEditor : LibraryDocumentEditor;

		public function LibraryTab()
		{
			super();

			_libraryDocumentEditor = UIEditorApp.instance.libraryDocumentEditor;

			initUI();

			_libraryDocumentEditor.addEventListener( DocumentEventType.CHANGE, onLibraryItemChange );
			_libraryDocumentEditor.addEventListener( DocumentEventType.BACK_GROUND_COLOR_CHANGE, onBgChange );

			UIEditorApp.instance.documentEditor.addEventListener( DocumentEventType.UPDATE_LIBRARY, onUpdateLibrary );
			onUpdateLibrary( null );
			onBgChange( null );
		}

		private function onUpdateLibrary( event : Event ) : void
		{
			_libraryCollection.removeAll();

			var librarys : Dictionary = UIEditorApp.instance.documentEditor.librarys;
			for each ( var item : * in librarys )
			{
				_libraryCollection.addItem({ label: item.params.name, data: item });
			}
		}

		private function onBgChange( event : Event ) : void
		{
			_background.clear();
			_background.beginFill( _libraryDocumentEditor.backgroundColor, 1 );
			_background.drawRectangle( 0, 0, _previewLayer.width, _previewLayer.height );
			_background.endFill();
		}

		private function onLibraryItemChange( event : Event ) : void
		{
			var oldIndex : int = _list.selectedIndex;
			_libraryCollection.removeAll();

			var librarys : Dictionary = UIEditorApp.instance.documentEditor.librarys;
			for each ( var item : * in librarys )
			{
				_libraryCollection.addItem({ label: item.params.name, data: item });
			}
			_list.selectedIndex = oldIndex;
			showPreview( _list.selectedIndex );
		}

		private function initUI() : void
		{
			var anchorLayoutData : AnchorLayoutData = new AnchorLayoutData();
			anchorLayoutData.bottom = 0;
			anchorLayoutData.top = 25;
			layoutData = anchorLayoutData;

			layout = new AnchorLayout();

			_previewLayer = new LayoutGroup();
			_previewLayer.width = 280;
			_previewLayer.height = 200;

			anchorLayoutData = new AnchorLayoutData();
			anchorLayoutData.top = 0;
			anchorLayoutData.left = 0;
			anchorLayoutData.right = 0;
			_previewLayer.layoutData = anchorLayoutData;

			_background = new Canvas();
			_previewLayer.addChild( _background );

			addChild( _previewLayer );

			_buttonGroup = createToolButtons( createTextButtons());

			//init list
			_list = new List();
			_list.width = 280;
			_list.height = 400;

			var listLayout : VerticalLayout = new VerticalLayout();
			listLayout.useVirtualLayout = true;
			listLayout.padding = 0;
			listLayout.gap = 1;
			listLayout.horizontalAlign = VerticalLayout.HORIZONTAL_ALIGN_JUSTIFY;
			listLayout.verticalAlign = VerticalLayout.VERTICAL_ALIGN_TOP;
			_list.layout = listLayout;

			anchorLayoutData = new AnchorLayoutData();
			anchorLayoutData.top = 0;
			anchorLayoutData.bottom = 0;
			anchorLayoutData.topAnchorDisplayObject = _previewLayer;
			anchorLayoutData.bottomAnchorDisplayObject = _buttonGroup;
			_list.layoutData = anchorLayoutData;

			_list.itemRendererFactory = function() : IListItemRenderer
			{
				return new LibraryItemRenderer();
			}

			_list.addEventListener( Event.CHANGE, onListChange );

			addChild( _list );

			_libraryCollection = new ListCollection();
			_list.dataProvider = _libraryCollection;

			_previewLayer.touchGroup = true;
			_previewLayer.addEventListener( TouchEvent.TOUCH, onTouchPreview );
		}

		private function onTouchPreview( event : TouchEvent ) : void
		{
			var touch : Touch = event.getTouch( _previewLayer, TouchPhase.ENDED );
			if(touch == null)
				return;
			
			if ( touch.tapCount >= 2 )
			{
				if ( _list.selectedItem != null )
					UIEditorApp.instance.notificationDispatcher.dispatchEventWith( DocumentEventType.EDIT_LIBRARY_ITEM, false, _list.selectedItem );
			}
		}

		private function createTextButtons() : Array
		{
			var atlas : TextureAtlas = EmbedAsset.getEditorTextureAtlas();

			return [{ defaultIcon: new Image( atlas.getTexture( "iconfont-file01" )), label: "", toolTip: "添加", triggered: onAddButton },
				{ defaultIcon: new Image( atlas.getTexture( "iconfont-edit" )), label: "", toolTip: "编辑", triggered: onEditButton },
				{ defaultIcon: new Image( atlas.getTexture( "iconfont-delete01" )), label: "", toolTip: "删除", triggered: onDeleteButton },
				{ defaultIcon: new Image( atlas.getTexture( "iconfont-chevronup" )), label: "", toolTip: "上移", triggered: onUpButton },
				{ defaultIcon: new Image( atlas.getTexture( "iconfont-chevrondown" )), label: "", toolTip: "下移", triggered: onDownButton },
				{ defaultIcon: new Image( atlas.getTexture( "iconfont-duplicate" )), label: "", toolTip: "直接复制为", triggered: onDuplicateButton }];
		}

		private function onEditButton( event : Event ) : void
		{
			UIEditorApp.instance.notificationDispatcher.dispatchEventWith( DocumentEventType.EDIT_LIBRARY_ITEM, false, _list.selectedItem );
		}

		private function onAddButton( event : Event ) : void
		{
			NewLibraryItemPopup.show( _onAddLibraryItem );
		}

		private function _onAddLibraryItem( param : LibrarySetting ) : void
		{
			if ( UIEditorApp.instance.documentEditor.hasLibrary( param.linkage ))
			{
				Alert.show( "已经存在相同命名的库项目，请重新选择名称", "提示", new ListCollection(
					[
					{ label: "OK" }
					]));
				return;
			}

			var data : Object = { cls: param.rootContainerClass, customParams: {}, params: { name: param.linkage, width: param.width, height: param.height }};
			_libraryCollection.addItem({ label: param.linkage, data: data });

			UIEditorApp.instance.documentEditor.updateLibrary( param.linkage, data );

			_list.selectedIndex = _libraryCollection.length - 1;
			onListChange( null );
			UIEditorApp.instance.notificationDispatcher.dispatchEventWith( DocumentEventType.EDIT_LIBRARY_ITEM, false, _list.selectedItem );
		}

		private var _deleteMsgBox : MsgBox;

		private function onDeleteButton( event : Event ) : void
		{
			var item : Object = _list.selectedItem;
			if ( item != null )
			{
				_deleteMsgBox = MsgBox.show( "警告", "您确定要删除库文件?删除库文件也将删除舞台上所有库文件的引用，此操作不可恢复！", [ "确定", "取消" ]);
				_deleteMsgBox.addEventListener( Event.COMPLETE, onDeleteItem );
			}
		}

		private function onDeleteItem( e : Event ) : void
		{
			var index : int = int( e.data );
			if ( index == 0 )
			{
				var linkage : String = _list.selectedItem.label;
				_libraryCollection.removeItem( _list.selectedItem );
				UIEditorApp.instance.documentEditor.removeLibrary( linkage );
			}
			_deleteMsgBox = null;
		}

		private function updateButtonStates() : void
		{
			var selectIndex : int = _list.selectedIndex;

			Button( _buttonGroup.getChildAt( 1 )).isEnabled = selectIndex != -1;
			Button( _buttonGroup.getChildAt( 2 )).isEnabled = selectIndex != -1;
			Button( _buttonGroup.getChildAt( 3 )).isEnabled = selectIndex > 0;
			Button( _buttonGroup.getChildAt( 4 )).isEnabled = selectIndex < _list.dataProvider.length - 1;
			Button( _buttonGroup.getChildAt( 5 )).isEnabled = selectIndex != -1;
		}

		private function onUpButton( event : Event ) : void
		{

			updateButtonStates();
		}

		private function onDownButton( event : Event ) : void
		{
			updateButtonStates();
		}

		private function onDuplicateButton( event : Event ) : void
		{
			var item : Object = _list.selectedItem;
			updateButtonStates();
			if ( item )
			{
				var newObject : Object = ObjectUtil.cloneObject( item.data );
				CloneLibraryItemPopUp.show( newObject, _onCloneLibraryItem );
			}
		}

		private function _onCloneLibraryItem( newObject : Object ) : void
		{
			if ( UIEditorApp.instance.documentEditor.hasLibrary( newObject.params.name ))
			{
				Alert.show( "已经存在相同命名的库项目，请重新选择名称", "提示", new ListCollection(
					[
					{ label: "OK" }
					]));
				return;
			}

			_libraryCollection.addItem({ label: newObject.params.name, data: newObject });

			UIEditorApp.instance.documentEditor.updateLibrary( newObject.params.name, newObject );

			_list.selectedIndex = _libraryCollection.length - 1;
			onListChange( null );
			UIEditorApp.instance.notificationDispatcher.dispatchEventWith( DocumentEventType.EDIT_LIBRARY_ITEM, false, _list.selectedItem );
		}

		private function createToolButtons( buttons : Array ) : ButtonGroup
		{
			var group : ButtonGroup = new ButtonGroup();
			group.paddingTop = 5;
			group.paddingBottom = 5;
			group.gap = 2;
			group.direction = ButtonGroup.DIRECTION_HORIZONTAL;
			//group.maxWidth = 200;
			group.dataProvider = new ListCollection( buttons );

			var layoutData : AnchorLayoutData = new AnchorLayoutData();
			layoutData.left = 0;
			layoutData.right = 0;
			layoutData.bottom = 0;

			group.layoutData = layoutData;

			addChild( group );

			return group;
		}

		private function onListChange( event : Event ) : void
		{
			if ( _list.selectedIndex >= 0 )
			{
				showPreview( _list.selectedIndex );
			}
		}

		private function showPreview( index : int ) : void
		{
			if ( _preview != null )
			{
				_preview.removeFromParent( true );
			}

			if ( index <= -1 )
				return;

			var data : Object = _libraryCollection.getItemAt( index );
			var uiObject : Object = data.data;
			if ( uiObject == null )
				return;

			_preview = createPreview( uiObject );

			var sx : Number = _previewLayer.width / _preview.width;
			var sy : Number = _previewLayer.height / _preview.height;
			var s : Number = Math.min( sx, sy );

			_preview.scale = s;

			_preview.x = ( _previewLayer.width - _preview.width ) * 0.5;
			_preview.y = ( _previewLayer.height - _preview.height ) * 0.5;

			_previewLayer.addChild( _preview );
		}

		public function createPreview( data : Object ) : Sprite
		{
			var newData : Object = { layout: data };

			var testContainer : Sprite = new Sprite();

			var documentEditor : DocumentEditor = UIEditorApp.instance.documentEditor;

			var root : DisplayObject = documentEditor.uiBuilder.load( newData, documentEditor.librarys ).object;

			testContainer.addChild( root );

			return testContainer;
		}
	}
}