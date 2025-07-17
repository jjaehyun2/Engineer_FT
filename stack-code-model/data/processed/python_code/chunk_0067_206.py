package com.unhurdle.spectrum.const
{
  public class IconType
  {
    public static const ALERT_MEDIUM:String = "AlertMedium"
    public static const ALERT_SMALL:String = "AlertSmall"
    public static const ARROW_DOWN_SMALL:String = "ArrowDownSmall"
    public static const ARROW_LEFT_MEDIUM:String = "ArrowLeftMedium"
    public static const ARROW_UP_SMALL:String = "ArrowUpSmall"
    public static const ASTERISK:String = "Asterisk"
    public static const CHECKMARK_MEDIUM:String = "CheckmarkMedium"
    public static const CHECKMARK_SMALL:String = "CheckmarkSmall"
    public static const CHEVRON_DOWN_MEDIUM:String = "ChevronDownMedium"
    public static const CHEVRON_DOWN_SMALL:String = "ChevronDownSmall"
    public static const CHEVRON_LEFT_LARGE:String = "ChevronLeftLarge"
    public static const CHEVRON_LEFT_MEDIUM:String = "ChevronLeftMedium"
    public static const CHEVRON_RIGHT_LARGE:String = "ChevronRightLarge"
    public static const CHEVRON_RIGHT_MEDIUM:String = "ChevronRightMedium"
    public static const CHEVRON_RIGHT_SMALL:String = "ChevronRightSmall"
    public static const CHEVRON_UP_SMALL:String = "ChevronUpSmall"
    public static const CORNER_TRIANGLE:String = "CornerTriangle"
    public static const CROSS_LARGE:String = "CrossLarge"
    public static const CROSS_MEDIUM:String = "CrossMedium"
    public static const CROSS_SMALL:String = "CrossSmall"
    public static const DASH_SMALL:String = "DashSmall"
    public static const DOUBLE_GRIPPER:String = "DoubleGripper"
    public static const FOLDER_BREADCRUMB:String = "FolderBreadcrumb"
    public static const HELP_MEDIUM:String = "HelpMedium"
    public static const HELP_SMALL:String = "HelpSmall"
    public static const INFO_MEDIUM:String = "InfoMedium"
    public static const INFO_SMALL:String = "InfoSmall"
    public static const MAGNIFIER:String = "Magnifier"
    public static const MORE:String = "More"
    public static const SKIP_LEFT:String = "SkipLeft"
    public static const SKIP_RIGHT:String = "SkipRight"
    public static const STAR:String = "Star"
    public static const STAR_OUTLINE:String = "StarOutline"
    public static const SUCCESS_MEDIUM:String = "SuccessMedium"
    public static const SUCCESS_SMALL:String = "SuccessSmall"
    public static const TRIPLE_GRIPPER:String = "TripleGripper"

    public static function hasType(value:String):Boolean{
      switch(value){
        case "AlertMedium":
        case "AlertSmall":
        case "ArrowDownSmall":
        case "ArrowLeftMedium":
        case "ArrowUpSmall":
        case "Asterisk":
        case "CheckmarkMedium":
        case "CheckmarkSmall":
        case "ChevronDownMedium":
        case "ChevronDownSmall":
        case "ChevronLeftLarge":
        case "ChevronLeftMedium":
        case "ChevronRightLarge":
        case "ChevronRightMedium":
        case "ChevronRightSmall":
        case "ChevronUpSmall":
        case "CornerTriangle":
        case "CrossLarge":
        case "CrossMedium":
        case "CrossSmall":
        case "DashSmall":
        case "DoubleGripper":
        case "FolderBreadcrumb":
        case "HelpMedium":
        case "HelpSmall":
        case "InfoMedium":
        case "InfoSmall":
        case "Magnifier":
        case "More":
        case "SkipLeft":
        case "SkipRight":
        case "Star":
        case "StarOutline":
        case "SuccessMedium":
        case "SuccessSmall":
        case "TripleGripper":
          return true;
        default:
          return false;
      }

    }
    // public static const VIEW_LIST:String = "viewList"
    // public static const VIEW_GRID:String = "viewGrid"
    // public static const VIEW_CARD:String = "viewCard"
    // public static const EDIT:String = "viewCard"
    // public static const COPY:String = "viewCard"
    // public static const DELETE:String = "viewCard"
  }
}