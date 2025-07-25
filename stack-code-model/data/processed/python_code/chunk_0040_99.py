package fairygui
{
	import fairygui.tween.GTween;
	import fairygui.tween.GTweener;
	
	public class GearLook extends GearBase
	{
		private var _storage:Object;
		private var _default:GearLookValue;
		private var _tweener:GTweener;
		
		public function GearLook(owner:GObject)
		{
			super(owner);
		}
		
		override protected function init():void
		{
			_default = new GearLookValue(_owner.alpha, _owner.rotation, _owner.grayed,_owner.touchable);
			_storage = {};
		}
		
		override protected function addStatus(pageId:String, value:String):void
		{
			if(value=="-" || value.length==0)
				return;
			
			var arr:Array = value.split(",");
			var gv:GearLookValue;
			if(pageId==null)
				gv = _default;
			else
			{
				gv = new GearLookValue();
				_storage[pageId] = gv;
			}
			gv.alpha = parseFloat(arr[0]);
			gv.rotation = parseInt(arr[1]);
			gv.grayed = arr[2]=="1"?true:false;
			if(arr.length<4)
				gv.touchable = _owner.touchable;
			else
				gv.touchable = arr[3]=="1"?true:false;
		}
		
		override public function apply():void
		{
			var gv:GearLookValue = _storage[_controller.selectedPageId];
			if(!gv)
				gv = _default;
			
			if(_tween && !UIPackage._constructing && !disableAllTweenEffect)
			{
				_owner._gearLocked = true;
				_owner.grayed = gv.grayed;
				_owner.touchable = gv.touchable;
				_owner._gearLocked = false;
				
				if (_tweener != null)
				{
					if (_tweener.endValue.x != gv.alpha || _tweener.endValue.y != gv.rotation)
					{
						_tweener.kill(true);
						_tweener = null;
					}
					else
						return;
				}
				
				var a:Boolean = gv.alpha!=_owner.alpha;
				var b:Boolean = gv.rotation!=_owner.rotation;
				if(a || b)
				{
					if(_owner.checkGearController(0, _controller))
						_displayLockToken = _owner.addDisplayLock();
					
					_tweener = GTween.to2(_owner.alpha, _owner.rotation, gv.alpha, gv.rotation, _tweenTime)
						.setDelay(_delay)
						.setEase(_easeType)
						.setUserData((a ? 1 : 0) + (b ? 2 : 0))
						.setTarget(this)
						.onUpdate(__tweenUpdate)
						.onComplete(__tweenComplete);
				}
			}
			else
			{
				_owner._gearLocked = true;
				_owner.alpha = gv.alpha;
				_owner.rotation = gv.rotation;
				_owner.grayed = gv.grayed;
				_owner.touchable = gv.touchable;
				_owner._gearLocked = false;
			}
		}
		
		private function __tweenUpdate(tweener:GTweener):void
		{
			var flag:int = int(tweener.userData);
			_owner._gearLocked = true;
			if ((flag & 1) != 0)
				_owner.alpha = tweener.value.x;
			if ((flag & 2) != 0)
				_owner.rotation = tweener.value.y;
			_owner._gearLocked = false;		
		}
		
		private function __tweenComplete():void
		{
			if(_displayLockToken!=0)
			{
				_owner.releaseDisplayLock(_displayLockToken);
				_displayLockToken = 0;
			}
			_tweener = null;
		}
		
		override public function updateState():void
		{
			var gv:GearLookValue = _storage[_controller.selectedPageId];
			if(!gv)
			{
				gv = new GearLookValue();
				_storage[_controller.selectedPageId] = gv;
			}
			
			gv.alpha = _owner.alpha;
			gv.rotation = _owner.rotation;
			gv.grayed = _owner.grayed;
			gv.touchable = _owner.touchable;
		}
	}
}

class GearLookValue
{
	public var alpha:Number;
	public var rotation:Number;
	public var grayed:Boolean;
	public var touchable:Boolean;
	
	public function GearLookValue(alpha:Number=0, rotation:Number=0, 
								  grayed:Boolean=false, touchable:Boolean=true)
	{
		this.alpha = alpha;
		this.rotation = rotation;
		this.grayed = grayed;
		this.touchable = touchable;
	}
}