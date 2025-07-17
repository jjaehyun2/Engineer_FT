package dom.tidesdk.ui
{
	/**
	 * <p>A module used for accessing clipboard data. 
	 * <br/> Please refer to the code examples below:</p>
	 * 
	 *   <pre><code>//Code below stores text into the
	 * clipboard.     <a
	 * href="#!/api/Ti.UI.Clipboard-method-setData"
	 * rel="Ti.UI.Clipboard-method-setData"
	 * class="docClass">Ti.UI.Clipboard.setData</a>('text/plain',
	 * 'This is my custom text');         //Retrieving
	 * the stored data. <a
	 * href="#!/api/Ti.UI.Clipboard-method-getData"
	 * rel="Ti.UI.Clipboard-method-getData"
	 * class="docClass">Ti.UI.Clipboard.getData</a>('text/plain');
	 * //should return 'This is my custom text'
	 * </code></pre>
	 * 
	 *   <h2>Working with text only</h2>
	 * 
	 *   <p>For setting text/plain data, rather than
	 * using the above methods, you may use the
	 * setText/getText methods.</p>
	 * 
	 *   <pre><code><a
	 * href="#!/api/Ti.UI.Clipboard-method-setText"
	 * rel="Ti.UI.Clipboard-method-setText"
	 * class="docClass">Ti.UI.Clipboard.setText</a>('This
	 * is my custom text'); <a
	 * href="#!/api/Ti.UI.Clipboard-method-getText"
	 * rel="Ti.UI.Clipboard-method-getText"
	 * class="docClass">Ti.UI.Clipboard.getText</a>();
	 * //should return 'This is my custom text'
	 * </code></pre>
	 */
	public class TClipboard
	{
		//
		// METHODS
		//

		/**
		 * <p>Clear data of the given mime-type from the
		 * clipboard. If no mime-type is given, clear all
		 * data from the clipboard.</p>
		 * 
		 * @param type  The mime-type of the data to clear. 
		 */
		public function clearData(type:String=null):void {}

		/**
		 * <p>Clear the text portion of the clipboard.</p>
		 */
		public function clearText():void {}

		/**
		 * <p>Get the data on the clipboard from the portion
		 * which contains data of the given mime-type.</p>
		 * 
		 * @param type  The mime-type of the data to get. 
		 * 
		 * @return String   
		 */
		public function getData(type:String):String { return ""; }

		/**
		 * <p>Get the current text on the clipboard.</p>
		 * 
		 * @return String   
		 */
		public function getText():String { return ""; }

		/**
		 * <p>Return true if there is any content of the
		 * given mime-type on the clipboard.</p>
		 * 
		 * @param type  The mime-type of the data to check. 
		 * 
		 * @return Boolean   
		 */
		public function hasData(type:String=null):Boolean { return false; }

		/**
		 * <p>Return true if there is any content in the text
		 * portion of the clipboard.</p>
		 * 
		 * @return Boolean   
		 */
		public function hasText():Boolean { return false; }

		/**
		 * <p>Set the data on the clipboard given a mime-type
		 * and the new data. This method will set data on the
		 * appropriate portion of the clipboard for the given
		 * mime-type.</p>
		 * 
		 * @param type  The mime-type of the data to set. 
		 * @param data  The new clipboard text. 
		 */
		public function setData(type:String, data:String):void {}

		/**
		 * <p>Set the text on the clipboard. This will
		 * overwrite the current contents of the
		 * clipboard.</p>
		 * 
		 * @param newText  The new clipboard text. If the text is an empty string, the text portion of the clipboard will be cleared. 
		 */
		public function setText(newText:String):void {}

		public function TClipboard() {}
	}
}