package qin.freeViewer{
	import flash.display.*;
	import flash.events.*;
	import flash.text.TextFieldAutoSize;
	//import mx.events.EventDispatcher;
	public class Operator {
		//Operator类是真正执行构建页面工作的。它的方法processAnElement被Timer一次次调用，做出所有的字，并且在formatManager_fm对象的指导下排好。
		public var myRootObj:Object;
		public var currentPageJp;
		public var fmObj:Object;
		public var dataXMLList:XMLList;
		//
		public var eleCounter_num:Number = 0;
		//元素计数.主要用于给字命名。
		private var jzCounter_num:Number = 0;
		//字计数.主要用于给字命名。
		private var currentPage_num:Number = 0;
		//页码。通过和formatManager_fm对象中的同名属相比较判断是否要新建页面。
		private var currentJzJp;
		//当前字的引用。
		//
		private var rh_fingering_str:String = "勾";
		//“挑”、“勾”、“撮”……这一类指法。
		private var rh_string1_str:String = "5";
		private var rh_string2_str:String;
		private var lh_fingering1_str:String = "食";
		//“大”、“名”、“中”、“散”……这一类指法。
		private var lh_subFingering1_str:String = "";
		//“注”、“搯起”、“上”……这一类指法。
		private var lh_subSubFingering1_str:String = "滸";
		//“滸”……这一类指法。
		private var lh_hui1_str:String = "5";
		private var lh_fen1_str:String = "1";
		private var lh_subHui1_str:String = "7";
		private var lh_subFen1_str:String = "6";
                //“上七六”这一类指法中的“七六”就关联上面的两个属性。
		private var lh_fingering2_str:String;
		private var lh_subFingering2_str:String;
		private var lh_hui2_str:String;
		private var lh_fen2_str:String;
		//存储指法数据的属性。它们每一次的值由jzp文档每一对应元素内容决定。
                private var regRectsArray_array:Array = new Array();
		//临时存储“上中下”类减字内部元素的数组。
                private var regRectsRulerY_num:Number = 0;
		//构建“上中下”类减字用到的标尺。此类减字不需要水平标尺。
		private var normalRect_width:Number;
		private var normalRect_height:Number;
                //标准字框。
		//下面是用来接收转送字体部件构架比例信息的属性。
		private var scale_lv1_lv2WithNothing_offsetX:Number;
		private var scale_lv1_lv2WithNothing_offsetY:Number;
		private var scale_lv1_lv2WithNothing_width:Number;
		private var scale_lv1_lv2WithNothing_height:Number;
		//Lv1中，右手指法为“挑”、“勾”这一类时，lv2的相关信息。右手指法是“撮”这一类时不适用。
		private var scale_lv1_lv2LWithCuo_offsetX:Number;
		private var scale_lv1_lv2LWithCuo_offsetY:Number;
		private var scale_lv1_lv2LWithCuo_width:Number;
		private var scale_lv1_lv2LWithCuo_height:Number;
		//Lv1中，右手指法为“撮”时，左边lv2的相关信息。
		private var scale_lv1_lv2RWithCuo_offsetX:Number;
		private var scale_lv1_lv2RWithCuo_offsetY:Number;
		private var scale_lv1_lv2RWithCuo_width:Number;
		private var scale_lv1_lv2RWithCuo_height:Number;
		//Lv1中，右手指法为“撮”时，右边lv2的相关信息。
		//“撮”。
		private var scale_lv1_Cuo_offsetX:Number;
		private var scale_lv1_Cuo_offsetY:Number;
		private var scale_lv1_Cuo_width:Number;
		private var scale_lv1_Cuo_height:Number;
		//Lv1中，“撮”的相关信息。
                //
		private var scale_lv2_lhFingeringWithoutHuifen_offsetX:Number;
		private var scale_lv2_lhFingeringWithoutHuifen_offsetY:Number;
		private var scale_lv2_lhFingeringWithoutHuifen_width:Number;
		private var scale_lv2_lhFingeringWithoutHuifen_height:Number;
		//Lv2中，左手指法为“散”时，左手指法“散”的相关信息。
		private var scale_lv2_lhFingeringWithHuiWithoutFen_offsetX:Number;
		private var scale_lv2_lhFingeringWithHuiWithoutFen_offsetY:Number;
		private var scale_lv2_lhFingeringWithHuiWithoutFen_width:Number;
		private var scale_lv2_lhFingeringWithHuiWithoutFen_height:Number;
		//Lv2中，左手指法为“大”“食”这一类且只显示徽位（即徽位为整）时，左手指法自身的相关信息。
		private var scale_lv2_lhFingeringWithHuifen_offsetX:Number;
		private var scale_lv2_lhFingeringWithHuifen_offsetY:Number;
		private var scale_lv2_lhFingeringWithHuifen_width:Number;
		private var scale_lv2_lhFingeringWithHuifen_height:Number;
		//Lv2中，左手指法为“大”“食”这一类且显示分（即徽位不为整）时，时，左手指法自身的相关信息。
		private var scale_lv2_lhHuiWithoutFen_offsetX:Number;
		private var scale_lv2_lhHuiWithoutFen_offsetY:Number;
		private var scale_lv2_lhHuiWithoutFen_width:Number;
		private var scale_lv2_lhHuiWithoutFen_height:Number;
		//Lv2中，只显示徽（即徽位为整）时，徽自身的相关信息。
		private var scale_lv2_lhHui1WithoutFen_offsetX:Number;
		private var scale_lv2_lhHui1WithoutFen_offsetY:Number;
		private var scale_lv2_lhHui1WithoutFen_width:Number;
		private var scale_lv2_lhHui1WithoutFen_height:Number;
		//Lv2中，只显示徽（即徽位为整）时，一徽自身的相关信息。
                //因为一徽的“一”很扁，所以其x、y、宽、高用一组单独的值。
		private var scale_lv2_lhHuiWithFen_offsetX:Number;
		private var scale_lv2_lhHuiWithFen_offsetY:Number;
		private var scale_lv2_lhHuiWithFen_width:Number;
		private var scale_lv2_lhHuiWithFen_height:Number;
		//Lv2中，显示徽也显示分（即徽位不为整）时，徽自身的相关信息。
		private var scale_lv2_lhHui1WithFen_offsetX:Number;
		private var scale_lv2_lhHui1WithFen_offsetY:Number;
		private var scale_lv2_lhHui1WithFen_width:Number;
		private var scale_lv2_lhHui1WithFen_height:Number;
		//Lv2中，显示徽也显示分（即徽位不为整）时，一徽自身的相关信息。
                //因为一徽的“一”很扁，所以其x、y、宽、高用一组单独的值。
		private var scale_lv2_lhFen_offsetX:Number;
		private var scale_lv2_lhFen_offsetY:Number;
		private var scale_lv2_lhFen_width:Number;
		private var scale_lv2_lhFen_height:Number;
		//Lv2中，显示徽也显示分（即徽位不为整）时，分的相关信息。
		private var scale_lv2_lhFen1_offsetX:Number;
		private var scale_lv2_lhFen1_offsetY:Number;
		private var scale_lv2_lhFen1_width:Number;
		private var scale_lv2_lhFen1_height:Number;
		//Lv2中，显示徽也显示分（即徽位不为整）时，一分的相关信息。
                //因为一分的“一”很扁，所以其x、y、宽、高用一组单独的值。
		private var scale_lv2_ChuoWithHuiWithoutFen_offsetX:Number;
		private var scale_lv2_ChuoWithHuiWithoutFen_offsetY:Number;
		private var scale_lv2_ChuoWithHuiWithoutFen_width:Number;
		private var scale_lv2_ChuoWithHuiWithoutFen_height:Number;
		//Lv2中，只显示徽（即徽位为整）时，绰的相关信息。
		private var scale_lv2_ChuoWithHuifen_offsetX:Number;
		private var scale_lv2_ChuoWithHuifen_offsetY:Number;
		private var scale_lv2_ChuoWithHuifen_width:Number;
		private var scale_lv2_ChuoWithHuifen_height:Number;
		//Lv2中，显示徽也显示分（即徽位不为整）时，绰的相关信息。
		private var scale_lv2_ZhuWithHuiWithoutFen1_offsetX:Number;
		private var scale_lv2_ZhuWithHuiWithoutFen1_offsetY:Number;
		private var scale_lv2_ZhuWithHuiWithoutFen1_width:Number;
		private var scale_lv2_ZhuWithHuiWithoutFen1_height:Number;
		//Lv2中，只显示徽（即徽位为整）时，高度最小的注的相关信息。
		private var scale_lv2_ZhuWithHuiWithoutFen2_offsetX:Number;
		private var scale_lv2_ZhuWithHuiWithoutFen2_offsetY:Number;
		private var scale_lv2_ZhuWithHuiWithoutFen2_width:Number;
		private var scale_lv2_ZhuWithHuiWithoutFen2_height:Number;
		//Lv2中，只显示徽（即徽位为整）时，高度中等的注的相关信息。
		private var scale_lv2_ZhuWithHuiWithoutFen3_offsetX:Number;
		private var scale_lv2_ZhuWithHuiWithoutFen3_offsetY:Number;
		private var scale_lv2_ZhuWithHuiWithoutFen3_width:Number;
		private var scale_lv2_ZhuWithHuiWithoutFen3_height:Number;
		//Lv2中，只显示徽（即徽位为整）时，高度最大的注的相关信息。
		private var scale_lv2_ZhuWithHuifen1_offsetX:Number;
		private var scale_lv2_ZhuWithHuifen1_offsetY:Number;
		private var scale_lv2_ZhuWithHuifen1_width:Number;
		private var scale_lv2_ZhuWithHuifen1_height:Number;
		//Lv2中，显示徽也显示分（即徽位不为整）时，高度最小的注的相关信息。
		private var scale_lv2_ZhuWithHuifen2_offsetX:Number;
		private var scale_lv2_ZhuWithHuifen2_offsetY:Number;
		private var scale_lv2_ZhuWithHuifen2_width:Number;
		private var scale_lv2_ZhuWithHuifen2_height:Number;
		//Lv2中，显示徽也显示分（即徽位不为整）时，高度中等的注的相关信息。
		private var scale_lv2_ZhuWithHuifen3_offsetX:Number;
		private var scale_lv2_ZhuWithHuifen3_offsetY:Number;
		private var scale_lv2_ZhuWithHuifen3_width:Number;
		private var scale_lv2_ZhuWithHuifen3_height:Number;
		//Lv2中，显示徽也显示分（即徽位不为整）时，高度最大的注的相关信息。

		private var scale_lv2_DaiqiWithHuiWithoutFen_offsetX:Number;
		private var scale_lv2_DaiqiWithHuiWithoutFen_offsetY:Number;
		private var scale_lv2_DaiqiWithHuiWithoutFen_width:Number;
		private var scale_lv2_DaiqiWithHuiWithoutFen_height:Number;
		//Lv2中，只显示徽（即徽位为整）时，“带起”的相关信息。
		private var scale_lv2_DaiqiWithHuifen_offsetX:Number;
		private var scale_lv2_DaiqiWithHuifen_offsetY:Number;
		private var scale_lv2_DaiqiWithHuifen_width:Number;
		private var scale_lv2_DaiqiWithHuifen_height:Number;
		//Lv2中，显示徽也显示分（即徽位不为整）时，“带起”的相关信息。
		private var scale_lv2_TaoqiWithHuiWithoutFen_offsetX:Number;
		private var scale_lv2_TaoqiWithHuiWithoutFen_offsetY:Number;
		private var scale_lv2_TaoqiWithHuiWithoutFen_width:Number;
		private var scale_lv2_TaoqiWithHuiWithoutFen_height:Number;
		//Lv2中，只显示徽（即徽位为整）时，“搯起”的相关信息。
		private var scale_lv2_TaoqiWithHuifen_offsetX:Number;
		private var scale_lv2_TaoqiWithHuifen_offsetY:Number;
		private var scale_lv2_TaoqiWithHuifen_width:Number;
		private var scale_lv2_TaoqiWithHuifen_height:Number;
		//Lv2中，显示徽也显示分（即徽位不为整）时，“搯起”的相关信息。
		private var scale_lv2_ZhuaqiWithHuiWithoutFen_offsetX:Number;
		private var scale_lv2_ZhuaqiWithHuiWithoutFen_offsetY:Number;
		private var scale_lv2_ZhuaqiWithHuiWithoutFen_width:Number;
		private var scale_lv2_ZhuaqiWithHuiWithoutFen_height:Number;
		//Lv2中，只显示徽（即徽位为整）时，“抓起”的相关信息。
		private var scale_lv2_ZhuaqiWithHuifen_offsetX:Number;
		private var scale_lv2_ZhuaqiWithHuifen_offsetY:Number;
		private var scale_lv2_ZhuaqiWithHuifen_width:Number;
		private var scale_lv2_ZhuaqiWithHuifen_height:Number;
		//Lv2中，显示徽也显示分（即徽位不为整）时，“抓起”的相关信息。

		private var scale_lv2_lv3WithLhFSan_offsetX:Number;
		private var scale_lv2_lv3WithLhFSan_offsetY:Number;
		private var scale_lv2_lv3WithLhFSan_width:Number;
		private var scale_lv2_lv3WithLhFSan_height:Number;
		//Lv2中，左手指法为“散”，且无“绰”、“注”时，lv3的相关信息。
		private var scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_offsetX:Number;
		private var scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_offsetY:Number;
		private var scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_width:Number;
		private var scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_height:Number;
		//Lv2中，只显示徽（即徽位为整），且无“绰”、“注”时，lv3的相关信息。
		private var scale_lv2_lv3WithHuiWithoutFenWithChuo_offsetX:Number;
		private var scale_lv2_lv3WithHuiWithoutFenWithChuo_offsetY:Number;
		private var scale_lv2_lv3WithHuiWithoutFenWithChuo_width:Number;
		private var scale_lv2_lv3WithHuiWithoutFenWithChuo_height:Number;
		//Lv2中，只显示徽（即徽位为整），且有“绰”时，lv3的相关信息。
		private var scale_lv2_lv3WithHuiWithoutFenWithZhu_offsetX:Number;
		private var scale_lv2_lv3WithHuiWithoutFenWithZhu_offsetY:Number;
		private var scale_lv2_lv3WithHuiWithoutFenWithZhu_width:Number;
		private var scale_lv2_lv3WithHuiWithoutFenWithZhu_height:Number;
		//Lv2中，只显示徽（即徽位为整），且有“注”时，lv3的相关信息。
		private var scale_lv2_lv3WithHuifenWithoutChuozhu_offsetX:Number;
		private var scale_lv2_lv3WithHuifenWithoutChuozhu_offsetY:Number;
		private var scale_lv2_lv3WithHuifenWithoutChuozhu_width:Number;
		private var scale_lv2_lv3WithHuifenWithoutChuozhu_height:Number;
		//Lv2中，显示徽也显示分（即徽位不为整），且无“绰”、“注”时，lv3的相关信息。
		private var scale_lv2_lv3WithHuifenWithChuo_offsetX:Number;
		private var scale_lv2_lv3WithHuifenWithChuo_offsetY:Number;
		private var scale_lv2_lv3WithHuifenWithChuo_width:Number;
		private var scale_lv2_lv3WithHuifenWithChuo_height:Number;
		//Lv2中，显示徽也显示分（即徽位不为整），且有“绰”时，lv3的相关信息。
		private var scale_lv2_lv3WithHuifenWithZhu_offsetX:Number;
		private var scale_lv2_lv3WithHuifenWithZhu_offsetY:Number;
		private var scale_lv2_lv3WithHuifenWithZhu_width:Number;
		private var scale_lv2_lv3WithHuifenWithZhu_height:Number;
		//Lv2中，显示徽也显示分（即徽位不为整），且有“注”时，lv3的相关信息。
		//“挑”。
		private var scale_lv3_Tiao_offsetX:Number;
		private var scale_lv3_Tiao_offsetY:Number;
		private var scale_lv3_Tiao_width:Number;
		private var scale_lv3_Tiao_height:Number;
		//Lv3中，“挑”的相关信息。
		private var scale_lv3_lv4WithTiao_offsetX:Number;
		private var scale_lv3_lv4WithTiao_offsetY:Number;
		private var scale_lv3_lv4WithTiao_width:Number;
		private var scale_lv3_lv4WithTiao_height:Number;
		//Lv3中，右手指法为“挑”时，lv4的相关信息。
		//“勾”。
		private var scale_lv3_Gou_offsetX:Number;
		private var scale_lv3_Gou_offsetY:Number;
		private var scale_lv3_Gou_width:Number;
		private var scale_lv3_Gou_height:Number;
		//Lv3中，“勾”的相关信息。
		private var scale_lv3_lv4WithGou_offsetX:Number;
		private var scale_lv3_lv4WithGou_offsetY:Number;
		private var scale_lv3_lv4WithGou_width:Number;
		private var scale_lv3_lv4WithGou_height:Number;
		//Lv3中，右手指法为“勾”时，lv4的相关信息。
		//“打”。
		private var scale_lv3_Da_offsetX:Number;
		private var scale_lv3_Da_offsetY:Number;
		private var scale_lv3_Da_width:Number;
		private var scale_lv3_Da_height:Number;
		//Lv3中，“打”的相关信息。
		private var scale_lv3_lv4WithDa_offsetX:Number;
		private var scale_lv3_lv4WithDa_offsetY:Number;
		private var scale_lv3_lv4WithDa_width:Number;
		private var scale_lv3_lv4WithDa_height:Number;
		//Lv3中，右手指法为“打”时，lv4的相关信息。
		//“抹”。
		private var scale_lv3_Mo_offsetX:Number;
		private var scale_lv3_Mo_offsetY:Number;
		private var scale_lv3_Mo_width:Number;
		private var scale_lv3_Mo_height:Number;
		//Lv3中，“抹”的相关信息。
		private var scale_lv3_lv4WithMo_offsetX:Number;
		private var scale_lv3_lv4WithMo_offsetY:Number;
		private var scale_lv3_lv4WithMo_width:Number;
		private var scale_lv3_lv4WithMo_height:Number;
		//Lv3中，右手指法为“抹”时，lv4的相关信息。
		//“摘”。
		private var scale_lv3_Zhai_offsetX:Number;
		private var scale_lv3_Zhai_offsetY:Number;
		private var scale_lv3_Zhai_width:Number;
		private var scale_lv3_Zhai_height:Number;
		//Lv3中，“摘”的相关信息。
		private var scale_lv3_lv4WithZhai_offsetX:Number;
		private var scale_lv3_lv4WithZhai_offsetY:Number;
		private var scale_lv3_lv4WithZhai_width:Number;
		private var scale_lv3_lv4WithZhai_height:Number;
		//Lv3中，右手指法为“摘”时，lv4的相关信息。
		//“剔”。
		private var scale_lv3_Ti_offsetX:Number;
		private var scale_lv3_Ti_offsetY:Number;
		private var scale_lv3_Ti_width:Number;
		private var scale_lv3_Ti_height:Number;
		//Lv3中，“剔”的相关信息。
		private var scale_lv3_lv4WithTi_offsetX:Number;
		private var scale_lv3_lv4WithTi_offsetY:Number;
		private var scale_lv3_lv4WithTi_width:Number;
		private var scale_lv3_lv4WithTi_height:Number;
		//Lv3中，右手指法为“剔”时，lv4的相关信息。
		//“擘”。
		private var scale_lv3_Bo_offsetX:Number;
		private var scale_lv3_Bo_offsetY:Number;
		private var scale_lv3_Bo_width:Number;
		private var scale_lv3_Bo_height:Number;
		//Lv3中，“擘”的相关信息。
		private var scale_lv3_lv4WithBo_offsetX:Number;
		private var scale_lv3_lv4WithBo_offsetY:Number;
		private var scale_lv3_lv4WithBo_width:Number;
		private var scale_lv3_lv4WithBo_height:Number;
		//Lv3中，右手指法为“擘”时，lv4的相关信息。
		//“托”。
		private var scale_lv3_Tuo_offsetX:Number;
		private var scale_lv3_Tuo_offsetY:Number;
		private var scale_lv3_Tuo_width:Number;
		private var scale_lv3_Tuo_height:Number;
		//Lv3中，“托”的相关信息。
		private var scale_lv3_lv4WithTuo_offsetX:Number;
		private var scale_lv3_lv4WithTuo_offsetY:Number;
		private var scale_lv3_lv4WithTuo_width:Number;
		private var scale_lv3_lv4WithTuo_height:Number;
		//Lv3中，右手指法为“托”时，lv4的相关信息。
		//“滾”。
		private var scale_lv3_Gun_offsetX:Number;
		private var scale_lv3_Gun_offsetY:Number;
		private var scale_lv3_Gun_width:Number;
		private var scale_lv3_Gun_height:Number;
		//Lv3中，“滾”的相关信息。
		private var scale_lv3_lv4WithGun_offsetX:Number;
		private var scale_lv3_lv4WithGun_offsetY:Number;
		private var scale_lv3_lv4WithGun_width:Number;
		private var scale_lv3_lv4WithGun_height:Number;
		//Lv3中，右手指法为“滾”时，lv4的相关信息。
		//
		private var scale_lv3_lv4WithNothing_offsetX:Number;
		private var scale_lv3_lv4WithNothing_offsetY:Number;
		private var scale_lv3_lv4WithNothing_width:Number;
		private var scale_lv3_lv4WithNothing_height:Number;
		//Lv3中，右手指法为“撮”一类时，lv4的相关信息。就是让lv4直接占满lv3。
		private var scale_lv4_String0_offsetX:Number;
		private var scale_lv4_String0_offsetY:Number;
		private var scale_lv4_String0_width:Number;
		private var scale_lv4_String0_height:Number;
		//右手指法为“勾”时，Lv4中，弦2-7的相关信息。
		private var scale_lv4_String1_offsetX:Number;
		private var scale_lv4_String1_offsetY:Number;
		private var scale_lv4_String1_width:Number;
		private var scale_lv4_String1_height:Number;
		//右手指法为“勾”时，Lv4中，弦2-7的相关信息。
		private var scale_regRects_singleRect_width:Number;
		private var scale_regRects_singleRect_height:Number;
                private var scale_regRects_spacing:Number;
		private var scale_regRects_singleRect1_width:Number;
		private var scale_regRects_singleRect1_height:Number;
                private var scale_regRects_exUpperSpacing:Number;
                private var scale_regRects_exLowerSpacing:Number;
                //因为“一”很扁，所以其宽、高用一组单独的值，且上下有额外的空白填充。
		//“规则矩形”的相关信息。“规则矩形”指的是“上九”、“上七六”这一类减字。
		//
		public function Operator() {
			//构造方法。
			//this.initialize();
		}
		public function isLhLRFingering(fingering:String):Boolean {
			//是“上”、“下”、“進”、“退”、“復”一类指法么。
                        if ((this.lh_subFingering1_str == "上") || (this.lh_subFingering1_str == "下") || (this.lh_subFingering1_str == "進") || (this.lh_subFingering1_str == "退")|| (this.lh_subFingering1_str == "復")|| (this.lh_subFingering1_str == "撞")){
                                //是“上”、“下”、“進”、“退”、“復”。
                                return true;
                        }else{
                                return false;
                        }
		}
		public function jzConstructLv1(x:Number,y:Number,width:Number,height:Number):void {
			//拼字第一步。确定大体架构，如果是“挑”、“勾”这一类的指法就不在这一步上具体部首，如果是“撮”这一类就直接上。
			trace("Lv1");
			if (this.rh_fingering_str == "blank"){
			//如果右手指法为空，那么，减字可能是“抓起”类或者“上”类。
				if (this.lh_fingering1_str == "blank"){
                        //此时，如果左手（第一级）指法为空，那么减字是“上”、“吟”等这类。
				        if (this.isLhLRFingering(lh_subFingering1_str)){
                                //是“上”、“下”、“進”、“退”、“復”、“撞”。
			                        if (this.lh_subSubFingering1_str != "blank"){
                                        //如果有“滸”一类的字，上。
                                        this.regRectsArray_array.push(this.lh_subSubFingering1_str);
                                    }
                                    this.regRectsArray_array.push(this.lh_subFingering1_str);
                                    //“上”、“下”、“進”、“退”、“復”、“撞”。
                                    if (this.lh_subFen1_str != "blank"){
                                    //如果徽位不为空，上。
                                        this.regRectsArray_array.push(this.lh_subHui1_str);
                                        if (this.lh_subFen1_str != "0"){
                                            //如果分不为0，上。
                                            this.regRectsArray_array.push(this.lh_subFen1_str);
                                        }
                                    }
                        }else {
                                //[未完成][“吟”等指法][考虑优化]
								if (this.lh_subSubFingering1_str != "blank"){
                                    //如果是单独的“滸”、“吟”等指法，上。
                                    this.regRectsArray_array.push(this.lh_subSubFingering1_str);
                                }
                        }
                        //注意，任何此类指法均被对应到lh_fingering1这一组，无论其之前的实际指法在上一字里是位于lh_fingering1组还是lh_fingering2组。			                
				}else{
                    //否则，减字是“抓起”类。
					this.currentJzJp = this.currentPageJp.createEmptyChild("jz_" + String(this.jzCounter_num) + "_jp");
					//生成一个新空白字。
				    this.myRootObj.jz_array.push(this.currentJzJp);
					//向减字数组放入新字。
			                this.jzConstructLv2(x+(width*this.scale_lv1_lv2WithNothing_offsetX),y+(height*this.scale_lv1_lv2WithNothing_offsetY),width*this.scale_lv1_lv2WithNothing_width,height*this.scale_lv1_lv2WithNothing_height,"left");
					//全部空间都给第二步。
                         		this.typeset();
			                //排一下版。
			        }
			}else if (this.rh_fingering_str == "撮"){
			//“撮”一类左手双弦的。
					this.currentJzJp = this.currentPageJp.createEmptyChild("jz_" + String(this.jzCounter_num) + "_jp");
					//生成一个新空白字。
					this.myRootObj.jz_array.push(this.currentJzJp);
					//向减字数组放入新字。
					this.currentJzJp.createJzPart("撮","lh1_fingenring_勾",x+(width*this.scale_lv1_Cuo_offsetX),y+(height*this.scale_lv1_Cuo_offsetY),width*this.scale_lv1_Cuo_width,height*this.scale_lv1_Cuo_height);
					//来一个“撮”。
					//[HERE!]
					this.currentJzJp.metaVel_num = this.myRootObj.dataConverter_dc.getVel(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].r_hand[0].action[0].@vel);
					//写入力度值。
		                        this.jzConstructLv2(x+(width*this.scale_lv1_lv2LWithCuo_offsetX),y+(height*this.scale_lv1_lv2LWithCuo_offsetY),width*this.scale_lv1_lv2LWithCuo_width,height*this.scale_lv1_lv2LWithCuo_height,"left");
					//第二步，左半边。
		                        this.jzConstructLv2(x+(width*this.scale_lv1_lv2RWithCuo_offsetX),y+(height*this.scale_lv1_lv2RWithCuo_offsetY),width*this.scale_lv1_lv2RWithCuo_width,height*this.scale_lv1_lv2RWithCuo_height,"right");
					//第二步，右半边。
                                        [未完成]
                                 	this.typeset();
			                //排一下版。
			}else{
			//其它情况，其实就是最常见的那些“抹挑勾剔打摘滾拂……”。
					this.currentJzJp = this.currentPageJp.createEmptyChild("jz_" + String(this.jzCounter_num) + "_jp");
					//生成一个新空白字。
					this.myRootObj.jz_array.push(this.currentJzJp);
					//向减字数组放入新字。
					//[HERE!]
					this.currentJzJp.metaVel_num = this.myRootObj.dataConverter_dc.getVel(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].r_hand[0].action[0].@vel);
					this.jzConstructLv2(x+(width*this.scale_lv1_lv2WithNothing_offsetX),y+(height*this.scale_lv1_lv2WithNothing_offsetY),width*this.scale_lv1_lv2WithNothing_width,height*this.scale_lv1_lv2WithNothing_height,"left");
					//全部空间都给第二步。
 			                this.typeset();
			                //排一下版。
            }
			this.myRootObj.formatManager_fm.space(1);
		}
		public function jzConstructLv2(x:Number,y:Number,width:Number,height:Number,part:String):void {
			//拼字第二步。左手指法的第一部分，例如“大九注”。“挑”、“勾”这一类右手指法只对应这第一部分的左手指法。
			var lh_fingering:String;
			var lh_subFingering:String;
			var lh_hui:String;
			var lh_fen:String;
			var tempHeight:Number;
			//由于这个方法可以用来处理同一个字中的多个左手指法部分，因此这里声明一些属性，在下面指向要处理的部分，以后的逻辑中就直接调用这些属性。

			if (part == "left") {
				lh_fingering = this.lh_fingering1_str;
				lh_subFingering = this.lh_subFingering1_str;
				lh_hui = this.lh_hui1_str;
				lh_fen = this.lh_fen1_str;
			} else {
				lh_fingering = this.lh_fingering2_str;
				lh_subFingering = this.lh_subFingering2_str;
				lh_hui = this.lh_hui2_str;
				lh_fen = this.lh_fen2_str;
			}
			trace("Lv2");
			if (lh_fingering == "散") {
				//“散”的情况下，不需要徽位显示，因此直接上“散”。
				trace("散");
				this.currentJzJp.createJzPart("散","lh_fingenring_散",x+(width*this.scale_lv2_lhFingeringWithoutHuifen_offsetX),y+(height*this.scale_lv2_lhFingeringWithoutHuifen_offsetY),width*this.scale_lv2_lhFingeringWithoutHuifen_width,height*this.scale_lv2_lhFingeringWithoutHuifen_height);
				this.jzConstructLv3(x+(width*this.scale_lv2_lv3WithLhFSan_offsetX),y+(height*this.scale_lv2_lv3WithLhFSan_offsetY),width*this.scale_lv2_lv3WithLhFSan_width,height*this.scale_lv2_lv3WithLhFSan_height,part);
				//剩余空间都给第三步。
			} else {
				//否则，先上徽位。
				//把左手指法拼上去。
				if (lh_fen == "0") {
					this.currentJzJp.createJzPart(lh_fingering,"lh_fingenring"+lh_fingering,x+(width*this.scale_lv2_lhFingeringWithHuiWithoutFen_offsetX),y+(height*this.scale_lv2_lhFingeringWithHuiWithoutFen_offsetY),width*this.scale_lv2_lhFingeringWithHuiWithoutFen_width,height*this.scale_lv2_lhFingeringWithHuiWithoutFen_height);
					trace("");
				} else {
					this.currentJzJp.createJzPart(lh_fingering,"lh_fingenring"+lh_fingering,x+(width*this.scale_lv2_lhFingeringWithHuifen_offsetX),y+(height*this.scale_lv2_lhFingeringWithHuifen_offsetY),width*this.scale_lv2_lhFingeringWithHuifen_width,height*this.scale_lv2_lhFingeringWithHuifen_height);
					trace("分啦"+(width*this.scale_lv2_lhFingeringWithHuifen_width));
				}
				if (lh_fen == "0") {
				        //如果不需要显示分，就把全部空间都留给徽。
					if (lh_hui == "1") {
                                                //一徽的“一”很扁，要单独处理。
					        this.currentJzJp.createJzPart(lh_hui,"lh_hui_"+lh_hui,x+(width*this.scale_lv2_lhHui1WithoutFen_offsetX),y+(height*this.scale_lv2_lhHui1WithoutFen_offsetY),width*this.scale_lv2_lhHui1WithoutFen_width,height*this.scale_lv2_lhHui1WithoutFen_height);
					}else{
                                                this.currentJzJp.createJzPart(lh_hui,"lh_hui_"+lh_hui,x+(width*this.scale_lv2_lhHuiWithoutFen_offsetX),y+(height*this.scale_lv2_lhHuiWithoutFen_offsetY),width*this.scale_lv2_lhHuiWithoutFen_width,height*this.scale_lv2_lhHuiWithoutFen_height);
                                        }
                                        //
					if (lh_subFingering == "綽") {
						this.currentJzJp.createJzPart("綽","lh_fingenring_綽",x+(width*this.scale_lv2_ChuoWithHuiWithoutFen_offsetX),y+(height*this.scale_lv2_ChuoWithHuiWithoutFen_offsetY),width*this.scale_lv2_ChuoWithHuiWithoutFen_width,height*this.scale_lv2_ChuoWithHuiWithoutFen_height);
						this.jzConstructLv3(x+(width*this.scale_lv2_lv3WithHuiWithoutFenWithChuo_offsetX),y+(height*this.scale_lv2_lv3WithHuiWithoutFenWithChuo_offsetY),width*this.scale_lv2_lv3WithHuiWithoutFenWithChuo_width,height*this.scale_lv2_lv3WithHuiWithoutFenWithChuo_height,part);
					} else if (lh_subFingering=="注") {
						tempHeight = this.jzConstructLv3(x+(width*this.scale_lv2_lv3WithHuiWithoutFenWithZhu_offsetX),y+(height*this.scale_lv2_lv3WithHuiWithoutFenWithZhu_offsetY),width*this.scale_lv2_lv3WithHuiWithoutFenWithZhu_width,height*this.scale_lv2_lv3WithHuiWithoutFenWithZhu_height,part);
						this.currentJzJp.createJzPart("注","lh_fingenring_注",x+(width*this.scale_lv2_ZhuWithHuiWithoutFen2_offsetX),y+(height*this.scale_lv2_ZhuWithHuiWithoutFen2_offsetY),width*this.scale_lv2_ZhuWithHuiWithoutFen2_width,height*this.scale_lv2_ZhuWithHuiWithoutFen2_height);
						//“注”的高度取决于第三步结果的高度。
					} else if (lh_subFingering=="帶起") {
						this.currentJzJp.createJzPart("帶起", "lh_fingenring_帶起", x + (width * this.scale_lv2_DaiqiWithHuiWithoutFen_offsetX), y + (height * this.scale_lv2_DaiqiWithHuiWithoutFen_offsetY), width * this.scale_lv2_DaiqiWithHuiWithoutFen_width, height * this.scale_lv2_DaiqiWithHuiWithoutFen_height);
						this.currentJzJp.metaVel_num = this.myRootObj.dataConverter_dc.getVel(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[0].action[0].@vel);
					} else if (lh_subFingering=="搯起") {
						this.currentJzJp.createJzPart("搯起", "lh_fingenring_搯起", x + (width * this.scale_lv2_TaoqiWithHuiWithoutFen_offsetX), y + (height * this.scale_lv2_TaoqiWithHuiWithoutFen_offsetY), width * this.scale_lv2_TaoqiWithHuiWithoutFen_width, height * this.scale_lv2_TaoqiWithHuiWithoutFen_height);
						this.currentJzJp.metaVel_num = this.myRootObj.dataConverter_dc.getVel(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[0].action[0].@vel);
					} else if (lh_subFingering=="抓起") {
						this.currentJzJp.createJzPart("抓起", "lh_fingenring_抓起", x + (width * this.scale_lv2_ZhuaqiWithHuiWithoutFen_offsetX), y + (height * this.scale_lv2_ZhuaqiWithHuiWithoutFen_offsetY), width * this.scale_lv2_ZhuaqiWithHuiWithoutFen_width, height * this.scale_lv2_ZhuaqiWithHuiWithoutFen_height);
						this.currentJzJp.metaVel_num = this.myRootObj.dataConverter_dc.getVel(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[0].action[0].@vel);
					} else {
						this.jzConstructLv3(x+(width*this.scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_offsetX),y+(height*this.scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_offsetY),width*this.scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_width,height*this.scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_height,part);
					}
				} else {
					//否则，徽分占地各半。
					if (lh_hui == "1") {
                                                //一徽的“一”很扁，要单独处理。
					        this.currentJzJp.createJzPart(lh_hui,"lh_hui_"+lh_hui,x+(width*this.scale_lv2_lhHui1WithFen_offsetX),y+(height*this.scale_lv2_lhHui1WithFen_offsetY),width*this.scale_lv2_lhHui1WithFen_width,height*this.scale_lv2_lhHui1WithFen_height);
					}else{
					        this.currentJzJp.createJzPart(lh_hui,"lh_hui_"+lh_hui,x+(width*this.scale_lv2_lhHuiWithFen_offsetX),y+(height*this.scale_lv2_lhHuiWithFen_offsetY),width*this.scale_lv2_lhHuiWithFen_width,height*this.scale_lv2_lhHuiWithFen_height);
                                        }
					if (lh_fen == "1") {
                                                //一分的“一”很扁，也要单独处理。
					        this.currentJzJp.createJzPart(lh_fen,"lh_fen_"+lh_fen,x+(width*this.scale_lv2_lhFen1_offsetX),y+(height*this.scale_lv2_lhFen1_offsetY),width*this.scale_lv2_lhFen1_width,height*this.scale_lv2_lhFen1_height);

					}else{
					        this.currentJzJp.createJzPart(lh_fen,"lh_fen_"+lh_fen,x+(width*this.scale_lv2_lhFen_offsetX),y+(height*this.scale_lv2_lhFen_offsetY),width*this.scale_lv2_lhFen_width,height*this.scale_lv2_lhFen_height);
                                        }					
                                        //
					if (lh_subFingering == "綽") {
						this.currentJzJp.createJzPart("綽","lh_fingenring_綽",x+(width*this.scale_lv2_ChuoWithHuifen_offsetX),y+(height*this.scale_lv2_ChuoWithHuifen_offsetY),width*this.scale_lv2_ChuoWithHuifen_width,height*this.scale_lv2_ChuoWithHuifen_height);
						this.jzConstructLv3(x+(width*this.scale_lv2_lv3WithHuifenWithChuo_offsetX),y+(height*this.scale_lv2_lv3WithHuifenWithChuo_offsetY),width*this.scale_lv2_lv3WithHuifenWithChuo_width,height*this.scale_lv2_lv3WithHuifenWithChuo_height,part);
					} else if (lh_subFingering=="注") {
						tempHeight = this.jzConstructLv3(x+(width*this.scale_lv2_lv3WithHuifenWithZhu_offsetX),y+(height*this.scale_lv2_lv3WithHuifenWithZhu_offsetY),width*this.scale_lv2_lv3WithHuifenWithZhu_width,height*this.scale_lv2_lv3WithHuifenWithZhu_height,part);
						this.currentJzJp.createJzPart("注","lh_fingenring_注",x+(width*this.scale_lv2_ZhuWithHuifen2_offsetX),y+(height*this.scale_lv2_ZhuWithHuifen2_offsetY),width*this.scale_lv2_ZhuWithHuifen2_width,height*this.scale_lv2_ZhuWithHuifen2_height);
						//“注”的高度取决于第三步结果的高度。
					} else if (lh_subFingering=="帶起") {
						this.currentJzJp.createJzPart("帶起", "lh_fingenring_帶起", x + (width * this.scale_lv2_DaiqiWithHuifen_offsetX), y + (height * this.scale_lv2_DaiqiWithHuifen_offsetY), width * this.scale_lv2_DaiqiWithHuifen_width, height * this.scale_lv2_DaiqiWithHuifen_height);
						this.currentJzJp.metaVel_num = this.myRootObj.dataConverter_dc.getVel(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[0].action[0].@vel);
					} else if (lh_subFingering=="搯起") {
						this.currentJzJp.createJzPart("搯起", "lh_fingenring_搯起", x + (width * this.scale_lv2_TaoqiWithHuifen_offsetX), y + (height * this.scale_lv2_TaoqiWithHuifen_offsetY), width * this.scale_lv2_TaoqiWithHuifen_width, height * this.scale_lv2_TaoqiWithHuifen_height);
						this.currentJzJp.metaVel_num = this.myRootObj.dataConverter_dc.getVel(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[0].action[0].@vel);
					} else if (lh_subFingering=="抓起") {
						this.currentJzJp.createJzPart("抓起", "lh_fingenring_抓起", x + (width * this.scale_lv2_ZhuaqiWithHuifen_offsetX), y + (height * this.scale_lv2_ZhuaqiWithHuifen_offsetY), width * this.scale_lv2_ZhuaqiWithHuifen_width, height * this.scale_lv2_ZhuaqiWithHuifen_height);
						this.currentJzJp.metaVel_num = this.myRootObj.dataConverter_dc.getVel(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[0].action[0].@vel);
					} else {
						this.jzConstructLv3(x+(width*this.scale_lv2_lv3WithHuifenWithoutChuozhu_offsetX),y+(height*this.scale_lv2_lv3WithHuifenWithoutChuozhu_offsetY),width*this.scale_lv2_lv3WithHuifenWithoutChuozhu_width,height*this.scale_lv2_lv3WithHuifenWithoutChuozhu_height,part);
					}
				}


			}

		}
		public function jzConstructLv3(x:Number,y:Number,width:Number,height:Number,part:String):Number {
			//拼字第三步。右手指法的第二部分，如果是“挑”、“勾”这一类的指法就先在这一步上具体部首再进行下一步，如果是“撮”这一类就直接下一步。
			trace("Lv3");
			switch (this.rh_fingering_str) {
				//[此部分代码待优化]
				case "挑" :
					trace("挑");
					this.currentJzJp.createJzPart("挑","lh1_fingenring_挑",x+(width*this.scale_lv3_Tiao_offsetX),y+(height*this.scale_lv3_Tiao_offsetY),width*this.scale_lv3_Tiao_width,height*this.scale_lv3_Tiao_height);
					this.jzConstructLv4(x+(width*this.scale_lv3_lv4WithTiao_offsetX),y+(height*this.scale_lv3_lv4WithTiao_offsetY),width*this.scale_lv3_lv4WithTiao_width,height*this.scale_lv3_lv4WithTiao_height,part);
					return height;
					break;
				case "勾" :
					trace("勾");
					this.currentJzJp.createJzPart("勾","lh1_fingenring_勾",x+(width*this.scale_lv3_Gou_offsetX),y+(height*this.scale_lv3_Gou_offsetY),width*this.scale_lv3_Gou_width,height*this.scale_lv3_Gou_height);
					this.jzConstructLv4(x+(width*this.scale_lv3_lv4WithGou_offsetX),y+(height*this.scale_lv3_lv4WithGou_offsetY),width*this.scale_lv3_lv4WithGou_width,height*this.scale_lv3_lv4WithGou_height,part);
					return height;
					break;
				case "打" :
					trace("打");
					this.currentJzJp.createJzPart("打","lh1_fingenring_打",x+(width*this.scale_lv3_Da_offsetX),y+(height*this.scale_lv3_Da_offsetY),width*this.scale_lv3_Da_width,height*this.scale_lv3_Da_height);
					this.jzConstructLv4(x+(width*this.scale_lv3_lv4WithDa_offsetX),y+(height*this.scale_lv3_lv4WithDa_offsetY),width*this.scale_lv3_lv4WithDa_width,height*this.scale_lv3_lv4WithDa_height,part);
					return height;
					break;
				case "抹" :
					trace("抹");
					this.currentJzJp.createJzPart("抹","lh1_fingenring_抹",x+(width*this.scale_lv3_Mo_offsetX),y+(height*this.scale_lv3_Mo_offsetY),width*this.scale_lv3_Mo_width,height*this.scale_lv3_Mo_height);
					this.jzConstructLv4(x+(width*this.scale_lv3_lv4WithMo_offsetX),y+(height*this.scale_lv3_lv4WithMo_offsetY),width*this.scale_lv3_lv4WithMo_width,height*this.scale_lv3_lv4WithMo_height,part);
					return height;
					break;
				case "摘" :
					trace("摘");
					this.currentJzJp.createJzPart("摘","lh1_fingenring_摘",x+(width*this.scale_lv3_Zhai_offsetX),y+(height*this.scale_lv3_Zhai_offsetY),width*this.scale_lv3_Zhai_width,height*this.scale_lv3_Zhai_height);
					this.jzConstructLv4(x+(width*this.scale_lv3_lv4WithZhai_offsetX),y+(height*this.scale_lv3_lv4WithZhai_offsetY),width*this.scale_lv3_lv4WithZhai_width,height*this.scale_lv3_lv4WithZhai_height,part);
					return height;
					break;
				case "剔" :
					trace("剔");
					this.currentJzJp.createJzPart("剔","lh1_fingenring_剔",x+(width*this.scale_lv3_Ti_offsetX),y+(height*this.scale_lv3_Ti_offsetY),width*this.scale_lv3_Ti_width,height*this.scale_lv3_Ti_height);
					this.jzConstructLv4(x+(width*this.scale_lv3_lv4WithTi_offsetX),y+(height*this.scale_lv3_lv4WithTi_offsetY),width*this.scale_lv3_lv4WithTi_width,height*this.scale_lv3_lv4WithTi_height,part);
					return height;
					break;
				case "擘" :
					trace("擘");
					this.currentJzJp.createJzPart("擘","lh1_fingenring_擘",x+(width*this.scale_lv3_Bo_offsetX),y+(height*this.scale_lv3_Bo_offsetY),width*this.scale_lv3_Bo_width,height*this.scale_lv3_Bo_height);
					this.jzConstructLv4(x+(width*this.scale_lv3_lv4WithBo_offsetX),y+(height*this.scale_lv3_lv4WithBo_offsetY),width*this.scale_lv3_lv4WithBo_width,height*this.scale_lv3_lv4WithBo_height,part);
					return height;
					break;
				case "托" :
					trace("托");
					this.currentJzJp.createJzPart("托","lh1_fingenring_托",x+(width*this.scale_lv3_Tuo_offsetX),y+(height*this.scale_lv3_Tuo_offsetY),width*this.scale_lv3_Tuo_width,height*this.scale_lv3_Tuo_height);
					this.jzConstructLv4(x+(width*this.scale_lv3_lv4WithTuo_offsetX),y+(height*this.scale_lv3_lv4WithTuo_offsetY),width*this.scale_lv3_lv4WithTuo_width,height*this.scale_lv3_lv4WithTuo_height,part);
					return height;
					break;
				case "滾" :
					trace("滾");
					this.currentJzJp.createJzPart("滾","lh1_fingenring_滾",x+(width*this.scale_lv3_Gun_offsetX),y+(height*this.scale_lv3_Gun_offsetY),width*this.scale_lv3_Gun_width,height*this.scale_lv3_Gun_height);
					this.jzConstructLv4(x + (width * this.scale_lv3_lv4WithGun_offsetX), y + (height * this.scale_lv3_lv4WithGun_offsetY), width * this.scale_lv3_lv4WithGun_width, height * this.scale_lv3_lv4WithGun_height, part);
					if (this.rh_string2_str != "blank") {
						if (Math.abs(int(this.rh_string2_str)-int(this.rh_string1_str))>1) {
							//处理是否需要“至”的情况。如果两弦非相邻，那么就要有“至”。
							this.regRectsArray_array.push("至");
						}
                        //指法"滾"的截止弦。
                        this.regRectsArray_array.push(this.rh_string2_str);
                    }
					return height;
					break;
                case "撮" :
					this.jzConstructLv4(x+(width*this.scale_lv3_lv4WithNothing_offsetX),y+(height*this.scale_lv3_lv4WithNothing_offsetY),width*this.scale_lv3_lv4WithNothing_width,height*this.scale_lv3_lv4WithNothing_height,part);
					return height;
					break;
			}
			return height;
		}
		function jzConstructLv4(x:Number,y:Number,width:Number,height:Number,part:String):void {
			//写弦数。
			var rh_string:String;
			//指定是哪边的弦。“撮”这一类字左右两边各有一个对应弦的字。
			if (part == "left") {
				rh_string = this.rh_string1_str;
                                trace("wooooooooooooooooooo"+rh_string);
			} else {
				rh_string = this.rh_string2_str;
			}

			if (rh_string == "1") {
				trace("1"+this);
				this.currentJzJp.createJzPart("1","rh1_string_1",x+(width*this.scale_lv4_String1_offsetX),y+(height*this.scale_lv4_String1_offsetY),width*this.scale_lv4_String1_width,height*this.scale_lv4_String1_height);
				//把弦拼上来。因为第一弦对应的“一”很扁，所以其x、y、宽、高用一组单独的值。
			} else {
				this.currentJzJp.createJzPart(rh_string,"rh1_string_"+rh_string,x+(width*this.scale_lv4_String0_offsetX),y+(height*this.scale_lv4_String0_offsetY),width*this.scale_lv4_String0_width,height*this.scale_lv4_String0_height);
				//把弦拼上来。
			}



		}
		public function typeset():void {
			var lastPageJp:JzPaper;
			trace("排版一次！Scale为："+this.fmObj.jzScale_num);
			//每做好一个字，就要调用本方法排一下版。
			this.currentJzJp.scaleX = 0.2 * this.fmObj.jzScale_num;
			this.currentJzJp.scaleY = 0.2 * this.fmObj.jzScale_num;
			//缩放当前字。0.2是基础的缩放倍率（刚作出的字本来就很大，长宽都要变到0.2倍才是预想中的基准大小）。
			this.fmObj.jzWidth_num = currentJzJp.width;
			this.fmObj.jzHeight_num = currentJzJp.height;
			this.fmObj.readOne();
			//给排版对象输入数据，并且让它计算。
			if (this.currentPage_num < this.fmObj.currentPage_num) {
				//this.dispatchEvent({type:"finishedOne", target:this});
				//调度完成一个页面的事件。打印的时候会有用！
				//隐藏当前页。
				lastPageJp = this.currentPageJp;
				this.currentPageJp = this.currentPageJp.parent.createEmptyChild("page_" + String(this.currentPage_num + 1) + "_jp");
				this.currentPageJp.x += this.myRootObj.formatManager_fm.sideDistanceX_num;
				this.currentPageJp.y += this.myRootObj.formatManager_fm.sideDistanceY_num;
				this.currentPageJp.visible = false;
				trace("处理中页面是否可见在这里设置！创建一个新页面！");


				//this.currentJzJp = 
				trace("当前减字的父对象还是"+this.currentJzJp.parent.name+"，但马上要改变了！");
				this.currentJzJp=this.currentJzJp.moveMyselfTo(this.currentPageJp);
				trace("//完成当前字所属页面的转换。");
				this.currentPage_num++;

				if (this.currentPage_num==1) {
					//lastPageJp.removeJzPaper();
					//this.myRootObj.pg_cb.removeAll();
					this.myRootObj.page_cb.removeAll();
					//每次重新排版开始的时候顺便把换页的comboBox内部的第一个项目“请载入文件”去掉。
					this.myRootObj.page_cb.addEventListener(Event.CHANGE, this.myRootObj.listener_obj.page_cbChangeHandler);
					//加监听。移走监听是在主文档的closeDocument方法里。
                                        try{
						this.myRootObj.title_txt.htmlText="<FONT SIZE='30'>"+this.myRootObj.JZP_xml.head[0].info[0].title[0]+"</FONT>";
                                        }catch(error){
						this.myRootObj.title_txt.htmlText="<FONT SIZE='30'>未命名</FONT>";
                                                //如果读取标题出错，就用“未命名”代替。
                                        }
					this.myRootObj.title_txt.autoSize=TextFieldAutoSize.LEFT;
					this.myRootObj.title_txt.x=this.fmObj.pageWidth_num*0.5-this.myRootObj.title_txt.width*0.5;
					this.currentPageJp.addChild(this.myRootObj.title_txt);
					//把标题内容加上。[未完成][此段移动到对应的类中]
				}

				this.myRootObj.page_cb.addItem({label:"第"+this.currentPage_num+"页",data:this.currentPage_num});
				//给页码切换用的ComboBox进行设置。
				trace("这个位置！！！！");
				//this.myRootObj.pg_cb.addItem({label:"第"+String(this.currentPage_num)+"页",data:this.currentPage_num});
				if (this.myRootObj.configObject_co.mode_num==0) {
					lastPageJp.visible=false;
					//标准模式下就是隐藏旧页面。
				} else {
					JzPaper(lastPageJp).removeAllChildren();
					//节约内存模式下可以删除旧页面。[可能会出错！][未完成]
				}

				if (this.currentJzJp.parent==lastPageJp) {
					trace("不是在新页面上！");
				}

				trace("当前字的名称是"+this.currentJzJp.name);
				trace("当前减字的父对象是"+this.currentJzJp.parent.name);
				trace("上一页是"+lastPageJp.name);
				trace("currentJzJp是"+currentJzJp);

				trace("上一页是否可见"+lastPageJp.visible);
				trace("当前字是否可见"+this.currentJzJp.visible);
				// = true;
				//}
			}
			this.currentJzJp.x=this.fmObj.jzX_num;
			this.currentJzJp.y=this.fmObj.jzY_num;
			trace(this.currentJzJp.x+"标尺x"+this.fmObj.jzX_num);
			trace(this.currentJzJp.y+"标尺y"+this.fmObj.jzY_num);
			trace(this.currentJzJp.width+"宽度"+this.fmObj.jzWidth_num);
			trace(this.currentJzJp.height+"高度"+this.fmObj.jzHeight_num);
			//排版！
		}
		public function processAnElement(event:Event):void {
			//用于处理一个元素。[未完成]还要有对于文档数据的判断后才继续下一步！
			trace("处理元素！");

			/*trace("这个字x"+this.currentJzJp._x);
			trace("这个字y"+this.currentJzJp._y);
			trace("这个字width"+this.currentJzJp._width);
			trace("这个字height"+this.currentJzJp._height);*/
			//this.currentJzJp.createJzPart("测试","part_01",0,0,this.normalRect_width,this.normalRect_height);
			//下面，从xml元素中读取数据！
			if (this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].@type=="sound") {
				trace("这个减字对应发声动作。");
				try {
					this.lh_fingering1_str=this.myRootObj.dataConverter_dc.getFingering(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[0].@fingering);
				} catch (e:Error) {
					this.lh_fingering1_str="blank";
				}
				//左手第一指法赋值。
				///*
				try {
					this.lh_hui1_str=this.myRootObj.dataConverter_dc.getHui(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[0].@ed_huiwei);
					trace("左手第一徽"+this.myRootObj.dataConverter_dc.getHui(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[0].@ed_huiwei));
				} catch (e:Error) {
					this.lh_hui1_str="0";
				}
				//左手第一徽赋值。
				try {
					this.lh_fen1_str=this.myRootObj.dataConverter_dc.getFen(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[0].@ed_huiwei);
					trace("左手第一分"+this.lh_fen1_str);
				} catch (e:Error) {
					this.lh_fen1_str="0";
				}
				//左手第一分赋值。
				try {
					this.lh_subHui1_str=this.myRootObj.dataConverter_dc.getHui(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[0].action[0].@ed_huiwei);
					trace("左手辅助第一徽"+this.myRootObj.dataConverter_dc.getHui(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[0].action[0].@st_huiwei));
				} catch (e:Error) {
					this.lh_subHui1_str="blank";
				}
				//左手辅助第一徽赋值。“上七六”这一类指法中的“七”就关联此属性。
				try {
					this.lh_subFen1_str=this.myRootObj.dataConverter_dc.getFen(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[0].action[0].@ed_huiwei);
				} catch (e:Error) {
					this.lh_subFen1_str="blank";
				}
				//左手辅助第一分赋值。“上七六”这一类指法中的“六”就关联此属性。
				try {
					this.lh_subFingering1_str=this.myRootObj.dataConverter_dc.getFingering(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[0].action[0].@fingering);
				} catch (e:Error) {
					this.lh_subFingering1_str="blank";
				}
				//左手第一辅助指法赋值。
				try {
					this.lh_subSubFingering1_str=this.myRootObj.dataConverter_dc.getFingering(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[0].action[0].action[0].@fingering);
				} catch (e:Error) {
					this.lh_subSubFingering1_str="blank";
				}
				//左手第一子辅助指法赋值。例如“滸”就属于这类指法。
				try {
					this.lh_fingering2_str=this.myRootObj.dataConverter_dc.getFingering(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[1].@fingering);
				} catch (e:Error) {
					this.lh_fingering2_str="blank";
				}
				//左手第二指法赋值。
				try {
					this.lh_hui2_str=this.myRootObj.dataConverter_dc.getHui(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[1].@ed_huiwei);
				} catch (e:Error) {
					this.lh_hui2_str="blank";
				}
				//左手第二徽赋值。
				try {
					this.lh_fen2_str=this.myRootObj.dataConverter_dc.getFen(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[1].@ed_huiwei);
				} catch (e:Error) {
					this.lh_fen2_str="blank";
				}
				//左手第二分赋值。
				try {
					this.lh_subFingering2_str=this.myRootObj.dataConverter_dc.getFingering(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].l_hand[0].action[1].action[0].@fingering);
				} catch (e:Error) {
					this.lh_subFingering2_str="blank";
				}
				//左手第二辅助指法赋值。
				//
				try {
					this.rh_fingering_str=this.myRootObj.dataConverter_dc.getFingering(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].r_hand[0].action[0].@fingering);
				} catch (e:Error) {
					this.rh_fingering_str="blank";
				}
				//右手指法赋值。
				try {
					this.rh_string1_str=this.myRootObj.dataConverter_dc.getFingering(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].r_hand[0].action[0].@st_string);
				} catch (e:Error) {
					this.rh_string1_str="blank";
				}
				//右手第一弦赋值。
				try {
					this.rh_string2_str=this.myRootObj.dataConverter_dc.getFingering(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].r_hand[0].action[0].@ed_string);
				} catch (e:Error) {
					this.rh_string2_str="blank";
				}
				//右手第二弦赋值。
			}else if (this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].jz[this.eleCounter_num].@type=="ctrl") {
                //[未完成][上控制类减字]
			}
				this.jzConstructLv1(0,0,this.normalRect_width,this.normalRect_height);
                //先构成主减字。[未完成][定义默认字大小]
                if (this.regRectsArray_array.length != 0){
                //如果存在“规则矩形”相关元素，那么就处理它们。
                this.regRectsRulerY_num=0;
                //标尺回零。
	            this.currentJzJp = this.currentPageJp.createEmptyChild("jz_" + String(this.jzCounter_num) + "_jp");
			    //生成一个新空白字。
				this.myRootObj.jz_array.push(this.currentJzJp);
				//向减字数组放入减字。
                for (var i = 0 ;i <= (this.regRectsArray_array.length-1); i++){
                    //用循环处理数组中的每一个元素，构建减字。
                    if (this.regRectsArray_array[i] != "1"){
		                        	//判断“1”的特殊情况。不是的话，直接拼。
						this.currentJzJp.createJzPart(this.regRectsArray_array[i],"regRect"+this.regRectsArray_array[i],0,this.regRectsRulerY_num,(this.scale_regRects_singleRect_width*this.normalRect_width),(this.scale_regRects_singleRect_height*this.normalRect_height));
                                        	//上一个减字部件。
                                        	this.regRectsRulerY_num += (this.scale_regRects_singleRect_height*200);
                                        	this.regRectsRulerY_num += (this.scale_regRects_spacing*200);
                                        }else{
                                                if (i != 0){
                                                	this.regRectsRulerY_num += (this.scale_regRects_exUpperSpacing*200);
                                        		//因为“一”很扁，所以其上有额外的空白填充。“一”作为第一个regRect时候，这个会造成整体的“下沉”，所以判断一下。
                                                }
						this.currentJzJp.createJzPart(this.regRectsArray_array[i],"regRect"+this.regRectsArray_array[i],0,this.regRectsRulerY_num,(this.scale_regRects_singleRect1_width*this.normalRect_width),(this.scale_regRects_singleRect1_height*this.normalRect_height));
                                        	//上一个减字部件。因为“一”很扁，所以其宽、高用一组单独的值。
                                                if (i == this.regRectsArray_array.length-1){
                                        		//如果“一”垫底，那么要画一个透明的东西给它垫上，防止“一”变成“下划线”。                                                        
                                                        //this.currentJzJp.graphics.beginFill(0x555555,0.5);
                                                        this.currentJzJp.graphics.drawRect(0,(this.regRectsRulerY_num+(this.scale_regRects_singleRect1_height*this.normalRect_height)),this.scale_regRects_singleRect_width*230,(this.scale_regRects_exLowerSpacing*this.normalRect_height));
                                                }
                                                this.regRectsRulerY_num += (this.scale_regRects_exLowerSpacing*this.normalRect_height);
                                        	//因为“一”很扁，所以其下有额外的空白填充。
                                        	this.regRectsRulerY_num += (this.scale_regRects_spacing*this.normalRect_height);
                                        
                                        }
                                }
                                this.regRectsArray_array.splice(0);
                                //清空数组。
 			        this.typeset();
			        //排一下版。
			        this.jzCounter_num++;
			        this.myRootObj.formatManager_fm.space(2);
                        };
			this.myRootObj.formatManager_fm.space(2);
			//this.currentJzJp.attachMovie("JzFont_宋体_12312", "part_02", this.currentJzJp.getNextHighestDepth());
			/*trace("这个字x"+this.currentJzJp._x);
			trace("这个字y"+this.currentJzJp._y);
			trace("这个字width"+this.currentJzJp._width);
			trace("这个字height"+this.currentJzJp._height);*/
			//this.currentJzJp._yscale = 20;
			//

			trace("当前元素标号（从0开始）："+this.eleCounter_num);
			trace("元素总数："+this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].elements().length());
			trace("=====标号为"+this.eleCounter_num+"（从0开始）的元素处理完毕！=====");
			this.myRootObj.processing_pb.setProgress(this.eleCounter_num+1, this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].elements().length());
			//更新一下进度条。
			if (this.eleCounter_num==(this.myRootObj.JZP_xml.tracks[0].group[0].jz_track[0].elements().length()-1)) {
				trace("处理完了最后一个元素！");
				//处理完了最后一个元素，可以停止了！调度完成一个页面的事件。也调度所有页面的事件！
				//this.dispatchEvent({type:"finishedOne", target:this});
				//this.dispatchEvent({type:"finishedAll", target:this});
				//调度完毕了！下面切换显示到第一页！[未完成]   
				switch (this.myRootObj.configObject_co.mode_num) {
					case 0 :
						trace("切换显示到第一页！");
						this.currentPageJp.visible=false;
						//让当前页面不可见。
						Sprite(this.myRootObj.mainPaper_jp.getChildByName("page_1_jp")).visible=true;
						//让用户选择的目标页面可见。
						this.myRootObj.currentPg_num=1;
						//设置好当前页面的计数。
						this.myRootObj.pageNumber_txt.text="第"+String(this.myRootObj.currentPg_num)+"页";
						this.myRootObj.mainPaper_jp.addChild(this.myRootObj.pageNumber_txt);
						this.myRootObj.viewPageNumber(this.fmObj.pgNumPosition_uint);
						break;
					case 1 :
						//1模式下的代码。（预排版后，用户切换页码，程序生成相应页面。）[未完成]
						break;
				}
				this.myRootObj.processing_pb.visible=false;
				//处理完毕，隐藏进度条。
				this.myRootObj.GUIUnlocker();
				//文档处理完毕后，界面解锁。P.S.加锁是在SuperKitListener类启动Timer的代码部分里。
			}

			this.jzCounter_num++;
			this.eleCounter_num++;
		}
		public function initialize(myRootObj:Object,currentPageJp:Sprite,fmObj:Object,dataXMLList:XMLList):void {
			//初始化。用于在新一次排版之前重置本对象。
			this.myRootObj=myRootObj;
			this.currentPageJp=currentPageJp;
			this.fmObj=fmObj;
			this.dataXMLList=dataXMLList;
			//
			this.eleCounter_num=0;
			this.jzCounter_num=0;
			this.currentPage_num=0;
			this.currentJzJp=null;
			//
			//下面读入字体架构信息。
			this.normalRect_width = this.myRootObj.currentJzFontInfo_jfi.normalRect_width_num;
			this.normalRect_height = this.myRootObj.currentJzFontInfo_jfi.normalRect_height_num;
                        //
			this.scale_lv1_lv2WithNothing_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_lv2WithNothing_offsetX_num;
			this.scale_lv1_lv2WithNothing_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_lv2WithNothing_offsetY_num;
			this.scale_lv1_lv2WithNothing_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_lv2WithNothing_width_num;
			this.scale_lv1_lv2WithNothing_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_lv2WithNothing_height_num;

                        this.scale_lv1_lv2LWithCuo_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_lv2LWithCuo_offsetX_num;
			this.scale_lv1_lv2LWithCuo_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_lv2LWithCuo_offsetY_num;
			this.scale_lv1_lv2LWithCuo_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_lv2LWithCuo_width_num;
			this.scale_lv1_lv2LWithCuo_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_lv2LWithCuo_height_num;

                        this.scale_lv1_lv2RWithCuo_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_lv2RWithCuo_offsetX_num;
			this.scale_lv1_lv2RWithCuo_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_lv2RWithCuo_offsetY_num;
			this.scale_lv1_lv2RWithCuo_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_lv2RWithCuo_width_num;
			this.scale_lv1_lv2RWithCuo_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_lv2RWithCuo_height_num;

			//“撮”
			this.scale_lv1_Cuo_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_Cuo_offsetX_num;
			this.scale_lv1_Cuo_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_Cuo_offsetY_num;
			this.scale_lv1_Cuo_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_Cuo_width_num;
			this.scale_lv1_Cuo_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv1_Cuo_height_num;
                        //以上是lv1的相关信息。

			this.scale_lv2_lhFingeringWithoutHuifen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFingeringWithoutHuifen_offsetX_num;
			this.scale_lv2_lhFingeringWithoutHuifen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFingeringWithoutHuifen_offsetY_num;
			this.scale_lv2_lhFingeringWithoutHuifen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFingeringWithoutHuifen_width_num;
			this.scale_lv2_lhFingeringWithoutHuifen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFingeringWithoutHuifen_height_num;

			this.scale_lv2_lhFingeringWithHuiWithoutFen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFingeringWithHuiWithoutFen_offsetX_num;
			this.scale_lv2_lhFingeringWithHuiWithoutFen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFingeringWithHuiWithoutFen_offsetY_num;
			this.scale_lv2_lhFingeringWithHuiWithoutFen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFingeringWithHuiWithoutFen_width_num;
			this.scale_lv2_lhFingeringWithHuiWithoutFen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFingeringWithHuiWithoutFen_height_num;

			this.scale_lv2_lhFingeringWithHuifen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFingeringWithHuifen_offsetX_num;
			this.scale_lv2_lhFingeringWithHuifen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFingeringWithHuifen_offsetY_num;
			this.scale_lv2_lhFingeringWithHuifen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFingeringWithHuifen_width_num;
			this.scale_lv2_lhFingeringWithHuifen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFingeringWithHuifen_height_num;

			this.scale_lv2_lhHuiWithoutFen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHuiWithoutFen_offsetX_num;
			this.scale_lv2_lhHuiWithoutFen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHuiWithoutFen_offsetY_num;
			this.scale_lv2_lhHuiWithoutFen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHuiWithoutFen_width_num;
			this.scale_lv2_lhHuiWithoutFen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHuiWithoutFen_height_num;

			this.scale_lv2_lhHui1WithoutFen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHui1WithoutFen_offsetX_num;
			this.scale_lv2_lhHui1WithoutFen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHui1WithoutFen_offsetY_num;
			this.scale_lv2_lhHui1WithoutFen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHui1WithoutFen_width_num;
			this.scale_lv2_lhHui1WithoutFen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHui1WithoutFen_height_num;

			this.scale_lv2_lhHuiWithFen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHuiWithFen_offsetX_num;
			this.scale_lv2_lhHuiWithFen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHuiWithFen_offsetY_num;
			this.scale_lv2_lhHuiWithFen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHuiWithFen_width_num;
			this.scale_lv2_lhHuiWithFen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHuiWithFen_height_num;

			this.scale_lv2_lhHui1WithFen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHui1WithFen_offsetX_num;
			this.scale_lv2_lhHui1WithFen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHui1WithFen_offsetY_num;
			this.scale_lv2_lhHui1WithFen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHui1WithFen_width_num;
			this.scale_lv2_lhHui1WithFen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhHui1WithFen_height_num;

			this.scale_lv2_lhFen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFen_offsetX_num;
			this.scale_lv2_lhFen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFen_offsetY_num;
			this.scale_lv2_lhFen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFen_width_num;
			this.scale_lv2_lhFen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFen_height_num;

			this.scale_lv2_lhFen1_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFen1_offsetX_num;
			this.scale_lv2_lhFen1_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFen1_offsetY_num;
			this.scale_lv2_lhFen1_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFen1_width_num;
			this.scale_lv2_lhFen1_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lhFen1_height_num;

			this.scale_lv2_ChuoWithHuiWithoutFen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ChuoWithHuiWithoutFen_offsetX_num;
			this.scale_lv2_ChuoWithHuiWithoutFen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ChuoWithHuiWithoutFen_offsetY_num;
			this.scale_lv2_ChuoWithHuiWithoutFen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ChuoWithHuiWithoutFen_width_num;
			this.scale_lv2_ChuoWithHuiWithoutFen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ChuoWithHuiWithoutFen_height_num;

			this.scale_lv2_ChuoWithHuifen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ChuoWithHuifen_offsetX_num;
			this.scale_lv2_ChuoWithHuifen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ChuoWithHuifen_offsetY_num;
			this.scale_lv2_ChuoWithHuifen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ChuoWithHuifen_width_num;
			this.scale_lv2_ChuoWithHuifen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ChuoWithHuifen_height_num;

			this.scale_lv2_ZhuWithHuiWithoutFen1_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuiWithoutFen1_offsetX_num;
			this.scale_lv2_ZhuWithHuiWithoutFen1_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuiWithoutFen1_offsetY_num;
			this.scale_lv2_ZhuWithHuiWithoutFen1_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuiWithoutFen1_width_num;
			this.scale_lv2_ZhuWithHuiWithoutFen1_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuiWithoutFen1_height_num;

			this.scale_lv2_ZhuWithHuiWithoutFen2_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuiWithoutFen2_offsetX_num;
			this.scale_lv2_ZhuWithHuiWithoutFen2_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuiWithoutFen2_offsetY_num;
			this.scale_lv2_ZhuWithHuiWithoutFen2_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuiWithoutFen2_width_num;
			this.scale_lv2_ZhuWithHuiWithoutFen2_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuiWithoutFen2_height_num;

			this.scale_lv2_ZhuWithHuiWithoutFen3_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuiWithoutFen3_offsetX_num;
			this.scale_lv2_ZhuWithHuiWithoutFen3_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuiWithoutFen3_offsetY_num;
			this.scale_lv2_ZhuWithHuiWithoutFen3_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuiWithoutFen3_width_num;
			this.scale_lv2_ZhuWithHuiWithoutFen3_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuiWithoutFen3_height_num;

			this.scale_lv2_ZhuWithHuifen1_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuifen1_offsetX_num;
			this.scale_lv2_ZhuWithHuifen1_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuifen1_offsetY_num;
			this.scale_lv2_ZhuWithHuifen1_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuifen1_width_num;
			this.scale_lv2_ZhuWithHuifen1_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuifen1_height_num;

			this.scale_lv2_ZhuWithHuifen2_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuifen2_offsetX_num;
			this.scale_lv2_ZhuWithHuifen2_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuifen2_offsetY_num;
			this.scale_lv2_ZhuWithHuifen2_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuifen2_width_num;
			this.scale_lv2_ZhuWithHuifen2_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuifen2_height_num;

			this.scale_lv2_ZhuWithHuifen3_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuifen3_offsetX_num;
			this.scale_lv2_ZhuWithHuifen3_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuifen3_offsetY_num;
			this.scale_lv2_ZhuWithHuifen3_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuifen3_width_num;
			this.scale_lv2_ZhuWithHuifen3_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuWithHuifen3_height_num;


			this.scale_lv2_DaiqiWithHuiWithoutFen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_DaiqiWithHuiWithoutFen_offsetX_num;
			this.scale_lv2_DaiqiWithHuiWithoutFen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_DaiqiWithHuiWithoutFen_offsetY_num;
			this.scale_lv2_DaiqiWithHuiWithoutFen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_DaiqiWithHuiWithoutFen_width_num;
			this.scale_lv2_DaiqiWithHuiWithoutFen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_DaiqiWithHuiWithoutFen_height_num;

			this.scale_lv2_TaoqiWithHuiWithoutFen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_TaoqiWithHuiWithoutFen_offsetX_num;
			this.scale_lv2_TaoqiWithHuiWithoutFen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_TaoqiWithHuiWithoutFen_offsetY_num;
			this.scale_lv2_TaoqiWithHuiWithoutFen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_TaoqiWithHuiWithoutFen_width_num;
			this.scale_lv2_TaoqiWithHuiWithoutFen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_TaoqiWithHuiWithoutFen_height_num;

			this.scale_lv2_ZhuaqiWithHuiWithoutFen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuaqiWithHuiWithoutFen_offsetX_num;
			this.scale_lv2_ZhuaqiWithHuiWithoutFen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuaqiWithHuiWithoutFen_offsetY_num;
			this.scale_lv2_ZhuaqiWithHuiWithoutFen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuaqiWithHuiWithoutFen_width_num;
			this.scale_lv2_ZhuaqiWithHuiWithoutFen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuaqiWithHuiWithoutFen_height_num;

			this.scale_lv2_DaiqiWithHuifen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_DaiqiWithHuifen_offsetX_num;
			this.scale_lv2_DaiqiWithHuifen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_DaiqiWithHuifen_offsetY_num;
			this.scale_lv2_DaiqiWithHuifen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_DaiqiWithHuifen_width_num;
			this.scale_lv2_DaiqiWithHuifen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_DaiqiWithHuifen_height_num;

			this.scale_lv2_TaoqiWithHuifen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_TaoqiWithHuifen_offsetX_num;
			this.scale_lv2_TaoqiWithHuifen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_TaoqiWithHuifen_offsetY_num;
			this.scale_lv2_TaoqiWithHuifen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_TaoqiWithHuifen_width_num;
			this.scale_lv2_TaoqiWithHuifen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_TaoqiWithHuifen_height_num;

			this.scale_lv2_ZhuaqiWithHuifen_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuaqiWithHuifen_offsetX_num;
			this.scale_lv2_ZhuaqiWithHuifen_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuaqiWithHuifen_offsetY_num;
			this.scale_lv2_ZhuaqiWithHuifen_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuaqiWithHuifen_width_num;
			this.scale_lv2_ZhuaqiWithHuifen_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_ZhuaqiWithHuifen_height_num;


			this.scale_lv2_lv3WithLhFSan_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithLhFSan_offsetX_num;
			this.scale_lv2_lv3WithLhFSan_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithLhFSan_offsetY_num;
			this.scale_lv2_lv3WithLhFSan_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithLhFSan_width_num;
			this.scale_lv2_lv3WithLhFSan_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithLhFSan_height_num;

			this.scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_offsetX_num;
			this.scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_offsetY_num;
			this.scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_width_num;
			this.scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuiWithoutFenWithoutChuozhu_height_num;

			this.scale_lv2_lv3WithHuiWithoutFenWithChuo_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuiWithoutFenWithChuo_offsetX_num;
			this.scale_lv2_lv3WithHuiWithoutFenWithChuo_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuiWithoutFenWithChuo_offsetY_num;
			this.scale_lv2_lv3WithHuiWithoutFenWithChuo_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuiWithoutFenWithChuo_width_num;
			this.scale_lv2_lv3WithHuiWithoutFenWithChuo_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuiWithoutFenWithChuo_height_num;

			this.scale_lv2_lv3WithHuiWithoutFenWithZhu_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuiWithoutFenWithZhu_offsetX_num;
			this.scale_lv2_lv3WithHuiWithoutFenWithZhu_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuiWithoutFenWithZhu_offsetY_num;
			this.scale_lv2_lv3WithHuiWithoutFenWithZhu_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuiWithoutFenWithZhu_width_num;
			this.scale_lv2_lv3WithHuiWithoutFenWithZhu_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuiWithoutFenWithZhu_height_num;

			this.scale_lv2_lv3WithHuifenWithoutChuozhu_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuifenWithoutChuozhu_offsetX_num;
			this.scale_lv2_lv3WithHuifenWithoutChuozhu_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuifenWithoutChuozhu_offsetY_num;
			this.scale_lv2_lv3WithHuifenWithoutChuozhu_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuifenWithoutChuozhu_width_num;
			this.scale_lv2_lv3WithHuifenWithoutChuozhu_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuifenWithoutChuozhu_height_num;

			this.scale_lv2_lv3WithHuifenWithChuo_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuifenWithChuo_offsetX_num;
			this.scale_lv2_lv3WithHuifenWithChuo_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuifenWithChuo_offsetY_num;
			this.scale_lv2_lv3WithHuifenWithChuo_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuifenWithChuo_width_num;
			this.scale_lv2_lv3WithHuifenWithChuo_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuifenWithChuo_height_num;

			this.scale_lv2_lv3WithHuifenWithZhu_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuifenWithZhu_offsetX_num;
			this.scale_lv2_lv3WithHuifenWithZhu_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuifenWithZhu_offsetY_num;
			this.scale_lv2_lv3WithHuifenWithZhu_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuifenWithZhu_width_num;
			this.scale_lv2_lv3WithHuifenWithZhu_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv2_lv3WithHuifenWithZhu_height_num;
			//“挑”
			this.scale_lv3_Tiao_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Tiao_offsetX_num;
			this.scale_lv3_Tiao_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Tiao_offsetY_num;
			this.scale_lv3_Tiao_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Tiao_width_num;
			this.scale_lv3_Tiao_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Tiao_height_num;

			this.scale_lv3_lv4WithTiao_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithTiao_offsetX_num;
			this.scale_lv3_lv4WithTiao_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithTiao_offsetY_num;
			this.scale_lv3_lv4WithTiao_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithTiao_width_num;
			this.scale_lv3_lv4WithTiao_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithTiao_height_num;
			//“勾”
			this.scale_lv3_Gou_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Gou_offsetX_num;
			this.scale_lv3_Gou_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Gou_offsetY_num;
			this.scale_lv3_Gou_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Gou_width_num;
			this.scale_lv3_Gou_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Gou_height_num;

			this.scale_lv3_lv4WithGou_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithGou_offsetX_num;
			this.scale_lv3_lv4WithGou_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithGou_offsetY_num;
			this.scale_lv3_lv4WithGou_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithGou_width_num;
			this.scale_lv3_lv4WithGou_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithGou_height_num;
			//“打”
			this.scale_lv3_Da_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Da_offsetX_num;
			this.scale_lv3_Da_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Da_offsetY_num;
			this.scale_lv3_Da_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Da_width_num;
			this.scale_lv3_Da_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Da_height_num;

			this.scale_lv3_lv4WithDa_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithDa_offsetX_num;
			this.scale_lv3_lv4WithDa_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithDa_offsetY_num;
			this.scale_lv3_lv4WithDa_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithDa_width_num;
			this.scale_lv3_lv4WithDa_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithDa_height_num;

			//“抹”
			this.scale_lv3_Mo_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Mo_offsetX_num;
			this.scale_lv3_Mo_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Mo_offsetY_num;
			this.scale_lv3_Mo_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Mo_width_num;
			this.scale_lv3_Mo_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Mo_height_num;

			this.scale_lv3_lv4WithMo_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithMo_offsetX_num;
			this.scale_lv3_lv4WithMo_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithMo_offsetY_num;
			this.scale_lv3_lv4WithMo_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithMo_width_num;
			this.scale_lv3_lv4WithMo_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithMo_height_num;

            //“摘”
			this.scale_lv3_Zhai_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Zhai_offsetX_num;
			this.scale_lv3_Zhai_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Zhai_offsetY_num;
			this.scale_lv3_Zhai_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Zhai_width_num;
			this.scale_lv3_Zhai_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Zhai_height_num;

			this.scale_lv3_lv4WithZhai_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithZhai_offsetX_num;
			this.scale_lv3_lv4WithZhai_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithZhai_offsetY_num;
			this.scale_lv3_lv4WithZhai_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithZhai_width_num;
			this.scale_lv3_lv4WithZhai_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithZhai_height_num;

            //“剔”
			this.scale_lv3_Ti_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Ti_offsetX_num;
			this.scale_lv3_Ti_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Ti_offsetY_num;
			this.scale_lv3_Ti_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Ti_width_num;
			this.scale_lv3_Ti_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Ti_height_num;

			this.scale_lv3_lv4WithTi_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithTi_offsetX_num;
			this.scale_lv3_lv4WithTi_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithTi_offsetY_num;
			this.scale_lv3_lv4WithTi_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithTi_width_num;
			this.scale_lv3_lv4WithTi_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithTi_height_num;

			//“擘”
			this.scale_lv3_Bo_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Bo_offsetX_num;
			this.scale_lv3_Bo_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Bo_offsetY_num;
			this.scale_lv3_Bo_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Bo_width_num;
			this.scale_lv3_Bo_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Bo_height_num;

			this.scale_lv3_lv4WithBo_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithBo_offsetX_num;
			this.scale_lv3_lv4WithBo_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithBo_offsetY_num;
			this.scale_lv3_lv4WithBo_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithBo_width_num;
			this.scale_lv3_lv4WithBo_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithBo_height_num;

			//“托”
			this.scale_lv3_Tuo_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Tuo_offsetX_num;
			this.scale_lv3_Tuo_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Tuo_offsetY_num;
			this.scale_lv3_Tuo_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Tuo_width_num;
			this.scale_lv3_Tuo_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Tuo_height_num;

			this.scale_lv3_lv4WithTuo_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithTuo_offsetX_num;
			this.scale_lv3_lv4WithTuo_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithTuo_offsetY_num;
			this.scale_lv3_lv4WithTuo_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithTuo_width_num;
			this.scale_lv3_lv4WithTuo_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithTuo_height_num;

			//“滾”
			this.scale_lv3_Gun_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Gun_offsetX_num;
			this.scale_lv3_Gun_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Gun_offsetY_num;
			this.scale_lv3_Gun_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Gun_width_num;
			this.scale_lv3_Gun_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_Gun_height_num;

			this.scale_lv3_lv4WithGun_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithGun_offsetX_num;
			this.scale_lv3_lv4WithGun_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithGun_offsetY_num;
			this.scale_lv3_lv4WithGun_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithGun_width_num;
			this.scale_lv3_lv4WithGun_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithGun_height_num;
			//
			//
			this.scale_lv3_lv4WithNothing_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithNothing_offsetX_num;
			this.scale_lv3_lv4WithNothing_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithNothing_offsetY_num;
			this.scale_lv3_lv4WithNothing_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithNothing_width_num;
			this.scale_lv3_lv4WithNothing_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv3_lv4WithNothing_height_num;

			//以上是lv3的内容。

			this.scale_lv4_String0_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv4_String0_offsetX_num;
			this.scale_lv4_String0_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv4_String0_offsetY_num;
			this.scale_lv4_String0_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv4_String0_width_num;
			this.scale_lv4_String0_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv4_String0_height_num;

			this.scale_lv4_String1_offsetX=this.myRootObj.currentJzFontInfo_jfi.scale_lv4_String1_offsetX_num;
			this.scale_lv4_String1_offsetY=this.myRootObj.currentJzFontInfo_jfi.scale_lv4_String1_offsetY_num;
			this.scale_lv4_String1_width=this.myRootObj.currentJzFontInfo_jfi.scale_lv4_String1_width_num;
			this.scale_lv4_String1_height=this.myRootObj.currentJzFontInfo_jfi.scale_lv4_String1_height_num;
                        //以上是lv4的内容。
			this.scale_regRects_singleRect_width=this.myRootObj.currentJzFontInfo_jfi.scale_regRects_singleRect_width_num;
			this.scale_regRects_singleRect_height=this.myRootObj.currentJzFontInfo_jfi.scale_regRects_singleRect_height_num;
			this.scale_regRects_spacing=this.myRootObj.currentJzFontInfo_jfi.scale_regRects_spacing_num;
			this.scale_regRects_singleRect1_width=this.myRootObj.currentJzFontInfo_jfi.scale_regRects_singleRect1_width_num;
			this.scale_regRects_singleRect1_height=this.myRootObj.currentJzFontInfo_jfi.scale_regRects_singleRect1_height_num;
			this.scale_regRects_exUpperSpacing=this.myRootObj.currentJzFontInfo_jfi.scale_regRects_exUpperSpacing_num;
			this.scale_regRects_exLowerSpacing=this.myRootObj.currentJzFontInfo_jfi.scale_regRects_exLowerSpacing_num;
		        //以上是“规则矩形”的内容。“规则矩形”指的是“上九”、“上七六”这一类减字。
			trace("初始化了Operator。");
		}
	}
}