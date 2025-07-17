/**
 * Created by Administrator on 2015/8/13.
 */
package guiFlex.ui
{
	import away3d.tools.utils.Drag3D;

	import constants.StringConst;

	import flash.events.MouseEvent;

	import guiFlex.utils.ObjectUtils;

	import org.flexlite.domUI.collections.ArrayCollection;
	import org.flexlite.domUI.components.Button;
	import org.flexlite.domUI.components.DropDownList;
	import org.flexlite.domUI.components.Group;
	import org.flexlite.domUI.components.UIAsset;
	import org.flexlite.domUI.core.UIComponent;
	import org.flexlite.domUI.layouts.HorizontalLayout;

	import universal.pattern.event.GameDispatcher;
	import universal.pattern.event.GameEventConst;

	public class TopToolUI extends Group
	{
		[Embed(source="../../assets/xyz.png")]
		private var XYZ:Class;

		[Embed(source="../../assets/xy.png")]
		private var XY:Class;

		[Embed(source="../../assets/xz.png")]
		private var XZ:Class;

		[Embed(source="../../assets/yz.png")]
		private var YZ:Class;

		[Embed(source="../../assets/hide.png")]
		private var HIDE:Class;

		[Embed(source="../../assets/delete.png")]
		private var DELETE:Class;

		[Embed(source="../../assets/litter_bin.png")]
		private var DELETE_ALL:Class;

		private var _assetContainer:Group;
		private var _assetXYZ:UIAsset;
		private var _assetXY:UIAsset;
		private var _assetXZ:UIAsset;
		private var _assetYZ:UIAsset;
		private var _selectAsset:UIAsset;
		private var _showAuxiliaryLine:Boolean = true;
		private var _hide:UIAsset;

		private var _deleteContainer:Group;
		private var _deleteLayout:HorizontalLayout;
		private var _delete:UIAsset;
		private var _delete_all:UIAsset;

		private var _shapeDownList:DropDownList;
		private var _createCollection:ArrayCollection;
		private var _createBtn:Button;

		private var _rotationDownList:DropDownList;
		private var _rotationCollection:ArrayCollection;
		private var _rotationBtn:Button;
		private var _rotationStopBtn:Button;

		private var _layout:HorizontalLayout;
		private var _assetLayout:HorizontalLayout;

		private var _createContainer:Group;
		private var _createLayout:HorizontalLayout;

		private var _rotationContainer:Group;
		private var _rotationLayout:HorizontalLayout;

		public function TopToolUI()
		{
			super();
			_layout = new HorizontalLayout();
			_layout.gap = 30;
			layout = _layout;
			mouseEnabled = false;

			_assetContainer = new Group();
			_assetLayout = new HorizontalLayout();
			_assetLayout.gap = 10;
			_assetContainer.layout = _assetLayout;
			addElement(_assetContainer);
			_assetContainer.mouseEnabled = false;

			_deleteLayout = new HorizontalLayout();
			_deleteLayout.gap = 10;
			_deleteContainer = new Group();
			_deleteContainer.layout = _deleteLayout;
			addElement(_deleteContainer);
			_deleteContainer.mouseEnabled = false;

			_createContainer = new Group();
			_createLayout = new HorizontalLayout();
			_createLayout.gap = 10;
			_createContainer.layout = _createLayout;
			addElement(_createContainer);
			_createContainer.mouseEnabled = false;

			_rotationContainer = new Group();
			_rotationContainer.mouseEnabled = false;
			_rotationLayout = new HorizontalLayout();
			_rotationLayout.gap = 10;
			_rotationContainer.layout = _rotationLayout;
			addElement(_rotationContainer);

			_assetXYZ = new UIAsset();
			_assetXYZ.id = "xyz";
			_assetXYZ.skinName = XYZ;
			_assetXYZ.toolTip = StringConst.DRAG_ITEM_TIP_XYZ;
			_assetContainer.addElement(_assetXYZ);


			_assetXY = new UIAsset();
			_assetXY.id = Drag3D.PLANE_XY;
			_assetXY.skinName = XY;
			_assetXY.toolTip = StringConst.DRAG_ITEM_TIP_XY;
			_assetContainer.addElement(_assetXY);
			ObjectUtils.grey(_assetXY);


			_assetXZ = new UIAsset();
			_assetXZ.id = Drag3D.PLANE_XZ;
			_assetXZ.skinName = XZ;
			_assetXZ.toolTip = StringConst.DRAG_ITEM_TIP_XZ;
			_assetContainer.addElement(_assetXZ);
			ObjectUtils.grey(_assetXZ);


			_assetYZ = new UIAsset();
			_assetYZ.id = Drag3D.PLANE_ZY;
			_assetYZ.skinName = YZ;
			_assetYZ.toolTip = StringConst.DRAG_ITEM_TIP_YZ;
			_assetContainer.addElement(_assetYZ);
			ObjectUtils.grey(_assetYZ);


			_hide = new UIAsset();
			_hide.name = "hide";
			_hide.skinName = HIDE;
			_hide.toolTip = StringConst.HIDE_SHOW;
			_deleteContainer.addElement(_hide);

			_delete = new UIAsset();
			_delete.toolTip = StringConst.TIP_DELETE;
			_delete.name = "delete";
			_delete.skinName = DELETE;
			_deleteContainer.addElement(_delete);

			_delete_all = new UIAsset();
			_delete_all.toolTip = StringConst.TIP_DELETE_ALL;
			_delete_all.name = "delete_all";
			_delete_all.skinName = DELETE_ALL;
			_deleteContainer.addElement(_delete_all);

			_shapeDownList = new DropDownList();
			_shapeDownList.prompt = StringConst.TIPS_001;
			_createContainer.addElement(_shapeDownList);

			_createCollection = new ArrayCollection();
			_createCollection.addItem(StringConst.SHAPE_001);
			_createCollection.addItem(StringConst.SHAPE_002);
			_createCollection.addItem(StringConst.SHAPE_003);
			_createCollection.addItem(StringConst.SHAPE_004);

			_shapeDownList.dataProvider = _createCollection;

			_createBtn = new Button();
			_createBtn.toolTip = StringConst.TIP_CREATE_MODEL;
			_createBtn.name = "create";
			_createBtn.label = StringConst.TIPS_002;
			_createContainer.addElement(_createBtn);

			_rotationDownList = new DropDownList();
			_rotationDownList.prompt = StringConst.TIPS_003;
			_rotationContainer.addElement(_rotationDownList);

			_rotationCollection = new ArrayCollection();
			_rotationCollection.addItem(StringConst.ROTATION_X);
			_rotationCollection.addItem(StringConst.ROTATION_Y);
			_rotationCollection.addItem(StringConst.ROTATION_Z);
			_rotationDownList.dataProvider = _rotationCollection;

			_rotationBtn = new Button();
			_rotationBtn.toolTip = StringConst.TIP_STOP_ROTATION_MODEL;
			_rotationBtn.name = "rotation";
			_rotationBtn.label = StringConst.TIPS_004;
			_rotationContainer.addElement(_rotationBtn);

			_rotationStopBtn = new Button();
			_rotationStopBtn.toolTip = StringConst.TIP_STOP_ROTATION_MODEL;
			_rotationStopBtn.name = "rotationStop";
			_rotationStopBtn.label = StringConst.TIPS_005;
			_rotationContainer.addElement(_rotationStopBtn);

			_assetContainer.addEventListener(MouseEvent.CLICK, onAssetClick, false, 0, true);
			_deleteContainer.addEventListener(MouseEvent.CLICK, onDeleteContainerClick, false, 0, true);
			_createContainer.addEventListener(MouseEvent.CLICK, onCreateContainerClick, false, 0, true);
			_rotationContainer.addEventListener(MouseEvent.CLICK, onRotationClick, false, 0, true);

			_selectAsset = _assetXYZ;
			setSelect(1);
		}

		private function onRotationClick(event:MouseEvent):void
		{
			var target:UIComponent = event.target as UIComponent;
			if (target.name == "rotation")
			{
				if(_rotationDownList.selectedIndex==-1) return;
				var type:int = _rotationDownList.selectedIndex + 1;
				GameDispatcher.dispatchEvent(GameEventConst.ROTATION_ANIMATE, {type: type});
			} else if (target.name == "rotationStop")
			{
				GameDispatcher.dispatchEvent(GameEventConst.ROTATION_ANIMATE, {type: -1});
			}
		}

		private function onCreateContainerClick(event:MouseEvent):void
		{
			var target:UIComponent = event.target as UIComponent;
			if (target.name == "create")
			{
				createModel();
			}
		}

		public function createModel():void
		{
			if(_shapeDownList.selectedIndex==-1) return;
			var type:int = _shapeDownList.selectedIndex + 1;
			GameDispatcher.dispatchEvent(GameEventConst.CREATE_SHAPE, {type: type});
		}

		private function onDeleteContainerClick(event:MouseEvent):void
		{
			var target:UIComponent = event.target as UIComponent;
			if (target.name == "hide")
			{
				updateAuxiliaryVisible();
			} else if (target.name == "delete")
			{
				GameDispatcher.dispatchEvent(GameEventConst.DELETE_SHAPE, {type: 1});
			} else if (target.name == "delete_all")
			{
				GameDispatcher.dispatchEvent(GameEventConst.DELETE_SHAPE, {type: 2});
			}
		}

		/*
		* 显示隐藏辅助线
		* */
		public function updateAuxiliaryVisible():void
		{
			_showAuxiliaryLine = !_showAuxiliaryLine;
			GameDispatcher.dispatchEvent(GameEventConst.HIDE_SHOW_AUXILIARYLINE, {value: _showAuxiliaryLine});
		}

		private function onAssetClick(event:MouseEvent):void
		{
			if (_selectAsset)
			{
				ObjectUtils.grey(_selectAsset);
			}
			_selectAsset = event.target as UIAsset;
			ObjectUtils.grey(_selectAsset, false);
			GameDispatcher.dispatchEvent(GameEventConst.DRAG_SELECT_ITEM, {type: _selectAsset.id});
		}

		public function setSelect(index:int = 0):void
		{
			if (_selectAsset)
			{
				ObjectUtils.grey(_selectAsset);
			}
			_selectAsset = getSelect(index);
			ObjectUtils.grey(_selectAsset, false);
			GameDispatcher.dispatchEvent(GameEventConst.DRAG_SELECT_ITEM, {type: _selectAsset.id});
		}

		public function getSelect(index:int = 0):UIAsset
		{
			switch (index)
			{
				case 1:
					return _assetXYZ;
				case 2:
					return _assetXY;
				case 3:
					return _assetXZ;
				case 4:
					return _assetYZ;
			}
			return null;
		}

		/**
		 * 当前选择的缓动类型
		 * */
		public function get currentSelectRotationType():int
		{
			if (!_rotationDownList) return -1;
			return _rotationDownList.selectedIndex + 1;
		}

		public function destroy():void
		{
			removeAllElements();

			_layout && (_layout = null);
			_assetLayout && (_assetLayout = null);
			_createLayout && (_createLayout = null);

			if (_assetContainer)
			{
				_assetContainer.layout = null;
				_assetContainer.removeAllElements();
				_assetContainer.removeEventListener(MouseEvent.CLICK, onAssetClick);
				_assetContainer = null;
			}

			if (_deleteContainer)
			{
				_deleteContainer.layout = null;
				_deleteContainer.removeAllElements();
				_deleteContainer.removeEventListener(MouseEvent.CLICK, onDeleteContainerClick);
				_deleteContainer = null;
			}
			if (_createContainer)
			{
				_createContainer.layout = null;
				_createContainer.removeAllElements();
				_createContainer.removeEventListener(MouseEvent.CLICK, onCreateContainerClick);
				_createContainer = null;
			}

			if (_rotationContainer)
			{
				_rotationContainer.layout = null;
				_rotationContainer.removeAllElements();
				_rotationContainer.removeEventListener(MouseEvent.CLICK, onRotationClick);
				_rotationContainer = null;
			}

			if (_assetXYZ)
			{
				_assetXYZ.skinName = null;
				_assetXYZ.toolTip = null;
				_assetXYZ = null;
			}

			if (_assetXY)
			{
				_assetXY.skinName = null;
				_assetXY.toolTip = null;
				_assetXY = null;
			}

			if (_assetXZ)
			{
				_assetXZ.skinName = null;
				_assetXZ.toolTip = null;
				_assetXZ = null;
			}

			if (_assetYZ)
			{
				_assetYZ.skinName = null;
				_assetYZ.toolTip = null;
				_assetYZ = null;
			}
			_selectAsset && (_selectAsset = null);


			if (_hide)
			{
				_hide.skinName = null;
				_hide.toolTip = null;
				_hide = null;
			}
			if (_delete)
			{
				_delete.skinName = null;
				_delete.toolTip = null;
				_delete = null;
			}
			if (_delete_all)
			{
				_delete_all.skinName = null;
				_delete_all.toolTip = null;
				_delete_all = null;
			}

			if (_createCollection)
			{
				_createCollection.removeAll();
				_createCollection = null;
			}
			if (_shapeDownList)
			{
				_shapeDownList.prompt = null;
				_shapeDownList.dataProvider = null;
				_shapeDownList = null;
			}
			if (_createBtn)
			{
				_createBtn.toolTip = null;
				_createBtn = null;
			}
			if (_rotationBtn)
			{
				_rotationBtn.toolTip = null;
				_rotationBtn = null;
			}
			_instance && (_instance = null);
		}

		private static var _instance:TopToolUI = null;

		public static function get getInstance():TopToolUI
		{
			if (_instance == null)
			{
				_instance = new TopToolUI();
			}
			return _instance;
		}
	}
}