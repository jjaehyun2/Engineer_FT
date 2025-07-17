package qin.freeViewer{
	public class FormatManager {
		//典型齿轮同学于2010年10月7日基本完成此类~9日修正字体名属性注释及相关方法。
		//FormatManager类用于排版，但它不回直接操作可视对象，而只是提供数据。
		//其基本使用流程如下：
		//调用initialize方法初始化，然后给版式相关属性赋值，调用lockFormat方法确定。
		//一次次调用readOne方法进行预排版（同时输出相关数值结果），全部完毕之后调用inputFinished方法。
		//通过setPage方法设定页码，然后进行单页排版。
		private var _eleIndex_num:Number = 0;
		//以上属性用于保存当前xml文档中的减字所属元素索引（从0开始）。一个元素可对应一或多个字。
		private var _jzIndex_num:Number = 0;
		//以上属性用于保存当前元素中的减字索引（从0开始）。当前字是它所属元素中的第几号字。
		private var _jzSurplus_num:Number = 0;
		//以上属性用于保存本页起始元素中还有几个字不属于本页。
		//这个属性在每一次setPage之后的初始值等于_myData_array中相应页面对象的stJzIndex_num值。
		//排一个不属于本页的字，本属性数值减1，减到0就说明下一个字是本页第一字。
		private var _jzWidth_num:Number = 0;
		private var _jzHeight_num:Number = 0;
		private var _jzX_num:Number = 0;
		private var _jzY_num:Number = 0;
		//以上属性用于保存当前减字的宽高和坐标（注册点为左上角）
		private var _sideDistanceX_num:Number = 35;
		private var _sideDistanceY_num:Number = 35;
		//以上属性用于保存页边距。
		private var _pageWidth_num:Number;
		private var _pageHeight_num:Number;
		//以上属性用于保存实用页面区域的宽和高。
		private var _innerDistance_num:Number = 20;
		//以上属性用于保存行/列间距。
		private var _pg1BlankHeight_num:Number = 100;
		private var _jzScale_num:Number = 1;
		private var _characterSpacing1_num:Number = 1;
		private var _characterSpacing2_num:Number = 3;
		private var _characterSpacing3_num:Number = 5;
		//以上属性用于保存三个级别的字间距。
		private var _titleAreaX_num:Number;
		private var _titleAreaY_num:Number;
		private var _titleAreaWidth_num:Number;
		private var _titleAreaHeight_num:Number;
		//以上属性用于保存第一页标题区域的X、Y、宽、高。
		private var _infoAreaX_num:Number;
		private var _infoAreaY_num:Number;
		private var _infoAreaWidth_num:Number;
		private var _infoAreaHeight_num:Number;
		//以上属性用于保存第一页曲谱信息区域的X、Y、宽、高。
		private var _pitchAreaX_num:Number;
		private var _pitchAreaY_num:Number;
		private var _pitchAreaWidth_num:Number;
		private var _pitchAreaHeight_num:Number;
		//以上属性用于保存第一页调信息区域的X、Y、宽、高。
		private var _pgNumAreaX_num:Number;
		private var _pgNumAreaY_num:Number;
		private var _pgNumAreaWidth_num:Number;
		private var _pgNumAreaHeight_num:Number;
		//以上属性用于保存每页页码区域的X、Y、宽、高。
		private var _preX_num:Number;
		private var _preY_num:Number;
		//以上属性用于保存上页多余减字信息区域的X、Y。
		private var _tailX_num:Number;
		private var _tailY_num:Number;
		//以上属性用于保存下页多余减字信息区域的X、Y。
		//
		private var _format_num:Number = 0;
		//以上属性，横排字为0，竖排字为1。
		private var _currentPage_num:Number = 0;
		//以上属性用于保存当前页面号码，初始为0。
		private var _finishedCurrentPage_bool:Boolean;
		//以上属性用于确定当前页面是否排满了字。
		private var _formatConfirmed_bool:Boolean;
		//以上属性，只有为false时才可以更改版式设定。
		private var _readyForOutput_bool:Boolean;
		//以上属性，预排版完毕后设为真。
		//
		private var _myData_array:Array = [{stEleIndex_num:0,stJzIndex_num:0,eleAmount:0}];
		//以上数组，保存内部含有页面数据的对象，事先定义索引为0的一项（无实际用处）。在运行期会加入和页码对应的对象。
		private var _rulerX_num:Number;
		private var _rulerY_num:Number;
		//以上属性是标尺。
		private var _lastPage_num:Number = 0;
		//以上属性用于保存最末页码。由此数可知共有几页。
		private var _flexObjMode_bool:Boolean = false;
		//以上属性用标记是否是宽松模式，即是否允许不应该修改某属性的时候对于此属性的修改。和Adobe Flex没关系！
		private var _fontName_str:String = "qin.jzFonts.droidSansFallback.JzFont_DroidSansFallback_";
		//减字字体名。
		public var pgNumPosition_uint:uint = 9;
		public var pgNumLeftMargin_num:Number = 15;
		public var pgNumTopMargin_num:Number = 15;
		public var pgNumRightMargin_num:Number = 15;
		public var pgNumBottomMargin_num:Number = 15;
		public var pgNumPosAutoChange_bool:Boolean = true;
		//前五个属性指明了页码栏在页面中的位置（参考数字小键盘）和页码栏与页边的水平、垂直距离。
		//第六个属性指明了是否需要自动进行页码栏的左右交替更换。比如，第一页页码栏在左上角，第二页页码栏就在右上角，以此类推。
		//FormatManager类的构造函数！
		public function FormatManager() {
			this.initialize();
		}
		//
		//[这里要写设定、读取属性值的方法。]
		//首先是任何时候都可以从外部设定值的属性。
		//_EleIndex_num
		public function setEleIndex_num(myData:Number):void {
			this._eleIndex_num = myData;
		}
		public function getEleIndex_num():Number {
			return this._eleIndex_num;
		}
		public function set eleIndex_num(myData:Number):void {
			this.setEleIndex_num(myData);
		}
		public function get eleIndex_num():Number {
			return this.getEleIndex_num();
		}
		//_jzIndex_num
		public function setJzIndex_num(myData:Number):void {
			this._jzIndex_num = myData;
		}
		public function getJzIndex_num():Number {
			return this._jzIndex_num;
		}
		public function set jzIndex_num(myData:Number):void {
			this.setJzIndex_num(myData);
		}
		public function get jzIndex_num():Number {
			return this.getJzIndex_num();
		}
		//_flexObjMode_bool
		public function setFlexObjMode_bool(myData:Boolean):void {
			this._flexObjMode_bool = myData;
		}
		public function getFlexObjMode_bool():Boolean {
			return this._flexObjMode_bool;
		}
		public function set flexObjMode_bool(myData:Boolean):void {
			this.setFlexObjMode_bool(myData);
		}
		public function get flexObjMode_bool():Boolean {
			return this.getFlexObjMode_bool();
		}
		//lockFormat后不应该从外部改写的：
		//_fontName_str
		public function setFontName_str(myData:String):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._fontName_str = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_fontName_str的值！");
				return false;
			}
		}
		public function getFontName_str():String {
			return this._fontName_str;
		}
		public function set fontName_str(myData:String):void {
			this.setFontName_str(myData);
		}
		public function get fontName_str():String {
			return this.getFontName_str();
		}
		//_pageWidth_num
		public function setPageWidth_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._pageWidth_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_pageWidth_num的值！");
				return false;
			}
		}
		public function getPageWidth_num():Number {
			return this._pageWidth_num;
		}
		public function set pageWidth_num(myData:Number):void {
			this.setPageWidth_num(myData);
		}
		public function get pageWidth_num():Number {
			return this.getPageWidth_num();
		}
		//_pageHeight_num
		public function setPageHeight_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._pageHeight_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_pageHeight_num的值！");
				return false;
			}
		}
		public function getPageHeight_num():Number {
			return this._pageHeight_num;
		}
		public function set pageHeight_num(myData:Number):void {
			this.setPageHeight_num(myData);
		}
		public function get pageHeight_num():Number {
			return this.getPageHeight_num();
		}
		//_infoAreaX_num
		//_sideDistanceX_num
		public function setSideDistanceX_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._sideDistanceX_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_sideDistanceX_num的值！");
				return false;
			}
		}
		public function getSideDistanceX_num():Number {
			return this._sideDistanceX_num;
		}
		public function set sideDistanceX_num(myData:Number):void {
			this.setSideDistanceX_num(myData);
		}
		public function get sideDistanceX_num():Number {
			return this.getSideDistanceX_num();
		}
		//_sideDistanceY_num
		public function setSideDistanceY_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._sideDistanceY_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_sideDistanceY_num的值！");
				return false;
			}
		}
		public function getSideDistanceY_num():Number {
			return this._sideDistanceY_num;
		}
		public function set sideDistanceY_num(myData:Number):void {
			this.setSideDistanceY_num(myData);
		}
		public function get sideDistanceY_num():Number {
			return this.getSideDistanceY_num();
		}
		//_innerDistance_num
		public function setInnerDistance_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._innerDistance_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_innerDistance_num的值！");
				return false;
			}
		}
		public function getInnerDistance_num():Number {
			return this._innerDistance_num;
		}
		public function set innerDistance(myData:Number):void {
			this.setInnerDistance_num(myData);
		}
		public function get innerDistance():Number {
			return this.getInnerDistance_num();
		}
		//_pg1BlankHeight_num
		public function setPg1BlankHeight_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._pg1BlankHeight_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_pg1BlankHeight_num的值！");
				return false;
			}
		}
		public function getPg1BlankHeight_num():Number {
			return this._pg1BlankHeight_num;
		}
		public function set pg1BlankHeight(myData:Number):void {
			this.setPg1BlankHeight_num(myData);
		}
		public function get pg1BlankHeight():Number {
			return this.getPg1BlankHeight_num();
		}
		//_jzScale_num
		public function setJzScale_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._jzScale_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_jzScale_num的值！");
				return false;
			}
		}
		public function getJzScale_num():Number {
			return this._jzScale_num;
		}
		public function set jzScale_num(myData:Number):void {
			this.setJzScale_num(myData);
		}
		public function get jzScale_num():Number {
			return this.getJzScale_num();
		}
		//_characterSpacing1_num
		public function setCharacterSpacing1_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._characterSpacing1_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_characterSpacing1_num的值！");
				return false;
			}
		}
		public function getCharacterSpacing1_num():Number {
			return this._characterSpacing1_num;
		}
		public function set characterSpacing1_num(myData:Number):void {
			this.setCharacterSpacing1_num(myData);
		}
		public function get characterSpacing1_num():Number {
			return this.getCharacterSpacing1_num();
		}
		//_characterSpacing2_num
		public function setCharacterSpacing2_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._characterSpacing2_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_characterSpacing2_num的值！");
				return false;
			}
		}
		public function getCharacterSpacing2_num():Number {
			return this._characterSpacing2_num;
		}
		public function set characterSpacing2_num(myData:Number):void {
			this.setCharacterSpacing2_num(myData);
		}
		public function get characterSpacing2_num():Number {
			return this.getCharacterSpacing2_num();
		}
		//_characterSpacing3_num
		public function setCharacterSpacing3_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._characterSpacing3_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_characterSpacing3_num的值！");
				return false;
			}
		}
		public function getCharacterSpacing3_num():Number {
			return this._characterSpacing3_num;
		}
		public function set characterSpacing3_num(myData:Number):void {
			this.setCharacterSpacing3_num(myData);
		}
		public function get characterSpacing3_num():Number {
			return this.getCharacterSpacing3_num();
		}
		//_titleAreaX_num
		public function setTitleAreaX_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._titleAreaX_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_titleAreaX_num的值！");
				return false;
			}
		}
		public function getTitleAreaX_num():Number {
			return this._titleAreaX_num;
		}
		public function set titleAreaX_num(myData:Number):void {
			this.setTitleAreaX_num(myData);
		}
		public function get titleAreaX_num():Number {
			return this.getTitleAreaX_num();
		}
		//_titleAreaY_num
		public function setTitleAreaY_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._titleAreaY_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_titleAreaY_num的值！");
				return false;
			}
		}
		public function getTitleAreaY_num():Number {
			return this._titleAreaY_num;
		}
		public function set titleAreaY_num(myData:Number):void {
			this.setTitleAreaY_num(myData);
		}
		public function get titleAreaY_num():Number {
			return this.getTitleAreaY_num();
		}
		//_titleAreaWidth_num
		public function setTitleAreaWidth_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._titleAreaWidth_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_titleAreaWidth_num的值！");
				return false;
			}
		}
		public function getTitleAreaWidth_num():Number {
			return this._titleAreaWidth_num;
		}
		public function set titleAreaWidth_num(myData:Number):void {
			this.setTitleAreaWidth_num(myData);
		}
		public function get titleAreaWidth_num():Number {
			return this.getTitleAreaWidth_num();
		}
		//_titleAreaHeight_num
		public function setTitleAreaHeight_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._titleAreaHeight_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_titleAreaHeight_num的值！");
				return false;
			}
		}
		public function getTitleAreaHeight_num():Number {
			return this._titleAreaHeight_num;
		}
		public function set titleAreaHeight_num(myData:Number):void {
			this.setTitleAreaHeight_num(myData);
		}
		public function get titleAreaHeight_num():Number {
			return this.getTitleAreaHeight_num();
		}
		//_infoAreaX_num
		public function setInfoAreaX_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._infoAreaX_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_infoAreaX_num的值！");
				return false;
			}
		}
		public function getInfoAreaX_num():Number {
			return this._infoAreaX_num;
		}
		public function set infoAreaX_num(myData:Number):void {
			this.setInfoAreaX_num(myData);
		}
		public function get infoAreaX_num():Number {
			return this.getInfoAreaX_num();
		}
		//_infoAreaY_num
		public function setInfoAreaY_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._infoAreaY_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_infoAreaY_num的值！");
				return false;
			}
		}
		public function getInfoAreaY_num():Number {
			return this._infoAreaY_num;
		}
		public function set infoAreaY_num(myData:Number):void {
			this.setInfoAreaY_num(myData);
		}
		public function get infoAreaY_num():Number {
			return this.getInfoAreaY_num();
		}
		//_infoAreaWidth_num
		public function setInfoAreaWidth_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._infoAreaWidth_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_infoAreaWidth_num的值！");
				return false;
			}
		}
		public function getInfoAreaWidth_num():Number {
			return this._infoAreaWidth_num;
		}
		public function set infoAreaWidth_num(myData:Number):void {
			this.setInfoAreaWidth_num(myData);
		}
		public function get infoAreaWidth_num():Number {
			return this.getInfoAreaWidth_num();
		}
		//_infoAreaHeight_num
		public function setInfoAreaHeight_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._infoAreaHeight_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_infoAreaHeight_num的值！");
				return false;
			}
		}
		public function getInfoAreaHeight_num():Number {
			return this._infoAreaHeight_num;
		}
		public function set infoAreaHeight_num(myData:Number):void {
			this.setInfoAreaHeight_num(myData);
		}
		public function get infoAreaHeight_num():Number {
			return this.getInfoAreaHeight_num();
		}
		//_pitchAreaX_num
		public function setPitchAreaX_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._pitchAreaX_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_pitchAreaX_num的值！");
				return false;
			}
		}
		public function getPitchAreaX_num():Number {
			return this._pitchAreaX_num;
		}
		public function set pitchAreaX_num(myData:Number):void {
			this.setPitchAreaX_num(myData);
		}
		public function get pitchAreaX_num():Number {
			return this.getPitchAreaX_num();
		}
		//_pitchAreaY_num
		public function setPitchAreaY_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._pitchAreaY_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_pitchAreaY_num的值！");
				return false;
			}
		}
		public function getPitchAreaY_num():Number {
			return this._pitchAreaY_num;
		}
		public function set pitchAreaY_num(myData:Number):void {
			this.setPitchAreaY_num(myData);
		}
		public function get pitchAreaY_num():Number {
			return this.getPitchAreaY_num();
		}
		//_pitchAreaWidth_num
		public function setPitchAreaWidth_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._pitchAreaWidth_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_pitchAreaWidth_num的值！");
				return false;
			}
		}
		public function getPitchAreaWidth_num():Number {
			return this._pitchAreaWidth_num;
		}
		public function set pitchAreaWidth_num(myData:Number):void {
			this.setPitchAreaWidth_num(myData);
		}
		public function get pitchAreaWidth_num():Number {
			return this.getPitchAreaWidth_num();
		}
		//_pitchAreaHeight_num
		public function setPitchAreaHeight_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._pitchAreaHeight_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_pitchAreaHeight_num的值！");
				return false;
			}
		}
		public function getPitchAreaHeight_num():Number {
			return this._pitchAreaHeight_num;
		}
		public function set pitchAreaHeight_num(myData:Number):void {
			this.setPitchAreaHeight_num(myData);
		}
		public function get pitchAreaHeight_num():Number {
			return this.getPitchAreaHeight_num();
		}
		//_pgNumAreaX_num
		public function setPgNumAreaX_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._pgNumAreaX_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_pgNumAreaX_num的值！");
				return false;
			}
		}
		public function getPgNumAreaX_num():Number {
			return this._pgNumAreaX_num;
		}
		public function set pgNumAreaX_num(myData:Number):void {
			this.setPgNumAreaX_num(myData);
		}
		public function get pgNumAreaX_num():Number {
			return this.getPgNumAreaX_num();
		}
		//_pgNumAreaY_num
		public function setPgNumAreaY_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._pgNumAreaY_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_pgNumAreaY_num的值！");
				return false;
			}
		}
		public function getPgNumAreaY_num():Number {
			return this._pgNumAreaY_num;
		}
		public function set pgNumAreaY_num(myData:Number):void {
			this.setPgNumAreaY_num(myData);
		}
		public function get pgNumAreaY_num():Number {
			return this.getPgNumAreaY_num();
		}
		//_pgNumAreaWidth_num
		public function setPgNumAreaWidth_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._pgNumAreaWidth_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_pgNumAreaWidth_num的值！");
				return false;
			}
		}
		public function getPgNumAreaWidth_num():Number {
			return this._pgNumAreaWidth_num;
		}
		public function set pgNumAreaWidth_num(myData:Number):void {
			this.setPgNumAreaWidth_num(myData);
		}
		public function get pgNumAreaWidth_num():Number {
			return this.getPgNumAreaWidth_num();
		}
		//_pgNumAreaHeight_num
		public function setPgNumAreaHeight_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._pgNumAreaHeight_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_pgNumAreaHeight_num的值！");
				return false;
			}
		}
		public function getPgNumAreaHeight_num():Number {
			return this._pgNumAreaHeight_num;
		}
		public function set pgNumAreaHeight_num(myData:Number):void {
			this.setPgNumAreaHeight_num(myData);
		}
		public function get pgNumAreaHeight_num():Number {
			return this.getPgNumAreaHeight_num();
		}
		//_preX_num
		public function setPreX_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._preX_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_preX_num的值！");
				return false;
			}
		}
		public function getPreX_num():Number {
			return this._preX_num;
		}
		public function set preX_num(myData:Number):void {
			this.setPreX_num(myData);
		}
		public function get preX_num():Number {
			return this.getPreX_num();
		}
		//_preY_num
		public function setPreY_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._preY_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_preY_num的值！");
				return false;
			}
		}
		public function getPreY_num():Number {
			return this._preY_num;
		}
		public function set preY_num(myData:Number):void {
			this.setPreY_num(myData);
		}
		public function get preY_num():Number {
			return this.getPreY_num();
		}
		//_tailX_num
		public function setTailX_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._tailX_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_tailX_num的值！");
				return false;
			}
		}
		public function getTailX_num():Number {
			return this._tailX_num;
		}
		public function set tailX_num(myData:Number):void {
			this.setTailX_num(myData);
		}
		public function get tailX_num():Number {
			return this.getTailX_num();
		}
		//_tailY_num
		public function setTailY_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._tailY_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_tailY_num的值！");
				return false;
			}
		}
		public function getTailY_num():Number {
			return this._tailY_num;
		}
		public function set tailY_num(myData:Number):void {
			this.setTailY_num(myData);
		}
		public function get tailY_num():Number {
			return this.getTailY_num();
		}
		//_format_num
		public function setFormat_num(myData:Number):Boolean {
			if (!(this._formatConfirmed_bool) || this._flexObjMode_bool) {
				this._format_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_format_num的值！");
				return false;
			}
		}
		public function getFormat_num():Number {
			return this._format_num;
		}
		public function set format_num(myData:Number):void {
			this.setFormat_num(myData);
		}
		public function get format_num():Number {
			return this.getFormat_num();
		}
		//lockFormat后才应该从外部改写的：
		//_jzWidth_num
		public function setJzWidth_num(myData:Number):Boolean {
			if (this._formatConfirmed_bool || this._flexObjMode_bool) {
				this._jzWidth_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_jzWidth_num的值！");
				return false;
			}
		}
		public function getJzWidth_num():Number {
			return this._jzWidth_num;
		}
		public function set jzWidth_num(myData:Number):void {
			this.setJzWidth_num(myData);
		}
		public function get jzWidth_num():Number {
			return this.getJzWidth_num();
		}
		//_jzHeight_num
		public function setJzHeight_num(myData:Number):Boolean {
			if (this._formatConfirmed_bool || this._flexObjMode_bool) {
				this._jzHeight_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_jzHeight_num的值！");
				return false;
			}
		}
		public function getJzHeight_num():Number {
			return this._jzHeight_num;
		}
		public function set jzHeight_num(myData:Number):void {
			this.setJzHeight_num(myData);
		}
		public function get jzHeight_num():Number {
			return this.getJzHeight_num();
		}
		//_jzX_num
		public function setJzX_num(myData:Number):Boolean {
			if (this._formatConfirmed_bool || this._flexObjMode_bool) {
				this._jzX_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_jzX_num的值！");
				return false;
			}
		}
		public function getJzX_num():Number {
			return this._jzX_num;
		}
		public function set jzX_num(myData:Number):void {
			this.setJzX_num(myData);
		}
		public function get jzX_num():Number {
			return this.getJzX_num();
		}
		//_jzY_num
		public function setJzY_num(myData:Number):Boolean {
			if (this._formatConfirmed_bool || this._flexObjMode_bool) {
				this._jzY_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_jzY_num的值！");
				return false;
			}
		}
		public function getJzY_num():Number {
			return this._jzY_num;
		}
		public function set jzY_num(myData:Number):void {
			this.setJzY_num(myData);
		}
		public function get jzY_num():Number {
			return this.getJzY_num();
		}
		//任何时候都不该从外部改写的：
		//_jzSurplus_num
		public function setJzSurplus_num(myData:Number):Boolean {
			if (this._flexObjMode_bool) {
				this._jzSurplus_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_jzSurplus_num的值！");
				return false;
			}
		}
		public function getJzSurplus_num():Number {
			return this._jzSurplus_num;
		}
		public function set jzSurplus_num(myData:Number):void {
			this.setJzSurplus_num(myData);
		}
		public function get jzSurplus_num():Number {
			return this.getJzSurplus_num();
		}
		//_currentPage_num
		public function setCurrentPage_num(myData:Number):Boolean {
			if (this._flexObjMode_bool) {
				this._currentPage_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_currentPage_num的值！");
				return false;
			}
		}
		public function getCurrentPage_num():Number {
			return this._currentPage_num;
		}
		public function set currentPage_num(myData:Number):void {
			this.setCurrentPage_num(myData);
		}
		public function get currentPage_num():Number {
			return this.getCurrentPage_num();
		}
		//_finishedCurrentPage_bool
		public function setFinishedCurrentPage_bool(myData:Boolean):Boolean {
			if (this._flexObjMode_bool) {
				this._finishedCurrentPage_bool = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_finishedCurrentPage_bool的值！");
				return false;
			}
		}
		public function getFinishedCurrentPage_bool():Boolean {
			return this._finishedCurrentPage_bool;
		}
		public function set finishedCurrentPage_bool(myData:Boolean):void {
			this.setFinishedCurrentPage_bool(myData);
		}
		public function get finishedCurrentPage_bool():Boolean {
			return this.getFinishedCurrentPage_bool();
		}
		//_formatConfirmed_bool
		public function setFormatConfirmed_bool(myData:Boolean):Boolean {
			if (this._flexObjMode_bool) {
				this._formatConfirmed_bool = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_formatConfirmed_bool的值！");
				return false;
			}
		}
		public function getFormatConfirmed_bool():Boolean {
			return this._formatConfirmed_bool;
		}
		public function set formatConfirmed_bool(myData:Boolean):void {
			this.setFormatConfirmed_bool(myData);
		}
		public function get formatConfirmed_bool():Boolean {
			return this.getFormatConfirmed_bool();
		}
		//_readyForOutput_bool
		public function setReadyForOutput_bool(myData:Boolean):Boolean {
			if (this._flexObjMode_bool) {
				this._readyForOutput_bool = myData;
				return true;
			} else {
				trace("现在_readyForOutput_bool的值为"+this._readyForOutput_bool+"，其为True时不应该改变_readyForOutput_bool的值！");
				return false;
			}
		}
		public function getReadyForOutput_bool():Boolean {
			return this._readyForOutput_bool;
		}
		public function set readyForOutput_bool(myData:Boolean):void {
			this.setReadyForOutput_bool(myData);
		}
		public function get readyForOutput_bool():Boolean {
			return this.getReadyForOutput_bool();
		}
		//_myData_array
		public function setMyData_array(myData:Array):Boolean {
			if (this._flexObjMode_bool) {
				this._myData_array = myData;
				return true;
			} else {
				trace("现在_myData_array的值为"+this._myData_array+"，其为True时不应该改变_myData_array的值！");
				return false;
			}
		}
		public function getMyData_array():Array {
			return this._myData_array;
		}
		public function set myData_array(myData:Array):void {
			this.setMyData_array(myData);
		}
		public function get myData_array():Array {
			return this.getMyData_array();
		}
		//_rulerX_num
		public function setRulerX_num(myData:Number):Boolean {
			if (this._flexObjMode_bool) {
				this._rulerX_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_rulerX_num的值！");
				return false;
			}
		}
		public function getRulerX_num():Number {
			return this._rulerX_num;
		}
		public function set rulerX_num(myData:Number):void {
			this.setRulerX_num(myData);
		}
		public function get rulerX_num():Number {
			return this.getRulerX_num();
		}
		//_rulerY_num
		public function setRulerY_num(myData:Number):Boolean {
			if (this._flexObjMode_bool) {
				this._rulerY_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_rulerY_num的值！");
				return false;
			}
		}
		public function getRulerY_num():Number {
			return this._rulerY_num;
		}
		public function set rulerY_num(myData:Number):void {
			this.setRulerY_num(myData);
		}
		public function get rulerY_num():Number {
			return this.getRulerY_num();
		}
		//_lastPage_num
		public function setLastPage_num(myData:Number):Boolean {
			if (this._flexObjMode_bool) {
				this._lastPage_num = myData;
				return true;
			} else {
				trace("现在_formatConfirmed_bool的值为"+this._formatConfirmed_bool+"，其为True时不应该改变_lastPage_num的值！");
				return false;
			}
		}
		public function getLastPage_num():Number {
			return this._lastPage_num;
		}
		public function set lastPage_num(myData:Number):void {
			this.setLastPage_num(myData);
		}
		public function get lastPage_num():Number {
			return this.getLastPage_num();
		}
		//
		//
		//以下方法用于锁定格式设置，预排版前调用。
		public function lockFormat():void {
			//如果格式还没锁，就锁。
			var myRulerY_num:Number = 0;
			//用于标题信息排位的临时小标尺。
			if (!(this._formatConfirmed_bool)) {
				this._formatConfirmed_bool = true;
				//行/列间距按要求缩放。
				this._innerDistance_num *= this._jzScale_num;
				//把标尺移动到右下角，这是因为刚开始排版时候，需要有一个从空白的0页切换到1页的过程，其原理是让0页一开始就是处于满的状态，自然第一个字就跑到1页去了。
				//注意_jzScale_num是百分数，所以要除以100！
				this._rulerX_num=this._pageWidth_num;
				this._rulerY_num=this._pageHeight_num;
				//标题等信息的排位。
				this._titleAreaX_num = Math.round((this._pageWidth_num-this._titleAreaX_num)*0.5);
				myRulerY_num+=this._titleAreaHeight_num;
				this._infoAreaX_num=this._pageWidth_num-this._infoAreaWidth_num;
				this._infoAreaY_num=myRulerY_num;
				myRulerY_num+=this._infoAreaHeight_num;
				this._pitchAreaX_num=0;
				this._pitchAreaY_num=myRulerY_num;
				myRulerY_num+=this._pitchAreaHeight_num;
			}
		}
		//在预排版完毕后，调用以下方法。
		public function inputFinished():void {
			if (!(this._readyForOutput_bool)) {
				this._readyForOutput_bool=true;
				this._lastPage_num=this._currentPage_num;
			}
		}
		//以下方法用于硬换页。
		public function newPage():void {
			switch (this._format_num) {
				case 0 :
					//若为横排。
					this._myData_array[this._currentPage_num].eleAmount = (this._eleIndex_num-this._myData_array[this._currentPage_num].stEleIndex_num);
					//上一页有多少元素，现在就可以确定了！
					this._myData_array.push({stEleIndex_num:this._eleIndex_num, stJzIndex_num:this._jzIndex_num, eleAmount:0});
					//页码更新。
					this._currentPage_num+=1;
					//设定标尺。
					this._rulerX_num=0;
					this._rulerY_num=this._innerDistance_num;
					//如果新的页面是第一页，那么要留出标题等信息的空间。
					if (this._currentPage_num==1) {
						this._rulerY_num+=_pg1BlankHeight_num;
					}
					break;
				case 1 :
					//[还没完成] [竖排版代码] 
					break;
			}
		}
		//以下方法用于硬换行。
		public function newLine():void {
			switch (this._format_num) {
					//若为横排。
				case 0 :
					//如果本页还能容纳下新一行，就直接换行，否则换页。
					if ((this._rulerY_num+this._innerDistance_num)<=this._pageHeight_num) {
						this._rulerX_num=0;
						this._rulerY_num+=this._innerDistance_num;
					} else {
						//换页。
						this.newPage();
					}
					break;
				case 1 :
					//[还没完成] [竖排版代码] 
					break;
			}
		}
		public function readOne():void {
			//先锁定格式设置
			this.lockFormat();
			//开始：
			switch (this._format_num) {
					//若为横排。
				case 0 :
					//如果本行能再容纳当前字，直接排上，否则就要换行（甚至换页）。
					if ((this._rulerX_num+this._jzWidth_num)<=(this._pageWidth_num)) {
						//把标尺坐标值赋予给减字指示的属性。   
						this._jzX_num=this._rulerX_num;
						this._jzY_num=this._rulerY_num-this._jzHeight_num;
						//接着，标尺移动至下一个位置。
						this._rulerX_num=this._rulerX_num+this._jzWidth_num;
					} else {
						//下面，换行（甚至换页）。
						//这时候，如果本页至少还能再容纳一行字，就换行。
						if ((this._rulerY_num+this._innerDistance_num)<=this._pageHeight_num) {
							this._rulerX_num=0;
							this._rulerY_num+=this._innerDistance_num;
							//把标尺坐标值赋予给减字指示的属性。
							this._jzX_num=this._rulerX_num;
							this._jzY_num=this._rulerY_num-this._jzHeight_num;
							//接着，标尺移动至下一个位置。
							this._rulerX_num=this._rulerX_num+this._jzWidth_num;
						} else {
							//反之，如果本页不能再容纳下一行字，就换页。
							//先把刚排完一页的元素总数设值。
							//如果当前字是它所属元素的0号字（第一个字），那么这一页的元素数量就是当前元素索引值减去开始元素索引值的结果。
							if (this._jzIndex_num==0) {
								this._myData_array[this._currentPage_num].eleAmount = (this._eleIndex_num-this._myData_array[this._currentPage_num].stEleIndex_num);
							} else {
								//否则，要加1才是。
								this._myData_array[this._currentPage_num].eleAmount = (this._eleIndex_num+1-this._myData_array[this._currentPage_num].stEleIndex_num);
							}
							this._myData_array.push({stEleIndex_num:this._eleIndex_num, stJzIndex_num:this._jzIndex_num, eleAmount:0});
							//接下来，页码更新。
							this._currentPage_num+=1;
							//设定标尺。
							this._rulerX_num=0;
							this._rulerY_num=this._innerDistance_num;
							trace("fm的innerDistance"+this._innerDistance_num);
							//如果新的页面是第一页，那么要留出标题等信息的空间。
							if (this._currentPage_num==1) {
								this._rulerY_num+=_pg1BlankHeight_num;
							}
							//把标尺坐标值赋予给减字指示的属性。                                                                             
							this._jzX_num=this._rulerX_num;
							this._jzY_num=this._rulerY_num-this._jzHeight_num;
							//接着，标尺移动至下一个位置。
							this._rulerX_num=this._rulerX_num+this._jzWidth_num;
						}
					}
					break;
				case 1 :
					//[还没完成] [竖排版代码] 
					break;
			}
		}
		//readOne方法到此结束。
		//以下方法用于设定即将单独显示的页码，需要预排版完成之后才可使用。
		public function setPage(pgNumber:Number):void {
			if (this._currentPage_num<=this._lastPage_num) {
				//如果当前页码不大于总页数。
				this.inputFinished();
				//都设定页码了，那肯定是预排版结束了。
				this._currentPage_num=pgNumber;
				this._finishedCurrentPage_bool=false;
				//刚开始读取一页的信息，所以本页是没有完成的。
				this._eleIndex_num=this._myData_array[pgNumber].stEleIndex_num;
				this._jzSurplus_num=this._myData_array[pgNumber].stJzIndex_num;
				//把当前页的信息从_myData_arra里读出。
				//
				switch (this._format_num) {
					case 0 :
						//若为横排。
						this._rulerX_num=0;
						this._rulerY_num=this._innerDistance_num;
						this._preY_num=this._innerDistance_num;
						//标尺回到左上角。与本页第一字同元素的上页码最后的那几个字要用到的标尺也设定一下。
						if (this._currentPage_num==1) {
							this._rulerY_num+=_pg1BlankHeight_num;
						}
						break;
					case 1 :
						//[还没完成] [竖排版代码] 
						break;
				}
			}
		}
		//setPage方法到此结束。
		//以下方法用于取得当前字应在位置的信息。
		public function getOne():void {
			switch (this._format_num) {
				case 0 :
					//若为横排。
					if (this._jzSurplus_num>0) {
						//如果还有与本页第一字同元素的前页最后的字没排完，就把它们排到pre区。
						this._jzX_num=this._preX_num;
						this._jzY_num=this._preY_num-this._jzHeight_num;
						//计算如何排字！
						this._preX_num+=this._jzWidth_num;
						//pre标尺移动。
					} else if (this._finishedCurrentPage_bool) {
						//如果本页排满，就把当前字排到tail区。
						this._jzX_num=this._tailX_num;
						this._jzY_num=this._tailY_num-this._jzHeight_num;
						//计算如何排字！
						this._tailX_num+=this._jzWidth_num;
						//tail标尺移动。
					} else {
						//如果不属于以上两种情况，那当前字就是应该排在本页的字。开始排！
						if ((this._rulerX_num+this._jzWidth_num)<=(this._pageWidth_num)) {
							//如果本行还能容纳当前字，就排在这行！
							//把标尺坐标值赋予给减字指示的属性。   
							this._jzX_num=this._rulerX_num;
							this._jzY_num=this._rulerY_num-this._jzHeight_num;
							//接着，标尺移动至下一个位置。
							this._rulerX_num=this._rulerX_num+this._jzWidth_num;
						} else {
							//如果本行不能容纳当前字，换行（甚至准备往tail区排字）。
							//这时候，如果本页至少还能再容纳一行字，就换行。
							if ((this._rulerY_num+this._innerDistance_num)<=this._pageHeight_num) {
								this._rulerX_num=0;
								this._rulerY_num+=this._innerDistance_num;
								//把标尺坐标值赋予给减字指示的属性。
								this._jzX_num=this._rulerX_num;
								this._jzY_num=this._rulerY_num-this._jzHeight_num;
								//接着，标尺移动至下一个位置。
								this._rulerX_num=this._rulerX_num+this._jzWidth_num;
							} else {
								//反之，如果本页不能再容纳下一行字，就往tail区排字。
								this._jzY_num=this._tailY_num-this._jzHeight_num;
								//计算如何排字！
								this._tailX_num+=this._jzWidth_num;
								//tail标尺移动。
							}
						}
					}
					break;
				case 1 :
					//[还没完成] [竖排版代码] 
					break;
			}
		}
		//getOne方法到此结束。
		//以下方法用于打字间空格。
		public function space(level:uint):void {
			switch (this._format_num) {
				case 0 :
					if (level==1) {
						this._rulerX_num+=(this._characterSpacing1_num*this._jzScale_num);
					} else if (level==2) {
						this._rulerX_num+=(this._characterSpacing2_num*this._jzScale_num);
					} else if (level>=3) {
						this._rulerX_num+=(this._characterSpacing3_num*this._jzScale_num);
					}
					break;
				case 1 :
					//[还没完成] [竖排版代码] 
					break;
			}
		}
		//space方法到此结束。
		//以下方法用于初始化。每一次重新排版前（即便不是载入新文件，只是调整字体等）都要初始化一次。
		public function initialize():void {
			this._jzSurplus_num=0;
			this._currentPage_num=0;
			this._finishedCurrentPage_bool=false;
			this._formatConfirmed_bool=false;
			this._readyForOutput_bool=false;
			this._myData_array=[{stEleIndex_num:0,stJzIndex_num:0,eleAmount:0}];
			this._rulerX_num=0;
			this._rulerY_num=0;
			this._fontName_str="DroidSansFallback";
			this._lastPage_num=0;
			this._pageWidth_num=500;
			this._pageHeight_num=750;
			this._sideDistanceX_num=35;
			this._sideDistanceY_num=35;
			this._innerDistance_num=75;
			this._pg1BlankHeight_num=90;
			this._jzScale_num=100;
			this._characterSpacing1_num=3;
			this._characterSpacing2_num=6;
			this._characterSpacing3_num=9;
			this._titleAreaX_num=75;
			this._titleAreaY_num=0;
			this._titleAreaWidth_num=200;
			this._titleAreaHeight_num=100;
			this._infoAreaX_num=200;
			this._infoAreaY_num=110;
			this._infoAreaWidth_num=50;
			this._infoAreaHeight_num=50;
			this._pitchAreaX_num=50;
			this._pitchAreaY_num=150;
			this._pitchAreaWidth_num=100;
			this._pitchAreaHeight_num=50;
			this._pgNumAreaX_num=320;
			this._pgNumAreaY_num=650;
			this._pgNumAreaWidth_num=50;
			this._pgNumAreaHeight_num=50;
			this._preX_num=0;
			this._preY_num=150;
			this._tailX_num=0;
			this._tailY_num=650;
			this._format_num=0;
			this._jzWidth_num=0;
			this._jzHeight_num=0;
			this._jzX_num=0;
			this._jzY_num=0;
			this._eleIndex_num=0;
			this._jzIndex_num=0;
			this._flexObjMode_bool=false;
		}
		//initialize方法到此结束。
	}
}