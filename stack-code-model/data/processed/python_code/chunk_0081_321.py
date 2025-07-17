package 
{
    import flash.display.*;
    import flash.events.*;
    import flash.net.*;
    import flash.text.*;

    dynamic public class contactContent extends MovieClip
    {
        public var getProcessor:URLRequest;
        public var responseText:TextField;
        public var xml:XML;
        public var contact:XMLList;
        public var sendMail:MovieClip;
        public var clearFields:MovieClip;
        public var Email:TextField;
        public var goodSheet:StyleSheet;
        public var req:URLRequest;
        public var emailProcessorPath:String;
        public var Name:TextField;
        public var nuLoader:URLLoader;
        public var eXternalImage1:Bitmap;
        public var emailVars:URLVariables;
        public var Message:TextField;
        public var reply:String;
        public var cssLoader:URLLoader;

        public function contactContent()
        {
            addFrameScript(0, frame1);
            return;
        }// end function

        public function imageLoaded1(param1:Event) : void
        {
            eXternalImage1.bitmapData = Bitmap(param1.target.content).bitmapData;
            addChild(eXternalImage1);
            return;
        }// end function

        public function AddImage1(param1, param2, param3) : void
        {
            var _loc_4:String;
            var _loc_5:URLRequest;
            var _loc_6:*;
            _loc_4 = param3;
            _loc_5 = new URLRequest(_loc_4);
            _loc_6 = new Loader();
            _loc_6.contentLoaderInfo.addEventListener(Event.COMPLETE, imageLoaded1, false, 0, true);
            _loc_6.load(_loc_5);
            eXternalImage1.x = param1;
            eXternalImage1.y = param2;
            return;
        }// end function

        public function CreateTextField(param1, param2, param3, param4, param5) : void
        {
            var _loc_6:TextField;
            var _loc_7:String;
            _loc_7 = param5;
            _loc_6 = new TextField();
            _loc_6.styleSheet = goodSheet;
            _loc_6.htmlText = _loc_7;
            _loc_6.selectable = false;
            _loc_6.width = param3;
            _loc_6.autoSize = TextFieldAutoSize.LEFT;
            _loc_6.wordWrap = param4;
            _loc_6.x = param1;
            _loc_6.y = param2;
            addChild(_loc_6);
            return;
        }// end function

        public function sendEmail(param1:Event) : void
        {
            responseText.text = "";
            if (stage.displayState == StageDisplayState.FULL_SCREEN)
            {
                stage.displayState = StageDisplayState.NORMAL;
            }// end if
            if (Name.text == "NAME" || Name.text == "")
            {
                responseText.text = "Please Provide Your Name";
                return;
            }// end if
            if (Email.text == "EMAIL" || Email.text == "")
            {
                responseText.text = "Please Provide Your Email";
                return;
            }// end if
            if (Message.text == "MSG." || Message.text == "")
            {
                responseText.text = "Please Provide A Message";
                return;
            }// end if
            sendMail.removeEventListener(MouseEvent.CLICK, sendEmail);
            emailVars.Name = Name.text;
            emailVars.Email = Email.text;
            emailVars.Message = Message.text;
            getProcessor.data = emailVars;
            nuLoader.addEventListener(Event.COMPLETE, emailSent);
            getProcessor.method = URLRequestMethod.POST;
            nuLoader.load(getProcessor);
            return;
        }// end function

        public function messageClickHandler(param1:MouseEvent) : void
        {
            if (stage.displayState == StageDisplayState.FULL_SCREEN)
            {
                stage.displayState = StageDisplayState.NORMAL;
            }// end if
            responseText.text = "";
            if (Message.text == "MSG.")
            {
                Message.replaceText(0, 5, "");
            }// end if
            if (Email.text.length < 1)
            {
                Email.text = "EMAIL";
            }// end if
            if (Name.text.length < 1)
            {
                Name.text = "NAME";
            }// end if
            return;
        }// end function

        public function emailSent(param1:Event) : void
        {
            responseText.text = "Message has been delivered";
            Name.text = "NAME";
            Email.text = "EMAIL";
            Message.text = "MSG.";
            sendMail.addEventListener(MouseEvent.CLICK, sendEmail);
            return;
        }// end function

        public function xmlFinishedLoading(param1:Event) : void
        {
            xml = new XML(param1.target.data);
            contact = xml.contact;
            cssLoader = new URLLoader();
            cssLoader.addEventListener(Event.COMPLETE, cssLoaded, false, 0, true);
            cssLoader.load(req);
            return;
        }// end function

        public function emailClickHandler(param1:MouseEvent) : void
        {
            if (stage.displayState == StageDisplayState.FULL_SCREEN)
            {
                stage.displayState = StageDisplayState.NORMAL;
            }// end if
            responseText.text = "";
            if (Email.text == "EMAIL")
            {
                Email.replaceText(0, 5, "");
            }// end if
            if (Name.text.length < 1)
            {
                Name.text = "NAME";
            }// end if
            if (Message.text.length < 1)
            {
                Message.text = "MSG.";
            }// end if
            return;
        }// end function

        function frame1()
        {
            if (stage.displayState == StageDisplayState.FULL_SCREEN)
            {
                stage.displayState = StageDisplayState.NORMAL;
            }// end if
            req = new URLRequest("site_stylesheets/contact.css");
            goodSheet = new StyleSheet();
            reply = "Email sent successfully!";
            emailProcessorPath = "email.php";
            getProcessor = new URLRequest(emailProcessorPath);
            emailVars = new URLVariables();
            nuLoader = new URLLoader();
            eXternalImage1 = new Bitmap();
            Name.addEventListener(MouseEvent.CLICK, nameClickHandler);
            Email.addEventListener(MouseEvent.CLICK, emailClickHandler);
            Message.addEventListener(MouseEvent.CLICK, messageClickHandler);
            responseText.selectable = false;
            sendMail.buttonMode = true;
            sendMail.mouseChildren = false;
            clearFields.buttonMode = true;
            clearFields.mouseChildren = false;
            sendMail.addEventListener(MouseEvent.CLICK, sendEmail);
            clearFields.addEventListener(MouseEvent.CLICK, clearAllFields);
            return;
        }// end function

        public function nameClickHandler(param1:MouseEvent) : void
        {
            if (stage.displayState == StageDisplayState.FULL_SCREEN)
            {
                stage.displayState = StageDisplayState.NORMAL;
            }// end if
            responseText.text = "";
            if (Name.text == "NAME")
            {
                Name.replaceText(0, 5, "");
            }// end if
            if (Email.text.length < 1)
            {
                Email.text = "EMAIL";
            }// end if
            if (Message.text.length < 1)
            {
                Message.text = "MSG.";
            }// end if
            return;
        }// end function

        public function kickitoff(param1) : void
        {
            var _loc_2:*;
            _loc_2 = new URLLoader();
            _loc_2.load(new URLRequest(param1));
            _loc_2.addEventListener(Event.COMPLETE, xmlFinishedLoading);
            return;
        }// end function

        public function clearAllFields(param1:Event) : void
        {
            if (stage.displayState == StageDisplayState.FULL_SCREEN)
            {
                stage.displayState = StageDisplayState.NORMAL;
            }// end if
            Name.text = "NAME";
            Email.text = "EMAIL";
            Message.text = "MSG.";
            return;
        }// end function

        public function cssLoaded(param1:Event) : void
        {
            goodSheet.parseCSS(cssLoader.data);
            AddImage1(10, 10, contact.imageURL.text());
            CreateTextField(12, 245, 100, false, contact.location.text());
            CreateTextField(12, 261, 100, false, contact.address1.text());
            CreateTextField(12, 272, 100, false, contact.address2.text());
            CreateTextField(9, 332, 300, false, contact.pageName.text());
            CreateTextField(422, 27, 200, false, contact.companyName.text());
            CreateTextField(428, 46, 200, true, contact.companyDescription.text());
            CreateTextField(422, 92, 200, false, contact.details.text());
            CreateTextField(429, 112, 200, false, contact.telephone.text());
            CreateTextField(429, 125, 200, false, contact.fax.text());
            CreateTextField(429, 138, 200, false, contact.email.text());
            CreateTextField(429, 152, 200, false, contact.web.text());
            return;
        }// end function

    }
}