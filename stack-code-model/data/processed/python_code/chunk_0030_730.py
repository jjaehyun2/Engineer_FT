package com.db.rds.content.ExceptionManagement.view.controls
{
	import com.db.rds.content.ExceptionManagement.events.PageEvent;
	
	import flash.events.MouseEvent;
	
	import mx.collections.ArrayCollection;
	import mx.core.UIComponent;
	
	import spark.components.HGroup;
	import spark.components.Label;
	
	[Event(name="pageSelected", type="events.PageEvent")]
	public class PagingControl extends HGroup
	{
		private static const LABEL_PROPERTY:String = "text";
		
		public var differencePagesCountFromSelected:int = 3;
		public var selectedPage:int = 1;
		private var _pagesCount:int = 0;
		
		private var lblPages:Label;
		
		private var pages:ArrayCollection = new ArrayCollection();
		
		public function PagingControl()
		{
			super();
			setStyle('horizontalGap', 1);
			setStyle('horizontalAlign', 'center');
			
			lblPages = new Label();
		}

		public function set pagesCount(value:int):void
		{
			_pagesCount = value;
			createPagesLinks();
		}
		
		public function get pagesCount():int
		{
			return _pagesCount; 
		}
		
		private function addLinks():void
		{
			for each(var page:UIComponent in pages)
			{
				if(page.hasOwnProperty(LABEL_PROPERTY) && Number(page[LABEL_PROPERTY]) == selectedPage)
					setLinkStyle(page, true);
				this.addElement(page);
			}
		}
		
		private function removeLinks():void
		{
			for each(var p:UIComponent in pages)
			{
				this.removeElement(p);
			}
			pages = new ArrayCollection();
		}
		
		private function createPagesLinks():void
		{
			var link:UIComponent;

			removeLinks();

			if(pagesCount <= 0)
				return;
			
			lblPages.text = "Pages: ";
			pages.addItemAt(lblPages, 0);
			
			// First page
			pages.addItemAt(createPageLink("1"), 1);
			
			if(pagesCount == 1)
			{
				addLinks();
				return;
			}
			
			var startRangePage:int = 2;
			var endRangePage:int = pagesCount - 1;
			
			var needLeftRangeLabel:Boolean = false;
			var needRightRangeLabel:Boolean = false;
			
			if(selectedPage > differencePagesCountFromSelected)
			{
				startRangePage = selectedPage - differencePagesCountFromSelected >= 2 ? selectedPage - differencePagesCountFromSelected : 2;
				needLeftRangeLabel = selectedPage - differencePagesCountFromSelected - 1 > 1 ? true : false;
			}
			
			if(pagesCount > selectedPage + differencePagesCountFromSelected)
			{
				endRangePage = selectedPage + differencePagesCountFromSelected;
				needRightRangeLabel = endRangePage + 1 < pagesCount ? true : false;
			}

			if(needLeftRangeLabel)
			{
				link = createPageLink('...');
				pages.addItem(link);
			}
				
			for (var p:int = startRangePage; p <= endRangePage; p++)
			{
				link = createPageLink(p.toString());
				pages.addItem(link);
			}
			
			if(needRightRangeLabel)
			{
				link = createPageLink('...');
				pages.addItem(link);
			}
			
			// Last page
			pages.addItem(createPageLink(pagesCount.toString()));
			
			addLinks();
		}

		private function setLinkStyle(link:UIComponent, selected:Boolean=false):void
		{
			if(!selected)
			{
				link.setStyle('color', 'blue');
				link.setStyle('textDecoration', 'underline');
			}
			else
			{
				link.setStyle('color', 0x000000);
				link.setStyle('textDecoration', 'none');
			}
			
			link.setStyle('paddingLeft', 0);
			link.setStyle('paddingRight', 0);
			link.setStyle('paddingTop', 0);
			link.setStyle('paddingBottom', 0);
			link.setStyle('rollOverColor', 0xffffff);
			link.setStyle('selectionColor', 0xffffff);
			link.mouseChildren = false;
			link.useHandCursor = true;
			buttonMode = true; 
		}
		
		private function createPageLink(label:String):UIComponent
		{
			var l:UIComponent;
			if(label != "...")
			{
				l = new Label();
				l.addEventListener(MouseEvent.CLICK, onPageSelected);
				l[LABEL_PROPERTY] = label;
				setLinkStyle(l);
			}
			else
			{
				l = new Label();
				l[LABEL_PROPERTY] = label;
			}
			return l;
		}
		
		private function onPageSelected(event:MouseEvent):void
		{
			if(selectedPage != Number(event.currentTarget[LABEL_PROPERTY]))
			{
				selectedPage = Number(event.currentTarget[LABEL_PROPERTY]);
				createPagesLinks();
				dispatchEvent(new PageEvent(PageEvent.PAGE_SELECTED, selectedPage));
			}
		}
	}
}