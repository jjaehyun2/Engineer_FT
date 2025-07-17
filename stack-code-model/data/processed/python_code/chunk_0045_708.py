/*
Copyright (c) Lightstreamer Srl

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
package flex_demo {
	
	import com.lightstreamer.as_client.item_renderers.HighlightCellItemRenderer;
	import mx.formatters.NumberFormatter;

	public class CustomHighlightCellItemRenderer extends HighlightCellItemRenderer {
		
		public var formatter:NumberFormatter = null;		
		public var isChangeField:Boolean = false;
		
		public override function newInstance():* {
			var instance:CustomHighlightCellItemRenderer = new CustomHighlightCellItemRenderer();
		
			this.decorateNewInstance(instance);
			
			instance.formatter = new NumberFormatter();
			instance.formatter.precision = 2;
			
			return instance;
		}
		
		protected override function formatValue(newVal:String, oldVal:String):String {
			return formatter.format(newVal);
		}
	}
}