package devoron.components.labels
{
	import devoron.components.labels.DSLabel;
	import flash.events.MouseEvent;
	import flash.filters.GlowFilter;
	import flash.geom.Matrix;
	import net.kawa.tween.KTJob;
	import org.aswing.ASColor;
	import org.aswing.ASFont;
	import org.aswing.ASFontAdvProperties;
	import org.aswing.AssetIcon;
	import org.aswing.Component;
	import org.aswing.decorators.GradientBackgroundDecorator;
	import org.aswing.event.AWEvent;
	import org.aswing.geom.IntDimension;
	import org.aswing.Icon;
	import org.aswing.JFrame;
	import org.aswing.JLabel;
	import org.aswing.JToggleButton;
	
	/**
	 * TitleLabel
	 * @author Devoron
	 */
	public class TitleLabel extends DSLabel
	{
		[Embed(source="../../../../assets/icons/fuckit/ScrollBar_arrowRight_defaultImage.png")]
		private var rightDef:Class;
		
		[Embed(source="../../../../assets/icons/fuckit/ScrollBar_arrowRight_selectedImage.png")]
		private var rightSel:Class;
		
		[Embed(source="../../../../assets/icons/fuckit/ScrollBar_arrowRight_disabledImage.png")]
		private var rightDis:Class;
		
		[Embed(source="../../../../assets/icons/fuckit/ScrollBar_arrowRight_pressedImage.png")]
		private var rightPress:Class;
		
		[Embed(source="../../../../assets/icons/fuckit/ScrollBar_arrowRight_rolloverImage.png")]
		private var rightRoll:Class;
		
		[Embed(source="../../../../assets/icons/fuckit/ScrollBar_arrowRight_pressedSelectedImage.png")]
		private var rightSelPress:Class;
		
		[Embed(source="../../../../assets/icons/fuckit/ScrollBar_arrowRight_rolloverSelectedImage.png")]
		private var rightSelRoll:Class;
		public var tgb:JToggleButton;
		private var relatedComponent:Component;
		
		public function TitleLabel(text:String = "", icon:Icon = null, horizontalAlignment:int = JLabel.CENTER, relatedComponent:Component = null)
		{
			//this.relatedComponent = relatedComponent;
			//var titleLB:DSLabel = new DSLabel((dataContainer as IDataContainer).dataContainerType.toUpperCase(), dataContainer.icon, JLabel.CENTER);
			super(text, icon, horizontalAlignment);
			setRelatedComponent(relatedComponent);
			setForeground(new ASColor(0xFFFFFF, 0.4));
			setPreferredWidth(270);
			var colors:Array = [0x000000, 0x000000, 0x000000, 0x000000, 0x000000];
			var alphas:Array = [0.24, 0.14, 0.08, 0.04, 0.01];
			var ratios:Array = [0, 70, 145, 200, 255];
			var matrix:Matrix = new Matrix();
			matrix.createGradientBox(270, 22, 0, 0, 0);
			setBackgroundDecorator(new GradientBackgroundDecorator(GradientBackgroundDecorator.LINEAR, colors, alphas, ratios, matrix, "pad", "rgb", 0, new ASColor(0xFFFFFF, 0), 2));
			buttonMode = true;
			
				
			var advProp:ASFontAdvProperties = new ASFontAdvProperties(true, "advanced", "pixel");
			var font:ASFont = new ASFont("Palatino", 10, false, false, false, advProp);
			setFont(font);
			setForeground(new ASColor(0xFFFFFF, 0.4));
			
			tgb = new JToggleButton("", new AssetIcon(new rightDef, 16, 16), true);
			//tgb.setSize(new IntDimension(16, 22));
			tgb.setSize(new IntDimension(16, 16));
			tgb.setVisible(false);
			tgb.addActionListener(dataContainerBtnHandler);
			tgb.setBackgroundDecorator(null);
			tgb.setDisabledIcon(new AssetIcon(new rightDis, 16, 16));
			tgb.setRollOverIcon(new AssetIcon(new rightRoll, 16, 16));
			tgb.setSelectedIcon(new AssetIcon(new rightSel, 16, 16));
			tgb.setRollOverSelectedIcon(new AssetIcon(new rightSelRoll, 16, 16));
			tgb.mouseChildren = false;
			//tgb.y = 4;
			
			
			super.addChild(tgb);
			
			//addEventListener(MouseEvent.ROLL_OVER, onFormRollOver);
			//addEventListener(MouseEvent.ROLL_OUT, onFormRollOut);
			//doubleClickEnabled = true;
			//addEventListener(MouseEvent.DOUBLE_CLICK, onFormDoubleClick);
			//getI
			addEventListener(MouseEvent.CLICK, onFormDoubleClick);
			
			//tgb.ad
			//glowFilter = new GlowFilter(0xFFFFFF, 0.9, 0, 0, 2, 2);
			setTextFilters(text_filters);
			//labelFilters = [glowFilter];
			//glowFilter.blurX =
			//ktTween = KTween.to(glowFilter, 3, {alpha: 0.3}, Linear.easeIn);
			//ktTween = KTween.to(this, 0.71, {omg: 0.3}, Linear.easeIn);
			
			//ktTween2 = KTween.to(glowFilter, 3, {alpha: 0}, Linear.easeIn);
			//ktTween2 = KTween.to(this, 0.1, {omg: 0}, Linear.easeIn);
		}
		
		private var text_filters:Array = [new GlowFilter(0xFFFFFF, 0.3, 3, 3, 2, 2)];
		
		public function set omg(value:Number):void{
			//glowFilter.alpha = value;
			//if (super.getChildAt(0) )
			//(super.getChildAt(0)).filters = [glowFilter];
			//super.setTextFilters(labelFilters);
			//(getUI() as BasicLabelUI).textFi
		}
		
		public function get omg():Number{
			return glowFilter.blurX;
		}
		
		private function onChange():void
		{
			
		}
		
		private var frame:JFrame;
		private var glowFilter:GlowFilter;
		private var ktTween:KTJob;
		private var ktTween2:KTJob;
		private var labelFilters:Array;
		
		public function setFrameMode(frame:JFrame):void
		{
			this.frame = frame;
		}
		
		private function onFormDoubleClick(e:MouseEvent):void
		{
			tgb.setSelected(!tgb.isSelected());
			dataContainerBtnHandler(null);
		}
		
		public function setRelatedComponent(c:Component):void
		{
			if (relatedComponent)
			{
				relatedComponent.removeEventListener(MouseEvent.ROLL_OVER, onFormRollOver);
				relatedComponent.removeEventListener(MouseEvent.ROLL_OUT, onFormRollOut);
			}
			relatedComponent = c;
			if (c)
			{
				c.addEventListener(MouseEvent.ROLL_OVER, onFormRollOver);
				c.addEventListener(MouseEvent.ROLL_OUT, onFormRollOut);
			}
		}
		
		public function getRelatedComponent():Component
		{
			return relatedComponent;
		}
		
		private function dataContainerBtnHandler(e:AWEvent):void
		{
			if (relatedComponent)
			{
				
				if (frame)
				{
					/*var p:JScrollPane = relatedComponent.getParent() as JScrollPane;
					 gtrace(p);*/
						 //frame.getTitleBar().setM
					/*frame.getContentPane().setVisible(tgb.isSelected());
					   frame.revalidate();
					   frame.pack();
					   frame.updateUI();
					 frame.repaint();*/
				}
				else
				{
					relatedComponent.setVisible(tgb.isSelected());
				}
				
			}
		}
		
		private function onFormClick(e:MouseEvent):void
		{
			//if (tgb.hitTestMouse())
			//{
			//tgb.setSelected(!tgb.isSelected());
			//tgb.dispatchEvent(new AWEvent(AWEvent.ACT));
		//}
		}
		
		protected function onFormRollOut(e:MouseEvent):void
		{
			//super.setForeground(new ASColor(0xFFFFFF, 0.4));
			tgb.setVisible(false);
			//super.setTextFilters([]);
			//ktTween.abort();
			//ktTween2.init();
		}
		
		protected function onFormRollOver(e:MouseEvent):void
		{
			//super.setForeground(new ASColor(0xFFFFFF, 0.75));
			//super.setForeground(new ASColor(0xFFFFFF, 0.8));
			tgb.setVisible(true);
			
			//glowFilter.alpha = 0;
			omg = 0;
			//super.setTextFilters([glowFilter]);
			//ktTween.init();
			//ktTween.resume
		}
	
	}

}