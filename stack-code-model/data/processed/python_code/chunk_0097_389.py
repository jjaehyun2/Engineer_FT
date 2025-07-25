/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */
import com.adobe.test.Assert;

//     var SECTION = "15.5.4.11-1";
//     var VERSION = "ECMA_1";
//     var TITLE   = "String.prototype.toLowerCase()";


    var testcases = getTestCases();

function getTestCases() {
    var array = new Array();
    var item = 0;

    array[item++] = Assert.expectEq(   "String.prototype.toLowerCase.length",        0,          String.prototype.toLowerCase.length );
    array[item++] = Assert.expectEq(   "delete String.prototype.toLowerCase.length", false,      delete String.prototype.toLowerCase.length );
    array[item++] = Assert.expectEq(   "delete String.prototype.toLowerCase.length; String.prototype.toLowerCase.length", 0,      (delete String.prototype.toLowerCase.length, String.prototype.toLowerCase.length) );

    // Basic Latin, Latin-1 Supplement, Latin Extended A
    for ( var i = 0; i <= 0x017f; i++ ) {
        var U = new Unicode(i);
        var s = new String(String.fromCharCode(i));
/*
        array[item++] = Assert.expectEq(   
                                        "var s = new String( String.fromCharCode("+i+") ); s.toLowerCase()",
                                        String.fromCharCode(U.lower),
                                        (s = new String( String.fromCharCode("+i+ ) ), s.toLowerCase()") );
*/
        array[item++] = Assert.expectEq(   
                                        "var s = new String( String.fromCharCode("+i+") ); s.toLowerCase().charCodeAt(0)",
                                        U.lower,
                                        ( s.toLowerCase().charCodeAt(0) ) );

    }

    return array;
}
function MyObject( value ) {
    this.value = value;
    this.substring = String.prototype.substring;
    this.toString = function() { return this.value+'';}
}
function Unicode( c ) {
    u = GetUnicodeValues( c );
    this.upper = u[0];
    this.lower = u[1]
    return this;
}
function GetUnicodeValues( c ) {
    u = new Array();

    u[0] = c;
    u[1] = c;

    // upper case Basic Latin

    if ( c >= 0x0041 && c <= 0x005A) {
        u[0] = c;
        u[1] = c + 32;
        return u;
    }

    // lower case Basic Latin
    if ( c >= 0x0061 && c <= 0x007a ) {
        u[0] = c - 32;
        u[1] = c;
        return u;
    }

    // upper case Latin-1 Supplement
    if ( (c >= 0x00C0 && c <= 0x00D6) || (c >= 0x00D8 && c<=0x00DE) ) {
        u[0] = c;
        u[1] = c + 32;
        return u;
    }

    // lower case Latin-1 Supplement
    if ( (c >= 0x00E0 && c <= 0x00F6) || (c >= 0x00F8 && c <= 0x00FE) ) {
        u[0] = c - 32;
        u[1] = c;
        return u;
    }
    if ( c == 0x00FF ) {
        u[0] = 0x0178;
        u[1] = c;
        return u;
    }
    // Latin Extended A
    if ( (c >= 0x0100 && c < 0x0138) || (c > 0x0149 && c < 0x0178) ) {
        // special case for capital I
        if ( c == 0x0130 ) {
            u[0] = c;
            u[1] = 0x0069;
            return u;
        }
        if ( c == 0x0131 ) {
            u[0] = 0x0049;
            u[1] = c;
            return u;
        }

        if ( c % 2 == 0 ) {
        // if it's even, it's a capital and the lower case is c +1
            u[0] = c;
            u[1] = c+1;
        } else {
        // if it's odd, it's a lower case and upper case is c-1
            u[0] = c-1;
            u[1] = c;
        }
        return u;
    }
    if ( c == 0x0178 ) {
        u[0] = c;
        u[1] = 0x00FF;
        return u;
    }

    if ( (c >= 0x0139 && c < 0x0149) || (c > 0x0178 && c < 0x017F) ) {
        if ( c % 2 == 1 ) {
        // if it's odd, it's a capital and the lower case is c +1
            u[0] = c;
            u[1] = c+1;
        } else {
        // if it's even, it's a lower case and upper case is c-1
            u[0] = c-1;
            u[1] = c;
        }
        return u;
    }
    if ( c == 0x017F ) {
        u[0] = 0x0053;
        u[1] = c;
    }

    // Latin Extended B
    // need to improve this set

    if ( c >= 0x0200 && c <= 0x0217 ) {
        if ( c % 2 == 0 ) {
            u[0] = c;
            u[1] = c+1;
        } else {
            u[0] = c-1;
            u[1] = c;
        }
        return u;
    }

    // Latin Extended Additional
    // Range: U+1E00 to U+1EFF
    // http://www.unicode.org/Unicode.charts/glyphless/U1E00.html

    // Spacing Modifier Leters
    // Range: U+02B0 to U+02FF

    // Combining Diacritical Marks
    // Range: U+0300 to U+036F

    // skip Greek for now
    // Greek
    // Range: U+0370 to U+03FF

    // Cyrillic
    // Range: U+0400 to U+04FF

    if ( (c >= 0x0401 && c <= 0x040C) || ( c>= 0x040E && c <= 0x040F ) ) {
        u[0] = c;
        u[1] = c + 80;
        return u;
    }


    if ( c >= 0x0410  && c <= 0x042F ) {
        u[0] = c;
        u[1] = c + 32;
        return u;
    }

    if ( c >= 0x0430 && c<= 0x044F ) {
        u[0] = c - 32;
        u[1] = c;
        return u;

    }
    if ( (c >= 0x0451 && c <= 0x045C) || (c >=0x045E && c<= 0x045F) ) {
        u[0] = c -80;
        u[1] = c;
        return u;
    }

    if ( c >= 0x0460 && c <= 0x047F ) {
        if ( c % 2 == 0 ) {
            u[0] = c;
            u[1] = c +1;
        } else {
            u[0] = c - 1;
            u[1] = c;
        }
        return u;
    }

    // Armenian
    // Range: U+0530 to U+058F
    if ( c >= 0x0531 && c <= 0x0556 ) {
        u[0] = c;
        u[1] = c + 48;
        return u;
    }
    if ( c >= 0x0561 && c < 0x0587 ) {
        u[0] = c - 48;
        u[1] = c;
        return u;
    }

    // Hebrew
    // Range: U+0590 to U+05FF


    // Arabic
    // Range: U+0600 to U+06FF

    // Devanagari
    // Range: U+0900 to U+097F


    // Bengali
    // Range: U+0980 to U+09FF


    // Gurmukhi
    // Range: U+0A00 to U+0A7F


    // Gujarati
    // Range: U+0A80 to U+0AFF


    // Oriya
    // Range: U+0B00 to U+0B7F
    // no capital / lower case


    // Tamil
    // Range: U+0B80 to U+0BFF
    // no capital / lower case


    // Telugu
    // Range: U+0C00 to U+0C7F
    // no capital / lower case


    // Kannada
    // Range: U+0C80 to U+0CFF
    // no capital / lower case


    // Malayalam
    // Range: U+0D00 to U+0D7F

    // Thai
    // Range: U+0E00 to U+0E7F


    // Lao
    // Range: U+0E80 to U+0EFF


    // Tibetan
    // Range: U+0F00 to U+0FBF

    // Georgian
    // Range: U+10A0 to U+10F0
    if ( c >= 0x10A0 && c <= 0x10C5 ) {
        u[0] = c;
        u[1] = c + 48;
        return u;
    }
    if ( c >= 0x10D0 && c <= 0x10F5 ) {
        u[0] = c;
        u[1] = c;
        return u;
    }

    // Hangul Jamo
    // Range: U+1100 to U+11FF

    // Greek Extended
    // Range: U+1F00 to U+1FFF
    // skip for now


    // General Punctuation
    // Range: U+2000 to U+206F

    // Superscripts and Subscripts
    // Range: U+2070 to U+209F

    // Currency Symbols
    // Range: U+20A0 to U+20CF


    // Combining Diacritical Marks for Symbols
    // Range: U+20D0 to U+20FF
    // skip for now


    // Number Forms
    // Range: U+2150 to U+218F
    // skip for now


    // Arrows
    // Range: U+2190 to U+21FF

    // Mathematical Operators
    // Range: U+2200 to U+22FF

    // Miscellaneous Technical
    // Range: U+2300 to U+23FF

    // Control Pictures
    // Range: U+2400 to U+243F

    // Optical Character Recognition
    // Range: U+2440 to U+245F

    // Enclosed Alphanumerics
    // Range: U+2460 to U+24FF

    // Box Drawing
    // Range: U+2500 to U+257F

    // Block Elements
    // Range: U+2580 to U+259F

    // Geometric Shapes
    // Range: U+25A0 to U+25FF

    // Miscellaneous Symbols
    // Range: U+2600 to U+26FF

    // Dingbats
    // Range: U+2700 to U+27BF

    // CJK Symbols and Punctuation
    // Range: U+3000 to U+303F

    // Hiragana
    // Range: U+3040 to U+309F

    // Katakana
    // Range: U+30A0 to U+30FF

    // Bopomofo
    // Range: U+3100 to U+312F

    // Hangul Compatibility Jamo
    // Range: U+3130 to U+318F

    // Kanbun
    // Range: U+3190 to U+319F


    // Enclosed CJK Letters and Months
    // Range: U+3200 to U+32FF

    // CJK Compatibility
    // Range: U+3300 to U+33FF

    // Hangul Syllables
    // Range: U+AC00 to U+D7A3

    // High Surrogates
    // Range: U+D800 to U+DB7F

    // Private Use High Surrogates
    // Range: U+DB80 to U+DBFF

    // Low Surrogates
    // Range: U+DC00 to U+DFFF

    // Private Use Area
    // Range: U+E000 to U+F8FF

    // CJK Compatibility Ideographs
    // Range: U+F900 to U+FAFF

    // Alphabetic Presentation Forms
    // Range: U+FB00 to U+FB4F

    // Arabic Presentation Forms-A
    // Range: U+FB50 to U+FDFF

    // Combining Half Marks
    // Range: U+FE20 to U+FE2F

    // CJK Compatibility Forms
    // Range: U+FE30 to U+FE4F

    // Small Form Variants
    // Range: U+FE50 to U+FE6F

    // Arabic Presentation Forms-B
    // Range: U+FE70 to U+FEFF

    // Halfwidth and Fullwidth Forms
    // Range: U+FF00 to U+FFEF

    if ( c >= 0xFF21 && c <= 0xFF3A ) {
        u[0] = c;
        u[1] = c + 32;
        return u;
    }

    if ( c >= 0xFF41 && c <= 0xFF5A ) {
        u[0] = c - 32;
        u[1] = c;
        return u;
    }

    // Specials
    // Range: U+FFF0 to U+FFFF

    return u;
}

function DecimalToHexString( n ) {
    n = Number( n );
    var h = "0x";

    for ( var i = 3; i >= 0; i-- ) {
        if ( n >= Math.pow(16, i) ){
            var t = Math.floor( n  / Math.pow(16, i));
            n -= t * Math.pow(16, i);
            if ( t >= 10 ) {
                if ( t == 10 ) {
                    h += "A";
                }
                if ( t == 11 ) {
                    h += "B";
                }
                if ( t == 12 ) {
                    h += "C";
                }
                if ( t == 13 ) {
                    h += "D";
                }
                if ( t == 14 ) {
                    h += "E";
                }
                if ( t == 15 ) {
                    h += "F";
                }
            } else {
                h += String( t );
            }
        } else {
            h += "0";
        }
    }

    return h;
}