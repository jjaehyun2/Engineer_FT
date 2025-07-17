package devoron.components.hidebuttons
{
	import flash.events.Event;
	import flash.geom.Rectangle;
	import org.aswing.AsWingConstants;
	import org.aswing.AsWingUtils;
	import org.aswing.Component;
	import org.aswing.event.AWEvent;
	import org.aswing.geom.IntPoint;
	import org.aswing.geom.IntRectangle;
	import org.aswing.JPopup;
	import org.aswing.JToggleButton;
	import org.aswing.util.ASTimer;
	
	/**
	 * ...
	 * @author Devoron
	 */
	public class HideButton extends JToggleButton
	{
		private var hideTarget:Component;
		private var hideTargetContainer:Component;
		private var popupTimer:ASTimer;
		
		private var scrollRect2:Rectangle;
		
		public function HideButton(hideTarget:Component = null, hideTargetContainer:Component = null)
		{
			this.hideTargetContainer = hideTargetContainer;
			this.hideTarget = hideTarget;
			addActionListener(onStateChange);
		}
		
		private function onStateChange(e:AWEvent):void
		{
			if (hideTarget)
			{
				hideTarget.setVisible(!isSelected());
				
				/*popupTimer = new ASTimer(70);
				popupTimer.addActionListener(__movePopup);
				//popupTimer.start();
				startMoveToView();*/
				if (hideTargetContainer)
				   {
				   hideTargetContainer.pack();
				   hideTargetContainer.revalidate();
				   }
				   else
				   {
				   hideTarget.getParent().pack();
				 }
			}
		
			//popupTimer = new ASTimer(18);
			//popupTimer = new ASTimer(40);
			//popupTimer.addActionListener(__movePopup);
		
		}
		
		//private var scrollRect:Rectangle;
		
		//return the destination pos
		private function startMoveToView():void
		{
			var moveDir:int = 1;
			//var hideTarget:JPopup = getPopup();
			var height:int = hideTarget.getHeight();
			var popupPaneHeight:int = height;
			var downDest:IntPoint = super.componentToGlobal(new IntPoint(0, super.getHeight()));
			var upDest:IntPoint = new IntPoint(downDest.x, downDest.y - super.getHeight() - popupPaneHeight);
			var visibleBounds:IntRectangle = AsWingUtils.getVisibleMaximizedBounds(hideTarget.parent);
			var distToBottom:int = visibleBounds.y + visibleBounds.height - downDest.y - popupPaneHeight;
			var distToTop:int = upDest.y - visibleBounds.y;
			
			var gp:IntPoint = super.getGlobalLocation();
			//var popupGap:int = (button as JDropDownButton).getPopupGap();
			scrollRect2 = new Rectangle( /*0, height, popupPane.getWidth(), 0*/);
			var popupGap:int = 4;
			if (distToBottom > 0 || (distToBottom < 0 && distToTop < 0 && distToBottom > distToTop))
			{
				moveDir = 1;
				//if((button as JDropDownButton).getPopupAlignment()
				scrollRect2 = new Rectangle( /*0, height, popupPane.getWidth(), 0*/);
				
				var alignment:int = AsWingConstants.LEFT;
				switch (alignment)
				{
					case AsWingConstants.RIGHT: 
						//gp.x = gp.x ;
						break;
					case AsWingConstants.CENTER: 
						scrollRect2 = new Rectangle(0, 0, hideTarget.getWidth(), 0);
						//gp.x = gp.x - popupPane.getWidth() * .5 + button.getWidth() * .5;
						//gp.y -= popupPane.getHeight();
						break;
					case AsWingConstants.LEFT: 
						scrollRect2 = new Rectangle(0, 0, hideTarget.getWidth(), hideTarget.getHeight());
						//gp.x = gp.x - hideTargp.x = gp.x ;get.getWidth() + super.getWidth();
						gp.x = gp.x ;
						break;
					case AsWingConstants.BOTTOM: 
						scrollRect2 = new Rectangle(0, 0, hideTarget.getWidth() * 2, 0);
						gp.x -= hideTarget.getWidth() * .5 - super.getWidth() * .5; // выравниване по левому краю
						gp.y += popupGap + super.getHeight();
						//gp.y += gp.y - popupPane.getHeight() /*+ 20*/;
						break;
				}
				
					//gp.y += /*button.getHeight() - 10 */- popupPane.getHeight()-popupGap/*-button.getHeight() *.5*/;
					//gp.x += popupGap;
					//scrollRect = new Rectangle(0, height, 0, 0);
					//scrollRect = new Rectangle(0, height, popupPane.getWidth(), 0);
			}
			else
			{
				moveDir = -1;
					//scrollRect = new Rectangle(0, 0, popupPane.getWidth(), 0);
			}
			hideTarget.setGlobalLocation(gp);
			
			hideTarget.scrollRect = scrollRect2;
			
			//popupPane.setLocation(new IntPoint(100, 200));
			//scrollRect.width = 0;
			
			//popupTimer.restart();
			popupTimer.start();
		}
		
		protected function __movePopup(e:Event):void
		{
			//var hideTarget: = getPopup();
			
			/*switch ((button as JDropDownButton).getPopupAlignment())
			   {
			   case AsWingConstants.RIGHT:
			   scrollRect.width += speed;
			   break;
			   case AsWingConstants.CENTER:
			   //popupPane.x = speed*2;
			   popupPane.y += speed;
			   scrollRect.height += speed;
			   //scrollRect.width += speed*2;
			   break;
			   case AsWingConstants.LEFT:
			   scrollRect.width += speed;
			   break;
			   case AsWingConstants.BOTTOM:
			   popupPane.x -= speed * 2;
			   popupPane.y += speed * .01;
			   scrollRect.height += speed;
			   scrollRect.width += speed * 2;
			   break;
			 }*/
			
			//scrollRect.width = popupPane.getWidth();
			//hideTarget 
			var popupPaneWidth:int = hideTarget.getWidth();
			var popupPaneHeight:int = hideTarget.getHeight();
			var maxTime:int = 10;
			var minTime:int = 3;
			var speed:int = 50;
			
			//if (!scrollRect)
			//return;
			
			//scrollRect2.width = popupPaneWidth;
			
			var alignment:int = AsWingConstants.LEFT;
			switch (alignment)
			{
				case AsWingConstants.RIGHT: 
				case AsWingConstants.LEFT: 
					if (popupPaneWidth < speed * minTime)
					{
						speed = Math.ceil(popupPaneWidth / minTime);
					}
					else if (popupPaneWidth > speed * maxTime)
					{
						speed = Math.ceil(popupPaneWidth / maxTime);
					}
					
					if (hideTarget.width - scrollRect2.width <= speed)
					{
						//motion ending
						speed = hideTarget.width - scrollRect2.width;
						popupTimer.stop();
					}
					
					break;
				case AsWingConstants.CENTER: 
					if (popupPaneHeight < speed * minTime)
					{
						speed = Math.ceil(popupPaneHeight / minTime);
					}
					else if (popupPaneHeight > speed * maxTime)
					{
						speed = Math.ceil(popupPaneHeight / maxTime);
					}
					
					if (popupPaneHeight - scrollRect2.height <= speed)
					{
						//motion ending
						speed = popupPaneHeight - scrollRect2.height;
						popupTimer.stop();
					}
					//case AsWingConstants.LEFT: 
					break;
			}
			
			/*if (popupPaneWidth < speed * minTime)
			   {
			   speed = Math.ceil(popupPaneWidth / minTime);
			   }
			   else if (popupPaneWidth > speed * maxTime)
			   {
			   speed = Math.ceil(popupPaneWidth / maxTime);
			   }
			
			   if (popupPane.width - scrollRect.width<= speed)
			   {
			   //motion ending
			   speed = popupPane.width - scrollRect.width;
			   popupTimer.stop();
			   }
			 */ /*if (moveDir > 0)
			   {
			   scrollRect.x -= speed;
			   scrollRect.width += speed;
			   }
			   else
			 {*/
			//popupPane.x -= speed;
			//scrollRect2.x = 0;
			//scrollRect2.y = 0;
			//scrollRect2.width = hideTarget.width;
			//scrollRect2.height = hideTarget.height;
			//scrollRect2.width -= hideTarget
			//scrollRect2.width = hideTarget.get
					//scrollRect2.height += speed;
			//scrollRect2.x = hideTarget.x;
					//scrollRect2.y = hideTarget.getLocation().y;
			speed  = 18;
			switch (alignment)
			{
				case AsWingConstants.RIGHT: 
					scrollRect2.width += speed;
					break;
				case AsWingConstants.CENTER: 
					//popupPane.x = speed*2;
					hideTarget.y += speed * 2;
					scrollRect2.height += speed;
					//scrollRect.width += speed*2;
					break;
				case AsWingConstants.LEFT: 
					scrollRect2.width -= speed* .01;
					//scrollRect2.height += speed;
					hideTarget.x += speed * .01;
					//var x1:int = hideTarget.getBounds(hideTarget.getParent()).x;
					//hideTarget.x -= speed;
					//hideTarget.setLocationXY(hideTarget.getLocation().x- speed, hideTarget.getLocation().y);
					break;
				case AsWingConstants.BOTTOM: 
					//popupPane.x -= speed * 2;
					hideTarget.y += speed * .01;
					scrollRect2.height += speed;
					scrollRect2.width += speed * 2;
					break;
			}
			
			//scrollRect.height += speed;
			//}
			hideTarget.scrollRect = scrollRect2;
			//hideTarget.mask = scrollRect2;
		}
		
		public function getHideTarget():Component
		{
			return hideTarget;
		}
		
		public function setHideTarget(component:Component):void
		{
			hideTarget = component;
		}
	
	}

}