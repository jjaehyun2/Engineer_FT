package devoron.components
{
	import away3d.loaders.parsers.particleSubParsers.values.setters.threeD.ThreeDConstSetter;
	import devoron.gameeditor.particleeditor.nodeforms.components.color.CompositeColorComponent;
	import devoron.gameeditor.particleeditor.nodeforms.components.color.ConstColorComponent;
	import devoron.gameeditor.particleeditor.nodeforms.components.fourD.FourDCompositeWithOneDComponent;
	import devoron.gameeditor.particleeditor.nodeforms.components.fourD.FourDCompositeWithThreeDComponent;
	import devoron.gameeditor.particleeditor.nodeforms.components.oneD.OneDValueComponent;
	import devoron.gameeditor.particleeditor.nodeforms.components.threeD.ThreeDValueComponent;
	import devoron.particles.values.CompositeColor;
	import devoron.particles.values.ConstColor;
	import devoron.particles.values.FourDCompositeWithOneDValue;
	import devoron.particles.values.FourDCompositeWithThreeDValue;
	import devoron.particles.values.OneDValue;
	import devoron.particles.values.ThreeDValue;
	import devoron.utils.components.GrayCB;
	import org.aswing.event.AWEvent;
	import org.aswing.ext.Form;
	import org.aswing.ext.FormRow;
	import org.aswing.util.HashMap;
	
	/**
	 * ...
	 * @author ...
	 */
	public class CompoundComponent extends Form
	{
		private var typesCB:GrayCB;
		private var tdvc:ThreeDValueComponent;
		private var odvc:OneDValueComponent;
		private var ccc:ConstColorComponent;
		private var ccc2:CompositeColorComponent;
		private var fdcwodc:FourDCompositeWithOneDComponent;
		private var fdcwtdc:FourDCompositeWithThreeDComponent;
		
		private var cccFR:FormRow;
		private var cccFR2:FormRow;
		
		public function CompoundComponent()
		{
			super();
			super.setBackgroundDecorator(new formDec());
			
			typesCB = new GrayCB();
			typesCB.setListData(["ThreeDConst", "ThreeDComposite", "ThreeDSphere", "ThreeDCylinder", "OneDConst", "OneDRandom", "ConstColor", "FourDCompositeWithOneD", "FourDCompositeWithThreeD", "CompositeColor"]);
			typesCB.setPreferredWidth(170);
			
			typesCB.addActionListener(typesCBHandler);
			super.addLeftHoldRow(0, typesCB);
			
			var typesAndRows:HashMap = new HashMap();
			
			tdvc = new ThreeDValueComponent();
			odvc = new OneDValueComponent();
			ccc = new ConstColorComponent();
			ccc2 = new CompositeColorComponent();
			fdcwodc = new FourDCompositeWithOneDComponent();
			fdcwtdc = new FourDCompositeWithThreeDComponent();
			
			tdvc.setOwnerForm(super, 10);
			odvc.setOwnerForm(super, 10);
			cccFR = super.addLeftHoldRow(0, 10, ccc);
			cccFR2 = super.addLeftHoldRow(0, 10, ccc2);
			fdcwodc.setOwnerForm(super, 10);
			fdcwtdc.setOwnerForm(super, 10);
			
			typesCB.setSelectedIndex(0);
		}
		
		private function typesCBHandler(e:AWEvent):void
		{
			tdvc.setVisible(false);
			odvc.setVisible(false);
			cccFR.setVisible(false);
			cccFR2.setVisible(false);
			fdcwodc.setVisible(false);
			fdcwtdc.setVisible(false);
			
			var type:String = typesCB.getSelectedItem();
			
			if (type == "ThreeDConst" || type == "ThreeDComposite" || type == "ThreeDSphere" || type == "ThreeDCylinder")
			{
				tdvc.threeDValuesCB.setSelectedItem(type);
				tdvc.setVisible(true);
			}
			else if (type == "OneDConst" || type == "OneDRandom")
			{
				odvc.oneDValuesCB.setSelectedItem(type);
				odvc.setVisible(true);
			}
			else if (type == "ConstColor")
			{
				cccFR.setVisible(true);
			}
			else if (type == "CompositeColor")
			{
				cccFR2.setVisible(true);
			}
			else if (type == "FourDCompositeWithOneD")
			{
				fdcwodc.setVisible(true);
			}
			else if (type == "FourDCompositeWithThreeD")
			{
				fdcwtdc.setVisible(true);
			}
		
		}
		
		public function getValue():*
		{
			var type:String = typesCB.getSelectedItem();
			
			if (type == "ThreeDConst" || type == "ThreeDComposite" || type == "ThreeDSphere" || type == "ThreeDCylinder")
			{
				return tdvc.getRelatedThreeDValue();
			}
			else if (type == "OneDConst" || type == "OneDRandom")
			{
				return odvc.getRelatedOneDValue();
			}
			else if (type == "ConstColor")
			{
				return ccc.getRelatedConstColor();
			}
			else if (type == "CompositeColor")
			{
				return ccc2.getRelatedCompositeColor();
			}
			else if (type == "FourDCompositeWithOneD")
			{
				return fdcwodc.getRelatedFourDValue();
			}
			else if (type == "FourDCompositeWithThreeD")
			{
				return fdcwtdc.getRelatedFourDValue();
			}
			return null;
		}
		
		public function setValue(value:*):void
		{
			if (value is ThreeDValue) {
				tdvc.setRelatedThreeDValue(value);
				typesCB.setSelectedItem(tdvc.threeDValuesCB.getSelectedItem());
			}
			else if (value  is OneDValue) {
				odvc.setRelatedOneDValue(value);
				typesCB.setSelectedItem(odvc.oneDValuesCB.getSelectedItem());
			}
			else if (value is ConstColor) {
				ccc.setRelatedConstColor(value);
				typesCB.setSelectedItem("ConstColor");
			}
			else if (value is CompositeColor) {
				ccc2.setRelatedCompositeColor(value);
				typesCB.setSelectedItem("CompositeColor");
			}
			else if (value is FourDCompositeWithOneDValue) {
				fdcwodc.setRelatedFourDValue(value);
				typesCB.setSelectedItem("FourDCompositeWithOneDValue");
			}
			else if (value is FourDCompositeWithThreeDValue) {
				fdcwtdc.setRelatedFourDValue(value);
				typesCB.setSelectedItem("FourDCompositeWithThreeDValue");
			}
		}
		
	}

}

import flash.display.DisplayObject;
import flash.display.Sprite;
import org.aswing.ASColor;
import org.aswing.geom.IntRectangle;
import org.aswing.graphics.Graphics2D;
import org.aswing.Component;
import org.aswing.graphics.Pen;
import org.aswing.graphics.SolidBrush;
import org.aswing.GroundDecorator;

internal class formDec implements GroundDecorator
{
	
	public function formDec()
	{
	
	}
	
	/* INTERFACE org.aswing.GroundDecorator */
	
	public function updateDecorator(c:Component, g:Graphics2D, b:IntRectangle):void
	{
		//var pen:
		g.beginFill(new SolidBrush(new ASColor(0x0E1012)));
		g.drawRoundRect(new Pen(new ASColor(0XFFFFFF, 0.4), 1), b.x, b.y, b.width - 1, b.height - 1, 3);
		g.endDraw();
		g.endFill();
	}
	
	public function getDisplay(c:Component):DisplayObject
	{
		return new Sprite();
	}

}