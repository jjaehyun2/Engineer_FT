////////////////////////////////////////////////////////////////////////////////
//
//  Licensed to the Apache Software Foundation (ASF) under one or more
//  contributor license agreements.  See the NOTICE file distributed with
//  this work for additional information regarding copyright ownership.
//  The ASF licenses this file to You under the Apache License, Version 2.0
//  (the "License"); you may not use this file except in compliance with
//  the License.  You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
//
////////////////////////////////////////////////////////////////////////////////
package actionScripts.plugin.search
{
    import flash.display.DisplayObject;
    import flash.events.Event;
    
    import mx.collections.ArrayCollection;
    import mx.core.FlexGlobals;
    import mx.events.CloseEvent;
    import mx.events.CollectionEvent;
    import mx.events.CollectionEventKind;
    import mx.managers.PopUpManager;
    
    import actionScripts.events.AddTabEvent;
    import actionScripts.events.GlobalEventDispatcher;
    import actionScripts.plugin.PluginBase;
    import actionScripts.plugin.actionscript.as3project.vo.AS3ProjectVO;
    import actionScripts.ui.IContentWindow;
    import actionScripts.ui.tabview.TabEvent;
    import actionScripts.valueObjects.ConstantsCoreVO;
    import actionScripts.valueObjects.ProjectVO;
    
    import components.popup.SearchInProjectPopup;
    import components.views.other.SearchInProjectView;

    public class SearchPlugin extends PluginBase
    {
		public static const SEARCH_IN_PROJECTS:String = "SEARCH_IN_PROJECTS";
		public static const WORKSPACE:String = "WORKSPACE";
		public static const PROJECT:String = "PROJECT";
		public static const LINKED_PROJECTS:String = "LINKED_PROJECTS";
		
		[Bindable] public static var IS_REPLACE_APPLIED:Boolean;
		
		public static var LAST_SCOPE_INDEX:int = 1;
		public static var LAST_SELECTED_SCOPE_ENCLOSING_PROJECTS:Boolean;
		public static var LAST_SELECTED_PATTERNS:ArrayCollection;
		public static var LAST_SEARCH:String;
		public static var LAST_SELECTED_PROJECT:ProjectVO;
		
		private var searchPopup:SearchInProjectPopup;
		private var searchResultView:SearchInProjectView;
		private var isCollectionChangeListenerAdded:Boolean;
		
        override public function get name():String 	{return "Search in Projects";}
        override public function get author():String {return ConstantsCoreVO.MOONSHINE_IDE_LABEL +" Project Team";}
        override public function get description():String 	{return "Search string in one or multiple project files.";}

        public function SearchPlugin()
        {
            super();
        }

        override public function activate():void
        {
            dispatcher.addEventListener(SEARCH_IN_PROJECTS, onSearchRequested, false, 0, true);
            super.activate();
        }

        override public function deactivate():void
        {
			dispatcher.removeEventListener(SEARCH_IN_PROJECTS, onSearchRequested);
            super.deactivate();
        }
		
		protected function onSearchRequested(event:Event):void
		{
			// probable termination
			if (model.projects.length == 0) return;
			
			if (!searchPopup)
			{
				searchPopup = PopUpManager.createPopUp(FlexGlobals.topLevelApplication as DisplayObject, SearchInProjectPopup, false) as SearchInProjectPopup;
				searchPopup.addEventListener(CloseEvent.CLOSE, onSearchPopupClosed);
				PopUpManager.centerPopUp(searchPopup);
				
				if (!isCollectionChangeListenerAdded) 
				{
					model.projects.addEventListener(CollectionEvent.COLLECTION_CHANGE, onProjectsCollectionChanged, false, 0, true);
					isCollectionChangeListenerAdded = true;
				}
			}
			else
			{
				PopUpManager.bringToFront(searchPopup);
			}
		}
		
		private function onProjectsCollectionChanged(event:CollectionEvent):void
		{
			if (event.kind == CollectionEventKind.REMOVE && event.items[0] == LAST_SELECTED_PROJECT) 
			{
				LAST_SELECTED_PROJECT = null;
			}
		}
		
		private function onSearchPopupClosed(event:CloseEvent):void
		{
			event.target.removeEventListener(CloseEvent.CLOSE, onSearchPopupClosed);
			
			// probable termination
			if (!searchPopup.isClosedAsSubmit || !searchPopup.ddlProjects.selectedItem)
			{
				searchPopup = null;
				return;
			}
			
			LAST_SCOPE_INDEX = searchPopup.rbgScope.selectedIndex;
			LAST_SEARCH = searchPopup.txtSearch.text;
			IS_REPLACE_APPLIED = false;
			LAST_SELECTED_SCOPE_ENCLOSING_PROJECTS = searchPopup.cbEnclosingProjects.selected;
			LAST_SELECTED_PROJECT = searchPopup.ddlProjects.selectedItem ? searchPopup.ddlProjects.selectedItem as ProjectVO : null;
			
			if (!searchResultView)
			{
				searchResultView = new SearchInProjectView();
				searchResultView.addEventListener(TabEvent.EVENT_TAB_CLOSE, onSearchResultsClosed);
				updateProperties();	
				
				// adding as a tab
				GlobalEventDispatcher.getInstance().dispatchEvent(
					new AddTabEvent(searchResultView as IContentWindow)
				);
			}
			else
			{
				// another new search initiated
				// while existing search tab already opens
				updateProperties();
				model.activeEditor = searchResultView;
				searchResultView.resetSearch();
			}
			
			searchPopup = null;
			
			/*
			 * @local
			 */
			function updateProperties():void
			{
				searchResultView.valueToSearch = searchPopup.txtSearch.text;
				searchResultView.patterns = searchPopup.txtPatterns.text;
				searchResultView.scope = String(searchPopup.rbgScope.selectedValue);
				searchResultView.isEnclosingProjects = searchPopup.cbEnclosingProjects.selected;
				searchResultView.isMatchCase = searchPopup.optionMatchCase.selected;
				searchResultView.isRegexp = searchPopup.optionRegExp.selected;
				searchResultView.isEscapeChars = searchPopup.optionEscapeChars.selected;
				searchResultView.isShowReplaceWhenDone = searchPopup.isShowReplaceWhenDone;
				searchResultView.selectedProjectToSearch = LAST_SELECTED_PROJECT ? LAST_SELECTED_PROJECT : null;
			}
		}
		
		private function onSearchResultsClosed(event:TabEvent):void
		{
			event.target.removeEventListener(TabEvent.EVENT_TAB_CLOSE, onSearchResultsClosed);
			searchResultView = null;
		}
    }
}