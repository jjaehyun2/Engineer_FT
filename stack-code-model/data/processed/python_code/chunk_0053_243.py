﻿/*
Copyright (c) 2010 Trevor McCauley

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
*/
package com.myavatareditor.avatarcore {
	
	import com.myavatareditor.avatarcore.Collection;
	import com.myavatareditor.avatarcore.debug.print;
	import com.myavatareditor.avatarcore.debug.PrintLevel;
	import com.myavatareditor.avatarcore.events.FeatureEvent;
	import com.myavatareditor.avatarcore.events.FeatureDefinitionEvent;
	import flash.display.Sprite;
	import flash.events.Event;
	
	/**
	 * Dispatched when the avatar is rebuilt using the rebuild() method.
	 * Avatars are also rebuilt when the associated Library changes.
	 * @see REBUILD
	 */
	[Event(name="avatarRebuild", type="flash.events.Event")]
	
	/**
	 * Dispatched when the library associated with this Avatar changes.
	 * @see LIBRARY_CHANGED
	 */
	[Event(name="avatarLibraryChanged", type="flash.events.Event")]
		
	/**
	 * Dispatched when a new Feature instance is added to the Avatar.
	 * @see FeatureEvent#ADDED
	 */
	[Event(name="featureEventAdded", type="com.myavatareditor.avatarcore.events.FeatureEvent")]
	
	/**
	 * Dispatched when an existing Feature instance within the Avatar
	 * is changed.
	 * @see FeatureEvent#CHANGED
	 */
	[Event(name="featureEventChanged", type="com.myavatareditor.avatarcore.events.FeatureEvent")]
	
	/**
	 * Dispatched when an existing Feature instance within the Avatar
	 * is removed.
	 * @see FeatureEvent#REMOVED
	 */
	[Event(name="featureEventRemoved", type="com.myavatareditor.avatarcore.events.FeatureEvent")]

	/**
	 * Avatar instances are the primary components of the Avatar Core framework.
	 * Everything revolves around Avatar objects.  They contain the data describing avatar
	 * characters. Each characteristic within an Avatar object is in turn defined by
	 * Feature instances added to Avatar objects through the Collection API.
	 * Feature instances themselves contain additional properties which describe 
	 * that feature, either explicitly or by referencing feature information
	 * in a linked Library defined by the Avatar.
	 * <p>
	 * The visual representations 
	 * of an Avatar object is generated by an AvatarDisplay instances. Any number of
	 * AvatarDisplay objects can reference the same Avatar instance.  Where Avatar
	 * represents the model, AvatarDisplay represents the view.
	 * </p>
	 * @author Trevor McCauley; www.senocular.com
	 * @see Feature
	 * @see Collection
	 * @see Library
	 * @see com.myavatareditor.avatarcore.display.AvatarDisplay
	 */
	public class Avatar extends Collection {
		
		/**
		 * Rebuild event constant.
		 * @see #rebuild()
		 */
		public static const REBUILD:String = "avatarRebuild";
		/**
		 * Changed library event constant.
		 * @see #library
		 */
		public static const LIBRARY_CHANGED:String = "avatarLibraryChanged";
		
		/**
		 * The name of the library to be associated with this
		 * avatar.  Associations with libraries through this
		 * property are made when an Avatar instance is created
		 * within a Definitions object. Changing libraryName will
		 * not invoke a new lookup for the related library. If no
		 * library is associated with this Avatar, libraryName can
		 * still be set and retrieved as an independent value. If
		 * this value was set to some value other than the name
		 * of the associated library, the name of that associated
		 * library will be returned when getting the value of
		 * libraryName. Setting libraryName when a library is
		 * associated will only affect this value, not the name
		 * value of that library.
		 * @see #library
		 */
		public function get libraryName():String { 
			return _library ? _library.name : _libraryName;
		}
		public function set libraryName(value:String):void {
			_libraryName = value;
		}
		private var _libraryName:String;
		
		/**
		 * Library associated with this avatar.  When a new
		 * library is defined, that library is coupled with
		 * the avatar instance and each Feature it contains
		 * gets updated with the library's definitions.
		 * When set, both a Avatar.REBUILD event and a
		 * Avatar.LIBRARY_CHANGED event are dispatched.
		 * @see #libraryName
		 */
		public function get library():Library { return _library; }
		public function set library(value:Library):void {
			if (value == _library) return;
			
			cleanupLibrary();
			_library = value;
			setupLibrary();
			
			assignFeatureDefaults();
			
			// inherit name of library if not defined here
			// this also works the other way around
			if (_library){
				if (!_libraryName){
					_libraryName = _library.name;
				}else if (!_library.name){
					_library.name = _libraryName;
				}
			}
			
			rebuild();
			dispatchEvent(new Event(LIBRARY_CHANGED));
		}
		private var _library:Library;
		
		/**
		 * When true, events are not dispatched.  This is useful
		 * for batch operations where events are not necessary
		 * such as cloning.
		 */
		protected function get suppressEvents():Boolean { return _suppressEvents; }
		protected function set suppressEvents(value:Boolean):void {
			_suppressEvents = value;
		}
		private var _suppressEvents:Boolean = false;
		
		/**
		 * Constructor for creating new Avatar instances.
		 * @param name Name of this instance.
		 * @param	library Library to be associated with the
		 * Avatar instance.
		 * @see #library
		 */
		public function Avatar(name:String = null, library:Library = null) {
			if (name) this.name = name;
			if (library) this.library = library;
		}
		/**
		 * Returns the string representation of the Avatar object with the
		 * value of its name property.
		 * @return The string representation of the specified object.
		 */
		public override function toString():String {
			return "[Avatar name=\"" + name + "\"]";
		}
		
		/**
		 * Creates and returns a copy of the Avatar object. Any library
		 * associated with the avatar is copied by reference; it isn't
		 * cloned.
		 * @return A copy of this Avatar object.
		 */
		override public function clone(copyInto:Object = null):Object {
			suppressEvents = true;
			try {
				var copy:Avatar = (copyInto) ? copyInto as Avatar : new Avatar();
				if (copy == null) return null;
				super.clone(copy);
				
				copy._libraryName = _libraryName;
				copy.library = library; // link to same instance, not cloned.
			}catch (error:*){
				// errors pass through. Errors must be
				// handled however, to allow suppressEvents 
				// to be restored to false
				throw(error);
			}finally{
				suppressEvents = false;
			}
			return copy;
		}
		
		/**
		 * Implementation for IXMLWritable for XML generation. Avatars do not
		 * include library in XML.
		 * @inheritDoc
		 */
		public override function getPropertiesIgnoredByXML():Object {
			var obj:Object = super.getPropertiesIgnoredByXML();
			obj.library = 1;
			return obj;
		}
		
		/**
		 * Implementation for IXMLWritable for XML generation. Avatars place
		 * their libraryName properties in XML attributes.
		 * @inheritDoc
		 */
		public override function getPropertiesAsAttributesInXML():Object {
			var obj:Object = super.getPropertiesAsAttributesInXML();
			obj.libraryName = 1;
			return obj;
		}
		
		/**
		 * Custom add item that will dispatch events for Feature instances
		 * added to the Avatar's collection.  If another Feature instance
		 * already exists within the avatar of the same name, that feature
		 * is replaced with the new feature and a FEATURE_CHANGED event is 
		 * dispatched.  If a Feature is added with a unique name, a
		 * FEATURE_ADDED event is dispatched.  Features added to the 
		 * avatar's collection are automatically associated with this avatar
		 * and the library assigned to the avatar if one exists (defining
		 * Feature.definition).
		 * @param	item Object to add to the avatar's collection.
		 * @return Item added to the collection.
		 */
		public override function addItem(item:*):* {
			var eventType:String;
			
			// remove existing item by name without events
			// assumes (forces) requireUniqueNames true
			var itemName:String = (Collection.nameKey in item) ? item[Collection.nameKey] : null;
			if (itemName && super.removeItemByName(itemName)) { 
				eventType = FeatureEvent.CHANGED;
			}else{
				eventType = FeatureEvent.ADDED;
			}
			
			var added:* = super.addItem(item);
			if (added is Feature) {
				var feature:Feature = added as Feature;
				
				// remove feature from any previous avatar
				// features require one avatar since
				// information stored in the feature object
				// is specific to the environment provided
				// by the avatar instance (i.e. parenting)
				var oldAvatar:Avatar = feature.avatar;
				if (oldAvatar && oldAvatar != this){
					oldAvatar.removeItem(feature);
				}
				
				// link feature to this avatar
				feature.avatar = this;
				
				// assign any defaults that may exist within the library
				if (_library){
					feature.assignDefaults();
				}
				
				// update feature parent information
				updateParentHierarchy();
				
				dispatchEvent(new FeatureEvent(eventType, false, false, feature));
			}
			return added;
		}
		
		/**
		 * Custom removeItem method that removes an item from the
		 * Avatar's collection. If that item is of the type Feature
		 * a FeatureEvent.REMOVED event is dispatched.  Values set up in
		 * Avatar.addItem, such as Feature.avatar and Feature.definition
		 * are set to null.
		 * @param	item Object to be removed from the collection.
		 * @return Item removed if an item is removed. Null is returned
		 * if no item is removed.
		 */
		public override function removeItem(item:*):* {
			var removed:* = super.removeItem(item);
			if (removed is Feature) {
				var feature:Feature = removed as Feature;
				dispatchEvent(new FeatureEvent(FeatureEvent.REMOVED, false, false, feature));
				feature.avatar = null;
			}
			return removed;
		}
		
		/**
		 * Invokes a FeatureEvent.CHANGED event to indicate to AvatarDisplay
		 * objects that the feature needs to be redrawn.  This mirrors the 
		 * behavior of Feature.redraw() which is typically called instead of
		 * this method.
		 * @param	feature The feature within the Avatar instance that
		 * needs to be redrawn.
		 * @param	originalName The original name for the feature of a cause
		 * for the redraw includes changing the name. Since links are made through
		 * names, an original name helps identify old references.
		 * @see Feature#redraw()
		 * @private
		 */
		internal function redrawFeature(feature:Feature, originalName:String = null):void {
			if (feature == null) return;
			dispatchEvent(new FeatureEvent(FeatureEvent.CHANGED, false, false, feature, originalName));
		}
		
		/**
		 * Redraws the Avatar, or more specifically, each Feature instance
		 * within this Avatar instance (via Feature.redraw()).
		 */
		public function redraw():void {
			updateParentHierarchy();
			var feature:Feature;
			var features:Array = this.collection;
			var i:int = features.length;
			while (i--){
				redrawFeature(features[i] as Feature);
			}
		}
		
		/**
		 * Updates the parent hierarchy used within the features of the
		 * Avatar instance. If at any point in time, parents or parentName
		 * values change, the parent hierarchy will need to be updated so 
		 * that child features will be able to correctly reference their
		 * parents and be drawn after their parents are done drawing. This 
		 * is handled internally upon assigning values to Feature.parent and
		 * Feature.parentName and when adding new features to the Avatar
		 * collection as well as whenever Avatar.redraw() is called.
		 * @see Feature#parent
		 * @see Feature#parentName
		 */
		public function updateParentHierarchy():void {
			var feature:Feature;
			var features:Array = this.collection;
			var i:int;
			
			// pass one: make sure all parent references are set
			i = features.length;
			while (i--){
				feature = features[i] as Feature;
				if (feature) feature.updateParent();
			}
			
			// pass two: update parent counts for drawing order
			i = features.length;
			while (i--){
				feature = features[i] as Feature;
				if (feature) feature.updateParentCount();
			}
		}
		
		/**
		 * Copies any FeatureDefinition defaults in the linked Library
		 * into all Feature instances within the Avatar's collection.
		 */
		private function assignFeatureDefaults():void {
			if (_library == null) return;
			var feature:Feature;
			var features:Array = this.collection;
			var i:int = features.length;
			while (i--){
				feature = features[i] as Feature;
				if (feature) feature.assignDefaults();
			}
		}
		
		/**
		 * Calls Feature.consolidate on all features within the
		 * avatar.  This would be used to create a self-contained
		 * version of the avatar that would be able to be displayed 
		 * without the library.
		 * @see Feature#consolidate()
		 */
		public function consolidateFeatures():void {
			var feature:Feature;
			var features:Array = this.collection;
			var i:int = features.length;
			while (i--){
				feature = features[i] as Feature;
				if (feature) feature.consolidate();
			}
		}
		
		/**
		 * Signals that the avatar should be rebuilt by dispatching the 
		 * Avatar.REBUILD event. AvatarDisplay objects use this event
		 * to rebuild their display list. When being rebuilt, an AvatarDisplay
		 * object clears all existing art sprites and reloads them from
		 * scratch.
		 */
		public function rebuild():void {
			updateParentHierarchy();
			dispatchEvent(new Event(REBUILD));
		}
		
		private function setupLibrary():void {
			if (_library == null) return;
			_library.addEventListener(FeatureDefinitionEvent.ADDED, definitionChangedHandler, false, 0, true);
			_library.addEventListener(FeatureDefinitionEvent.CHANGED, definitionChangedHandler, false, 0, true);
			_library.addEventListener(FeatureDefinitionEvent.REMOVED, definitionChangedHandler, false, 0, true);
		}
		private function cleanupLibrary():void {
			if (_library == null) return;
			_library.removeEventListener(FeatureDefinitionEvent.ADDED, definitionChangedHandler, false);
			_library.removeEventListener(FeatureDefinitionEvent.CHANGED, definitionChangedHandler, false);
			_library.removeEventListener(FeatureDefinitionEvent.REMOVED, definitionChangedHandler, false);
		}
		
		private function definitionChangedHandler(definitionEvent:FeatureDefinitionEvent):void {
			
			if (definitionEvent.featureDefinition) {
				
				var featureName:String = definitionEvent.featureDefinition.name;
				var feature:Feature = getItemByName(featureName) as Feature;
				var origFeature:Feature = getItemByName(definitionEvent.originalName) as Feature;
				
				if (feature || origFeature){
					updateParentHierarchy();
					if (feature) redrawFeature(feature);
					if (origFeature) redrawFeature(origFeature);
				}
			}
		}
		
		/**
		 * @inheritDoc
		 */
		override public function dispatchEvent(event:Event):Boolean {
			return (suppressEvents) ? false : super.dispatchEvent(event);
		}
	}
}