package org.ro.view {
public class ImageRepository {

    //FIXME move to App.mxml
    [Embed('../../../../resources/images/history.png')]
    [Bindable]
    public static var LogIcon:Class;

    [Embed('../../../../resources/images/check-circle.png')]
    [Bindable]
    public static var GreenIcon:Class;

    [Embed('../../../../resources/images/question-circle.png')]
    [Bindable]
    public static var YellowIcon:Class;

    [Embed('../../../../resources/images/times-circle.png')]
    [Bindable]
    public static var RedIcon:Class;

    [Embed('../../../../resources/images/info-circle.png')]
    [Bindable]
    public static var BlueIcon:Class;

    [Embed('../../../../resources/images/cubes.png')]
    [Bindable]
    public static var ObjectsIcon:Class;

    [Embed('../../../../resources/images/cube.png')]
    [Bindable]
    public static var ObjectIcon:Class;

    [Embed("../../../../resources/images/pencil-alt.png")]
    [Bindable]
    public static var PencilIcon:Class;

    [Embed("../../../../resources/images/Magere_Brug_isis.png")]
    [Bindable]
    public static var AboutImage:Class;

    [Embed("../../../../resources/images/calendar.png")]
    [Bindable]
    public static var CalendarIcon:Class;

    [Embed("../../../../resources/images/check.png")]
    [Bindable]
    public static var CheckIcon:Class;

    [Embed("../../../../resources/images/times.png")]
    [Bindable]
    public static var TimesIcon:Class;

    [Embed("../../../../resources/images/tree.png")]
    [Bindable]
    public static var TreeIcon:Class;

 //TODO check when App.mxml is the right place for icons ...
    
    public function ImageRepository() {
    }
}
}