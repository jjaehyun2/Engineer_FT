/*
 * Scratch Project Editor and Player
 * Copyright (C) 2014 Massachusetts Institute of Technology
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 */

// PaletteSelector.as
// John Maloney, August 2009
//
// PaletteSelector is a UI widget that holds set of PaletteSelectorItems
// and supports changing the selected category. When the category is changed,
// the blocks palette is filled with the blocks for the selected category.

package ui {
	import flash.display.*;
	import flash.utils.Dictionary;
	import translation.Translator;
	import scratch.PaletteBuilder;
	import uiwidgets.*;

public class PaletteSelector extends Sprite {

	private static const categories:Array = [
		'Motion', 'Looks', 'Sound', 'Pen', 'Data', // column 1
		'Events', 'Control', 'Sensing', 'Operators', 'More Blocks']; // column 2

	public var sageCategories:Array = [
		false, // placeholder
		true, true, true, true, true, // column 1
		true, true, true, true, true]; // column 2
		
	public var sageBlockIncludes:Dictionary;

	public var selectedCategory:int = 0;
	
	private var app:Scratch;

	public function PaletteSelector(app:Scratch) {
		this.app = app;
		initCategories();
	}

	public static function strings():Array { return categories }
	
	public function updateTranslation():void { 
		initCategories();
		updateCategorySelection(); 
	}
	
	// update palette selected if entering play mode on unSageSelected palette 
	private function updateCategorySelection():void {
		if(app.interp.sagePlayMode && !sageCategories[selectedCategory])
		{
			for(var i:int=1; i<sageCategories.length; ++i)
				if(sageCategories[i])
				{
					select(i);
					break;
				}
		}
	}

	public function select(id:int, shiftKey:Boolean = false):void {
		for (var i:int = 0; i < numChildren; i++) {
			var item:PaletteSelectorItem = getChildAt(i) as PaletteSelectorItem;
			item.setSelected(item.categoryID == id);
		}
		var oldID:int = selectedCategory;
		selectedCategory = id;
		app.getPaletteBuilder().showBlocksForCategory(selectedCategory, (id != oldID), shiftKey);
	}
	
	public function sageSelect(pLabel:String, checkbox:IconButton):void {
		var entry:Array = Specs.entryForCategory(pLabel);
		sageCategories[entry[0]] = !sageCategories[entry[0]];
		var offCount:int = 0;
		for(var i:int=0; i<sageCategories.length; ++i)
			if(!sageCategories[i])
				++offCount;
		if(offCount == sageCategories.length)
		{
			sageCategories[entry[0]] = !sageCategories[entry[0]];
			checkbox.turnOn();
			DialogBox.notify('SAGE Alert', 'At least one palette must be selected');
		}
		else { // update BlockPalette & ScriptsPane
			app.getStage().refresh();
			app.getViewedObject().updateScriptsAfterTranslation(); // resest ScriptsPane
		}
	}

	private function initCategories():void {
		const numberOfRows:int = 5;
		const w:int = 208;
		const startY:int = 3;
		var itemH:int;
		var x:int, i:int;
		var y:int = startY;
		while (numChildren > 0) removeChildAt(0); // remove old contents

		for (i = 0; i < categories.length; i++) {
			if (i == numberOfRows) {
				x = (w / 2) - 3;
				y = startY;
			}
			var entry:Array = Specs.entryForCategory(categories[i]);
			var item:PaletteSelectorItem = new PaletteSelectorItem(entry[0], Translator.map(entry[1]), entry[2], app.interp.sageDesignMode, app.interp.sagePlayMode, sageCategories[entry[0]]);
			itemH = item.height;
			item.x = x;
			item.y = y;
			addChild(item);
			y += itemH;
		}
		setWidthHeightColor(w, startY + (numberOfRows * itemH) + 5);
	}

	private function setWidthHeightColor(w:int, h:int):void {
		var g:Graphics = graphics;
		g.clear();
		g.beginFill(0xFFFF00, 0); // invisible (alpha = 0) rectangle used to set size
		g.drawRect(0, 0, w, h);
	}
	
	

}}