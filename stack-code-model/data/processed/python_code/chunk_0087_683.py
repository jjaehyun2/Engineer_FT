package com {
	import controls.Alert.AlertPopUp;
	import controls.events.tips.CustomErrorTipsChangedEvent;
	
	import flash.display.DisplayObject;
	import flash.display.Graphics;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	import flash.utils.Dictionary;
	
	import mx.collections.ArrayCollection;
	import mx.containers.Canvas;
	import mx.controls.Button;
	import mx.core.FlexGlobals;
	import mx.events.FlexEvent;
	import mx.styles.CSSStyleDeclaration;
	
	import vyperlogix.shapes.DrawingHandle;
	import vyperlogix.shapes.DrawingShapes;

	public class CustomErrorTips {
		import mx.controls.ToolTip;
		import mx.managers.ToolTipManager;

		public static const className:String = 'CustomErrorTips';
		
		public static var tips:Object = {};
		
		private static var _watchers_:Array = [];
		
		public static const ERROR_TIP_ABOVE:String = 'errorTipAbove';
		public static const ERROR_TIP_RIGHT:String = 'errorTipRight';
		public static const ERROR_TIP_LEFT:String = '';
		public static const ERROR_TIP_BELOW:String = 'errorTipBelow';
		
		private static var _valid_tip_orientations_:Array = [CustomErrorTips.ERROR_TIP_ABOVE,CustomErrorTips.ERROR_TIP_BELOW,CustomErrorTips.ERROR_TIP_LEFT, CustomErrorTips.ERROR_TIP_RIGHT];
		
		public static var colors:Array = [
			{'label':'Choose...','data':''},
			{'label':'Red','data':'red'},
			{'label':'Orange','data':'haloOrange'},
			{'label':'Yellow','data':'yellow','color':'blue'},
			{'label':'Green','data':'haloGreen'},
			{'label':'Blue','data':'haloBlue'}
		];
		
		private static var _colors:Dictionary = null;

		public static function get_tips_color_for(aColorName:String):String {
			var color:String = null;
			var i:int = ArrayCollectionUtils.findIndexOfItemCaseless(colors,'label',aColorName);
			if (i > -1) {
				color = colors[i].data;
			}
			return color;
		}
		
		public static function get dataProvider():ArrayCollection {
			return new ArrayCollection(CustomErrorTips._valid_tip_orientations_);
		}
		
		public static function set_tips_color(value:String,color:String=null):void {
			if (CustomErrorTips._colors == null) {
				CustomErrorTips._colors = new Dictionary();
				for (var i:String in CustomErrorTips.colors) {
					CustomErrorTips._colors[CustomErrorTips.colors[i].data] = CustomErrorTips.colors[i];
				}
			}
			var aColor:Object = CustomErrorTips._colors[value];
			if (aColor) {
				var cssObj:CSSStyleDeclaration;
				if ( (value is String) && (value.length > 0) ) {
					cssObj = FlexGlobals.topLevelApplication.styleManager.getStyleDeclaration('.errorTip')
					cssObj.setStyle("borderColor", value);
					if ( (color is String) && (color.length > 0) ) {
						cssObj.setStyle("color", color);
					} else {
						if (aColor['color']) {
							cssObj.setStyle("color", aColor['color']);
						} else {
							cssObj.setStyle("color", '#ffffff');
						}
					}
				}
			}
		}

		public static function watch_for_changes(target:*):void {
			if (CustomErrorTips._watchers_.indexOf(target) == -1) {
				CustomErrorTips._watchers_.push(target);
			}
		}
		
		public static function check_for_overlaps():void {
			var aToolTip:ToolTip;
			var aRect:Rectangle;
			var rects:Array = [];
			var rects_dict:Dictionary = new Dictionary();
			var rect_parents_dict:Dictionary = new Dictionary();
			var aBucket:Array;
			for (var target:* in CustomErrorTips.tips) {
				aToolTip = CustomErrorTips.tips[target];
//				trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.1 --> target='+target.toString()+', aToolTip.rect='+aRect.toString());
				if (rect_parents_dict[target.parentDocument] == null) {
					aBucket = [];
				} else {
					aBucket = rect_parents_dict[target.parentDocument];
				}
				aBucket.push(target);
				rect_parents_dict[target.parentDocument] = aBucket;
			}
			
			// Radial layout of tooltips - eventually this code will seek to spread-out all tips around a radial pattern... 
			var deltaY:Number;
			var aTarget:*;
			var largestRect:Rectangle;
			var container:Canvas;
			var overlay_container:*;
			var children:Array;
			var origin:Point = new Point(0,0);
			var container_name:String = CustomErrorTips.className+'_GraphicsOverlay';
			var radius_outer:Number;
			var radius_inner:Number;
			var handler:Function = function (event:FlexEvent):void {
				var handle:DrawingHandle = new DrawingHandle();
				handle.callback = function (h:DrawingHandle,pt:*):void {
					function draw_line(vectorFrom:Object,vectorTo:Object):void {
						graphics.lineStyle(3, 0xff0000);
						try {
							graphics.moveTo(vectorFrom.origin.x,vectorFrom.origin.y);
							graphics.lineTo(vectorTo.origin.x,vectorTo.origin.y);
						} catch (err:Error) {}
					}
					if (pt is Point) {
						//trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.1 --> pt='+pt.toString());
					} else {
						// Draw a line between the outside verticies using the DrawingShapes.drawDash() function to allow those points to be known...
						var aVector1:Object;
						var aVector2:Object;
						for (var i:int = 0; i < h.vectors_for_schema.length-1; i++) {
							aVector1 = h.vectors_for_schema[i];
							aVector2 = h.vectors_for_schema[i+1];
							//trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.1.1 --> i='+i+', (i+1)='+(i+1));
							draw_line(aVector1,aVector2);
						}
						aVector1 = aVector2;
						aVector2 = h.vectors_for_schema[0];
						draw_line(aVector1,aVector2);
					}
				};
				var graphics:Graphics = container.graphics;
				if (graphics is Graphics) {
					if ( (aBucket is Array) && (aBucket.length > 0) ) {
						graphics.lineStyle(1, 0x0000ff);
						if (container.width > container.height) {
							origin.x = (container.width - container.height) + (container.height/2);
							origin.y = container.height/2;
							radius_outer = Math2D.RadiusOfCircleForRectangle(container.height,container.height);
							//trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.2a --> origin='+origin.toString()+', radius_outer='+radius_outer);
						} else if (container.width < container.height) {
							origin.x = container.width/2;
							origin.y = (container.height - container.width) + (container.width/2);
							radius_outer = Math2D.RadiusOfCircleForRectangle(container.width,container.width);
							//trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.2b --> origin='+origin.toString()+', radius_outer='+radius_outer);
						} else {
							origin.x = container.width/2;
							origin.y = container.height/2;
							radius_outer = Math2D.RadiusOfCircleForRectangle(container.width,container.height);
							//trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.2c --> origin='+origin.toString()+', radius_outer='+radius_outer);
						}
						radius_inner = radius_outer*0.1;
						//trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.3 --> aBucket.length='+aBucket.length+', radius_inner='+radius_inner+', radius_outer='+radius_outer);
						DrawingShapes.drawStar( handle, graphics, origin.x, origin.y, aBucket.length + ((aBucket.length % 2) ? 0 : 1), radius_inner, radius_outer, 0); // MathUtils.randRange(0,90) 
					}
				}
				
			};
			for (var parentDocument:* in rect_parents_dict) {
				aBucket = rect_parents_dict[parentDocument];
				if (aBucket.length > 2) {
					var total_height:Number = 0;
					for (var i:String in aBucket) {
						aTarget = aBucket[i];
						aToolTip = CustomErrorTips.tips[aTarget];
						if (aToolTip is ToolTip) {
							aRect = new Rectangle(aToolTip.x,aToolTip.y,aToolTip.width,aToolTip.height);
							rects.push(aRect);
							rects_dict[aRect] = aToolTip;
							total_height += aRect.height;
						} else {
							var ii:int = -1;
						}
					}
					// Is it possible to arrange the tips vertically ?
					// Is is possible to arrange the tips horizontally ?
					// Place a Canvas over the parentDocument ! (Place it in the parentDocument.parentDocument !
					if (parentDocument.parentDocument) {
						container = parentDocument.parentDocument.getChildByName(container_name) as Canvas;
						//trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.4 --> container='+((container) ? container.toString() : container));
						if (container is Canvas) {
							container.graphics.clear();
							container.removeEventListener(FlexEvent.CREATION_COMPLETE, handler);
							parentDocument.parentDocument.removeChild(container);
						}
						overlay_container = parentDocument.parentDocument;
						container = new Canvas();
						container.x = parentDocument.parentDocument.x;
						container.y = parentDocument.parentDocument.y;
						if (parentDocument.parentDocument.container) {
							var pt:Point = new Point(parentDocument.parentDocument.container.x,parentDocument.parentDocument.container.y);
							var pt2:Point = parentDocument.parentDocument.container.localToGlobal(pt);
							var pt3:Point = pt2.subtract(pt);
							container.x = pt.x;
							container.y = pt3.y;
						}
						container.name = container_name;
						container.width = ((parentDocument.parentDocument.container) ? parentDocument.parentDocument.container.width : parentDocument.parentDocument.width);
						container.height = ((parentDocument.parentDocument.container) ? parentDocument.parentDocument.container.height : parentDocument.parentDocument.height);
						container.setStyle('backgroundColor',0x00ff00);
						container.setStyle('backgroundAlpha',0.25);
						//trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.5 --> total_height='+total_height+', container.height='+container.height);
						if (total_height < container.height) {
							//trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.6 --> layout vertically... !!!');
						} else {
							//trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.7 --> container.x='+container.x+', container.y='+container.y+', container.width='+container.width+', container.height='+container.height);
							container.addEventListener(FlexEvent.CREATION_COMPLETE, handler);
							try { parentDocument.parentDocument.addChild(container);}
							catch (err:Error) {
								try {parentDocument.parentDocument.addElement(container);} 
								catch (err:Error) {
									AlertPopUp.surpriseNoOkay('Cannot add an overlay at this time... Sorry !','WARNING ('+CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+').2');
								}
							}
						}
					} else {
						AlertPopUp.surpriseNoOkay('Cannot deal with the request... Sorry !','WARNING ('+CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+').1');
					}
				}
//				aBucket = rect_parents_dict[parentDocument];
//				deltaY = parentDocument.height / rects.length;
//				rects.sortOn(['x','y']);
//				if (deltaY < largestRect.height) {
//					var ii:int = -1;
//				} else {
//					trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.2 --> Cannot layout vertically - Oops !');
//				}
			}

//			var rect1:Rectangle;
//			for (var n:int=0; n < rects.length; n++) {
//				for (var m:int=0; m < rects.length; m++) {
//					if (n != m) {
//						rect1 = rects[n];
//						aRect = rects[m];
//						if (rect1.intersects(aRect)) {
//							aToolTip = rects_dict[aRect];
//							if (aToolTip is ToolTip) {
//								deltaY = Math.abs(aRect.y - (rect1.y+rect1.height));
//								aToolTip.y += deltaY;
//							}
//						}
//					}
//				}
//			}
		}
		
		public static function createToolTip(text:String,target:*,position:Point,tip_orientation:String,use_contentToLocal:Boolean=true):ToolTip {
			var aToolTip:ToolTip;
			//trace(StringUtils.repeatedChars('=',30));
			var is_errorTipAbove:Boolean = false;
			var is_errorTipBelow:Boolean = false;
			var pt:Point = position.clone();
			if (CustomErrorTips._valid_tip_orientations_.indexOf(tip_orientation) > -1) {
				if ( tip_orientation == CustomErrorTips.ERROR_TIP_ABOVE ) {
					pt = pt.subtract(new Point(target.width,0));
					is_errorTipAbove = true;
					//trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.2 --> pt='+pt.toString()+', tip_orientation="'+tip_orientation+'"');
				}
				if ( tip_orientation == CustomErrorTips.ERROR_TIP_LEFT ) {
					//trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.3 --> pt='+pt.toString()+', tip_orientation="'+tip_orientation+'"');
				}
				if ( tip_orientation == CustomErrorTips.ERROR_TIP_BELOW ) {
					pt = pt.subtract(new Point(target.width,0));
					is_errorTipBelow = true;
					//trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.4 --> pt='+pt.toString()+', tip_orientation="'+tip_orientation+'"');
				}
				if ( tip_orientation == CustomErrorTips.ERROR_TIP_RIGHT ) {
					pt = pt.add(new Point(0,20));
					//trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.5 --> pt='+pt.toString()+', tip_orientation="'+tip_orientation+'"');
				}
				var _pt:Point = pt.clone();
				if (use_contentToLocal) {
					_pt = new Point(target.contentToLocal(pt).x,target.contentToGlobal(new Point(0,0)).y);
				}
				//trace(CustomErrorTips.className+'.'+DebuggerUtils.getFunctionName(new Error())+'.6 --> pt='+pt.toString()+', tip_orientation="'+tip_orientation+'"'+', _pt='+_pt.toString());
				aToolTip = ToolTipManager.createToolTip(text, _pt.x, _pt.y, tip_orientation) as ToolTip;
				if (is_errorTipAbove) {
					aToolTip.move(_pt.x,_pt.y-aToolTip.height);
				} else if (is_errorTipBelow) {
					aToolTip.move(_pt.x,_pt.y+target.height);
				}
				CustomErrorTips.tips[target] = aToolTip;
				try {target.dispatchEvent(new CustomErrorTipsChangedEvent(CustomErrorTipsChangedEvent.TYPE_CUSTOM_ERROR_TIPS_CHANGED_EVENT,target));} 
				catch (err:Error) {
					//trace(DebuggerUtils.getFunctionName(new Error())+'.ERROR.1 '+err.toString()+', '+err.getStackTrace());
				}
				//trace(StringUtils.repeatedChars('=',30)+'\n');
			} else {
				AlertPopUp.surpriseNoOkay(tip_orientation+' is not valid !','WARNING');
			}
			return aToolTip;
		}
		
		public static function destroyToolTip(aToolTip:ToolTip):void {
			if (aToolTip is ToolTip) {
				ToolTipManager.destroyToolTip( aToolTip);
			}
		}

		public static function destroyToolTip_for(target:*):void {
			var aToolTip:ToolTip = CustomErrorTips.tips[target];
			CustomErrorTips.destroyToolTip(aToolTip);
		}

		public static function destroyToolTips():void {
			var aToolTip:ToolTip;
			for (var target:* in CustomErrorTips.tips) {
				aToolTip = CustomErrorTips.tips[target];
				CustomErrorTips.destroyToolTip(aToolTip);
			}
		}
	}
}