package airdock
{
	import airdock.config.ContainerConfig;
	import airdock.config.DockConfig;
	import airdock.config.PanelConfig;
	import airdock.enums.ContainerSide;
	import airdock.enums.ContainerState;
	import airdock.enums.CrossDockingPolicy;
	import airdock.events.PanelContainerEvent;
	import airdock.events.PanelContainerStateEvent;
	import airdock.events.PropertyChangeEvent;
	import airdock.impl.strategies.DockHelperStrategy;
	import airdock.impl.strategies.ResizerStrategy;
	import airdock.interfaces.docking.IBasicDocker;
	import airdock.interfaces.docking.IContainer;
	import airdock.interfaces.docking.ICustomizableDocker;
	import airdock.interfaces.docking.IDockFormat;
	import airdock.interfaces.docking.IPanel;
	import airdock.interfaces.docking.ITreeResolver;
	import airdock.interfaces.factories.IContainerFactory;
	import airdock.interfaces.factories.IPanelFactory;
	import airdock.interfaces.factories.IPanelListFactory;
	import airdock.interfaces.strategies.IDockerStrategy;
	import airdock.interfaces.strategies.IThumbnailStrategy;
	import airdock.interfaces.ui.IDockHelper;
	import airdock.interfaces.ui.IPanelList;
	import airdock.interfaces.ui.IResizer;
	import airdock.util.IDisposable;
	import airdock.util.PropertyChangeProxy;
	import flash.desktop.Clipboard;
	import flash.desktop.ClipboardTransferMode;
	import flash.desktop.NativeApplication;
	import flash.desktop.NativeDragActions;
	import flash.desktop.NativeDragManager;
	import flash.desktop.NativeDragOptions;
	import flash.display.BitmapData;
	import flash.display.DisplayObject;
	import flash.display.DisplayObjectContainer;
	import flash.display.NativeWindow;
	import flash.display.NativeWindowInitOptions;
	import flash.display.Stage;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.errors.IllegalOperationError;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.events.IEventDispatcher;
	import flash.events.MouseEvent;
	import flash.events.NativeDragEvent;
	import flash.events.NativeWindowBoundsEvent;
	import flash.geom.Point;
	import flash.utils.Dictionary;
	
	/**
	 * Dispatched whenever a panel is about to be added to, or removed from a container.
	 * Can be canceled to prevent default action.
	 * @eventType	airdock.events.PanelContainerStateEvent.VISIBILITY_TOGGLING
	 */
	[Event(name="pcPanelVisibilityToggling", type="airdock.events.PanelContainerStateEvent")]
	
	/**
	 * Dispatched whenever a panel is either added to a container, or when it is removed from its container.
	 * This is always preceded by a cancelable visibilityToggling event.
	 * @eventType	airdock.events.PanelContainerStateEvent.VISIBILITY_TOGGLED
	 */
	[Event(name="pcPanelVisibilityToggled", type="airdock.events.PanelContainerStateEvent")]
	
	
	/**
	 * Dispatched whenever a panel is moved to its parked container (docked), or when it is moved into another container which is not its own parked container (integrated).
	 */
	[Event(name="pcPanelStateToggled", type="airdock.events.PanelContainerStateEvent")]
	
	/**
	 * Dispatched whenever an IContainer instance is about to be created by the current Docker, using the IContainerFactory instance available to it.
	 * Can be canceled to prevent default action.
	 */
	[Event(name="pcContainerCreating", type="airdock.events.PanelContainerEvent")]
	
	/**
	 * Dispatched when an IContainer instance has been created by the current Docker using the IContainerFactory instance available to it.
	 * However, if it has been created via the createContainer() method, then this is dispatched before the function returns.
	 * This can then be used to customize or apply other operations on the container before it is actually used.
	 */
	[Event(name="pcContainerCreated", type="airdock.events.PanelContainerEvent")]
	
	/**
	 * The constant used to define a removed event.
	 * Is dispatched whenever a container (which has requested to be removed) has been removed from its parent container.
	 * Containers which are removed from their parent containers (and are not parked) are unreachable and can be safely disposed of.
	 */
	[Event(name="pcContainerRemoved", type="airdock.events.PanelContainerEvent")]
	
	/**
	 * Implementation of ICustomizableDocker (and by extension, IBasicDocker) which manages the main docking panels mechanism.
	 * 
	 * @author	Gimmick
	 * @see	airdock.interfaces.docking.IBasicDocker
	 * @see	airdock.interfaces.docking.ICustomizableDocker
	 */
	public final class AIRDock implements ICustomizableDocker, IDisposable
	{
		private static const COLLECT:Boolean = true;
		
		private static const FORWARD:Boolean = false;
		/**
		 * The list of allowed NativeDragActions for docking.
		 * Currently, only NativeDragActions.MOVE is allowed.
		 */
		private const cl_allowedDragActions:NativeDragOptions = new NativeDragOptions();
		/**
		 * The list of listener types added to containers registered by the Docker instance.
		 * Used to determine whether a container has been setup by the Docker instance or not.
		 */
		private const vec_allContainerListeners:Vector.<String> = new <String>
		[
			Event.REMOVED, Event.ADDED, MouseEvent.MOUSE_MOVE, PanelContainerEvent.CONTAINER_REMOVE_REQUESTED,
			PanelContainerEvent.STATE_TOGGLE_REQUESTED, PanelContainerEvent.CONTAINER_CREATING,
			PanelContainerEvent.CONTAINER_CREATED, PanelContainerEvent.SETUP_REQUESTED,
			PanelContainerEvent.DRAG_REQUESTED, PanelContainerEvent.PANEL_ADDED
		];
		/**
		 * Delegate event dispatcher instance.
		 */
		private var cl_dispatcher:IEventDispatcher;
		/**
		 * A Dictionary of all the containers local to this Docker instance.
		 */
		private var dct_containers:Dictionary;
		/**
		 * A Dictionary of all the NativeWindow instances created by this docker via the createWindow() method.
		 */
		private var dct_windows:Dictionary;
		/**
		 * The panel state information for each panel local to this Docker.
		 * Lists the previous (non-parked) container it was attached to, with its relative distance.
		 * @see PanelStateInformation
		 */
		private var dct_panelStateInfo:Dictionary;
		/**
		 * Is used to decide whether panels and containers are foreign to the current Docker instance or not.
		 * The key is more important than the value, since the mere existence of a key marks it as local.
		 * As a result, the value does not matter, but it is taken as the presence of listeners (i.e. whether listeners have been added)
		 * This is because listeners are registered for all local panels (to mark them as local.)
		 */
		private var dct_foreignCounter:Dictionary;
		/**
		 * The default IPanelFactory instance used to create panels by this Docker.
		 */
		private var cl_panelFactory:IPanelFactory;
		/**
		 * The default IPanelListFactory instance used to creaate panel lists for each panel local to this Docker.
		 */
		private var cl_panelListFactory:IPanelListFactory;
		/**
		 * The default IContainerFactory instance used to create containers by this Docker.
		 */
		private var cl_containerFactory:IContainerFactory;
		/**
		 * Temporary thumbnail strategy, used to draw thumbails for drag-dock operations.
		 * To be removed after implementation of DockStrategy related classes and interfaces.
		 */
		private var cl_thumbnailStrategy:IThumbnailStrategy;
		/**
		 * Dispatches events whenever a public property changes within this class, which can be intercepted and prevented.
		 * @see	airdock.util.PropertyChangeProxy
		 */
		private var cl_propertyChangeProxy:PropertyChangeProxy;
		/**
		 * The list of dock strategies which, taken together, let the Docker initiate, manage and terminate drag-docking operations.
		 * Currently, the <<implemented>> dock strategies are:
			* ResizerStrategy
				* The instance which handles when and how the resizer should be shown, and how it resizes containers.
				* @see airdock.impl.strategies.ResizerStrategy
			* DockHelperStrategy
				* The instance which handles when the dock helper should be shown, and how it interfaces with the rest of the docking system.
				* NOTE: Currently, it is structured in a way that precludes use of any other drag-docking method apart from the default NativeDrag method.
				* @see airdock.impl.strategies.DockHelperStrategy
		 */
		private var vec_dockStrategies:Vector.<IDockerStrategy>
		/**
		 * Creates a new AIRDock instance.
		 * However, creating it directly is discouraged, and it is recommended to use the static create() function instead.
		 * 
		 * @see airdock.AIRDock#create
		 */
		public function AIRDock() {
			init()
		}
		
		private function init():void 
		{
			dct_windows = new Dictionary()
			dct_containers = new Dictionary()
			dct_panelStateInfo = new Dictionary(true)
			dct_foreignCounter = new Dictionary(true)
			cl_dispatcher = new EventDispatcher(this)
			cl_propertyChangeProxy = new PropertyChangeProxy(this);
			cl_allowedDragActions.allowLink = cl_allowedDragActions.allowCopy = false;
			vec_dockStrategies = new <IDockerStrategy>[new DockHelperStrategy(), new ResizerStrategy()];	// define the strategies here
			crossDockingPolicy = CrossDockingPolicy.UNRESTRICTED;
			dragImageWidth = dragImageHeight = 1;
			
			addEventListener(PropertyChangeEvent.PROPERTY_CHANGED, applyPropertyChanges, false, 0, true);
			vec_dockStrategies.forEach(function setupStrategies(item:IDockerStrategy, index:int, array:Vector.<IDockerStrategy>):void {
				item.setup(this as IBasicDocker);
			}, this);
		}
		
		private function applyPropertyChanges(evt:PropertyChangeEvent):void 
		{
			if (evt.fieldName == "dockHelper")
			{
				const newHelper:IDockHelper = evt.newValue as IDockHelper
				const prevHelper:IDockHelper = evt.oldValue as IDockHelper
				if(prevHelper) {
					prevHelper.removeEventListener(NativeDragEvent.NATIVE_DRAG_DROP, preventDockOnIncomingCrossViolation)
				}
				if(newHelper) {
					newHelper.addEventListener(NativeDragEvent.NATIVE_DRAG_DROP, preventDockOnIncomingCrossViolation, false, 0, true)
				}
			}
		}
		
		private function startPanelContainerDragOnEvent(evt:PanelContainerEvent):void 
		{
			if (evt.isDefaultPrevented()) {
				return;
			}
			const panels:Vector.<IPanel> = evt.relatedPanels;
			const transferObject:Clipboard = new Clipboard();
			const container:IContainer = evt.relatedContainer || findCommonContainer(panels);	//the container is the target to be dragged as well
			transferObject.setData(dockFormat.panelFormat, panels, false);
			transferObject.setData(dockFormat.containerFormat, container, false);
			transferObject.setData(dockFormat.destinationFormat, new DragDockContainerInformation(), false);
			
			var proxyImage:BitmapData, offsetPoint:Point;
			if (cl_thumbnailStrategy)
			{
				cl_thumbnailStrategy.createThumbnail(container, new Point(dragImageWidth, dragImageHeight))
				proxyImage = cl_thumbnailStrategy.thumbnail
				offsetPoint = cl_thumbnailStrategy.offset
			}
			
			/**
			 * Used to determine the final position of the window of the panel or container being dragged.
			 * Without this, the position of the window at the end of a drag-dock operation will not be consistent with the mouse location.
			 */
			bindDragInformation(mainContainer, container.stage, container.mouseX / container.width, container.mouseY / container.height)
			NativeDragManager.doDrag(mainContainer, transferObject, proxyImage, offsetPoint, cl_allowedDragActions);
			if (cl_thumbnailStrategy) {
				cl_thumbnailStrategy.dispose();
			}
			evt.stopImmediatePropagation();
		}
		
		private function bindDragInformation(mainContainer:DisplayObjectContainer, stage:Stage, localX:Number, localY:Number):void
		{
			const thisObj:AIRDock = this;
			function finishDragDockOperation(evt:NativeDragEvent):void 
			{
				var allPanels:Object
				var window:NativeWindow;
				var container:IContainer 
				var dropContainerInfo:DragDockContainerInformation 
				var relatedContainer:IContainer, parkedContainer:IContainer;
				const clipBoard:Clipboard = evt.clipboard
				with (thisObj) 
				{
					if(!isCompatibleClipboard(clipBoard)) {
						return;
					}
					container = clipBoard.getData(dockFormat.containerFormat, ClipboardTransferMode.ORIGINAL_ONLY) as IContainer	|| findCommonContainer(allPanels)
					dropContainerInfo = clipBoard.getData(dockFormat.destinationFormat, ClipboardTransferMode.ORIGINAL_ONLY) as DragDockContainerInformation;
					//Object instead of Vector.<IPanel> because of mysterious compiler error here
					allPanels = Vector.<IPanel>(clipBoard.getData(dockFormat.panelFormat, ClipboardTransferMode.ORIGINAL_ONLY))
					if (!(allPanels && allPanels.length) && container) {
						allPanels = container.getPanels(false);
					}
					
					allPanels = extractDockablePanels(allPanels as Vector.<IPanel>)
					relatedContainer = dropContainerInfo.destinationContainer
					parkedContainer = treeResolver.findRootContainer(relatedContainer)	//check parked container for all non-dockable panels and prevent event
					if (evt.dropAction == NativeDragActions.NONE || (getContainerWindow(parkedContainer) && !extractDockablePanels(parkedContainer.getPanels(true)).length))
					{
						window = getContainerWindow(dockPanels(allPanels as Vector.<IPanel>, container))
						moveWindowTo(window, localX, localY, stage.nativeWindow.globalToScreen(new Point(evt.stageX, evt.stageY)));
						showPanels(allPanels as Vector.<IPanel>)
					}
					else if (relatedContainer) {
						movePanelsIntoContainer(extractOrderedPanelSideCodes(allPanels as Vector.<IPanel>, container), resolveContainerSideSequence(relatedContainer, dropContainerInfo.sideSequence));
					}
				}
				mainContainer.removeEventListener(NativeDragEvent.NATIVE_DRAG_COMPLETE, finishDragDockOperation)
			}
			
			mainContainer.addEventListener(NativeDragEvent.NATIVE_DRAG_COMPLETE, finishDragDockOperation)
		}
		
		private function preventDockIfInvalid(evt:PanelContainerEvent):void
		{
			if (!(extractDockablePanels(evt.relatedPanels || evt.relatedContainer.getPanels(false)).length)) {
				evt.preventDefault();	//prevent the drag-dock operation from starting if no panel is dockable
			}
		}
		
		private function removeContainerOnEvent(evt:NativeDragEvent):void
		{
			const clipBoard:Clipboard = evt.clipboard
			if (evt.isDefaultPrevented() || !isCompatibleClipboard(clipBoard)) {
				return;
			}
			const ORIGINAL_ONLY:String = ClipboardTransferMode.ORIGINAL_ONLY
			const panels:Vector.<IPanel> = clipBoard.getData(dockFormat.panelFormat, ORIGINAL_ONLY) as Vector.<IPanel>
			const container:IContainer = clipBoard.getData(dockFormat.containerFormat, ORIGINAL_ONLY) as IContainer || findCommonContainer(panels)
			if (!violatesIncomingCrossPolicy(crossDockingPolicy, container)) {
				hideContainerPanels(panels, dockPanels(panels, container))	//remove panels only if the panel belongs to this Docker
			}
		}
		
		private function togglePanelStateOnEvent(evt:PanelContainerEvent):void 
		{
			const panels:Vector.<IPanel> = extractDockablePanels(evt.relatedPanels)
			if (evt.isDefaultPrevented() || !(panels && panels.length)) {
				return;
			}
			const container:IContainer = evt.relatedContainer || findCommonContainer(panels)
			const prevState:Boolean = getAuthoritativeContainerState(container)
			if (prevState == ContainerState.DOCKED) {
				integratePanels(panels, container);
			}
			else {
				dockPanels(panels, container)
			}
			
			showPanels(panels)
			dispatchEvent(new PanelContainerStateEvent(PanelContainerStateEvent.STATE_TOGGLED, panels, container, prevState, !prevState, false, false))
		}
		
		/**
		 * Finds and returns all dockable IPanel instances from the given vector of IPanel instances.
		 * @param	panels	The list of IPanel instances to get the dockable IPanel instances from.
		 * @return	A new vector of dockable IPanel instances from the supplied list.
		 */
		private function extractDockablePanels(panels:Vector.<IPanel>):Vector.<IPanel>
		{
			return panels && extractLocalPanels(panels).filter(function(item:IPanel, index:int, array:Vector.<IPanel>):Boolean {
				return item && item.dockable
			}, this);
		}
		
		/**
		 * Finds and returns all IPanel instances local to the Docker instance, from the given vector of IPanel instances.
		 * @param	panels	The list of IPanel instances to get the local IPanel instances from.
		 * @return	A new vector of IPanel instances local to the Docker, from the supplied list.
		 */
		private function extractLocalPanels(panels:Vector.<IPanel>):Vector.<IPanel>
		{
			return panels && panels.filter(function(item:IPanel, index:int, array:Vector.<IPanel>):Boolean {
				return item && !isForeignPanel(item);
			}, this);
		}
		
		private function moveWindowTo(window:NativeWindow, localX:Number, localY:Number, windowPoint:Point):void 
		{
			if (!(window && windowPoint) || isNaN(windowPoint.x) || isNaN(windowPoint.y) || isNaN(localX) || isNaN(localY)) {
				return;
			}
			const chromeOffset:Point = window.globalToScreen(new Point(localX * window.stage.stageWidth, localY * window.stage.stageHeight))
			window.x += windowPoint.x - chromeOffset.x;
			window.y += windowPoint.y - chromeOffset.y;
		}
		
		/**
		 * Performs a lazy initialization of the container from the given window, if it does not exist and should be created.
		 * @param	window	The window to lookup.
		 * @param	createIfNotExist	Creates a new container for the given window if this parameter is true and it does not exist; if false, it performs a simple lookup which may fail (i.e. return undefined)
		 * @return	An IContainer instance which is the parked container contained by the corresponding window.
		 * 			This is also a panel's parked container. To find out which panel's parked container this belongs to, use the getWindowPanel() method.
		 * @see	#getWindowPanel()
		 */
		private function getContainerFromWindow(window:NativeWindow, createIfNotExist:Boolean):IContainer
		{
			if (createIfNotExist && window && !(window in dct_containers))
			{
				var container:IContainer 
				const stage:Stage = window.stage
				const panel:IPanel = getWindowPanel(window)
				const defWidth:Number = panel.getDefaultWidth(), defHeight:Number = panel.getDefaultHeight()
				defaultContainerOptions.width = defWidth;
				defaultContainerOptions.height = defHeight;
				container = dct_containers[window] = createContainer(defaultContainerOptions)
				//container.removeEventListener(PanelContainerEvent.PANEL_ADDED, setRoot)
				container.containerState = ContainerState.DOCKED
				stage.addChild(container as DisplayObject)
				stage.stageHeight = defHeight
				stage.stageWidth = defWidth
			}
			return dct_containers[window]
		}
		
		/**
		 * Performs a lazy initialization of the window of the given panel if it should be created, or a simple lookup otherwise.
		 * @param	panel	The panel whose window should be retrieved.
		 * @param	createIfNotExist	Creates the window if this parameter is true, and the window does not yet exist.
		 * 								If this parameter is false, it performs a simple lookup which may fail (i.e. return undefined)
		 * @return	A NativeWindow which contains the panel's parked container, and by extension, the panel (when it is docked to its parked container.)
		 */
		private function getWindowFromPanel(panel:IPanel, createIfNotExist:Boolean):NativeWindow
		{
			if (!panel) {
				return null;
			}
			else if (!dct_windows[panel] && createIfNotExist) {
				dct_windows[panel] = createWindow(panel)
			}
			return dct_windows[panel] as NativeWindow
		}
		
		/**
		 * @inheritDoc
		 */
		public function getPanelWindow(panel:IPanel):NativeWindow {
			return getWindowFromPanel(panel, !isForeignPanel(panel))
		}
		
		/**
		 * @inheritDoc
		 */
		public function getContainerWindow(container:IContainer):NativeWindow
		{
			const tempContainer:IContainer = treeResolver.findRootContainer(container)
			for (var window:Object in dct_containers)
			{
				if (dct_containers[window] == tempContainer) {
					return window as NativeWindow;
				}
			}
			return null;
		}
		
		/**
		 * @inheritDoc
		 * Note: This does not initialize the container if it does not already exist.
		 */
		public function getWindowContainer(window:NativeWindow):IContainer {
			return getContainerFromWindow(window, false)
		}
		
		/**
		 * @inheritDoc
		 */
		public function getWindowPanel(window:NativeWindow):IPanel
		{
			for (var panel:Object in dct_windows)
			{
				if (dct_windows[panel] == window) {
					return panel as IPanel
				}
			}
			return null;
		}
		
		/**
		 * Performs a lazy initialization of the PanelStateInformation for the given panel.
		 * @param	panel	The panel to get the state information of.
		 * @return	The panel's state information. Creates it if it does not exist.
		 */
		private function getPanelStateInfo(panel:IPanel):PanelStateInformation {
			return dct_panelStateInfo[panel] ||= new PanelStateInformation()
		}
		
		private function addContainerListeners(container:IContainer):void
		{
			container.addEventListener(Event.REMOVED, addContainerListenersOnUnlink, false, 0, true)
			container.addEventListener(Event.ADDED, removeContainerListenersOnLink, false, 0, true)
			container.addEventListener(PanelContainerEvent.PANEL_REMOVED, setRoot, false, 0, true)
			container.addEventListener(PanelContainerEvent.DRAG_REQUESTED, preventDockIfInvalid, false, 0, true)
			container.addEventListener(PanelContainerEvent.DRAG_REQUESTED, startPanelContainerDragOnEvent, false, 0, true)
			container.addEventListener(PanelContainerEvent.STATE_TOGGLE_REQUESTED, togglePanelStateOnEvent, false, 0, true)
			container.addEventListener(PanelContainerEvent.CONTAINER_REMOVE_REQUESTED, removeContainerIfEmpty, false, 0, true)
			container.addEventListener(PanelContainerEvent.CONTAINER_CREATED, registerContainerOnCreate, false, 0, true)
			container.addEventListener(PanelContainerEvent.CONTAINER_CREATING, createContainerOnEvent, false, 0, true)
			container.addEventListener(PanelContainerEvent.SETUP_REQUESTED, customizeContainerOnSetup, false, 0, true)
		}
		
		/**
		 * Used to pass an IContainer instance to the container which requests an IContainer instance.
		 * This is triggered after a PanelContainerEvent.CONTAINER_CREATING event is dispatched by the container, which signals a new container request.
		 * A response is sent in the form of a PanelContainerEvent.CONTAINER_CREATED event on the requesting container.
		 * @see	airdock.events.PanelContainerEvent
		 */
		private function createContainerOnEvent(evt:PanelContainerEvent):void
		{
			function redispatchOnContainer(innerEvt:PanelContainerEvent):void
			{
				evt.relatedContainer.dispatchEvent(innerEvt);
				removeEventListener(PanelContainerEvent.CONTAINER_CREATED, arguments.callee);
			}
			addEventListener(PanelContainerEvent.CONTAINER_CREATED, redispatchOnContainer, false, 0, true)
			createContainer(defaultContainerOptions);	//this function dispatches the CONTAINER_CREATED event indirectly
		}
		
		/**
		 * Used to prevent docking from a foreign panel or container into a local container (with respect to the current Docker instance.)
		 * This is triggered whenever the following crossDockingPolicy flags are used:
		 * * CrossDockingPolicy.REJECT_INCOMING
		 * * CrossDockingPolicy.INTERNAL_ONLY
		 * 
		 * Note that this function is called by the target container's Docker, not the source container's Docker, during a drag-dock operation.
		 * @see	airdock.enums.CrossDockingPolicy
		 */
		private function preventDockOnIncomingCrossViolation(evt:NativeDragEvent):void 
		{
			const clipBoard:Clipboard = evt.clipboard
			if(!isCompatibleClipboard(clipBoard)) {
				return;
			}
			const panels:Vector.<IPanel> = clipBoard.getData(dockFormat.panelFormat, ClipboardTransferMode.ORIGINAL_ONLY) as Vector.<IPanel>
			const container:IContainer = clipBoard.getData(dockFormat.containerFormat, ClipboardTransferMode.ORIGINAL_ONLY) as IContainer || findCommonContainer(panels)
			if (violatesIncomingCrossPolicy(crossDockingPolicy, container)) {
				evt.dropAction = NativeDragActions.NONE;	//set the drop action to NONE so that it won't commit the operation
			}
		}
		
		private function preventDockOnOutgoingCrossViolation(evt:NativeDragEvent):void
		{
			const clipBoard:Clipboard = evt.clipboard
			if(!isCompatibleClipboard(clipBoard)) {
				return;
			}
			const panels:Vector.<IPanel> = clipBoard.getData(dockFormat.panelFormat, ClipboardTransferMode.ORIGINAL_ONLY) as Vector.<IPanel>
			const container:IContainer = clipBoard.getData(dockFormat.containerFormat, ClipboardTransferMode.ORIGINAL_ONLY) as IContainer || findCommonContainer(panels)
			const dropContainerInfo:DragDockContainerInformation = clipBoard.getData(dockFormat.destinationFormat, ClipboardTransferMode.ORIGINAL_ONLY) as DragDockContainerInformation
			if (violatesOutgoingCrossPolicy(crossDockingPolicy, dropContainerInfo.destinationContainer)) {
				evt.dropAction = NativeDragActions.NONE;	//prevent the event and hence roll back docking process
			}
		}
		
		/**
		 * Adds the container to the list of containers created by this Docker instance, and marks it as local, i.e. non-foreign.
		 */
		private function registerContainerOnCreate(evt:PanelContainerEvent):void 
		{
			const container:IContainer = evt.relatedContainer
			if (!isForeignContainer(treeResolver.findRootContainer(evt.currentTarget as IContainer))) {
				dct_foreignCounter[container] = hasContainerListeners(container)
			}
		}
		
		/**
		 * Removes the listeners for a given container.
		 * Does not check whether it is a foreign container or not, prior to removal, since there is no effect if it is.
		 * Calling this function multiple times has no additional effect.
		 * @param	container	The container to remove listeners from.
		 */
		private function removeContainerListeners(container:IContainer):void
		{
			container.removeEventListener(PanelContainerEvent.CONTAINER_REMOVE_REQUESTED, removeContainerIfEmpty)
			container.removeEventListener(PanelContainerEvent.STATE_TOGGLE_REQUESTED, togglePanelStateOnEvent)
			container.removeEventListener(PanelContainerEvent.DRAG_REQUESTED, startPanelContainerDragOnEvent)
			container.removeEventListener(PanelContainerEvent.CONTAINER_CREATED, registerContainerOnCreate)
			container.removeEventListener(PanelContainerEvent.CONTAINER_CREATING, createContainerOnEvent)
			container.removeEventListener(PanelContainerEvent.SETUP_REQUESTED, customizeContainerOnSetup)
			container.removeEventListener(PanelContainerEvent.DRAG_REQUESTED, preventDockIfInvalid)
			container.removeEventListener(PanelContainerEvent.PANEL_ADDED, setRoot)
			container.removeEventListener(Event.ADDED, removeContainerListenersOnLink)
			container.removeEventListener(Event.REMOVED, addContainerListenersOnUnlink)
		}
		
		/**
		 * Removes a container whenever it dispatches a PanelContainerEvent.CONTAINER_REMOVE_REQUESTED event and fulfils the criteria for removal.
		 * A container can be removed if:
			* It has no panels in it, or
			* Any panels in it are about to be removed (e.g. as part of a REMOVED event)
		 * A PanelContainerEvent.CONTAINER_REMOVED event is dispatched after this event.
		 * However, if the container is a parked container, no event is dispatched; instead, its window is hidden.
		 */
		private function removeContainerIfEmpty(evt:PanelContainerEvent):void
		{
			if (evt.isDefaultPrevented()) {
				return;
			}
			const panels:Vector.<IPanel> = evt.relatedPanels
			const container:IContainer = evt.relatedContainer as IContainer || findCommonContainer(panels)
			const currentPanels:Vector.<IPanel> = container.getPanels(false);
			const hasChildren:Boolean = panels.length < currentPanels.length && currentPanels.some(function getDisjointPanels(item:IPanel, index:int, array:Vector.<IPanel>):Boolean {
				return item && panels.indexOf(item) == -1;
			});
			
 			if (hasChildren) {
				return;	//has children, do not remove - either more than the panel being removed, or a different panel from that which is being removed
			}
			const rootContainer:IContainer = treeResolver.findRootContainer(container)
			const rootWindow:NativeWindow = getContainerWindow(rootContainer)
			if (container == rootContainer && rootWindow) {
				rootWindow.visible = false; //do not dispose of container; since it is a parked container, just hide it
			}
			else if(rootContainer.removeContainer(container)) {
				dispatchEvent(new PanelContainerEvent(PanelContainerEvent.CONTAINER_REMOVED, panels, container, false, false))	//not a parked container; can remove
			}
			clearContainerCustomizations(container)
		}
		
		/**
		 * Removes listeners when a free container instance becomes contained by another container.
		 * This is done because the parent containers (or other containers up the chain) have the same listeners.
		 * That is, only a rooted (i.e. free-floating) container should possess these listeners.
		 * 
		 * Listeners are not removed if the container is rooted (that is, if findRootContainer(container) == container)
		 */
		private function removeContainerListenersOnLink(evt:Event):void 
		{
			const target:IContainer = evt.target as IContainer
			const root:IContainer = treeResolver.findRootContainer(target)
			if (!(isForeignContainer(target) || root == target))
			{
				removeContainerListeners(target)
				dct_foreignCounter[target] = hasContainerListeners(target);
			}
		}
		
		/**
		 * Adds container listeners whenever a container is about to be removed.
		 * This is done because rooted (i.e. free-floating) containers need these listeners to function correctly.
		 * 
		 * Listeners are not added if the container already has them.
		 */
		private function addContainerListenersOnUnlink(evt:Event):void 
		{
			const target:IContainer = evt.target as IContainer
			if (target != evt.currentTarget && !isForeignContainer(target) && !dct_foreignCounter[target])
			{
				addContainerListeners(target);
				dct_foreignCounter[target] = hasContainerListeners(target);
			}
		}
		
		/**
		 * Checks if the supplied container has the container listeners added to it by the current Docker instance..
		 * @param	container
		 * @return
		 */
		private function hasContainerListeners(container:IContainer):Boolean
		{
			return container && vec_allContainerListeners.every(function hasListener(item:String, index:int, array:Vector.<String>):Boolean {
				return container.hasEventListener(item)
			})
		}
		
		/**
		 * Customizes the container when it dispatches a PanelContainerEvent.SETUP_REQUESTED event which has not been prevented.
		 * This is used to add or remove panel lists to containers.
		 * 
		 * Panel lists are added to containers if:
			* The container contains panels, and
			* It does not have any subcontainers.
		 * If it does not fulfil the above conditions, the panel list, if any, is removed from the container.
		 */
		private function customizeContainerOnSetup(evt:PanelContainerEvent):void
		{
			const container:IContainer = evt.relatedContainer || findCommonContainer(evt.relatedPanels)
			const rootContainer:IContainer = evt.currentTarget as IContainer
			if (!(evt.isDefaultPrevented() || isForeignContainer(rootContainer)))
			{
				/* Foreign container policy note:
					* Don't modify foreign container's containers, since that container's Docker will already have listeners for it
					* In effect, whenever a foreign container changes, the source Docker will add or remove its panelLists to the container.
				 */
				if (!container.hasSides && container.hasPanels(false)) {
					setupContainerCustomizations(container)
				}
				else {
					clearContainerCustomizations(container)
				}
			}
		}
		
		/**
		 * Strips all customizations from the given container.
		 * Currently, this is limited to the container's panelList and displayFilters.
		 * @param	container	The container to remove customizations from.
		 */
		private function clearContainerCustomizations(container:IContainer):void
		{
			container.panelList = null;
			//container.displayFilters = null;
		}
		
		/**
		 * Adds customizations to the given container.
		 * Currently, this is limited to adding a panelList to the container.
		 * @param	container	The container to add customizations to.
		 */
		private function setupContainerCustomizations(container:IContainer):void {
			container.panelList ||= cl_panelListFactory.createPanelList() as IPanelList
		}
		
		/**
		 * Shadows the destination container so that its window appears behind the source container's window.
		 * @param	sourceContainer	The source container to be shadowed.
		 * @param	destContainer	The destination container whose window will shadow the source container's window.
		 * 							A window which shadows another will be located behind the shadowing window and possess the same bounds as the shadowing window.
		 */
		private function shadowContainer(sourceContainer:IContainer, destContainer:IContainer):void
		{
			const sourceWindow:NativeWindow = getContainerWindow(sourceContainer)
			const destWindow:NativeWindow = getContainerWindow(destContainer)
			if (sourceWindow && destWindow)
			{
				destWindow.bounds = sourceWindow.bounds;
				destContainer.width = destWindow.stage.stageWidth;		//manually resize container
				destContainer.height = destWindow.stage.stageHeight;	//since no resize event dispatched in window
				destWindow.visible = sourceWindow.visible;
				destWindow.orderInBackOf(sourceWindow);
			}
		}
		
		/**
		 * @inheritDoc
		 */
		public function addPanelToSideSequence(panel:IPanel, container:IContainer, sideCode:String):IContainer
		{
			if(!(panel && container)) {
				return null;
			}
			const prevContainer:IContainer = treeResolver.findParentContainer(panel as DisplayObject);
			const currContainer:IContainer = resolveContainerSideSequence(container, sideCode);
			if (prevContainer)
			{
				if(prevContainer == currContainer) {
					return currContainer;
				}
				prevContainer.removePanel(panel);
			}
			return currContainer.addToSide(ContainerSide.FILL, panel);
		}
		
		/**
		 * Returns a list of panels which are sorted based on their depth with respect to the root container supplied.
		 * @param	panels	The list of panels to be sorted based on depth order.
		 * @param	rootContainer	The root container on which the panel depth order is based upon.
		 * @return	A Vector of PanelSideSequence instances (a key-value pair), where the key is the panel and the value is the side code.
		 * 			If no rootContainer is specified, the value in each pair is the default value returned by the Docker's treeResolver's serializeCode() method - usually null.
		 */
		private function extractOrderedPanelSideCodes(panels:Vector.<IPanel>, rootContainer:IContainer):Vector.<PanelSideSequence>
		{
			if (!panels) {
				return null;
			}
			const sides:Vector.<PanelSideSequence> = new Vector.<PanelSideSequence>();
			panels.forEach(function extractSideCodes(item:IPanel, index:int, array:Vector.<IPanel>):void {
				sides.push(new PanelSideSequence(item, treeResolver.serializeCode(rootContainer, item as DisplayObject)))
			}, this);
			
			return sides.sort(function deeperLevels(pairA:PanelSideSequence, pairB:PanelSideSequence):int {	//sort side sequences according to increasing length
				return int(pairA.sideSequence && pairB.sideSequence && pairA.sideSequence.length - pairB.sideSequence.length) || 0;
			});
		}
		
		private function movePanelsIntoContainer(panelPairs:Vector.<PanelSideSequence>, newRoot:IContainer):void
		{
			if (!(newRoot && panelPairs)) {
				return;
			}
			
			panelPairs.forEach(function preserveSideOnDock(item:PanelSideSequence, index:int, array:Vector.<PanelSideSequence>):void
			{
				if (item) {
					addPanelToSideSequence(item.panel, newRoot, item.sideSequence);	//re-add to same position; note this approach means they will not be part of the same container
				}
			});
		}
		
		private function renameWindow(evt:PropertyChangeEvent):void
		{
			if (evt.fieldName == "panelName")
			{
				const window:NativeWindow = getWindowFromPanel(evt.currentTarget as IPanel, false);	//false since plain lookup
				if (window) {
					window.title = evt.newValue as String;
				}
			}
		}
		
		private function resizeContainerOnEvent(evt:NativeWindowBoundsEvent):void 
		{
			const window:NativeWindow = evt.currentTarget as NativeWindow
			const container:IContainer = getWindowContainer(window)
			if (container)
			{
				container.height = window.stage.stageHeight;
				container.width = window.stage.stageWidth;
			}
		}
		
		/**
		 * Updates the panelStateInformation object for the panel which has been added to a container, and all panels in containers deeper than it.
		 */
		private function setRoot(evt:PanelContainerEvent):void 
		{
			const panels:Vector.<IPanel> = evt.relatedPanels;
			const root:IContainer = treeResolver.findRootContainer(evt.relatedContainer);
			if(root.stage != mainContainer.stage) {
				return;
			}
			if (isForeignContainer(root) || getContainerWindow(root) || root.stage != mainContainer.stage) {
				return;
			}
			else panels.forEach(function setRootFor(panel:IPanel, index:int, array:Vector.<IPanel>):void
			{
				var currentCode:String = treeResolver.serializeCode(root, panel as DisplayObject)
				if (panel && currentCode && currentCode.length)
				{
					const panelStateInfo:PanelStateInformation = getPanelStateInfo(panel)
					if(panelStateInfo.masked) {
						return;
					}
					panelStateInfo.setIntegratedCode(currentCode, maskSideSequence(root, currentCode, 1));
					panelStateInfo.previousRoot = root;
				}
			}, this);
			
			const allStates:Dictionary = dct_panelStateInfo;
			for (var currPanel:Object in allStates)
			{
				var panelStateInfo:PanelStateInformation = allStates[currPanel] as PanelStateInformation;
				if (panels.indexOf(currPanel as IPanel) == -1 && treeResolver.findRootContainer(panelStateInfo.previousRoot) == root)
				{
					var currentCode:String = treeResolver.serializeCode(root, currPanel as DisplayObject) || panelStateInfo.maskedIntegratedCode
					if(panelStateInfo.masked) {
						continue
					}
					panelStateInfo.setIntegratedCode(currentCode, maskSideSequence(root, currentCode, 1));
					panelStateInfo.previousRoot = root;
				}
			}
		}
		
		private function addWindowListeners(window:NativeWindow):void
		{
			window.addEventListener(Event.CLOSING, hidePanelsOnWindowClose, false, 0, true)
			window.addEventListener(NativeWindowBoundsEvent.RESIZE, resizeContainerOnEvent, false, 0, true)
		}
		
		private function removeWindowListeners(window:NativeWindow):void
		{
			window.removeEventListener(NativeWindowBoundsEvent.RESIZE, resizeContainerOnEvent)
			window.removeEventListener(Event.CLOSING, hidePanelsOnWindowClose)
		}
		
		private function hidePanelsOnWindowClose(evt:Event):void 
		{
			const container:IContainer = getWindowContainer(evt.currentTarget as NativeWindow)
			if(!container) {
				return;	//do not prevent event if container doesn't exist - must be a "stray" window in that case
			}
			evt.preventDefault();	//prevent the window from closing automatically
			var hiddenPanels:Vector.<IPanel> = container.getPanels(true)
			if (dispatchEvent(new PanelContainerStateEvent(PanelContainerStateEvent.VISIBILITY_TOGGLING, hiddenPanels, container, ContainerState.VISIBLE, ContainerState.INVISIBLE, false, true)))
			{
				var newContainer:IContainer = hideContainerPanels(hiddenPanels, container)	//hide the window via hideContainerPanels()
				dispatchEvent(new PanelContainerStateEvent(PanelContainerStateEvent.VISIBILITY_TOGGLED, hiddenPanels, newContainer, ContainerState.VISIBLE, ContainerState.INVISIBLE, false, false));
			}
		}
		
		private function addPanelListeners(panel:IPanel):void {
			panel.addEventListener(PropertyChangeEvent.PROPERTY_CHANGED, renameWindow, false, 0, true)
		}
		
		private function removePanelListeners(panel:IPanel):void {
			panel.removeEventListener(PropertyChangeEvent.PROPERTY_CHANGED, renameWindow)
		}
		
		/**
		 * Returns the panel's parked container, and creates it if specified.
		 * Alias for getContainerFromWindow(getWindowFromPanel(panel))
		 * @param	panel	The panel to get the container of.
		 * @param	createIfNotExist	A Boolean indicating whether the container of the panel should be created if it does not exist.
		 * 								If true, both the window and the container are created if they do not exist.
		 * @return	The panel's parked container.
		 */
		private function getContainerFromPanel(panel:IPanel, createIfNotExist:Boolean):IContainer {
			return getContainerFromWindow(getWindowFromPanel(panel, createIfNotExist), createIfNotExist);
		}
		
		/**
		 * @inheritDoc
		 */
		public function getPanelContainer(panel:IPanel):IContainer {
			return getContainerFromPanel(panel, !isForeignPanel(panel))
		}
		
		/**
		 * @inheritDoc
		 */
		public function setupPanel(panel:IPanel):void
		{
			if (!((panel in dct_foreignCounter) && dct_foreignCounter[panel]))
			{
				addPanelListeners(panel)
				dct_foreignCounter[panel] = true;
			}
		}
		
		/**
		 * Sets up basic listeners for a window. Some listeners which are attached include, but are not limited to:
		 * * Automatically resizing any containers which may be present in the window's stage, and
		 * * Preventing the window from being disposed of when the user closes it.
		 * @param	window	The window which is to have listeners attached to it.
		 */
		private function setupWindow(window:NativeWindow):void {
			addWindowListeners(window)
		}
		
		/**
		 * Removes any listeners set up by this Docker instance for the given window, as dictated by the setupWindow() method.
		 * @param	window	The window whose listeners, previously added by this Docker instance, are to be removed from it.
		 */
		private function unhookWindow(window:NativeWindow):void {
			removeWindowListeners(window)
		}
		
		/**
		 * @inheritDoc
		 */
		public function unhookPanel(panel:IPanel):void
		{
			if (!((panel in dct_foreignCounter) && dct_foreignCounter[panel])) {
				return;
			}
			const window:NativeWindow = getWindowFromPanel(panel, false)
			if (window)
			{
				var container:IContainer = getContainerFromWindow(window, false)
				var remainingPanels:Vector.<IPanel> = (container && container.getPanels(true).filter(function excludePanel(item:IPanel, index:int, array:Vector.<IPanel>):Boolean {
					return item && item != panel;		//exclude panel from list of panels
				})) as Vector.<IPanel>;
				dockPanels(remainingPanels, container)	//move panels in this window to another window, since this will be closed
				unhookWindow(window)
				window.close()
			}
			delete dct_panelStateInfo[panel];
			delete dct_foreignCounter[panel];
			removePanelListeners(panel)
		}
		
		/**
		 * @inheritDoc
		 */
		public function createPanel(options:PanelConfig):IPanel
		{
			const panel:IPanel = cl_panelFactory.createPanel(options)
			setupPanel(panel)
			return panel
		}
		
		/**
		 * @inheritDoc
		 */
		public function createWindow(panel:IPanel):NativeWindow
		{
			if (!panel) {
				return null
			}
			else if (panel in dct_windows) {
				return dct_windows[panel] as NativeWindow
			}
			
			const options:NativeWindowInitOptions = defaultWindowOptions
			options.resizable = panel.resizable
			
			const window:NativeWindow = new NativeWindow(options)
			const stage:Stage = window.stage
			setupWindow(window)
			dct_windows[panel] = window
			window.title = panel.panelName
			stage.stageWidth = panel.width
			stage.stageHeight = panel.height
			stage.align = StageAlign.TOP_LEFT
			stage.scaleMode = StageScaleMode.NO_SCALE
			return window
		}
		
		/**
		 * @inheritDoc
		 */
		public function createContainer(options:ContainerConfig):IContainer
		{
			if (dispatchEvent(new PanelContainerEvent(PanelContainerEvent.CONTAINER_CREATING, null, null, false, true)))
			{
				const container:IContainer = cl_containerFactory.createContainer(options)
				container.panelList = cl_panelListFactory.createPanelList()
				addContainerListeners(container);
				dct_foreignCounter[container] = hasContainerListeners(container)
				dispatchEvent(new PanelContainerEvent(PanelContainerEvent.CONTAINER_CREATED, null, container, false, false));
			}
			return container
		}
		
		/**
		 * @inheritDoc
		 */
		public function setPanelFactory(panelFactory:IPanelFactory):void
		{
			if (!panelFactory) {
				throw new ArgumentError("Error: Argument panelFactory must be a non-null value.");
			}
			else {
				cl_panelFactory = panelFactory
			}
		}
		
		/**
		 * @inheritDoc
		 */
		public function setContainerFactory(containerFactory:IContainerFactory):void 
		{
			if (!containerFactory) {
				throw new ArgumentError("Error: Argument containerFactory must be a non-null value.");
			}
			else {
				cl_containerFactory = containerFactory
			}
		}
		
		/**
		 * @inheritDoc
		 */
		public function setPanelListFactory(panelListFactory:IPanelListFactory):void
		{
			cl_panelListFactory = panelListFactory
			for each(var container:IContainer in dct_containers) {
				container.panelList = (panelListFactory && panelListFactory.createPanelList()) as IPanelList
			}
		}
		
		/**
		 * @inheritDoc
		 */
		public function dockPanels(panels:Vector.<IPanel>, parentContainer:IContainer):IContainer
		{
			/* Procedure:
				* Get the (first panel in panels)'s parked container as firstContainer
				* Move all the panels into firstContainer
				* Special case: If some panels already exist in firstContainer, which are not in panels:
					* Move them to the container of their first panel:
						* Find the panels in firstContainer which are NOT in panels as preExistingPanels
						* Call dockPanels() recursively on preExistingPanels
			 * Note: If all the panels are removed from the container, the container must also be removed
				* This is handled by the removeContainerIfEmpty() method.
			 */
			var dockablePanels:Vector.<IPanel> = extractDockablePanels(panels);
			if(!(dockablePanels && dockablePanels.length)) {
				return null;
			}
			var panelPairs:Vector.<PanelSideSequence> = extractOrderedPanelSideCodes(dockablePanels, parentContainer);
			var firstContainer:IContainer = getPanelContainer(panelPairs[0].panel);	//first panel's parked container will have all the other panels moved into it
			var preExistingPanels:Vector.<IPanel> = firstContainer.getPanels(true).filter(function getPanelsDifference(item:IPanel, index:int, array:Vector.<IPanel>):Boolean {
				return item && dockablePanels.indexOf(item) == -1;	//exclude panels which are going to be moved to this container
			});
			if (parentContainer != firstContainer)
			{
				movePanelsIntoContainer(panelPairs, firstContainer)
				shadowContainer(parentContainer, firstContainer)
			}
			dockPanels(preExistingPanels, firstContainer)	//recursively empty the first panel's parked container by calling dockPanels() on it
			return firstContainer;
		}
		
		
		/**
		 * @inheritDoc
		 */
		public function integratePanels(panels:Vector.<IPanel>, parentContainer:IContainer):IContainer
		{
			/* Structurally similar to the dockPanels() method.
			 * The only difference is that this method does not care if the previous root is occupied.
			 * Procedure:
				* Get the (first panel in panels)'s previous root container as firstContainer
				* Move all the panels into firstContainer
			 * Note: If all the panels are removed from the container, the container must also be removed
				* This is handled by the removeContainerIfEmpty() method.
			 */
			const dockablePanels:Vector.<IPanel> = extractDockablePanels(panels);
			if(!(dockablePanels && dockablePanels.length)) {
				return null;
			}
			var panelPairs:Vector.<PanelSideSequence> = extractOrderedPanelSideCodes(dockablePanels, parentContainer);
			var topPanel:IPanel = panelPairs[0].panel
			var sideInfo:PanelStateInformation = getPanelStateInfo(topPanel);	//get top level panels
			var previousRoot:IContainer = sideInfo.previousRoot
			var firstContainer:IContainer, currPanel:IPanel;
			var newInfo:PanelStateInformation, info:PanelStateInformation 
			var maskedPanels:Vector.<PanelSideSequence> = new Vector.<PanelSideSequence>()//var maskedPanels:Vector.<IPanel> = new Vector.<IPanel>()
			var allStates:Dictionary = dct_panelStateInfo
			/**
			 * suppose you have two docked panels whose integrated codes are:
			 * BTLF, BTRF
			 * dock BTLF; it becomes:
			 * BTLF (docked), BTF (because no L anymore)
			 * then, dock BTF; it becomes:
			 * BTLF (docked), BTF (docked)
			 * integrate BTLF, but keep BTF docked; with masking:
			 * BT(L)F, BTF (docked)
			 * integrate BTF - now panels deeper than BTF have to get docked before BTF is inserted
			 * when integrating BTF, any masked panels are docked first and reintegrated
			 * lift mask on panels on 1) reintegration and 2) when container at mask level exists
			 * e.g. "BT(L)F" => "BTF"; if "BTF" exists already, then remove mask and use "BTLF" as we can afford to split
			 */
			
			//update masks
			sideInfo.setIntegratedCode(sideInfo.unmaskedIntegratedCode, maskSideSequence(previousRoot, sideInfo.unmaskedIntegratedCode, 1))
			
			for (var panel:Object in allStates)
			{
				currPanel = panel as IPanel
				info = allStates[currPanel];
				if (dockablePanels.indexOf(currPanel) == -1 && previousRoot == info.previousRoot)
				{
					//add to masked panel list only if it's integrated and is as deep or deeper than the panel to be integrated
					var currCode:String = treeResolver.serializeCode(previousRoot, currPanel as DisplayObject)
					var relativeLevel:int = ContainerSide.compareCode(currCode, sideInfo.maskedIntegratedCode)
					if (info.masked && relativeLevel == 0 || relativeLevel == 1) { //ContainerSide.compareCode(info.unmaskedIntegratedCode, sideInfo.unmaskedIntegratedCode) != -1) {
						maskedPanels.push(new PanelSideSequence(currPanel, info.unmaskedIntegratedCode)); //maskedPanels.push(currPanel);	//add if it's not docked, the panels share the same root and the current panel is deeper
					}
				}
			}
			/**
			 * If a panel is being integrated into a deeper container and its mask is longer because of the presence of 
			 * a deeper panel, then the deeper panel should not be included in the list of panels to reintegrate as it
			 * will result in a spiral of "dependent updates"
			 * 
			 * integrate RTLBF first
			 * E.g. RTLF and RTLBF; RTLBF has mask of RT(LB)F, and RTLF has mask of RT(L)F
			 * RT(LB)F , RT(L)F (docked)
			 * integrate RTLF next, this will cause RTLBF to be reintegrated as it is deeper than RTLF
			 * RT(LB)F , RTLF
			 * -> RTLBF, RTLF
			 * But RTF no longer exists (since RTLBF was acting as RT(LB)F = RTF)!
			 * -> New codes are:
			 * RTTF, RTBF (B may be omitted)
			 */
			
			panelPairs = panelPairs.map(function concatSideCodes(item:PanelSideSequence, index:int, array:Vector.<PanelSideSequence>):PanelSideSequence {
				return new PanelSideSequence(item.panel, sideInfo.maskedIntegratedCode + item.sideSequence)
			}).concat(maskedPanels).sort(function sortByLevel(itemA:PanelSideSequence, itemB:PanelSideSequence):int {
				return ContainerSide.compareCode(itemA.sideSequence, itemB.sideSequence)
			})
			
			for (var i:uint = 0, anchor:int = -1, j:uint = 0; i < panelPairs.length; ++i)
			{
				currPanel = panelPairs[i].panel;
				info = allStates[currPanel];
				var maskedSequence:String = maskSideSequence(info.previousRoot, info.unmaskedIntegratedCode, 1)
				if(maskedSequence == info.unmaskedIntegratedCode) {
					anchor = i;
				} else if(anchor != -1) {
					panelPairs[i] = new PanelSideSequence(currPanel, maskSideSequence(info.previousRoot, info.unmaskedIntegratedCode, ++j))
				}
			}
			
			var preemptedPanels:Vector.<IPanel> = new Vector.<IPanel>()			
			for each(var seq:PanelSideSequence in maskedPanels) {
				preemptedPanels.push(seq.panel)
			}
			hidePanels(preemptedPanels)
			movePanelsIntoContainer(panelPairs, sideInfo.previousRoot);
			return firstContainer;
		}
		
		private function resolveContainerSideSequence(container:IContainer, sideCode:String):IContainer
		{
			var currContainer:IContainer = container
			if (sideCode)
			{
				for (var i:uint = 0; i < sideCode.length; ++i) {
					currContainer = currContainer.fetchSide(sideCode.charAt(i));
				}
			}
			return currContainer
		}
		
		private function maskSideSequence(container:IContainer, sideCode:String, maxFetch:uint):String
		{
			var currContainer:IContainer = container
			sideCode ||= "";
			for (var i:uint = 0; i < sideCode.length; ++i)
			{
				currContainer = currContainer.getSide(sideCode.charAt(i));
				if (!currContainer) {
					break;
				}
			}
			return ContainerSide.stripFills(sideCode.slice(0, i + maxFetch)) + ContainerSide.FILL
		}
		
		/**
		 * Makes the panels supplied in the parameter visible, and dispatches a PanelContainerStateEvent if it was previously hidden.
		 * No event is dispatched if the panel supplied was already visible prior to calling the function.
		 * @inheritDoc
		 */
		public function showPanels(panels:Vector.<IPanel>):Vector.<IPanel>
		{
			const localPanels:Vector.<IPanel> = panels && panels.filter(function(item:IPanel, index:int, array:Vector.<IPanel>):Boolean {
				return item && !isForeignPanel(item);
			}, this);
			if(!dispatchEvent(new PanelContainerStateEvent(PanelContainerStateEvent.VISIBILITY_TOGGLING, localPanels, container, ContainerState.INVISIBLE, ContainerState.VISIBLE, false, true))) {
				return null;
			}
			const invisibleDockablePanels:Vector.<IPanel> = localPanels.filter(function isVisible(item:IPanel, index:int, array:Vector.<IPanel>):Boolean {
				return !isPanelVisible(item);
			}, this);
			
			var changeOccurred:Boolean;
			var panelsToShow:Vector.<IPanel> = localPanels;	//assume show for panels which are visible, but not active;
			if (invisibleDockablePanels && invisibleDockablePanels.length)
			{
				var container:IContainer = findCommonContainer(invisibleDockablePanels)
				if (container && isForeignContainer(container)) {
					return null;	//do not attempt to show panel for external/foreign containers
				}
				else 
				{
					const previousRoot:IContainer = getPanelStateInfo(invisibleDockablePanels[0]).previousRoot
					if (previousRoot && getAuthoritativeContainerState(container) == ContainerState.INTEGRATED) {
						changeOccurred = integratePanels(invisibleDockablePanels, previousRoot) != previousRoot
					}
					else
					{
						/* Panels are part of no container, or a parked container;
						 * move it to one of the panels' windows if required
						 * and show the window and the panel along with it */
						container ||= dockPanels(invisibleDockablePanels, null);
						
						const window:NativeWindow = getContainerWindow(container);
						changeOccurred = !window.visible;
						window.activate();
					}
				}
				panelsToShow = invisibleDockablePanels
			}
			const newParent:IContainer = findCommonContainer(panelsToShow);
			dispatchEvent(new PanelContainerStateEvent(PanelContainerStateEvent.VISIBILITY_TOGGLED, panelsToShow, newParent, ContainerState.INVISIBLE, ContainerState.VISIBLE, false, false));
			return panelsToShow.filter(function showAllPanels(item:IPanel, index:int, array:Vector.<IPanel>):Boolean {
				return newParent && newParent.showPanel(item);
			});
		}
		
		/**
		 * @inheritDoc
		 */
		public function hidePanels(panels:Vector.<IPanel>):Vector.<IPanel>
		{
			const hiddenPanels:Vector.<IPanel> = extractLocalPanels(panels).filter(function getVisible(item:IPanel, index:int, array:Vector.<IPanel>):Boolean {
				return isPanelVisible(item);
			});
			const container:IContainer = findCommonContainer(hiddenPanels);
			if (container && dispatchEvent(new PanelContainerStateEvent(PanelContainerStateEvent.VISIBILITY_TOGGLING, hiddenPanels, container, ContainerState.VISIBLE, ContainerState.INVISIBLE, false, true)))
			{
				//const newContainer:IContainer = hideContainerPanels(hiddenPanels, container)
				var window:NativeWindow = getContainerWindow(treeResolver.findRootContainer(container))
				var newContainer:IContainer;
				if (window)
				{
					window.visible = false
					newContainer = container;
				}
				else hiddenPanels.forEach(function removePanelsFromContainer(item:IPanel, index:int, array:Vector.<IPanel>):void {
					container.removePanel(item)
				});
				dispatchEvent(new PanelContainerStateEvent(PanelContainerStateEvent.VISIBILITY_TOGGLED, hiddenPanels, newContainer, ContainerState.VISIBLE, ContainerState.INVISIBLE, false, false));
				return hiddenPanels;
			}
			return null;
		}
		
		/**
		 * Moves all the panels to the parked container of each panel in the list until a parked container whose window is invisible is reached.
		 * If all windows are visible, such that no invisible container is found, null is returned, indicating failure.
		 * 
		 * @param	panels		The panels to move to an invisible container.
		 * @param	container	The current parent container of the panels.
		 * @return	The new container to which the panels have been moved to.
		 */
		private function hideContainerPanels(panels:Vector.<IPanel>, container:IContainer):IContainer
		{
			var newContainer:IContainer = container;
			var rootWindow:NativeWindow = getContainerWindow(treeResolver.findRootContainer(newContainer))
			if(rootWindow) {
				rootWindow.visible = false;	//if they all belong to a parked container window, hide the window
			}
			else if(panels && panels.length)
			{
				var cyclicPanels:Vector.<IPanel> = panels.concat();
				panels.some(function moveToFirstInvisibleContainer(item:IPanel, index:int, array:Vector.<IPanel>):Boolean
				{
					//keep cycling panels for dockPanels() method until an invisible window is reached
					newContainer = dockPanels(cyclicPanels, newContainer);
					rootWindow = getContainerWindow(newContainer)
					cyclicPanels.push(cyclicPanels.shift())
					return rootWindow && !rootWindow.visible; 
				})
			}
			return newContainer
		}
		
		/**
		 * @inheritDoc
		 */
		public function isPanelVisible(panel:IPanel):Boolean
		{
			const parentContainer:IContainer = treeResolver.findParentContainer(panel as DisplayObject);
			const rootContainer:IContainer = treeResolver.findRootContainer(parentContainer);
			if (!rootContainer || isForeignContainer(rootContainer)) {
				return false;	//will also return false if panel is null
			}
			const window:NativeWindow = getContainerWindow(rootContainer);
			return (!window && panel.stage) || (window && window.visible);
		}
		
		/**
		 * @inheritDoc
		 */
		public function get dockHelper():IDockHelper {
			return cl_propertyChangeProxy.dockHelper as IDockHelper;
		}
		
		/**
		 * @inheritDoc
		 */
		public function set dockHelper(dockHelper:IDockHelper):void {
			cl_propertyChangeProxy.dockHelper = dockHelper;
		}
		
		/**
		 * @inheritDoc
		 */
		public function get resizeHelper():IResizer {
			return cl_propertyChangeProxy.resizeHelper as IResizer
		}
		
		/**
		 * @inheritDoc
		 */
		public function set resizeHelper(resizer:IResizer):void {
			cl_propertyChangeProxy.resizeHelper = resizer
		}
		
		/**
		 * @inheritDoc
		 */
		public function set crossDockingPolicy(policyFlags:int):void {
			cl_propertyChangeProxy.crossDockingPolicy = policyFlags
		}
		
		/**
		 * @inheritDoc
		 */
		public function get crossDockingPolicy():int {
			return int(cl_propertyChangeProxy.crossDockingPolicy)
		}
		
		/**
		 * @inheritDoc
		 */
		public function get mainContainer():DisplayObjectContainer {
			return cl_propertyChangeProxy.mainContainer as DisplayObjectContainer
		}
		
		/**
		 * @inheritDoc
		 */
		public function get thumbnailStrategy():IThumbnailStrategy {
			return cl_thumbnailStrategy;
		}
		
		/**
		 * @inheritDoc
		 */
		public function set thumbnailStrategy(value:IThumbnailStrategy):void {
			cl_thumbnailStrategy = value;
		}
		
		/**
		 * @inheritDoc
		 */
		public function set mainContainer(container:DisplayObjectContainer):void
		{
			function setMainContainer(evt:PropertyChangeEvent):void
			{
				if (evt.fieldName == "mainContainer")
				{
					const prevContainer:DisplayObjectContainer = evt.oldValue as DisplayObjectContainer
					const container:DisplayObjectContainer = evt.newValue as DisplayObjectContainer
					if (prevContainer)
					{
						/**
						 * Remove previous container listeners before setting up the new container as the main.
						 * Note: Any drag-dock operations already in effect will run to completion, even if this property is changed during one.
						 */
						prevContainer.removeEventListener(NativeDragEvent.NATIVE_DRAG_START, removeContainerOnEvent)
						prevContainer.removeEventListener(NativeDragEvent.NATIVE_DRAG_COMPLETE, preventDockOnOutgoingCrossViolation)
					}
					
					if (container)
					{
						/**
						 * Docking process:
						 * 1) Check if the drag-dock operation can be started. If the panel is not dockable, stop.
						 * 2) Start the native drag via NativeDragManager.doDrag()
						 * 3) Remove the panel or container from its parent container.
						 * 3.5) Continually update the dragging coordinates for the window (if it ends up being docked)
						 * 4) Finish the docking operation by adding the panel or container to the target (NativeDragEvent.NATIVE_DRAG_COMPLETE)
						 * 5) Clean up - hide the dock helper, update the drag coordinates one last time, and if step 3 does not succeed, dock the container
						 * 
						 * Note: The priority for preventDockOnOutgoingCrossViolation must be higher (i.e. before) finishDragDockOperation
						 */
						container.addEventListener(NativeDragEvent.NATIVE_DRAG_START, removeContainerOnEvent, false, 0, true)
						container.addEventListener(NativeDragEvent.NATIVE_DRAG_COMPLETE, preventDockOnOutgoingCrossViolation, false, 0, true)
					}
				}
				removeEventListener(PropertyChangeEvent.PROPERTY_CHANGED, arguments.callee)
			}
			addEventListener(PropertyChangeEvent.PROPERTY_CHANGED, setMainContainer, false, 0, true)
			
			cl_propertyChangeProxy.mainContainer = container;
			removeEventListener(PropertyChangeEvent.PROPERTY_CHANGED, setMainContainer)
		}
		
		/**
		 * @inheritDoc
		 */
		public function get dragImageHeight():Number {
			return Number(cl_propertyChangeProxy.dragImageHeight)
		}
		
		/**
		 * @inheritDoc
		 */
		public function set dragImageHeight(value:Number):void {
			cl_propertyChangeProxy.dragImageHeight = value;
		}
		
		/**
		 * @inheritDoc
		 */
		public function get dragImageWidth():Number {
			return Number(cl_propertyChangeProxy.dragImageWidth)
		}
		
		/**
		 * @inheritDoc
		 */
		public function set dragImageWidth(value:Number):void {
			cl_propertyChangeProxy.dragImageWidth = value;
		}
		
		/**
		 * @inheritDoc
		 */
		public function get defaultWindowOptions():NativeWindowInitOptions {
			return cl_propertyChangeProxy.defaultWindowOptions as NativeWindowInitOptions;
		}
		
		/**
		 * @inheritDoc
		 */
		public function set defaultWindowOptions(value:NativeWindowInitOptions):void
		{
			if (!value) {
				throw new ArgumentError("Error: Option defaultWindowOptions must be a non-null value.")
			}
			else {
				cl_propertyChangeProxy.defaultWindowOptions = value
			}
		}
		
		/**
		 * @inheritDoc
		 */
		public function get defaultContainerOptions():ContainerConfig {
			return cl_propertyChangeProxy.defaultContainerOptions as ContainerConfig
		}
		
		/**
		 * @inheritDoc
		 */
		public function set defaultContainerOptions(value:ContainerConfig):void 
		{
			if (!value) {
				throw new ArgumentError("Error: Option defaultContainerOptions must be a non-null value.")
			}
			else {
				cl_propertyChangeProxy.defaultContainerOptions = value
			}
		}
		
		/**
		 * @inheritDoc
		 */
		public function get dockFormat():IDockFormat {
			return cl_propertyChangeProxy.dockFormat as IDockFormat;
		}
		
		/**
		 * @inheritDoc
		 */
		public function set dockFormat(value:IDockFormat):void 
		{
			if (!value) {
				throw new ArgumentError("Error: Option dockFormat must be a non-null value.")
			}
			else {
				cl_propertyChangeProxy.dockFormat = value
			}
		}
		
		/**
		 * @inheritDoc
		 */
		public function get treeResolver():ITreeResolver {
			return cl_propertyChangeProxy.treeResolver
		}
		
		/**
		 * @inheritDoc
		 */
		public function set treeResolver(value:ITreeResolver):void 
		{
			if (!value) {
				throw new ArgumentError("Error: Option treeResolver must be a non-null value.")
			}
			else {
				cl_propertyChangeProxy.treeResolver = value
			}
		}
		
		/**
		 * Disposes of all the windows and removes all listeners and other references of the panels registered to this Docker.
		 * Once this method is called, it is advised not to use the Docker instance again, and to create a new one instead.
		 * @inheritDoc
		 */
		public function dispose():void
		{
			mainContainer = null;
			for each(var window:NativeWindow in dct_windows) {
				window.close()
			}
			dct_windows = null;
			dct_containers = null;
			dragImageWidth = dragImageHeight = NaN;
			vec_dockStrategies.forEach(function disposeObject(item:IDockerStrategy, index:int, array:Vector.<IDockerStrategy>):void
			{
				if (item is IDisposable) {
					(item as IDisposable).dispose();
				}
			});
			setPanelListFactory(null);
			dockHelper = null;
		}
		
		/**
		 * @inheritDoc
		 */
		public function addEventListener(type:String, listener:Function, useCapture:Boolean = false, priority:int = 0, useWeakReference:Boolean = false):void {
			cl_dispatcher.addEventListener(type, listener, useCapture, priority, useWeakReference);
		}
		
		/**
		 * @inheritDoc
		 */
		public function dispatchEvent(event:Event):Boolean {
			return cl_dispatcher.dispatchEvent(event);
		}
		
		/**
		 * @inheritDoc
		 */
		public function hasEventListener(type:String):Boolean {
			return cl_dispatcher.hasEventListener(type);
		}
		
		/**
		 * @inheritDoc
		 */
		public function removeEventListener(type:String, listener:Function, useCapture:Boolean = false):void {
			cl_dispatcher.removeEventListener(type, listener, useCapture);
		}
		
		/**
		 * @inheritDoc
		 */
		public function willTrigger(type:String):Boolean {
			return cl_dispatcher.willTrigger(type);
		}
		
		[Inline]
		private function isForeignContainer(container:IContainer):Boolean {
			return !(container && (container in dct_foreignCounter))
		}
		
		[Inline]
		private function isForeignPanel(panel:IPanel):Boolean {
			return !(panel in dct_foreignCounter)
		}
		
		[Inline]
		private function isMatchingDockPolicy(crossDockingPolicy:int, flag:int):Boolean {
			return (crossDockingPolicy & flag) != 0;
		}
		
		
		private function isCompatibleClipboard(clipboard:Clipboard):Boolean {
			return clipboard.hasFormat(dockFormat.panelFormat) || clipboard.hasFormat(dockFormat.containerFormat)
		}
		
		[Inline]
		private function violatesIncomingCrossPolicy(crossDockingPolicy:int, container:IContainer):Boolean {
			return isMatchingDockPolicy(crossDockingPolicy, CrossDockingPolicy.REJECT_INCOMING) && isForeignContainer(container)
		}
		
		[Inline]
		private function violatesOutgoingCrossPolicy(crossDockingPolicy:int, container:IContainer):Boolean {
			return isMatchingDockPolicy(crossDockingPolicy, CrossDockingPolicy.PREVENT_OUTGOING) && isForeignContainer(container)
		}
		
		[Inline]
		private function findCommonContainer(panels:Vector.<IPanel>):IContainer
		{
			const displayObject:DisplayObject = treeResolver.findCommonParent(Vector.<DisplayObject>(panels))
			return displayObject as IContainer || treeResolver.findParentContainer(displayObject)
		}
		
		/**
		 * Gets the authoritative state of the container, by querying the root container's state.
		 * If the root container is a parked container, then it is most likely DOCKED; 
		 * otherwise, it is most likely INTEGRATED (assuming no changes have been made manually to the state)
		 * @param	container	The container to get the authoritative state of.
		 * @return	The authoritative state of the container.
		 * @see	airdock.enums.ContainerState
		 */
		[Inline]
		private function getAuthoritativeContainerState(container:IContainer):Boolean
		{
			const root:IContainer = treeResolver.findRootContainer(container)
			return root && root.containerState;
		}
		
		/**
		 * Checks whether AIRDock is supported on the target runtime or not.
		 * Use this method to determine whether AIRDock is supported on the target runtime before creating an instance via the create() method.
		 * However, in general, any system which supports both the NativeWindow and NativeDragManager class will support AIRDock as well.
		 * @see	#create()
		 */
		public static function get isSupported():Boolean {
			return NativeWindow.isSupported && NativeDragManager.isSupported;
		}
		
		/**
		 * Creates an AIRDock instance, based on the supplied configuration, if supported. To check whether it is supported, see the static isSupported() method.
		 * It is advised to use this method to create a new AIRDock instance rather than creating it via the new() operator.
		 * @param	config	A DockConfig instance representing the configuration options that must be used when creating the new AIRDock instance.
		 * @throws	ArgumentError If either the configuration is null, or any of the mainContainer, defaultWindowOptions, or treeResolver attributes are null in the configuration.
		 * @throws	IllegalOperationError If AIRDock is not supported on the target system. To check whether it is supported, see the static isSupported() method.
		 * @return	An AIRDock instance as an ICustomizableDocker.
		 * @see	#isSupported
		 */
		public static function create(config:DockConfig):ICustomizableDocker
		{
			if (!isSupported) {
				throw new IllegalOperationError("Error: AIRDock is not supported on the current system.");
			}
			else if (!(config && config.mainContainer && config.defaultWindowOptions && config.treeResolver))
			{
				const reason:Vector.<String> = new <String>["Invalid options:"]
				if (!config) {
					reason.push("Options must be non-null.")
				}
				else 
				{
					if (!config.mainContainer) {
						reason.push("Option mainContainer must be a non-null value.");
					}
					if (!config.defaultWindowOptions) {
						reason.push("Option defaultWindowOptions must be a non-null value.");
					}
					if (!config.treeResolver) {
						reason.push("Option treeResolver must be a non-null value.");
					}
				}
				throw new ArgumentError(reason.join("\n"))
			}
			const docker:AIRDock = new AIRDock()
			if (config.mainContainer.stage) {
				config.defaultWindowOptions.owner = config.mainContainer.stage.nativeWindow
			}
			docker.setPanelFactory(config.panelFactory)
			docker.setPanelListFactory(config.panelListFactory)
			docker.setContainerFactory(config.containerFactory)
			docker.defaultWindowOptions = config.defaultWindowOptions
			docker.defaultContainerOptions = config.defaultContainerOptions
			docker.crossDockingPolicy = config.crossDockingPolicy
			docker.thumbnailStrategy = config.thumbnailStrategy
			docker.mainContainer = config.mainContainer
			docker.treeResolver = config.treeResolver
			docker.resizeHelper = config.resizeHelper
			docker.dockFormat = config.dockFormat
			docker.dockHelper = config.dockHelper
			if (!(isNaN(config.dragImageWidth) || isNaN(config.dragImageHeight)))
			{
				docker.dragImageHeight = config.dragImageHeight
				docker.dragImageWidth = config.dragImageWidth
			}
			return docker as ICustomizableDocker
		}
	}
}

