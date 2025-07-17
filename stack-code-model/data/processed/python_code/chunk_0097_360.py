/**
* @author Arnaud FOUCAL - afoucal@free.fr - http://afoucal.free.fr
* 
* @licence
* http://creativecommons.org/licenses/by/3.0/
* Just give my name and the url of my blog somewhere where you use the component
* 
* @version v1.0
* - first release
* - extends the VBox and is composed of 2 HBoxes : 1 for the buttons level (buttonBar), the 2nd for the children level (mainBar)
* - can be shown or hiden using buttons
* - CSS styles can be applied to the buttonBar and the mainBar to suit with the application theme.
*
* @known issues
* 1- For Flex applications : the StatusBar is not resized when the browser window is reduced (although the resize event listener in the application)
* 	 To adress this issue, the width of the AppStatusBar is "reset" in the updateDisplayLit function using the owner.width.
* 2- For AIR application (consequence of the previous solution) : owner.width generates an error in AIR apps. The error is simply catched, nothing is done.
* 
* @usage
* 	- New components have to be added explicitly in the mainBar
* 	- widthPercents have to be specified each time a new component is added to the mainBar. Otherwise, the width of all components will be equal
* 
* 	! Warning !
* 	Required to switch off the compilation strict mode
* 
*/

package com 
{
	import mx.containers.HBox;
	import mx.containers.VBox;
	import mx.controls.Image;
	import mx.controls.Label;
	import mx.effects.Resize;
	import mx.states.*;
	
	import com.LogComboBox;
	
	public class AppStatusBar extends VBox
	{
		/*==================================================================
			CONSTRUCTOR
		==================================================================*/
		public function AppStatusBar() 
		{
			super();
		}
		
		
		/*==================================================================
			METHODS
		==================================================================*/
		
		
		/**
		 * @private
		 * Set the default ratio of width when a component is added to the mainBar
 		 * 
		 * @return an array of the default width for each component
		 */
		private function setDefaultWidth() :Array
		{
			var arr:Array = new Array();
			var w:Number = 100 / (( mainBar.numChildren > 0 ) ? mainBar.numChildren : 1 );
			
			for (var i:Number = 0 ; i < mainBar.numChildren ; i++)
			{
				arr.push( w );
			}

			return arr;
		}
		
		
		/*==================================================================
			PROPERTIES
		==================================================================*/
		
		
		public var buttonBar:HBox;
		private var openButton:Image;
		private var closeButton:Image;
		
		public var mainBar:HBox;
		public var statusField:Label;
		
		/**
		 * Show the StatuBar
		 */
		private var _shown:Boolean = true;
		public function get shown() :Boolean
		{
			return _shown;
		}
		public function set shown( b:Boolean ) :void
		{
			_shown = b;
			(b) ? currentState = '' : currentState = 'barHidden';
		}		
		
		
		/**
		 * Determine if the status field must be shown
		 */
		private var _showStatusField:Boolean = true;
		public function get showStatusField():Boolean
		{
			return _showStatusField;
		}
		public function set showStatusField( b:Boolean ) :void
		{
			_showStatusField = b;
			
			if (b)
			{
				// always adds the status field at the first position in the mainBar
				mainBar.addChildAt( statusField, 0);
			}
			else
			{
				mainBar.removeChild( statusField );
			}
		}
		
		
		/**
		 * Defines the status string to be displayed in the status bar of the application
		 */
		private var _status:String;
		public function get status():String
		{
			return statusField.text;
		}
		public function set status( s:String ):void
		{
			statusField.text = s;
		}
		
		
		/**
		 * Define a fake 'percentWidth' of each children in the mainBar
		 * If its length is not the same than the number of children in the mainBar, a default ratio of width will be calculated (equal width for all components in the Bar)
		 */
		private var _widthPercents:Array = new Array();
		public function get widthPercents() :Array
		{
			return _widthPercents;
		}
		public function set widthPercents( arr:Array ) :void
		{
			var sum:Number = 0;
			
			for (var i:Number = 0 ; i < arr.length ; i++)
			{
				sum += arr[i];
			}

			if ( sum == 100)
			{
				_widthPercents = arr;
				invalidateDisplayList();
			}
			else
			{
				throw new Error( "Invalid values in widthPercents property. The sum must equal to 100" );
			}
	
		}
		

		/**
		 * Defines the icon for open button of the Bar
		 */
		private var _openButtonIcon:Class;
		public function get openButtonIcon() :Class
		{
			return _openButtonIcon;
		}
		public function set openButtonIcon( c:Class ) :void
		{
			_openButtonIcon = c;
		}
		
		/**
		 * Defines the icon for close button of the Bar
		 */
		private var _closeButtonIcon:Class;
		public function get closeButtonIcon() :Class
		{
			return _closeButtonIcon;
		}
		public function set closeButtonIcon( c:Class ) :void
		{
			_closeButtonIcon = c;
		}
		
		
		/*==================================================================
			OVERRIDES
		==================================================================*/

		
		/**
		 * @inheritDoc
		 */
		override protected function createChildren() :void
		{
			super.createChildren();

			/*
			 * Add the HBox for open/close buttons
			 */
			buttonBar = new HBox();
			addChild( buttonBar );
			
			/*
			 * Add the open/close buttons
			 */
			openButton = new Image();
			openButton.addEventListener( 'click', function():void
				{
					currentState = '';
				} );
			buttonBar.addChild( openButton );
			
			closeButton = new Image();
			closeButton.addEventListener( 'click', function():void
				{
					currentState = 'barHidden';
				});
			buttonBar.addChild( closeButton );
			
			/*
			 * Add the HBox for the components of the statusBar
			 */
			mainBar = new HBox();
			addChild( mainBar );
			
			/*
			 * Add the status Label
			 */
			statusField = new Label();
			mainBar.addChild( statusField );
			
			/*
			 * Define states of the component
			 */
			var state1:State = new State();
			state1.name = "barHidden";
			var setProperty1:SetProperty = new SetProperty(mainBar, "height", 0);
			state1.overrides.push( setProperty1 );
			
			states = new Array();
			states.push( state1 );
			
			/*
			 * Define the transitions between the 2 states of the StatusBar
			 */
			var effectOnBar:Resize = new Resize();
			effectOnBar.duration = 300;
			effectOnBar.target = mainBar;
			
			var to_hiddenBar:Transition = new Transition();
			to_hiddenBar.toState = 'barHidden';
			to_hiddenBar.effect = effectOnBar;
			transitions.push( to_hiddenBar );
			
			var from_hiddenBar:Transition = new Transition();
			from_hiddenBar.fromState = 'barHidden';
			from_hiddenBar.effect = effectOnBar;
			transitions.push( from_hiddenBar );
		}
		
		
		/**
		 * @inheritDoc
		 */
		override protected function commitProperties() :void
		{
			super.commitProperties();
			
			horizontalScrollPolicy = "off";
			percentWidth = 100;
			
			with (buttonBar)
			{
				percentWidth = 100;
				setStyle( 'verticalAlign', 'middle' );
			}
			
			with (openButton)
			{
				scaleContent = true;
				toolTip = "Show the status bar";
				buttonMode = true;
				source = _openButtonIcon;
			}
			
			with (closeButton)
			{
				scaleContent = true;
				toolTip = "Hide the status bar";
				buttonMode = true;
				source = _closeButtonIcon;
			}
			
			with (mainBar)
			{
				percentWidth = 100;
			}
			
			with (statusField)
			{
				truncateToFit = true;
			}
		}
		
		
		/**
		 * @inheritDoc
		 * @param	unscaledWidth
		 * @param	unscaledHeight
		 */
		override protected function updateDisplayList( unscaledWidth:Number, unscaledHeight:Number ) :void
		{
			super.updateDisplayList( unscaledWidth, unscaledHeight );
			
			// See known issue at the top about this error catching
			try
			{
				width = owner.width;			
			}
			catch ( err:TypeError )
			{
				// nothing
			}
			
			// If the number of component in the mainBar doesn't match with the length of the property _widthPercents
			if ( mainBar.numChildren != _widthPercents.length )
				// then assign default and equal width
				_widthPercents = setDefaultWidth();

			var n:Number = mainBar.numChildren;
			
			// sum of different kind of width
			var paddingsWidth:Number = mainBar.getStyle( 'paddingLeft' ) + mainBar.getStyle( 'paddingRight' );
			var borderMetricsWidth:Number = mainBar.borderMetrics.left + mainBar.borderMetrics.right + borderMetrics.left + borderMetrics.right;
			var gapWidth:Number = ( (n) > 1 ? n-1 : 0 ) * mainBar.getStyle( 'horizontalGap' );

			for ( var i:Number = 0 ; i < n ; i++ )
			{
				// Assign the calculated width of each component using the ratio given in the widthPercents property
				mainBar.getChildAt(i).width = ( width - paddingsWidth - borderMetricsWidth - gapWidth) * ( _widthPercents[i] / 100 );
			}
		}
	}
}