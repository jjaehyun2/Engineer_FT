package{
	import flash.events.*;
	import flash.display.*;
	public class txtft{
	public function Tab(tune:String) {
    var _tune = tune;
    var mainSprite:Sprite = new Sprite();
    addChild(mainSprite);
    drawBorder();
    createFormat();
    placeArtist();
    placeTitle();
    placeAlbum();
    coverArt();

}

private function placeButton():void {
    _button = new Sprite();
    _button.graphics.beginFill(0xFF000,0);
    _button.graphics.drawRect(0,0,229,40);
    _button.graphics.endFill();
    _button.addEventListener(MouseEvent.MOUSE_OVER, mouseListener);
    _button.addEventListener(MouseEvent.MOUSE_OUT, mouseListener);
    _button.buttonMode = true;
    mainSprite.addChild(_button);
}

private function mouseListener(event:MouseEvent):void {
        switch(event.type){
            case MouseEvent.MOUSE_OVER :
                hilite(true);
                break;
            case MouseEvent.MOUSE_OUT :
                hilite(false);
                break;
        }
}

private function createFormat():void {
    _format = new TextFormat();
    _format.font = "FFF Neostandard";
    _format.size = 8;
    _format.color = 0xFFFFFF;
}

private function placeArtist():void {
    var artist : TextField = new TextField();
    artist.selectable = false;
    artist.defaultTextFormat = _format;

    artist.x = 41;
    artist.y = 3;
    artist.width = 135;
    artist.text = _tune.artist;
    artist.mouseEnabled = false;
    mainSprite.addChild(artist);
}

private function placeTitle():void {
    var title : TextField = new TextField();
    title.selectable = false;
    title.defaultTextFormat = _format;

    title.x = 41;
    title.y = 14;
    title.width = 135;
    title.text = _tune.title;
    title.mouseEnabled = false;
    mainSprite.addChild(title);
}

private function placeAlbum():void {
    var album : TextField = new TextField();
    album.selectable = false;
    album.defaultTextFormat = _format;

    album.x = 41;
    album.y = 25;
    album.width = 135;
    album.text = _tune.album;
    album.mouseEnabled = false;
    mainSprite.addChild(album);
}

private function drawBorder():void {
    _border = new Sprite();
    _border.graphics.lineStyle(1, 0x545454);
    _border.graphics.drawRect (0,0,229,40);
    mainSprite.addChild(_border);
}

private function coverArt():void {
    _image = new Sprite();
    var imageLoader : Loader = new Loader();

    _loaderInfo = imageLoader.contentLoaderInfo;
    _loaderInfo.addEventListener(Event.COMPLETE, coverLoaded)

    var image:URLRequest = new URLRequest(_tune.coverArt);
    imageLoader.load(image);
    _image.x = 1.5;
    _image.y = 2;
    _image.addChild(imageLoader);
}

private function coverLoaded(event:Event):void {
    _loaderInfo.removeEventListener(Event.COMPLETE, coverLoaded);
    var scaling : Number = IMAGE_SIZE / _image.width;
    _image.scaleX = scaling;
    _image.scaleY = scaling;
    mainSprite.addChild (_image);
    placeButton();
}

public function hilite(state:Boolean):void{
    var col : ColorTransform = new ColorTransform();
    if(state){
        col.color = 0xFFFFFF;
    } else {
        col.color = 0x545454;
    }
    _border.transform.colorTransform =  col;
}
	}
}