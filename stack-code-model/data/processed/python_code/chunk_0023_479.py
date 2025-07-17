package classes
{	
	import caurina.transitions.Tweener;
	
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.events.MouseEvent;
	
	import flash.text.*;
	
	public class Field extends Sprite
	{
		[Embed(source='HelveticaNeueLTStd-Hv.otf', fontFamily = 'HelveticaHeavy')]
        private var HeavyHelvetica:Class;
        [Embed(source='HelveticaNeueLTStd-Lt.otf', fontFamily = 'HelveticaLite')]
        private var LiteHelvetica:Class;
		
		public var _myXML:theXML;
		public var _lengthXML:int;
		public var _Slider:Slider;
		public var _Position:int=0;
		public var _Year:String;
		
		public var speechBubble:MovieClip;
		public var exit_btn:Screen_Speechbaloon_Exit_btn = new Screen_Speechbaloon_Exit_btn;
		public var _n:int=0;

		
		public var dotArray:Array = new Array();
		public var coArray:Array = new Array();
		
		private var Pop_Ticker:Screen_Poulation_Ticker = new Screen_Poulation_Ticker;
		
		
		public function Field()
		{	
			
			var format:TextFormat = new TextFormat();
            format.color = 0x000000;
            format.size = 15;
            format.font = 'HelveticaHeavy';
            
            var format2:TextFormat = new TextFormat();
            format2.color = 0x000000;
            format2.size = 12;
            format2.font = 'HelveticaLite';
			
			speechBubble = new Screen_Speechbaloon;
			speechBubble.mouseChildren = true;
			speechBubble.Headline.embedFonts = true; 
			speechBubble.Headline.antiAliasType = AntiAliasType.ADVANCED; 
			speechBubble.Headline.defaultTextFormat = format;
			speechBubble.Date.embedFonts = true;
			speechBubble.Date.antiAliasType = AntiAliasType.ADVANCED; 
			speechBubble.Date.defaultTextFormat = format2;
			speechBubble.alpha=0.5;
			speechBubble.exit_btn.addEventListener(MouseEvent.CLICK, closeSpeechBubble);
			
			_Year = "";
			
			Pop_Ticker.x = 1024 - Pop_Ticker.width - 20;
			Pop_Ticker.y = 20;
			Pop_Ticker.population_txt.text = "";
			this.addChild(Pop_Ticker);
		}
		
		
		public function getCoords():void {
			

			for(var j:int=0;j<_myXML.myXML.Events.item.length();j++) { 
			
				coArray[j]=_myXML.myXML..coordinates[j].text().split(",");
				trace("coarray["+j+"][0]: "+coArray[j][0]);
				trace("coarray["+j+"][1]: "+coArray[j][1]);
				
			}
			
		}
		
		
		public function generateDots():void {
				

			for(var j:int=0;j<_myXML.myXML.Events.item.length();j++) {
				
				var clip:MovieClip = new MovieClip();
				clip.graphics.beginFill(0x000000,1);
				clip.graphics.drawCircle(3,3,4);
				clip.graphics.endFill();
				clip.name = j.toString();
				dotArray.push(clip);
				clip.x = coArray[j][0];
				clip.y = coArray[j][1];
				clip.addEventListener(MouseEvent.MOUSE_OVER, showSpeechBubble);
				
			}
		
		}
		
		public function showDot():void {
			
			if(this.contains(speechBubble)){
				this.removeChild(speechBubble);
			}
			
			for(var i:int=0;i<_myXML.myXML.Events.item.length();i++){
				
				dotArray[i].visible=false;
			}
			
			if(_Position>=_myXML.myXML.Events.item.length())	
				_Position = _myXML.myXML.Events.item.length() - 1;

			if(_Position<0)
				_Position = 0;
			
			Pop_Ticker.population_txt.text = _myXML.myXML..population[_Position].text();
			
			
			this.addChild(dotArray[_Position]);
			dotArray[_Position].visible=true;
			
		}
		
		public function showSpeechBubble(evt:MouseEvent):void {
			
				
			this.addChild(speechBubble);
			speechBubble.alpha=0.5;
			speechBubble.x=evt.target.x - (speechBubble.width/2)+4;
			speechBubble.y=evt.target.y - speechBubble.height;
			Tweener.addTween(speechBubble,{alpha:1,time:2,transition:"easeInOut"});
			_n = parseInt(evt.target.name);
			setContent();
			
		}
		
		public function closeSpeechBubble(evt:MouseEvent):void {
			
			
			this.removeChild(speechBubble);
		}
		
		public function setContent():void {
		
			trace("ausgewaehlt: "+_n);
			trace("item anzahl: "+_myXML.myXML.Events.item.length());
			
			speechBubble.Headline.text = _myXML.myXML..title[_n].text();
			//speechBubble.Subline.text = _myXML.myXML..description[_n].text();
			speechBubble.Text.text = _myXML.myXML..description[_n].text() + '\n' + _myXML.myXML..text[_n].text();
			speechBubble.Date.text = _myXML.myXML..date[_n].text();
			
		}
		
		
		public function get lengthXML():int
		{
			_lengthXML = _myXML.myXML.Events.item.length();
		
			return _lengthXML;
		}
		
		public function set position(pos:int):void {
			
			_Position = pos;
		}
		
		public function get year():String {
			
			_Year = _myXML.myXML..date[_Position].text();
			
			return _Year;
		}
	}
}