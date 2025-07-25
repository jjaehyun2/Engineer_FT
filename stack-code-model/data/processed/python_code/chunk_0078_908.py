// Copyright (c) 2012, Unwrong Ltd. http://www.unwrong.com
// All rights reserved. 

package cadetEditor2DFlashBox2D.tools
{
	import cadet.core.ComponentContainer;
	import cadet.core.IComponentContainer;
	import cadet.util.ComponentUtil;
	
	import cadet2D.components.connections.Pin;
	import cadet2D.components.core.Entity;
	import cadet2D.components.skins.IRenderable;
	import cadet2D.components.transforms.Transform2D;
	import cadet2D.geom.Vertex;
	import cadet2DFlash.components.renderers.Renderer2D;
	import cadet2DFlash.components.skins.AbstractSkin2D;
	import cadet2DFlash.components.skins.PinSkin;
	
	import cadet2DBox2D.components.behaviours.RevoluteJointBehaviour;
	
	import cadetEditor.assets.CadetEditorIcons;
	import cadetEditor.contexts.ICadetEditorContext;
	import cadetEditor.entities.ToolFactory;
	
	import cadetEditor2D.operations.PickComponentsOperation;
	import cadetEditor2D.ui.controlBars.PinToolControlBar;
	
	import cadetEditor2DFlash.tools.CadetEditorTool2D;
	
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.geom.Point;
	
	import flox.app.operations.AddDependencyOperation;
	import flox.app.operations.AddItemOperation;
	import flox.app.operations.ChangePropertyOperation;
	import flox.app.operations.UndoableCompoundOperation;
	import flox.ui.managers.CursorManager;
	
	public class PinTool extends CadetEditorTool2D
	{
		static public function getFactory():ToolFactory
		{
			return new ToolFactory( ICadetEditorContext, PinTool, "Pin Tool", CadetEditorIcons.Pin );
		}
		
		private var transformA		:Transform2D;
		private var transformB		:Transform2D;
		private var offset			:Point;
		
		protected var SkinType		:Class = PinSkin;
		
		private var pickComponentOperation	:PickComponentsOperation;
		
		public function PinTool()
		{
			
		}
		
		override public function enable():void
		{
			if ( !pickComponentOperation )
			{
				pickComponentOperation = new PickComponentsOperation(context, 2);
				pickComponentOperation.execute();
				pickComponentOperation.addEventListener(Event.COMPLETE, pickCompleteHandler);
			}
			
			statusBarText = "Click two overlapping components to pin them together."; 
			
			super.enable();
		}
		
		override public function disable():void
		{			
			if ( pickComponentOperation )
			{
				pickComponentOperation.cancel();
				pickComponentOperation = null;
			}
			
			CursorManager.setCursor(null);
			
			transformA = null;
			transformB = null;
			super.disable()
		}
		
		private function pickCompleteHandler( event:Event ):void
		{
			var pickedComponents:Array = pickComponentOperation.getResult();
			
			var componentA:IComponentContainer = pickedComponents[0];
			var componentB:IComponentContainer = pickedComponents[1];
			
			var skinA:IRenderable = ComponentUtil.getChildOfType(componentA, IRenderable);
			var skinB:IRenderable = ComponentUtil.getChildOfType(componentB, IRenderable);
			
			transformA = skinA.transform2D;
			transformB = skinB.transform2D;
			
			offset = context.view2D.renderer.worldToViewport( pickComponentOperation.getClickLoc() );
		
			//offset = context.view2D.viewport.localToGlobal(offset);
			offset = Renderer2D(context.view2D.renderer).viewport.localToGlobal(offset);
			
			offset = AbstractSkin2D(skinA).displayObjectContainer.globalToLocal(offset);
			
			createPin();
		}
		
		protected function createPin():void
		{
			var entity:Entity = new Entity();
			entity.name = ComponentUtil.getUniqueName( getName(), context.scene );
			
			var pin:Pin = new Pin();
			pin.transformA = transformA;
			pin.transformB = transformB;
			pin.localPos = new Vertex(offset.x, offset.y);
			entity.children.addItem(pin);
			
			var transform:Transform2D = new Transform2D();
			entity.children.addItem(transform);
			
			var skin:IRenderable = new PinSkin();
			entity.children.addItem(skin);
			
			
			var compoundOperation:UndoableCompoundOperation = new UndoableCompoundOperation();
			compoundOperation.addOperation( new AddItemOperation( entity, context.scene.children ) );
			compoundOperation.addOperation( new AddDependencyOperation( entity, transformA, context.scene.dependencyManager ) );
			compoundOperation.addOperation( new AddDependencyOperation( entity, transformB, context.scene.dependencyManager ) );
			compoundOperation.addOperation( new ChangePropertyOperation( context.selection, "source", [ entity ] ) );
			
			context.operationManager.addOperation( compoundOperation );
			
			transformA = null;
			transformB = null;
			
			pickComponentOperation.execute();
		}
		
		protected function getName():String { return "Pin"; }
	}
}