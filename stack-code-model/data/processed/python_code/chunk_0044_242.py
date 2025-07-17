package devoron.components.data.dsgridlist
{
	import away3d.containers.ObjectContainer3D;
	import away3d.entities.Mesh;
	import away3d.materials.ColorMaterial;
	import away3d.materials.methods.OutlineMethod;
	import devoron.components.buttons.AboutButton;
	import devoron.components.buttons.DSTextField;
	import devoron.dataui.DataContainerForm;
	import devoron.components.menus.CircleMenu;
	import devoron.components.multicontainers.table.DataContainersForm;
	import devoron.components.pcfs.PathChooserForm;
	import devoron.components.data.DataContainerTitleBar;
	import devoron.components.comboboxes.DSComboBox;
	import devoron.components.keyboardshortcuts.KeyboardShortcut;
	import devoron.components.labels.DSLabel;
	import devoron.components.buttons.StateToggleButton;
	import devoron.components.labels.TitleLabel;
	import devoron.data.core.base.DataStructur;
	import devoron.data.core.base.DataStructurObject;
	import devoron.data.core.DataStructursBinding;
	import devoron.data.core.base.IDataContainer;
	import devoron.data.core.base.IDataContainersManage;
	import devoron.data.core.IDataStructurContainer;
	import devoron.data.core.ISerializeObserver;
	import devoron.gui.parsers.components.JPanelParser;
	import devoron.studio.cameraeditor.CameraEditor;
	import devoron.studio.core.dsprocessor.BaseDataStructurProcessor;
	import devoron.studio.core.dstree.CirclDropDownButtonUI;
	import devoron.studio.core.dstree.IDataStructursControlPanel;
	import devoron.studio.core.StudioEvent;
	import devoron.studio.core.scenebrowser.CircleButton;
	import devoron.studio.core.scenebrowser.ContentTree;
	import devoron.studio.core.scenebrowser.ContentTreeCellRenderer;
	import devoron.studio.core.scenebrowser.ContentTreeNode;
	import devoron.studio.core.Studio;
	import devoron.studio.core.StudioModul;
	import devoron.studio.core.IStudioEditor;
	import devoron.studio.core.IStudioModul;
	import devoron.studio.core.workspace.IPropertiesPanelComponent;
	import devoron.studio.core.workspace.StudioWorkspaceLayout;
	import devoron.studio.mesheditor.material.ColorMaterialForm;
	import devoron.studio.mesheditor.MeshIcon;
	import devoron.studio.shadereditor.boxes.OperationBox;
	import devoron.studio.guidesinger.TextIcon;
	import devoron.studio.tools.studiomediator.StudioMediator;
	import devoron.utils.ArrayNamesHelper;
	import devoron.values.models.TreeModelValueComponent;
	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.IEventDispatcher;
	import flash.geom.Matrix;
	import flash.geom.Rectangle;
	import flash.utils.getDefinitionByName;
	import flash.utils.getQualifiedClassName;
	import org.aswing.ASColor;
	import org.aswing.ASFont;
	import org.aswing.ASFontAdvProperties;
	import org.aswing.AssetIcon;
	import org.aswing.border.EmptyBorder;
	import org.aswing.ButtonGroup;
	import org.aswing.Component;
	import org.aswing.Container;
	import org.aswing.decorators.ColorDecorator;
	import org.aswing.decorators.GradientBackgroundDecorator;
	import org.aswing.EmptyIcon;
	import org.aswing.event.AWEvent;
	import org.aswing.event.TreeSelectionEvent;
	import org.aswing.ext.Form;
	import org.aswing.ext.FormRow;
	import org.aswing.ext.GeneralGridListCellFactory;
	import org.aswing.ext.GridList;
	import org.aswing.geom.IntDimension;
	import org.aswing.geom.IntPoint;
	import org.aswing.geom.IntRectangle;
	import org.aswing.Icon;
	import org.aswing.Insets;
	import org.aswing.JButton;
	import org.aswing.JDropDownButton;
	import org.aswing.JFrame;
	import org.aswing.JFrameTitleBar;
	import org.aswing.JLabel;
	import org.aswing.JLabelButton;
	import org.aswing.JPanel;
	import org.aswing.JPathTextField;
	import org.aswing.JRadioButton;
	import org.aswing.JScrollPane;
	import org.aswing.JSprH;
	import org.aswing.JTabbedPane;
	import org.aswing.JTextField;
	import org.aswing.JToggleButton;
	import org.aswing.JTree;
	import org.aswing.KeyboardManager;
	import org.aswing.layout.BorderLayout;
	import org.aswing.layout.FlowLayout;
	import org.aswing.layout.GridLayout;
	import org.aswing.LoadIcon;
	import org.aswing.resizer.EmptyResizer;
	import org.aswing.tree.DefaultMutableTreeNode;
	import org.aswing.tree.DefaultTreeModel;
	import org.aswing.tree.DefaultTreeSelectionModel;
	import org.aswing.tree.GeneralTreeCellFactory;
	import org.aswing.tree.TreeModel;
	import org.aswing.tree.TreeNode;
	import org.aswing.tree.TreePath;
	import org.aswing.tree.TreeSelectionModel;
	import org.aswing.util.ArrayUtils;
	import org.aswing.util.HashMap;
	import org.aswing.VectorListModel;
	
	[Event(name="act",type="org.aswing.event.AWEvent")]
	
	/**
	 * Класс управления swf-пакетами проекта.
	 * @author ...
	 */
	public class DefaultDSGridListBrowser extends StudioModul /*implements IResi*/
	{
		[Embed(source="../../../../../assets/icons/unreal_logo.png")]
		private var unrealLogo:Class;
		
		private const GAME_STUDIO_SETTINGS_ICON16:String = "../assets/icons/assets_manager_icon16.png";
		
		[Embed(source="../../../../../assets/icons/mesh_editor_icon20.png")]
		private var MESH_EDITOR_ICON:Class;
		
		[Embed(source="../../../../../assets/icons/light_icon20.png")]
		private const LIGHT_EDITOR_ICON:Class;
		
		[Embed(source="../../../../../assets/icons/trash_icon20.png")]
		private var TRASH_ICON:Class;
		
		[Embed(source="../../../../../assets/icons/objectcontainer3D_icon20.png")]
		private var OBJECT_CONTAINER3D_ICON16:Class;
		
		[Embed(source="../../../../../assets/icons/search_icon16.png")]
		private const SELECT_COLOR_ICON:Class;
		
		/*[Embed(source = "../../../../../assets/icons/packages_manager_icon20.png")]
		 private var MESH_EDITOR_ICON:Class;*/
		
		private const PACKAGES_MANAGER_ICON:String = "../assets/icons/packages_manager_icon20.png";
		private const INFO_ICON:String = "../assets/icons/info_icon20.png";
		private const WARNING_ICON:String = "../assets/icons/warning_icon20.png";
		
		private var globalKeyboardManager:KeyboardManager;
		private var keyboardShortcuts:Vector.<KeyboardShortcut>;
		private var formRow:FormRow;
		protected var theroot:DefaultMutableTreeNode;
		protected var contentGridList:GridList;
		
		public var contentGridListScP:JScrollPane;
		//private var modulForm:Form;
		protected var relatedModuls:Vector.<String>;
		private var nodes:HashMap = new HashMap();
		private var editorsControlPanel:IDataStructursControlPanel;
		private var addItemBtn:CircleButton;
		
		// структры данных и редакторы BaseEditors
		public var datasAndEditors:HashMap = new HashMap();
		public var dataNameAndDataContainers:HashMap = new HashMap();
		public var dataTypesAndEditors:HashMap = new HashMap();
		
		// IDataContainersManager :) ^^ _ ^)&
		//public var datasAnd:HashMap = new HashMap();
		
		private var objectContainer3DBtn:JButton;
		private var meshBtn:JButton;
		private var lightBtn:JButton;
		
		protected var currentNode:DefaultMutableTreeNode;
		public var contentTreeModel:DefaultTreeModel;
		public var contentTreeSelectionModel:TreeSelectionModel;
		
		private var moduls:Array = [];
		protected var gotoParentNodeBtn:JLabelButton;
		protected var removeNodeBtn:JLabelButton;
		protected var copyNodeBtn:JLabelButton;
		protected var gotoRootNodeBtn:JLabelButton;
		private var title2:DataContainerTitleBar;
		private const GEOMETRY_ICON:String = "../assets/icons/geometry_icon20.png";
		private var searchPreferencesFR:FormRow;
		private var findAndReplaceTool:*;
		private var showSearchPreferencesBtn:StateToggleButton;
		protected var searchField:JTextField;
		protected var containerTypes:Array = ["objectContainer3DData"];
		
		protected var subModulForm:Form;
		
		public function DefaultDSGridListBrowser(modulName:String = "", modulIcon:Class = null, modulVersion:String = "")
		{
			super(modulName, modulIcon, modulVersion);
			
			//super.name = "SceneBrowser";
			//setSize(new IntDimension(270, 470));
			//setPreferredSize(new IntDimension(270, 470));
			//modulForm = new DataContainerForm("Нога Вольнова", "jds");
			
			title2 = new DataContainerTitleBar(modulName.toUpperCase(), new AssetIcon(new MESH_EDITOR_ICON, 20, 20), JLabel.CENTER);
			title2.setPreferredHeight(24);
			//fos.addLeftHoldRow(0, 5, titleLB);
			
			modulForm = new DataContainerForm();
			subModulForm = new Form();
			
			titleLBFR = modulForm.addLeftHoldRow(0, title2);
			modulForm.addLeftHoldRow(0, subModulForm);
			//var tableFR:FormRow = super.addLeftHoldRow(0, modulForm);
			
			topPanel = getTopControlsPanel();
			setTopControlsPanel(topPanel);
			
			createContentGridList();
			
			//var buttonsPanel:JPanel = new JPanel(new GridLayout(0, 1, 0, 0));
			var buttonsPanel:JPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 0, 5));
			buttonsPanel.setPreferredWidth(25);
			buttonsPanel.setPreferredHeight(300);
			var buttonsGroup:ButtonGroup = new ButtonGroup();
			for (var i:int = 0; i < 10; i++) 
			{
				var bnt:AboutButton = new AboutButton(String(i));
				buttonsPanel.append(bnt);
				bnt.setPreferredSize(new IntDimension(22, 22));
				buttonsGroup.append(bnt);
				//bnt.setPreferredHeight(18);
				//bnt.setMaximumHeight(18);
				//bnt.setHeight(18);
			}
			
			buttonsGroup.setSelectedIndex(0);
			subModulForm.addLeftHoldRow(0, buttonsPanel, 15, contentGridListScP);
			title2.setRelatedComponent(subModulForm);
			
			/*fos.setDragEnabled(true);
			   fos.addEventListener(DragAndDropEvent.DRAG_RECOGNIZED, __startDrag);
			 fos.addEventListener(DragAndDropEvent.DRAG_DROP, __stopDrag);*/
			
			//setBackgroundDecorator(new ColorDecorator(new ASColor(0x262F2B, 1), new ASColor(0xFFFFFF, 0.4)));
			
			//setSize(new IntDimension(510, 470));
			
			//super.addLeftHoldRow(0, [0, 20]);
			
			//var columnsVLMDC:VectorListModelDataComponent = new VectorListModelDataComponent(blocksModel);
			//super.setDataContainerChangeComponents({cisternsModel: cisternVLMDC, blocksModel: columnsVLMDC});
			
			//setBottomControlsPanel(getBottomControlsPanel());
			
			//setBottomControlsPanel(getTopControlsPanel());
			
			/*editorsControlPanel = new CircleMenu();
			   editorsControlPanel.addEventListener(AWEvent.HIDDEN, onHidden);
			   editorsControlPanel.addActionListener(circleMenuSelectionHandler);
			
			 addItemBtn.setRelatedObject(editorsControlPanel, AWEvent.SHOWN, showMenu, AWEvent.HIDDEN, editorsControlPanel.hide);*/
			
			//contentTreeSelectionModel.setSelectionPath(new TreePath(theroot.getPath()));
			
			//pack();5, 
			subModulForm.setBorder(new EmptyBorder(null, new Insets(0, 5)));
			subModulForm.pack();
			//setVisible(true);
			
			//var treeModelValueComponent:TreeModelValueComponent = new TreeModelValueComponent(contentGridList);
			//(modulForm as DataContainerForm).setDataContainerChangeComponents({tree: treeModelValueComponent});
			//super.setDataContainerChangeComponents( { color: colorCCF, bothSide: bothSideChB, blendMode: blendModeCB, alpha: alphaST /*,lightPickerId: lightPickerIdSDC,*/ /*methods: methodsForm*/} );
			
			//new getGameStudioComponent("Find and replace", setFindAndReplaceTool);
			//addEventListener(
		}
		
		public function setBottomControlsPanel(bottomPanel:Container):void
		{
			if (bottomPanel)
				subModulForm.addLeftHoldRow(0, bottomPanel);
		}
		
		public function setTopControlsPanel(topPanel:Container):void
		{
			if (topPanel)
				subModulForm.addLeftHoldRow(0, topPanel);
		}
		
		public function getTopControlsPanel():Container
		{
			var fos:Form = new Form();
			
			//var titleLB:DSLabel = new DSLabel("DEVORON GAME STUDIO" /*+ dataName.toUpperCase()*/, new AssetIcon(new unrealLogo, 22, 22, true), JLabel.LEFT);
			//titleLB.setPreferredWidth(270);
			//var colors:Array = [0x000000, 0x000000, 0x000000, 0x000000, 0x000000];
			//var alphas:Array = [0.24, 0.14, 0.08, 0.04, 0.01];
			//var ratios:Array = [0, 70, 145, 200, 255];
			//var matrix:Matrix = new Matrix();
			//matrix.createGradientBox(270, 22, 0, 0, 0);
			//fos.setBackgroundDecorator(new GradientBackgroundDecorator(GradientBackgroundDecorator.LINEAR, colors, alphas, ratios, matrix, "pad", "rgb", 0, new ASColor(0xFFFFFF, 0), 2));
			
			fos.setDragEnabled(true);
			
			//fos.addEventListener(DragAndDropEvent.DRAG_RECOGNIZED, __startDrag);
			//fos.addEventListener(DragAndDropEvent.DRAG_DROP, __stopDrag);
			
			var composite:Form = new Form();
			//setContentPane(
			
			composite.addLeftHoldRow(0, fos);
			
			var tableFR:FormRow = modulForm.addLeftHoldRow(0, composite);
			
			fos.metaData = composite;
			
			//title2.setRelatedComponent(subModulForm);
			
			showSearchPreferencesBtn = new StateToggleButton("", new AssetIcon(new SELECT_COLOR_ICON, 20, 20));
			showSearchPreferencesBtn.setBackgroundDecorator(null);
			//showChooserBtn.addActionListener(showSearchPreferencesBtnHandler);
			
			//getTopControlsPanle(getTopControlsPanel());
			
			searchField = new DSTextField();
			searchField.setPreferredWidth(240);
			searchField.addActionListener(searchFieldHandler);
			composite.addLeftHoldRow(0, searchField, 3, showSearchPreferencesBtn);
			
			//var panel:JPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
			//panel.setPreferredWidth(270);
			//panel.appendAll( searchField, new JSprH(3), showSearchPreferencesBtn);
			
			return composite;
		}
		
		public function getBottomControlsPanel():Container
		{
			var panel:JPanel = new JPanel(new FlowLayout(FlowLayout.LEFT, 2));
			addItemBtn = new CircleButton("");
			addItemBtn.setPreferredSize(new IntDimension(40, 40));
			
			var dcf:DataContainersForm = new DataContainersForm();
			//dcf.containersGridList.addSelectionListener(selectContentViewListener);
			
			var bb:JDropDownButton = new JDropDownButton("", null, false, dcf);
			bb.setUI(new CirclDropDownButtonUI());
			bb.setPopupAlignment(JDropDownButton.RIGHT);
			bb.setForeground(new ASColor(0xFFFFFF, 0.8));
			//bb.setFont(bb.getFont().changeBold(true));
			bb.setFont(bb.getFont().changeUnderline(true));
			bb.setBackgroundDecorator(null);
			//bb.setPreferredWidth(100);
			
			objectContainer3DBtn = new JButton("", new AssetIcon(new OBJECT_CONTAINER3D_ICON16, 20, 20));
			gotoParentNodeBtn = createButton("♂", gotoParentNodeBtnHandler);
			gotoRootNodeBtn = createButton("♀", gotoRootNodeBtnHandler);
			removeNodeBtn = createButton("R", removeNodeBtnHandler);
			copyNodeBtn = createButton("C", copyNodeBtnHandler);
			panel.appendAll(bb, 10, gotoParentNodeBtn, gotoRootNodeBtn, removeNodeBtn, copyNodeBtn);
			//modulForm.addLeftHoldRow(0, 100, addItemBtn, 10, gotoParentNodeBtn, gotoRootNodeBtn, removeNodeBtn, copyNodeBtn /*, 5, removeBtn*/);
			return panel;
		}
		
		public function getSearchPanel():Container
		{
			return null;
		}
		
		public function getTreeModel():DefaultTreeModel
		{
			return contentTreeModel;
		}
		
		public function getSelectionModel():TreeSelectionModel
		{
			return contentTreeSelectionModel;
		}
		
		private function searchFieldHandler(e:AWEvent):void
		{
			var searchText:String = searchField.getText();
			
			if (searchText == "")
			{
				// восстановить изначальные узлы
			}
			else
			{
				
			}
			
			var nodes:Array = theroot.children();
			
			//var dataStructur:DataStructur = new ViewData();
			//dataStructur.dataName = "view"
			
			//theroot = new ContentTreeNode(root.getDataStructur(), new EmptyIcon(20, 20));
			//treeModel = new DefaultTreeModel(theroot);
			
			// мне придётся спуститься вниз по всем узлам и если узел в потомках имеет ключевые слова, то сохранить его и развернуть
			// иначе - удалить узел или не добавлять
			// нужен красивый рекурсивчик. один шаг до разбоя, два - до победы
			theroot.removeAllChildren();
			
			for each (var item:ContentTreeNode in nodes)
			{
				var dataStructur:DataStructur = item.getDataStructur();
				
				if (dataStructur.dataName.indexOf(searchText) != -1)
				{
					//var newNode:ContentTreeNode = new ContentTreeNode(dataStructur, new EmptyIcon(20, 20));
					//contentTreeModel.insertNodeInto(item, theroot, theroot.getChildCount());
					theroot.append(item);
						//contentTreeModel.insertNodeInto(newNode, theroot, theroot.getChildCount());
						//gtrace("4:" + dataStructur.dataChangeTimestamp);
				}
			}
			
			//resultsTree.setModel(treeModel);
			contentGridList.updateUI();
			
			var nodes2:Array = theroot.children();
		
			//gtrace("nodes " + nodes + " " + nodes2);
		
			//treeModel.
			// перебрать циклом все DataStructur
			// оставить только те, которые содержат подстроку поиска в своём названии
		
			// по сути - всё просто. Перебираем дерево, оставляя только те узлы,
			// у которых имена совпадают с подстрокой
		
		}
		
		private function setFindAndReplaceTool(findAndReplaceTool:*):void
		{
			this.findAndReplaceTool = findAndReplaceTool;
			showSearchPreferencesBtn.setRelatedObject(findAndReplaceTool, "popupOpened", findAndReplaceTool.show, "popupClosed", findAndReplaceTool.hide);
		}
		
		public override function setTitle(title:String):void
		{
			//title2.setText(title);
		
		}
		
		public override function getTitle():String
		{
			//return title2.getText();
			return "";
		}
		
		public function getContentTree():GridList
		{
			return contentGridList;
		}
		
		override public function setVisible(v:Boolean):void
		{
			super.setVisible(v);
			if (v)
			{
				updateUI();
			}
		}
		
		public function getDataStructrurNames():Array
		{
			var arr:Array = [];
			for each (var modul:BaseDataStructurProcessor in moduls)
				arr.push(modul.getDataName());
			return arr;
		}
		
		override public function setStudioComponents(components:Array):void
		{
			//gtrace(components);
			setModuls(components);
		}
		
		protected var dispatcher:IEventDispatcher;
		private var tableFR:FormRow;
		protected var titleLBFR:FormRow;
		protected var parentsTypes:Array;
		
		override public function setStudioDispatcher(dispatcher:IEventDispatcher):void
		{
			//super.setStudioDispatcher(dispatcher);
			this.dispatcher = dispatcher;
		}
		
		override public function installStudioListeners():void
		{
			//super.installStudioListeners();
			dispatcher.addEventListener(StudioEvent.STUDIO_MODUL_ADDED, onModulAdded);
		}
		
		private function onModulAdded(e:StudioEvent):void
		{
			var modul:* = e.data;
			
			if (!(modul is IStudioEditor))
				return;
			
			moduls.push(modul);
			
			//editorsControlPanel.setData(moduls);
			
			//for each (var modul:BaseEditor in this.moduls)
			//var className:String = getQualifiedClassName();
			datasAndEditors.put(modul.getDataName(), modul);
			
			dataTypesAndEditors.put(modul.getDataName(), modul);
			
			//if (modul.getModulName() == "View editor")
				//setRoot();
		}
		
		public var folders:HashMap = new HashMap();
		
		public function setModuls(moduls:Array):void
		{
			//this.moduls = [];
			var editor:BaseDataStructurProcessor;
			var dcf:DataContainerForm;
			var opBox:OperationBox;
			
			for (var i:int = 0; i < moduls.length; i++)
			{
				if (moduls[i] is IStudioEditor || moduls[i] is IDataContainersManager || moduls[i] is DataContainerForm || moduls[i] is OperationBox)
					this.moduls.push(moduls[i]);
				
				var modul:* = moduls[i];
				// если модуль, работающий с данными - это редактор, который возвращает DataStructur
				
				// первый вариант
				/*if (modul is BaseEditor)
				   {
				   editor = modul as BaseEditor;
				   //var className:String = getQualifiedClassName(modul.getDataStructurClass());
				   datasAndEditors.put(editor.getDataName(), modul);
				   //datasAndEditors.put(modul.getDataStructurClass(), modul);
				
				   dataTypesAndEditors.put(modul.getDataName(), modul);
				   gtrace("2: dataTypesAndEditors" + dataTypesAndEditors.keys() + " modul.getDataName() " + modul.getDataName());
				   if (modul.getModulName() == "View editor")
				   setRoot();
				 }*/
				
				if (modul is BaseDataStructurProcessor)
				{
					editor = modul as BaseDataStructurProcessor;
					var className:String = getQualifiedClassName(modul.getDataStructurClass());
					datasAndEditors.put(editor.getDataName(), modul);
					/*var dsNode:DefaultMutableTreeNode = */
					addDataStructur(editor.getDataStructurClass(), editor.getDataName(), editor.getModulIcon());
				}
				
				/*else if (modul is DataContainerForm)
				   {
				   dcf = modul as DataContainerForm;
				   dataNameAndDataContainers.put(dcf.dataContainerName, dcf);
				   addDataContainerForm(dcf, dcf.dataContainerName, dcf.icon);
				   //addDataStructurObject(dcf.collectDataFromContainer() as DataStructurObject, dcf.dataContainerName, dcf.icon);
				 }*/
				else if (modul is OperationBox)
				{
					opBox = modul as OperationBox;
					var dcf:DataContainerForm = opBox.getContentForm() as DataContainerForm;
					//gtrace(dcf);
					dataNameAndDataContainers.put(dcf.dataContainerName, dcf);
					var dsNode:DefaultMutableTreeNode = addDataContainerForm(dcf, dcf.dataContainerName, dcf.icon);
					
					//var node:DefaultMutableTreeNode = new ContentTreeNode(dataStructur, editor.getModulIcon());
					
					var node:DefaultMutableTreeNode = folders.get(dcf.dataContainerType);
					
					if (!node)
					{
						//var ds:DataStructur = new ObjectContainer3DData;
						//var ob:ObjectContainer3D = new ObjectContainer3D();
						//ob.name = dcf.dataContainerType;
						//ds.relatedObject = ob;
						//ds.dataName = dcf.dataContainerType;
						////node = addDataStructur2(ds);
						//node = new ContentTreeNode(ds /*editor.getModulIcon()*/);
						//folders.put(dcf.dataContainerType, node);
						//
						//theroot.append(node);
						//
					}
					
					contentTreeModel.insertNodeInto(dsNode, node, node.getChildCount());
					//contentGridList.setSelectionPath(new TreePath(dsNode.getPath()));
					
				}
				
			}
		
			
			topPanel.repaintAndRevalidate();
			//editorsControlPanel.setData(this.moduls);
		
			// временно, чтобы разделять менеджер IDataContainer и BaseEditor
			// надо перебрать все IDataContainer в IDataContainersManager
			//function getDataContainersNames():Array;
		
		}
		
		private function onHidden(e:AWEvent):void
		{
			gtrace("hide");
		}
		
		private function showMenu():void
		{
		/*if (editorsControlPanel.parent == null)
		   stage.addChild(editorsControlPanel);
		   editorsControlPanel.setVisible(true);
		
		   //stage.setChildIndex(circleMenu, stage.numChildren - 1);
		
		   var ds:Rectangle = addItemBtn.getBounds(stage);
		   var pos:IntPoint = new IntPoint(ds.x - 200 * .5 + ds.width * .5, ds.y - 200 * .5 + ds.height * .5);
		
		   editorsControlPanel.x = pos.x;
		 editorsControlPanel.y = pos.y;*/
		}
		
		/*public function setDefaultNodeFactory(columnClass:String, renderer:SceneBrowserTreeNodeFactory):void
		   {
		   if (renderer != null)
		   {
		   defaultRenderersByColumnClass.put(columnClass, renderer);
		   }
		   else
		   {
		   defaultRenderersByColumnClass.remove(columnClass);
		   }
		   }
		
		   public function createDefaultCellFactories():void
		   {
		   defaultRenderersByColumnClass = new HashMap();
		   defaultRenderersByColumnClass.put("objectContainer3DData", new SceneBrowserTreeNodeFactory(ObjectContainer3DNode));
		   defaultRenderersByColumnClass.put("*", new SceneBrowserTreeNodeFactory(Object3DNode));
		 }*/
		
		/*public function getDefaultCellFactory(columnClass:String):TableCellFactory
		   {
		   //gtrace("getDefaultRenderer of " + columnClass);
		   if (columnClass == null)
		   {
		   return null;
		   }
		   else
		   {
		   var renderer:Object = defaultRenderersByColumnClass.get(columnClass);
		   //gtrace("defaultRenderersByColumnClass " + renderer);
		   if (renderer != null)
		   {
		   return TableCellFactory(renderer);
		   }
		   else
		   {
		   return getDefaultCellFactory("Object");
		   }
		   }
		 }*/
		
		public function addDataContainerForm(dcf:DataContainerForm, dataName:String, dataIcon:Icon):DefaultMutableTreeNode
		{
			var parentNode:DefaultMutableTreeNode = currentNode /*nodes.get(folder.parentPath)*/;
			if (!parentNode)
				parentNode = theroot;
			//var dso:DataStructurObject = dataStructurObject;
			
			if (!parentNode)
				parentNode = theroot;
			
			//dso.dataName = getNewDataStructurName(parentNode, dataName) /*getNewDataStructurName()*/;
			
			var node:DefaultMutableTreeNode = new ContentTreeNode(dcf, dataIcon);
			parentNode.append(node);
			
			if (String(node) == "")
			{
				gtrace(node);
			}
			
			contentTreeModel.insertNodeInto(node, parentNode, parentNode.getChildCount());
			//contentGridList.setSelectionPath(new TreePath(node.getPath()));
			
			return node;
			// создание структуры данных должно изменять историю
		}
		
		public function addDataStructurObject(dataStructurObject:DataStructurObject, dataName:String, dataIcon:Icon):DataStructurObject
		{
			var parentNode:DefaultMutableTreeNode = currentNode /*nodes.get(folder.parentPath)*/;
			if (!parentNode)
				parentNode = theroot;
			var dso:DataStructurObject = dataStructurObject;
			
			if (!parentNode)
				parentNode = theroot;
			
			dso.dataName = getNewDataStructurName(parentNode, dataName) /*getNewDataStructurName()*/;
			
			//var node:DefaultMutableTreeNode = new ContentTreeNode(dso, dataIcon);
			//parentNode.append(node);
			//contentTreeModel.insertNodeInto(node, parentNode, parentNode.getChildCount());
			
			//contentTreeModel.removeNodeFromParent(
			//contentTreeModel.
			
			//contentGridList.setSelectionPath(new TreePath(node.getPath()));
			return dso;
			// создание структуры данных должно изменять историю
		}
		
		public function removeDataStructurObject(dataStructurObject:DataStructurObject, node:DefaultMutableTreeNode = null):void
		{
			if (node == null)
			{
				node = theroot;
			}
			
			if (node.getUserObject() == dataStructurObject)
			{
				contentTreeModel.removeNodeFromParent(node);
				contentGridList.updateUI();
				return;
			}
			
			var count:uint = node.getChildCount();
			for (var i:int = 0; i < count; i++)
			{
				removeDataStructurObject(dataStructurObject, node.getChildAt(i) as DefaultMutableTreeNode);
			}
			
			//contentGridList.setRowHeight(24);
			//var node:DefaultMutableTreeNode = new ContentTreeNode(dso, dataIcon);
			//parentNode.append(node);
			//contentTreeModel.insertNodeInto(node, parentNode, parentNode.getChildCount());
		
		}
		
		public function addDataStructur2(dataStructur:DataStructur):DefaultMutableTreeNode
		{
			var parentNode:DefaultMutableTreeNode = currentNode /*nodes.get(folder.parentPath)*/;
			if (!parentNode)
				parentNode = theroot;
			
			/*var className:String = getQualifiedClassName(dataStructur);
			 var dataClass:Class = getDefinitionByName(className) as Class;*/
			
			var editor:BaseDataStructurProcessor = dataTypesAndEditors.get(dataStructur.dataType);
			var dataStructurClass:Class = editor.getDataStructurClass();
			var newDataStructur:DataStructur = new dataStructurClass();
			
			newDataStructur.dataName = getNewDataStructurName(parentNode, editor.getDataName()) /*getNewDataStructurName()*/;
			
			var node:DefaultMutableTreeNode = new ContentTreeNode(newDataStructur, editor.getModulIcon());
			
			//var node:DefaultMutableTreeNode = new DefaultMutableTreeNode(dataStructur);
			
			/*	if (dataStructur is ObjectContainer3DData)
			   {
			   node = new ObjectContainer3DNode(dataStructur);
			   }
			   else
			   {
			   node = new Object3DNode(dataStructur, null);
			   }
			 */
			parentNode.append(node);
			
			//contentTree.repaintAndRevalidate();
			
			contentTreeModel.insertNodeInto(node, parentNode, parentNode.getChildCount());
			return node;
		}
		
		public function addDataStructur3(dataStructur:DataStructur):void
		{
			var parentNode:DefaultMutableTreeNode = currentNode /*nodes.get(folder.parentPath)*/;
			if (!parentNode)
				parentNode = theroot;
			
			var className:String = getQualifiedClassName(dataStructur);
			var dataClass:Class = getDefinitionByName(className) as Class;
			
			var editor:BaseDataStructurProcessor = datasAndEditors.get(dataClass);
			//var dataStructurClass:Class = editor.getDataStructurClass();
			//var dataStructur:DataStructur = new dataStructurClass();
			
			//dataStructur.dataName = getNewDataStructurName(parentNode, editor.getDataName()) /*getNewDataStructurName()*/;
			//dataStructur.dataName = getNewDataStructurName(parentNode, dataStructur.relatedObject.name) /*getNewDataStructurName()*/;
			dataStructur.dataName = getNewDataStructurName(parentNode, dataStructur.dataName);
			
			//var node:DefaultMutableTreeNode = new ContentTreeNode(dataStructur, editor.getModulIcon());
			var node:DefaultMutableTreeNode = new ContentTreeNode(dataStructur, new TextIcon("LB"));
			
			//var node:DefaultMutableTreeNode = new DefaultMutableTreeNode(dataStructur);
			
			/*	if (dataStructur is ObjectContainer3DData)
			   {
			   node = new ObjectContainer3DNode(dataStructur);
			   }
			   else
			   {
			   node = new Object3DNode(dataStructur, null);
			   }
			 */
			
			parentNode.append(node);
			/*if (dataStructur.relatedObject is Container){
			   if ( ((parentNode as ContentTreeNode).getDataStructur().relatedObject as Container).getChildIndex(dataStructur.relatedObject as Container) == -1){
			   parentNode.append(node);
			   }
			   else{
			   parentNode = theroot;
			
			   }
			   //if((dataStructur.relatedObject as Container).
			   currentNode = node;
			 }*/
			
			//contentTree.repaintAndRevalidate();
			
			contentTreeModel.insertNodeInto(node, parentNode, parentNode.getChildCount());
		}
		
		/*	private function object3DBtnHandler(e:AWEvent):void
		   {
		   var dataStructurClass:Class = (e.currentTarget as JButton).metaData as Class;
		   addDataStructur(new dataStructurClass());
		 }*/
		
		protected function getNewDataStructurName(node:DefaultMutableTreeNode, dataName:String):String
		{
			var dsOrDSO:*; // DataStructur or DataStructurObject
			var childNode:TreeNode;
			var childrenCount:int = node.getChildCount();
			var dataStructurs:Array = [];
			
			for (var i:int = 0; i < childrenCount; i++)
			{
				childNode = node.getChildAt(i);
				dsOrDSO = (childNode as DefaultMutableTreeNode).getUserObject();
				dataStructurs.push(dsOrDSO);
			}
			
			return ArrayNamesHelper.createNewOrdinalName(dataStructurs, "dataName", dataName)
			//return ArrayNamesHelper.createNewOrdinalName(dataStructurs, "dataContainerName", dataName)
		}
		
		private function setGameStudioModul(e:AWEvent):void
		{
			gtrace("mo");
		
			//theroot
		}
		
		//protected function 
		
		public function createContentGridList():void
		{
			contentGridList = new GridList(null, new GeneralGridListCellFactory(DataStructurGridListCell), 0, 1);
			contentGridList.setHGap(5);
			//contentGridList.setVGap(10);
			contentGridList.setTileWidth(64);
			contentGridList.setTileHeight(64);
			contentGridList.setSelectedIndex(0);
			
			contentGridListScP = new JScrollPane(contentGridList);
			contentGridListScP.setPreferredSize(new IntDimension(227, 300));
			contentGridListScP.setVerticalScrollBarPolicy(JScrollPane.SCROLLBAR_ALWAYS);
			contentGridListScP.setHorizontalScrollBarPolicy(JScrollPane.SCROLLBAR_NEVER);
			contentGridListScP.buttonMode = true;
		}
		
		
		private function contentTreeChange(e:AWEvent):void
		{
			gtrace("toString " + contentTreeModel.toString());
		}
		
		public function addActionListener(listener:Function, useCapture:Boolean = false, priority:int = 0, useWeakReference:Boolean = false):void
		{
			super.addEventListener(AWEvent.ACT, listener, useCapture, priority, useWeakReference);
		}
		
		public function removeActionListener(listener:Function):void
		{
			super.removeEventListener(AWEvent.ACT, listener);
		}
		
		/*public function setOwnerForm(ownerForm:Form):FormRow
		 {*/
		
		/*var form:Form = new Form();
		   var titleLabel:DataContainerTitleLabel = new DataContainerTitleLabel("Scene browser", new AssetIcon(new MESH_EDITOR_ICON, 20, 20), JLabel.CENTER);
		   form.addLeftHoldRow(0, titleLabel);
		
		   titleLabel.metaData = super;
		
		   form.addLeftHoldRow(0, super);
		 titleLabel.setRelatedComponent(form);*/
		
		//var modulFormRow:FormRow = ownerForm.addRow(super);
		//var modulFormRow:FormRow = ownerForm.addRow(new JLabel("sdafjkldsajfkldjslafkjdslkafjklsdajflkasdj"));
		/*	return modulFormRow;
		 }*/
		
		/* INTERFACE devoron.studio.core.IPropertiesPanelComponent */
		
		/*public function getDashboardComponent():Component
		   {
		   return this;
		 }*/
		//Studio.instance.addStudioComponent(
		override public function setOwnerContainer(ownerContainer:Container):void
		{
			//super.setOwnerContainer(ownerContainer);
			//ownerContainer.append(modulForm, BorderLayout.WEST);
			//ownerContainer.append(modulForm, StudioWorkspaceLayout.WEST);
			ownerContainer.append(modulForm, StudioWorkspaceLayout.EAST);
		}
		
		/* INTERFACE devoron.gameeditor.core.IPropertiesPanelComponent */
		
		/*public function getDashboardComponent():Component
		   {
		   return this;
		 }*/
		
		public function getDashboardMinimalComponent():Component
		{
			return new JToggleButton("ds");
		}
		
		public function gotoParentNode():void
		{
			var selectionPath:TreePath = contentTreeSelectionModel.getSelectionPath();
			if (!selectionPath)
				return;
			var node:DefaultMutableTreeNode = selectionPath.getLastPathComponent() as DefaultMutableTreeNode;
			var parentNode:DefaultMutableTreeNode = node.getParent() as DefaultMutableTreeNode;
			
			if (parentNode == null)
				return;
			
			contentTreeSelectionModel.setSelectionPath(new TreePath(parentNode.getPath()));
		}
		
		public function gotoRootNode():void
		{
			contentTreeSelectionModel.setSelectionPath(new TreePath(theroot.getPath()));
		}
		
		public function copySelectedNode():void
		{
			var selection:TreePath = contentTreeSelectionModel.getSelectionPath();
			if (selection == null)
				return;
			
			var node:DefaultMutableTreeNode = selection.getLastPathComponent() as DefaultMutableTreeNode;
			
			//var node:DefaultMutableTreeNode = theroot;
			//if (node == theroot)
			//return;
			
			var parentNode:DefaultMutableTreeNode = node.getParent() as DefaultMutableTreeNode;
			if (parentNode == null)
				parentNode = theroot;
			
			//if (parentNode != null)
			if (true)
			{
				// ------------------------ если данные, вложенные в узел являются DataStructur -----------------------
				var dataStructur:DataStructur = node.getUserObject() as DataStructur;
				if (dataStructur)
				{
					var newDataStructur:* = dataStructur.clone() /*as dataClass*/;
					newDataStructur.dataName = getNewDataStructurName(parentNode, newDataStructur.dataName + "_copy");
					
					var newNode:DefaultMutableTreeNode;
					
					var editor:BaseDataStructurProcessor = datasAndEditors.get(dataStructur.dataType);
					newNode = new ContentTreeNode(newDataStructur, editor.getModulIcon());
					
					contentTreeModel.insertNodeInto(newNode, parentNode, parentNode.getChildCount());
					
					if (newDataStructur.dataType in containerTypes)
					{
						fillContainerNode(node, newNode);
					}
					
					// если при копировании должны быть созданы связанные объекты,
					// то создаётся новый объект связи или новая DataStructur добавляется в 
					// уже существующий, к которому прикреплена исходная DataStructur
					// это происходит один раз, но сложность в том, что нужно перебрать все UIDs
					// во всех массивах DataStructur каждой DataStructursBinding
					// как проще - хз. Только если вести отдельно HashMap, в котором есть
					// uid: binding
					if (copyMode == "binded_objects")
					{
						//if(!isBindingExists(dataStructur))
						var binding:DataStructursBinding = uidsAndBindings.get(dataStructur.uid);
						if (binding)
							binding.addDataStructur(newDataStructur);
						else
							createBinding(dataStructur, newDataStructur);
					}
					
					//contentGridList.setSelectionPath(new TreePath(newNode.getPath()));
				}
				
				// ------------------------ если данные, вложенные в узел являются DataStructurObject -----------------------
				//var color:ColorMaterialForm = new ColorMaterialForm();
				
				var dataStructurObject:DataStructurObject = node.getUserObject() as DataStructurObject;
				//var dataStructurObject:DataStructurObject = color.collectDataFromContainer() as DataStructurObject;
				if (dataStructurObject)
				{
					var newDataStructurObject:DataStructurObject = dataStructurObject.clone() as DataStructurObject;
					//newDataStructurObject.dataName = getNewDataStructurName(parentNode, newDataStructurObject.dataName + "_copy");
					newDataStructurObject.dataName = getNewDataStructurName(node, newDataStructurObject.dataName + "_copy");
					
					var newNode:DefaultMutableTreeNode;
					
					/*var className:String = getQualifiedClassName(dataStructur);
					   var dataClass:Class = getDefinitionByName(className) as Class;
					 var editor:BaseEditor = datasAndEditors.get(dataClass);*/
					
					newNode = new ContentTreeNode(newDataStructurObject);
					
					contentTreeModel.insertNodeInto(newNode, parentNode, parentNode.getChildCount());
					
					if (newDataStructurObject.dataType in containerTypes)
					{
						fillContainerNode(node, newNode);
					}
					
					//contentGridList.setSelectionPath(new TreePath(newNode.getPath()));
				}
				
			}
		}
		
		private function removeSelectedNode():void
		{
			var selection:TreePath = contentTreeSelectionModel.getSelectionPath();
			if (selection == null)
				return;
			
			var node:DefaultMutableTreeNode = selection.getLastPathComponent() as DefaultMutableTreeNode;
			
			if (node == theroot)
				return;
			
			if (node.getUserObject() as DataStructur)
				(node.getUserObject() as DataStructur).dispose();
			
			var parentNode:DefaultMutableTreeNode = node.getParent() as DefaultMutableTreeNode;
			
			if (parentNode != null)
			{
				var previousNode:DefaultMutableTreeNode = node.getPreviousNode();
				if (previousNode != null)
				{
					contentTreeSelectionModel.setSelectionPath(new TreePath(previousNode.getPath()));
				}
				else
				{
					var nexNode:DefaultMutableTreeNode = node.getNextNode();
					if (nexNode != null)
					{
						contentTreeSelectionModel.setSelectionPath(new TreePath(nexNode.getPath()));
					}
				}
			}
			
			contentTreeModel.removeNodeFromParent(node);
		}
		
		protected function setCurrentDataStructur(ds:DataStructur):void
		{
			var editor:BaseDataStructurProcessor = datasAndEditors.get(ds.dataType);
			
			if (editor)
			{
				//Studio.instance.setCurrentModul(null);
				
				var modulComponents:* = editor.getModulComponents();
				
				// 
				ds.addSerializeObserver(editor);
				
				// полагаю, нужно удалять прежний SerializeObserver, когда закончена работа с формой
				
				//GameStudio.instance.
				//ds.addSerializeObserver(this);
				
				// установить модуль в GameStudio
				//Studio.instance.setCurrentModul(editor);
				var dataParametersObj:*;
				
				// пройтись по всем компонентам 
				for each (dataParametersObj in modulComponents)
				{
					// добавить каждый контейнер данных в структуру данных
					if (dataParametersObj is IDataContainer)
						ds.addDataContainer(dataParametersObj);
					// отдть каждому контейнеру структур данных структуру данных
					else if (dataParametersObj is IDataStructurContainer)
						dataParametersObj.setDataStructur(ds);
					// отдать каждому наблюдателю сериализации структуру данных	
					if (dataParametersObj is ISerializeObserver)
						ds.addSerializeObserver(dataParametersObj);
					
					//ISerializeObserver(dataParametersObj).setSerializedData(
					ds.addDataContainer(dataParametersObj);
					
				}
				
				// нужно раздать и собственным компонентам(например, SerializedDataMonitorTool
				for each (dataParametersObj in this.modulComponents)
				{
					if (dataParametersObj is ISerializeObserver)
						ds.addSerializeObserver(dataParametersObj);
				}
				
				ds.serializable = true;
				
					//if (dataStructur.relatedObject is Mesh)
					//((dataStructur.relatedObject as Mesh).material as ColorMaterial).addMethod(new OutlineMethod(0xDD7333, 3));
			}
		}
		
		//**************************************************** ♪ ОБРАБОТЧИКИ СОБЫТИЙ ***************************************		
		
		protected function gotoRootNodeBtnHandler(e:AWEvent):void
		{
			gotoRootNode();
		}
		
		protected function gotoParentNodeBtnHandler(e:AWEvent):void
		{
			gotoParentNode();
		}
		
		protected function contentTreeSelectionHandler(e:TreeSelectionEvent):void
		{
			var node:DefaultMutableTreeNode = e.getPath().getLastPathComponent() as DefaultMutableTreeNode;
			if (!node)
				return;
			
			var dsOrDSO:* = node.getUserObject()
			//gtrace("object " + object);
			
			if (node == theroot)
			{
				//objectContainer3DBtn.setEnabled(true);
				//addItemBtn.setEnabled(true);
				removeNodeBtn.setEnabled(false);
				copyNodeBtn.setEnabled(false);
			}
			//else if ((dsOrDSO is ObjectContainer3DData) || (dsOrDSO is ViewData))
			//{
				////objectContainer3DBtn.setEnabled(true);
				////addItemBtn.setEnabled(true);
				//removeNodeBtn.setEnabled(true);
				//copyNodeBtn.setEnabled(true);
			//}
			else
			{
				//objectContainer3DBtn.setEnabled(false);
				//addItemBtn.setEnabled(false);
				removeNodeBtn.setEnabled(true);
				copyNodeBtn.setEnabled(true);
			}
			
			currentNode = node;
			
			if (dsOrDSO is DataStructur)
			{
				setCurrentDataStructur(dsOrDSO);
			}
		
		}
		
		public static const UNICAL_OBJECTS:String = "unical_objects";
		public static const BINDED_OBJECTS:String = "binded_objects";
		public var copyMode:String = "binded_objects";
		private var bindings:HashMap = new HashMap();
		private var uidsAndBindings:HashMap = new HashMap();
		protected var topPanel:Container;
		
		protected function copyNodeBtnHandler(e:AWEvent):void
		{
			copySelectedNode();
		}
		
		private function createBinding(ds1:DataStructur, ds2:DataStructur):DataStructursBinding
		{
			var dsb:DataStructursBinding = new DataStructursBinding(ds1, ds2);
			uidsAndBindings.put(ds1.uid, dsb);
			uidsAndBindings.put(ds2.uid, dsb);
			return dsb;
		}
		
		private function fillContainerNode(source:DefaultMutableTreeNode, target:DefaultMutableTreeNode):void
		{
			var chidlrenCount:int = source.getChildCount();
			var parentNode:DefaultMutableTreeNode = target.getParent() as DefaultMutableTreeNode;
			
			for (var i:int = 0; i < chidlrenCount; i++)
			{
				var childNode:DefaultMutableTreeNode = source.getChildAt(i) as DefaultMutableTreeNode;
				
				// получить DataStructur потомка и клонировать её
				var dataStructur:DataStructur = childNode.getUserObject() as DataStructur;
				var newDataStructur:DataStructur = dataStructur.clone() as DataStructur;
				
				var newNode:DefaultMutableTreeNode;
				
				var className:String = getQualifiedClassName(dataStructur);
				var dataClass:Class = getDefinitionByName(className) as Class;
				var editor:BaseDataStructurProcessor = datasAndEditors.get(dataClass);
				
				newNode = new DefaultMutableTreeNode(newDataStructur);
				
				if (newDataStructur.dataType in containerTypes)
				{
					fillContainerNode(childNode, newNode);
				}
				
				contentTreeModel.insertNodeInto(newNode, target, target.getChildCount());
			}
		}
		
		protected function removeNodeBtnHandler(e:AWEvent):void
		{
			removeSelectedNode();
		}
		
		protected function selectContentViewListener(e:AWEvent):void
		{
			//editorsControlPanel.setVisible(false);
			var editor:BaseDataStructurProcessor = (editorsControlPanel.getSelectedValue() as BaseDataStructurProcessor);
			addDataStructur(editor.getDataStructurClass(), editor.getDataName(), editor.getModulIcon());
		}
		
		/**
		 *
		 * @exception Not support for type.
		 */
		public function addDataStructurByType(type:String):void
		{
			var editor:BaseDataStructurProcessor = dataTypesAndEditors.get(type);
			
			if (editor)
			{
				addDataStructur(editor.getDataStructurClass(), editor.getDataName(), editor.getModulIcon());
			}
			else
			{
				throw new Error("SceneBrowser not support for " + type);
			}
		}
		
		public function getParentsTypes():Array
		{
			return parentsTypes;
		}
		
		public function addDataStructur(dataStructurClass:Class, dataName:String, dataIcon:Icon):void
		{
			var dataStructur:DataStructur = new dataStructurClass();
			//contentTabbedPane.append
			
			/*var form:Form = new Form();
			form.setPreferredSize(new IntDimension(100, 100));
			form.setSize(new IntDimension(100, 100));
			
			var lb:JLabel = new JLabel("", dataIcon);
			form.addLeftHoldRow(0, lb);*/
			
				//contentGridList.appendTab(form, dataStructur.dataType /*, dataContainer.icon*/);
				(contentGridList.getModel() as VectorListModel).append({dataStructur:dataStructur, icon:dataIcon});
				
				
				/*var btn:JLabel = new JLabel("dataStructur.dataType");
				btn.setPreferredSize(new IntDimension(100, 18));
				btn.setSize(new IntDimension(100, 18));
				topPanel.appendAll(btn);*/
				//topPanel.repaintAndRevalidate();
				//gtrace(datasAndEditors);
			
		}
		
		public function addDataStructurTree(dataStructurClass:Class, dataName:String, dataIcon:Icon):void
		{
			var dataStructur:DataStructur = new dataStructurClass();
			
			var parentNode:DefaultMutableTreeNode; /*nodes.get(folder.parentPath)*/
			
			if (currentNode)
			{
				if ((currentNode as ContentTreeNode).getDataStructur().dataType == "objectcontainer3D")
				{
					parentNode = currentNode;
				}
				
				if ((currentNode as ContentTreeNode).getDataStructur().dataType == "view")
				{
					parentNode = currentNode;
				}
			}
			
			//var parentNode:DefaultMutableTreeNode = theroot /*nodes.get(folder.parentPath)*/;
			if (!parentNode)
				parentNode = theroot;
			
			dataStructur.dataName = getNewDataStructurName(parentNode, dataName) /*getNewDataStructurName()*/;
			
			var node:DefaultMutableTreeNode = new ContentTreeNode(dataStructur, dataIcon);
			parentNode.append(node);
			contentTreeModel.insertNodeInto(node, parentNode, parentNode.getChildCount());
			//contentGridList.setSelectionPath(new TreePath(node.getPath()));
		
			// создание структуры данных должно изменять историю
		}
		
		//**************************************************** ☼ СОЗДАНИЕ КОМПОНЕНТОВ ***************************************
		
		protected function createButton(text:String, listener:Function, toolTip:String = ""):JLabelButton
		{
			//var btn:JButton = new JButton(text);
			var btn:JLabelButton = new JLabelButton(text);
			btn.setPreferredWidth(20);
			btn.setForeground(new ASColor(0xFFFFFF, 0.14));
			btn.setRollOverColor(new ASColor(0XFFFFFF, 0.8));
			btn.setBackgroundDecorator(null);
			btn.setPreferredSize(new IntDimension(24, 24));
			btn.addActionListener(listener);
			btn.setToolTipText(toolTip);
			return btn;
		}
	
	}

}