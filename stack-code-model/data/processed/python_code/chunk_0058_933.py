package cn.seisys.TGISViewer.components.checkTree
{
	import com.esri.ags.Graphic;
	
	import flash.events.MouseEvent;
	import flash.geom.Rectangle;
	
	import mx.collections.ICollectionView;
	import mx.collections.IList;
	import mx.collections.IViewCursor;
	import mx.controls.CheckBox;
	import mx.controls.Tree;
	import mx.controls.treeClasses.ITreeDataDescriptor;
	import mx.controls.treeClasses.TreeItemRenderer;
	import mx.controls.treeClasses.TreeListData;
	import mx.events.ListEvent;
	
	public class CheckTreeItemRenderer extends TreeItemRenderer
	{
		private var _checkBox:CheckBox;
		private var _tree:CheckTree;
		
		/**
		 * 部分子项选中
		 * */
		public static var STATE_INDETERMINATE:int = 2;
		/**
		 * 全部子项选中
		 * */
		public static var STATE_CHECKED:int = 1;
		/**
		 * 全部子项未选中
		 * */
		public static var STATE_UNCHECKED:int = 0;
		
		public function CheckTreeItemRenderer()
		{
			super();
			mouseEnabled = true;
		}
		
		override protected function createChildren():void
		{
			_checkBox = new CheckBox();
			addChild( _checkBox );
			_checkBox.addEventListener( MouseEvent.CLICK, checkBox_clickHandler );
			
			_tree = this.owner as CheckTree;
			
			super.createChildren();
			_tree.addEventListener( ListEvent.CHANGE, tree_propertyChangeHandler );
		}
		
		private function checkBox_clickHandler( event:MouseEvent ):void 
		{
			if ( data )
			{
				var myListData:TreeListData = TreeListData( this.listData );
				var selectedNode:Object = myListData.item;
				_tree = myListData.owner as CheckTree;
				var selected:Boolean = _checkBox.selected;
				if ( selected )
				{
					loopChildren( data, _tree, STATE_CHECKED );
					if ( _tree.checkBoxOpenItemsOnCheck )
					{
						_tree.expandChildrenOf( data, true );
					}
				}
				else
				{
					loopChildren( data, _tree, STATE_UNCHECKED );
					if ( _tree.checkBoxOpenItemsOnCheck )
					{
						_tree.expandChildrenOf( data, false );
					}
				}
				
				if ( _tree.checkBoxCascadeOnCheck )
				{
					var parent:Object = _tree.getParentItem( data );
					if ( parent )
					{
						loopParents( parent, _tree, getParentState( _tree, parent ) );
					}
				}
				
				_tree.dispatchEvent( new MouseEvent( "checkBoxClick" ) );
			}
		}
		
		private function tree_propertyChangeHandler( event:ListEvent ):void
		{
			this.updateDisplayList( unscaledWidth, unscaledHeight );
		}
		
		/**
		 * 递归设置父项目状态
		 * */
		private function loopParents( item:Object, tree:Tree, state:int ):void
		{
			if ( !item )
			{
				return;
			}
			
			var stateField:String = _tree.checkBoxStateField;
			var tmpTree:IList = _tree.dataProvider as IList;
			var oldValue:Number = item[stateField] as Number;
			var newValue:Number = state as Number;
			
			item[_tree.checkBoxStateField] = state;
			tmpTree.itemUpdated( item, stateField, oldValue, newValue );
			
			var parentItem:Object = tree.getParentItem( item );
			if ( parentItem)
			{
				loopParents( parentItem, tree, getParentState( tree, parentItem ) );
			}
		}
		
		/**
		 * 获取父项的状态
		 * */
		private function getParentState( tree:Tree, parent:Object ):int
		{
			var checkCount:int = 0;
			var inderterminateCount:int = 0;
			var uncheckCount:int = 0;
			
			if ( parent )
			{
				var treeData:ITreeDataDescriptor = tree.dataDescriptor;
				var cursor:IViewCursor = treeData.getChildren( parent ).createCursor();
				while ( !cursor.afterLast )
				{
					if ( cursor.current[_tree.checkBoxStateField] == STATE_CHECKED )
					{
						checkCount++;
					}
					else if ( cursor.current[_tree.checkBoxStateField] == STATE_INDETERMINATE )
					{
						inderterminateCount++;
					}
					else if ( cursor.current[_tree.checkBoxStateField] == STATE_UNCHECKED )
					{
						uncheckCount++;
					}
					cursor.moveNext();
				}
			}
			if ( ( checkCount > 0 && uncheckCount > 0 ) || inderterminateCount > 0 )
			{
				return STATE_INDETERMINATE;
			}
			else if ( checkCount > 0 )
			{
				return STATE_CHECKED;
			}
			else 
			{
				return STATE_UNCHECKED;
			}
		}
		
		/**
		 * 设置项目和子项的状态
		 * */
		private function loopChildren( item:Object, tree:Tree, state:int ):void
		{
			if ( !item )
			{
				return;
			}
			
			var stateField:String = _tree.checkBoxStateField;
			var tmpTree:IList = _tree.dataProvider as IList;
			var oldValue:Number = item[stateField] as Number;
			var newValue:Number = state as Number;
			
			item[stateField] = state;
			tmpTree.itemUpdated( item, stateField, oldValue, newValue );
			
			var graphic:Graphic = item.graphic;
			if ( graphic )
			{
				graphic.visible = ( state == STATE_CHECKED );
			}
			
			var treeData:ITreeDataDescriptor = tree.dataDescriptor;
			if ( _tree.checkBoxCascadeOnCheck && treeData.hasChildren( item ) )
			{
				var children:ICollectionView = treeData.getChildren( item );
				var cursor:IViewCursor = children.createCursor();
				while( !cursor.afterLast )
				{
					loopChildren( cursor.current, tree, state );
					cursor.moveNext();
				}
			}
				
		}
		
		private function setCheckState( checkBox:CheckBox, value:Object, state:int ):void
		{
			if ( state == STATE_CHECKED )
			{
				checkBox.selected = true;
			}
			else
			{
				checkBox.selected = false;
			}
		}
		
		override public function set data( value:Object ):void
		{
			if ( value )
			{
				super.data = value;
				setCheckState( _checkBox, value, value[_tree.checkBoxStateField] );
			}
		}
		
		override protected function updateDisplayList(unscaledWidth:Number, unscaledHeight:Number):void
		{
			super.updateDisplayList(unscaledWidth, unscaledHeight);  
			if (super.data)  
			{  
				if (super.icon != null)  
				{  
					_checkBox.x = super.icon.x + _tree.checkBoxLeftGap;  
					_checkBox.y = ( height - _checkBox.height ) / 2;  
					super.icon.x = _checkBox.x + _checkBox.width + _tree.checkBoxRightGap;  
					super.label.x = super.icon.x + super.icon.width + 3;  
				}  
				else  
				{  
					_checkBox.x = super.label.x + _tree.checkBoxLeftGap;  
					_checkBox.y = ( height - _checkBox.height ) / 2;  
					super.label.x=_checkBox.x + _checkBox.width + _tree.checkBoxRightGap;  
				}  
				
				setCheckState( _checkBox, data, data[_tree.checkBoxStateField] );  
				if ( _tree.checkBoxEnableState && data[_tree.checkBoxStateField] == STATE_INDETERMINATE )  
				{  
					fillCheckBox(true);  
				}  
				else  
				{
					fillCheckBox(false); 
				}
			}  
		}
		
		protected function fillCheckBox( isFill:Boolean ):void  
		{  
			_checkBox.graphics.clear();  
			if ( isFill )  
			{  
				var myRect:Rectangle = getCheckTreeBgRect( _tree.checkBoxBgPadding );  
				_checkBox.graphics.beginFill( _tree.checkBoxBgColor, _tree.checkBoxBgAlpha )  
				_checkBox.graphics.drawRoundRect( myRect.x, myRect.y, myRect.width, myRect.height, 
					_tree.checkBoxBgElips, _tree.checkBoxBgElips);  
				_checkBox.graphics.endFill();  
			}  
		}  
		
		protected function getCheckTreeBgRect( checkTreeBgPadding:Number ):Rectangle  
		{  
			var myRect:Rectangle = _checkBox.getBounds( _checkBox );  
			myRect.top += checkTreeBgPadding;  
			myRect.left += checkTreeBgPadding;  
			myRect.bottom -= checkTreeBgPadding;  
			myRect.right -= checkTreeBgPadding;  
			return myRect;  
		} 
	}
}