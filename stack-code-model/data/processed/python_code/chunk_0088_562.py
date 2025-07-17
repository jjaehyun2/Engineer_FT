package org.aswing.components.steppers
{
	
	import flash.globalization.NumberFormatter;
	import org.aswing.Component;
	import org.aswing.EditableComponent;
	import org.aswing.event.*;
	import org.aswing.plaf.*;
	import org.aswing.plaf.basic.BasicNumberStepperUI;
	import org.aswing.plaf.basic.BasicStepperUI;
	import org.aswing.UIManager;
	
	/**
	 * Dispatched when when user finish a stepper input such as
	 * stepper arrow button is released, Enter key is entered, Focus transfered.
	 * @eventType org.aswing.event.AWEvent.ACT
	 * @see #addActionListener()
	 */
	[Event(name="act",type="org.aswing.event.AWEvent")]
	
	/**
	 * Dispatched when the stepper's value changed, number inputed arrow button pressed etc.
	 * @see NumberBoundedRangeModel
	 * @eventType org.aswing.event.InteractiveEvent.STATE_CHANGED
	 */
	[Event(name="stateChanged",type="org.aswing.event.InteractiveEvent")]
	
	/**
	 * A component that combine a input text and two arrow button to let user change a
	 * number value step by step.
	 *
	 * @author iiley
	 */
	public class JNumberStepper extends Component implements EditableComponent
	{
		
		private var model:NumberBoundedRangeModel;
		private var columns:int;
		private var editable:Boolean;
		private var valueTranslator:Function;
		private var valueParser:Function;
		private var unit:Number;
		private var maxChars:int;
		private var restrict:String;
		
		/**
		 * Creates a stepper with the specified columns input text.
		 * Defalut model is a instance of <code>DefaultNumberBoundedRangeModel</code>
		 * @param columns (optional)the number of columns to use to calculate the input text preferred width
		 * @see org.aswing.DefaultNumberBoundedRangeModel
		 */
		public function JNumberStepper(value:Number = 100, min:Number = -100000, max:Number = Number.MAX_VALUE, step:Number = 0.01, columns:int = 3)
		{
			super();
			setColumns(columns);
			
			editable = true;
			valueTranslator = DEFAULT_VALUE_TRANSLATOR;
			valueParser = DEFAULT_VALUE_PARSER;
			unit = step;
			maxChars = 6;
			restrict = "0123456789.\\-";
			setModel(new NumberBoundedRangeModel(value, 0, min, max));
			updateUI();
		}
		
		/**
		 * The default translator translate a int value to a integer string representation.
		 */
		public static const DEFAULT_VALUE_TRANSLATOR:Function = function(value:Number):String
		{
			value = Math.round(value * 1000) / 1000;
			return value + "";
		};
		
		/**
		 * The default parser parse a int value from the string, if NaN, 0 will be returned.
		 */
		public static const DEFAULT_VALUE_PARSER:Function = function(text:String):Number
		{
			var value:Number = Number(text);
			if (isNaN(value))
			{
				value = 0;
			}
			return value;
		};
		
		override public function updateUI():void
		{
			setUI(UIManager.getUI(this));
		}
		
		override public function getDefaultBasicUIClass():Class
		{
			return org.aswing.plaf.basic.BasicNumberStepperUI;
		}
		
		override public function getUIClassID():String
		{
			return "NumberStepperUI";
		}
		
		/**
		 * Sets the number of columns for the input text.
		 * @param columns the number of columns to use to calculate the preferred width.
		 */
		public function setColumns(columns:int):void
		{
			if (columns < 0)
				columns = 0;
			if (this.columns != columns)
			{
				this.columns = columns;
				repaint();
				revalidate();
			}
		}
		
		/**
		 * @see #setColumns
		 */
		public function getColumns():int
		{
			return columns;
		}
		
		public function setMaxChars(n:int):void
		{
			if (maxChars != n)
			{
				maxChars = n;
				repaint();
			}
		}
		
		public function getMaxChars():int
		{
			return maxChars;
		}
		
		public function setRestrict(r:String):void
		{
			if (restrict != r)
			{
				restrict = r;
				repaint();
			}
		}
		
		public function getRestrict():String
		{
			return restrict;
		}
		
		/**
		 * Returns data model that handles the slider's four fundamental properties: minimum, maximum, value, extent.
		 * @return the data model
		 */
		public function getModel():NumberBoundedRangeModel
		{
			return model;
		}
		
		/**
		 * Sets the model that handles the slider's four fundamental properties: minimum, maximum, value, extent.
		 * @param the data model
		 */
		public function setModel(newModel:NumberBoundedRangeModel):void
		{
			if (model != null)
			{
				model.removeStateListener(__onModelStateChanged);
			}
			model = newModel;
			if (model != null)
			{
				model.addStateListener(__onModelStateChanged);
			}
		}
		
		private function __onModelStateChanged(event:InteractiveEvent):void
		{
			dispatchEvent(new InteractiveEvent(InteractiveEvent.STATE_CHANGED, event.isProgrammatic()));
		}
		
		/**
		 * Sets a function(int):String to translator the value to the string representation in
		 * the input text.
		 * <p>
		 * Generally, if you changed translator, you should change a right valueParser to suit it.
		 * @param translator a function(int):String.
		 * @see #getValueTranslator()
		 * @see #setValueParser()
		 */
		public function setValueTranslator(translator:Function):void
		{
			if (valueTranslator != translator)
			{
				valueTranslator = translator;
				repaint();
			}
		}
		
		/**
		 * Returns the value translator function(int):String.
		 * @see #setValueTranslator()
		 */
		public function getValueTranslator():Function
		{
			return valueTranslator;
		}
		
		/**
		 * Sets a function(String):int to parse the value from the string in
		 * the input text.
		 * <p>
		 * Generally, if you changed parser, you should change a right valueTranslator to suit it.
		 * @param parser a function(String):int.
		 * @see #getValueParser()
		 * @see #setValueTranslator()
		 */
		public function setValueParser(parser:Function):void
		{
			if (valueParser != parser)
			{
				valueParser = parser;
				repaint();
			}
		}
		
		/**
		 * Returns the value parser function(String):int.
		 * @see #setValueParser()
		 * @see #getValueTranslator()
		 */
		public function getValueParser():Function
		{
			return valueParser;
		}
		
		public function getUnitIncrement():Number
		{
			return unit;
		}
		
		public function setUnitIncrement(u:Number):void
		{
			unit = u;
		}
		
		/**
		 * Sets whether the stepper is editable to adjust, both the input text and pop-up slider.
		 * @param b true to make the stepper can be edited the value, no to not.
		 * @see #isEditable()
		 */
		public function setEditable(b:Boolean):void
		{
			if (editable != b)
			{
				editable = b;
				repaint();
				revalidate();
			}
		}
		
		/**
		 * Returns whether the stepper is editable.
		 * @return whether the stepper is editable.
		 * @see #setEditable()
		 */
		public function isEditable():Boolean
		{
			return editable;
		}
		
		/**
		 * Returns the slider's value.
		 * @return the slider's value property.
		 * @see #setValue()
		 * @see NumberBoundedRangeModel#getValue()
		 */
		public function getValue():Number
		{
			var value:Number = getModel().getValue();
			var kof:Number = Math.pow(10, 3);
			value = Math.round(value * kof) / kof;
			return value;
		}
		
		/**
		 * Sets the slider's value. This method just forwards the value to the model.
		 * @param value the value to set.
		 * @see #getValue()
		 * @see NumberBoundedRangeModel#setValue()
		 */
		public function setValue(value:Number, programmatic:Boolean = true):void
		{
			var m:NumberBoundedRangeModel = getModel();
			m.setValue(value, programmatic);
		
		}
		
		/**
		 * Returns the "extent" -- the range of values "covered" by the knob.
		 * @return an int representing the extent
		 * @see #setExtent()
		 * @see NumberBoundedRangeModel#getExtent()
		 */
		public function getExtent():Number
		{
			return getModel().getExtent();
		}
		
		/**
		 * Sets the size of the range "covered" by the knob.  Most look
		 * and feel implementations will change the value by this amount
		 * if the user clicks on either side of the knob.
		 *
		 * @see #getExtent()
		 * @see NumberBoundedRangeModel#setExtent()
		 */
		public function setExtent(extent:Number):void
		{
			getModel().setExtent(extent);
		}
		
		/**
		 * Returns the minimum value supported by the slider (usually zero).
		 * @return the minimum value supported by the slider
		 * @see #setMinimum()
		 * @see NumberBoundedRangeModel#getMinimum()
		 */
		public function getMinimum():Number
		{
			return getModel().getMinimum();
		}
		
		/**
		 * Sets the model's minimum property.
		 * @param minimum the minimum to set.
		 * @see #getMinimum()
		 * @see NumberBoundedRangeModel#setMinimum()
		 */
		public function setMinimum(minimum:Number):void
		{
			getModel().setMinimum(minimum);
		}
		
		/**
		 * Returns the maximum value supported by the slider.
		 * @return the maximum value supported by the slider
		 * @see #setMaximum()
		 * @see NumberBoundedRangeModel#getMaximum()
		 */
		public function getMaximum():Number
		{
			return getModel().getMaximum();
		}
		
		/**
		 * Sets the model's maximum property.
		 * @param maximum the maximum to set.
		 * @see #getMaximum()
		 * @see NumberBoundedRangeModel#setMaximum()
		 */
		public function setMaximum(maximum:Number):void
		{
			getModel().setMaximum(maximum);
		}
		
		/**
		 * True if the slider knob is being dragged.
		 * @return the value of the model's valueIsAdjusting property
		 */
		public function getValueIsAdjusting():Boolean
		{
			return getModel().getValueIsAdjusting();
		}
		
		/**
		 * Sets the model's valueIsAdjusting property. Slider look and feel
		 * implementations should set this property to true when a knob drag begins,
		 * and to false when the drag ends. The slider model will not generate
		 * ChangeEvents while valueIsAdjusting is true.
		 * @see NumberBoundedRangeModel#setValueIsAdjusting()
		 */
		public function setValueIsAdjusting(b:Boolean):void
		{
			var m:NumberBoundedRangeModel = getModel();
			m.setValueIsAdjusting(b);
		}
		
		/**
		 * Sets the four NumberBoundedRangeModel properties after forcing the arguments to
		 * obey the usual constraints: "minimum le value le value+extent le maximum"
		 * ("le" means less or equals)
		 */
		public function setValues(newValue:Number, newExtent:Number, newMin:Number, newMax:Number):void
		{
			var m:NumberBoundedRangeModel = getModel();
			m.setRangeProperties(newValue, newExtent, newMin, newMax, m.getValueIsAdjusting());
		}
		
		/**
		 * Adds a action listener to this stepper. Adjuster fire a <code>AWEvent.ACT</code>
		 * event when user finished a adjusting.
		 * @param listener the listener
		 * @param priority the priority
		 * @param useWeakReference Determines whether the reference to the listener is strong or weak.
		 * @see org.aswing.event.AWEvent#ACT
		 */
		public function addActionListener(listener:Function, priority:int = 0, useWeakReference:Boolean = false):void
		{
			addEventListener(AWEvent.ACT, listener, false, priority, useWeakReference);
		}
		
		/**
		 * Removes a action listener.
		 * @param listener the listener to be removed.
		 * @see org.aswing.event.AWEvent#ACT
		 */
		public function removeActionListener(listener:Function):void
		{
			removeEventListener(AWEvent.ACT, listener);
		}
		
		/**
		 * Adds a listener to listen the stepper's state change event.
		 * @param listener the listener
		 * @param priority the priority
		 * @param useWeakReference Determines whether the reference to the listener is strong or weak.
		 * @see org.aswing.event.InteractiveEvent#STATE_CHANGED
		 */
		public function addStateListener(listener:Function, priority:int = 0, useWeakReference:Boolean = false):void
		{
			addEventListener(InteractiveEvent.STATE_CHANGED, listener, false, priority);
		}
		
		/**
		 * Removes a state listener.
		 * @param listener the listener to be removed.
		 * @see org.aswing.event.InteractiveEvent#STATE_CHANGED
		 */
		public function removeStateListener(listener:Function):void
		{
			removeEventListener(InteractiveEvent.STATE_CHANGED, listener);
		}
	}
}