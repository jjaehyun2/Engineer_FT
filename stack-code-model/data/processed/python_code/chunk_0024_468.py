dynamic class tm.utils.RegExp
{
    var const = null;
    var source = null;
    var global: Boolean = false;
    var ignoreCase: Boolean = false;
    var multiline: Boolean = false;
    var lastIndex = null;
    static var _xrStatic = null;
    var _xr = null;
    static var _xp = null;
    static var _xxa = null;
    static var _xxlp = null;
    var _xq = null;
    var _xqc = null;
    static var d = null;
    static var _xiStatic = null;
    var _xi: Number = 0;
    static var _xxlm = null;
    static var _xxlc = null;
    static var _xxrc = null;
    static var lastMatch = null;
    static var leftContext = null;
    static var rightContext = null;
    static var _xa = new Array();
    static var lastParen = null;
    static var _xaStatic = new Array();
    static var $1 = null;
    static var $2 = null;
    static var $3 = null;
    static var $4 = null;
    static var $5 = null;
    static var $6 = null;
    static var $7 = null;
    static var $8 = null;
    static var $9 = null;
    static var _setString = tm.utils.RegExp.setStringMethods();
    var old_split;
    var valueOf;

    function RegExp()
    {
        if (arguments[0] != null) 
        {
            this.const = "RegExp";
            this.compile.apply(this, arguments);
        }
    }

    function invStr(sVal)
    {
        var __reg5 = sVal;
        var __reg4 = length(__reg5);
        var __reg1 = undefined;
        var __reg3 = undefined;
        var __reg6 = "";
        var __reg2 = 1;
        while (__reg2 < 255) 
        {
            __reg3 = chr(__reg2);
            __reg1 = 0;
            for (;;) 
            {
                if (!(__reg1 <= __reg4 && substring(__reg5, 1 + __reg1++, 1) != __reg3)) 
                {
                    break;
                }
            }
            if (__reg1 > __reg4) 
            {
                __reg6 = __reg6 + __reg3;
            }
            ++__reg2;
        }
        return __reg5;
    }

    function compile()
    {
        this.source = arguments[0];
        if (arguments.length > 1) 
        {
            var __reg17 = (arguments[1] + "").toLowerCase();
            var __reg11 = 0;
            while (__reg11 < length(__reg17)) 
            {
                if (substring(__reg17, __reg11 + 1, 1) == "g") 
                {
                    this.global = true;
                }
                if (substring(__reg17, __reg11 + 1, 1) == "i") 
                {
                    this.ignoreCase = true;
                }
                if (substring(__reg17, __reg11 + 1, 1) == "m") 
                {
                    this.multiline = true;
                }
                ++__reg11;
            }
        }
        if (arguments.length < 3) 
        {
            __reg20 = true;
            tm.utils.RegExp._xrStatic = 1;
            __reg11 = 0;
        }
        else 
        {
            var __reg20 = false;
            this._xr = tm.utils.RegExp._xrStatic++;
            __reg11 = arguments[2];
        }
        this.lastIndex = 0;
        var __reg9 = this.source;
        var __reg21 = undefined;
        var __reg14 = length(__reg9);
        var __reg6 = [];
        var __reg4 = 0;
        var __reg5 = undefined;
        var __reg8 = false;
        var __reg16 = undefined;
        var __reg15 = undefined;
        var __reg18 = false;
        var __reg19 = undefined;
        __reg11 = __reg11;
        while (__reg11 < __reg14) 
        {
            var __reg3 = substring(__reg9, __reg11 + 1, 1);
            if (__reg3 == "\\") 
            {
                ++__reg11;
                __reg19 = false;
                __reg3 = substring(__reg9, __reg11 + 1, 1);
            }
            else 
            {
                __reg19 = true;
            }
            var __reg13 = substring(__reg9, __reg11 + 2, 1);
            __reg6[__reg4] = new Object();
            __reg6[__reg4].t = 0;
            __reg6[__reg4].a = 0;
            __reg6[__reg4].b = 999;
            __reg6[__reg4].c = -10;
            if (__reg19) 
            {
                if (__reg3 == "(") 
                {
                    __reg21 = new tm.utils.RegExp(__reg9, this.ignoreCase ? "gi" : "g", __reg11 + 1);
                    __reg11 = tm.utils.RegExp._xiStatic;
                    __reg6[__reg4].t = 3;
                    __reg3 = __reg21;
                    __reg13 = substring(__reg9, __reg11 + 2, 1);
                    if (__reg13 == "*") 
                    {
                        __reg6[__reg4].s = __reg3;
                        ++__reg4;
                        ++__reg11;
                    }
                    else 
                    {
                        if (__reg13 == "?") 
                        {
                            __reg6[__reg4].s = __reg3;
                            __reg6[__reg4].b = 1;
                            ++__reg4;
                            ++__reg11;
                        }
                        else 
                        {
                            if (__reg13 == "+") 
                            {
                                __reg6[__reg4].s = __reg3;
                                __reg6[__reg4].a = 1;
                                ++__reg4;
                                ++__reg11;
                            }
                            else 
                            {
                                if (__reg13 == "{") 
                                {
                                    __reg12 = false;
                                    __reg7 = 0;
                                    __reg8 = "";
                                    ++__reg11;
                                    while (__reg11 + 1 < __reg14 && (__reg5 = substring(__reg9, 2 + __reg11++, 1)) != "}") 
                                    {
                                        if (!__reg12 && __reg5 == ",") 
                                        {
                                            __reg12 = true;
                                            __reg7 = Number(__reg8);
                                            __reg7 = Math.floor(isNaN(__reg7) ? 0 : __reg7);
                                            if (__reg7 < 0) 
                                            {
                                                __reg7 = 0;
                                            }
                                            __reg8 = "";
                                        }
                                        else 
                                        {
                                            __reg8 = __reg8 + __reg5;
                                        }
                                    }
                                    __reg10 = Number(__reg8);
                                    __reg10 = Math.floor(isNaN(__reg10) ? 0 : __reg10);
                                    if (__reg10 < 1) 
                                    {
                                        __reg10 = 999;
                                    }
                                    if (__reg10 < __reg7) 
                                    {
                                        __reg10 = __reg7;
                                    }
                                    __reg6[__reg4].s = __reg3;
                                    __reg6[__reg4].b = __reg10;
                                    __reg6[__reg4].a = __reg12 ? __reg7 : __reg10;
                                    ++__reg4;
                                }
                                else 
                                {
                                    __reg6[__reg4].s = __reg3;
                                    __reg6[__reg4].a = 1;
                                    __reg6[__reg4].b = 1;
                                    ++__reg4;
                                }
                            }
                        }
                    }
                }
                else 
                {
                    if (!__reg20 && __reg3 == ")") 
                    {
                        break;
                    }
                    if (__reg3 == "^") 
                    {
                        if (__reg4 == 0 || __reg6[__reg4 - 1].t == 7) 
                        {
                            __reg6[__reg4].t = 9;
                            __reg6[__reg4].a = 1;
                            __reg6[__reg4].b = 1;
                            ++__reg4;
                        }
                    }
                    else 
                    {
                        if (__reg3 == "$") 
                        {
                            if (__reg20) 
                            {
                                __reg18 = true;
                            }
                        }
                        else 
                        {
                            if (__reg3 == "[") 
                            {
                                ++__reg11;
                                if (__reg13 == "^") 
                                {
                                    __reg6[__reg4].t = 2;
                                    ++__reg11;
                                }
                                else 
                                {
                                    __reg6[__reg4].t = 1;
                                }
                                __reg3 = "";
                                __reg8 = false;
                                while (__reg11 < __reg14 && (__reg5 = substring(__reg9, 1 + __reg11++, 1)) != "]") 
                                {
                                    if (__reg8) 
                                    {
                                        __reg5 != "\\";
                                        __reg15 = __reg5 == "\\" ? (__reg5 == "b" ? "" : substring(__reg9, 1 + __reg11++, 1)) : __reg5;
                                        __reg16 = ord(substring(__reg3, length(__reg3), 1)) + 1;
                                        while (__reg15 >= (__reg5 = chr(__reg16++))) 
                                        {
                                            __reg3 = __reg3 + __reg5;
                                        }
                                        __reg8 = false;
                                    }
                                    else 
                                    {
                                        if (__reg5 == "-" && length(__reg3) > 0) 
                                        {
                                            __reg8 = true;
                                        }
                                        else 
                                        {
                                            if (__reg5 == "\\") 
                                            {
                                                __reg5 = substring(__reg9, 1 + __reg11++, 1);
                                                if (__reg5 == "d") 
                                                {
                                                    __reg3 = __reg3 + "0123456789";
                                                }
                                                else 
                                                {
                                                    if (__reg5 == "D") 
                                                    {
                                                        __reg3 = __reg3 + this.invStr("0123456789");
                                                    }
                                                    else 
                                                    {
                                                        if (__reg5 == "s") 
                                                        {
                                                            __reg3 = __reg3 + " \n\r\t\\";
                                                        }
                                                        else 
                                                        {
                                                            if (__reg5 == "S") 
                                                            {
                                                                __reg3 = __reg3 + this.invStr(" \n\r\t\\");
                                                            }
                                                            else 
                                                            {
                                                                if (__reg5 == "w") 
                                                                {
                                                                    __reg3 = __reg3 + "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_";
                                                                }
                                                                else 
                                                                {
                                                                    if (__reg5 == "W") 
                                                                    {
                                                                        __reg3 = __reg3 + this.invStr("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_");
                                                                    }
                                                                    else 
                                                                    {
                                                                        if (__reg5 == "b") 
                                                                        {
                                                                            __reg3 = __reg3 + "";
                                                                        }
                                                                        else 
                                                                        {
                                                                            if (__reg5 == "\\") 
                                                                            {
                                                                                __reg3 = __reg3 + __reg5;
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                            else 
                                            {
                                                __reg3 = __reg3 + __reg5;
                                            }
                                        }
                                    }
                                }
                                if (__reg8) 
                                {
                                    __reg3 = __reg3 + "-";
                                }
                                --__reg11;
                                __reg13 = substring(__reg9, __reg11 + 2, 1);
                                if (__reg13 == "*") 
                                {
                                    __reg6[__reg4].s = __reg3;
                                    ++__reg4;
                                    ++__reg11;
                                }
                                else 
                                {
                                    if (__reg13 == "?") 
                                    {
                                        __reg6[__reg4].s = __reg3;
                                        __reg6[__reg4].b = 1;
                                        ++__reg4;
                                        ++__reg11;
                                    }
                                    else 
                                    {
                                        if (__reg13 == "+") 
                                        {
                                            __reg6[__reg4].s = __reg3;
                                            __reg6[__reg4].a = 1;
                                            ++__reg4;
                                            ++__reg11;
                                        }
                                        else 
                                        {
                                            if (__reg13 == "{") 
                                            {
                                                __reg12 = false;
                                                __reg7 = 0;
                                                __reg8 = "";
                                                ++__reg11;
                                                while (__reg11 + 1 < __reg14 && (__reg5 = substring(__reg9, 2 + __reg11++, 1)) != "}") 
                                                {
                                                    if (!__reg12 && __reg5 == ",") 
                                                    {
                                                        __reg12 = true;
                                                        __reg7 = Number(__reg8);
                                                        __reg7 = Math.floor(isNaN(__reg7) ? 0 : __reg7);
                                                        if (__reg7 < 0) 
                                                        {
                                                            __reg7 = 0;
                                                        }
                                                        __reg8 = "";
                                                    }
                                                    else 
                                                    {
                                                        __reg8 = __reg8 + __reg5;
                                                    }
                                                }
                                                __reg10 = Number(__reg8);
                                                __reg10 = Math.floor(isNaN(__reg10) ? 0 : __reg10);
                                                if (__reg10 < 1) 
                                                {
                                                    __reg10 = 999;
                                                }
                                                if (__reg10 < __reg7) 
                                                {
                                                    __reg10 = __reg7;
                                                }
                                                __reg6[__reg4].s = __reg3;
                                                __reg6[__reg4].b = __reg10;
                                                __reg6[__reg4].a = __reg12 ? __reg7 : __reg10;
                                                ++__reg4;
                                            }
                                            else 
                                            {
                                                __reg6[__reg4].s = __reg3;
                                                __reg6[__reg4].a = 1;
                                                __reg6[__reg4].b = 1;
                                                ++__reg4;
                                            }
                                        }
                                    }
                                }
                            }
                            else 
                            {
                                if (__reg3 == "|") 
                                {
                                    if (__reg18) 
                                    {
                                        __reg6[__reg4].t = 10;
                                        __reg6[__reg4].a = 1;
                                        __reg6[__reg4].b = 1;
                                        ++__reg4;
                                        __reg6[__reg4] = new Object();
                                        __reg18 = false;
                                    }
                                    __reg6[__reg4].t = 7;
                                    __reg6[__reg4].a = 1;
                                    __reg6[__reg4].b = 1;
                                    ++__reg4;
                                }
                                else 
                                {
                                    if (__reg3 == ".") 
                                    {
                                        __reg6[__reg4].t = 2;
                                        __reg3 = "\n";
                                        if (__reg13 == "*") 
                                        {
                                            __reg6[__reg4].s = __reg3;
                                            ++__reg4;
                                            ++__reg11;
                                        }
                                        else 
                                        {
                                            if (__reg13 == "?") 
                                            {
                                                __reg6[__reg4].s = __reg3;
                                                __reg6[__reg4].b = 1;
                                                ++__reg4;
                                                ++__reg11;
                                            }
                                            else 
                                            {
                                                if (__reg13 == "+") 
                                                {
                                                    __reg6[__reg4].s = __reg3;
                                                    __reg6[__reg4].a = 1;
                                                    ++__reg4;
                                                    ++__reg11;
                                                }
                                                else 
                                                {
                                                    if (__reg13 == "{") 
                                                    {
                                                        __reg12 = false;
                                                        __reg7 = 0;
                                                        __reg8 = "";
                                                        ++__reg11;
                                                        while (__reg11 + 1 < __reg14 && (__reg5 = substring(__reg9, 2 + __reg11++, 1)) != "}") 
                                                        {
                                                            if (!__reg12 && __reg5 == ",") 
                                                            {
                                                                __reg12 = true;
                                                                __reg7 = Number(__reg8);
                                                                __reg7 = Math.floor(isNaN(__reg7) ? 0 : __reg7);
                                                                if (__reg7 < 0) 
                                                                {
                                                                    __reg7 = 0;
                                                                }
                                                                __reg8 = "";
                                                            }
                                                            else 
                                                            {
                                                                __reg8 = __reg8 + __reg5;
                                                            }
                                                        }
                                                        __reg10 = Number(__reg8);
                                                        __reg10 = Math.floor(isNaN(__reg10) ? 0 : __reg10);
                                                        if (__reg10 < 1) 
                                                        {
                                                            __reg10 = 999;
                                                        }
                                                        if (__reg10 < __reg7) 
                                                        {
                                                            __reg10 = __reg7;
                                                        }
                                                        __reg6[__reg4].s = __reg3;
                                                        __reg6[__reg4].b = __reg10;
                                                        __reg6[__reg4].a = __reg12 ? __reg7 : __reg10;
                                                        ++__reg4;
                                                    }
                                                    else 
                                                    {
                                                        __reg6[__reg4].s = __reg3;
                                                        __reg6[__reg4].a = 1;
                                                        __reg6[__reg4].b = 1;
                                                        ++__reg4;
                                                    }
                                                }
                                            }
                                        }
                                    }
                                    else 
                                    {
                                        if (!(__reg3 == "*" || __reg3 == "?" || __reg3 == "+")) 
                                        {
                                            if (__reg13 == "*") 
                                            {
                                                __reg6[__reg4].s = __reg3;
                                                ++__reg4;
                                                ++__reg11;
                                            }
                                            else 
                                            {
                                                if (__reg13 == "?") 
                                                {
                                                    __reg6[__reg4].s = __reg3;
                                                    __reg6[__reg4].b = 1;
                                                    ++__reg4;
                                                    ++__reg11;
                                                }
                                                else 
                                                {
                                                    if (__reg13 == "+") 
                                                    {
                                                        __reg6[__reg4].s = __reg3;
                                                        __reg6[__reg4].a = 1;
                                                        ++__reg4;
                                                        ++__reg11;
                                                    }
                                                    else 
                                                    {
                                                        if (__reg13 == "{") 
                                                        {
                                                            __reg12 = false;
                                                            __reg7 = 0;
                                                            __reg8 = "";
                                                            ++__reg11;
                                                            while (__reg11 + 1 < __reg14 && (__reg5 = substring(__reg9, 2 + __reg11++, 1)) != "}") 
                                                            {
                                                                if (!__reg12 && __reg5 == ",") 
                                                                {
                                                                    __reg12 = true;
                                                                    __reg7 = Number(__reg8);
                                                                    __reg7 = Math.floor(isNaN(__reg7) ? 0 : __reg7);
                                                                    if (__reg7 < 0) 
                                                                    {
                                                                        __reg7 = 0;
                                                                    }
                                                                    __reg8 = "";
                                                                }
                                                                else 
                                                                {
                                                                    __reg8 = __reg8 + __reg5;
                                                                }
                                                            }
                                                            __reg10 = Number(__reg8);
                                                            __reg10 = Math.floor(isNaN(__reg10) ? 0 : __reg10);
                                                            if (__reg10 < 1) 
                                                            {
                                                                __reg10 = 999;
                                                            }
                                                            if (__reg10 < __reg7) 
                                                            {
                                                                __reg10 = __reg7;
                                                            }
                                                            __reg6[__reg4].s = __reg3;
                                                            __reg6[__reg4].b = __reg10;
                                                            __reg6[__reg4].a = __reg12 ? __reg7 : __reg10;
                                                            ++__reg4;
                                                        }
                                                        else 
                                                        {
                                                            __reg6[__reg4].s = __reg3;
                                                            __reg6[__reg4].a = 1;
                                                            __reg6[__reg4].b = 1;
                                                            ++__reg4;
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            else 
            {
                if (__reg3 >= "1" && __reg3 <= "9") 
                {
                    __reg6[__reg4].t = 4;
                }
                else 
                {
                    if (__reg3 == "b") 
                    {
                        __reg6[__reg4].t = 1;
                        __reg3 = "--wb--";
                    }
                    else 
                    {
                        if (__reg3 == "B") 
                        {
                            __reg6[__reg4].t = 2;
                            __reg3 = "--wb--";
                        }
                        else 
                        {
                            if (__reg3 == "d") 
                            {
                                __reg6[__reg4].t = 1;
                                __reg3 = "0123456789";
                            }
                            else 
                            {
                                if (__reg3 == "D") 
                                {
                                    __reg6[__reg4].t = 2;
                                    __reg3 = "0123456789";
                                }
                                else 
                                {
                                    if (__reg3 == "s") 
                                    {
                                        __reg6[__reg4].t = 1;
                                        __reg3 = " \n\r\t\\";
                                    }
                                    else 
                                    {
                                        if (__reg3 == "S") 
                                        {
                                            __reg6[__reg4].t = 2;
                                            __reg3 = " \n\r\t\\";
                                        }
                                        else 
                                        {
                                            if (__reg3 == "w") 
                                            {
                                                __reg6[__reg4].t = 1;
                                                __reg3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_";
                                            }
                                            else 
                                            {
                                                if (__reg3 == "W") 
                                                {
                                                    __reg6[__reg4].t = 2;
                                                    __reg3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_";
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                if (__reg13 == "*") 
                {
                    __reg6[__reg4].s = __reg3;
                    ++__reg4;
                    ++__reg11;
                }
                else 
                {
                    if (__reg13 == "?") 
                    {
                        __reg6[__reg4].s = __reg3;
                        __reg6[__reg4].b = 1;
                        ++__reg4;
                        ++__reg11;
                    }
                    else 
                    {
                        if (__reg13 == "+") 
                        {
                            __reg6[__reg4].s = __reg3;
                            __reg6[__reg4].a = 1;
                            ++__reg4;
                            ++__reg11;
                        }
                        else 
                        {
                            if (__reg13 == "{") 
                            {
                                var __reg12 = false;
                                var __reg7 = 0;
                                __reg8 = "";
                                ++__reg11;
                                while (__reg11 + 1 < __reg14 && (__reg5 = substring(__reg9, 2 + __reg11++, 1)) != "}") 
                                {
                                    if (!__reg12 && __reg5 == ",") 
                                    {
                                        __reg12 = true;
                                        __reg7 = Number(__reg8);
                                        __reg7 = Math.floor(isNaN(__reg7) ? 0 : __reg7);
                                        if (__reg7 < 0) 
                                        {
                                            __reg7 = 0;
                                        }
                                        __reg8 = "";
                                    }
                                    else 
                                    {
                                        __reg8 = __reg8 + __reg5;
                                    }
                                }
                                var __reg10 = Number(__reg8);
                                __reg10 = Math.floor(isNaN(__reg10) ? 0 : __reg10);
                                if (__reg10 < 1) 
                                {
                                    __reg10 = 999;
                                }
                                if (__reg10 < __reg7) 
                                {
                                    __reg10 = __reg7;
                                }
                                __reg6[__reg4].s = __reg3;
                                __reg6[__reg4].b = __reg10;
                                __reg6[__reg4].a = __reg12 ? __reg7 : __reg10;
                                ++__reg4;
                            }
                            else 
                            {
                                __reg6[__reg4].s = __reg3;
                                __reg6[__reg4].a = 1;
                                __reg6[__reg4].b = 1;
                                ++__reg4;
                            }
                        }
                    }
                }
            }
            ++__reg11;
        }
        if (__reg20 && __reg18) 
        {
            __reg6[__reg4] = new Object();
            __reg6[__reg4].t = 10;
            __reg6[__reg4].a = 1;
            __reg6[__reg4].b = 1;
            ++__reg4;
        }
        if (!__reg20) 
        {
            tm.utils.RegExp._xiStatic = __reg11;
            this.source = substring(__reg9, arguments[2] + 1, __reg11 - arguments[2]);
        }
        if (tm.utils.RegExp.d) 
        {
            __reg11 = 0;
            while (__reg11 < __reg4) 
            {
                trace("xr" + this._xr + " " + __reg6[__reg11].t + " : " + __reg6[__reg11].a + " : " + __reg6[__reg11].b + " : " + __reg6[__reg11].s);
                ++__reg11;
            }
        }
        this._xq = __reg6;
        this._xqc = __reg4;
        tm.utils.RegExp._xp = 0;
    }

    function test()
    {
        if (tm.utils.RegExp._xp++ == 0) 
        {
            tm.utils.RegExp._xxa = [];
            tm.utils.RegExp._xxlp = 0;
        }
        var __reg11 = arguments[0] + "";
        var __reg15 = undefined;
        var __reg4 = this._xq;
        var __reg18 = this._xqc;
        var __reg14 = undefined;
        var __reg7 = undefined;
        var __reg8 = undefined;
        var __reg9 = undefined;
        var __reg13 = undefined;
        var __reg12 = length(__reg11);
        var __reg5 = this.global ? this.lastIndex : 0;
        var __reg21 = __reg5;
        var __reg19 = __reg11;
        if (this.ignoreCase) 
        {
            __reg11 = __reg11.toLowerCase();
        }
        var __reg16 = new Object();
        __reg16.i = -1;
        var __reg3 = -1;
        while (__reg3 < __reg18 - 1) 
        {
            ++__reg3;
            if (tm.utils.RegExp.d) 
            {
                trace("New section started at i=" + __reg3);
            }
            __reg5 = __reg21;
            __reg14 = __reg3;
            __reg4[__reg14].c = -10;
            var __reg20 = false;
            while (__reg3 > __reg14 || __reg5 < __reg12 + 1) 
            {
                if (__reg4[__reg3].t == 7) 
                {
                    break;
                }
                else 
                {
                    if (__reg4[__reg3].t == 9) 
                    {
                        ++__reg3;
                        if (__reg3 == __reg14 + 1) 
                        {
                            var __reg17 = true;
                            __reg14 = __reg3;
                        }
                        __reg4[__reg14].c = -10;
                        continue;
                    }
                    if (__reg16.i >= 0 && __reg5 >= __reg16.i) 
                    {
                        break;
                    }
                    if (__reg4[__reg3].c == -10) 
                    {
                        if (tm.utils.RegExp.d) 
                        {
                            trace("Lookup #" + __reg3 + " at index " + __reg5 + " for \\\\\\\\\\\\\\\\\'" + __reg4[__reg3].s + "\\\\\\\\\\\\\\\\\' type " + __reg4[__reg3].t);
                        }
                        var __reg6 = 0;
                        __reg4[__reg3].i = __reg5;
                        if (__reg4[__reg3].t == 0) 
                        {
                            __reg7 = this.ignoreCase ? __reg4[__reg3].s.toLowerCase() : __reg4[__reg3].s;
                            while (__reg6 < __reg4[__reg3].b && __reg5 < __reg12) 
                            {
                                if (substring(__reg11, 1 + __reg5, 1) == __reg7) 
                                {
                                    ++__reg6;
                                    ++__reg5;
                                }
                                else 
                                {
                                    break;
                                }
                            }
                        }
                        else 
                        {
                            if (__reg4[__reg3].t == 1) 
                            {
                                if (__reg4[__reg3].s == "--wb--") 
                                {
                                    __reg4[__reg3].a = 1;
                                    if (__reg5 > 0 && __reg5 < __reg12) 
                                    {
                                        __reg9 = substring(__reg11, __reg5, 1);
                                        if (__reg9 == " " || __reg9 == "\\\\\\\\\\\\\\\\n") 
                                        {
                                            __reg6 = 1;
                                        }
                                        if (__reg6 == 0) 
                                        {
                                            __reg9 = substring(__reg11, 1 + __reg5, 1);
                                            if (__reg9 == " " || __reg9 == "\\\\\\\\\\\\\\\\n") 
                                            {
                                                __reg6 = 1;
                                            }
                                        }
                                    }
                                    else 
                                    {
                                        __reg6 = 1;
                                    }
                                }
                                else 
                                {
                                    __reg7 = this.ignoreCase ? __reg4[__reg3].s.toLowerCase() : __reg4[__reg3].s;
                                    __reg8 = length(__reg7);
                                    __reg10 = undefined;
                                    while (__reg6 < __reg4[__reg3].b && __reg5 < __reg12) 
                                    {
                                        __reg9 = substring(__reg11, 1 + __reg5, 1);
                                        __reg10 = 0;
                                        for (;;) 
                                        {
                                            if (!(__reg10 <= __reg8 && substring(__reg7, 1 + __reg10++, 1) != __reg9)) 
                                            {
                                                break;
                                            }
                                        }
                                        if (__reg10 <= __reg8) 
                                        {
                                            ++__reg6;
                                            ++__reg5;
                                        }
                                        else 
                                        {
                                            break;
                                        }
                                    }
                                }
                            }
                            else 
                            {
                                if (__reg4[__reg3].t == 2) 
                                {
                                    __reg7 = this.ignoreCase ? __reg4[__reg3].s.toLowerCase() : __reg4[__reg3].s;
                                    __reg8 = length(__reg7);
                                    if (__reg4[__reg3].s == "--wb--") 
                                    {
                                        __reg4[__reg3].a = 1;
                                        if (__reg5 > 0 && __reg5 < __reg12) 
                                        {
                                            __reg9 = substring(__reg11, __reg5, 1);
                                            __reg13 = substring(__reg11, 1 + __reg5, 1);
                                            if (__reg9 != " " && __reg9 != "\\\\\\\\\\\\\\\\n" && __reg13 != " " && __reg13 != "\\\\\\\\\\\\\\\\n") 
                                            {
                                                __reg6 = 1;
                                            }
                                        }
                                        else 
                                        {
                                            __reg6 = 0;
                                        }
                                    }
                                    else 
                                    {
                                        while (__reg6 < __reg4[__reg3].b && __reg5 < __reg12) 
                                        {
                                            __reg9 = substring(__reg11, 1 + __reg5, 1);
                                            var __reg10 = 0;
                                            for (;;) 
                                            {
                                                if (!(__reg10 <= __reg8 && substring(__reg7, 1 + __reg10++, 1) != __reg9)) 
                                                {
                                                    break;
                                                }
                                            }
                                            if (__reg10 <= __reg8) 
                                            {
                                                break;
                                            }
                                            ++__reg6;
                                            ++__reg5;
                                        }
                                    }
                                }
                                else 
                                {
                                    if (__reg4[__reg3].t == 10) 
                                    {
                                        __reg13 = substring(__reg11, 1 + __reg5, 1);
                                        __reg6 = this.multiline && __reg13 == "\\\\\\\\\\\\\\\\n" || __reg13 == "\\\\\\\\\\\\\\\\r" || __reg5 == __reg12 ? 1 : 0;
                                    }
                                    else 
                                    {
                                        if (__reg4[__reg3].t == 3) 
                                        {
                                            __reg15 = __reg4[__reg3].s;
                                            __reg4[__reg3].ix = [];
                                            __reg4[__reg3].ix[__reg6] = __reg5;
                                            __reg15.lastIndex = __reg5;
                                            while (__reg6 < __reg4[__reg3].b && __reg15.test(__reg19)) 
                                            {
                                                __reg8 = length(tm.utils.RegExp._xxlm);
                                                if (__reg8 > 0) 
                                                {
                                                    __reg5 = __reg5 + __reg8;
                                                    ++__reg6;
                                                    __reg4[__reg3].ix[__reg6] = __reg5;
                                                }
                                                else 
                                                {
                                                    __reg6 = __reg4[__reg3].a;
                                                    __reg4[__reg3].ix[__reg6 - 1] = __reg5;
                                                    break;
                                                }
                                            }
                                            if (__reg6 == 0) 
                                            {
                                                tm.utils.RegExp._xxlm = "";
                                            }
                                            if (__reg15._xr > tm.utils.RegExp._xxlp) 
                                            {
                                                tm.utils.RegExp._xxlp = __reg15._xr;
                                            }
                                            tm.utils.RegExp._xxa[Number(__reg15._xr)] = tm.utils.RegExp._xxlm;
                                        }
                                        else 
                                        {
                                            if (__reg4[__reg3].t == 4) 
                                            {
                                                if (tm.utils.RegExp._xp >= (__reg7 = Number(__reg4[__reg3].s))) 
                                                {
                                                    __reg7 = tm.utils.RegExp._xxa[__reg7];
                                                    __reg7 = this.ignoreCase ? __reg7.toLowerCase() : __reg7;
                                                    __reg8 = length(__reg7);
                                                    __reg4[__reg3].ix = [];
                                                    __reg4[__reg3].ix[__reg6] = __reg5;
                                                    if (__reg8 > 0) 
                                                    {
                                                        while (__reg6 < __reg4[__reg3].b && __reg5 < __reg12) 
                                                        {
                                                            if (substring(__reg11, 1 + __reg5, __reg8) == __reg7) 
                                                            {
                                                                ++__reg6;
                                                                __reg5 = __reg5 + __reg8;
                                                                __reg4[__reg3].ix[__reg6] = __reg5;
                                                            }
                                                            else 
                                                            {
                                                                break;
                                                            }
                                                        }
                                                    }
                                                    else 
                                                    {
                                                        __reg6 = 0;
                                                        __reg4[__reg3].a = 0;
                                                    }
                                                }
                                                else 
                                                {
                                                    __reg7 = chr(__reg7);
                                                    __reg4[__reg3].ix = [];
                                                    __reg4[__reg3].ix[__reg6] = __reg5;
                                                    while (__reg6 < __reg4[__reg3].b && __reg5 < __reg12) 
                                                    {
                                                        if (substring(__reg11, 1 + __reg5, 1) == __reg7) 
                                                        {
                                                            ++__reg6;
                                                            ++__reg5;
                                                            __reg4[__reg3].ix[__reg6] = __reg5;
                                                        }
                                                        else 
                                                        {
                                                            break;
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                        __reg4[__reg3].c = __reg6;
                        if (tm.utils.RegExp.d) 
                        {
                            trace("   " + __reg6 + " matches found");
                        }
                    }
                    if (__reg4[__reg3].c < __reg4[__reg3].a) 
                    {
                        if (tm.utils.RegExp.d) 
                        {
                            trace("   not enough matches");
                        }
                        if (__reg3 > __reg14) 
                        {
                            --__reg3;
                            --__reg4[__reg3].c;
                            if (__reg4[__reg3].c >= 0) 
                            {
                                __reg5 = __reg4[__reg3].t == 3 || __reg4[__reg3].t == 4 ? __reg4[__reg3].ix[__reg4[__reg3].c] : __reg4[__reg3].i + __reg4[__reg3].c;
                            }
                            if (tm.utils.RegExp.d) 
                            {
                                trace("Retreat to #" + __reg3 + " c=" + __reg4[__reg3].c + " index=" + __reg5);
                            }
                        }
                        else 
                        {
                            if (tm.utils.RegExp._xp > 1) 
                            {
                                break;
                            }
                            if (__reg17) 
                            {
                                if (this.multiline) 
                                {
                                    while (__reg5 <= __reg12) 
                                    {
                                        __reg13 = substring(__reg11, 1 + __reg5++, 1);
                                        if (__reg13 == "\\\\\\\\\\\\\\\\n" || __reg13 == "\\\\\\\\\\\\\\\\r") 
                                        {
                                            break;
                                        }
                                    }
                                    __reg4[__reg3].c = -10;
                                }
                                else 
                                {
                                    break;
                                }
                            }
                            else 
                            {
                                ++__reg5;
                                __reg4[__reg3].c = -10;
                            }
                        }
                    }
                    else 
                    {
                        if (tm.utils.RegExp.d) 
                        {
                            trace("   enough matches!");
                        }
                        ++__reg3;
                        if (__reg3 == __reg18 || __reg4[__reg3].t == 7) 
                        {
                            if (tm.utils.RegExp.d) 
                            {
                                trace("Saving better result: r.i = q[" + __reg14 + "].i = " + __reg4[__reg14].i);
                            }
                            __reg16.i = __reg4[__reg14].i;
                            __reg16.li = __reg5;
                            break;
                        }
                        __reg4[__reg3].c = -10;
                    }
                }
            }
            while (__reg3 < __reg18 && __reg4[__reg3].t != 7) 
            {
                ++__reg3;
            }
        }
        if (__reg16.i < 0) 
        {
            this.lastIndex = 0;
            if (tm.utils.RegExp._xp-- == 1) 
            {
                tm.utils.RegExp._xxa = [];
                tm.utils.RegExp._xxlp = 0;
            }
            return false;
            return;
        }
        __reg5 = __reg16.li;
        this._xi = __reg16.i;
        tm.utils.RegExp._xxlm = substring(__reg19, __reg16.i + 1, __reg5 - __reg16.i);
        tm.utils.RegExp._xxlc = substring(__reg19, 1, __reg16.i);
        tm.utils.RegExp._xxrc = substring(__reg19, __reg5 + 1, __reg12 - __reg5);
        if (__reg5 == __reg16.i) 
        {
            ++__reg5;
        }
        this.lastIndex = __reg5;
        if (tm.utils.RegExp._xp-- == 1) 
        {
            tm.utils.RegExp.lastMatch = tm.utils.RegExp._xxlm;
            tm.utils.RegExp.leftContext = tm.utils.RegExp._xxlc;
            tm.utils.RegExp.rightContext = tm.utils.RegExp._xxrc;
            tm.utils.RegExp._xaStatic = tm.utils.RegExp._xxa;
            tm.utils.RegExp.lastParen = tm.utils.RegExp._xxa[Number(tm.utils.RegExp._xxlp)];
            __reg3 = 1;
            while (__reg3 < 10) 
            {
                tm.utils.RegExp["$" + __reg3] = tm.utils.RegExp._xaStatic[Number(__reg3)];
                ++__reg3;
            }
        }
        return true;
    }

    function exec()
    {
        var __reg5 = arguments[0] + "";
        if (__reg5 == "") 
        {
            return false;
        }
        var __reg6 = this.test(__reg5);
        if (__reg6) 
        {
            __reg7 = new Array();
            __reg7.index = this._xi;
            __reg7.input = __reg5;
            __reg7[0] = tm.utils.RegExp.lastMatch;
            var __reg4 = tm.utils.RegExp._xaStatic.length;
            var __reg3 = 1;
            while (__reg3 < __reg4) 
            {
                __reg7[__reg3] = tm.utils.RegExp._xaStatic[Number(__reg3)];
                ++__reg3;
            }
        }
        else 
        {
            var __reg7 = null;
        }
        return __reg7;
    }

    static function setStringMethods()
    {
        if (String.prototype.match == undefined) 
        {
            String.prototype.match = function ()
            {
                if (typeof arguments[0] != "object") 
                {
                    return null;
                }
                if (arguments[0].const != "RegExp") 
                {
                    return null;
                }
                var __reg3 = arguments[0];
                var __reg5 = this.valueOf();
                var __reg6 = 0;
                var __reg4 = 0;
                if (__reg3.global) 
                {
                    __reg3.lastIndex = 0;
                    while (__reg3.test(__reg5)) 
                    {
                        if (__reg4 == 0) 
                        {
                            __reg7 = new Array();
                        }
                        __reg7[__reg4++] = tm.utils.RegExp.lastMatch;
                        __reg6 = __reg3.lastIndex;
                    }
                    __reg3.lastIndex = __reg6;
                }
                else 
                {
                    var __reg7 = __reg3.exec(__reg5);
                    ++__reg4;
                }
                return __reg4 == 0 ? null : __reg7;
            }
            ;
            String.prototype.replace = function ()
            {
                if (typeof arguments[0] != "object") 
                {
                    return null;
                }
                if (arguments[0].const != "RegExp") 
                {
                    return null;
                }
                var __reg8 = arguments[0];
                var __reg7 = arguments[1] + "";
                this;
                var __reg12 = "";
                __reg8.lastIndex = 0;
                if (__reg8.global) 
                {
                    var __reg13 = 0;
                    var __reg10 = 0;
                    while (__reg8.test(this)) 
                    {
                        var __reg5 = 0;
                        var __reg9 = length(__reg7);
                        var __reg3 = "";
                        var __reg6 = "";
                        var __reg4 = "";
                        while (__reg5 < __reg9) 
                        {
                            __reg3 = substring(__reg7, 1 + __reg5++, 1);
                            if (__reg3 == "$" && __reg6 != "\\") 
                            {
                                __reg3 = substring(__reg7, 1 + __reg5++, 1);
                                if (isNaN(Number(__reg3)) || Number(__reg3) > 9) 
                                {
                                    __reg4 = __reg4 + ("$" + __reg3);
                                }
                                else 
                                {
                                    __reg4 = __reg4 + tm.utils.RegExp._xaStatic[Number(__reg3)];
                                }
                            }
                            else 
                            {
                                __reg4 = __reg4 + __reg3;
                            }
                            __reg6 = __reg3;
                        }
                        __reg12 = __reg12 + (substring(this, __reg10 + 1, __reg8._xi - __reg10) + __reg4);
                        __reg10 = __reg8._xi + length(tm.utils.RegExp.lastMatch);
                        __reg13 = __reg8.lastIndex;
                    }
                    __reg8.lastIndex = __reg13;
                }
                else 
                {
                    if (__reg8.test(this)) 
                    {
                        __reg12 = __reg12 + (tm.utils.RegExp.leftContext + __reg7);
                    }
                }
                __reg12 = __reg12 + (__reg8.lastIndex == 0 ? this : tm.utils.RegExp.rightContext);
                return __reg12;
            }
            ;
            String.prototype.search = function ()
            {
                if (typeof arguments[0] != "object") 
                {
                    return null;
                }
                if (arguments[0].const != "RegExp") 
                {
                    return null;
                }
                var __reg3 = arguments[0];
                this;
                __reg3.lastIndex = 0;
                var __reg4 = __reg3.test(this);
                return __reg4 ? __reg3._xi : -1;
            }
            ;
            String.prototype.old_split = String.prototype.split;
            String.prototype.split = function ()
            {
                if (typeof arguments[0] == "object" && arguments[0].const == "RegExp") 
                {
                    var __reg3 = arguments[0];
                    var __reg8 = arguments[1] == null ? 9999 : Number(arguments[1]);
                    if (isNaN(__reg8)) 
                    {
                        __reg8 = 9999;
                    }
                    this;
                    var __reg9 = new Array();
                    var __reg5 = 0;
                    var __reg11 = __reg3.global;
                    __reg3.global = true;
                    __reg3.lastIndex = 0;
                    var __reg7 = 0;
                    var __reg10 = 0;
                    var __reg4 = 0;
                    while (__reg5 < __reg8 && __reg3.test(this)) 
                    {
                        if (__reg3._xi != __reg4) 
                        {
                            __reg9[__reg5++] = substring(this, __reg4 + 1, __reg3._xi - __reg4);
                        }
                        __reg4 = __reg3._xi + length(tm.utils.RegExp.lastMatch);
                        __reg10 = __reg7;
                        __reg7 = __reg3.lastIndex;
                    }
                    if (__reg5 == __reg8) 
                    {
                        __reg3.lastIndex = __reg10;
                    }
                    else 
                    {
                        __reg3.lastIndex = __reg7;
                    }
                    if (__reg5 == 0) 
                    {
                        __reg9[__reg5] = this;
                    }
                    else 
                    {
                        if (__reg5 < __reg8 && length(tm.utils.RegExp.rightContext) > 0) 
                        {
                            __reg9[__reg5++] = tm.utils.RegExp.rightContext;
                        }
                    }
                    __reg3.global = __reg11;
                    return __reg9;
                    return;
                }
                return this.old_split(arguments[0], arguments[1]);
            }
            ;
            return true;
        }
    }

}