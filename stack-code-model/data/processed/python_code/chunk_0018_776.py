class zcl_creation definition
  public
  final
  create public .

  public section.

    interfaces if_oo_adt_classrun.
  protected section.
  private section.
endclass.



class zcl_creation implementation.

  method if_oo_adt_classrun~main.
**********************************************************************
* ZAPO_RETAILERS
**********************************************************************
    select * from zapo_retailers
    into table @data(lt_free_ret).

    if sy-subrc is initial.

      delete zapo_retailers from table @lt_free_ret.

    endif.

    types: lty_retailers type standard table of zapo_retailers with default key.

    data(lt_retailers) = value lty_retailers( ( retailerid = 'OQB' land1 = 'SE' name1 = 'Shufflester' fax = '(938) 1388352' email = 'nbeart0@theatlantic.com' street = '53558 Mcguire Way' )
                                            ( retailerid = 'KLJ' land1 = 'PL' name1 = 'Flashset' fax = '(857) 3493447' email = 'erollo1@boston.com' street = '4826 Logan Lane' )
                                            ( retailerid = 'ZOB' land1 = 'CN' name1 = 'Yozio' fax = '(551) 2821075' email = 'ycicculini2@google.com' street = '72 Bellgrove Terrace' )
                                            ( retailerid = 'HSU' land1 = 'PE' name1 = 'Viva' fax = '(802) 3109493' email = 'byeoman3@icio.us' street = '9 Garrison Pass' )
                                            ( retailerid = 'QSM' land1 = 'CN' name1 = 'Layo' fax = '(717) 3376859' email = 'dfibbens4@reverbnation.com' street = '769 Onsgard Park' )
                                            ( retailerid = 'ISL' land1 = 'ID' name1 = 'Lazz' fax = '(557) 4118786' email = 'jfillgate5@tripadvisor.com' street = '6 Continental Trail' )
                                            ( retailerid = 'CLR' land1 = 'PH' name1 = 'Twimbo' fax = '(999) 5708739' email = 'snancarrow6@bloomberg.com' street = '8006 Jenna Place' )
                                            ( retailerid = 'UXT' land1 = 'CN' name1 = 'Feedfire' fax = '(479) 9946987' email = 'ployd7@lycos.com' street = '90332 Wayridge Center' )
                                            ( retailerid = 'EAM' land1 = 'CH' name1 = 'Realmix' fax = '(281) 8510117' email = 'cwoehler8@tinypic.com' street = '673 6th Drive' )
                                            ( retailerid = 'TMQ' land1 = 'FI' name1 = 'Mydo' fax = '(270) 7934976' email = 'fmuller9@yahoo.com' street = '7651 Valley Edge Parkway' )
                                            ( retailerid = 'KYI' land1 = 'IE' name1 = 'Zoozzy' fax = '(105) 3191135' email = 'gstoutea@yelp.com' street = '6999 Sugar Way' )
                                            ( retailerid = 'QKH' land1 = 'ID' name1 = 'Topicware' fax = '(829) 5365474' email = 'bkidb@columbia.edu' street = '31 Milwaukee Road' )
                                            ( retailerid = 'IST' land1 = 'FR' name1 = 'Oozz' fax = '(587) 7713727' email = 'ahogbournec@google.com' street = '4 Porter Road' )
                                            ( retailerid = 'DLD' land1 = 'PE' name1 = 'Yabox' fax = '(837) 1854987' email = 'bbrandenburgd@dagondesign.com' street = '8176 Florence Center' )
                                            ( retailerid = 'UDX' land1 = 'ID' name1 = 'Gabcube' fax = '(736) 2918138' email = 'dkinge@freewebs.com' street = '0335 Prairie Rose Hill' )
                                            ( retailerid = 'ADB' land1 = 'NL' name1 = 'Youfeed' fax = '(306) 6771784' email = 'mkneaphseyf@clickbank.net' street = '67856 Forest Terrace' )
                                            ( retailerid = 'MIN' land1 = 'PH' name1 = 'Skipstorm' fax = '(486) 7101923' email = 'fdetoileg@cbsnews.com' street = '7916 Jenifer Park' )
                                            ( retailerid = 'YBO' land1 = 'RU' name1 = 'Rhyloo' fax = '(535) 8683611' email = 'kwintersgillh@list-manage.com' street = '9114 Red Cloud Parkway' )
                                            ( retailerid = 'HTF' land1 = 'CN' name1 = 'Realblab' fax = '(434) 8159550' email = 'jthongeri@e-recht24.de' street = '1 David Street' )
                                            ( retailerid = 'SFI' land1 = 'AL' name1 = 'Divavu' fax = '(235) 1073827' email = 'marnholdtj@simplemachines.org' street = '7759 Ohio Center' )
                                            ( retailerid = 'TUM' land1 = 'UG' name1 = 'Edgeclub' fax = '(710) 1165254' email = 'llillecrapk@wikimedia.org' street = '45126 Carpenter Terrace' )
                                            ( retailerid = 'WOH' land1 = 'PT' name1 = 'Wikibox' fax = '(815) 4299449' email = 'rmatczakl@wikispaces.com' street = '72 Carioca Circle' )
                                            ( retailerid = 'GDU' land1 = 'CO' name1 = 'Fadeo' fax = '(235) 1986038' email = 'ccasbournem@odnoklassniki.ru' street = '34 Burrows Center' )
                                            ( retailerid = 'BJZ' land1 = 'BR' name1 = 'Tagopia' fax = '(738) 1633739' email = 'dlynchn@t-online.de' street = '84 Garrison Terrace' )
                                            ( retailerid = 'KVS' land1 = 'CN' name1 = 'Livepath' fax = '(919) 1997069' email = 'gwaistello@smugmug.com' street = '3 Porter Court' )
                                            ( retailerid = 'LTT' land1 = 'CN' name1 = 'Dazzlesphere' fax = '(777) 6450667' email = 'dmaplethorpep@geocities.jp' street = '90221 Dakota Trail' )
                                            ( retailerid = 'LBL' land1 = 'KZ' name1 = 'Eamia' fax = '(978) 5827124' email = 'ocodq@go.com' street = '9 Old Shore Avenue' )
                                            ( retailerid = 'YNL' land1 = 'ID' name1 = 'Zoomdog' fax = '(797) 6560108' email = 'pfilyakovr@youtube.com' street = '11825 Gateway Street' )
                                            ( retailerid = 'ODU' land1 = 'FR' name1 = 'Riffpedia' fax = '(726) 3200150' email = 'jorourkes@trellian.com' street = '52901 Ridgeway Plaza' )
                                            ( retailerid = 'QBT' land1 = 'BR' name1 = 'Blogspan' fax = '(321) 8937934' email = 'gbelchert@foxnews.com' street = '2742 Washington Way' )
                                            ( retailerid = 'LVG' land1 = 'PH' name1 = 'Oyope' fax = '(156) 5405903' email = 'lhadleighu@baidu.com' street = '47 Magdeline Place' )
                                            ( retailerid = 'GTB' land1 = 'CN' name1 = 'Dynava' fax = '(800) 6131933' email = 'jmaillardv@xinhuanet.com' street = '54 Sheridan Terrace' )
                                            ( retailerid = 'GNU' land1 = 'YE' name1 = 'Ntags' fax = '(749) 8948009' email = 'rhuggonw@cpanel.net' street = '3001 Orin Trail' )
                                            ( retailerid = 'ADV' land1 = 'BR' name1 = 'Roodel' fax = '(693) 5315097' email = 'tkynanx@ibm.com' street = '95035 Birchwood Pass' )
                                            ( retailerid = 'VBL' land1 = 'FR' name1 = 'Browsedrive' fax = '(958) 5906221' email = 'twabeyy@people.com.cn' street = '85924 Park Meadow Drive' )
                                            ( retailerid = 'SKB' land1 = 'AF' name1 = 'Browsebug' fax = '(959) 1060575' email = 'lbalbeckz@clickbank.net' street = '5 Independence Circle' )
                                            ( retailerid = 'RTM' land1 = 'PH' name1 = 'Chatterpoint' fax = '(919) 1647731' email = 'landrzejak10@blogger.com' street = '527 Dapin Plaza' )
                                            ( retailerid = 'UXG' land1 = 'GT' name1 = 'Jetpulse' fax = '(528) 1441583' email = 'sinsall11@artisteer.com' street = '57603 Sheridan Crossing' )
                                            ( retailerid = 'TTF' land1 = 'SE' name1 = 'Jaxspan' fax = '(803) 3388426' email = 'lrosini12@state.gov' street = '8796 Lerdahl Parkway' )
                                            ( retailerid = 'YIP' land1 = 'CN' name1 = 'Thoughtmix' fax = '(853) 1247175' email = 'pdemars13@furl.net' street = '7358 Loomis Court' )
                                            ( retailerid = 'RER' land1 = 'CN' name1 = 'Gabtune' fax = '(519) 7794120' email = 'jedmeads14@youtube.com' street = '9 Springs Terrace' )
                                            ( retailerid = 'DAK' land1 = 'FR' name1 = 'Feednation' fax = '(721) 4723550' email = 'chachard15@earthlink.net' street = '1 Clyde Gallagher Point' )
                                            ( retailerid = 'FQK' land1 = 'CN' name1 = 'Edgepulse' fax = '(611) 8053418' email = 'etissington16@rakuten.co.jp' street = '896 Gale Pass' )
                                            ( retailerid = 'IAV' land1 = 'GT' name1 = 'Mycat' fax = '(240) 5714342' email = 'lgiannasi17@addtoany.com' street = '6 American Ash Center' )
                                            ( retailerid = 'VUX' land1 = 'CN' name1 = 'Twinte' fax = '(660) 2432685' email = 'gwhitcombe18@cornell.edu' street = '0 Corry Trail' )
                                            ( retailerid = 'DBK' land1 = 'US' name1 = 'Mycat' fax = '(602) 2877979' email = 'abretland19@altervista.org' street = '72141 South Circle' )
                                            ( retailerid = 'RIK' land1 = 'PT' name1 = 'Jaxnation' fax = '(933) 8516414' email = 'rwarwicker1a@toplist.cz' street = '07364 Park Meadow Lane' )
                                            ( retailerid = 'FIF' land1 = 'CO' name1 = 'Mynte' fax = '(944) 2169821' email = 'cgoodred1b@un.org' street = '059 Shoshone Junction' )
                                            ( retailerid = 'CTC' land1 = 'CN' name1 = 'Livepath' fax = '(595) 2958889' email = 'aneve1c@tinypic.com' street = '9 Westerfield Pass' )
                                            ( retailerid = 'JHF' land1 = 'CN' name1 = 'Edgewire' fax = '(616) 5258281' email = 'dcolpus1d@amazonaws.com' street = '3513 Waxwing Junction' )
                                            ( retailerid = 'HPX' land1 = 'BR' name1 = 'Skimia' fax = '(897) 3134336' email = 'bgoadby1e@soundcloud.com' street = '75463 Melrose Hill' )
                                            ( retailerid = 'AJL' land1 = 'ME' name1 = 'Viva' fax = '(750) 5931942' email = 'pjefferson1f@dagondesign.com' street = '8 Dexter Pass' )
                                            ( retailerid = 'QFE' land1 = 'CM' name1 = 'Mybuzz' fax = '(959) 9963603' email = 'ahammarberg1g@wordpress.com' street = '2 Upham Pass' )
                                            ( retailerid = 'IGK' land1 = 'MG' name1 = 'Dabvine' fax = '(739) 6742156' email = 'hedmenson1h@php.net' street = '50 Bashford Plaza' )
                                            ( retailerid = 'VXI' land1 = 'UA' name1 = 'Shuffledrive' fax = '(528) 3501544' email = 'kbrastead1i@google.com.br' street = '3 Cardinal Hill' )
                                            ( retailerid = 'LPW' land1 = 'DE' name1 = 'Realbuzz' fax = '(191) 2886307' email = 'areading1j@purevolume.com' street = '0 Anderson Circle' )
                                            ( retailerid = 'QJS' land1 = 'FR' name1 = 'Wikido' fax = '(402) 8897790' email = 'singles1k@pinterest.com' street = '93 Summer Ridge Hill' )
                                            ( retailerid = 'DGV' land1 = 'BR' name1 = 'Lajo' fax = '(192) 5344508' email = 'cmcquilliam1l@msu.edu' street = '85062 Bartillon Alley' )
                                            ( retailerid = 'NLT' land1 = 'AL' name1 = 'Meezzy' fax = '(635) 9440120' email = 'glandrieu1m@prlog.org' street = '9 Toban Parkway' )
                                            ( retailerid = 'UEA' land1 = 'CN' name1 = 'Mybuzz' fax = '(778) 9729259' email = 'jledger1n@hud.gov' street = '7 School Avenue' )
                                            ( retailerid = 'QXW' land1 = 'CA' name1 = 'Shuffletag' fax = '(545) 1350490' email = 'opankethman1o@jigsy.com' street = '101 Dakota Pass' )
                                            ( retailerid = 'TRZ' land1 = 'BF' name1 = 'Avaveo' fax = '(746) 9123017' email = 'rduplock1p@unblog.fr' street = '81 Walton Lane' )
                                            ( retailerid = 'SKV' land1 = 'PL' name1 = 'Photospace' fax = '(526) 6219523' email = 'ykingscote1q@pagesperso-orange.fr' street = '67282 Caliangt Pass' )
                                            ( retailerid = 'MQI' land1 = 'TZ' name1 = 'Twitterwire' fax = '(295) 6450902' email = 'marsmith1r@webeden.co.uk' street = '52 Tony Center' )
                                            ( retailerid = 'NML' land1 = 'PT' name1 = 'Gabcube' fax = '(404) 5360169' email = 'mcalderwood1s@miitbeian.gov.cn' street = '5 Prairie Rose Circle' )
                                            ( retailerid = 'TUJ' land1 = 'ID' name1 = 'Fivechat' fax = '(514) 6305816' email = 'akinneir1t@nydailynews.com' street = '7356 Rusk Court' )
                                            ( retailerid = 'VJI' land1 = 'GT' name1 = 'Izio' fax = '(449) 3748786' email = 'mtace1u@infoseek.co.jp' street = '1093 Quincy Pass' )
                                            ( retailerid = 'GPS' land1 = 'GR' name1 = 'Dazzlesphere' fax = '(595) 9625712' email = 'mclementel1v@dagondesign.com' street = '61895 8th Court' )
                                            ( retailerid = 'ZGX' land1 = 'CA' name1 = 'Meembee' fax = '(891) 2559630' email = 'nrabbitt1w@engadget.com' street = '7348 Esker Way' )
                                            ( retailerid = 'LCA' land1 = 'NI' name1 = 'Blognation' fax = '(597) 5762706' email = 'hjobbings1x@google.fr' street = '45198 Cambridge Plaza' )
                                            ( retailerid = 'GYC' land1 = 'MD' name1 = 'Meemm' fax = '(901) 7617595' email = 'shubbucke1y@disqus.com' street = '07 Reinke Avenue' )
                                            ( retailerid = 'RFM' land1 = 'MA' name1 = 'Agimba' fax = '(709) 1098964' email = 'avacher1z@sourceforge.net' street = '4409 Mendota Drive' )
                                            ( retailerid = 'SIJ' land1 = 'RU' name1 = 'Skinix' fax = '(381) 3746976' email = 'mfarnill20@4shared.com' street = '2216 Gerald Drive' )
                                            ( retailerid = 'IHV' land1 = 'SE' name1 = 'Photojam' fax = '(169) 6915530' email = 'bchapleo21@army.mil' street = '844 Lawn Circle' )
                                            ( retailerid = 'PSY' land1 = 'HR' name1 = 'Lazz' fax = '(102) 1759722' email = 'bdaud22@cocolog-nifty.com' street = '4115 Bayside Street' )
                                            ( retailerid = 'GWA' land1 = 'NG' name1 = 'Youspan' fax = '(479) 9643741' email = 'mgalbreth23@friendfeed.com' street = '78 Forest Dale Avenue' )
                                            ( retailerid = 'SBS' land1 = 'CN' name1 = 'Oloo' fax = '(658) 6051684' email = 'lprime24@networkadvertising.org' street = '9042 Debs Place' )
                                            ( retailerid = 'ZIT' land1 = 'CZ' name1 = 'Edgepulse' fax = '(680) 1545094' email = 'ldehn25@tinyurl.com' street = '2575 Arapahoe Avenue' )
                                            ( retailerid = 'CEP' land1 = 'US' name1 = 'Zoovu' fax = '(913) 7294352' email = 'atellenbrok26@purevolume.com' street = '5196 Longview Avenue' )
                                            ( retailerid = 'XSE' land1 = 'UA' name1 = 'Skipfire' fax = '(171) 1352947' email = 'lcaron27@gnu.org' street = '4948 Russell Park' )
                                            ( retailerid = 'UTU' land1 = 'HN' name1 = 'Flashdog' fax = '(417) 7635596' email = 'lmcelmurray28@newsvine.com' street = '2665 Homewood Circle' )
                                            ( retailerid = 'XFJ' land1 = 'ID' name1 = 'Photolist' fax = '(940) 7307052' email = 'rpordal29@dion.ne.jp' street = '1857 Marcy Street' )
                                            ( retailerid = 'MNV' land1 = 'ID' name1 = 'Plajo' fax = '(853) 8337871' email = 'hsweedland2a@pcworld.com' street = '3624 Corry Road' )
                                            ( retailerid = 'MYU' land1 = 'VN' name1 = 'Topiczoom' fax = '(661) 5761995' email = 'pwyborn2b@unesco.org' street = '8486 Reindahl Crossing' )
                                            ( retailerid = 'AIJ' land1 = 'PL' name1 = 'Meevee' fax = '(461) 5403427' email = 'nstetlye2c@nps.gov' street = '52458 Golden Leaf Alley' )
                                            ( retailerid = 'IDN' land1 = 'SE' name1 = 'Voomm' fax = '(599) 3010992' email = 'hmerrison2d@google.ru' street = '69 Lyons Lane' )
                                            ( retailerid = 'TAE' land1 = 'GT' name1 = 'Meejo' fax = '(114) 9518488' email = 'tmollison2e@comcast.net' street = '110 Logan Terrace' )
                                            ( retailerid = 'SNP' land1 = 'VN' name1 = 'Blognation' fax = '(240) 8442462' email = 'bboggas2f@bloglines.com' street = '5860 Hoepker Alley' )
                                            ( retailerid = 'CDH' land1 = 'GB' name1 = 'Divape' fax = '(590) 9667949' email = 'jvasentsov2g@paypal.com' street = '59552 Hoepker Way' )
                                            ( retailerid = 'ESJ' land1 = 'RU' name1 = 'Talane' fax = '(504) 2364882' email = 'ffiddeman2h@theguardian.com' street = '9 Carpenter Center' )
                                            ( retailerid = 'GYL' land1 = 'CA' name1 = 'Demizz' fax = '(350) 8454230' email = 'cschonfeld2i@miitbeian.gov.cn' street = '30913 Anzinger Park' )
                                            ( retailerid = 'GMP' land1 = 'PH' name1 = 'Vinte' fax = '(148) 8508023' email = 'sjeune2j@utexas.edu' street = '75 Vahlen Plaza' )
                                            ( retailerid = 'ITT' land1 = 'TH' name1 = 'Wordtune' fax = '(854) 6417624' email = 'cmanville2k@imdb.com' street = '51460 Shelley Parkway' )
                                            ( retailerid = 'BXU' land1 = 'CN' name1 = 'Wikizz' fax = '(597) 8931001' email = 'claidler2l@artisteer.com' street = '5929 Welch Court' )
                                            ( retailerid = 'DOF' land1 = 'MD' name1 = 'Cogidoo' fax = '(776) 2296215' email = 'apaschek2m@nationalgeographic.com' street = '928 Gale Terrace' )
                                            ( retailerid = 'SZK' land1 = 'PH' name1 = 'Skiptube' fax = '(463) 7117611' email = 'fchristescu2n@oracle.com' street = '56 8th Trail' )
                                            ( retailerid = 'GNK' land1 = 'BR' name1 = 'Wordtune' fax = '(711) 4618548' email = 'hlumby2o@miitbeian.gov.cn' street = '1 Forster Drive' )
                                            ( retailerid = 'LKU' land1 = 'KR' name1 = 'Yakitri' fax = '(258) 2010457' email = 'rlouth2p@de.vu' street = '18776 Forest Avenue' )
                                            ( retailerid = 'FYW' land1 = 'CZ' name1 = 'Camido' fax = '(744) 7560886' email = 'lbunce2q@state.gov' street = '59 Blaine Drive' )
                                            ( retailerid = 'CMW' land1 = 'ID' name1 = 'Jaxworks' fax = '(150) 7950290' email = 'ddressel2r@indiegogo.com' street = '18097 Grover Trail' )
                                            ).

    insert zapo_retailers from table @lt_retailers.

