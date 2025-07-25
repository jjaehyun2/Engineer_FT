// Copyright (c) 2012, Unwrong Ltd. http://www.unwrong.com
// All rights reserved. 

package cadetEditor2DFlash.tools
{
	import cadet.core.IComponentContainer;
	import cadet.util.ComponentUtil;
	
	import cadet2D.components.skins.IRenderable;
	
	import cadetEditor.assets.CadetEditorIcons;
	import cadetEditor.contexts.ICadetEditorContext;
	import cadetEditor.entities.ToolFactory;
	import cadetEditor.tools.ITool;
	import cadetEditor.util.DragDetector;
	
	import cadetEditor2D.contexts.ICadetEditorContext2D;
	import cadetEditor2D.controllers.DragItemsController;
	import cadetEditor2D.controllers.IDragSelectionController;
	import cadetEditor2D.events.PickingManagerEvent;
	import cadetEditor2D.util.SelectionUtil;
	
	import cadetEditor2DFlash.controllers.DragSelectController;
	
	import flash.events.Event;
	
	import flox.app.core.contexts.IContext;
	import flox.app.operations.ChangePropertyOperation;
	import flox.app.util.ArrayUtil;
	import flox.app.util.IntrospectionUtil;
	import flox.editor.FloxEditor;
	
	public class SelectionTool extends CadetEditorTool2D implements ITool
	{
		public static function getFactory():ToolFactory
		{
			return new ToolFactory( ICadetEditorContext, SelectionTool, "Selection Tool", CadetEditorIcons.SelectionTool );
		}
		
		// State
		protected var ignoreNextMouseUp				:Boolean = false;
		protected var ignoreDragDetect				:Boolean = false;
		protected var allowMultipleSelection		:Boolean = true;
		protected var allowDrag						:Boolean = true;
		protected var allowDragSelect				:Boolean = true;
		
		private var shiftKeyDown					:Boolean = false;
		private var pressedSkin						:IRenderable;
		
		// Controllers
		private var dragItemsController				:DragItemsController;
		private var dragSelectController			:IDragSelectionController;
		
		/**
		 * Constructor 
		 * 
		 */		
		public function SelectionTool()
		{
			
		}
		
		override public function init( context:IContext ):void
		{
			super.init( context );
			
			dragItemsController = new DragItemsController( this.context, this );
			dragSelectController = new DragSelectController( this.context );
		}
			
		override public function dispose():void
		{
			dragItemsController.dispose()
			dragItemsController = null
			dragSelectController.dispose()
			dragSelectController = null
			pressedSkin = null
			
			super.dispose()
		}
		
		
		/**
		 * Begin drag select behaviour when clicking on nothing. 
		 * @param event
		 */		
		override protected function onMouseDownBackground(event:PickingManagerEvent):void
		{
			if ( allowDragSelect == false ) return;
			var dragDetector:DragDetector = new DragDetector(FloxEditor.stage)
			dragDetector.addEventListener(DragDetector.BEGIN_DRAG, dragSelectDetectedHandler)
			shiftKeyDown = event.shiftKey
		}
		
		protected function dragSelectDetectedHandler(event:Event):void
		{
			if ( ignoreDragDetect )
			{
				ignoreDragDetect = false
				return;
			}
			dragSelectController.beginDrag();
		}
		
		/**
		 * Clicking on a clear area of the background is symbolic for clearing the selection. 
		 * @param event
		 */		
		override protected function onClickBackground(event:PickingManagerEvent):void
		{
			if (ignoreNextMouseUp) 
			{
				ignoreNextMouseUp = false;
				return;
			}
			if (dragSelectController.dragging) return;
			if ( ArrayUtil.compare( [], context.selection.source ) == true ) return;
			var changeSelectionOperation:ChangePropertyOperation = new ChangePropertyOperation( context.selection, "source", [] );
			changeSelectionOperation.label = "Change Selection";
			context.operationManager.addOperation( changeSelectionOperation );
		}
		
		/**
		 * When first pressing the mouse on an item, the user may be about to click it, or they may
		 * be about to click and drag. This function creates a drag detector helper to determine
		 * which situation occurs.
		 * @param item
		 * @param event
		 */		
		override protected function onMouseDownSkins( event:PickingManagerEvent ):void
		{
			if ( !allowDrag ) return;
			shiftKeyDown = event.shiftKey;
			
			var skin:IRenderable = event.skinsUnderMouse[0];
			var dragDetector:DragDetector = new DragDetector( view.container );
			pressedSkin = skin;
			dragDetector.addEventListener( DragDetector.BEGIN_DRAG, dragDetectedHandler );
		}
		
		
		override protected function onMouseMoveContainer(event:PickingManagerEvent) : void
		{
			previouslyClickedComponent = null;
		}
		
		/**
		 * The user started dragging the item pressed on above. We use the dragItemsController to
		 * take care of the dragging items behaviour. 
		 * @param event
		 */		
		protected function dragDetectedHandler(event:Event):void
		{
			// Automatically select the dragged item
			var pressedComponent:IComponentContainer = pressedSkin.parentComponent;
			
			if ( !pressedComponent ) return;
			if ( context.selection.contains( pressedComponent ) == false ) 
			{
				handleSelection( pressedComponent, shiftKeyDown, false );
			}
			// When the drag ends, the user will likely release the mouse over the same item, resulting in a
			// 'click' event. Clicking an item is usually interpreted as selecting it, which is not what we want
			// after a drag select. This flag causes the click event to be ignored.
			ignoreNextMouseUp = true
			
			var skins:Array = SelectionUtil.getSkinsFromComponents( context.selection.source );
			
			skins = skins.filter( 
			function( item:*, index:int, array:Array ):Boolean 
			{ 
				var value:String = IntrospectionUtil.getMetadataByNameAndKey(item, "CadetEditor", "transformable");
				if ( value == "false" ) return false;
				return true;
			} );
			
			if ( skins.length > 0 )
			{
				dragItemsController.beginDrag( skins );
			}			
		}
		
		
		/**
		 * Clicking an actor results in selecting the actor.
		 * @param item
		 * @param event
		 */
		private var previouslyClickedComponent:IComponentContainer;
		override protected function onClickSkins( event:PickingManagerEvent ):void
		{	
			if (ignoreNextMouseUp) 
			{
				ignoreNextMouseUp = false;
				return;
			}
			
			var components:Vector.<IComponentContainer> = ComponentUtil.getComponentContainers( event.skinsUnderMouse );
			
			if ( previouslyClickedComponent == null || components.indexOf(previouslyClickedComponent) == -1 || components.length == 1)
			{
				handleSelection(components[0], event.shiftKey)
				previouslyClickedComponent = components[0];
				return
			}
			
			var index:int = components.indexOf(previouslyClickedComponent);
			index = index == components.length-1 ? 0 : index+1;
			
			var component:IComponentContainer = components[index];
			handleSelection(component, event.shiftKey)
			
			var alreadySelected:Boolean = context.selection.contains( previouslyClickedComponent );
			if ( alreadySelected )
			{
				handleSelection( previouslyClickedComponent, true );
			}
			
			
			previouslyClickedComponent = component;
		}
		
		/**
		 * This function takes care of the toggling the selection on an item, and updating the current selection. 
		 * @param item
		 * @param shiftSelect
		 * @param allowDeselect
		 */		
		protected function handleSelection( component:IComponentContainer, shiftSelect:Boolean = false, allowDeselect:Boolean = true ):void
		{
			var alreadySelected:Boolean = SelectionUtil.doesArrayContainComponentAnscestor( context.selection.source, component );
			var newSelection:Array = context.selection.source;
						
			// No shift selection, so only select the item clicked on
			if ( shiftSelect == false )
			{
				// If not already selected, then select it
				if ( !alreadySelected )
				{
					newSelection = [component];
				}
			}
			
			// Otherwise we're modifying an existing selection
			else
			{
				// If already selected, remove it from the current selection
				if ( alreadySelected )
				{
					newSelection.splice( newSelection.indexOf( component ), 1 );
				}
				// Otherwise add it to the current selection
				else
				{
					// Only if multiple selection is allowed however
					if ( allowMultipleSelection )
					{
						newSelection.push( component );
					}
				}
			}
			
			
			if ( ArrayUtil.compare( newSelection, context.selection.source ) == true ) return;
			
			var changeSelectionOperation:ChangePropertyOperation = new ChangePropertyOperation( context.selection, "source", newSelection );
			changeSelectionOperation.label = "Change Selection";
			context.operationManager.addOperation( changeSelectionOperation );
		}
	}
}