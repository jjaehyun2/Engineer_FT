package com.ixiyou.speUI.mcontrols 
{
	import com.greensock.TweenMax;
	import com.ixiyou.speUI.collections.MSprite;
	
	import flash.display.*;
	import flash.events.*;
	import flash.geom.*;
	import flash.utils.*;

	/**
	 * 直接影片转滚动条
	 * 
	 * 
		FLASH里快速创建
		import com.ixiyou.speUI.mcontrols.MovieToVScrollBar;
		var sl:MovieToVScrollBar = new MovieToVScrollBar(_sl,null,true,true);
		box.mask = boxMask;
		sl.content = box;
	 * @author spe email:md9yue@@q.com
	 */
	public class MovieToVScrollBar extends MSprite
	{
		public static const  HITAll:String = 'all_hit'
		public static const  HITSSLIDER:String = 'slider_hit'
		//是否背景点击
		protected var _allowTrackClick:Boolean = true
		//最大;
		protected var _maxScrollPosition:Number = 0;
		//最小
		protected var _minScrollPosition:Number = 0;
		//按下箭头按钮时的滚动量（以像素为单位）。
		protected var _lineScrollSize:Number = 10;
		//按下滚动条轨道时滚动滑块的移动量（以像素为单位）。
		protected var _wheelScrollSize:Number = 10;
		//[read-only] 获取下一个可以滚动的值。该属性为只读
		protected var _nextScroll: Number
		//[read-only] 获取上一个可以滚动的值。该属性为只读 
		protected var _previousScroll: Number
		protected var _hideType:String=HITSSLIDER
		//是否自动隐藏滑块 或者全部
		protected var  _hideBool:Boolean = false
		//滚动轴
		protected var _wheelBool:Boolean = true
		//坐标系对齐
		public var coordinateBool:Boolean=true
		//是否缓动
		public var tweenerBool:Boolean = true
		//缓动时间
		public var tweenerTime:Number = .2
		//鼠标按住事件
		protected var _mouseDownBool:Boolean = false
		//滚动方向
		protected var _scrollSense:Boolean = false
		//延迟滚动时间毫秒
		public var scrollDelay:uint = 350
		protected var _oldDelayTime:uint
		//控制的显示对象
		protected var _content:DisplayObject
		//显示对象对应的遮罩
		protected var _mask:DisplayObject
		//皮肤
		protected var _skin:Sprite
		protected var _slider:MovieToCheck2
		//记录原始滑块大小
		protected var _sliderRect:Rectangle=new Rectangle()
		protected var _sliderBtn:MovieClip
		protected var _nextBtn:SimpleButton
		protected var _previousBtn:SimpleButton
		protected var _scrollBg:DisplayObject
		//是否自动计算
		public var sliderAutoSize:Boolean = true
		protected var sliderPot:Point=new Point()
		//更新
		public static var UPDATA:String = Event.SCROLL
		/**
		 * 创建
		 * @param	skin
		 * @param	config
		 * @param	formerly
		 * @param	parentBool
		 * @return
		 */
		public static function found(skin:Sprite, config:*= null, formerly:Boolean = false, parentBool:Boolean = false):MovieToVScrollBar {
			var vscrollBar:MovieToVScrollBar=new MovieToVScrollBar(skin,config,formerly,parentBool)
			return vscrollBar
		}
		
		
		public function MovieToVScrollBar(skin:Sprite,config:*=null,formerly:Boolean=false,parentBool:Boolean=false)  
		{
			var tempParent:DisplayObjectContainer
			var skinh:uint=100
			if (formerly) {
				this.x = skin.x
				this.y = skin.y
				skinh = skin.getChildByName('_scrollBg').height
				this.height = skinh
			}
			//trace(skinh)
			if (skin.parent && parentBool) {
				tempParent = skin.parent
			}
			if (skin) this.skin = skin
			else return
			if (tempParent) {
				//trace('添加')
				tempParent.addChild(this)
			}
			if (config) {
				if(config.x!=null)
					x = config.x;
				if(config.y!=null)
					y = config.y;
				if(config.autoSize!=null)
					autoSize = config.autoSize;
				if (config.size != null&&config.size is Array)
				{
					width = config.size[0];
					height = config.size[1];
				}
				if (config.width != null)width = config.width;
				if (config.height != null)height = config.height;

				if (config.hideType!=null) hideType = config.hideType
				if (config.scrollDelay) scrollDelay = config.scrollDelay
				if (config.wheelBool!=null)  wheelBool = config.wheelBool
				if (config.hideBool!=null)  hideBool = config.hideBool
				if (config.scrollDelay)  scrollDelay = config.scrollDelay
				if (config.allowTrackClick!=null) allowTrackClick = config.allowTrackClick
				if (config.tweenerBool!=null) tweenerBool = config.tweenerBool
				if (config.tweenerTime) tweenerTime = config.tweenerTime
				if (config.coordinateBool!=null)coordinateBool=config.coordinateBool
				if (config.content!=null) content = config.content
			}
			if (height <= 0) this.height = skinh
			//trace()
		}
		/**
		 * 组件皮肤
		 */
		public function get skin():Sprite { return _skin; }
		
		public function set skin(value:Sprite):void 
		{
			try {
					if (_skin && this.contains(_skin)) removeChild(_skin)
					//if (_skin) {}
					_skin = value;
					var skin1:Sprite=Sprite(_skin)
					addChild(skin1)
					skin1.x=skin1.y=0
					if (_previousBtn) {
						_previousBtn.removeEventListener(MouseEvent.MOUSE_DOWN, btnDown)
					}
					if (Sprite(_skin).getChildByName('_previousBtn')) {
						_previousBtn = Sprite(_skin).getChildByName('_previousBtn') as SimpleButton
						_previousBtn.addEventListener(MouseEvent.MOUSE_DOWN,btnDown)
					}else {
						_previousBtn=new SimpleButton()
					}
				

					
					if (_nextBtn) {
						_nextBtn.removeEventListener(MouseEvent.MOUSE_DOWN, btnDown)
					}
					if (Sprite(_skin).getChildByName('_nextBtn')) {
						_nextBtn = Sprite(_skin).getChildByName('_nextBtn') as SimpleButton
						_nextBtn.addEventListener(MouseEvent.MOUSE_DOWN,btnDown)
					}else {
						_nextBtn=new SimpleButton()
					}
					

					
					_sliderBtn = Sprite(_skin).getChildByName('_sliderBtn') as MovieClip;
					
					_sliderRect.width = _sliderBtn.width
					_sliderRect.height = _sliderBtn.height
					_slider=new MovieToCheck2(_sliderBtn)
					
					addChild(_slider)
					//_slider.setSize(_sliderRect.width,_sliderRect.height)
					_slider.addEventListener(MouseEvent.MOUSE_DOWN,sliderDown)

					if(_scrollBg)_scrollBg.removeEventListener(MouseEvent.MOUSE_DOWN,scrollDown)
					_scrollBg = Sprite(_skin).getChildByName('_scrollBg')
					//_scrollBg.x =0
					_scrollBg.y=0
					_scrollBg.addEventListener(MouseEvent.MOUSE_DOWN, scrollDown)
					_width = Math.max(_scrollBg.width,_sliderBtn.width)
					upSize()	
				}catch (e:TypeError) {
					trace('Error:',e)
					//skin= new VScrollBarSkin()
				}
		}
		/**
		 * 设置内容
		 */
		public function set content(value:DisplayObject):void {
			if (_content == value) return;
			if (value.mask == null) return;
			if (_content && _content.hasEventListener(Event.RESIZE))_content.removeEventListener(Event.RESIZE, contentResize)
			
			_content = value
			_mask = _content.mask
			
			if (_content is InteractiveObject)_content.addEventListener(Event.RESIZE,contentResize)
			if (wheelBool) if (_content is InteractiveObject) InteractiveObject(_content).addEventListener(MouseEvent.MOUSE_WHEEL, MOUSE_WHEEL)
			else if (_content is InteractiveObject) InteractiveObject(_content).removeEventListener(MouseEvent.MOUSE_WHEEL, MOUSE_WHEEL)
			upSlider()
		}
		public function get content():DisplayObject { return _content; }
		/**
		 * 大小改变时候
		 * @param	e
		 */
		private function contentResize(e:Event):void {
			//trace('resize',DisplayObject(e.target).height)
			upSlider()
		}
		/**
		 * 是否支持滚轮
		 */
		public function set wheelBool(value:Boolean):void 
		{
			if (_wheelBool == value) return
			_wheelBool = value
			if (_wheelBool) if (_content is InteractiveObject) InteractiveObject(_content).addEventListener(MouseEvent.MOUSE_WHEEL, MOUSE_WHEEL)
			else if (_content is InteractiveObject) InteractiveObject(_content).removeEventListener(MouseEvent.MOUSE_WHEEL, MOUSE_WHEEL)
		}
		public function get wheelBool():Boolean { return _wheelBool; }
		/**
		 * 是否自动隐藏
		 */
		public function set hideBool(value:Boolean):void 
		{
			if (_hideBool == value) return
			_hideBool = value
			if (_slider) upSlider()
		}
		/**
		 * 是否自动隐藏
		 */
		public function get hideBool():Boolean { return _hideBool; }
		/**
		 * 滚轮事件
		 * @param	e
		 */
		private function MOUSE_WHEEL(e:MouseEvent):void {
			if(!content)return
			if (e.delta < 0) {
				if(content)wheelScrollSize=Number((content.height*.1)>>0)
				scrollToValue(wheelScrollSize,true)
			}else {
				if(content)wheelScrollSize=Number((content.height*.1)>>0)
				scrollToValue(wheelScrollSize,false)
			}
		}
		//背景按下
		private function scrollDown(e:MouseEvent):void {
			if (_scrollBg && e.target != _scrollBg) return
			if(!allowTrackClick)return
			if (content == null) return
			if (this.mouseY > _previousBtn.height && this.mouseY <= _previousBtn.height + pageSize + _slider.height) {
				var num:Number=mouseY
				if (mouseY >= _previousBtn.height + pageSize) num = _previousBtn.height + pageSize
				TweenMax.to(_slider, tweenerTime,{ y:num, 
					onUpdate:function(mc):void { 
						mc.computeContentValue(mc.computeNumFormSlider())
						mc.dispatchEvent(new Event(Event.SCROLL))
					}
					,onUpdateParams:[this]
				})
			}
		}
		
		//前后按钮按下
		private function btnDown(e:MouseEvent):void {
			if (content == null) return
			_mouseDownBool = true
			if (e.target == _nextBtn)_scrollSense = true
			else _scrollSense = false
			scrollToValue(lineScrollSize,_scrollSense)
			_oldDelayTime = getTimer()
			stage.addEventListener(MouseEvent.MOUSE_UP,stageUp)
			addEventListener(Event.ENTER_FRAME,ENTER_FRAME)
		}
		//按钮鼠标放开
		private function stageUp(e:MouseEvent):void {
			_mouseDownBool = false
			stage.removeEventListener(MouseEvent.MOUSE_UP,stageUp)
			removeEventListener(Event.ENTER_FRAME,ENTER_FRAME)
		}
		
		//滑块按下
		private function sliderDown(e:MouseEvent):void {
			if (content == null) return
			sliderPot.x = _slider.mouseX
			sliderPot.y=_slider.mouseY
			_slider.selectLock=false
			_slider.select = true
			_slider.selectLock=true
			stage.addEventListener(MouseEvent.MOUSE_UP, sliderUp)
			stage.addEventListener(MouseEvent.MOUSE_MOVE, sliderMove)
			
		}
		//滑块放开
		private function sliderUp(e:MouseEvent):void {
			_slider.selectLock=false
			_slider.select = false
			_slider.selectLock=true
			stage.removeEventListener(MouseEvent.MOUSE_UP, sliderUp)
			stage.removeEventListener(MouseEvent.MOUSE_MOVE, sliderMove)
			//_slider.stopDrag()
			if(content==null)return
		}
		//滑块移动
		private function sliderMove(e:MouseEvent):void {
			var pt:Point =new Point(0, this.mouseY) 
			if (pt.y < _previousBtn.height+sliderPot.y)pt.y = _previousBtn.height
			else if (pt.y > pageSize+_previousBtn.height+sliderPot.y)pt.y  = pageSize+_previousBtn.height
			else pt.y=pt.y-sliderPot.y
			_slider.y=pt.y 
			computeContentValue(computeNumFormSlider())
		}
		/**
		 * 帧触发
		 * @param	e
		 */
		private function ENTER_FRAME(e:Event):void {
			if (getTimer() - _oldDelayTime > scrollDelay) {
				scrollToValue(lineScrollSize,_scrollSense)
			}
		}
		/**
		 * 设置滚动
		 * @param	value 滚动距离
		 * @param	sense 滚动方向
		 */
		public function scrollToValue(value:Number, sense:Boolean):void {
			if (!computeCMBool()) return
			var num:Number
			if (sense) {
				if ( -(content.y - _mask.y)+value >= computeContentSize()) num = _mask.y - computeContentSize()
				else num = content.y - value
				if (tweenerBool) TweenMax.to(content, tweenerTime,{  y:num,
					onUpdate:function(mc):void { 
						mc.upSlider()
						mc.dispatchEvent(new Event(Event.SCROLL))
					}
					,onUpdateParams:[this]
				})
				else {
					content.y = num
					upSlider()
					dispatchEvent(new Event(Event.SCROLL))
				}
			}else {
				if (content.y + value >= _mask.y)num = _mask.y
				else num = content.y + value
				if (tweenerBool) TweenMax.to(content, tweenerTime,{ y:num,
					onUpdate:function(mc):void { 
						mc.upSlider()
						mc.dispatchEvent(new Event(Event.SCROLL))
					},onUpdateParams:[this]
				})
				else {
					content.y = num
					upSlider()
					dispatchEvent(new Event(Event.SCROLL))
				}
			}
		}
		/**
		 * 百分比计算对象的位置
		 */
		private function computeContentValue(value:Number):void {
			if (!computeCMBool())return
			if (content.height <= content.mask.height) {
				content.y = content.mask.y
				dispatchEvent(new Event(Event.SCROLL))
				return
			}
			if(value>1||value<0)return
			var __y:Number=-value*computeContentSize()+content.mask.y
			if (tweenerBool) TweenMax.to(content, tweenerTime,{  y:__y,
					onUpdate:function(mc):void { 
						mc.upSlider()
						mc.dispatchEvent(new Event(Event.SCROLL))
					},onUpdateParams:[this]
			})
			else {
				content.y = __y
				upSlider()
				dispatchEvent(new Event(Event.SCROLL))
				
			}
			
		}
		/**
		 * 根据滑块计算百分比
		 * @return
		 */
		private function computeNumFormSlider():Number {
			return	(_slider.y-_previousBtn.height)/pageSize
		}	
		/**
		 * 计算滑动位置
		 */
		public function upSlider():void {
			if (computeCMBool()) {
				this.visible=true
				_slider.visible = true
				_slider.y=_previousBtn.height+pageSize*computeNumFormContent()
			}
			else {
				_slider.y = _previousBtn.height
				if (hideBool) {
					if (hideType == HITAll) {
						_slider.visible = true
						this.visible=false
					}else {
						_slider.visible = false
						this.visible=true
					}
				}
				else {
					_slider.visible = true
					this.visible=true
				}
			}
		}
		/**
		 * 根据对象计算当前百分比
		 * @return
		 */
		public function computeNumFormContent():Number {
			computeCMBool()
			return (_mask.y-content.y)/computeContentSize()
		}
		/**
		 * 计算可以移动范围
		 * @return
		 */
		public function computeContentSize():Number {
			var _size:Number = 0
			if (computeCMBool()) {
				_size = content.height - content.mask.height
				 return _size
			}
			else return _size
		}
		/**
		 * 计算位置合理性
		 */
		private function  computeCMBool():Boolean {
			
			var bool:Boolean=false
			if (content != null && content.mask != null) {
				if (content.height > content.mask.height) bool = true
				if (coordinateBool&&content.x > content.mask.x) content.x = content.mask.x
				if (content.y > content.mask.y) content.y = content.mask.y
				if (bool && content.y < content.mask.y &&  content.mask.y-content.y  > content.height - content.mask.height) content.y=content.mask.y-(content.height-content.mask.height)
			}
			if (!bool) {
				_slider.y = _previousBtn.height
				if (content != null && content.mask!=null )content.y=content.mask.y
				//if (sliderAutoSize)_slider.height = _maxScrollPosition - _minScrollPosition 
				//else _slider.height = _sliderRect.height
				if (hideBool) {
					if (hideType == HITAll) {
						_slider.visible = true
						this.visible=false
					}else {
						_slider.visible = false
						this.visible=true
					}
				}
				else {
					_slider.visible = true
					this.visible=true
				}
			}
			else {
				
				//if (sliderAutoSize) {
					//var num:Number=(content.height - content.mask.height)/(_maxScrollPosition - _minScrollPosition)
					//if (num < 1) {
					//	num = (_maxScrollPosition - _minScrollPosition) * (1 - num)
					//	if(_sliderRect.height>num)num= _sliderRect.height
					//	_slider.height = num
					//}
					//else _slider.height = _sliderRect.height
				//}
				//else {
				//	_slider.height = _sliderRect.height
				//}
				//if (_slider.height > (_maxScrollPosition - _minScrollPosition) / 5) dragBool = false
				//else dragBool=true
			}
			return bool
		}
		/**
		 * 当前滚动条位置
		 */
		public function set scrollPosition(value:Number):void {
			if(value<0&&value>1)return
			computeContentValue(value)
		}
		public function get scrollPosition():Number {return computeNumFormSlider()}
		/**
		 * 下一滚动位置
		 */
		public function get nextScroll():Number { 
			if (!computeCMBool()) return _nextScroll
			var num:Number
			if ( -(content.y - _mask.y)+lineScrollSize >= computeContentSize()) num = _mask.y - computeContentSize()
			else num = content.y - lineScrollSize
			return num
		}
		/**
		 * 上一滚动位置
		 */
		public function get previousScroll():Number {
			if (!computeCMBool()) return _previousScroll
			var num:Number
			if (content.y + lineScrollSize >= _mask.y)num = _mask.y
			else num = content.y + lineScrollSize
			return num
		}
		/**
		 * 点击滚动
		 */
		public function set lineScrollSize(value:Number):void { 
			
			_lineScrollSize=value
		}
		public function get lineScrollSize():Number { return _lineScrollSize; }
		/**
		 * 滚动
		 */
		public function set wheelScrollSize(value:Number):void 
		{
			_wheelScrollSize=value
		}
		public function get wheelScrollSize():Number { return _wheelScrollSize; }
		
		/**
		 * 差值
		 */
		public function get pageSize():Number { return _maxScrollPosition - _minScrollPosition-_slider.height }
		/**
		 * 最小值
		 */
		public function get minScrollPosition():Number { return _minScrollPosition; }
		/**
		 * 最大值
		 */
		public function get maxScrollPosition():Number { return _maxScrollPosition; }
		/**
		 * 背景点选
		 */
		public function set allowTrackClick(value:Boolean):void {
			if (_allowTrackClick == value) return
			_allowTrackClick=value
		}
		public function get allowTrackClick():Boolean { return _allowTrackClick; }
		/**
		 * 隐藏模式
		 */
		public function get hideType():String { return _hideType; }
		
		public function set hideType(value:String):void 
		{
			if (_hideType == value) return 
			_hideType = value
			upSlider()
		}
		/**组件大小更新*/
		override public function upSize():void {
			if (_previousBtn) {
				if (height < _previousBtn.height + _nextBtn.height + _sliderRect.height) {
					setSize(_scrollBg.width, _previousBtn.height + _nextBtn.height + _sliderRect.height + 10)
					return
				}
				_maxScrollPosition = this.height - _nextBtn.height
				_minScrollPosition = this._previousBtn.height
				//_pageSize = _maxScrollPosition - _minScrollPosition-_slider.height
				_scrollBg.x=_scrollBg.y=0
				_previousBtn.x = _previousBtn.y = 0
				_previousBtn.x=(_scrollBg.width-_previousBtn.width)/2
				_slider.x = 0
				_slider.x=(_scrollBg.width-_slider.width)/2
				_slider.y = _previousBtn.height
				
				_scrollBg.height = this.height
				_nextBtn.x = 0
				_nextBtn.x=(_scrollBg.width-_nextBtn.width)/2
				_nextBtn.y = this.height - _nextBtn.height
				upSlider()
			}	
			
		}
		/**
		 * 破坏所有索引，垃圾回收
		 */
		override public function destory():void {
			super.destory()
			if (_scrollBg)_scrollBg.removeEventListener(MouseEvent.MOUSE_DOWN, scrollDown)
			if (_slider) _slider.removeEventListener(MouseEvent.MOUSE_DOWN, sliderDown) 
			if (_nextBtn) {
				_nextBtn.removeEventListener(MouseEvent.MOUSE_DOWN, btnDown) 
				//_nextBtn.removeEventListener(MouseEvent.MOUSE_UP, btnUp)
			}
			if (_previousBtn) {
				_previousBtn.removeEventListener(MouseEvent.MOUSE_DOWN, btnDown)
				//_previousBtn.removeEventListener(MouseEvent.MOUSE_UP, btnUp)
			}
			stage.removeEventListener(MouseEvent.MOUSE_UP,stageUp)
			removeEventListener(Event.ENTER_FRAME, ENTER_FRAME)
			stage.removeEventListener(MouseEvent.MOUSE_UP, sliderUp)
			stage.removeEventListener(MouseEvent.MOUSE_MOVE, sliderMove)
			if (_content!=null&&_content is InteractiveObject)InteractiveObject(_content).removeEventListener(MouseEvent.MOUSE_WHEEL, MOUSE_WHEEL)
			_content=null
			_mask=null
		}
		
		
	}

}