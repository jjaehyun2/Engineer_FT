package framework.components.rhythmList
{
	import flash.display.DisplayObject;
	
	import framework.model.AppModelLocator;
	import services.vo.GlobalSettings;
	import services.vo.common.DataListVO;
	
	import h2olib.utils.DateUtils;
	
	import mx.collections.ArrayCollection;
	import mx.containers.HBox;
	import mx.containers.VBox;
	import mx.controls.CheckBox;
	import mx.controls.DateField;
	import mx.controls.RadioButton;
	import mx.controls.Spacer;
	import mx.core.Container;

	public class RhythmList extends VBox
	{

		private var displayObjectList:ArrayCollection = new ArrayCollection();

		public function RhythmList()
		{
			super();
			//verticalScrollPolicy = "on";
			horizontalScrollPolicy = "off";
		}

		private var _dataProvider:ArrayCollection;

		[Bindable]
		private var model:AppModelLocator = AppModelLocator.getInstance();

		[Bindable]
		public function get dataProvider():ArrayCollection
		{
			return _dataProvider;
		}

		public function set dataProvider(value:ArrayCollection):void
		{

				_dataProvider = value;
				this.removeAllChildren();
				var firstItem:Boolean = true;

				for each(var item:DataListVO in value)
				{
					var itemRadioButton:RadioButton = new RadioButton();
					itemRadioButton.name = item.sCode;
					itemRadioButton.id = item.sCode;
					itemRadioButton.label = item.sName
					itemRadioButton.groupName = "rhythmList";
					this.addChild(itemRadioButton);
					if(firstItem && selectedRhythmCode == "")
					{
						itemRadioButton.selected = true;
						firstItem = false;
					}
					else if(item.sCode == selectedRhythmCode)
					{
						itemRadioButton.selected = true;
					}

					if(item.sCode == "RHYTHM_WEEKDAYS") //RHYTHM_CUSTOMIZED
					{
						//Monday
						var mondayConteiner:HBox = new HBox();
						mondayConteiner.percentWidth = 100;
						mondayConteiner.name = "Monday";

						var mondaySpacer:Spacer = new Spacer();
						mondaySpacer.width = 30;
						mondayConteiner.addChild(mondaySpacer);

						var monday:CheckBox = new CheckBox();
						monday.name = "Monday";
						monday.label = "Monday";
						if(selectedRhythm != "" && selectedRhythmCode == "RHYTHM_WEEKDAYS")
						{
							try {
								monday.selected = rhythmNameToArray(selectedRhythm)[0] == "1";
							} catch(e:Error){}
						}
						mondayConteiner.addChild(monday);

						this.addChild(mondayConteiner);

						//Tuesday
						var tuesdayConteiner:HBox = new HBox();
						tuesdayConteiner.percentWidth = 100;
						tuesdayConteiner.name = "Tuesday";

						var tuesdaySpacer:Spacer = new Spacer();
						tuesdaySpacer.width = 30;
						tuesdayConteiner.addChild(tuesdaySpacer);

						var tuesday:CheckBox = new CheckBox();
						tuesday.name = "Tuesday";
						tuesday.label = "Tuesday";
						if(selectedRhythm != "" && selectedRhythmCode == "RHYTHM_WEEKDAYS")
						{
							try {
								tuesday.selected = rhythmNameToArray(selectedRhythm)[1] == "1";
							} catch(e:Error){}
						}
						tuesdayConteiner.addChild(tuesday);

						this.addChild(tuesdayConteiner);

						//Wednesday
						var wednesdayConteiner:HBox = new HBox();
						wednesdayConteiner.percentWidth = 100;
						wednesdayConteiner.name = "Wednesday";

						var wednesdaySpacer:Spacer = new Spacer();
						wednesdaySpacer.width = 30;
						wednesdayConteiner.addChild(wednesdaySpacer);

						var wednesday:CheckBox = new CheckBox();
						wednesday.name = "Wednesday";
						wednesday.label = "Wednesday";
						if(selectedRhythm != "" && selectedRhythmCode == "RHYTHM_WEEKDAYS")
						{
							try {
								wednesday.selected = rhythmNameToArray(selectedRhythm)[2] == "1";
							} catch(e:Error){}
						}
						wednesdayConteiner.addChild(wednesday);

						this.addChild(wednesdayConteiner);

						//Thursday
						var thursdayConteiner:HBox = new HBox();
						thursdayConteiner.percentWidth = 100;
						thursdayConteiner.name = "Thursday";

						var thursdaySpacer:Spacer = new Spacer();
						thursdaySpacer.width = 30;
						thursdayConteiner.addChild(thursdaySpacer);

						var thursday:CheckBox = new CheckBox();
						thursday.name = "Thursday";
						thursday.label = "Thursday";
						if(selectedRhythm != "" && selectedRhythmCode == "RHYTHM_WEEKDAYS")
						{
							try {
								thursday.selected = rhythmNameToArray(selectedRhythm)[3] == "1";
							} catch(e:Error){}
						}
						thursdayConteiner.addChild(thursday);

						this.addChild(thursdayConteiner);

						//Friday
						var fridayConteiner:HBox = new HBox();
						fridayConteiner.percentWidth = 100;
						fridayConteiner.name = "Friday";

						var fridaySpacer:Spacer = new Spacer();
						fridaySpacer.width = 30;
						fridayConteiner.addChild(fridaySpacer);

						var friday:CheckBox = new CheckBox();
						friday.name = "Friday";
						friday.label = "Friday";
						if(selectedRhythm != "" && selectedRhythmCode == "RHYTHM_WEEKDAYS")
						{
							try {
								friday.selected = rhythmNameToArray(selectedRhythm)[4] == "1";
							} catch(e:Error){}
						}
						fridayConteiner.addChild(friday);

						this.addChild(fridayConteiner);

						//Saturday
						var saturdayConteiner:HBox = new HBox();
						saturdayConteiner.percentWidth = 100;
						saturdayConteiner.name = "Saturday";

						var saturdaySpacer:Spacer = new Spacer();
						saturdaySpacer.width = 30;
						saturdayConteiner.addChild(saturdaySpacer);

						var saturday:CheckBox = new CheckBox();
						saturday.name = "Saturday";
						saturday.label = "Saturday";
						if(selectedRhythm != "" && selectedRhythmCode == "RHYTHM_WEEKDAYS")
						{
							try {
								saturday.selected = rhythmNameToArray(selectedRhythm)[5] == "1";
							} catch(e:Error){}
						}
						saturdayConteiner.addChild(saturday);

						this.addChild(saturdayConteiner);

						//Sunday
						var sundayConteiner:HBox = new HBox();
						sundayConteiner.percentWidth = 100;
						sundayConteiner.name = "Sunday";

						var sundaySpacer:Spacer = new Spacer();
						sundaySpacer.width = 30;
						sundayConteiner.addChild(sundaySpacer);

						var sunday:CheckBox = new CheckBox();
						sunday.name = "Sunday";
						sunday.label = "Sunday";
						if(selectedRhythm != "" && selectedRhythmCode == "RHYTHM_WEEKDAYS")
						{
							try {
								sunday.selected = rhythmNameToArray(selectedRhythm)[6] == "1";
							} catch(e:Error){}
						}
						sundayConteiner.addChild(sunday);

						this.addChild(sundayConteiner);

					}
					if(item.sCode == "RHYTHM_CUSTOMIZED")
					{
						var dDiff:int = model.ratesModule.barModule.currentPackage.iMaxStay;// UtilsDate.dateDiff("d",DateField.stringToDate(model.barModule.currentPackage.sDateEnd,GlobalSettings.DATE_SERVER_FORMAT),DateField.stringToDate(model.barModule.currentPackage.sDateStart,GlobalSettings.DATE_SERVER_FORMAT));
						for (var i:int = 1; i < dDiff+1; i++)
						{
							var dayConteiner:HBox = new HBox();
							dayConteiner.percentWidth = 100;
							dayConteiner.name = "packageDay" + i;

							var daySpacer:Spacer = new Spacer();
							daySpacer.width = 30;
							dayConteiner.addChild(daySpacer);

							var day:CheckBox = new CheckBox();
							day.label = i.toString();
							day.name = "packageDay" + i;
							day.id = "packageDay" + i;
							if(selectedRhythm != "" && selectedRhythmCode == "RHYTHM_CUSTOMIZED")
							{
								try {
									day.selected = rhythmNameToArray(selectedRhythm)[i-1] == "1";
								} catch(e:Error){}
							}
							dayConteiner.addChild(day);

							this.addChild(dayConteiner);
						}
					}
				}

				if(onDataProviderCallBack != null)
				{
					onDataProviderCallBack();
					//onDataProviderCallBack = null;
				}

		}

		private var _rhythm:DataListVO;
		private var onDataProviderCallBack:Function;

		public var selectedRhythm:String = "";
		public var selectedRhythmCode:String = "";

		private function setRhythm():void
		{
			rhythm = _rhythm;
		}

		public function set rhythm(value:DataListVO):void
		{
			_rhythm = value;
			var o:DisplayObject = this.getChildByName(value.sCode);
			if(dataProvider.length != 0)
			{
				if(this.getChildByName(value.sCode) != null)
				{
					(this.getChildByName(value.sCode) as RadioButton).selected = true;
					if(value.sCode == "RHYTHM_WEEKDAYS")
					{
						((this.getChildByName("Monday") as Container).getChildByName("Monday") as CheckBox).selected  = rhythmNameToArray(value.sName)[0] == "1";
						((this.getChildByName("Tuesday") as Container).getChildByName("Tuesday") as CheckBox).selected  = rhythmNameToArray(value.sName)[1] == "1";
						((this.getChildByName("Wednesday") as Container).getChildByName("Wednesday") as CheckBox).selected  = rhythmNameToArray(value.sName)[2] == "1";
						((this.getChildByName("Thursday") as Container).getChildByName("Thursday") as CheckBox).selected  = rhythmNameToArray(value.sName)[3] == "1";
						((this.getChildByName("Friday") as Container).getChildByName("Friday") as CheckBox).selected  = rhythmNameToArray(value.sName)[4] == "1";
						((this.getChildByName("Saturday") as Container).getChildByName("Saturday") as CheckBox).selected  = rhythmNameToArray(value.sName)[5] == "1";
						((this.getChildByName("Sunday") as Container).getChildByName("Sunday") as CheckBox).selected  = rhythmNameToArray(value.sName)[6] == "1";
					}
					else if(value.sCode == "RHYTHM_CUSTOMIZED")
					{
						try {
							var dDiff:int = DateUtils.dateDiff(DateUtils.DAY_OF_MONTH,DateField.stringToDate(model.ratesModule.barModule.currentPackage.sDateStart,GlobalSettings.DATE_SERVER_FORMAT),DateField.stringToDate(model.ratesModule.barModule.currentPackage.sDateEnd,GlobalSettings.DATE_SERVER_FORMAT));

							for (var i:int=1; i<dDiff+1;i++)
							{
								((this.getChildByName("packageDay" + i) as Container).getChildByName("packageDay" + i) as CheckBox).selected  = rhythmNameToArray(value.sName)[i-1] == "1";
							}
						}catch(e:Error){}
					}

					selectedRhythmCode = value.sCode;
					selectedRhythm = value.sName;
					this.invalidateDisplayList();
				}
			}
			else
			{
				onDataProviderCallBack = setRhythm;
			}
		}

		private function rhythmNameToArray(rhythmName:String):Array
		{
			var result:Array = new Array(rhythmName.length);
				result = rhythmName.split('');
			return result;
		}

		public function get rhythm():DataListVO
		{
			var result:DataListVO = new DataListVO();

			for each(var item:DataListVO in dataProvider)
			{
				var o:DisplayObject = this.getChildByName(item.sCode);

				if((this.getChildByName(item.sCode) as RadioButton).selected)
				{
					result.sCode = item.sCode;
					if(item.sCode == "RHYTHM_WEEKDAYS")
					{
						result.sName = "";
						result.sName += ((this.getChildByName("Monday") as Container).getChildByName("Monday") as CheckBox).selected ? "1": "0";
						result.sName += ((this.getChildByName("Tuesday") as Container).getChildByName("Tuesday") as CheckBox).selected ? "1": "0";
						result.sName += ((this.getChildByName("Wednesday") as Container).getChildByName("Wednesday") as CheckBox).selected ? "1": "0";
						result.sName += ((this.getChildByName("Thursday") as Container).getChildByName("Thursday") as CheckBox).selected ? "1": "0";
						result.sName += ((this.getChildByName("Friday") as Container).getChildByName("Friday") as CheckBox).selected ? "1": "0";
						result.sName += ((this.getChildByName("Saturday") as Container).getChildByName("Saturday") as CheckBox).selected ? "1": "0";
						result.sName += ((this.getChildByName("Sunday") as Container).getChildByName("Sunday") as CheckBox).selected ? "1": "0";
					}
					else if(item.sCode == "RHYTHM_CUSTOMIZED")
					{
						var dDiff:int = DateUtils.dateDiff(DateUtils.DAY_OF_MONTH, DateField.stringToDate(model.ratesModule.barModule.currentPackage.sDateStart,GlobalSettings.DATE_SERVER_FORMAT),DateField.stringToDate(model.ratesModule.barModule.currentPackage.sDateEnd,GlobalSettings.DATE_SERVER_FORMAT));

						result.sName = "";
						for (var i:int=1; i<dDiff+1;i++)
						{
							result.sName += ((this.getChildByName("packageDay" + i) as Container).getChildByName("packageDay" + i) as CheckBox).selected ? "1": "0";
						}
					}
					else
					{
						result.sName = item.sName;
					}


					break;
				}
			}

			return result;
		}
	}
}