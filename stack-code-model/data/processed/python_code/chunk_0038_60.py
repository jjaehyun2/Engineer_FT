/*
   Copyright aswing.org, see the LICENCE.txt.
 */

package org.aswing
{
	import org.aswing.AbstractButton;
	import org.aswing.border.EmptyBorder;
	import org.aswing.decorators.ColorBackgroundDecorator;
	import org.aswing.decorators.ColorDecorator;
	import org.aswing.geom.IntDimension;
	import org.aswing.layout.BorderLayout;
	import org.aswing.plaf.basic.BasicDropDownButtonUI;
	import org.aswing.plaf.basic.BasicToggleButtonUI;
	
	/**
	 * An implementation of a two-state button.
	 * The <code>JRadioButton</code> and <code>JCheckBox</code> classes
	 * are subclasses of this class.
	 * @author iiley
	 */
	public class JDropDownButton extends AbstractButton
	{
		/**
		 * A fast access to AsWingConstants Constant
		 * @see org.aswing.AsWingConstants
		 */
		public static const CENTER:int = AsWingConstants.CENTER;
		/**
		 * A fast access to AsWingConstants Constant
		 * @see org.aswing.AsWingConstants
		 */
		public static const TOP:int = AsWingConstants.TOP;
		/**
		 * A fast access to AsWingConstants Constant
		 * @see org.aswing.AsWingConstants
		 */
		public static const LEFT:int = AsWingConstants.LEFT;
		/**
		 * A fast access to AsWingConstants Constant
		 * @see org.aswing.AsWingConstants
		 */
		public static const BOTTOM:int = AsWingConstants.BOTTOM;
		/**
		 * A fast access to AsWingConstants Constant
		 * @see org.aswing.AsWingConstants
		 */
		public static const RIGHT:int = AsWingConstants.RIGHT;
		
		private var popup:JPopup;
		private var popupGap:int;
		
		private var horizontalAlignment:int = AsWingConstants.RIGHT;
		private var popupOffset:int;
		
		public function JDropDownButton(text:String = "32", icon:Icon = null, isSelected:Boolean = false, popupOrComponent:* = null)
		{
			super(text, icon);
			setName("JDropDownButton");
			setModel(new ToggleButtonModel());
			setPopupGap(4);
			setHorizontalAlignment(AbstractButton.LEFT);
			setSelected(isSelected);
			
			if (popupOrComponent)
			{
				if (popupOrComponent is JPopup)
					setPopup(popupOrComponent);
				else if (popupOrComponent is Component)
					createPopupFromComponent(popupOrComponent);
			}
			
			updateUI();
		}
		
		public function createPopupFromComponent(component:Component):void
		{
			var popup:JPopup = getPopup();
			popup.append(component);
			setPopup(popup);
		}
		
		public function getPopup():JPopup
		{
			if (popup == null)
			{
				popup = new JPopup(root, false);
				popup.setLayout(new BorderLayout());
				//popup.append(getScollPane(), BorderLayout.CENTER);
				popup.buttonMode = true;
				//popup.setAlpha(0.5);
				//popup.setClipMasked(false);
				popup.setSize(new IntDimension(100, 100));
				//popup.setBackgroundDecorator(new ColorBackgroundDecorator(new ASColor(0x000000, 0.14), new ASColor(0XFFFFFF, 0), 4));
				//popup = btn.getPopup();
				
				var id:ColorDecorator = new ColorDecorator(new ASColor(0x0F1E1C, 1), new ASColor(0XFFFFFF, 0.24), 4);
				//var id:ColorDecorator = new ColorDecorator(new ASColor(0x161C1F, 1), new ASColor(0XFFFFFF, 0.24), 4);
				//var id:ColorDecorator = new ColorDecorator(new ASColor(0x0F151E, 1), new ASColor(0XFFFFFF, 0.24), 4);
				//var id:ColorDecorator = new ColorDecorator(new ASColor(0X000000, 0.08), new ASColor(0XFFFFFF, 0.24), 4);
				id.setGaps(-2, 1, 1, -2);
				//id.setGaps(-1, 0, 0, 0);
				popup.setBackgroundDecorator(id);
			}
			return popup;
		}
		
		public function setPopup(popup:JPopup):void
		{
			this.popup = popup;
		}
		
		public function setPopupAlignment(alignment:Number):void
		{
			if (alignment == horizontalAlignment)
			{
				return;
			}
			else
			{
				horizontalAlignment = alignment;
				repaint();
			}
		}
		
		public function getPopupAlignment():Number
		{
			return horizontalAlignment;
		}
		
		override public function updateUI():void
		{
			//setUI(UIManager.getUI(this));
			setUI(new BasicDropDownButtonUI);
		}
		
		override public function getDefaultBasicUIClass():Class
		{
			return org.aswing.plaf.basic.BasicDropDownButtonUI;
		}
		
		override public function getUIClassID():String
		{
			return "ButtonUI";
		}
		
		/**
		 * Returns the ui for this combobox with <code>ComboBoxUI</code> instance
		 * @return the combobox ui.
		 */
		public function getDropDownButtonUI():BasicDropDownButtonUI
		{
			return getUI() as BasicDropDownButtonUI;
		}
		
		/**
		 * Enables the combo box so that items can be selected. When the
		 * combo box is disabled, items cannot be selected and values
		 * cannot be typed into its field (if it is editable).
		 *
		 * @param b a boolean value, where true enables the component and
		 *          false disables it
		 */
		override public function setEnabled(b:Boolean):void
		{
			super.setEnabled(b);
			if (!b && isPopupVisible())
			{
				setPopupVisible(false);
			}
		}
		
		/**
		 * Causes the combo box to display its popup window.
		 * @see #setPopupVisible()
		 */
		public function showPopup():void
		{
			setPopupVisible(true);
		}
		
		/**
		 * Causes the combo box to close its popup window.
		 * @see #setPopupVisible()
		 */
		public function hidePopup():void
		{
			setPopupVisible(false);
		}
		
		/**
		 * Sets the visibility of the popup, open or close.
		 */
		public function setPopupVisible(v:Boolean):void
		{
			getDropDownButtonUI().setPopupVisible(this, v);
		}
		
		public function setArrowIconVisible(v:Boolean):void
		{
			getDropDownButtonUI().setArrowIconVisible(v);
		}
		
		public function getArrowIconVisible():Boolean
		{
			return getDropDownButtonUI().getArrowIconVisible();
		}
		
		/**
		 * Determines the visibility of the popup.
		 *
		 * @return true if the popup is visible, otherwise returns false
		 */
		public function isPopupVisible():Boolean
		{
			return getDropDownButtonUI().isPopupVisible(this);
		}
		
		public function getPopupGap():int
		{
			return popupGap;
		}
		
		public function setPopupGap(gap:int):void
		{
			popupGap = gap;
		}
		
		public function setPopupOffset(offset:int):void
		{
			popupOffset = offset;
		}
		
		public function getPopupOffset():int
		{
			return popupOffset;
		}
	
	}

}