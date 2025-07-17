package interfaces.skin
{
    import spark.components.Group;
    import spark.components.Scroller;
import spark.layouts.VerticalLayout;
import spark.skins.mobile.supportClasses.MobileSkin;

public class AbstractSkin extends MobileSkin
    {
        /**
         *  @copy spark.components.SkinnableContainer#contentGroup
         */
        public var contentGroup:Group;

        public var scroller:Scroller;
        public var content:Group;

        public function AbstractSkin() {

        }

        override protected function createChildren():void
        {
            super.createChildren();

            scroller = new Scroller();
            addChild(scroller);

            contentGroup = new Group();
            contentGroup.left = contentGroup.right = contentGroup.top = contentGroup.bottom = 0;
            contentGroup.minWidth = contentGroup.minHeight = 0;

            content = new Group();
            content.id = "content";
            content.left = content.right = content.top = content.bottom = 10;
            contentGroup.addElement(content);

            addChild(contentGroup);
        }

        override protected function layoutContents(unscaledWidth:Number, unscaledHeight:Number):void
        {
            super.layoutContents(unscaledWidth, unscaledHeight);

            setElementPosition(scroller, 0, 0);
            setElementSize(scroller, unscaledWidth, unscaledHeight);

            scroller.viewport = contentGroup;

            setElementPosition(contentGroup, 0, 0);
            setElementSize(contentGroup, unscaledWidth, unscaledHeight);

            var verticalLayout:VerticalLayout = new VerticalLayout();
            verticalLayout.horizontalAlign = "center";
            verticalLayout.verticalAlign = "middle";
            verticalLayout.gap = 10;

            content.layout = verticalLayout;
            content.percentWidth = 100;
        }

        override protected function measure():void
        {
            super.measure();

            measuredWidth = contentGroup.getPreferredBoundsWidth();
            measuredHeight = contentGroup.getPreferredBoundsHeight();
        }
    }
}