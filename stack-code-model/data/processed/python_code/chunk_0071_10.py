package devoron.components.buttons
{
	//import org.aswing.graphics.Pen;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.filters.GlowFilter;
	import org.aswing.AbstractButton;
	import org.aswing.ASColor;
	import org.aswing.AssetIcon;
	import org.aswing.event.AWEvent;
	import org.aswing.ext.FormRow;
	import org.aswing.geom.IntDimension;
	import org.aswing.GroundDecorator;
	import org.aswing.Icon;
	import org.aswing.Insets;
	import org.aswing.JButton;
	import org.aswing.JCheckBox;
	import org.aswing.JToggleButton;
	import org.aswing.LoadIcon;
	import org.aswing.plaf.basic.BasicButtonUI;
	import org.aswing.skinbuilder.ButtonStateObject;
	
	/**
	 * Кнопка.
	 * @author Devoron
	 */
	public class DropDownButton extends AboutButton
	{
		[Embed(source="../../../../assets/icons/commons/ddb_close_icon8.png")]
		private const CLOSE_BTN_ICON:Class;
		public var internalChB:JCheckBox = null;
		public var internalCloseBtn:JButton = null;
		
		protected var relatedFormRow:FormRow = null;
		protected var selectionFunction:Function = null;
		protected var closeFunction:Function = null;
		
		/**
		 *
		 * @param	text
		 * @param	useSelectedMode возможность работать с внутренним чекбоксом
		 * @param	useCloseMode возможность работать с кнопкой закрытия(удаления)
		 */
		public function DropDownButton(text:String = "", relatedFormRow:FormRow = null, useSelectMode:Boolean = true, useCloseMode:Boolean = false)
		{
			super(text, null);
			super.buttonMode = true;
			super.setWidth(160);
			selectedTextColor = new ASColor(0xFFFFFF, 0.5);
			setPreferredWidth(160);
			setPreferredHeight(20);
			setHeight(20);
			setHorizontalAlignment(AbstractButton.LEFT);
			(super.getUI() as BasicButtonUI).setTextGap(35);
			super.setForeground(new ASColor(0xFFFFFF, 0.3));
			
			this.relatedFormRow = relatedFormRow;
			
			// внутренний компонент - чекбокс
			if (useSelectMode)
			{
				internalChB = new JCheckBox("");
				internalChB.setSizeWH(20, 18);
				internalChB.x = 12;
				internalChB.y = 2;
				super.addChild(internalChB);
			}
			
			// внутренний компонент - закрывающая кнопка
			if (useCloseMode)
			{
				internalCloseBtn = new JButton("", new AssetIcon(new CLOSE_BTN_ICON));
				internalCloseBtn.setPreferredSize(new IntDimension(15, 15));
				internalCloseBtn.setSizeWH(20, 18);
				internalCloseBtn.setFocusable(false);
				internalCloseBtn.setBackgroundDecorator(null);
				internalCloseBtn.setMargin(new Insets());
				internalCloseBtn.setBorder(null);
				internalCloseBtn.setMideground(null);
				internalCloseBtn.setStyleTune(null);
				internalCloseBtn.x = 30;
				internalCloseBtn.y = 2;
				super.addChild(internalCloseBtn);
				super.addEventListener(MouseEvent.MOUSE_MOVE, mouseMoveHandler);
				super.addEventListener(MouseEvent.MOUSE_OUT, mouseMoveHandler);
			}
			
			super.addEventListener(MouseEvent.CLICK, mouseClickHandler);
		
		}
		
		override public function repaint():void 
		{
			super.repaint();
			
			// ВРЕМЕННЫЙ КОСТЫЛЬ!
			if(internalCloseBtn)
			internalCloseBtn.x = getSize().width - 24;
		}
		
		private function showOrHideRelatedFR():void
		{
			if (relatedFormRow != null)
				relatedFormRow.setVisible(!relatedFormRow.isVisible());
		}
		
		public function setCheckboxSelected(b:Boolean):void
		{
			internalChB.setSelected(b);
		}
		
		public function isCheckboxSelected():Boolean
		{
			return internalChB.isSelected();
		}
		
		public function addCheckboxActionListener(listener:Function, priority:int = 0, useWeakReference:Boolean = false):void
		{
			internalChB.addActionListener(listener, priority, useWeakReference);
		}
		
		public function removeCheckboxActionListener(listener:Function):void
		{
			internalChB.removeActionListener(listener);
		}
		
		public function addCloseButtonActionListener(listener:Function, priority:int = 0, useWeakReference:Boolean = false):void
		{
			internalCloseBtn.addActionListener(listener, priority, useWeakReference);
		}
		
		public function removeCloseButtonActionListener(listener:Function):void
		{
			internalCloseBtn.removeActionListener(listener);
		}
		
		/**
		 * Обработчик щелчка мыши, чтобы проверить вхождение
		 * во внутренний компонент - чекбокс и, при необходимости,
		 * кнопку закрытия.
		 * Если ни чекбокс, ни кнопка закрытия не обработали событие,
		 * то его обрабатывает сам компонент.
		 * @param	e
		 */
		private function mouseClickHandler(e:MouseEvent):void
		{
			if (internalChB)
			{
				if (internalChB.hitTestMouse())
				{
					internalChB.setSelected(!internalChB.isSelected());
					internalChB.dispatchEvent(new AWEvent(AWEvent.ACT));
					if (selectionFunction != null)
						selectionFunction.call(null, internalChB.isSelected());
					return;
				}
			}
			
			if (internalCloseBtn)
			{
				if (internalCloseBtn.hitTestMouse())
				{
					internalCloseBtn.dispatchEvent(new AWEvent(AWEvent.ACT));
					if (closeFunction != null)
						closeFunction.call();
					return;
				}
			}
			
			// скрыть или показать вложенный FormRow
			showOrHideRelatedFR();
		}
		
		/**
		 * Обработчик движения мыши.
		 * @param	e
		 */
		private function mouseMoveHandler(e:MouseEvent):void
		{
			if (internalCloseBtn.getRect(super).contains(e.localX, e.localY))
			{
				internalCloseBtn.filters = [new GlowFilter(0xDEE4DE, 1, 3, 3, 2)];
			}
			else
			{
				internalCloseBtn.filters = null;
			}
		}
		
		public function showRelatedFormRow():void
		{
			relatedFormRow.setVisible(true);
		}
		
		public function hideRelatedFormRow():void
		{
			relatedFormRow.setVisible(false);
		}
		
		public function getRelatedFormRow():FormRow
		{
			return relatedFormRow;
		}
		
		public function setRelatedFormRow(value:FormRow, makeVisible:Boolean = true):void
		{
			relatedFormRow = value;
			relatedFormRow.setVisible(makeVisible);
		}
		
		public function setSelectionFunction(value:Function):void
		{
			selectionFunction = value;
		}
		
		public function setCloseFunction(value:Function):void
		{
			closeFunction = value;
		}
	
	}

}