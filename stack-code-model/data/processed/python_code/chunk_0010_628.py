class ZCL_DATE_TOOL0 definition
  public
  final
  create public .

public section.

  class-methods CLASS_CONSTRUCTOR .
  class-methods GET_LUNAR
    importing
      !SOLAR_DATE type D default SY-DATUM
    exporting
      !ISLEAP_MONTH type CHAR1
    returning
      value(LUNAR_DATE) type NUM08 .
  class-methods GET_SOLAR
    importing
      !LUNAR_DATE type NUM08
      !ISLEAP_MONTH type CHAR1 default ''
    returning
      value(SOLAR_DATE) type D .
protected section.
PRIVATE SECTION.
  TYPES:
    BEGIN OF ys_lunar_year,
      spring_solar_date TYPE d,
      lunar             TYPE x LENGTH 3,
    END OF ys_lunar_year .
  TYPES:
    yt_lunar_year TYPE TABLE OF ys_lunar_year .

  CLASS-DATA lunar_year TYPE yt_lunar_year .
ENDCLASS.



CLASS ZCL_DATE_TOOL0 IMPLEMENTATION.


  METHOD CLASS_CONSTRUCTOR.
    IF lunar_year IS INITIAL.
      "field SPRING_SOLAR_DATE storage Solar date of Spring Festival
      "field LUNAR storage Lunar Year binary code,the length is 3 Byte
      "eg.
      "1900 year info
      "  Bit-Num 1234 5678  9ABC DEFG  HIJK LMNO
      " Byte-Seq 0000-0100--1011-1101--0000-1000
      "the 1-4 bit place is not use
      "the 5-16 bit place is days number of 1-12 month per month of
      "Lunar Year, and bit place value is 0 symbol 29 days,
      "value is 1 symbol 30.
      "the 17-19 bit place is not use
      "the 20 bit place is symbol days number of leap month, and
      " bit place value is 0 symbol 29 days, value is 1 symbol 30.
      "the 21-24 bit place is symbol month number of leap month
      lunar_year = VALUE #(
        ( spring_solar_date = '19000131' lunar = '04BD08' )
        ( spring_solar_date = '19010219' lunar = '04AE00' )
        ( spring_solar_date = '19020208' lunar = '0A5700' )
        ( spring_solar_date = '19030129' lunar = '054D05' )
        ( spring_solar_date = '19040216' lunar = '0D2600' )
        ( spring_solar_date = '19050204' lunar = '0D9500' )
        ( spring_solar_date = '19060125' lunar = '065514' )
        ( spring_solar_date = '19070213' lunar = '056A00' )
        ( spring_solar_date = '19080202' lunar = '09AD00' )
        ( spring_solar_date = '19090122' lunar = '055D02' )
        ( spring_solar_date = '19100210' lunar = '04AE00' )
        ( spring_solar_date = '19110130' lunar = '0A5B06' )
        ( spring_solar_date = '19120218' lunar = '0A4D00' )
        ( spring_solar_date = '19130206' lunar = '0D2500' )
        ( spring_solar_date = '19140126' lunar = '0D2515' )
        ( spring_solar_date = '19150214' lunar = '0B5400' )
        ( spring_solar_date = '19160203' lunar = '0D6A00' )
        ( spring_solar_date = '19170123' lunar = '0ADA02' )
        ( spring_solar_date = '19180211' lunar = '095B00' )
        ( spring_solar_date = '19190201' lunar = '049717' )
        ( spring_solar_date = '19200220' lunar = '049700' )
        ( spring_solar_date = '19210208' lunar = '0A4B00' )
        ( spring_solar_date = '19220128' lunar = '0B4B05' )
        ( spring_solar_date = '19230216' lunar = '06A500' )
        ( spring_solar_date = '19240205' lunar = '06D400' )
        ( spring_solar_date = '19250124' lunar = '0AB514' )
        ( spring_solar_date = '19260213' lunar = '02B600' )
        ( spring_solar_date = '19270202' lunar = '095700' )
        ( spring_solar_date = '19280123' lunar = '052F02' )
        ( spring_solar_date = '19290210' lunar = '049700' )
        ( spring_solar_date = '19300130' lunar = '065606' )
        ( spring_solar_date = '19310217' lunar = '0D4A00' )
        ( spring_solar_date = '19320206' lunar = '0EA500' )
        ( spring_solar_date = '19330126' lunar = '06A915' )
        ( spring_solar_date = '19340214' lunar = '05AD00' )
        ( spring_solar_date = '19350204' lunar = '02B600' )
        ( spring_solar_date = '19360124' lunar = '086E13' )
        ( spring_solar_date = '19370211' lunar = '092E00' )
        ( spring_solar_date = '19380131' lunar = '0C8D17' )
        ( spring_solar_date = '19390219' lunar = '0C9500' )
        ( spring_solar_date = '19400208' lunar = '0D4A00' )
        ( spring_solar_date = '19410127' lunar = '0D8A16' )
        ( spring_solar_date = '19420215' lunar = '0B5500' )
        ( spring_solar_date = '19430205' lunar = '056A00' )
        ( spring_solar_date = '19440125' lunar = '0A5B14' )
        ( spring_solar_date = '19450213' lunar = '025D00' )
        ( spring_solar_date = '19460202' lunar = '092D00' )
        ( spring_solar_date = '19470122' lunar = '0D2B02' )
        ( spring_solar_date = '19480210' lunar = '0A9500' )
        ( spring_solar_date = '19490129' lunar = '0B5507' )
        ( spring_solar_date = '19500217' lunar = '06CA00' )
        ( spring_solar_date = '19510206' lunar = '0B5500' )
        ( spring_solar_date = '19520127' lunar = '053515' )
        ( spring_solar_date = '19530214' lunar = '04DA00' )
        ( spring_solar_date = '19540203' lunar = '0A5B00' )
        ( spring_solar_date = '19550124' lunar = '045713' )
        ( spring_solar_date = '19560212' lunar = '052B00' )
        ( spring_solar_date = '19570131' lunar = '0A9A08' )
        ( spring_solar_date = '19580218' lunar = '0E9500' )
        ( spring_solar_date = '19590208' lunar = '06AA00' )
        ( spring_solar_date = '19600128' lunar = '0AEA06' )
        ( spring_solar_date = '19610215' lunar = '0AB500' )
        ( spring_solar_date = '19620205' lunar = '04B600' )
        ( spring_solar_date = '19630125' lunar = '0AAE04' )
        ( spring_solar_date = '19640213' lunar = '0A5700' )
        ( spring_solar_date = '19650202' lunar = '052600' )
        ( spring_solar_date = '19660121' lunar = '0F2603' )
        ( spring_solar_date = '19670209' lunar = '0D9500' )
        ( spring_solar_date = '19680130' lunar = '05B507' )
        ( spring_solar_date = '19690217' lunar = '056A00' )
        ( spring_solar_date = '19700206' lunar = '096D00' )
        ( spring_solar_date = '19710127' lunar = '04DD05' )
        ( spring_solar_date = '19720215' lunar = '04AD00' )
        ( spring_solar_date = '19730203' lunar = '0A4D00' )
        ( spring_solar_date = '19740123' lunar = '0D4D04' )
        ( spring_solar_date = '19750211' lunar = '0D2500' )
        ( spring_solar_date = '19760131' lunar = '0D5508' )
        ( spring_solar_date = '19770218' lunar = '0B5400' )
        ( spring_solar_date = '19780207' lunar = '0B6A00' )
        ( spring_solar_date = '19790128' lunar = '095A16' )
        ( spring_solar_date = '19800216' lunar = '095B00' )
        ( spring_solar_date = '19810205' lunar = '049B00' )
        ( spring_solar_date = '19820125' lunar = '0A9704' )
        ( spring_solar_date = '19830213' lunar = '0A4B00' )
        ( spring_solar_date = '19840202' lunar = '0B270A' )
        ( spring_solar_date = '19850220' lunar = '06A500' )
        ( spring_solar_date = '19860209' lunar = '06D400' )
        ( spring_solar_date = '19870129' lunar = '0AF406' )
        ( spring_solar_date = '19880217' lunar = '0AB600' )
        ( spring_solar_date = '19890206' lunar = '095700' )
        ( spring_solar_date = '19900127' lunar = '04AF05' )
        ( spring_solar_date = '19910215' lunar = '049700' )
        ( spring_solar_date = '19920204' lunar = '064B00' )
        ( spring_solar_date = '19930123' lunar = '074A03' )
        ( spring_solar_date = '19940210' lunar = '0EA500' )
        ( spring_solar_date = '19950131' lunar = '06B508' )
        ( spring_solar_date = '19960219' lunar = '05AC00' )
        ( spring_solar_date = '19970207' lunar = '0AB600' )
        ( spring_solar_date = '19980128' lunar = '096D05' )
        ( spring_solar_date = '19990216' lunar = '092E00' )
        ( spring_solar_date = '20000205' lunar = '0C9600' )
        ( spring_solar_date = '20010124' lunar = '0D9504' )
        ( spring_solar_date = '20020212' lunar = '0D4A00' )
        ( spring_solar_date = '20030201' lunar = '0DA500' )
        ( spring_solar_date = '20040122' lunar = '075502' )
        ( spring_solar_date = '20050209' lunar = '056A00' )
        ( spring_solar_date = '20060129' lunar = '0ABB07' )
        ( spring_solar_date = '20070218' lunar = '025D00' )
        ( spring_solar_date = '20080207' lunar = '092D00' )
        ( spring_solar_date = '20090126' lunar = '0CAB05' )
        ( spring_solar_date = '20100214' lunar = '0A9500' )
        ( spring_solar_date = '20110203' lunar = '0B4A00' )
        ( spring_solar_date = '20120123' lunar = '0BAA04' )
        ( spring_solar_date = '20130210' lunar = '0AD500' )
        ( spring_solar_date = '20140131' lunar = '055D09' )
        ( spring_solar_date = '20150219' lunar = '04BA00' )
        ( spring_solar_date = '20160208' lunar = '0A5B00' )
        ( spring_solar_date = '20170128' lunar = '051716' )
        ( spring_solar_date = '20180216' lunar = '052B00' )
        ( spring_solar_date = '20190205' lunar = '0A9300' )
        ( spring_solar_date = '20200125' lunar = '079504' )
        ( spring_solar_date = '20210212' lunar = '06AA00' )
        ( spring_solar_date = '20220201' lunar = '0AD500' )
        ( spring_solar_date = '20230122' lunar = '05B502' )
        ( spring_solar_date = '20240210' lunar = '04B600' )
        ( spring_solar_date = '20250129' lunar = '0A6E06' )
        ( spring_solar_date = '20260217' lunar = '0A4E00' )
        ( spring_solar_date = '20270206' lunar = '0D2600' )
        ( spring_solar_date = '20280126' lunar = '0EA605' )
        ( spring_solar_date = '20290213' lunar = '0D5300' )
        ( spring_solar_date = '20300203' lunar = '05AA00' )
        ( spring_solar_date = '20310123' lunar = '076A03' )
        ( spring_solar_date = '20320211' lunar = '096D00' )
        ( spring_solar_date = '20330131' lunar = '04AF0B' )
        ( spring_solar_date = '20340219' lunar = '04AD00' )
        ( spring_solar_date = '20350208' lunar = '0A4D00' )
        ( spring_solar_date = '20360128' lunar = '0D0B16' )
        ( spring_solar_date = '20370215' lunar = '0D2500' )
        ( spring_solar_date = '20380204' lunar = '0D5200' )
        ( spring_solar_date = '20390124' lunar = '0DD405' )
        ( spring_solar_date = '20400212' lunar = '0B5A00' )
        ( spring_solar_date = '20410201' lunar = '056D00' )
        ( spring_solar_date = '20420122' lunar = '055B02' )
        ( spring_solar_date = '20430210' lunar = '049B00' )
        ( spring_solar_date = '20440130' lunar = '0A5707' )
        ( spring_solar_date = '20450217' lunar = '0A4B00' )
        ( spring_solar_date = '20460206' lunar = '0AA500' )
        ( spring_solar_date = '20470126' lunar = '0B2515' )
        ( spring_solar_date = '20480214' lunar = '06D200' )
        ( spring_solar_date = '20490202' lunar = '0ADA00' )
        ( spring_solar_date = '20500123' lunar = '04B613' )
        ( spring_solar_date = '20510211' lunar = '093700' )
        ( spring_solar_date = '20520201' lunar = '049F08' )
        ( spring_solar_date = '20530219' lunar = '049700' )
        ( spring_solar_date = '20540208' lunar = '064B00' )
        ( spring_solar_date = '20550128' lunar = '068A16' )
        ( spring_solar_date = '20560215' lunar = '0EA500' )
        ( spring_solar_date = '20570204' lunar = '06AA00' )
        ( spring_solar_date = '20580124' lunar = '0A6C14' )
        ( spring_solar_date = '20590212' lunar = '0AAE00' )
        ( spring_solar_date = '20600202' lunar = '092E00' )
        ( spring_solar_date = '20610121' lunar = '0D2E03' )
        ( spring_solar_date = '20620209' lunar = '0C9600' )
        ( spring_solar_date = '20630129' lunar = '0D5507' )
        ( spring_solar_date = '20640217' lunar = '0D4A00' )
        ( spring_solar_date = '20650205' lunar = '0DA500' )
        ( spring_solar_date = '20660126' lunar = '05D505' )
        ( spring_solar_date = '20670214' lunar = '056A00' )
        ( spring_solar_date = '20680203' lunar = '0A6D00' )
        ( spring_solar_date = '20690123' lunar = '055D04' )
        ( spring_solar_date = '20700211' lunar = '052D00' )
        ( spring_solar_date = '20710131' lunar = '0A9B08' )
        ( spring_solar_date = '20720219' lunar = '0A9500' )
        ( spring_solar_date = '20730207' lunar = '0B4A00' )
        ( spring_solar_date = '20740127' lunar = '0B6A06' )
        ( spring_solar_date = '20750215' lunar = '0AD500' )
        ( spring_solar_date = '20760205' lunar = '055A00' )
        ( spring_solar_date = '20770124' lunar = '0ABA04' )
        ( spring_solar_date = '20780212' lunar = '0A5B00' )
        ( spring_solar_date = '20790202' lunar = '052B00' )
        ( spring_solar_date = '20800122' lunar = '0B2703' )
        ( spring_solar_date = '20810209' lunar = '069300' )
        ( spring_solar_date = '20820129' lunar = '073307' )
        ( spring_solar_date = '20830217' lunar = '06AA00' )
        ( spring_solar_date = '20840206' lunar = '0AD500' )
        ( spring_solar_date = '20850126' lunar = '04B515' )
        ( spring_solar_date = '20860214' lunar = '04B600' )
        ( spring_solar_date = '20870203' lunar = '0A5700' )
        ( spring_solar_date = '20880124' lunar = '054E04' )
        ( spring_solar_date = '20890210' lunar = '0D1600' )
        ( spring_solar_date = '20900130' lunar = '0E9608' )
        ( spring_solar_date = '20910218' lunar = '0D5200' )
        ( spring_solar_date = '20920207' lunar = '0DAA00' )
        ( spring_solar_date = '20930127' lunar = '06AA16' )
        ( spring_solar_date = '20940215' lunar = '056D00' )
        ( spring_solar_date = '20950205' lunar = '04AE00' )
        ( spring_solar_date = '20960125' lunar = '0A9D04' )
        ( spring_solar_date = '20970212' lunar = '0A2D00' )
        ( spring_solar_date = '20980201' lunar = '0D1500' )
        ( spring_solar_date = '20990121' lunar = '0F2502' )
        ( spring_solar_date = '21000209' lunar = '0D5200' )
        ).
    ENDIF.
  ENDMETHOD.


  METHOD GET_LUNAR.
    CHECK solar_date >= '19000131' AND solar_date <= '21010129'.

    " index of line symbol year number
    DATA(l_year_index) = ( CONV i( solar_date+0(4) ) - 1900 ) + 1.
    DATA(l_spring) = lunar_year[ l_year_index ]-spring_solar_date.
    IF l_spring > solar_date.
      l_year_index = l_year_index - 1.
      l_spring = lunar_year[ l_year_index ]-spring_solar_date.
    ENDIF.
    DATA(l_lunaryear_code) = lunar_year[ l_year_index ]-lunar.
    "solar date distance date of Spring Festival
    DATA(l_distance) = solar_date - l_spring + 1.
    "Get date is Spring Festival
    IF l_distance = 1.
      lunar_date = |{ l_spring+0(4) }0101|.
      RETURN.
    ENDIF.
    " Get days number of leap month, and month number of leap month
    GET BIT 20 OF l_lunaryear_code INTO DATA(l_bin).
    DATA(l_leap_month_days) = COND i( WHEN l_bin = 0 THEN 29 ELSE 30 ).
    DATA(l_leap_month) = l_lunaryear_code BIT-AND
      CONV xstring( '00000F' ).

    WHILE 0 = 0.
      DATA(l_index) = sy-index.

      GET BIT ( l_index + 4 ) OF l_lunaryear_code INTO l_bin.
      DATA(l_month_days) = COND i( WHEN l_bin = 0 THEN 29 ELSE 30 ).

      IF l_distance - l_month_days <= 0.

        lunar_date = |{ l_spring+0(4) }{ CONV num02( l_index )
          WIDTH = 2 }{ CONV num02( l_distance ) WIDTH = 2 }|.
        EXIT.
      ENDIF.
      l_distance = l_distance - l_month_days.

      CHECK CONV i( l_leap_month ) = l_index." When leap month
      IF l_distance - l_leap_month_days <= 0.

        lunar_date = |{ l_spring+0(4) }{ CONV num02( l_index )
          WIDTH = 2 }{ CONV num02( l_distance ) WIDTH = 2 }|.
        isleap_month = abap_true.
        EXIT.
      ENDIF.
      l_distance = l_distance - l_leap_month_days.
    ENDWHILE.
  ENDMETHOD.


  METHOD GET_SOLAR.
    CHECK lunar_date >= '19000101' AND lunar_date <= '21001229'.

    " sequence Lunar Date
    DATA(l_month) = CONV i( lunar_date+4(2) ).
    DATA(l_day) = CONV i( lunar_date+6(2) ).
    " index of line symbol year number
    DATA(l_year_index) = ( CONV i( lunar_date+0(4) ) - 1900 ) + 1.
    DATA(l_spring) = lunar_year[ l_year_index ]-spring_solar_date.
    DATA(l_lunaryear_code) = lunar_year[ l_year_index ]-lunar.
    "Get date is Spring Festival
    IF lunar_date+4(4) = '0101'.
      solar_date = l_spring.
      RETURN.
    ENDIF.
    " Get Get days number of leap month, and month number of leap month
    GET BIT 20 OF l_lunaryear_code INTO DATA(l_bin).
    DATA(l_leap_month_days) = COND i( WHEN l_bin = 0 THEN 29 ELSE 30 ).
    DATA(l_leap_month) = l_lunaryear_code BIT-AND
      CONV xstring( '00000F' ).
    " Check Luanar
    IF isleap_month = abap_true.
      CHECK l_month = CONV i( l_leap_month ) AND l_day <= l_leap_month_days.
    ELSE.
      GET BIT ( l_month + 4 ) OF l_lunaryear_code INTO l_bin.
      DATA(l_month_days) = COND i( WHEN l_bin = 0 THEN 29 ELSE 30 ).
      CHECK l_day <= l_month_days.
    ENDIF.
    "Lunar date distance date of Spring Festival
    DATA(l_distance) = 0.
    WHILE 0 = 0.
      DATA(l_index) = sy-index.

      GET BIT ( l_index + 4 ) OF l_lunaryear_code INTO l_bin.
      l_month_days = COND i( WHEN l_bin = 0 THEN 29 ELSE 30 ).
      IF l_month = sy-index AND isleap_month = abap_false.
        l_distance = l_distance + l_day.
        EXIT.
      ENDIF.
      l_distance = l_distance + l_month_days.

      CHECK CONV i( l_leap_month ) = l_index." When leap month
      IF l_month = sy-index AND isleap_month = abap_true.
        l_distance = l_distance + l_day.
        EXIT.
      ENDIF.
      l_distance = l_distance + l_leap_month_days.
    ENDWHILE.

    solar_date = l_spring + l_distance - 1.
  ENDMETHOD.
ENDCLASS.