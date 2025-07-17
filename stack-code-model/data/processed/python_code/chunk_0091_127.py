package {

	import flash.display.*;
	import flash.events.*;
	import flash.text.*;
	import fl.controls.*;
	import flash.net.URLRequest;


	//Call this class the SAME NAME as the file - VERY IMPORTANT
	public class DocumentClass extends MovieClip {



		public var test: MovieClip;
		public var BookTitle: String = "Title";
		public var AuthorName: String = "Your name";
		public var StoryText: String = "Story goes here...";
		public var TitleTi: TextArea;
		public var AuthorTi: TextArea;
		public var Story_Ti: TextArea;
		public var bee: String = "images/bee.png";
		public var blankImage: String = "images/blankImage.png";
		public var cat: String = "images/cat.png";
		public var dino: String = "images/dino.png";
		public var dog: String = "images/dog_with_bone.png";
		public var hotdog: String = "images/hotdog.png";
		public var house: String = "images/house.png";
		public var cookies: String = "images/milk_cookies.png";
		public var sandwhich: String = "images/sandwhich.png";
		public var tv: String = "images/tv.png";
		//public var Prev_btn: SimpleButton;
		//public var Next_btn: SimpleButton;
		public var counter: int = 0;


		//BAD CODING WARNING
		public function CaptureText(): void {
			if (TitleTi)
				BookTitle = TitleTi.text;
			if (AuthorTi)
				AuthorName = AuthorTi.text;
		}

		public function changeImage(fileName: String): void {
			test = PageImage_mc;
			var image: Bitmap;
			var request: URLRequest = new URLRequest(fileName);
			var loader: Loader = new Loader();
			loader.contentLoaderInfo.addEventListener(Event.COMPLETE, onImageLoaded);
			loader.load(request);
			test.removeChildAt(0);

			function onImageLoaded(e: Event): void {
				image = new Bitmap(e.target.content.bitmapData);
				image.width = 200;
				image.height = 150;
				test.addChild(image);
			}

		}

		//This is called a construct - this function automatically
		//runs when this class is seen by flash.
		public function DocumentClass() {

			var Pages: Array = new Array();
			for (var i: int = 0; i < 10; i++) {
				var Page: Object = {
					pageImage: String,
					story: String,
					pageNumber: int
				};
				Pages.push(Page);
			}

			for (var p: int = 0; p < 10; p++) {
				Pages[p].story = "Pages " + (p + 1);
				Pages[p].pageImage = "images/blankImage.png";
			}



			stop();

			var Cover_tf: TextFormat = new TextFormat();


			Cover_tf.font = "Verdana";
			Cover_tf.size = 30;
			Cover_tf.align = "center";
			Cover_tf.italic = true;
			TitleTi.setStyle("textFormat", Cover_tf);
			AuthorTi.setStyle("textFormat", Cover_tf);
			TitleTi.text = BookTitle;
			AuthorTi.text = AuthorName;


			Header_mc.Cover_btn.addEventListener(MouseEvent.CLICK, goCover);
			function goCover(event: MouseEvent): void {
				Pages[counter].story = Story_Ti.text;
				counter = 0;

				gotoAndStop(1);
				Cover_tf.font = "Verdana";
				Cover_tf.size = 30;
				Cover_tf.align = "center";
				Cover_tf.italic = true;
				TitleTi.setStyle("textFormat", Cover_tf);
				AuthorTi.setStyle("textFormat", Cover_tf);
				TitleTi.text = BookTitle;
				AuthorTi.text = AuthorName;
			}

			Header_mc.Story_btn.addEventListener(MouseEvent.CLICK, goStory);

			function goStory(event: MouseEvent): void {
				CaptureText();
				counter = 0;

				gotoAndStop(2);
				var Story_tf: TextFormat = new TextFormat();

				Story_tf.font = "TimesNewRoman";
				Story_tf.size = 14;
				Story_tf.align = "center";
				Story_Ti.setStyle("textFormat", Story_tf);
				Story_Ti.text = Pages[0].story;


				Next_btn.addEventListener(MouseEvent.CLICK, nextPage);

				function nextPage(event: MouseEvent): void {

					Pages[counter].story = Story_Ti.text;
					counter += 1;
					changeImage(Pages[counter].pageImage);
					Story_Ti.text = Pages[counter].story;
					if (counter == 9) {
						Next_btn.enabled = false;
						Next_btn.visible = false;
					} else if (counter < 9) {
						Next_btn.enabled = true;
						Next_btn.visible = true;
					}
					if (counter == 0) {
						Prev_btn.enabled = false;
						Prev_btn.visible = false;
					} else if (counter > 0) {
						Prev_btn.enabled = true;
						Prev_btn.visible = true;
					}
				}


				Prev_btn.addEventListener(MouseEvent.CLICK, prevPage);
				Prev_btn.enabled = false;
				Prev_btn.visible = false;
				function prevPage(event: MouseEvent): void {

					Pages[counter].story = Story_Ti.text;
					counter -= 1;
					changeImage(Pages[counter].pageImage);
					Story_Ti.text = Pages[counter].story;
					if (counter == 9) {
						Next_btn.enabled = false;
						Next_btn.visible = false;
					} else if (counter < 9) {
						Next_btn.enabled = true;
						Next_btn.visible = true;
					}
					if (counter == 0) {
						//Prev_btn.enabled = false;
						Prev_btn.visible = false;
					} else if (counter > 0) {
						//Prev_btn.enabled = true;
						Prev_btn.visible = true;
					}
				}


				PageImage_mc.addEventListener(MouseEvent.CLICK, open_closeImages);

				function open_closeImages(event: MouseEvent): void {
					if (ImageBox.visible == false)
						ImageBox.visible = true;
					else if (ImageBox.visible == true)
						ImageBox.visible = false;
				}

				ImageBox.Image1_btn.addEventListener(MouseEvent.CLICK, getImage);

				function getImage(event: MouseEvent): void {
					changeImage(dog);
					Pages[counter].pageImage = dog
				}

				ImageBox.hotdog_btn.addEventListener(MouseEvent.CLICK, getHotdog);

				function getHotdog(event: MouseEvent): void {
					changeImage(hotdog);
					Pages[counter].pageImage = hotdog
				}

				ImageBox.bee_btn.addEventListener(MouseEvent.CLICK, getBee);

				function getBee(event: MouseEvent): void {
					changeImage(bee);
					Pages[counter].pageImage = bee
				}

				ImageBox.house_btn.addEventListener(MouseEvent.CLICK, getHouse);

				function getHouse(event: MouseEvent): void {
					changeImage(house);
					Pages[counter].pageImage = house
				}

				ImageBox.tv_btn.addEventListener(MouseEvent.CLICK, getTv);

				function getTv(event: MouseEvent): void {
					changeImage(tv);
					Pages[counter].pageImage = tv
				}

				ImageBox.cat_btn.addEventListener(MouseEvent.CLICK, getCat);

				function getCat(event: MouseEvent): void {
					changeImage(cat);
					Pages[counter].pageImage = cat
				}



				Header_mc.Back_btn.addEventListener(MouseEvent.CLICK, goBack);

				function goBack(event: MouseEvent): void {
					CaptureText();
					//Pages[counter].story = Story_Ti.text;
					//counter = 0;
					gotoAndStop(3);
				}

				

			}

		}
	}

}