**********************************************************************
* ZAPO_STOCK
**********************************************************************
    data: system_uuid type ref to if_system_uuid.
    data: oref        type ref to cx_uuid_error.


    system_uuid = cl_uuid_factory=>create_system_uuid( ).

    select * from zapo_sku
    into table @data(lt_free_sku).

    if sy-subrc is initial.

      delete zapo_sku from table @lt_free_sku.

    endif.

    types: lty_stock type standard table of zapo_sku with default key.

    data(lt_stock) = value lty_stock(
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '7605492' description = 'Chevrolet' theme = 'Beretta' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '1476193' description = 'Maybach' theme = '57S' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '4815990' description = 'Cadillac' theme = 'Seville' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '9068799' description = 'Mazda' theme = 'Familia' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '5213275' description = 'Ford' theme = 'F350' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '7684563' description = 'Chevrolet' theme = 'Malibu' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2786929' description = 'Ford' theme = 'Econoline E350' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '4435871' description = 'Buick' theme = 'Park Avenue' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '3054695' description = 'Hummer' theme = 'H2' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '1062527' description = 'Lincoln' theme = 'Mark VIII' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '8396732' description = 'Chevrolet' theme = 'Sportvan G30' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '4936474' description = 'Mercedes-Benz' theme = 'C-Class' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '6275332' description = 'Dodge' theme = 'Neon' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '7266258' description = 'Mitsubishi' theme = '3000GT' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '9795144' description = 'Daewoo' theme = 'Lanos' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2095028' description = 'Plymouth' theme = 'Sundance' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '87547' description = 'Hummer' theme = 'H1' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '8631046' description = 'Dodge' theme = 'Dakota Club' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '878804' description = 'Hummer' theme = 'H2' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '5275716' description = 'Kia' theme = 'Sportage' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '901320' description = 'Pontiac' theme = 'Grand Prix' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '6104049' description = 'Ford' theme = 'Ranger' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '7319830' description = 'Mazda' theme = 'B-Series Plus' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '6591761' description = 'Lexus' theme = 'SC' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '7674558' description = 'Kia' theme = 'Sportage' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2875521' description = 'Pontiac' theme = 'Vibe' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '3495267' description = 'Mercedes-Benz' theme = 'CL-Class' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '5563804' description = 'Mitsubishi' theme = 'Expo' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '3841585' description = 'Ford' theme = 'F-Series Super Duty' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2269745' description = 'Volkswagen' theme = 'Routan' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '5852695' description = 'Volvo' theme = 'V50' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '3672013' description = 'Lexus' theme = 'GX' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '3726996' description = 'Chevrolet' theme = 'Express' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2424906' description = 'Dodge' theme = 'Ram Van 3500' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '8621736' description = 'Honda' theme = 'Element' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '3014579' description = 'Volkswagen' theme = 'Eos' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2326847' description = 'Lexus' theme = 'LX' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '9161265' description = 'Jeep' theme = 'Compass' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '7197276' description = 'Pontiac' theme = 'Firefly' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '8675884' description = 'Suzuki' theme = 'Samurai' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2827217' description = 'BMW' theme = '5 Series' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '5699263' description = 'Acura' theme = 'CL' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '6609949' description = 'Volvo' theme = 'XC70' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2216403' description = 'Nissan' theme = 'Rogue' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '1542198' description = 'Lotus' theme = 'Elan' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '732053' description = 'Infiniti' theme = 'Q' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '4743938' description = 'Chevrolet' theme = 'Venture' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '7166711' description = 'Mercury' theme = 'Sable' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '524465' description = 'Honda' theme = 'CR-X' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '5250824' description = 'Isuzu' theme = 'i-290' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '6861189' description = 'Audi' theme = '200' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '6611805' description = 'Plymouth' theme = 'Acclaim' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '1827396' description = 'Lotus' theme = 'Elise' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '7573583' description = 'Chevrolet' theme = 'G-Series G10' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2447026' description = 'Mercedes-Benz' theme = 'SL-Class' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2391887' description = 'Lincoln' theme = 'Continental' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '5914804' description = 'BMW' theme = 'X5' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '4747095' description = 'Acura' theme = 'Legend' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '6340704' description = 'Mercedes-Benz' theme = 'SLR McLaren' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '7808831' description = 'Ford' theme = 'Expedition' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '7051304' description = 'Cadillac' theme = 'Eldorado' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '6816772' description = 'Bentley' theme = 'Arnage' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '4180758' description = 'Ford' theme = 'Crown Victoria' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '8777423' description = 'Mercedes-Benz' theme = 'SL-Class' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '4057230' description = 'Buick' theme = 'Rendezvous' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '5440637' description = 'Chrysler' theme = '200' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '9033357' description = 'Ford' theme = 'Aerostar' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '82005' description = 'Ford' theme = 'Mustang' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '7764881' description = 'BMW' theme = 'Z4 M' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2317191' description = 'Kia' theme = 'Forte' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '7314810' description = 'Ford' theme = 'E-Series' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '4188938' description = 'Chevrolet' theme = 'Suburban 2500' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '4961295' description = 'Mercedes-Benz' theme = 'C-Class' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '5048576' description = 'Dodge' theme = 'Ram 2500' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '7403158' description = 'Suzuki' theme = 'Daewoo Magnus' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '9313720' description = 'Eagle' theme = 'Talon' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '6232851' description = 'Honda' theme = 'Accord' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '9875460' description = 'Pontiac' theme = 'GTO' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2212759' description = 'Ford' theme = 'Mustang' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2676837' description = 'Nissan' theme = 'Pathfinder' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '7250490' description = 'Jaguar' theme = 'XJ' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2919301' description = 'Kia' theme = 'Sportage' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '45692' description = 'Oldsmobile' theme = 'Alero' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '3344443' description = 'Mazda' theme = 'CX-9' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2733822' description = 'Chevrolet' theme = 'Suburban 1500' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '5919304' description = 'Oldsmobile' theme = 'Aurora' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '6801361' description = 'Ford' theme = 'Ranger' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '4012900' description = 'Mercedes-Benz' theme = '600SEL' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '8637280' description = 'Ford' theme = 'E-Series' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '1003218' description = 'Jaguar' theme = 'XJ Series' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '2041036' description = 'Maserati' theme = 'Gran Sport' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '7084454' description = 'BMW' theme = 'X5' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '3272529' description = 'Ford' theme = 'Festiva' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '5373277' description = 'Bentley' theme = 'Azure' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '3615725' description = 'Pontiac' theme = 'Firebird' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '8692712' description = 'Nissan' theme = 'Sentra' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '1550458' description = 'Lincoln' theme = 'Town Car' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '4119249' description = 'Volvo' theme = '960' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '1511405' description = 'Dodge' theme = 'Ram 50' )
                                      ( skuuuid = system_uuid->create_uuid_x16( ) sku = '1986171' description = 'Mercedes-Benz' theme = 'W126' )
                                      ).

    insert zapo_sku from table @lt_stock.

