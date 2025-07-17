/*
 Copyright aswing.org, see the LICENCE.txt.
*/

package org.aswing.plaf{

import devoron.aswing3d.*;
import org.aswing.lookandfeel.plaf.AdjusterUI;
import org.aswing.lookandfeel.plaf.ComponentUI;

/**
 * Pluginable ui for JAdjuster.
 * @see devoron.aswing3d.JAdjuster
 * @author iiley
 */
public interface AdjusterUI extends ComponentUI{
	
	function getInputText():JTextField;
	
	function getPopupSlider():JSlider;
}
}