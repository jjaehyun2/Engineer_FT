package {

import com.tuarua.Spotlight;
import com.tuarua.spotlight.ContentType;
import com.tuarua.spotlight.IndexError;
import com.tuarua.spotlight.SearchQuery;
import com.tuarua.spotlight.SearchQueryError;
import com.tuarua.spotlight.SearchableIndex;
import com.tuarua.spotlight.SearchableItem;
import com.tuarua.spotlight.SearchableItemAttributeSet;

import flash.desktop.NativeApplication;
import flash.events.Event;
import flash.filesystem.File;

import starling.display.Sprite;
import starling.events.Touch;
import starling.events.TouchEvent;
import starling.events.TouchPhase;
import starling.text.TextField;
import starling.utils.Align;

import views.SimpleButton;

public class StarlingRoot extends Sprite {
    private var indexBtn:SimpleButton = new SimpleButton("Index Items");
    private var deleteBtn:SimpleButton = new SimpleButton("Delete Index");
    private var queryBtn:SimpleButton = new SimpleButton("Get");

    private var statusLabel:TextField;
    private var index:SearchableIndex;

    public function StarlingRoot() {
        super();
        TextField.registerCompositor(Fonts.getFont("fira-sans-semi-bold-13"), "Fira Sans Semi-Bold 13");
        NativeApplication.nativeApplication.addEventListener(Event.EXITING, onExiting);
    }

    public function start():void {
        if (SearchableIndex.isIndexingAvailable) {
            initMenu();
            var spotlightId:String = SearchableIndex.spotlightId;
            if (spotlightId) {
                statusLabel.text = "Opened via Spotlight with id: " + SearchableIndex.spotlightId;
            }
        } else {
            trace("Spotlight is only supported on Mac OSX 10.11+ and iOS 9.0+");
        }
    }

    private function initMenu():void {
        indexBtn.y = 100;
        deleteBtn.y = 180;
        queryBtn.y = 260;
        indexBtn.addEventListener(TouchEvent.TOUCH, onIndexTouch);
        deleteBtn.addEventListener(TouchEvent.TOUCH, onDeleteTouch);
        queryBtn.addEventListener(TouchEvent.TOUCH, onQueryTouch);

        queryBtn.x = deleteBtn.x = indexBtn.x = (stage.stageWidth - 200) / 2;
        statusLabel = new TextField(stage.stageWidth, 100, "");
        statusLabel.format.setTo(Fonts.NAME, 13, 0x222222, Align.CENTER, Align.TOP);
        statusLabel.touchable = false;
        statusLabel.y = queryBtn.y + 75;

        addChild(indexBtn);
        addChild(deleteBtn);
        addChild(queryBtn);

        addChild(statusLabel);
    }

    private function onIndexTouch(event:TouchEvent):void {
        event.stopPropagation();
        var touch:Touch = event.getTouch(indexBtn, TouchPhase.ENDED);
        if (touch && touch.phase == TouchPhase.ENDED) {
            var attributeSet:SearchableItemAttributeSet = new SearchableItemAttributeSet(ContentType.text);
            attributeSet.title = "My First Spotlight Search";
            attributeSet.contentDescription = "This is a starry document";
            attributeSet.keywords = new <String>["example", "beer"];
            attributeSet.thumbnailURL = File.applicationDirectory.resolvePath("docs-icon.png").nativePath;
            attributeSet.importantDates = new Vector.<Date>();
            attributeSet.importantDates.push(new Date());

            var item:SearchableItem = new SearchableItem("starlightDoc", "com.tuarua", attributeSet);
            index = new SearchableIndex();
            var items:Vector.<SearchableItem> = new <SearchableItem>[item];

            index.indexSearchableItems(items, function (error:IndexError):void {
                if (error) {
                    statusLabel.text = "Error: " + error.errorID + " : " + error.message;
                    return;
                }
                statusLabel.text = "Index complete";
                index.dispose();
            });
        }
    }

    private function onDeleteTouch(event:TouchEvent):void {
        event.stopPropagation();
        var touch:Touch = event.getTouch(deleteBtn, TouchPhase.ENDED);
        if (touch && touch.phase == TouchPhase.ENDED) {
            index = new SearchableIndex();
            index.deleteSearchableItems(null, new <String>["com.tuarua"], function (error:IndexError):void {
                if (error) {
                    statusLabel.text = "Error: " + error.errorID + " : " + error.message;
                    return;
                }
                statusLabel.text = "Index Delete complete";
            });
        }
    }

    private function onQueryTouch(event:TouchEvent):void {
        event.stopPropagation();
        var touch:Touch = event.getTouch(queryBtn, TouchPhase.ENDED);
        if (touch && touch.phase == TouchPhase.ENDED) {
            var query:SearchQuery = new SearchQuery("contentDescription == \"*starry*\"c",
                    new <String>["title", "displayName", "keywords", "contentDescription", "contentType"]);
            query.start(function (results:Vector.<SearchableItem>, error:SearchQueryError):void {
                if (error) {
                    statusLabel.text = "Error: " + error.errorID + " : " + error.message;
                    return;
                }
                statusLabel.text = results.length + " results";
                for each (var result:SearchableItem in results) {
                    trace(result.uniqueIdentifier, result.domainIdentifier);
                    var attrSet:SearchableItemAttributeSet = result.attributeSet;
                    trace(attrSet.title, attrSet.contentDescription,
                            attrSet.keywords, attrSet.displayName, attrSet.contentType);

                }
                query.dispose();
            });
        }
    }

    private function onExiting(event:Event):void {
        Spotlight.dispose();
    }

}
}