import airdock.enums.ContainerSide;
import airdock.interfaces.docking.IContainer;
import airdock.interfaces.docking.IDragDockFormat;
import airdock.interfaces.docking.IPanel;
internal class PanelStateInformation
{
	private var plc_prevRoot:IContainer;
	private var str_maskedIntegratedCode:String;
	private var str_unmaskedIntegratedCode:String;
	public function PanelStateInformation() { }
	
	public function get previousRoot():IContainer {
		return plc_prevRoot; 
	}
	
	public function set previousRoot(value:IContainer):void {
		plc_prevRoot = value;
	}
	
	public function setIntegratedCode(unmasked:String, masked:String):void
	{
		str_unmaskedIntegratedCode = unmasked;
		str_maskedIntegratedCode = masked;
	}
	
	public function get masked():Boolean {
		return ContainerSide.stripFills(maskedIntegratedCode) != ContainerSide.stripFills(unmaskedIntegratedCode)
	}
	
	public function get maskedIntegratedCode():String {
		return str_maskedIntegratedCode;
	}
	
	public function get unmaskedIntegratedCode():String {
		return str_unmaskedIntegratedCode;
	}
}

/**
 * The class containing information about the container which is to receive a panel or container near the end of a drag-dock operation.
 */
internal class DragDockContainerInformation implements IDragDockFormat
{
	private var str_sideSequence:String
	private var plc_destination:IContainer
	public function DragDockContainerInformation() { }
	
	public function get destinationContainer():IContainer {
		return plc_destination
	}
	
	public function set destinationContainer(dropTarget:IContainer):void {
		plc_destination = dropTarget
	}
	
	public function get sideSequence():String {
		return str_sideSequence;
	}
	
	public function set sideSequence(value:String):void {
		str_sideSequence = value;
	}
}

internal class PanelSideSequence
{
	private var pl_panel:IPanel
	private var str_sideSequence:String
	public function PanelSideSequence(panel:IPanel, sideSequence:String)
	{
		pl_panel = panel;
		str_sideSequence = sideSequence
	}
	
	public function get sideSequence():String {
		return str_sideSequence;
	}
	
	public function get panel():IPanel {
		return pl_panel;
	}
}