**********************************************************************
* ZAPO_SALES
**********************************************************************
    select * from zapo_sales
    into table @data(lt_free_sales).

    if sy-subrc is initial.

      delete zapo_retailers from table @lt_free_sales.

    endif.

    types: lty_sales type standard table of zapo_sales with default key.

    data(lt_sales) = value lty_sales(
                                    ( retailerid = 'MQI' sku = '2317191' salesdate = '20210903' description = 'Kia' theme = 'Forte' quantity = 244 quantityunit = 'PS' )
                                    ( retailerid = 'ODU' sku = '45692' salesdate = '20210922' description = 'Oldsmobile' theme = 'Alero' quantity = 585 quantityunit = 'W' )
                                    ( retailerid = 'SNP' sku = '9875460' salesdate = '20210914' description = 'Pontiac' theme = 'GTO' quantity = 737 quantityunit = 'JMO' )
                                    ( retailerid = 'BJZ' sku = '3014579' salesdate = '20210924' description = 'Volkswagen' theme = 'Eos' quantity = 878 quantityunit = 'DM' )
                                    ( retailerid = 'MYU' sku = '7266258' salesdate = '20210930' description = 'Mitsubishi' theme = '3000GT' quantity = 699 quantityunit = 'JMO' )
                                    ( retailerid = 'YBO' sku = '8637280' salesdate = '20210925' description = 'Ford' theme = 'E-Series' quantity = 986 quantityunit = 'HAR' )
                                    ( retailerid = 'UTU' sku = '2041036' salesdate = '20210924' description = 'Maserati' theme = 'Gran Sport' quantity = 636 quantityunit = 'PS' )
                                    ( retailerid = 'QFE' sku = '7573583' salesdate = '20211002' description = 'Chevrolet' theme = 'G-Series G10' quantity = 782 quantityunit = 'PS' )
                                    ( retailerid = 'SKV' sku = '5914804' salesdate = '20210909' description = 'BMW' theme = 'X5' quantity = 560 quantityunit = 'PS' )
                                    ( retailerid = 'GMP' sku = '7808831' salesdate = '20210909' description = 'Ford' theme = 'Expedition' quantity = 444 quantityunit = 'KG' )
                                    ( retailerid = 'AJL' sku = '3344443' salesdate = '20211002' description = 'Mazda' theme = 'CX-9' quantity = 149 quantityunit = 'HAR' )
                                    ( retailerid = 'RER' sku = '2269745' salesdate = '20210916' description = 'Volkswagen' theme = 'Routan' quantity = 27 quantityunit = 'PS' )
                                    ( retailerid = 'IAV' sku = '7314810' salesdate = '20210919' description = 'Ford' theme = 'E-Series' quantity = 52 quantityunit = 'HAR' )
                                    ( retailerid = 'GWA' sku = '2733822' salesdate = '20210901' description = 'Chevrolet' theme = 'Suburban 1500' quantity = 932 quantityunit = 'KG' )
                                    ( retailerid = 'GMP' sku = '8692712' salesdate = '20210904' description = 'Nissan' theme = 'Sentra' quantity = 112 quantityunit = 'N' )
                                    ( retailerid = 'DGV' sku = '4435871' salesdate = '20210927' description = 'Buick' theme = 'Park Avenue' quantity = 974 quantityunit = 'DM' )
                                    ( retailerid = 'RTM' sku = '2676837' salesdate = '20210921' description = 'Nissan' theme = 'Pathfinder' quantity = 296 quantityunit = 'FT' )
                                    ( retailerid = 'NML' sku = '7403158' salesdate = '20210924' description = 'Suzuki' theme = 'Daewoo Magnus' quantity = 679 quantityunit = 'MG' )
                                    ( retailerid = 'TAE' sku = '4936474' salesdate = '20210908' description = 'Mercedes-Benz' theme = 'C-Class' quantity = 884 quantityunit = 'FT' )
                                    ( retailerid = 'SNP' sku = '2875521' salesdate = '20210915' description = 'Pontiac' theme = 'Vibe' quantity = 118 quantityunit = 'W' )
                                    ( retailerid = 'DGV' sku = '7314810' salesdate = '20210919' description = 'Ford' theme = 'E-Series' quantity = 583 quantityunit = 'N' )
                                    ( retailerid = 'LVG' sku = '2269745' salesdate = '20210930' description = 'Volkswagen' theme = 'Routan' quantity = 947 quantityunit = 'PS' )
                                    ( retailerid = 'KLJ' sku = '1827396' salesdate = '20210913' description = 'Lotus' theme = 'Elise' quantity = 957 quantityunit = 'MG' )
                                    ( retailerid = 'IGK' sku = '6611805' salesdate = '20210907' description = 'Plymouth' theme = 'Acclaim' quantity = 745 quantityunit = 'N' )
                                    ( retailerid = 'IGK' sku = '7403158' salesdate = '20211002' description = 'Suzuki' theme = 'Daewoo Magnus' quantity = 613 quantityunit = 'N' )
                                    ( retailerid = 'YBO' sku = '5213275' salesdate = '20210905' description = 'Ford' theme = 'F350' quantity = 705 quantityunit = 'PS' )
                                    ( retailerid = 'QXW' sku = '2212759' salesdate = '20210906' description = 'Ford' theme = 'Mustang' quantity = 856 quantityunit = 'FT' )
                                    ( retailerid = 'LTT' sku = '5563804' salesdate = '20210908' description = 'Mitsubishi' theme = 'Expo' quantity = 897 quantityunit = 'PS' )
                                    ( retailerid = 'IGK' sku = '2269745' salesdate = '20210903' description = 'Volkswagen' theme = 'Routan' quantity = 46 quantityunit = 'GLL' )
                                    ( retailerid = 'IHV' sku = '87547' salesdate = '20210925' description = 'Hummer' theme = 'H1' quantity = 898 quantityunit = 'JMO' )
                                    ( retailerid = 'ISL' sku = '6104049' salesdate = '20211002' description = 'Ford' theme = 'Ranger' quantity = 465 quantityunit = 'N' )
                                    ( retailerid = 'PSY' sku = '7684563' salesdate = '20210915' description = 'Chevrolet' theme = 'Malibu' quantity = 566 quantityunit = 'MG' )
                                    ( retailerid = 'XSE' sku = '8777423' salesdate = '20210920' description = 'Mercedes-Benz' theme = 'SL-Class' quantity = 551 quantityunit = 'GLL' )
                                    ( retailerid = 'GMP' sku = '2269745' salesdate = '20210915' description = 'Volkswagen' theme = 'Routan' quantity = 266 quantityunit = 'MG' )
                                    ( retailerid = 'TRZ' sku = '2676837' salesdate = '20210915' description = 'Nissan' theme = 'Pathfinder' quantity = 18 quantityunit = 'W' )
                                    ( retailerid = 'VBL' sku = '9161265' salesdate = '20210906' description = 'Jeep' theme = 'Compass' quantity = 512 quantityunit = 'PS' )
                                    ( retailerid = 'TUJ' sku = '2919301' salesdate = '20210915' description = 'Kia' theme = 'Sportage' quantity = 919 quantityunit = 'N' )
                                    ( retailerid = 'GYL' sku = '87547' salesdate = '20210920' description = 'Hummer' theme = 'H1' quantity = 488 quantityunit = 'PS' )
                                    ( retailerid = 'PSY' sku = '4119249' salesdate = '20210921' description = 'Volvo' theme = '960' quantity = 236 quantityunit = 'GLL' )
                                    ( retailerid = 'GNK' sku = '2447026' salesdate = '20210915' description = 'Mercedes-Benz' theme = 'SL-Class' quantity = 706 quantityunit = 'JMO' )
                                    ( retailerid = 'CLR' sku = '8631046' salesdate = '20210908' description = 'Dodge' theme = 'Dakota Club' quantity = 506 quantityunit = 'KG' )
                                    ( retailerid = 'GYL' sku = '2827217' salesdate = '20211003' description = 'BMW' theme = '5 Series' quantity = 619 quantityunit = 'KG' )
                                    ( retailerid = 'TMQ' sku = '9033357' salesdate = '20210929' description = 'Ford' theme = 'Aerostar' quantity = 331 quantityunit = 'JMO' )
                                    ( retailerid = 'WOH' sku = '7250490' salesdate = '20210910' description = 'Jaguar' theme = 'XJ' quantity = 283 quantityunit = 'DM' )
                                    ( retailerid = 'LPW' sku = '3495267' salesdate = '20210907' description = 'Mercedes-Benz' theme = 'CL-Class' quantity = 463 quantityunit = 'HAR' )
                                    ( retailerid = 'FQK' sku = '6861189' salesdate = '20210907' description = 'Audi' theme = '200' quantity = 554 quantityunit = 'KG' )
                                    ( retailerid = 'MQI' sku = '2212759' salesdate = '20210902' description = 'Ford' theme = 'Mustang' quantity = 633 quantityunit = 'DM' )
                                    ( retailerid = 'GYL' sku = '5440637' salesdate = '20210928' description = 'Chrysler' theme = '200' quantity = 938 quantityunit = 'PS' )
                                    ( retailerid = 'LKU' sku = '4012900' salesdate = '20210930' description = 'Mercedes-Benz' theme = '600SEL' quantity = 18 quantityunit = 'KG' )
                                    ( retailerid = 'CTC' sku = '8692712' salesdate = '20210929' description = 'Nissan' theme = 'Sentra' quantity = 784 quantityunit = 'DM' )
                                    ( retailerid = 'GPS' sku = '7166711' salesdate = '20210903' description = 'Mercury' theme = 'Sable' quantity = 170 quantityunit = 'FT' )
                                    ( retailerid = 'DLD' sku = '4936474' salesdate = '20210922' description = 'Mercedes-Benz' theme = 'C-Class' quantity = 298 quantityunit = 'JMO' )
                                    ( retailerid = 'UTU' sku = '7403158' salesdate = '20210916' description = 'Suzuki' theme = 'Daewoo Magnus' quantity = 752 quantityunit = 'PS' )
                                    ( retailerid = 'KYI' sku = '8621736' salesdate = '20210921' description = 'Honda' theme = 'Element' quantity = 473 quantityunit = 'HAR' )
                                    ( retailerid = 'BJZ' sku = '3841585' salesdate = '20210914' description = 'Ford' theme = 'F-Series Super Duty' quantity = 83 quantityunit = 'DM' )
                                    ( retailerid = 'BJZ' sku = '8675884' salesdate = '20210926' description = 'Suzuki' theme = 'Samurai' quantity = 987 quantityunit = 'DM' )
                                    ( retailerid = 'HSU' sku = '2447026' salesdate = '20210906' description = 'Mercedes-Benz' theme = 'SL-Class' quantity = 17 quantityunit = 'JMO' )
                                    ( retailerid = 'OQB' sku = '7250490' salesdate = '20210917' description = 'Jaguar' theme = 'XJ' quantity = 139 quantityunit = 'DM' )
                                    ( retailerid = 'GYL' sku = '5563804' salesdate = '20210924' description = 'Mitsubishi' theme = 'Expo' quantity = 702 quantityunit = 'FT' )
                                    ( retailerid = 'TUM' sku = '1003218' salesdate = '20210919' description = 'Jaguar' theme = 'XJ Series' quantity = 10 quantityunit = 'W' )
                                    ( retailerid = 'ZOB' sku = '7573583' salesdate = '20210908' description = 'Chevrolet' theme = 'G-Series G10' quantity = 391 quantityunit = 'HAR' )
                                    ( retailerid = 'HPX' sku = '7051304' salesdate = '20210903' description = 'Cadillac' theme = 'Eldorado' quantity = 511 quantityunit = 'PS' )
                                    ( retailerid = 'QJS' sku = '5275716' salesdate = '20210909' description = 'Kia' theme = 'Sportage' quantity = 484 quantityunit = 'PS' )
                                    ( retailerid = 'XFJ' sku = '5563804' salesdate = '20210920' description = 'Mitsubishi' theme = 'Expo' quantity = 466 quantityunit = 'DM' )
                                    ( retailerid = 'FYW' sku = '2447026' salesdate = '20210902' description = 'Mercedes-Benz' theme = 'SL-Class' quantity = 490 quantityunit = 'GLL' )
                                    ( retailerid = 'TRZ' sku = '6801361' salesdate = '20210912' description = 'Ford' theme = 'Ranger' quantity = 728 quantityunit = 'KG' )
                                    ( retailerid = 'CEP' sku = '6275332' salesdate = '20210926' description = 'Dodge' theme = 'Neon' quantity = 960 quantityunit = 'N' )
                                    ( retailerid = 'HPX' sku = '8621736' salesdate = '20211001' description = 'Honda' theme = 'Element' quantity = 563 quantityunit = 'W' )
                                    ( retailerid = 'DLD' sku = '4815990' salesdate = '20210909' description = 'Cadillac' theme = 'Seville' quantity = 79 quantityunit = 'N' )
                                    ( retailerid = 'FIF' sku = '9033357' salesdate = '20210907' description = 'Ford' theme = 'Aerostar' quantity = 274 quantityunit = 'W' )
                                    ( retailerid = 'CTC' sku = '2216403' salesdate = '20210917' description = 'Nissan' theme = 'Rogue' quantity = 420 quantityunit = 'KG' )
                                    ( retailerid = 'QSM' sku = '4747095' salesdate = '20210913' description = 'Acura' theme = 'Legend' quantity = 795 quantityunit = 'FT' )
                                    ( retailerid = 'XFJ' sku = '6275332' salesdate = '20210916' description = 'Dodge' theme = 'Neon' quantity = 892 quantityunit = 'DM' )
                                    ( retailerid = 'GMP' sku = '7250490' salesdate = '20210926' description = 'Jaguar' theme = 'XJ' quantity = 536 quantityunit = 'JMO' )
                                    ( retailerid = 'SZK' sku = '8396732' salesdate = '20210916' description = 'Chevrolet' theme = 'Sportvan G30' quantity = 734 quantityunit = 'GLL' )
                                    ( retailerid = 'FIF' sku = '2212759' salesdate = '20210925' description = 'Ford' theme = 'Mustang' quantity = 98 quantityunit = 'FT' )
                                    ( retailerid = 'GNK' sku = '4936474' salesdate = '20210926' description = 'Mercedes-Benz' theme = 'C-Class' quantity = 474 quantityunit = 'MG' )
                                    ( retailerid = 'IAV' sku = '4012900' salesdate = '20210915' description = 'Mercedes-Benz' theme = '600SEL' quantity = 842 quantityunit = 'JMO' )
                                    ( retailerid = 'MIN' sku = '7166711' salesdate = '20210923' description = 'Mercury' theme = 'Sable' quantity = 896 quantityunit = 'MG' )
                                    ( retailerid = 'GNU' sku = '2676837' salesdate = '20210910' description = 'Nissan' theme = 'Pathfinder' quantity = 456 quantityunit = 'PS' )
                                    ( retailerid = 'GPS' sku = '2424906' salesdate = '20210925' description = 'Dodge' theme = 'Ram Van 3500' quantity = 987 quantityunit = 'MG' )
                                    ( retailerid = 'SKV' sku = '4961295' salesdate = '20210910' description = 'Mercedes-Benz' theme = 'C-Class' quantity = 203 quantityunit = 'GLL' )
                                    ( retailerid = 'IGK' sku = '4180758' salesdate = '20210901' description = 'Ford' theme = 'Crown Victoria' quantity = 404 quantityunit = 'PS' )
                                    ( retailerid = 'ITT' sku = '5919304' salesdate = '20210915' description = 'Oldsmobile' theme = 'Aurora' quantity = 87 quantityunit = 'DM' )
                                    ( retailerid = 'DOF' sku = '7684563' salesdate = '20210904' description = 'Chevrolet' theme = 'Malibu' quantity = 658 quantityunit = 'HAR' )
                                    ( retailerid = 'CMW' sku = '9068799' salesdate = '20210910' description = 'Mazda' theme = 'Familia' quantity = 631 quantityunit = 'DM' )
                                    ( retailerid = 'SNP' sku = '45692' salesdate = '20210903' description = 'Oldsmobile' theme = 'Alero' quantity = 455 quantityunit = 'MG' )
                                    ( retailerid = 'VBL' sku = '8777423' salesdate = '20210926' description = 'Mercedes-Benz' theme = 'SL-Class' quantity = 732 quantityunit = 'KG' )
                                    ( retailerid = 'YNL' sku = '8692712' salesdate = '20210924' description = 'Nissan' theme = 'Sentra' quantity = 759 quantityunit = 'KG' )
                                    ( retailerid = 'DGV' sku = '7573583' salesdate = '20210914' description = 'Chevrolet' theme = 'G-Series G10' quantity = 709 quantityunit = 'N' )
                                    ( retailerid = 'TUM' sku = '7808831' salesdate = '20210930' description = 'Ford' theme = 'Expedition' quantity = 89 quantityunit = 'GLL' )
                                    ( retailerid = 'YNL' sku = '1476193' salesdate = '20211002' description = 'Maybach' theme = '57S' quantity = 819 quantityunit = 'FT' )
                                    ( retailerid = 'BXU' sku = '2391887' salesdate = '20210907' description = 'Lincoln' theme = 'Continental' quantity = 455 quantityunit = 'GLL' )
                                    ( retailerid = 'GWA' sku = '1986171' salesdate = '20210927' description = 'Mercedes-Benz' theme = 'W126' quantity = 114 quantityunit = 'W' )
                                    ( retailerid = 'GYL' sku = '8637280' salesdate = '20210923' description = 'Ford' theme = 'E-Series' quantity = 518 quantityunit = 'GLL' )
                                    ( retailerid = 'OQB' sku = '8637280' salesdate = '20210906' description = 'Ford' theme = 'E-Series' quantity = 401 quantityunit = 'DM' )
                                    ( retailerid = 'DBK' sku = '82005' salesdate = '20210911' description = 'Ford' theme = 'Mustang' quantity = 601 quantityunit = 'MG' )
                                    ( retailerid = 'DAK' sku = '7808831' salesdate = '20210926' description = 'Ford' theme = 'Expedition' quantity = 166 quantityunit = 'JMO' )
                                    ( retailerid = 'SZK' sku = '5440637' salesdate = '20210920' description = 'Chrysler' theme = '200' quantity = 862 quantityunit = 'N' )
                                    ( retailerid = 'AIJ' sku = '4188938' salesdate = '20210926' description = 'Chevrolet' theme = 'Suburban 2500' quantity = 125 quantityunit = 'MG' )

                                            ).

    insert zapo_sales from table @lt_sales.

  endmethod.

endclass.