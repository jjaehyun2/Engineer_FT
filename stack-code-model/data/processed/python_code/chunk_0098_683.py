package flash.xml
{

    public class XMLDocument extends XMLNode
    {
        public var xmlDecl:Object = null;
        public var docTypeDecl:Object = null;
        public var idMap:Object;
        public var ignoreWhite:Boolean = false;
        private static const kNoError:int = 0;
        private static const kEndOfDocument:int = -1;
        private static const kUnterminatedCdata:int = -2;
        private static const kUnterminatedXmlDeclaration:int = -3;
        private static const kUnterminatedDoctypeDeclaration:int = -4;
        private static const kUnterminatedComment:int = -5;
        private static const kMalformedElement:int = -6;
        private static const kOutOfMemory:int = -7;
        private static const kUnterminatedAttributeValue:int = -8;
        private static const kUnterminatedElement:int = -9;
        private static const kElementNeverBegun:int = -10;

        public function XMLDocument(param1:String = null)
        {
            this.idMap = {};
            super(1, "");
            nodeName = null;
            if (param1 != null)
            {
                this.parseXML(param1);
            }
            return;
        }// end function

        public function createElement(param1:String) : XMLNode
        {
            return new XMLNode(1, param1);
        }// end function

        public function createTextNode(param1:String) : XMLNode
        {
            return new XMLNode(3, param1);
        }// end function

        override public function toString() : String
        {
            var _loc_2:* = null;
            var _loc_1:* = "";
            if (this.xmlDecl != null)
            {
                _loc_1 = _loc_1 + this.xmlDecl;
            }
            if (this.docTypeDecl != null)
            {
                _loc_1 = _loc_1 + this.docTypeDecl;
            }
            if (hasChildNodes())
            {
                _loc_2 = firstChild;
                while (_loc_2 != null)
                {
                    
                    _loc_1 = _loc_1 + _loc_2.toString();
                    _loc_2 = _loc_2.nextSibling;
                }
            }
            else
            {
                _loc_1 = _loc_1 + "<>";
            }
            return _loc_1;
        }// end function

        public function parseXML(param1:String) : void
        {
            var _loc_4:* = 0;
            var _loc_7:* = 0;
            var _loc_8:* = null;
            var _loc_9:* = null;
            var _loc_10:* = null;
            firstChild = null;
            lastChild = null;
            childNodes.splice(0);
            attributes = null;
            this.xmlDecl = null;
            this.docTypeDecl = null;
            var _loc_2:* = new XMLParser();
            _loc_2.startParse(param1, this.ignoreWhite);
            var _loc_3:* = this;
            var _loc_5:* = new XMLTag();
            var _loc_6:* = 0;
            do
            {
                
                _loc_7 = _loc_5.type;
                _loc_8 = _loc_5.value;
                if (_loc_7 === 1)
                {
                    _loc_9 = new XMLNode(1, _loc_8);
                    if (_loc_5.attrs !== null)
                    {
                        _loc_10 = _loc_5.attrs;
                        if ("id" in _loc_10)
                        {
                            this.idMap[_loc_10.id] = _loc_9;
                        }
                        _loc_9.attributes = _loc_10;
                    }
                    if (_loc_8.charCodeAt(0) == 47)
                    {
                        if (_loc_8.substr(1) === _loc_3.nodeName)
                        {
                            _loc_3 = _loc_3.parentNode;
                        }
                        else
                        {
                            _loc_6 = kElementNeverBegun;
                        }
                    }
                    else
                    {
                        _loc_3.appendChild(_loc_9);
                        if (!_loc_5.empty)
                        {
                            _loc_3 = _loc_9;
                        }
                    }
                }
                else
                {
                    if (_loc_7 !== 3)
                    {
                    }
                    if (_loc_7 === 4)
                    {
                        _loc_9 = new XMLNode(3, _loc_8);
                        _loc_3.appendChild(_loc_9);
                    }
                    else if (_loc_7 === 13)
                    {
                        if (this.xmlDecl == null)
                        {
                            this.xmlDecl = "";
                        }
                        this.xmlDecl = this.xmlDecl + ("<?" + _loc_8 + "?>");
                    }
                    else if (_loc_7 === 10)
                    {
                        this.docTypeDecl = _loc_8;
                    }
                }
                var _loc_11:* = _loc_2.getNext(_loc_5);
                _loc_4 = _loc_2.getNext(_loc_5);
            }while (_loc_11 == kNoError)
            if (_loc_4 == kEndOfDocument)
            {
                _loc_4 = kNoError;
            }
            else
            {
                _loc_6 = _loc_4;
            }
            if (_loc_3 != this)
            {
            }
            if (_loc_4 == kNoError)
            {
                _loc_6 = kUnterminatedElement;
            }
            if (_loc_6 != kNoError)
            {
                nodeType = 1;
                nextSibling = null;
                previousSibling = null;
                parentNode = null;
                firstChild = null;
                lastChild = null;
                childNodes.splice(0);
                attributes = null;
                nodeName = "";
                nodeValue = null;
                switch(_loc_6)
                {
                    case kUnterminatedCdata:
                    {
                        Error.throwError(Error, 1091);
                        break;
                    }
                    case kUnterminatedXmlDeclaration:
                    {
                        Error.throwError(Error, 1092);
                        break;
                    }
                    case kUnterminatedDoctypeDeclaration:
                    {
                        Error.throwError(Error, 1093);
                        break;
                    }
                    case kUnterminatedComment:
                    {
                        Error.throwError(Error, 1094);
                        break;
                    }
                    case kMalformedElement:
                    {
                        Error.throwError(Error, 1090);
                        break;
                    }
                    case kOutOfMemory:
                    {
                        Error.throwError(Error, 1000);
                        break;
                    }
                    case kUnterminatedAttributeValue:
                    {
                        Error.throwError(Error, 1095);
                        break;
                    }
                    case kUnterminatedElement:
                    {
                        Error.throwError(Error, 1096);
                        break;
                    }
                    case kElementNeverBegun:
                    {
                        Error.throwError(Error, 2070);
                        break;
                    }
                    default:
                    {
                        Error.throwError(Error, 2071);
                        break;
                        break;
                    }
                }
            }
            return;
        }// end function

    }
}