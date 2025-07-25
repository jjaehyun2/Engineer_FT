/*******************************************************************************
* The MIT License
* 
* Copyright (c) 2011 Jens Struwe.
* 
* Permission is hereby granted, free of charge, to any person obtaining a copy
* of this software and associated documentation files (the "Software"), to deal
* in the Software without restriction, including without limitation the rights
* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
* copies of the Software, and to permit persons to whom the Software is
* furnished to do so, subject to the following conditions:
* 
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
* 
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
* THE SOFTWARE.
******************************************************************************/
package com.sibirjak.angara.core {

	import flash.events.IEventDispatcher;

	/**
	 * Defines the progress information of loader items.
	 * 
	 * <p>The progress information contains number of the items to be loaded
	 * within an item, the number of items loaded and the number of items failed.</p>
	 * 
	 * <p>The progress value of the progress information returns the overall progress
	 * of the particular loader item. If the item is of type LoaderItemType.LOADER,
	 * the progress value returns the progress only of that single item.</p>
	 * 
	 * @author jes 10.02.2009
	 */
	public interface IProgressInfo extends IEventDispatcher {
		
		/**
		 * Returns the number of items to be loaded within the loader item.
		 * 
		 * <p>If the item is of type LoaderItemType.LOADER the number will be
		 * always 1.</p>
		 * 
		 * <p>If the item is of type LoaderItemType.SEQUENCE, the method returns
		 * the number of all loaders added to the sequence. Removing a loader from
		 * the sequence will decrease this value by 1.</p>
		 * 
		 * <p>If the item is of type LoaderItemType.SEQUENCE_MANAGER, the method
		 * returns the cumulative number of items of all assigned sequences.
		 * The value will be calculated at runtime.</p>
		 * 
		 * @return The number of items to be loaded.
		 */
		function get numItems() : uint;

		/**
		 * Returns the number of items loaded within the loader item.
		 * 
		 * <p>If the item is of type LoaderItemType.LOADER the number will be zero
		 * initally and 1, after the loader has been completed successfully.</p>
		 * 
		 * <p>If the item is of type LoaderItemType.SEQUENCE, the method returns
		 * the number of all completed loaders added to the sequence.</p>
		 * 
		 * <p>If the item is of type LoaderItemType.SEQUENCE_MANAGER, the method
		 * returns the cumulative number of loaded items of all assigned sequences.
		 * The value will be calculated at runtime.</p>
		 * 
		 * @return The number of items succesfully loaded.
		 */
		function get numItemsLoaded() : uint;

		/**
		 * Returns the number of items failed within the loader item.
		 * 
		 * <p>If the item is of type LoaderItemType.LOADER the number will be zero
		 * initally and 1, if the loader could not successfully finish loading. In this
		 * case numItemsLoaded() will return zero.</p>
		 * 
		 * <p>If the item is of type LoaderItemType.SEQUENCE, the method returns
		 * the number of all failed loaders added to the sequence.</p>
		 * 
		 * <p>If the item is of type LoaderItemType.SEQUENCE_MANAGER, the method
		 * returns the cumulative number of failed items of all assigned sequences.
		 * The value will be calculated at runtime.</p></p>
		 * 
		 * @return The number of items failed loading.
		 */
		function get numItemsFailed() : uint;

		/**
		 * Returns the progress of the loader item as a decimal value between zero and 1.
		 * 
		 * <p>If the item is of type LoaderItemType.LOADER the number will be zero
		 * initally and 1, after the loader has been completed successfully. The progress
		 * will not be reset if the loader fails e.g. after a progress of 0.5. It is guaranteed,
		 * that the progress value is set to 1 at the time the COMPLETE event is dispatched.</p>
		 * 
		 * <p>If the item is of type LoaderItemType.SEQUENCE, the method returns the overall
		 * progress of that sequence. It is possible specify a weight to each added loader to
		 * achieve a unbalanced distibution of loader progress values.</p>
		 * 
		 * <p>If the item is of type LoaderItemType.SEQUENCE_MANAGER, the method
		 * returns the arithmetic average of the progress of all assigned sequences.
		 * The value will be calculated at runtime.</p></p>
		 * 
		 * @return The overall progress of the particular loader item.
		 */
		function get progress() : Number;

	}
}