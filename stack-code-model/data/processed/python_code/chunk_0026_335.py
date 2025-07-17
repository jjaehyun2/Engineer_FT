/**
 * Created by bslote on 3/29/15.
 */
package pw.fractal.vbm.view
{
    import flash.display.Shape;
    import flash.display.Sprite;
    import flash.text.TextField;
    import flash.text.TextFieldAutoSize;

    import pw.fractal.vbm.model.GoldenRhombusModel;

    public class GoldenRhombus extends Sprite
    {
        private var _model:GoldenRhombusModel;
        private var _shape:Shape;
        private var _textField:TextField;

        public function GoldenRhombus(model:GoldenRhombusModel)
        {
            _model = model;
            _shape = new Shape();
            _textField = new TextField();

            draw();

            addChild(_shape);
            addChild(_textField);

            setText();
        }

        private function draw():void
        {
            var p:Number = _model.p;
            var q:Number = _model.q;

            with (_shape.graphics)
            {
                lineStyle(_model.lineThicknes, _model.lineColor);

                beginFill(_model.backgroundColor);

                moveTo(p / 2, 0);
                lineTo(p, q / 2);

                moveTo(p / 2, 0);
                lineTo(0, q / 2);

                moveTo(p / 2, q);
                lineTo(p, q / 2);

                moveTo(p / 2, q);
                lineTo(0, q / 2);

                endFill();
            }
        }

        private function setText():void
        {
            _textField.autoSize = TextFieldAutoSize.LEFT;
//            _textField.embedFonts = true;
            _textField.text = _model.text;

            _textField.x = (width - _textField.width) / 2;
            _textField.y = (height - _textField.height) / 2;
        }
    }
}