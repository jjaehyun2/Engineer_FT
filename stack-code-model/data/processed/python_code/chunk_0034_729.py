package io.decagames.rotmg.tos.popups.buttons {
    import io.decagames.rotmg.ui.buttons.SliceScalingButton;
    import io.decagames.rotmg.ui.defaults.DefaultLabelFormat;
    import io.decagames.rotmg.ui.texture.TextureParser;
    
    public class GoBackButton extends SliceScalingButton {
        
        
        public function GoBackButton() {
            super(TextureParser.instance.getSliceScalingBitmap("UI", "generic_green_button"));
            setLabel("Go Back", DefaultLabelFormat.defaultButtonLabel);
            width = 100;
        }
    }
}