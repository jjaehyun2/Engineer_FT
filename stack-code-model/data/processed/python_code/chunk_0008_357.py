"
" ABAP transpiler version of Wordle Assistant
"
" Contribution by Marc Bernard
"
" Based on https://github.com/hdegroot/zwordle
" MIT License - Copyright (c) 2022 Hugo de Groot
"
" 1. Open https://transpiler.abaplint.org/
" 2. Cut & paste this code (zwordle.abap) into left window
" 3. Adjust call at end of code
" 4. Runs automatically and shows results in right window
"
class lcl_wordle definition.

  public section.

    types:
      char1        type c length 1,
      char5        type c length 5,
      char6        type c length 6,
      char26       type c length 26,
      string_table type table of string.

    types:
      begin of submatch_result,
        offset type i,
        length type i,
      end of submatch_result,
      submatch_tab type table of submatch_result,
      begin of match_result,
        line   type i,
        offset type i,
        length type i,
        submatches type submatch_tab,
      end of match_result,
      match_result_tab type table of match_result.

    class-data:
      letter1        type char26,
      letter2        type char26,
      letter3        type char26,
      letter4        type char26,
      letter5        type char26,
      black_letters  type char26,
      orange_letters type char26.

    class-methods:
      remove_black_letters.

    methods:
      main
        importing
          i_letter_1       type char26
          i_letter_2       type char26
          i_letter_3       type char26
          i_letter_4       type char26
          i_letter_5       type char26
          i_black_letters  type char26
          i_orange_letters type char26.

  private section.

    types:

      ty_word_score type f, "p length 6 decimals 1,

      begin of ty_matched_word,
        word                        type char5,
        vowel_count                 type i,
        consonant_count             type i,
        contains_all_orange_letters type abap_bool,
        word_score                  type ty_word_score,
      end of ty_matched_word,

      ty_matched_word_tab type standard table of ty_matched_word with default key,

      ty_relative_frequency type f, "p length 6 decimals 4,

      begin of ty_letter_frequency,
        first_letter  type ty_relative_frequency,
        other_letters type ty_relative_frequency,
      end of ty_letter_frequency,

      ty_letter_frequency_tab type standard table of ty_letter_frequency with default key.

    data:
      word_tab             type string_table,
      letter_frequency_tab type ty_letter_frequency_tab,
      regex_string         type string,
      matched_word_tab     type ty_matched_word_tab.

    methods:
      build_word_tab_v2,  "List of 5-letter words. Source: Collins Scrabble Words Dec 2021
      build_letter_frequency_tab, "Letter Frequency for English Dictionary Words
      build_regex_string,
      get_matched_words,
      display_output,

      get_vowel_count             importing i_word type char5 returning value(r_count) type i,
      contains_all_orange_letters importing i_word type char5 returning value(r_contains_all_orange_letters) type abap_bool,
      get_word_score              importing i_word type char5 returning value(r_word_score) type ty_word_score,
      get_letter_frequency        importing i_letter type char1 i_first type abap_bool returning value(r_frequency) type ty_relative_frequency.


endclass.


class lcl_wordle implementation.


  method main.

    data inp type string.

    write / 'WORDLE ASSISTANT'.

    inp = i_letter_1 && i_letter_2 && i_letter_3 && i_letter_4 && i_letter_5 && i_black_letters && i_orange_letters.

    if inp is initial.
      write: /,
        / 'Fill in the parameters of the MAIN method call',
        / 'at the end of the ABAP coding'.
      return.
    endif.

    if i_letter_1 is initial.
      letter1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
    else.
      letter1 = i_letter_1.
    endif.
    if i_letter_2 is initial.
      letter2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
    else.
      letter2 = i_letter_2.
    endif.
    if i_letter_3 is initial.
      letter3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
    else.
      letter3 = i_letter_3.
    endif.
    if i_letter_4 is initial.
      letter4 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
    else.
      letter4 = i_letter_4.
    endif.
    if i_letter_5 is initial.
      letter5 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
    else.
      letter5 = i_letter_5.
    endif.

    black_letters = i_black_letters.

    orange_letters = i_orange_letters.

    remove_black_letters( ).

    build_word_tab_v2( ).

    build_letter_frequency_tab( ).

    build_regex_string( ).

    get_matched_words( ).

    display_output( ).

  endmethod.


  method remove_black_letters.

    data black_letters_regex type string.

    if black_letters is not initial.

      if strlen( black_letters ) = 1.
        black_letters_regex = black_letters+0(1).
      else.
        black_letters_regex = |[{ black_letters }]|.
      endif.

      replace all occurrences of regex black_letters_regex in letter1 with ''.
      replace all occurrences of regex black_letters_regex in letter2 with ''.
      replace all occurrences of regex black_letters_regex in letter3 with ''.
      replace all occurrences of regex black_letters_regex in letter4 with ''.
      replace all occurrences of regex black_letters_regex in letter5 with ''.

    endif.

  endmethod.


  method build_regex_string.

    data:
      vletter1 type string,
      vletter2 type string,
      vletter3 type string,
      vletter4 type string,
      vletter5 type string.

    if letter1 is initial.
      vletter1 = '.'.
    elseif strlen( letter1 ) = 1.
      vletter1 = letter1.
    else.
      vletter1 = |[{ letter1 }]|.
    endif.

    if letter2 is initial.
      vletter2 = '.'.
    elseif strlen( letter2 ) = 1.
      vletter2 = letter2.
    else.
      vletter2 = |[{ letter2 }]|.
    endif.

    if letter3 is initial.
      vletter3 = '.'.
    elseif strlen( letter3 ) = 1.
      vletter3 = letter3.
    else.
      vletter3 = |[{ letter3 }]|.
    endif.

    if letter4 is initial.
      vletter4 = '.'.
    elseif strlen( letter4 ) = 1.
      vletter4 = letter4.
    else.
      vletter4 = |[{ letter4 }]|.
    endif.

    if letter5 is initial.
      vletter5 = '.'.
    elseif strlen( letter5 ) = 1.
      vletter5 = letter5.
    else.
      vletter5 = |[{ letter5 }]|.
    endif.

    regex_string = |^{ vletter1 }{ vletter2 }{ vletter3 }{ vletter4 }{ vletter5 }$|.

  endmethod.


  method get_matched_words.

    data:
      matched_word type ty_matched_word,
      word_word    like line of word_tab.

    loop at word_tab into word_word.

      find regex regex_string in word_word.
      if sy-subrc = 0.

        matched_word-word = word_word.

        matched_word-vowel_count = get_vowel_count( matched_word-word ).

        matched_word-consonant_count = 5 - matched_word-vowel_count.

        matched_word-contains_all_orange_letters = contains_all_orange_letters( matched_word-word ).

        matched_word-word_score = get_word_score( matched_word-word ).

        append matched_word to matched_word_tab.

      endif.

    endloop.

  endmethod.


  method display_output.

    data matched_word like line of matched_word_tab.
    data score type i.

    sort matched_word_tab by contains_all_orange_letters descending
                             word_score descending.

    write: /,
      / 'Black Letters:  ', black_letters,
      / 'Orange Letters: ', orange_letters,
      / 'Letter 1:       ', letter1,
      / 'Letter 2:       ', letter2,
      / 'Letter 3:       ', letter3,
      / 'Letter 4:       ', letter4,
      / 'Letter 5:       ', letter5,
      /.

    write: /
      'Word   ',
      ' ',
      'Vowels',
      ' ',
      'Consonants',
      ' ',
      'All Orange?',
      ' ',
      'Word Score',
      / '------------------------------------------------'.

    loop at matched_word_tab into matched_word.
      score = matched_word-word_score * 100.
      write: /
        matched_word-word,
        '   ',
        matched_word-vowel_count,
        '      ',
        matched_word-consonant_count,
        '          ',
        matched_word-contains_all_orange_letters,
        '           ',
        score.
    endloop.

  endmethod.


  method get_vowel_count.

    data vowels_regex type string value '[AEIOUY]'.

    find all occurrences of regex vowels_regex in i_word
    match count r_count.

  endmethod.


  method contains_all_orange_letters.

    data:
      word             type char6,
      orange1          type c,
      orange2          type c,
      orange3          type c,
      orange4          type c,
      orange5          type c,
      contains_orange1 type abap_bool,
      contains_orange2 type abap_bool,
      contains_orange3 type abap_bool,
      contains_orange4 type abap_bool,
      contains_orange5 type abap_bool.

    r_contains_all_orange_letters = '-'. "abap_false.

    if orange_letters is initial.

      r_contains_all_orange_letters = abap_true.

    else.

      word = i_word.

      orange1 = orange_letters+0(1).
      orange2 = orange_letters+1(1).
      orange3 = orange_letters+2(1).
      orange4 = orange_letters+3(1).
      orange5 = orange_letters+4(1).

      if word ca orange1 or orange1 is initial.
        contains_orange1 = abap_true.
      endif.

      if word ca orange2 or orange2 is initial.
        contains_orange2 = abap_true.
      endif.

      if word ca orange3 or orange3 is initial.
        contains_orange3 = abap_true.
      endif.

      if word ca orange4 or orange4 is initial.
        contains_orange4 = abap_true.
      endif.

      if word ca orange5 or orange5 is initial.
        contains_orange5 = abap_true.
      endif.

      if contains_orange1 = abap_true and
         contains_orange2 = abap_true and
         contains_orange3 = abap_true and
         contains_orange4 = abap_true and
         contains_orange5 = abap_true .

        r_contains_all_orange_letters = abap_true.

      else.

        r_contains_all_orange_letters = '-'. "abap_false.

      endif.

    endif.

  endmethod.


  method get_word_score.

    if strlen( letter1 ) > 1.
      r_word_score = r_word_score + get_letter_frequency( i_letter = i_word+0(1) i_first = abap_true ).
    endif.
    if strlen( letter2 ) > 1.
      r_word_score = r_word_score + get_letter_frequency( i_letter = i_word+1(1) i_first = abap_false ).
    endif.
    if strlen( letter3 ) > 1.
      r_word_score = r_word_score + get_letter_frequency( i_letter = i_word+2(1) i_first = abap_false ).
    endif.
    if strlen( letter4 ) > 1.
      r_word_score = r_word_score + get_letter_frequency( i_letter = i_word+3(1) i_first = abap_false ).
    endif.
    if strlen( letter5 ) > 1.
      r_word_score = r_word_score + get_letter_frequency( i_letter = i_word+4(1) i_first = abap_false ).
    endif.

  endmethod.


  method get_letter_frequency.

    field-symbols <frequency> like line of letter_frequency_tab.

    data v_index type i.

    v_index = find( val = sy-abcde sub = i_letter ) + 1.

    read table letter_frequency_tab assigning <frequency> index v_index.
    assert sy-subrc = 0.

    if i_first = abap_true.
      r_frequency = <frequency>-first_letter.
    else.
      r_frequency = <frequency>-other_letters.
    endif.

  endmethod.


  method build_letter_frequency_tab.

    "
    " Source of Letter Frequency for English Dictionary Words:
    " https://en.wikipedia.org/wiki/Letter_frequency
    "

    data frequency like line of letter_frequency_tab.

    frequency-first_letter  = '5.7'.
    frequency-other_letters = '7.8'. "A
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '6.0'.
    frequency-other_letters = '2.0'. "B
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '9.4'.
    frequency-other_letters = '4.0'. "C
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '6.1'.
    frequency-other_letters = '3.8'. "D
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '3.9'.
    frequency-other_letters = '11.0'. "E
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '4.1'.
    frequency-other_letters = '1.4'. "F
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '3.3'.
    frequency-other_letters = '3.0'. "G
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '3.7'.
    frequency-other_letters = '2.3'. "H
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '3.9'.
    frequency-other_letters = '8.2'. "I
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '1.1'.
    frequency-other_letters = '0.21'. "J
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '1.0'.
    frequency-other_letters = '2.5'. "K
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '3.1'.
    frequency-other_letters = '5.3'. "L
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '5.6'.
    frequency-other_letters = '2.7'. "M
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '2.2'.
    frequency-other_letters = '7.2'. "N
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '2.5'.
    frequency-other_letters = '6.1'. "O
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '7.7'.
    frequency-other_letters = '2.8'. "P
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '0.49'.
    frequency-other_letters = '0.24'. "Q
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '6.0'.
    frequency-other_letters = '7.3'. "R
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '11.0'.
    frequency-other_letters = '8.7'. "S
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '5.0'.
    frequency-other_letters = '6.7'. "T
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '2.9'.
    frequency-other_letters = '3.3'. "U
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '1.5'.
    frequency-other_letters = '1.0'. "V
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '2.7'.
    frequency-other_letters = '0.91'. "W
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '0.05'.
    frequency-other_letters = '0.27'. "X
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '0.36'.
    frequency-other_letters = '1.6'. "Y
    insert frequency into table letter_frequency_tab.
    frequency-first_letter  = '0.24'.
    frequency-other_letters = '0.44'. "Z
    insert frequency into table letter_frequency_tab.

  endmethod.


  method build_word_tab_v2.

    data lv_words type string.

    lv_words =
      'AAHED,AALII,AARGH,AARTI,ABACA,ABACI,ABACK,ABACS,ABAFT,ABAKA,ABAMP,ABAND,ABASE,ABASH,ABASK,ABATE,ABAYA,ABBAS,ABBED,' &&
      'ABBES,ABBEY,ABBOT,ABCEE,ABEAM,ABEAR,ABELE,ABERS,ABETS,ABHOR,ABIDE,ABIES,ABLED,ABLER,ABLES,ABLET,ABLOW,ABMHO,ABODE,' &&
      'ABOHM,ABOIL,ABOMA,ABOON,ABORD,ABORE,ABORT,ABOUT,ABOVE,ABRAM,ABRAY,ABRIM,ABRIN,ABRIS,ABSEY,ABSIT,ABUNA,ABUNE,ABUSE,' &&
      'ABUTS,ABUZZ,ABYES,ABYSM,ABYSS,ACAIS,ACARI,ACCAS,ACCOY,ACERB,ACERS,ACETA,ACHAR,ACHED,ACHES,ACHOO,ACIDS,ACIDY,ACING,' &&
      'ACINI,ACKEE,ACKER,ACMES,ACMIC,ACNED,ACNES,ACOCK,ACOLD,ACORN,ACRED,ACRES,ACRID,ACROS,ACTED,ACTIN,ACTON,ACTOR,ACUTE,' &&
      'ACYLS,ADAGE,ADAPT,ADAWS,ADAYS,ADBOT,ADDAX,ADDED,ADDER,ADDIO,ADDLE,ADEEM,ADEPT,ADHAN,ADIEU,ADIOS,ADITS,ADMAN,ADMEN,' &&
      'ADMIN,ADMIT,ADMIX,ADOBE,ADOBO,ADOPT,ADORE,ADORN,ADOWN,ADOZE,ADRAD,ADRED,ADSUM,ADUKI,ADULT,ADUNC,ADUST,ADVEW,ADYTA,' &&
      'ADZED,ADZES,AECIA,AEDES,AEGIS,AEONS,AERIE,AEROS,AESIR,AFALD,AFARA,AFARS,AFEAR,AFFIX,AFIRE,AFLAJ,AFOOT,AFORE,AFOUL,' &&
      'AFRIT,AFROS,AFTER,AGAIN,AGAMA,AGAMI,AGAPE,AGARS,AGAST,AGATE,AGAVE,AGAZE,AGENE,AGENT,AGERS,AGGER,AGGIE,AGGRI,AGGRO,' &&
      'AGGRY,AGHAS,AGILA,AGILE,AGING,AGIOS,AGISM,AGIST,AGITA,AGLEE,AGLET,AGLEY,AGLOO,AGLOW,AGLUS,AGMAS,AGOGE,AGONE,AGONS,' &&
      'AGONY,AGOOD,AGORA,AGREE,AGRIA,AGRIN,AGROS,AGUED,AGUES,AGUNA,AGUTI,AHEAD,AHEAP,AHENT,AHIGH,AHIND,AHING,AHINT,AHOLD,' &&
      'AHULL,AHURU,AIDAS,AIDED,AIDER,AIDES,AIDOI,AIDOS,AIERY,AIGAS,AIGHT,AILED,AIMED,AIMER,AINEE,AINGA,AIOLI,AIRED,AIRER,' &&
      'AIRNS,AIRTH,AIRTS,AISLE,AITCH,AITUS,AIVER,AIYEE,AIZLE,AJIES,AJIVA,AJUGA,AJWAN,AKEES,AKELA,AKENE,AKING,AKITA,AKKAS,' &&
      'ALAAP,ALACK,ALAMO,ALAND,ALANE,ALANG,ALANS,ALANT,ALAPA,ALAPS,ALARM,ALARY,ALATE,ALAYS,ALBAS,ALBEE,ALBUM,ALCID,ALCOS,' &&
      'ALDEA,ALDER,ALDOL,ALECK,ALECS,ALEFS,ALEFT,ALEPH,ALERT,ALEWS,ALEYE,ALFAS,ALGAE,ALGAL,ALGAS,ALGID,ALGIN,ALGOR,ALGUM,' &&
      'ALIAS,ALIBI,ALIEN,ALIFS,ALIGN,ALIKE,ALINE,ALIST,ALIVE,ALIYA,ALKIE,ALKOS,ALKYD,ALKYL,ALLAY,ALLEE,ALLEL,ALLEY,ALLIS,' &&
      'ALLOD,ALLOT,ALLOW,ALLOY,ALLYL,ALMAH,ALMAS,ALMEH,ALMES,ALMUD,ALMUG,ALODS,ALOED,ALOES,ALOFT,ALOHA,ALOIN,ALONE,ALONG,' &&
      'ALOOF,ALOOS,ALOUD,ALOWE,ALPHA,ALTAR,ALTER,ALTHO,ALTOS,ALULA,ALUMS,ALURE,ALVAR,ALWAY,AMAHS,AMAIN,AMASS,AMATE,AMAUT,' &&
      'AMAZE,AMBAN,AMBER,AMBIT,AMBLE,AMBOS,AMBRY,AMEBA,AMEER,AMEND,AMENE,AMENS,AMENT,AMIAS,AMICE,AMICI,AMIDE,AMIDO,AMIDS,' &&
      'AMIES,AMIGA,AMIGO,AMINE,AMINO,AMINS,AMIRS,AMISS,AMITY,AMLAS,AMMAN,AMMON,AMMOS,AMNIA,AMNIC,AMNIO,AMOKS,AMOLE,AMONG,' &&
      'AMORT,AMOUR,AMOVE,AMOWT,AMPED,AMPLE,AMPLY,AMPUL,AMRIT,AMUCK,AMUSE,AMYLS,ANANA,ANATA,ANCHO,ANCLE,ANCON,ANDRO,ANEAR,' &&
      'ANELE,ANENT,ANGAS,ANGEL,ANGER,ANGLE,ANGLO,ANGRY,ANGST,ANIGH,ANILE,ANILS,ANIMA,ANIME,ANIMI,ANION,ANISE,ANKER,ANKHS,' &&
      'ANKLE,ANKUS,ANLAS,ANNAL,ANNAS,ANNAT,ANNEX,ANNOY,ANNUL,ANOAS,ANODE,ANOLE,ANOMY,ANSAE,ANTAE,ANTAR,ANTAS,ANTED,ANTES,' &&
      'ANTIC,ANTIS,ANTRA,ANTRE,ANTSY,ANURA,ANVIL,ANYON,AORTA,APACE,APAGE,APAID,APART,APAYD,APAYS,APEAK,APEEK,APERS,APERT,' &&
      'APERY,APGAR,APHID,APHIS,APIAN,APING,APIOL,APISH,APISM,APNEA,APODE,APODS,APOOP,APORT,APPAL,APPAY,APPEL,APPLE,APPLY,' &&
      'APPRO,APPUI,APPUY,APRES,APRON,APSES,APSIS,APSOS,APTED,APTER,APTLY,AQUAE,AQUAS,ARABA,ARAKS,ARAME,ARARS,ARBAS,ARBOR,' &&
      'ARCED,ARCHI,ARCOS,ARCUS,ARDEB,ARDOR,ARDRI,AREAD,AREAE,AREAL,AREAR,AREAS,ARECA,AREDD,AREDE,AREFY,AREIC,ARENA,ARENE,' &&
      'AREPA,ARERE,ARETE,ARETS,ARETT,ARGAL,ARGAN,ARGIL,ARGLE,ARGOL,ARGON,ARGOT,ARGUE,ARGUS,ARHAT,ARIAS,ARIEL,ARIKI,ARILS,' &&
      'ARIOT,ARISE,ARISH,ARKED,ARLED,ARLES,ARMED,ARMER,ARMET,ARMIL,ARMOR,ARNAS,ARNUT,AROBA,AROHA,AROID,AROMA,AROSE,ARPAS,' &&
      'ARPEN,ARRAH,ARRAS,ARRAY,ARRET,ARRIS,ARROW,ARROZ,ARSED,ARSES,ARSEY,ARSIS,ARSON,ARTAL,ARTEL,ARTIC,ARTIS,ARTSY,ARUHE,' &&
      'ARUMS,ARVAL,ARVEE,ARVOS,ARYLS,ASANA,ASCON,ASCOT,ASCUS,ASDIC,ASHED,ASHEN,ASHES,ASHET,ASIDE,ASKED,ASKER,ASKEW,ASKOI,' &&
      'ASKOS,ASPEN,ASPER,ASPIC,ASPIS,ASPRO,ASSAI,ASSAM,ASSAY,ASSES,ASSET,ASSEZ,ASSOT,ASTER,ASTIR,ASTUN,ASURA,ASWAY,ASWIM,' &&
      'ASYLA,ATAPS,ATAXY,ATIGI,ATILT,ATIMY,ATLAS,ATMAN,ATMAS,ATMOS,ATOCS,ATOKE,ATOKS,ATOLL,ATOMS,ATOMY,ATONE,ATONY,ATOPY,' &&
      'ATRIA,ATRIP,ATTAP,ATTAR,ATTIC,ATUAS,AUDAD,AUDIO,AUDIT,AUGER,AUGHT,AUGUR,AULAS,AULIC,AULOI,AULOS,AUMIL,AUNES,AUNTS,' &&
      'AUNTY,AURAE,AURAL,AURAR,AURAS,AUREI,AURES,AURIC,AURIS,AURUM,AUTOS,AUXIN,AVAIL,AVALE,AVANT,AVAST,AVELS,AVENS,AVERS,' &&
      'AVERT,AVGAS,AVIAN,AVINE,AVION,AVISE,AVISO,AVIZE,AVOID,AVOWS,AVYZE,AWAIT,AWAKE,AWARD,AWARE,AWARN,AWASH,AWATO,AWAVE,' &&
      'AWAYS,AWDLS,AWEEL,AWETO,AWFUL,AWING,AWMRY,AWNED,AWNER,AWOKE,AWOLS,AWORK,AXELS,AXIAL,AXILE,AXILS,AXING,AXIOM,AXION,' &&
      'AXITE,AXLED,AXLES,AXMAN,AXMEN,AXOID,AXONE,AXONS,AYAHS,AYAYA,AYELP,AYGRE,AYINS,AYONT,AYRES,AYRIE,AZANS,AZIDE,AZIDO,' &&
      'AZINE,AZLON,AZOIC,AZOLE,AZONS,AZOTE,AZOTH,AZUKI,AZURE,AZURN,AZURY,AZYGY,AZYME,AZYMS,BAAED,BAALS,BABAS,BABEL,BABES,' &&
      'BABKA,BABOO,BABUL,BABUS,BACCA,BACCO,BACCY,BACHA,BACHS,BACKS,BACON,BADDY,BADGE,BADLY,BAELS,BAFFS,BAFFY,BAFTS,BAGEL,' &&
      'BAGGY,BAGHS,BAGIE,BAHTS,BAHUS,BAHUT,BAILS,BAIRN,BAISA,BAITH,BAITS,BAIZA,BAIZE,BAJAN,BAJRA,BAJRI,BAJUS,BAKED,BAKEN,' &&
      'BAKER,BAKES,BALAS,BALDS,BALDY,BALED,BALER,BALES,BALKS,BALKY,BALLS,BALLY,BALMS,BALMY,BALOO,BALSA,BALTI,BALUN,BALUS,' &&
      'BAMBI,BANAK,BANAL,BANCO,BANCS,BANDA,BANDH,BANDS,BANDY,BANED,BANES,BANGS,BANIA,BANJO,BANKS,BANNS,BANTS,BANTY,BANYA,' &&
      'BAPUS,BARBE,BARBS,BARBY,BARCA,BARDE,BARDO,BARDS,BARDY,BARED,BARER,BARES,BARFI,BARFS,BARGE,BARIC,BARKS,BARKY,BARMS,' &&
      'BARMY,BARNS,BARNY,BARON,BARPS,BARRA,BARRE,BARRO,BARRY,BARYE,BASAL,BASAN,BASED,BASEN,BASER,BASES,BASHO,BASIC,BASIJ,' &&
      'BASIL,BASIN,BASIS,BASKS,BASON,BASSE,BASSI,BASSO,BASSY,BASTA,BASTE,BASTI,BASTO,BASTS,BATCH,BATED,BATES,BATHE,BATHS,' &&
      'BATIK,BATON,BATTA,BATTS,BATTU,BATTY,BAUDS,BAUKS,BAULK,BAURS,BAVIN,BAWDS,BAWDY,BAWKS,BAWLS,BAWNS,BAWRS,BAWTY,BAYED,' &&
      'BAYER,BAYES,BAYLE,BAYOU,BAYTS,BAZAR,BAZOO,BEACH,BEADS,BEADY,BEAKS,BEAKY,BEALS,BEAMS,BEAMY,BEANO,BEANS,BEANY,BEARD,' &&
      'BEARE,BEARS,BEAST,BEATH,BEATS,BEATY,BEAUS,BEAUT,BEAUX,BEBOP,BECAP,BECKE,BECKS,BEDAD,BEDEL,BEDES,BEDEW,BEDIM,BEDYE,' &&
      'BEECH,BEEDI,BEEFS,BEEFY,BEEPS,BEERS,BEERY,BEETS,BEFIT,BEFOG,BEGAD,BEGAN,BEGAR,BEGAT,BEGEM,BEGET,BEGIN,BEGOT,BEGUM,' &&
      'BEGUN,BEIGE,BEIGY,BEING,BEINS,BEKAH,BELAH,BELAR,BELAY,BELCH,BELEE,BELGA,BELIE,BELLE,BELLS,BELLY,BELON,BELOW,BELTS,' &&
      'BEMAD,BEMAS,BEMIX,BEMUD,BENCH,BENDS,BENDY,BENES,BENET,BENGA,BENIS,BENNE,BENNI,BENNY,BENTO,BENTS,BENTY,BEPAT,BERAY,' &&
      'BERES,BERET,BERGS,BERKO,BERKS,BERME,BERMS,BEROB,BERRY,BERTH,BERYL,BESAT,BESAW,BESEE,BESES,BESET,BESIT,BESOM,BESOT,' &&
      'BESTI,BESTS,BETAS,BETED,BETEL,BETES,BETHS,BETID,BETON,BETTA,BETTY,BEVEL,BEVER,BEVOR,BEVUE,BEVVY,BEWET,BEWIG,BEZEL,' &&
      'BEZES,BEZIL,BEZZY,BHAIS,BHAJI,BHANG,BHATS,BHELS,BHOOT,BHUNA,BHUTS,BIACH,BIALI,BIALY,BIBBS,BIBES,BIBLE,BICCY,BICEP,' &&
      'BICES,BIDDY,BIDED,BIDER,BIDES,BIDET,BIDIS,BIDON,BIELD,BIERS,BIFFO,BIFFS,BIFFY,BIFID,BIGAE,BIGGS,BIGGY,BIGHA,BIGHT,' &&
      'BIGLY,BIGOS,BIGOT,BIJOU,BIKED,BIKER,BIKES,BIKIE,BILBO,BILBY,BILED,BILES,BILGE,BILGY,BILKS,BILLS,BILLY,BIMAH,BIMAS,' &&
      'BIMBO,BINAL,BINDI,BINDS,BINER,BINES,BINGE,BINGO,BINGS,BINGY,BINIT,BINKS,BIOGS,BIOME,BIONT,BIOTA,BIPED,BIPOD,BIRCH,' &&
      'BIRDS,BIRKS,BIRLE,BIRLS,BIROS,BIRRS,BIRSE,BIRSY,BIRTH,BISES,BISKS,BISOM,BISON,BITCH,BITER,BITES,BITOS,BITOU,BITSY,' &&
      'BITTE,BITTS,BITTY,BIVIA,BIVVY,BIZES,BIZZO,BIZZY,BLABS,BLACK,BLADE,BLADS,BLADY,BLAER,BLAES,BLAFF,BLAGS,BLAHS,BLAIN,' &&
      'BLAME,BLAMS,BLAND,BLANK,BLARE,BLART,BLASE,BLASH,BLAST,BLATE,BLATS,BLATT,BLAUD,BLAWN,BLAWS,BLAYS,BLAZE,BLEAK,BLEAR,' &&
      'BLEAT,BLEBS,BLECH,BLEED,BLEEP,BLEES,BLEND,BLENT,BLERT,BLESS,BLEST,BLETS,BLEYS,BLIMP,BLIMY,BLIND,BLING,BLINI,BLINK,' &&
      'BLINS,BLINY,BLIPS,BLISS,BLIST,BLITE,BLITS,BLITZ,BLIVE,BLOAT,BLOBS,BLOCK,BLOCS,BLOGS,BLOKE,BLOND,BLOOD,BLOOK,BLOOM,' &&
      'BLOOP,BLORE,BLOTS,BLOWN,BLOWS,BLOWY,BLUBS,BLUDE,BLUDS,BLUDY,BLUED,BLUER,BLUES,BLUET,BLUEY,BLUFF,BLUID,BLUME,BLUNK,' &&
      'BLUNT,BLURB,BLURS,BLURT,BLUSH,BLYPE,BOABS,BOAKS,BOARD,BOARS,BOART,BOAST,BOATS,BOBAC,BOBAK,BOBAS,BOBBY,BOBOL,BOBOS,' &&
      'BOCCA,BOCCE,BOCCI,BOCKS,BODED,BODES,BODGE,BODHI,BODLE,BOEPS,BOETS,BOEUF,BOFFO,BOFFS,BOGAN,BOGEY,BOGGY,BOGIE,BOGLE,' &&
      'BOGUE,BOGUS,BOHEA,BOHOS,BOILS,BOING,BOINK,BOITE,BOKED,BOKEH,BOKES,BOKOS,BOLAR,BOLAS,BOLDS,BOLES,BOLIX,BOLLS,BOLOS,' &&
      'BOLTS,BOLUS,BOMAS,BOMBE,BOMBO,BOMBS,BONCE,BONDS,BONED,BONER,BONES,BONEY,BONGO,BONGS,BONIE,BONKS,BONNE,BONNY,BONUS,' &&
      'BONZA,BONZE,BOOAI,BOOAY,BOOBS,BOOBY,BOODY,BOOED,BOOFY,BOOGY,BOOHS,BOOKS,BOOKY,BOOLS,BOOMS,BOOMY,BOONS,BOORD,BOORS,' &&
      'BOOSE,BOOST,BOOTH,BOOTS,BOOTY,BOOZE,BOOZY,BOPPY,BORAK,BORAL,BORAS,BORAX,BORDE,BORDS,BORED,BOREE,BOREL,BORER,BORES,' &&
      'BORGO,BORIC,BORKS,BORMS,BORNA,BORNE,BORON,BORTS,BORTY,BORTZ,BOSIE,BOSKS,BOSKY,BOSOM,BOSON,BOSSY,BOSUN,BOTAS,BOTCH,' &&
      'BOTEL,BOTES,BOTHY,BOTTE,BOTTS,BOTTY,BOUGE,BOUGH,BOUKS,BOULE,BOULT,BOUND,BOUNS,BOURD,BOURG,BOURN,BOUSE,BOUSY,BOUTS,' &&
      'BOVID,BOWAT,BOWED,BOWEL,BOWER,BOWES,BOWET,BOWIE,BOWLS,BOWNE,BOWRS,BOWSE,BOXED,BOXEN,BOXER,BOXES,BOXLA,BOXTY,BOYAR,' &&
      'BOYAU,BOYED,BOYFS,BOYGS,BOYLA,BOYOS,BOYSY,BOZOS,BRAAI,BRACE,BRACH,BRACK,BRACT,BRADS,BRAES,BRAGS,BRAID,BRAIL,BRAIN,' &&
      'BRAKE,BRAKS,BRAKY,BRAME,BRAND,BRANE,BRANK,BRANS,BRANT,BRASH,BRASS,BRAST,BRATS,BRAVA,BRAVE,BRAVI,BRAVO,BRAWL,BRAWN,' &&
      'BRAWS,BRAXY,BRAYS,BRAZA,BRAZE,BREAD,BREAK,BREAM,BREDE,BREDS,BREED,BREEM,BREER,BREES,BREID,BREIS,BREME,BRENS,BRENT,' &&
      'BRERE,BRERS,BREVE,BREWS,BREYS,BRIAR,BRIBE,BRICK,BRIDE,BRIEF,BRIER,BRIES,BRIGS,BRIKI,BRIKS,BRILL,BRIMS,BRINE,BRING,' &&
      'BRINK,BRINS,BRINY,BRIOS,BRISE,BRISK,BRISS,BRITH,BRITS,BRITT,BRIZE,BROAD,BROCH,BROCK,BRODS,BROGH,BROGS,BROIL,BROKE,' &&
      'BROME,BROMO,BRONC,BROND,BROOD,BROOK,BROOL,BROOM,BROOS,BROSE,BROSY,BROTH,BROWN,BROWS,BRUGH,BRUIN,BRUIT,BRULE,BRUME,' &&
      'BRUNG,BRUNT,BRUSH,BRUSK,BRUST,BRUTE,BRUTS,BUATS,BUAZE,BUBAL,BUBAS,BUBBE,BUBBY,BUBUS,BUCHU,BUCKO,BUCKS,BUCKU,BUDAS,' &&
      'BUDDY,BUDGE,BUDIS,BUDOS,BUFFA,BUFFE,BUFFI,BUFFO,BUFFS,BUFFY,BUFOS,BUGGY,BUGLE,BUHLS,BUHRS,BUIKS,BUILD,BUILT,BUIST,' &&
      'BUKES,BULBS,BULGE,BULGY,BULKS,BULKY,BULLA,BULLS,BULLY,BULSE,BUMBO,BUMFS,BUMPH,BUMPS,BUMPY,BUNAS,BUNCE,BUNCH,BUNCO,' &&
      'BUNDE,BUNDH,BUNDS,BUNDT,BUNDU,BUNDY,BUNGS,BUNGY,BUNIA,BUNJE,BUNJY,BUNKO,BUNKS,BUNNS,BUNNY,BUNTS,BUNTY,BUNYA,BUOYS,' &&
      'BUPPY,BURAN,BURAS,BURBS,BURDS,BURET,BURFI,BURGH,BURGS,BURIN,BURKA,BURKE,BURKS,BURLS,BURLY,BURNS,BURNT,BUROO,BURPS,' &&
      'BURQA,BURRO,BURRS,BURRY,BURSA,BURSE,BURST,BUSBY,BUSED,BUSES,BUSHY,BUSKS,BUSKY,BUSSU,BUSTI,BUSTS,BUSTY,BUTCH,BUTEO,' &&
      'BUTES,BUTLE,BUTOH,BUTTE,BUTTS,BUTTY,BUTUT,BUTYL,BUXOM,BUYER,BUZZY,BWANA,BWAZI,BYDED,BYDES,BYKED,BYKES,BYLAW,BYRES,' &&
      'BYRLS,BYSSI,BYTES,BYWAY,CAAED,CABAL,CABAS,CABBY,CABER,CABIN,CABLE,CABOB,CABOC,CABRE,CACAO,CACAS,CACHE,CACKS,CACKY,' &&
      'CACTI,CADDY,CADEE,CADES,CADET,CADGE,CADGY,CADIE,CADIS,CADRE,CAECA,CAESE,CAFES,CAFFS,CAGED,CAGER,CAGES,CAGEY,CAGOT,' &&
      'CAHOW,CAIDS,CAINS,CAIRD,CAIRN,CAJON,CAJUN,CAKED,CAKES,CAKEY,CALFS,CALID,CALIF,CALIX,CALKS,CALLA,CALLS,CALMS,CALMY,' &&
      'CALOS,CALPA,CALPS,CALVE,CALYX,CAMAN,CAMAS,CAMEL,CAMEO,CAMES,CAMIS,CAMOS,CAMPI,CAMPO,CAMPS,CAMPY,CAMUS,CANAL,CANDY,' &&
      'CANED,CANEH,CANER,CANES,CANGS,CANID,CANNA,CANNS,CANNY,CANOE,CANON,CANSO,CANST,CANTO,CANTS,CANTY,CAPAS,CAPED,CAPER,' &&
      'CAPES,CAPEX,CAPHS,CAPIZ,CAPLE,CAPON,CAPOS,CAPOT,CAPRI,CAPUL,CAPUT,CARAP,CARAT,CARBO,CARBS,CARBY,CARDI,CARDS,CARDY,' &&
      'CARED,CARER,CARES,CARET,CAREX,CARGO,CARKS,CARLE,CARLS,CARNS,CARNY,CAROB,CAROL,CAROM,CARON,CARPI,CARPS,CARRS,CARRY,' &&
      'CARSE,CARTA,CARTE,CARTS,CARVE,CARVY,CASAS,CASCO,CASED,CASES,CASKS,CASKY,CASTE,CASTS,CASUS,CATCH,CATER,CATES,CATTY,' &&
      'CAUDA,CAUKS,CAULD,CAULK,CAULS,CAUMS,CAUPS,CAURI,CAUSA,CAUSE,CAVAS,CAVED,CAVEL,CAVER,CAVES,CAVIE,CAVIL,CAWED,CAWKS,' &&
      'CAXON,CEASE,CEAZE,CEBID,CECAL,CECUM,CEDAR,CEDED,CEDER,CEDES,CEDIS,CEIBA,CEILI,CEILS,CELEB,CELLA,CELLI,CELLO,CELLS,' &&
      'CELOM,CELTS,CENSE,CENTO,CENTS,CENTU,CEORL,CEPES,CERCI,CERED,CERES,CERGE,CERIA,CERIC,CERNE,CEROC,CEROS,CERTS,CERTY,' &&
      'CESSE,CESTA,CESTI,CETES,CETYL,CEZVE,CHACE,CHACK,CHACO,CHADO,CHADS,CHAFE,CHAFF,CHAFT,CHAIN,CHAIR,CHAIS,CHALK,CHALS,' &&
      'CHAMP,CHAMS,CHANA,CHANG,CHANK,CHANT,CHAOS,CHAPE,CHAPS,CHAPT,CHARA,CHARD,CHARE,CHARK,CHARM,CHARR,CHARS,CHART,CHARY,' &&
      'CHASE,CHASM,CHATS,CHAVE,CHAVS,CHAWK,CHAWS,CHAYA,CHAYS,CHEAP,CHEAT,CHECK,CHEEK,CHEEP,CHEER,CHEFS,CHEKA,CHELA,CHELP,' &&
      'CHEMO,CHEMS,CHERE,CHERT,CHESS,CHEST,CHETH,CHEVY,CHEWS,CHEWY,CHIAO,CHIAS,CHIBS,CHICA,CHICH,CHICK,CHICO,CHICS,CHIDE,' &&
      'CHIEF,CHIEL,CHIKS,CHILD,CHILE,CHILI,CHILL,CHIMB,CHIME,CHIMO,CHIMP,CHINA,CHINE,CHING,CHINK,CHINO,CHINS,CHIPS,CHIRK,' &&
      'CHIRL,CHIRM,CHIRO,CHIRP,CHIRR,CHIRT,CHIRU,CHITS,CHIVE,CHIVS,CHIVY,CHIZZ,CHOCK,CHOCO,CHOCS,CHODE,CHOGS,CHOIL,CHOIR,' &&
      'CHOKE,CHOKO,CHOKY,CHOLA,CHOLI,CHOMP,CHONS,CHOOF,CHOOK,CHOOM,CHOON,CHOPS,CHORD,CHORE,CHOSE,CHOTA,CHOTT,CHOUT,CHOUX,' &&
      'CHOWK,CHOWS,CHUBS,CHUCK,CHUFA,CHUFF,CHUGS,CHUMP,CHUMS,CHUNK,CHURL,CHURN,CHURR,CHUSE,CHUTE,CHUTS,CHYLE,CHYME,CHYND,' &&
      'CIBOL,CIDED,CIDER,CIDES,CIELS,CIGAR,CIGGY,CILIA,CILLS,CIMAR,CIMEX,CINCH,CINCT,CINES,CINQS,CIONS,CIPPI,CIRCA,CIRCS,' &&
      'CIRES,CIRLS,CIRRI,CISCO,CISSY,CISTS,CITAL,CITED,CITER,CITES,CIVES,CIVET,CIVIC,CIVIE,CIVIL,CIVVY,CLACH,CLACK,CLADE,' &&
      'CLADS,CLAES,CLAGS,CLAIM,CLAME,CLAMP,CLAMS,CLANG,CLANK,CLANS,CLAPS,CLAPT,CLARO,CLART,CLARY,CLASH,CLASP,CLASS,CLAST,' &&
      'CLATS,CLAUT,CLAVE,CLAVI,CLAWS,CLAYS,CLEAN,CLEAR,CLEAT,CLECK,CLEEK,CLEEP,CLEFS,CLEFT,CLEGS,CLEIK,CLEMS,CLEPE,CLEPT,' &&
      'CLERK,CLEVE,CLEWS,CLICK,CLIED,CLIES,CLIFF,CLIFT,CLIMB,CLIME,CLINE,CLING,CLINK,CLINT,CLIPE,CLIPS,CLIPT,CLITS,CLOAK,' &&
      'CLOAM,CLOCK,CLODS,CLOFF,CLOGS,CLOKE,CLOMB,CLOMP,CLONE,CLONK,CLONS,CLOOP,CLOOT,CLOPS,CLOSE,CLOTE,CLOTH,CLOTS,CLOUD,' &&
      'CLOUR,CLOUS,CLOUT,CLOVE,CLOWN,CLOWS,CLOYE,CLOYS,CLOZE,CLUBS,CLUCK,CLUED,CLUES,CLUEY,CLUMP,CLUNG,CLUNK,CLYPE,CNIDA,' &&
      'COACH,COACT,COADY,COALA,COALS,COALY,COAPT,COARB,COAST,COATE,COATI,COATS,COBBS,COBBY,COBIA,COBLE,COBRA,COBZA,COCAS,' &&
      'COCCI,COCCO,COCKS,COCKY,COCOA,COCOS,CODAS,CODEC,CODED,CODEN,CODER,CODES,CODEX,CODON,COEDS,COFFS,COGIE,COGON,COGUE,' &&
      'COHAB,COHEN,COHOE,COHOG,COHOS,COIFS,COIGN,COILS,COINS,COIRS,COITS,COKED,COKES,COLAS,COLBY,COLDS,COLED,COLES,COLEY,' &&
      'COLIC,COLIN,COLLS,COLLY,COLOG,COLON,COLOR,COLTS,COLZA,COMAE,COMAL,COMAS,COMBE,COMBI,COMBO,COMBS,COMBY,COMER,COMES,' &&
      'COMET,COMFY,COMIC,COMIX,COMMA,COMMO,COMMS,COMMY,COMPO,COMPS,COMPT,COMTE,COMUS,CONCH,CONDO,CONED,CONES,CONEY,CONFS,' &&
      'CONGA,CONGE,CONGO,CONIA,CONIC,CONIN,CONKS,CONKY,CONNE,CONNS,CONTE,CONTO,CONUS,CONVO,COOCH,COOED,COOEE,COOER,COOEY,' &&
      'COOFS,COOKS,COOKY,COOLS,COOMB,COOMS,COOMY,COONS,COOPS,COOPT,COOST,COOTS,COOZE,COPAL,COPAY,COPED,COPEN,COPER,COPES,' &&
      'COPPY,COPRA,COPSE,COPSY,COQUI,CORAL,CORAM,CORBE,CORBY,CORDS,CORED,CORER,CORES,COREY,CORGI,CORIA,CORKS,CORKY,CORMS,' &&
      'CORNI,CORNO,CORNS,CORNU,CORNY,CORPS,CORSE,CORSO,COSEC,COSED,COSES,COSET,COSEY,COSIE,COSTA,COSTE,COSTS,COTAN,COTED,' &&
      'COTES,COTHS,COTTA,COTTS,COUCH,COUDE,COUGH,COULD,COUNT,COUPE,COUPS,COURB,COURD,COURE,COURS,COURT,COUTA,COUTH,COVED,' &&
      'COVEN,COVER,COVES,COVET,COVEY,COVIN,COWAL,COWAN,COWED,COWER,COWKS,COWLS,COWPS,COWRY,COXAE,COXAL,COXED,COXES,COXIB,' &&
      'COYAU,COYED,COYER,COYLY,COYPU,COZED,COZEN,COZES,COZEY,COZIE,CRAAL,CRABS,CRACK,CRAFT,CRAGS,CRAIC,CRAIG,CRAKE,CRAME,' &&
      'CRAMP,CRAMS,CRANE,CRANK,CRANS,CRAPE,CRAPS,CRAPY,CRARE,CRASH,CRASS,CRATE,CRAVE,CRAWL,CRAWS,CRAYS,CRAZE,CRAZY,CREAK,' &&
      'CREAM,CREDO,CREDS,CREED,CREEK,CREEL,CREEP,CREES,CREME,CREMS,CRENA,CREPE,CREPS,CREPT,CREPY,CRESS,CREST,CREWE,CREWS,' &&
      'CRIAS,CRIBS,CRICK,CRIED,CRIER,CRIES,CRIME,CRIMP,CRIMS,CRINE,CRIOS,CRIPE,CRISE,CRISP,CRITH,CRITS,CROAK,CROCI,CROCK,' &&
      'CROCS,CROFT,CROGS,CROMB,CROME,CRONE,CRONK,CRONS,CRONY,CROOK,CROOL,CROON,CROPS,CRORE,CROSS,CROST,CROUP,CROUT,CROWD,' &&
      'CROWN,CROWS,CROZE,CRUCK,CRUDE,CRUDO,CRUDS,CRUDY,CRUEL,CRUES,CRUET,CRUFT,CRUMB,CRUMP,CRUNK,CRUOR,CRURA,CRUSE,CRUSH,' &&
      'CRUST,CRUSY,CRUVE,CRWTH,CRYER,CRYPT,CTENE,CUBBY,CUBEB,CUBED,CUBER,CUBES,CUBIC,CUBIT,CUDDY,CUFFO,CUFFS,CUIFS,CUING,' &&
      'CUISH,CUITS,CUKES,CULCH,CULET,CULEX,CULLS,CULLY,CULMS,CULPA,CULTI,CULTS,CULTY,CUMEC,CUMIN,CUNDY,CUNEI,CUNIT,CUNTS,' &&
      'CUPEL,CUPID,CUPPA,CUPPY,CURAT,CURBS,CURCH,CURDS,CURDY,CURED,CURER,CURES,CURET,CURFS,CURIA,CURIE,CURIO,CURLI,CURLS,' &&
      'CURLY,CURNS,CURNY,CURRS,CURRY,CURSE,CURSI,CURST,CURVE,CURVY,CUSEC,CUSHY,CUSKS,CUSPS,CUSPY,CUSSO,CUSUM,CUTCH,CUTER,' &&
      'CUTES,CUTEY,CUTIE,CUTIN,CUTIS,CUTTO,CUTTY,CUTUP,CUVEE,CUZES,CWTCH,CYANO,CYANS,CYBER,CYCAD,CYCAS,CYCLE,CYCLO,CYDER,' &&
      'CYLIX,CYMAE,CYMAR,CYMAS,CYMES,CYMOL,CYNIC,CYSTS,CYTES,CYTON,CZARS,DAALS,DABBA,DACES,DACHA,DACKS,DADAH,DADAS,DADDY,' &&
      'DADOS,DAFFS,DAFFY,DAGGA,DAGGY,DAHLS,DAIKO,DAILY,DAINE,DAINT,DAIRY,DAISY,DAKER,DALED,DALES,DALIS,DALLE,DALLY,DALTS,' &&
      'DAMAN,DAMAR,DAMES,DAMME,DAMNS,DAMPS,DAMPY,DANCE,DANCY,DANDY,DANGS,DANIO,DANKS,DANNY,DANTS,DARAF,DARBS,DARCY,DARED,' &&
      'DARER,DARES,DARGA,DARGS,DARIC,DARIS,DARKS,DARNS,DARRE,DARTS,DARZI,DASHI,DASHY,DATAL,DATED,DATER,DATES,DATOS,DATTO,' &&
      'DATUM,DAUBE,DAUBS,DAUBY,DAUDS,DAULT,DAUNT,DAURS,DAUTS,DAVEN,DAVIT,DAWAH,DAWDS,DAWED,DAWEN,DAWKS,DAWNS,DAWTS,DAYAN,' &&
      'DAYCH,DAYNT,DAZED,DAZER,DAZES,DEADS,DEAIR,DEALS,DEALT,DEANS,DEARE,DEARN,DEARS,DEARY,DEASH,DEATH,DEAVE,DEAWS,DEAWY,' &&
      'DEBAG,DEBAR,DEBBY,DEBEL,DEBES,DEBIT,DEBTS,DEBUD,DEBUG,DEBUR,DEBUS,DEBUT,DEBYE,DECAD,DECAF,DECAL,DECAN,DECAY,DECKO,' &&
      'DECKS,DECOR,DECOS,DECOY,DECRY,DEDAL,DEEDS,DEEDY,DEELY,DEEMS,DEENS,DEEPS,DEERE,DEERS,DEETS,DEEVE,DEEVS,DEFAT,DEFER,' &&
      'DEFFO,DEFIS,DEFOG,DEGAS,DEGUM,DEGUS,DEICE,DEIDS,DEIFY,DEIGN,DEILS,DEISM,DEIST,DEITY,DEKED,DEKES,DEKKO,DELAY,DELED,' &&
      'DELES,DELFS,DELFT,DELIS,DELLS,DELLY,DELOS,DELPH,DELTA,DELTS,DELVE,DEMAN,DEMES,DEMIC,DEMIT,DEMOB,DEMOI,DEMON,DEMOS,' &&
      'DEMPT,DEMUR,DENAR,DENAY,DENCH,DENES,DENET,DENIM,DENIS,DENSE,DENTS,DEOXY,DEPOT,DEPTH,DERAT,DERAY,DERBY,DERED,DERES,' &&
      'DERIG,DERMA,DERMS,DERNS,DERNY,DEROS,DERRO,DERRY,DERTH,DERVS,DESEX,DESHI,DESIS,DESKS,DESSE,DETER,DETOX,DEUCE,DEVAS,' &&
      'DEVEL,DEVIL,DEVIS,DEVON,DEVOS,DEVOT,DEWAN,DEWAR,DEWAX,DEWED,DEXES,DEXIE,DHABA,DHAKS,DHALS,DHIKR,DHOBI,DHOLE,DHOLL,' &&
      'DHOLS,DHOTI,DHOWS,DHUTI,DIACT,DIALS,DIANE,DIARY,DIAZO,DIBBS,DICED,DICER,DICES,DICEY,DICHT,DICKS,DICKY,DICOT,DICTA,' &&
      'DICTS,DICTY,DIDDY,DIDIE,DIDOS,DIDST,DIEBS,DIELS,DIENE,DIETS,DIFFS,DIGHT,DIGIT,DIKAS,DIKED,DIKER,DIKES,DILDO,DILLI,' &&
      'DILLS,DILLY,DIMBO,DIMER,DIMES,DIMLY,DIMPS,DINAR,DINED,DINER,DINES,DINGE,DINGO,DINGS,DINGY,DINIC,DINKS,DINKY,DINNA,' &&
      'DINOS,DINTS,DIODE,DIOLS,DIOTA,DIPPY,DIPSO,DIRAM,DIRER,DIRGE,DIRKE,DIRKS,DIRLS,DIRTS,DIRTY,DISAS,DISCI,DISCO,DISCS,' &&
      'DISHY,DISKS,DISME,DITAL,DITAS,DITCH,DITED,DITES,DITSY,DITTO,DITTS,DITTY,DITZY,DIVAN,DIVAS,DIVED,DIVER,DIVES,DIVIS,' &&
      'DIVNA,DIVOS,DIVOT,DIVVY,DIWAN,DIXIE,DIXIT,DIYAS,DIZEN,DIZZY,DJINN,DJINS,DOABS,DOATS,DOBBY,DOBES,DOBIE,DOBLA,DOBRA,' &&
      'DOBRO,DOCHT,DOCKS,DOCOS,DOCUS,DODDY,DODGE,DODGY,DODOS,DOEKS,DOERS,DOEST,DOETH,DOFFS,DOGES,DOGEY,DOGGO,DOGGY,DOGIE,' &&
      'DOGMA,DOHYO,DOILT,DOILY,DOING,DOITS,DOJOS,DOLCE,DOLCI,DOLED,DOLES,DOLIA,DOLLS,DOLLY,DOLMA,DOLOR,DOLOS,DOLTS,DOMAL,' &&
      'DOMED,DOMES,DOMIC,DONAH,DONAS,DONEE,DONER,DONGA,DONGS,DONKO,DONNA,DONNE,DONNY,DONOR,DONSY,DONUT,DOOBS,DOOCE,DOODY,' &&
      'DOOKS,DOOLE,DOOLS,DOOLY,DOOMS,DOOMY,DOONA,DOORN,DOORS,DOOZY,DOPAS,DOPED,DOPER,DOPES,DOPEY,DORAD,DORBA,DORBS,DOREE,' &&
      'DORES,DORIC,DORIS,DORKS,DORKY,DORMS,DORMY,DORPS,DORRS,DORSA,DORSE,DORTS,DORTY,DOSAI,DOSAS,DOSED,DOSEH,DOSER,DOSES,' &&
      'DOSHA,DOTAL,DOTED,DOTER,DOTES,DOTTY,DOUAR,DOUBT,DOUCE,DOUCS,DOUGH,DOUKS,DOULA,DOUMA,DOUMS,DOUPS,DOURA,DOUSE,DOUTS,' &&
      'DOVED,DOVEN,DOVER,DOVES,DOVIE,DOWAR,DOWDS,DOWDY,DOWED,DOWEL,DOWER,DOWIE,DOWLE,DOWLS,DOWLY,DOWNA,DOWNS,DOWNY,DOWPS,' &&
      'DOWRY,DOWSE,DOWTS,DOXED,DOXES,DOXIE,DOYEN,DOYLY,DOZED,DOZEN,DOZER,DOZES,DRABS,DRACK,DRACO,DRAFF,DRAFT,DRAGS,DRAIL,' &&
      'DRAIN,DRAKE,DRAMA,DRAMS,DRANK,DRANT,DRAPE,DRAPS,DRATS,DRAVE,DRAWL,DRAWN,DRAWS,DRAYS,DREAD,DREAM,DREAR,DRECK,DREED,' &&
      'DREER,DREES,DREGS,DREKS,DRENT,DRERE,DRESS,DREST,DREYS,DRIBS,DRICE,DRIED,DRIER,DRIES,DRIFT,DRILL,DRILY,DRINK,DRIPS,' &&
      'DRIPT,DRIVE,DROID,DROIL,DROIT,DROKE,DROLE,DROLL,DROME,DRONE,DRONY,DROOB,DROOG,DROOK,DROOL,DROOP,DROPS,DROPT,DROSS,' &&
      'DROUK,DROVE,DROWN,DROWS,DRUBS,DRUGS,DRUID,DRUMS,DRUNK,DRUPE,DRUSE,DRUSY,DRUXY,DRYAD,DRYAS,DRYER,DRYLY,DSOBO,DSOMO,' &&
      'DUADS,DUALS,DUANS,DUARS,DUBBO,DUCAL,DUCAT,DUCES,DUCHY,DUCKS,DUCKY,DUCTS,DUDDY,DUDED,DUDES,DUELS,DUETS,DUETT,DUFFS,' &&
      'DUFUS,DUING,DUITS,DUKAS,DUKED,DUKES,DUKKA,DULCE,DULES,DULIA,DULLS,DULLY,DULSE,DUMAS,DUMBO,DUMBS,DUMKA,DUMKY,DUMMY,' &&
      'DUMPS,DUMPY,DUNAM,DUNCE,DUNCH,DUNES,DUNGS,DUNGY,DUNKS,DUNNO,DUNNY,DUNSH,DUNTS,DUOMI,DUOMO,DUPED,DUPER,DUPES,DUPLE,' &&
      'DUPLY,DUPPY,DURAL,DURAS,DURED,DURES,DURGY,DURNS,DUROC,DUROS,DUROY,DURRA,DURRS,DURRY,DURST,DURUM,DURZI,DUSKS,DUSKY,' &&
      'DUSTS,DUSTY,DUTCH,DUVET,DUXES,DWAAL,DWALE,DWALM,DWAMS,DWANG,DWARF,DWAUM,DWEEB,DWELL,DWELT,DWILE,DWINE,DYADS,DYERS,' &&
      'DYING,DYKED,DYKES,DYKON,DYNEL,DYNES,DZHOS,EAGER,EAGLE,EAGRE,EALED,EALES,EANED,EARDS,EARED,EARLS,EARLY,EARNS,EARNT,' &&
      'EARST,EARTH,EASED,EASEL,EASER,EASES,EASLE,EASTS,EATEN,EATER,EATHE,EAVED,EAVES,EBBED,EBBET,EBONS,EBONY,EBOOK,ECADS,' &&
      'ECHED,ECHES,ECHOS,ECLAT,ECRUS,EDEMA,EDGED,EDGER,EDGES,EDICT,EDIFY,EDILE,EDITS,EDUCE,EDUCT,EEJIT,EENSY,EERIE,EEVEN,' &&
      'EEVNS,EFFED,EGADS,EGERS,EGEST,EGGAR,EGGED,EGGER,EGMAS,EGRET,EHING,EIDER,EIDOS,EIGHT,EIGNE,EIKED,EIKON,EILDS,EISEL,' &&
      'EJECT,EJIDO,EKING,EKKAS,ELAIN,ELAND,ELANS,ELATE,ELBOW,ELCHI,ELDER,ELDIN,ELECT,ELEGY,ELEMI,ELFED,ELFIN,ELIAD,ELIDE,' &&
      'ELINT,ELITE,ELMEN,ELOGE,ELOGY,ELOIN,ELOPE,ELOPS,ELPEE,ELSIN,ELUDE,ELUTE,ELVAN,ELVEN,ELVER,ELVES,EMACS,EMAIL,EMBAR,' &&
      'EMBAY,EMBED,EMBER,EMBOG,EMBOW,EMBOX,EMBUS,EMCEE,EMEER,EMEND,EMERG,EMERY,EMEUS,EMICS,EMIRS,EMITS,EMMAS,EMMER,EMMET,' &&
      'EMMEW,EMMYS,EMOJI,EMONG,EMOTE,EMOVE,EMPTS,EMPTY,EMULE,EMURE,EMYDE,EMYDS,ENACT,ENARM,ENATE,ENDED,ENDER,ENDEW,ENDOW,' &&
      'ENDUE,ENEMA,ENEMY,ENEWS,ENFIX,ENIAC,ENJOY,ENLIT,ENMEW,ENNOG,ENNUI,ENOKI,ENOLS,ENORM,ENOWS,ENROL,ENSEW,ENSKY,ENSUE,' &&
      'ENTER,ENTIA,ENTRY,ENURE,ENURN,ENVOI,ENVOY,ENZYM,EORLS,EOSIN,EPACT,EPEES,EPHAH,EPHAS,EPHOD,EPHOR,EPICS,EPOCH,EPODE,' &&
      'EPOPT,EPOXY,EPRIS,EQUAL,EQUES,EQUID,EQUIP,ERASE,ERBIA,ERECT,EREVS,ERGON,ERGOS,ERGOT,ERHUS,ERICA,ERICK,ERICS,ERING,' &&
      'ERNED,ERNES,ERODE,EROSE,ERRED,ERROR,ERSES,ERUCT,ERUGO,ERUPT,ERUVS,ERVEN,ERVIL,ESCAR,ESCOT,ESILE,ESKAR,ESKER,ESNES,' &&
      'ESSAY,ESSES,ESTER,ESTOC,ESTOP,ESTRO,ETAGE,ETAPE,ETATS,ETENS,ETHAL,ETHER,ETHIC,ETHNE,ETHOS,ETHYL,ETICS,ETNAS,ETTIN,' &&
      'ETTLE,ETUDE,ETUIS,ETWEE,ETYMA,EUGHS,EUKED,EUPAD,EUROS,EUSOL,EVADE,EVENS,EVENT,EVERT,EVERY,EVETS,EVHOE,EVICT,EVILS,' &&
      'EVITE,EVOHE,EVOKE,EWERS,EWEST,EWHOW,EWKED,EXACT,EXALT,EXAMS,EXCEL,EXEAT,EXECS,EXEEM,EXEME,EXERT,EXFIL,EXIES,EXILE,' &&
      'EXINE,EXING,EXIST,EXITS,EXODE,EXOME,EXONS,EXPAT,EXPEL,EXPOS,EXTOL,EXTRA,EXUDE,EXULS,EXULT,EXURB,EYASS,EYERS,EYING,' &&
      'EYOTS,EYRAS,EYRES,EYRIE,EYRIR,EZINE,FABBY,FABLE,FACED,FACER,FACES,FACET,FACIA,FACTA,FACTS,FADDY,FADED,FADER,FADES,' &&
      'FADGE,FADOS,FAENA,FAERY,FAFFS,FAFFY,FAGIN,FAGOT,FAIKS,FAILS,FAINE,FAINS,FAINT,FAIRS,FAIRY,FAITH,FAKED,FAKER,FAKES,' &&
      'FAKEY,FAKIE,FAKIR,FALAJ,FALLS,FALSE,FAMED,FAMES,FANAL,FANCY,FANDS,FANES,FANGA,FANGO,FANGS,FANKS,FANNY,FANON,FANOS,' &&
      'FANUM,FAQIR,FARAD,FARCE,FARCI,FARCY,FARDS,FARED,FARER,FARES,FARLE,FARLS,FARMS,FAROS,FARRO,FARSE,FARTS,FASCI,FASTI,' &&
      'FASTS,FATAL,FATED,FATES,FATLY,FATSO,FATTY,FATWA,FAUGH,FAULD,FAULT,FAUNA,FAUNS,FAURD,FAUTS,FAUVE,FAVAS,FAVEL,FAVER,' &&
      'FAVES,FAVOR,FAVUS,FAWNS,FAWNY,FAXED,FAXES,FAYED,FAYER,FAYNE,FAYRE,FAZED,FAZES,FEALS,FEARE,FEARS,FEART,FEASE,FEAST,' &&
      'FEATS,FEAZE,FECAL,FECES,FECHT,FECIT,FECKS,FEDEX,FEEBS,FEEDS,FEELS,FEENS,FEERS,FEESE,FEEZE,FEHME,FEIGN,FEINT,FEIST,' &&
      'FELCH,FELID,FELLA,FELLS,FELLY,FELON,FELTS,FELTY,FEMAL,FEMES,FEMME,FEMMY,FEMUR,FENCE,FENDS,FENDY,FENIS,FENKS,FENNY,' &&
      'FENTS,FEODS,FEOFF,FERAL,FERER,FERES,FERIA,FERLY,FERMI,FERMS,FERNS,FERNY,FERRY,FESSE,FESTA,FESTS,FESTY,FETAL,FETAS,' &&
      'FETCH,FETED,FETES,FETID,FETOR,FETTA,FETTS,FETUS,FETWA,FEUAR,FEUDS,FEUED,FEVER,FEWER,FEYED,FEYER,FEYLY,FEZES,FEZZY,' &&
      'FIARS,FIATS,FIBER,FIBRE,FIBRO,FICES,FICHE,FICHU,FICIN,FICOS,FICUS,FIDES,FIDGE,FIDOS,FIEFS,FIELD,FIEND,FIENT,FIERE,' &&
      'FIERS,FIERY,FIEST,FIFED,FIFER,FIFES,FIFIS,FIFTH,FIFTY,FIGGY,FIGHT,FIGOS,FIKED,FIKES,FILAR,FILCH,FILED,FILER,FILES,' &&
      'FILET,FILII,FILKS,FILLE,FILLO,FILLS,FILLY,FILMI,FILMS,FILMY,FILOS,FILTH,FILUM,FINAL,FINCA,FINCH,FINDS,FINED,FINER,' &&
      'FINES,FINIS,FINKS,FINNY,FINOS,FIORD,FIQHS,FIQUE,FIRED,FIRER,FIRES,FIRIE,FIRKS,FIRMS,FIRNS,FIRRY,FIRST,FIRTH,FISCS,' &&
      'FISHY,FISKS,FISTS,FISTY,FITCH,FITLY,FITNA,FITTE,FITTS,FIVER,FIVES,FIXED,FIXER,FIXES,FIXIT,FIZZY,FJELD,FJORD,FLABS,' &&
      'FLACK,FLAFF,FLAGS,FLAIL,FLAIR,FLAKE,FLAKS,FLAKY,FLAME,FLAMM,FLAMS,FLAMY,FLANE,FLANK,FLANS,FLAPS,FLARE,FLARY,FLASH,' &&
      'FLASK,FLATS,FLAVA,FLAWN,FLAWS,FLAWY,FLAXY,FLAYS,FLEAM,FLEAS,FLECK,FLEEK,FLEER,FLEES,FLEET,FLEGS,FLEME,FLESH,FLEUR,' &&
      'FLEWS,FLEXI,FLEXO,FLEYS,FLICK,FLICS,FLIED,FLIER,FLIES,FLIMP,FLIMS,FLING,FLINT,FLIPS,FLIRS,FLIRT,FLISK,FLITE,FLITS,' &&
      'FLITT,FLOAT,FLOBS,FLOCK,FLOCS,FLOES,FLOGS,FLONG,FLOOD,FLOOR,FLOPS,FLORA,FLORS,FLORY,FLOSH,FLOSS,FLOTA,FLOTE,FLOUR,' &&
      'FLOUT,FLOWN,FLOWS,FLUBS,FLUED,FLUES,FLUEY,FLUFF,FLUID,FLUKE,FLUKY,FLUME,FLUMP,FLUNG,FLUNK,FLUOR,FLURR,FLUSH,FLUTE,' &&
      'FLUTY,FLUYT,FLYBY,FLYER,FLYPE,FLYTE,FOALS,FOAMS,FOAMY,FOCAL,FOCUS,FOEHN,FOGEY,FOGGY,FOGIE,FOGLE,FOGOU,FOHNS,FOIDS,' &&
      'FOILS,FOINS,FOIST,FOLDS,FOLEY,FOLIA,FOLIC,FOLIE,FOLIO,FOLKS,FOLKY,FOLLY,FOMES,FONDA,FONDS,FONDU,FONES,FONLY,FONTS,' &&
      'FOODS,FOODY,FOOLS,FOOTS,FOOTY,FORAM,FORAY,FORBS,FORBY,FORCE,FORDO,FORDS,FOREL,FORES,FOREX,FORGE,FORGO,FORKS,FORKY,' &&
      'FORME,FORMS,FORTE,FORTH,FORTS,FORTY,FORUM,FORZA,FORZE,FOSSA,FOSSE,FOUAT,FOUDS,FOUER,FOUET,FOULE,FOULS,FOUND,FOUNT,' &&
      'FOURS,FOUTH,FOVEA,FOWLS,FOWTH,FOXED,FOXES,FOXIE,FOYER,FOYLE,FOYNE,FRABS,FRACK,FRACT,FRAGS,FRAIL,FRAIM,FRAME,FRANC,' &&
      'FRANK,FRAPE,FRAPS,FRASS,FRATE,FRATI,FRATS,FRAUD,FRAUS,FRAYS,FREAK,FREED,FREER,FREES,FREET,FREIT,FREMD,FRENA,FREON,' &&
      'FRERE,FRESH,FRETS,FRIAR,FRIBS,FRIED,FRIER,FRIES,FRIGS,FRILL,FRISE,FRISK,FRIST,FRITH,FRITS,FRITT,FRITZ,FRIZE,FRIZZ,' &&
      'FROCK,FROES,FROGS,FROND,FRONS,FRONT,FRORE,FRORN,FRORY,FROSH,FROST,FROTH,FROWN,FROWS,FROWY,FROZE,FRUGS,FRUIT,FRUMP,' &&
      'FRUSH,FRUST,FRYER,FUBAR,FUBBY,FUBSY,FUCKS,FUCUS,FUDDY,FUDGE,FUDGY,FUELS,FUERO,FUFFS,FUFFY,FUGAL,FUGGY,FUGIE,FUGIO,' &&
      'FUGLE,FUGLY,FUGUE,FUGUS,FUJIS,FULLS,FULLY,FUMED,FUMER,FUMES,FUMET,FUNDI,FUNDS,FUNDY,FUNGI,FUNGO,FUNGS,FUNKS,FUNKY,' &&
      'FUNNY,FURAL,FURAN,FURCA,FURLS,FUROL,FUROR,FURRS,FURRY,FURTH,FURZE,FURZY,FUSED,FUSEE,FUSEL,FUSES,FUSIL,FUSKS,FUSSY,' &&
      'FUSTS,FUSTY,FUTON,FUZED,FUZEE,FUZES,FUZIL,FUZZY,FYCES,FYKED,FYKES,FYLES,FYRDS,FYTTE,GABBA,GABBY,GABLE,GADDI,GADES,' &&
      'GADGE,GADID,GADIS,GADJE,GADJO,GADSO,GAFFE,GAFFS,GAGED,GAGER,GAGES,GAIDS,GAILY,GAINS,GAIRS,GAITA,GAITS,GAITT,GAJOS,' &&
      'GALAH,GALAS,GALAX,GALEA,GALED,GALES,GALLS,GALLY,GALOP,GALUT,GALVO,GAMAS,GAMAY,GAMBA,GAMBE,GAMBO,GAMBS,GAMED,GAMER,' &&
      'GAMES,GAMEY,GAMIC,GAMIN,GAMMA,GAMME,GAMMY,GAMPS,GAMUT,GANCH,GANDY,GANEF,GANEV,GANGS,GANJA,GANOF,GANTS,GAOLS,GAPED,' &&
      'GAPER,GAPES,GAPOS,GAPPY,GARBE,GARBO,GARBS,GARDA,GARES,GARIS,GARMS,GARNI,GARRE,GARTH,GARUM,GASES,GASPS,GASPY,GASSY,' &&
      'GASTS,GATCH,GATED,GATER,GATES,GATHS,GATOR,GAUCH,GAUCY,GAUDS,GAUDY,GAUGE,GAUJE,GAULT,GAUMS,GAUMY,GAUNT,GAUPS,GAURS,' &&
      'GAUSS,GAUZE,GAUZY,GAVEL,GAVOT,GAWCY,GAWDS,GAWKS,GAWKY,GAWPS,GAWSY,GAYAL,GAYER,GAYLY,GAZAL,GAZAR,GAZED,GAZER,GAZES,' &&
      'GAZON,GAZOO,GEALS,GEANS,GEARE,GEARS,GEATS,GEBUR,GECKO,GECKS,GEEKS,GEEKY,GEEPS,GEESE,GEEST,GEIST,GEITS,GELDS,GELEE,' &&
      'GELID,GELLY,GELTS,GEMEL,GEMMA,GEMMY,GEMOT,GENAL,GENAS,GENES,GENET,GENIC,GENIE,GENII,GENIP,GENNY,GENOA,GENOM,GENRE,' &&
      'GENRO,GENTS,GENTY,GENUA,GENUS,GEODE,GEOID,GERAH,GERBE,GERES,GERLE,GERMS,GERMY,GERNE,GESSE,GESSO,GESTE,GESTS,GETAS,' &&
      'GETUP,GEUMS,GEYAN,GEYER,GHAST,GHATS,GHAUT,GHAZI,GHEES,GHEST,GHOST,GHOUL,GHYLL,GIANT,GIBED,GIBEL,GIBER,GIBES,GIBLI,' &&
      'GIBUS,GIDDY,GIFTS,GIGAS,GIGHE,GIGOT,GIGUE,GILAS,GILDS,GILET,GILLS,GILLY,GILPY,GILTS,GIMEL,GIMME,GIMPS,GIMPY,GINCH,' &&
      'GINGE,GINGS,GINKS,GINNY,GIPON,GIPPY,GIPSY,GIRDS,GIRLS,GIRLY,GIRNS,GIRON,GIROS,GIRRS,GIRSH,GIRTH,GIRTS,GISMO,GISMS,' &&
      'GISTS,GITCH,GITES,GIUST,GIVED,GIVEN,GIVER,GIVES,GIZMO,GLACE,GLADE,GLADS,GLADY,GLAIK,GLAIR,GLAMS,GLAND,GLANS,GLARE,' &&
      'GLARY,GLASS,GLAUM,GLAUR,GLAZE,GLAZY,GLEAM,GLEAN,GLEBA,GLEBE,GLEBY,GLEDE,GLEDS,GLEED,GLEEK,GLEES,GLEET,GLEIS,GLENS,' &&
      'GLENT,GLEYS,GLIAL,GLIAS,GLIBS,GLIDE,GLIFF,GLIFT,GLIKE,GLIME,GLIMS,GLINT,GLISK,GLITS,GLITZ,GLOAM,GLOAT,GLOBE,GLOBI,' &&
      'GLOBS,GLOBY,GLODE,GLOGG,GLOMS,GLOOM,GLOOP,GLOPS,GLORY,GLOSS,GLOST,GLOUT,GLOVE,GLOWS,GLOZE,GLUED,GLUER,GLUES,GLUEY,' &&
      'GLUGS,GLUME,GLUMS,GLUON,GLUTE,GLUTS,GLYPH,GNARL,GNARR,GNARS,GNASH,GNATS,GNAWN,GNAWS,GNOME,GNOWS,GOADS,GOAFS,GOALS,' &&
      'GOARY,GOATS,GOATY,GOBAN,GOBAR,GOBBI,GOBBO,GOBBY,GOBIS,GOBOS,GODET,GODLY,GODSO,GOELS,GOERS,GOEST,GOETH,GOETY,GOFER,' &&
      'GOFFS,GOGGA,GOGOS,GOIER,GOING,GOJIS,GOLDS,GOLDY,GOLEM,GOLES,GOLFS,GOLLY,GOLPE,GOLPS,GOMBO,GOMER,GOMPA,GONAD,GONCH,' &&
      'GONEF,GONER,GONGS,GONIA,GONIF,GONKS,GONNA,GONOF,GONYS,GONZO,GOOBY,GOODS,GOODY,GOOEY,GOOFS,GOOFY,GOOGS,GOOKS,GOOKY,' &&
      'GOOLD,GOOLS,GOOLY,GOONS,GOONY,GOOPS,GOOPY,GOORS,GOORY,GOOSE,GOOSY,GOPAK,GOPIK,GORAL,GORAS,GORED,GORES,GORGE,GORIS,' &&
      'GORMS,GORMY,GORPS,GORSE,GORSY,GOSHT,GOSSE,GOTCH,GOTHS,GOTHY,GOTTA,GOUCH,GOUGE,GOUKS,GOURA,GOURD,GOUTS,GOUTY,GOWAN,' &&
      'GOWDS,GOWFS,GOWKS,GOWLS,GOWNS,GOXES,GOYLE,GRAAL,GRABS,GRACE,GRADE,GRADS,GRAFF,GRAFT,GRAIL,GRAIN,GRAIP,GRAMA,GRAME,' &&
      'GRAMP,GRAMS,GRANA,GRAND,GRANS,GRANT,GRAPE,GRAPH,GRAPY,GRASP,GRASS,GRATE,GRAVE,GRAVS,GRAVY,GRAYS,GRAZE,GREAT,GREBE,' &&
      'GREBO,GRECE,GREED,GREEK,GREEN,GREES,GREET,GREGE,GREGO,GREIN,GRENS,GRESE,GREVE,GREWS,GREYS,GRICE,GRIDE,GRIDS,GRIEF,' &&
      'GRIFF,GRIFT,GRIGS,GRIKE,GRILL,GRIME,GRIMY,GRIND,GRINS,GRIOT,GRIPE,GRIPS,GRIPT,GRIPY,GRISE,GRIST,GRISY,GRITH,GRITS,' &&
      'GRIZE,GROAN,GROAT,GRODY,GROGS,GROIN,GROKS,GROMA,GRONE,GROOF,GROOM,GROPE,GROSS,GROSZ,GROTS,GROUF,GROUP,GROUT,GROVE,' &&
      'GROVY,GROWL,GROWN,GROWS,GRRLS,GRRRL,GRUBS,GRUED,GRUEL,GRUES,GRUFE,GRUFF,GRUME,GRUMP,GRUND,GRUNT,GRYCE,GRYDE,GRYKE,' &&
      'GRYPE,GRYPT,GUACO,GUANA,GUANO,GUANS,GUARD,GUARS,GUAVA,GUCKS,GUCKY,GUDES,GUESS,GUEST,GUFFS,GUGAS,GUIDE,GUIDS,GUILD,' &&
      'GUILE,GUILT,GUIMP,GUIRO,GUISE,GULAG,GULAR,GULAS,GULCH,GULES,GULET,GULFS,GULFY,GULLS,GULLY,GULPH,GULPS,GULPY,GUMBO,' &&
      'GUMMA,GUMMI,GUMMY,GUMPS,GUNDY,GUNGE,GUNGY,GUNKS,GUNKY,GUNNY,GUPPY,GUQIN,GURDY,GURGE,GURLS,GURLY,GURNS,GURRY,GURSH,' &&
      'GURUS,GUSHY,GUSLA,GUSLE,GUSLI,GUSSY,GUSTO,GUSTS,GUSTY,GUTSY,GUTTA,GUTTY,GUYED,GUYLE,GUYOT,GUYSE,GWINE,GYALS,GYANS,' &&
      'GYBED,GYBES,GYELD,GYMPS,GYNAE,GYNIE,GYNNY,GYNOS,GYOZA,GYPOS,GYPPY,GYPSY,GYRAL,GYRED,GYRES,GYRON,GYROS,GYRUS,GYTES,' &&
      'GYVED,GYVES,HAAFS,HAARS,HABIT,HABLE,HABUS,HACEK,HACKS,HADAL,HADED,HADES,HADJI,HADST,HAEMS,HAETS,HAFFS,HAFIZ,HAFTS,' &&
      'HAGGS,HAHAS,HAICK,HAIKA,HAIKS,HAIKU,HAILS,HAILY,HAINS,HAINT,HAIRS,HAIRY,HAITH,HAJES,HAJIS,HAJJI,HAKAM,HAKAS,HAKEA,' &&
      'HAKES,HAKIM,HAKUS,HALAL,HALED,HALER,HALES,HALFA,HALFS,HALID,HALLO,HALLS,HALMA,HALMS,HALON,HALOS,HALSE,HALTS,HALVA,' &&
      'HALVE,HALWA,HAMAL,HAMBA,HAMED,HAMES,HAMMY,HAMZA,HANAP,HANCE,HANCH,HANDS,HANDY,HANGI,HANGS,HANKS,HANKY,HANSA,HANSE,' &&
      'HANTS,HAOMA,HAPAX,HAPLY,HAPPI,HAPPY,HAPUS,HARAM,HARDS,HARDY,HARED,HAREM,HARES,HARIM,HARKS,HARLS,HARMS,HARNS,HAROS,' &&
      'HARPS,HARPY,HARRY,HARSH,HARTS,HASHY,HASKS,HASPS,HASTA,HASTE,HASTY,HATCH,HATED,HATER,HATES,HATHA,HAUDS,HAUFS,HAUGH,' &&
      'HAULD,HAULM,HAULS,HAULT,HAUNS,HAUNT,HAUSE,HAUTE,HAVEN,HAVER,HAVES,HAVOC,HAWED,HAWKS,HAWMS,HAWSE,HAYED,HAYER,HAYEY,' &&
      'HAYLE,HAZAN,HAZED,HAZEL,HAZER,HAZES,HEADS,HEADY,HEALD,HEALS,HEAME,HEAPS,HEAPY,HEARD,HEARE,HEARS,HEART,HEAST,HEATH,' &&
      'HEATS,HEAVE,HEAVY,HEBEN,HEBES,HECHT,HECKS,HEDER,HEDGE,HEDGY,HEEDS,HEEDY,HEELS,HEEZE,HEFTE,HEFTS,HEFTY,HEIDS,HEIGH,' &&
      'HEILS,HEIRS,HEIST,HEJAB,HEJRA,HELED,HELES,HELIO,HELIX,HELLO,HELLS,HELMS,HELOS,HELOT,HELPS,HELVE,HEMAL,HEMES,HEMIC,' &&
      'HEMIN,HEMPS,HEMPY,HENCE,HENCH,HENDS,HENGE,HENNA,HENNY,HENRY,HENTS,HEPAR,HERBS,HERBY,HERDS,HERES,HERLS,HERMA,HERMS,' &&
      'HERNS,HERON,HEROS,HERRY,HERSE,HERTZ,HERYE,HESPS,HESTS,HETES,HETHS,HEUCH,HEUGH,HEVEA,HEWED,HEWER,HEWGH,HEXAD,HEXED,' &&
      'HEXER,HEXES,HEXYL,HEYED,HIANT,HICKS,HIDED,HIDER,HIDES,HIEMS,HIGHS,HIGHT,HIJAB,HIJRA,HIKED,HIKER,HIKES,HIKOI,HILAR,' &&
      'HILCH,HILLO,HILLS,HILLY,HILTS,HILUM,HILUS,HIMBO,HINAU,HINDS,HINGE,HINGS,HINKY,HINNY,HINTS,HIOIS,HIPLY,HIPPO,HIPPY,' &&
      'HIRED,HIREE,HIRER,HIRES,HISSY,HISTS,HITCH,HITHE,HIVED,HIVER,HIVES,HIZEN,HOAED,HOAGY,HOARD,HOARS,HOARY,HOAST,HOBBY,' &&
      'HOBOS,HOCKS,HOCUS,HODAD,HODJA,HOERS,HOGAN,HOGEN,HOGGS,HOGHS,HOHED,HOICK,HOIED,HOIKS,HOING,HOISE,HOIST,HOKAS,HOKED,' &&
      'HOKES,HOKEY,HOKIS,HOKKU,HOKUM,HOLDS,HOLED,HOLES,HOLEY,HOLKS,HOLLA,HOLLO,HOLLY,HOLME,HOLMS,HOLON,HOLOS,HOLTS,HOMAS,' &&
      'HOMED,HOMER,HOMES,HOMEY,HOMIE,HOMME,HOMOS,HONAN,HONDA,HONDS,HONED,HONER,HONES,HONEY,HONGI,HONGS,HONKS,HONOR,HOOCH,' &&
      'HOODS,HOODY,HOOEY,HOOFS,HOOKA,HOOKS,HOOKY,HOOLY,HOONS,HOOPS,HOORD,HOORS,HOOSH,HOOTS,HOOTY,HOOVE,HOPAK,HOPED,HOPER,' &&
      'HOPES,HOPPY,HORAH,HORAL,HORAS,HORDE,HORKS,HORME,HORNS,HORNY,HORSE,HORST,HORSY,HOSED,HOSEL,HOSEN,HOSER,HOSES,HOSEY,' &&
      'HOSTA,HOSTS,HOTCH,HOTEL,HOTEN,HOTLY,HOTTY,HOUFF,HOUFS,HOUGH,HOUND,HOURI,HOURS,HOUSE,HOUTS,HOVEA,HOVED,HOVEL,HOVEN,' &&
      'HOVER,HOVES,HOWBE,HOWDY,HOWES,HOWFF,HOWFS,HOWKS,HOWLS,HOWRE,HOWSO,HOXED,HOXES,HOYAS,HOYED,HOYLE,HUBBY,HUCKS,HUDNA,' &&
      'HUDUD,HUERS,HUFFS,HUFFY,HUGER,HUGGY,HUHUS,HUIAS,HULAS,HULES,HULKS,HULKY,HULLO,HULLS,HULLY,HUMAN,HUMAS,HUMFS,HUMIC,' &&
      'HUMID,HUMOR,HUMPH,HUMPS,HUMPY,HUMUS,HUNCH,HUNKS,HUNKY,HUNTS,HURDS,HURLS,HURLY,HURRA,HURRY,HURST,HURTS,HUSHY,HUSKS,' &&
      'HUSKY,HUSOS,HUSSY,HUTCH,HUTIA,HUZZA,HUZZY,HWYLS,HYDRA,HYDRO,HYENA,HYENS,HYGGE,HYING,HYKES,HYLAS,HYLEG,HYLES,HYLIC,' &&
      'HYMEN,HYMNS,HYNDE,HYOID,HYPED,HYPER,HYPES,HYPHA,HYPHY,HYPOS,HYRAX,HYSON,HYTHE,IAMBI,IAMBS,IBRIK,ICERS,ICHED,ICHES,' &&
      'ICHOR,ICIER,ICILY,ICING,ICKER,ICKLE,ICONS,ICTAL,ICTIC,ICTUS,IDANT,IDEAL,IDEAS,IDEES,IDENT,IDIOM,IDIOT,IDLED,IDLER,' &&
      'IDLES,IDOLA,IDOLS,IDYLL,IDYLS,IFTAR,IGAPO,IGGED,IGLOO,IGLUS,IHRAM,IKANS,IKATS,IKONS,ILEAC,ILEAL,ILEUM,ILEUS,ILIAC,' &&
      'ILIAD,ILIAL,ILIUM,ILLER,ILLTH,IMAGE,IMAGO,IMAMS,IMARI,IMAUM,IMBAR,IMBED,IMBUE,IMIDE,IMIDO,IMIDS,IMINE,IMINO,IMMEW,' &&
      'IMMIT,IMMIX,IMPED,IMPEL,IMPIS,IMPLY,IMPOT,IMPRO,IMSHI,IMSHY,INANE,INAPT,INARM,INBOX,INBYE,INCEL,INCLE,INCOG,INCUR,' &&
      'INCUS,INCUT,INDEW,INDEX,INDIA,INDIE,INDOL,INDOW,INDRI,INDUE,INEPT,INERM,INERT,INFER,INFIX,INFOS,INFRA,INGAN,INGLE,' &&
      'INGOT,INION,INKED,INKER,INKLE,INLAY,INLET,INNED,INNER,INNIT,INORB,INPUT,INRUN,INSET,INSPO,INTEL,INTER,INTIL,INTIS,' &&
      'INTRA,INTRO,INULA,INURE,INURN,INUST,INVAR,INWIT,IODIC,IODID,IODIN,IONIC,IOTAS,IPPON,IRADE,IRATE,IRIDS,IRING,IRKED,' &&
      'IROKO,IRONE,IRONS,IRONY,ISBAS,ISHES,ISLED,ISLES,ISLET,ISNAE,ISSEI,ISSUE,ISTLE,ITCHY,ITEMS,ITHER,IVIED,IVIES,IVORY,' &&
      'IXIAS,IXNAY,IXORA,IXTLE,IZARD,IZARS,IZZAT,JAAPS,JABOT,JACAL,JACKS,JACKY,JADED,JADES,JAFAS,JAFFA,JAGAS,JAGER,JAGGS,' &&
      'JAGGY,JAGIR,JAGRA,JAILS,JAKER,JAKES,JAKEY,JALAP,JALOP,JAMBE,JAMBO,JAMBS,JAMBU,JAMES,JAMMY,JAMON,JANES,JANNS,JANNY,' &&
      'JANTY,JAPAN,JAPED,JAPER,JAPES,JARKS,JARLS,JARPS,JARTA,JARUL,JASEY,JASPE,JASPS,JATOS,JAUKS,JAUNT,JAUPS,JAVAS,JAVEL,' &&
      'JAWAN,JAWED,JAXIE,JAZZY,JEANS,JEATS,JEBEL,JEDIS,JEELS,JEELY,JEEPS,JEERS,JEEZE,JEFES,JEFFS,JEHAD,JEHUS,JELAB,JELLO,' &&
      'JELLS,JELLY,JEMBE,JEMMY,JENNY,JEONS,JERID,JERKS,JERKY,JERRY,JESSE,JESTS,JESUS,JETES,JETON,JETTY,JEUNE,JEWEL,JEWIE,' &&
      'JHALA,JIAOS,JIBBA,JIBBS,JIBED,JIBER,JIBES,JIFFS,JIFFY,JIGGY,JIGOT,JIHAD,JILLS,JILTS,JIMMY,JIMPY,JINGO,JINKS,JINNE,' &&
      'JINNI,JINNS,JIRDS,JIRGA,JIRRE,JISMS,JIVED,JIVER,JIVES,JIVEY,JNANA,JOBED,JOBES,JOCKO,JOCKS,JOCKY,JOCOS,JODEL,JOEYS,' &&
      'JOHNS,JOINS,JOINT,JOIST,JOKED,JOKER,JOKES,JOKEY,JOKOL,JOLED,JOLES,JOLLS,JOLLY,JOLTS,JOLTY,JOMON,JOMOS,JONES,JONGS,' &&
      'JONTY,JOOKS,JORAM,JORUM,JOTAS,JOTTY,JOTUN,JOUAL,JOUGS,JOUKS,JOULE,JOURS,JOUST,JOWAR,JOWED,JOWLS,JOWLY,JOYED,JUBAS,' &&
      'JUBES,JUCOS,JUDAS,JUDGE,JUDGY,JUDOS,JUGAL,JUGUM,JUICE,JUICY,JUJUS,JUKED,JUKES,JUKUS,JULEP,JUMAR,JUMBO,JUMBY,JUMPS,' &&
      'JUMPY,JUNCO,JUNKS,JUNKY,JUNTA,JUNTO,JUPES,JUPON,JURAL,JURAT,JUREL,JURES,JUROR,JUSTS,JUTES,JUTTY,JUVES,JUVIE,KAAMA,' &&
      'KABAB,KABAR,KABOB,KACHA,KACKS,KADAI,KADES,KADIS,KAGOS,KAGUS,KAHAL,KAIAK,KAIDS,KAIES,KAIFS,KAIKA,KAIKS,KAILS,KAIMS,' &&
      'KAING,KAINS,KAKAS,KAKIS,KALAM,KALES,KALIF,KALIS,KALPA,KAMAS,KAMES,KAMIK,KAMIS,KAMME,KANAE,KANAS,KANDY,KANEH,KANES,' &&
      'KANGA,KANGS,KANJI,KANTS,KANZU,KAONS,KAPAS,KAPHS,KAPOK,KAPOW,KAPPA,KAPUS,KAPUT,KARAS,KARAT,KARKS,KARMA,KARNS,KAROO,' &&
      'KAROS,KARRI,KARST,KARSY,KARTS,KARZY,KASHA,KASME,KATAL,KATAS,KATIS,KATTI,KAUGH,KAURI,KAURU,KAURY,KAVAL,KAVAS,KAWAS,' &&
      'KAWAU,KAWED,KAYAK,KAYLE,KAYOS,KAZIS,KAZOO,KBARS,KEBAB,KEBAR,KEBOB,KECKS,KEDGE,KEDGY,KEECH,KEEFS,KEEKS,KEELS,KEEMA,' &&
      'KEENO,KEENS,KEEPS,KEETS,KEEVE,KEFIR,KEHUA,KEIRS,KELEP,KELIM,KELLS,KELLY,KELPS,KELPY,KELTS,KELTY,KEMBO,KEMBS,KEMPS,' &&
      'KEMPT,KEMPY,KENAF,KENCH,KENDO,KENOS,KENTE,KENTS,KEPIS,KERBS,KEREL,KERFS,KERKY,KERMA,KERNE,KERNS,KEROS,KERRY,KERVE,' &&
      'KESAR,KESTS,KETAS,KETCH,KETES,KETOL,KEVEL,KEVIL,KEXES,KEYED,KEYER,KHADI,KHAFS,KHAKI,KHANS,KHAPH,KHATS,KHAYA,KHAZI,' &&
      'KHEDA,KHETH,KHETS,KHOJA,KHORS,KHOUM,KHUDS,KIAAT,KIACK,KIANG,KIBBE,KIBBI,KIBEI,KIBES,KIBLA,KICKS,KICKY,KIDDO,KIDDY,' &&
      'KIDEL,KIDGE,KIEFS,KIERS,KIEVE,KIEVS,KIGHT,KIKOI,KILEY,KILIM,KILLS,KILNS,KILOS,KILPS,KILTS,KILTY,KIMBO,KINAS,KINDA,' &&
      'KINDS,KINDY,KINES,KINGS,KININ,KINKS,KINKY,KINOS,KIORE,KIOSK,KIPES,KIPPA,KIPPS,KIRBY,KIRKS,KIRNS,KIRRI,KISAN,KISSY,' &&
      'KISTS,KITED,KITER,KITES,KITHE,KITHS,KITTY,KITUL,KIVAS,KIWIS,KLANG,KLAPS,KLETT,KLICK,KLIEG,KLIKS,KLONG,KLOOF,KLUGE,' &&
      'KLUTZ,KNACK,KNAGS,KNAPS,KNARL,KNARS,KNAUR,KNAVE,KNAWE,KNEAD,KNEED,KNEEL,KNEES,KNELL,KNELT,KNIFE,KNISH,KNITS,KNIVE,' &&
      'KNOBS,KNOCK,KNOLL,KNOPS,KNOSP,KNOTS,KNOUT,KNOWE,KNOWN,KNOWS,KNUBS,KNURL,KNURR,KNURS,KNUTS,KOALA,KOANS,KOAPS,KOBAN,' &&
      'KOBOS,KOELS,KOFFS,KOFTA,KOGAL,KOHAS,KOHEN,KOHLS,KOINE,KOJIS,KOKAM,KOKAS,KOKER,KOKRA,KOKUM,KOLAS,KOLOS,KOMBU,KONBU,' &&
      'KONDO,KONKS,KOOKS,KOOKY,KOORI,KOPEK,KOPHS,KOPJE,KOPPA,KORAI,KORAS,KORAT,KORES,KORMA,KOROS,KORUN,KORUS,KOSES,KOTCH,' &&
      'KOTOS,KOTOW,KOURA,KRAAL,KRABS,KRAFT,KRAIS,KRAIT,KRANG,KRANS,KRANZ,KRAUT,KRAYS,KREEP,KRENG,KREWE,KRILL,KRONA,KRONE,' &&
      'KROON,KRUBI,KRUNK,KSARS,KUBIE,KUDOS,KUDUS,KUDZU,KUFIS,KUGEL,KUIAS,KUKRI,KUKUS,KULAK,KULAN,KULAS,KULFI,KUMIS,KUMYS,' &&
      'KURIS,KURRE,KURTA,KURUS,KUSSO,KUTAS,KUTCH,KUTIS,KUTUS,KUZUS,KVASS,KVELL,KWELA,KYACK,KYAKS,KYANG,KYARS,KYATS,KYBOS,' &&
      'KYDST,KYLES,KYLIE,KYLIN,KYLIX,KYLOE,KYNDE,KYNDS,KYPES,KYRIE,KYTES,KYTHE,LAARI,LABDA,LABEL,LABIA,LABIS,LABOR,LABRA,' &&
      'LACED,LACER,LACES,LACET,LACEY,LACKS,LADDY,LADED,LADEN,LADER,LADES,LADLE,LAERS,LAEVO,LAGAN,LAGER,LAHAL,LAHAR,LAICH,' &&
      'LAICS,LAIDS,LAIGH,LAIKA,LAIKS,LAIRD,LAIRS,LAIRY,LAITH,LAITY,LAKED,LAKER,LAKES,LAKHS,LAKIN,LAKSA,LALDY,LALLS,LAMAS,' &&
      'LAMBS,LAMBY,LAMED,LAMER,LAMES,LAMIA,LAMMY,LAMPS,LANAI,LANAS,LANCE,LANCH,LANDE,LANDS,LANES,LANKS,LANKY,LANTS,LAPEL,' &&
      'LAPIN,LAPIS,LAPJE,LAPSE,LARCH,LARDS,LARDY,LAREE,LARES,LARGE,LARGO,LARIS,LARKS,LARKY,LARNS,LARNT,LARUM,LARVA,LASED,' &&
      'LASER,LASES,LASSI,LASSO,LASSU,LASSY,LASTS,LATAH,LATCH,LATED,LATEN,LATER,LATEX,LATHE,LATHI,LATHS,LATHY,LATKE,LATTE,' &&
      'LATUS,LAUAN,LAUCH,LAUDS,LAUFS,LAUGH,LAUND,LAURA,LAVAL,LAVAS,LAVED,LAVER,LAVES,LAVRA,LAVVY,LAWED,LAWER,LAWIN,LAWKS,' &&
      'LAWNS,LAWNY,LAXED,LAXER,LAXES,LAXLY,LAYED,LAYER,LAYIN,LAYUP,LAZAR,LAZED,LAZES,LAZOS,LAZZI,LAZZO,LEACH,LEADS,LEADY,' &&
      'LEAFS,LEAFY,LEAKS,LEAKY,LEAMS,LEANS,LEANT,LEANY,LEAPS,LEAPT,LEARE,LEARN,LEARS,LEARY,LEASE,LEASH,LEAST,LEATS,LEAVE,' &&
      'LEAVY,LEAZE,LEBEN,LECCY,LEDES,LEDGE,LEDGY,LEDUM,LEEAR,LEECH,LEEKS,LEEPS,LEERS,LEERY,LEESE,LEETS,LEEZE,LEFTE,LEFTS,' &&
      'LEFTY,LEGAL,LEGER,LEGES,LEGGE,LEGGO,LEGGY,LEGIT,LEHRS,LEHUA,LEIRS,LEISH,LEMAN,LEMED,LEMEL,LEMES,LEMMA,LEMME,LEMON,' &&
      'LEMUR,LENDS,LENES,LENGS,LENIS,LENOS,LENSE,LENTI,LENTO,LEONE,LEPER,LEPID,LEPRA,LEPTA,LERED,LERES,LERPS,LESTS,LETCH,' &&
      'LETHE,LETUP,LEUCH,LEUCO,LEUDS,LEUGH,LEVAS,LEVEE,LEVEL,LEVER,LEVES,LEVIN,LEVIS,LEWIS,LEXES,LEXIS,LIANA,LIANE,LIANG,' &&
      'LIARD,LIARS,LIART,LIBEL,LIBER,LIBRA,LIBRI,LICHI,LICHT,LICIT,LICKS,LIDAR,LIDOS,LIEFS,LIEGE,LIENS,LIERS,LIEUS,LIEVE,' &&
      'LIFER,LIFES,LIFTS,LIGAN,LIGER,LIGGE,LIGHT,LIGNE,LIKED,LIKEN,LIKER,LIKES,LIKIN,LILAC,LILLS,LILOS,LILTS,LIMAN,LIMAS,' &&
      'LIMAX,LIMBA,LIMBI,LIMBO,LIMBS,LIMBY,LIMED,LIMEN,LIMES,LIMEY,LIMIT,LIMMA,LIMNS,LIMOS,LIMPA,LIMPS,LINAC,LINCH,LINDS,' &&
      'LINDY,LINED,LINEN,LINER,LINES,LINEY,LINGA,LINGO,LINGS,LINGY,LININ,LINKS,LINKY,LINNS,LINNY,LINOS,LINTS,LINTY,LINUM,' &&
      'LINUX,LIONS,LIPAS,LIPES,LIPID,LIPIN,LIPOS,LIPPY,LIRAS,LIRKS,LIROT,LISKS,LISLE,LISPS,LISTS,LITAI,LITAS,LITED,LITER,' &&
      'LITES,LITHE,LITHO,LITHS,LITRE,LIVED,LIVEN,LIVER,LIVES,LIVID,LIVOR,LIVRE,LLAMA,LLANO,LOACH,LOADS,LOAFS,LOAMS,LOAMY,' &&
      'LOANS,LOAST,LOATH,LOAVE,LOBAR,LOBBY,LOBED,LOBES,LOBOS,LOBUS,LOCAL,LOCHE,LOCHS,LOCIE,LOCIS,LOCKS,LOCOS,LOCUM,LOCUS,' &&
      'LODEN,LODES,LODGE,LOESS,LOFTS,LOFTY,LOGAN,LOGES,LOGGY,LOGIA,LOGIC,LOGIE,LOGIN,LOGOI,LOGON,LOGOS,LOHAN,LOIDS,LOINS,' &&
      'LOIPE,LOIRS,LOKES,LOLLS,LOLLY,LOLOG,LOMAS,LOMED,LOMES,LONER,LONGA,LONGE,LONGS,LOOBY,LOOED,LOOEY,LOOFA,LOOFS,LOOIE,' &&
      'LOOKS,LOOKY,LOOMS,LOONS,LOONY,LOOPS,LOOPY,LOORD,LOOSE,LOOTS,LOPED,LOPER,LOPES,LOPPY,LORAL,LORAN,LORDS,LORDY,LOREL,' &&
      'LORES,LORIC,LORIS,LORRY,LOSED,LOSEL,LOSEN,LOSER,LOSES,LOSSY,LOTAH,LOTAS,LOTES,LOTIC,LOTOS,LOTSA,LOTTA,LOTTE,LOTTO,' &&
      'LOTUS,LOUED,LOUGH,LOUIE,LOUIS,LOUMA,LOUND,LOUNS,LOUPE,LOUPS,LOURE,LOURS,LOURY,LOUSE,LOUSY,LOUTS,LOVAT,LOVED,LOVER,' &&
      'LOVES,LOVEY,LOVIE,LOWAN,LOWED,LOWER,LOWES,LOWLY,LOWND,LOWNE,LOWNS,LOWPS,LOWRY,LOWSE,LOWTS,LOXED,LOXES,LOYAL,LOZEN,' &&
      'LUACH,LUAUS,LUBED,LUBES,LUCES,LUCID,LUCKS,LUCKY,LUCRE,LUDES,LUDIC,LUDOS,LUFFA,LUFFS,LUGED,LUGER,LUGES,LULLS,LULUS,' &&
      'LUMAS,LUMBI,LUMEN,LUMME,LUMMY,LUMPS,LUMPY,LUNAR,LUNAS,LUNCH,LUNES,LUNET,LUNGE,LUNGI,LUNGS,LUNKS,LUNTS,LUPIN,LUPUS,' &&
      'LURCH,LURED,LURER,LURES,LUREX,LURGI,LURGY,LURID,LURKS,LURRY,LURVE,LUSER,LUSHY,LUSKS,LUSTS,LUSTY,LUSUS,LUTEA,LUTED,' &&
      'LUTER,LUTES,LUVVY,LUXED,LUXER,LUXES,LWEIS,LYAMS,LYARD,LYART,LYASE,LYCEA,LYCEE,LYCRA,LYING,LYMES,LYMPH,LYNCH,LYNES,' &&
      'LYRES,LYRIC,LYSED,LYSES,LYSIN,LYSIS,LYSOL,LYSSA,LYTED,LYTES,LYTHE,LYTIC,LYTTA,MAAED,MAARE,MAARS,MABES,MACAS,MACAW,' &&
      'MACED,MACER,MACES,MACHE,MACHI,MACHO,MACHS,MACKS,MACLE,MACON,MACRO,MADAM,MADGE,MADID,MADLY,MADRE,MAERL,MAFIA,MAFIC,' &&
      'MAGES,MAGGS,MAGIC,MAGMA,MAGOT,MAGUS,MAHOE,MAHUA,MAHWA,MAIDS,MAIKO,MAIKS,MAILE,MAILL,MAILS,MAIMS,MAINS,MAIRE,MAIRS,' &&
      'MAISE,MAIST,MAIZE,MAJOR,MAKAR,MAKER,MAKES,MAKIS,MAKOS,MALAM,MALAR,MALAS,MALAX,MALES,MALIC,MALIK,MALIS,MALLS,MALMS,' &&
      'MALMY,MALTS,MALTY,MALUS,MALVA,MALWA,MAMAS,MAMBA,MAMBO,MAMEE,MAMEY,MAMIE,MAMMA,MAMMY,MANAS,MANAT,MANDI,MANEB,MANED,' &&
      'MANEH,MANES,MANET,MANGA,MANGE,MANGO,MANGS,MANGY,MANIA,MANIC,MANIS,MANKY,MANLY,MANNA,MANOR,MANOS,MANSE,MANTA,MANTO,' &&
      'MANTY,MANUL,MANUS,MAPAU,MAPLE,MAQUI,MARAE,MARAH,MARAS,MARCH,MARCS,MARDY,MARES,MARGE,MARGS,MARIA,MARID,MARKA,MARKS,' &&
      'MARLE,MARLS,MARLY,MARMS,MARON,MAROR,MARRA,MARRI,MARRY,MARSE,MARSH,MARTS,MARVY,MASAS,MASED,MASER,MASES,MASHY,MASKS,' &&
      'MASON,MASSA,MASSE,MASSY,MASTS,MASTY,MASUS,MATAI,MATCH,MATED,MATER,MATES,MATEY,MATHS,MATIN,MATLO,MATTE,MATTS,MATZA,' &&
      'MATZO,MAUBY,MAUDS,MAULS,MAUND,MAURI,MAUSY,MAUTS,MAUVE,MAUZY,MAVEN,MAVIE,MAVIN,MAVIS,MAWED,MAWKS,MAWKY,MAWNS,MAWRS,' &&
      'MAXED,MAXES,MAXIM,MAXIS,MAYAN,MAYAS,MAYBE,MAYED,MAYOR,MAYOS,MAYST,MAZED,MAZER,MAZES,MAZEY,MAZUT,MBIRA,MEADS,MEALS,' &&
      'MEALY,MEANE,MEANS,MEANT,MEANY,MEARE,MEASE,MEATH,MEATS,MEATY,MEBOS,MECCA,MECHS,MECKS,MEDAL,MEDIA,MEDIC,MEDII,MEDLE,' &&
      'MEEDS,MEERS,MEETS,MEFFS,MEINS,MEINT,MEINY,MEITH,MEKKA,MELAS,MELBA,MELDS,MELEE,MELIC,MELIK,MELLS,MELON,MELTS,MELTY,' &&
      'MEMES,MEMOS,MENAD,MENDS,MENED,MENES,MENGE,MENGS,MENSA,MENSE,MENSH,MENTA,MENTO,MENUS,MEOUS,MEOWS,MERCH,MERCS,MERCY,' &&
      'MERDE,MERED,MEREL,MERER,MERES,MERGE,MERIL,MERIS,MERIT,MERKS,MERLE,MERLS,MERRY,MERSE,MESAL,MESAS,MESEL,MESES,MESHY,' &&
      'MESIC,MESNE,MESON,MESSY,MESTO,METAL,METED,METER,METES,METHO,METHS,METIC,METIF,METIS,METOL,METRE,METRO,MEUSE,MEVED,' &&
      'MEVES,MEWED,MEWLS,MEYNT,MEZES,MEZZE,MEZZO,MHORR,MIAOU,MIAOW,MIASM,MIAUL,MICAS,MICHE,MICHT,MICKY,MICOS,MICRA,MICRO,' &&
      'MIDDY,MIDGE,MIDGY,MIDIS,MIDST,MIENS,MIEVE,MIFFS,MIFFY,MIFTY,MIGGS,MIGHT,MIHAS,MIHIS,MIKED,MIKES,MIKRA,MIKVA,MILCH,' &&
      'MILDS,MILER,MILES,MILFS,MILIA,MILKO,MILKS,MILKY,MILLE,MILLS,MILOR,MILOS,MILPA,MILTS,MILTY,MILTZ,MIMED,MIMEO,MIMER,' &&
      'MIMES,MIMIC,MIMSY,MINAE,MINAR,MINAS,MINCE,MINCY,MINDS,MINED,MINER,MINES,MINGE,MINGS,MINGY,MINIM,MINIS,MINKE,MINKS,' &&
      'MINNY,MINOR,MINOS,MINTS,MINTY,MINUS,MIRED,MIRES,MIREX,MIRID,MIRIN,MIRKS,MIRKY,MIRLY,MIROS,MIRTH,MIRVS,MIRZA,MISCH,' &&
      'MISDO,MISER,MISES,MISGO,MISOS,MISSA,MISSY,MISTS,MISTY,MITCH,MITER,MITES,MITIS,MITRE,MITTS,MIXED,MIXEN,MIXER,MIXES,' &&
      'MIXTE,MIXUP,MIZEN,MIZZY,MNEME,MOANS,MOATS,MOBBY,MOBES,MOBEY,MOBIE,MOBLE,MOCHA,MOCHI,MOCHS,MOCHY,MOCKS,MODAL,MODEL,' &&
      'MODEM,MODER,MODES,MODGE,MODII,MODUS,MOERS,MOFOS,MOGGY,MOGUL,MOHEL,MOHOS,MOHRS,MOHUA,MOHUR,MOILE,MOILS,MOIRA,MOIRE,' &&
      'MOIST,MOITS,MOJOS,MOKES,MOKIS,MOKOS,MOLAL,MOLAR,MOLAS,MOLDS,MOLDY,MOLED,MOLES,MOLLA,MOLLS,MOLLY,MOLTO,MOLTS,MOLYS,' &&
      'MOMES,MOMMA,MOMMY,MOMUS,MONAD,MONAL,MONAS,MONDE,MONDO,MONER,MONEY,MONGO,MONGS,MONIC,MONIE,MONKS,MONOS,MONTE,MONTH,' &&
      'MONTY,MOOBS,MOOCH,MOODS,MOODY,MOOED,MOOKS,MOOLA,MOOLI,MOOLS,MOOLY,MOONG,MOONS,MOONY,MOOPS,MOORS,MOORY,MOOSE,MOOTS,' &&
      'MOOVE,MOPED,MOPER,MOPES,MOPEY,MOPPY,MOPSY,MOPUS,MORAE,MORAL,MORAS,MORAT,MORAY,MOREL,MORES,MORIA,MORNE,MORNS,MORON,' &&
      'MORPH,MORRA,MORRO,MORSE,MORTS,MOSED,MOSES,MOSEY,MOSKS,MOSSO,MOSSY,MOSTE,MOSTS,MOTED,MOTEL,MOTEN,MOTES,MOTET,MOTEY,' &&
      'MOTHS,MOTHY,MOTIF,MOTIS,MOTOR,MOTTE,MOTTO,MOTTS,MOTTY,MOTUS,MOTZA,MOUCH,MOUES,MOULD,MOULS,MOULT,MOUND,MOUNT,MOUPS,' &&
      'MOURN,MOUSE,MOUST,MOUSY,MOUTH,MOVED,MOVER,MOVES,MOVIE,MOWAS,MOWED,MOWER,MOWRA,MOXAS,MOXIE,MOYAS,MOYLE,MOYLS,MOZED,' &&
      'MOZES,MOZOS,MPRET,MUCHO,MUCIC,MUCID,MUCIN,MUCKS,MUCKY,MUCOR,MUCRO,MUCUS,MUDDY,MUDGE,MUDIR,MUDRA,MUFFS,MUFTI,MUGGA,' &&
      'MUGGS,MUGGY,MUHLY,MUIDS,MUILS,MUIRS,MUIST,MUJIK,MULCH,MULCT,MULED,MULES,MULEY,MULGA,MULIE,MULLA,MULLS,MULSE,MULSH,' &&
      'MUMMS,MUMMY,MUMPS,MUMSY,MUMUS,MUNCH,MUNGA,MUNGE,MUNGO,MUNGS,MUNIS,MUONS,MURAL,MURAS,MURED,MURES,MUREX,MURID,MURKS,' &&
      'MURKY,MURLS,MURLY,MURRA,MURRE,MURRI,MURRS,MURRY,MURTI,MURVA,MUSAR,MUSCA,MUSED,MUSER,MUSES,MUSET,MUSHA,MUSHY,MUSIC,' &&
      'MUSIT,MUSKS,MUSKY,MUSOS,MUSSE,MUSSY,MUSTH,MUSTS,MUSTY,MUTCH,MUTED,MUTER,MUTES,MUTHA,MUTIS,MUTON,MUTTS,MUXED,MUXES,' &&
      'MUZAK,MUZZY,MVULE,MYALL,MYLAR,MYNAH,MYNAS,MYOID,MYOMA,MYOPE,MYOPS,MYOPY,MYRRH,MYSID,MYTHI,MYTHS,MYTHY,MYXOS,MZEES,' &&
      'NAAMS,NAANS,NABES,NABIS,NABKS,NABLA,NABOB,NACHE,NACHO,NACRE,NADAS,NADIR,NAEVE,NAEVI,NAFFS,NAGAS,NAGGY,NAGOR,NAHAL,' &&
      'NAIAD,NAIFS,NAIKS,NAILS,NAIRA,NAIRU,NAIVE,NAKED,NAKER,NAKFA,NALAS,NALED,NALLA,NAMED,NAMER,NAMES,NAMMA,NAMUS,NANAS,' &&
      'NANDU,NANNA,NANNY,NANOS,NANUA,NAPAS,NAPED,NAPES,NAPOO,NAPPA,NAPPE,NAPPY,NARAS,NARCO,NARCS,NARDS,NARES,NARIC,NARIS,' &&
      'NARKS,NARKY,NARRE,NASAL,NASHI,NASTY,NATAL,NATCH,NATES,NATIS,NATTY,NAUCH,NAUNT,NAVAL,NAVAR,NAVEL,NAVES,NAVEW,NAVVY,' &&
      'NAWAB,NAZES,NAZIR,NAZIS,NDUJA,NEAFE,NEALS,NEAPS,NEARS,NEATH,NEATS,NEBEK,NEBEL,NECKS,NEDDY,NEEDS,NEEDY,NEELD,NEELE,' &&
      'NEEMB,NEEMS,NEEPS,NEESE,NEEZE,NEGUS,NEIFS,NEIGH,NEIST,NEIVE,NELIS,NELLY,NEMAS,NEMNS,NEMPT,NENES,NEONS,NEPER,NEPIT,' &&
      'NERAL,NERDS,NERDY,NERKA,NERKS,NEROL,NERTS,NERTZ,NERVE,NERVY,NESTS,NETES,NETOP,NETTS,NETTY,NEUKS,NEUME,NEUMS,NEVEL,' &&
      'NEVER,NEVES,NEVUS,NEWBS,NEWED,NEWEL,NEWER,NEWIE,NEWLY,NEWSY,NEWTS,NEXTS,NEXUS,NGAIO,NGANA,NGATI,NGOMA,NGWEE,NICAD,' &&
      'NICER,NICHE,NICHT,NICKS,NICOL,NIDAL,NIDED,NIDES,NIDOR,NIDUS,NIECE,NIEFS,NIEVE,NIFES,NIFFS,NIFFY,NIFTY,NIGHS,NIGHT,' &&
      'NIHIL,NIKAB,NIKAH,NIKAU,NILLS,NIMBI,NIMBS,NIMPS,NINER,NINES,NINJA,NINNY,NINON,NINTH,NIPAS,NIPPY,NIQAB,NIRLS,NIRLY,' &&
      'NISEI,NISSE,NISUS,NITER,NITES,NITID,NITON,NITRE,NITRO,NITRY,NITTY,NIVAL,NIXED,NIXER,NIXES,NIXIE,NIZAM,NKOSI,NOAHS,' &&
      'NOBBY,NOBLE,NOBLY,NOCKS,NODAL,NODDY,NODES,NODUS,NOELS,NOGGS,NOHOW,NOILS,NOILY,NOINT,NOIRS,NOISE,NOISY,NOLES,NOLLS,' &&
      'NOLOS,NOMAD,NOMAS,NOMEN,NOMES,NOMIC,NOMOI,NOMOS,NONAS,NONCE,NONES,NONET,NONGS,NONIS,NONNY,NONYL,NOOBS,NOOIT,NOOKS,' &&
      'NOOKY,NOONS,NOOPS,NOOSE,NOPAL,NORIA,NORIS,NORKS,NORMA,NORMS,NORTH,NOSED,NOSER,NOSES,NOSEY,NOTAL,NOTCH,NOTED,NOTER,' &&
      'NOTES,NOTUM,NOULD,NOULE,NOULS,NOUNS,NOUNY,NOUPS,NOVAE,NOVAS,NOVEL,NOVUM,NOWAY,NOWED,NOWLS,NOWTS,NOWTY,NOXAL,NOXES,' &&
      'NOYAU,NOYED,NOYES,NUBBY,NUBIA,NUCHA,NUDDY,NUDER,NUDES,NUDGE,NUDIE,NUDZH,NUFFS,NUGAE,NUKED,NUKES,NULLA,NULLS,NUMBS,' &&
      'NUMEN,NUMMY,NUNNY,NURDS,NURDY,NURLS,NURRS,NURSE,NUTSO,NUTSY,NUTTY,NYAFF,NYALA,NYING,NYLON,NYMPH,NYSSA,OAKED,OAKEN,' &&
      'OAKER,OAKUM,OARED,OASES,OASIS,OASTS,OATEN,OATER,OATHS,OAVES,OBANG,OBEAH,OBELI,OBESE,OBEYS,OBIAS,OBIED,OBIIT,OBITS,' &&
      'OBJET,OBOES,OBOLE,OBOLI,OBOLS,OCCAM,OCCUR,OCEAN,OCHER,OCHES,OCHRE,OCHRY,OCKER,OCREA,OCTAD,OCTAL,OCTAN,OCTAS,OCTET,' &&
      'OCTYL,OCULI,ODAHS,ODALS,ODDER,ODDLY,ODEON,ODEUM,ODISM,ODIST,ODIUM,ODORS,ODOUR,ODYLE,ODYLS,OFFAL,OFFED,OFFER,OFFIE,' &&
      'OFLAG,OFTEN,OFTER,OGAMS,OGEED,OGEES,OGGIN,OGHAM,OGIVE,OGLED,OGLER,OGLES,OGMIC,OGRES,OHIAS,OHING,OHMIC,OHONE,OIDIA,' &&
      'OILED,OILER,OINKS,OINTS,OJIME,OKAPI,OKAYS,OKEHS,OKRAS,OKTAS,OLDEN,OLDER,OLDIE,OLEIC,OLEIN,OLENT,OLEOS,OLEUM,OLIOS,' &&
      'OLIVE,OLLAS,OLLAV,OLLER,OLLIE,OLOGY,OLPAE,OLPES,OMASA,OMBER,OMBRE,OMBUS,OMEGA,OMENS,OMERS,OMITS,OMLAH,OMOVS,OMRAH,' &&
      'ONCER,ONCES,ONCET,ONCUS,ONELY,ONERS,ONERY,ONION,ONIUM,ONKUS,ONLAY,ONNED,ONSET,ONTIC,OOBIT,OOHED,OOMPH,OONTS,OOPED,' &&
      'OORIE,OOSES,OOTID,OOZED,OOZES,OPAHS,OPALS,OPENS,OPEPE,OPERA,OPINE,OPING,OPIUM,OPPOS,OPSIN,OPTED,OPTER,OPTIC,ORACH,' &&
      'ORACY,ORALS,ORANG,ORANT,ORATE,ORBED,ORBIT,ORCAS,ORCIN,ORDER,ORDOS,OREAD,ORFES,ORGAN,ORGIA,ORGIC,ORGUE,ORIBI,ORIEL,' &&
      'ORIXA,ORLES,ORLON,ORLOP,ORMER,ORNIS,ORPIN,ORRIS,ORTHO,ORVAL,ORZOS,OSCAR,OSHAC,OSIER,OSMIC,OSMOL,OSSIA,OSTIA,OTAKU,' &&
      'OTARY,OTHER,OTTAR,OTTER,OTTOS,OUBIT,OUCHT,OUENS,OUGHT,OUIJA,OULKS,OUMAS,OUNCE,OUNDY,OUPAS,OUPED,OUPHE,OUPHS,OURIE,' &&
      'OUSEL,OUSTS,OUTBY,OUTDO,OUTED,OUTER,OUTGO,OUTRE,OUTRO,OUTTA,OUZEL,OUZOS,OVALS,OVARY,OVATE,OVELS,OVENS,OVERS,OVERT,' &&
      'OVINE,OVIST,OVOID,OVOLI,OVOLO,OVULE,OWCHE,OWIES,OWING,OWLED,OWLER,OWLET,OWNED,OWNER,OWRES,OWRIE,OWSEN,OXBOW,OXERS,' &&
      'OXEYE,OXIDE,OXIDS,OXIES,OXIME,OXIMS,OXLIP,OXTER,OYERS,OZEKI,OZONE,OZZIE,PAALS,PAANS,PACAS,PACED,PACER,PACES,PACEY,' &&
      'PACHA,PACKS,PACOS,PACTA,PACTS,PADDY,PADIS,PADLE,PADMA,PADRE,PADRI,PAEAN,PAEDO,PAEON,PAGAN,PAGED,PAGER,PAGES,PAGLE,' &&
      'PAGOD,PAGRI,PAIKS,PAILS,PAINS,PAINT,PAIRE,PAIRS,PAISA,PAISE,PAKKA,PALAS,PALAY,PALEA,PALED,PALER,PALES,PALET,PALIS,' &&
      'PALKI,PALLA,PALLS,PALLY,PALMS,PALMY,PALPI,PALPS,PALSA,PALSY,PAMPA,PANAX,PANCE,PANDA,PANDS,PANDY,PANED,PANEL,PANES,' &&
      'PANGA,PANGS,PANIC,PANIM,PANKO,PANNE,PANNI,PANSY,PANTO,PANTS,PANTY,PAOLI,PAOLO,PAPAL,PAPAS,PAPAW,PAPER,PAPES,PAPPI,' &&
      'PAPPY,PARAE,PARAS,PARCH,PARDI,PARDS,PARDY,PARED,PAREN,PAREO,PARER,PARES,PAREU,PAREV,PARGE,PARGO,PARIS,PARKA,PARKI,' &&
      'PARKS,PARKY,PARLE,PARLY,PARMA,PAROL,PARPS,PARRA,PARRS,PARRY,PARSE,PARTI,PARTS,PARTY,PARVE,PARVO,PASEO,PASES,PASHA,' &&
      'PASHM,PASKA,PASPY,PASSE,PASTA,PASTE,PASTS,PASTY,PATCH,PATED,PATEN,PATER,PATES,PATHS,PATIN,PATIO,PATKA,PATLY,PATSY,' &&
      'PATTE,PATTY,PATUS,PAUAS,PAULS,PAUSE,PAVAN,PAVED,PAVEN,PAVER,PAVES,PAVID,PAVIN,PAVIS,PAWAS,PAWAW,PAWED,PAWER,PAWKS,' &&
      'PAWKY,PAWLS,PAWNS,PAXES,PAYED,PAYEE,PAYER,PAYOR,PAYSD,PEACE,PEACH,PEAGE,PEAGS,PEAKS,PEAKY,PEALS,PEANS,PEARE,PEARL,' &&
      'PEARS,PEART,PEASE,PEATS,PEATY,PEAVY,PEAZE,PEBAS,PECAN,PECHS,PECKE,PECKS,PECKY,PEDAL,PEDES,PEDIS,PEDRO,PEECE,PEEKS,' &&
      'PEELS,PEENS,PEEOY,PEEPE,PEEPS,PEERS,PEERY,PEEVE,PEGGY,PEGHS,PEINS,PEISE,PEIZE,PEKAN,PEKES,PEKIN,PEKOE,PELAS,PELAU,' &&
      'PELES,PELFS,PELLS,PELMA,PELON,PELTA,PELTS,PENAL,PENCE,PENDS,PENDU,PENED,PENES,PENGO,PENIE,PENIS,PENKS,PENNA,PENNE,' &&
      'PENNI,PENNY,PENTS,PEONS,PEONY,PEPLA,PEPOS,PEPPY,PEPSI,PERAI,PERCE,PERCH,PERCS,PERDU,PERDY,PEREA,PERES,PERIL,PERIS,' &&
      'PERKS,PERKY,PERMS,PERNS,PEROG,PERPS,PERRY,PERSE,PERST,PERTS,PERVE,PERVO,PERVS,PERVY,PESKY,PESOS,PESTO,PESTS,PESTY,' &&
      'PETAL,PETAR,PETER,PETIT,PETRE,PETRI,PETTI,PETTO,PETTY,PEWEE,PEWIT,PEYSE,PHAGE,PHANG,PHARE,PHARM,PHASE,PHEER,PHENE,' &&
      'PHEON,PHESE,PHIAL,PHISH,PHIZZ,PHLOX,PHOCA,PHONE,PHONO,PHONS,PHONY,PHOTO,PHOTS,PHPHT,PHUTS,PHYLA,PHYLE,PIANI,PIANO,' &&
      'PIANS,PIBAL,PICAL,PICAS,PICCY,PICKS,PICKY,PICOT,PICRA,PICUL,PIECE,PIEND,PIERS,PIERT,PIETA,PIETS,PIETY,PIEZO,PIGGY,' &&
      'PIGHT,PIGMY,PIING,PIKAS,PIKAU,PIKED,PIKER,PIKES,PIKIS,PIKUL,PILAE,PILAF,PILAO,PILAR,PILAU,PILAW,PILCH,PILEA,PILED,' &&
      'PILEI,PILER,PILES,PILIS,PILLS,PILOT,PILOW,PILUM,PILUS,PIMAS,PIMPS,PINAS,PINCH,PINED,PINES,PINEY,PINGO,PINGS,PINKO,' &&
      'PINKS,PINKY,PINNA,PINNY,PINON,PINOT,PINTA,PINTO,PINTS,PINUP,PIONS,PIONY,PIOUS,PIOYE,PIOYS,PIPAL,PIPAS,PIPED,PIPER,' &&
      'PIPES,PIPET,PIPIS,PIPIT,PIPPY,PIPUL,PIQUE,PIRAI,PIRLS,PIRNS,PIROG,PISCO,PISES,PISKY,PISOS,PISSY,PISTE,PITAS,PITCH,' &&
      'PITHS,PITHY,PITON,PITOT,PITTA,PIUMS,PIVOT,PIXEL,PIXES,PIXIE,PIZED,PIZES,PIZZA,PLAAS,PLACE,PLACK,PLAGE,PLAID,PLAIN,' &&
      'PLAIT,PLANE,PLANK,PLANS,PLANT,PLAPS,PLASH,PLASM,PLAST,PLATE,PLATS,PLATT,PLATY,PLAYA,PLAYS,PLAZA,PLEAD,PLEAS,PLEAT,' &&
      'PLEBE,PLEBS,PLENA,PLEON,PLESH,PLEWS,PLICA,PLIED,PLIER,PLIES,PLIMS,PLING,PLINK,PLOAT,PLODS,PLONG,PLONK,PLOOK,PLOPS,' &&
      'PLOTS,PLOTZ,PLOUK,PLOWS,PLOYE,PLOYS,PLUCK,PLUES,PLUFF,PLUGS,PLUMB,PLUME,PLUMP,PLUMS,PLUMY,PLUNK,PLUOT,PLUSH,PLUTO,' &&
      'PLYER,POACH,POAKA,POAKE,POBOY,POCKS,POCKY,PODAL,PODDY,PODEX,PODGE,PODGY,PODIA,POEMS,POEPS,POESY,POETS,POGEY,POGGE,' &&
      'POGOS,POHED,POILU,POIND,POINT,POISE,POKAL,POKED,POKER,POKES,POKEY,POKIE,POLAR,POLED,POLER,POLES,POLEY,POLIO,POLIS,' &&
      'POLJE,POLKA,POLKS,POLLS,POLLY,POLOS,POLTS,POLYP,POLYS,POMBE,POMES,POMMY,POMOS,POMPS,PONCE,PONCY,PONDS,PONES,PONEY,' &&
      'PONGA,PONGO,PONGS,PONGY,PONKS,PONTS,PONTY,PONZU,POOCH,POODS,POOED,POOHS,POOJA,POOKA,POOKS,POOLS,POONS,POOPS,POOPY,' &&
      'POORI,POORT,POOTS,POPES,POPPA,POPPY,POPSY,PORAE,PORAL,PORCH,PORED,PORER,PORES,PORGE,PORGY,PORIN,PORKS,PORKY,PORNO,' &&
      'PORNS,PORNY,PORTA,PORTS,PORTY,POSED,POSER,POSES,POSEY,POSHO,POSIT,POSSE,POSTS,POTAE,POTCH,POTED,POTES,POTIN,POTOO,' &&
      'POTSY,POTTO,POTTS,POTTY,POUCH,POUFF,POUFS,POUKE,POUKS,POULE,POULP,POULT,POUND,POUPE,POUPT,POURS,POUTS,POUTY,POWAN,' &&
      'POWER,POWIN,POWND,POWNS,POWNY,POWRE,POXED,POXES,POYNT,POYOU,POYSE,POZZY,PRAAM,PRADS,PRAHU,PRAMS,PRANA,PRANG,PRANK,' &&
      'PRAOS,PRASE,PRATE,PRATS,PRATT,PRATY,PRAUS,PRAWN,PRAYS,PREDY,PREED,PREEN,PREES,PREIF,PREMS,PREMY,PRENT,PREON,PREOP,' &&
      'PREPS,PRESA,PRESE,PRESS,PREST,PREVE,PREXY,PREYS,PRIAL,PRICE,PRICK,PRICY,PRIDE,PRIED,PRIEF,PRIER,PRIES,PRIGS,PRILL,' &&
      'PRIMA,PRIME,PRIMI,PRIMO,PRIMP,PRIMS,PRIMY,PRINK,PRINT,PRION,PRIOR,PRISE,PRISM,PRISS,PRIVY,PRIZE,PROAS,PROBE,PROBS,' &&
      'PRODS,PROEM,PROFS,PROGS,PROIN,PROKE,PROLE,PROLL,PROMO,PROMS,PRONE,PRONG,PRONK,PROOF,PROPS,PRORE,PROSE,PROSO,PROSS,' &&
      'PROST,PROSY,PROTO,PROUD,PROUL,PROVE,PROWL,PROWS,PROXY,PROYN,PRUDE,PRUNE,PRUNT,PRUTA,PRYER,PRYSE,PSALM,PSEUD,PSHAW,' &&
      'PSION,PSOAE,PSOAI,PSOAS,PSORA,PSYCH,PSYOP,PUBCO,PUBES,PUBIC,PUBIS,PUCAN,PUCER,PUCES,PUCKA,PUCKS,PUDDY,PUDGE,PUDGY,' &&
      'PUDIC,PUDOR,PUDSY,PUDUS,PUERS,PUFFA,PUFFS,PUFFY,PUGGY,PUGIL,PUHAS,PUJAH,PUJAS,PUKAS,PUKED,PUKER,PUKES,PUKEY,PUKKA,' &&
      'PUKUS,PULAO,PULAS,PULED,PULER,PULES,PULIK,PULIS,PULKA,PULKS,PULLI,PULLS,PULLY,PULMO,PULPS,PULPY,PULSE,PULUS,PUMAS,' &&
      'PUMIE,PUMPS,PUNAS,PUNCE,PUNCH,PUNGA,PUNGS,PUNJI,PUNKA,PUNKS,PUNKY,PUNNY,PUNTO,PUNTS,PUNTY,PUPAE,PUPAL,PUPAS,PUPIL,' &&
      'PUPPY,PUPUS,PURDA,PURED,PUREE,PURER,PURES,PURGE,PURIN,PURIS,PURLS,PURPY,PURRS,PURSE,PURSY,PURTY,PUSES,PUSHY,PUSLE,' &&
      'PUSSY,PUTID,PUTON,PUTTI,PUTTO,PUTTS,PUTTY,PUZEL,PWNED,PYATS,PYETS,PYGAL,PYGMY,PYINS,PYLON,PYNED,PYNES,PYOID,PYOTS,' &&
      'PYRAL,PYRAN,PYRES,PYREX,PYRIC,PYROS,PYXED,PYXES,PYXIE,PYXIS,PZAZZ,QADIS,QAIDS,QAJAQ,QANAT,QAPIK,QIBLA,QOPHS,QORMA,' &&
      'QUACK,QUADS,QUAFF,QUAGS,QUAIL,QUAIR,QUAIS,QUAKE,QUAKY,QUALE,QUALM,QUANT,QUARE,QUARK,QUART,QUASH,QUASI,QUASS,QUATE,' &&
      'QUATS,QUAYD,QUAYS,QUBIT,QUEAN,QUEEN,QUEER,QUELL,QUEME,QUENA,QUERN,QUERY,QUEST,QUEUE,QUEYN,QUEYS,QUICH,QUICK,QUIDS,' &&
      'QUIET,QUIFF,QUILL,QUILT,QUIMS,QUINA,QUINE,QUINO,QUINS,QUINT,QUIPO,QUIPS,QUIPU,QUIRE,QUIRK,QUIRT,QUIST,QUITE,QUITS,' &&
      'QUOAD,QUODS,QUOIF,QUOIN,QUOIT,QUOLL,QUONK,QUOPS,QUOTA,QUOTE,QUOTH,QURSH,QUYTE,RABAT,RABBI,RABIC,RABID,RABIS,RACED,' &&
      'RACER,RACES,RACHE,RACKS,RACON,RADAR,RADGE,RADII,RADIO,RADIX,RADON,RAFFS,RAFTS,RAGAS,RAGDE,RAGED,RAGEE,RAGER,RAGES,' &&
      'RAGGA,RAGGS,RAGGY,RAGIS,RAGUS,RAHED,RAHUI,RAIAS,RAIDS,RAIKS,RAILE,RAILS,RAINE,RAINS,RAINY,RAIRD,RAISE,RAITA,RAITS,' &&
      'RAJAH,RAJAS,RAJES,RAKED,RAKEE,RAKER,RAKES,RAKIA,RAKIS,RAKUS,RALES,RALLY,RALPH,RAMAL,RAMEE,RAMEN,RAMET,RAMIE,RAMIN,' &&
      'RAMIS,RAMMY,RAMPS,RAMUS,RANAS,RANCE,RANCH,RANDS,RANDY,RANEE,RANGA,RANGE,RANGI,RANGS,RANGY,RANID,RANIS,RANKE,RANKS,' &&
      'RANTS,RAPED,RAPER,RAPES,RAPHE,RAPID,RAPPE,RARED,RAREE,RARER,RARES,RARKS,RASED,RASER,RASES,RASPS,RASPY,RASSE,RASTA,' &&
      'RATAL,RATAN,RATAS,RATCH,RATED,RATEL,RATER,RATES,RATHA,RATHE,RATHS,RATIO,RATOO,RATOS,RATTY,RATUS,RAUNS,RAUPO,RAVED,' &&
      'RAVEL,RAVEN,RAVER,RAVES,RAVEY,RAVIN,RAWER,RAWIN,RAWLY,RAWNS,RAXED,RAXES,RAYAH,RAYAS,RAYED,RAYLE,RAYNE,RAYON,RAZED,' &&
      'RAZEE,RAZER,RAZES,RAZOO,RAZOR,REACH,REACT,READD,READS,READY,REAIS,REAKS,REALM,REALO,REALS,REAME,REAMS,REAMY,REANS,' &&
      'REAPS,REARM,REARS,REAST,REATA,REATE,REAVE,REBAR,REBBE,REBEC,REBEL,REBID,REBIT,REBOP,REBUS,REBUT,REBUY,RECAL,RECAP,' &&
      'RECCE,RECCO,RECCY,RECIT,RECKS,RECON,RECTA,RECTI,RECTO,RECUR,RECUT,REDAN,REDDS,REDDY,REDED,REDES,REDIA,REDID,REDIP,' &&
      'REDLY,REDON,REDOS,REDOX,REDRY,REDUB,REDUX,REDYE,REECH,REEDE,REEDS,REEDY,REEFS,REEFY,REEKS,REEKY,REELS,REENS,REEST,' &&
      'REEVE,REFED,REFEL,REFER,REFIS,REFIT,REFIX,REFLY,REFRY,REGAL,REGAR,REGES,REGGO,REGIE,REGMA,REGNA,REGOS,REGUR,REHAB,' &&
      'REHEM,REIFS,REIFY,REIGN,REIKI,REIKS,REINK,REINS,REIRD,REIST,REIVE,REJIG,REJON,REKED,REKES,REKEY,RELAX,RELAY,RELET,' &&
      'RELIC,RELIE,RELIT,RELLO,REMAN,REMAP,REMEN,REMET,REMEX,REMIT,REMIX,RENAL,RENAY,RENDS,RENEW,RENEY,RENGA,RENIG,RENIN,' &&
      'RENNE,RENOS,RENTE,RENTS,REOIL,REORG,REPAY,REPEG,REPEL,REPIN,REPLA,REPLY,REPOS,REPOT,REPPS,REPRO,RERAN,RERIG,RERUN,' &&
      'RESAT,RESAW,RESAY,RESEE,RESES,RESET,RESEW,RESID,RESIN,RESIT,RESOD,RESOW,RESTO,RESTS,RESTY,RESUS,RETAG,RETAX,RETCH,' &&
      'RETEM,RETIA,RETIE,RETOX,RETRO,RETRY,REUSE,REVEL,REVET,REVIE,REVUE,REWAN,REWAX,REWED,REWET,REWIN,REWON,REWTH,REXES,' &&
      'REZES,RHEAS,RHEME,RHEUM,RHIES,RHIME,RHINE,RHINO,RHODY,RHOMB,RHONE,RHUMB,RHYME,RHYNE,RHYTA,RIADS,RIALS,RIANT,RIATA,' &&
      'RIBAS,RIBBY,RIBES,RICED,RICER,RICES,RICEY,RICHT,RICIN,RICKS,RIDER,RIDES,RIDGE,RIDGY,RIDIC,RIELS,RIEMS,RIEVE,RIFER,' &&
      'RIFFS,RIFLE,RIFTE,RIFTS,RIFTY,RIGGS,RIGHT,RIGID,RIGOL,RIGOR,RILED,RILES,RILEY,RILLE,RILLS,RIMAE,RIMED,RIMER,RIMES,' &&
      'RIMUS,RINDS,RINDY,RINES,RINGS,RINKS,RINSE,RIOJA,RIOTS,RIPED,RIPEN,RIPER,RIPES,RIPPS,RISEN,RISER,RISES,RISHI,RISKS,' &&
      'RISKY,RISPS,RISUS,RITES,RITTS,RITZY,RIVAL,RIVAS,RIVED,RIVEL,RIVEN,RIVER,RIVES,RIVET,RIYAL,RIZAS,ROACH,ROADS,ROAMS,' &&
      'ROANS,ROARS,ROARY,ROAST,ROATE,ROBED,ROBES,ROBIN,ROBLE,ROBOT,ROCKS,ROCKY,RODED,RODEO,RODES,ROGER,ROGUE,ROGUY,ROHES,' &&
      'ROIDS,ROILS,ROILY,ROINS,ROIST,ROJAK,ROJIS,ROKED,ROKER,ROKES,ROLAG,ROLES,ROLFS,ROLLS,ROMAL,ROMAN,ROMEO,ROMPS,RONDE,' &&
      'RONDO,RONEO,RONES,RONIN,RONNE,RONTE,RONTS,ROODS,ROOFS,ROOFY,ROOKS,ROOKY,ROOMS,ROOMY,ROONS,ROOPS,ROOPY,ROOSA,ROOSE,' &&
      'ROOST,ROOTS,ROOTY,ROPED,ROPER,ROPES,ROPEY,ROQUE,RORAL,RORES,RORIC,RORID,RORIE,RORTS,RORTY,ROSED,ROSES,ROSET,ROSHI,' &&
      'ROSIN,ROSIT,ROSTI,ROSTS,ROTAL,ROTAN,ROTAS,ROTCH,ROTED,ROTES,ROTIS,ROTLS,ROTON,ROTOR,ROTOS,ROTTE,ROUEN,ROUES,ROUGE,' &&
      'ROUGH,ROULE,ROULS,ROUMS,ROUND,ROUPS,ROUPY,ROUSE,ROUST,ROUTE,ROUTH,ROUTS,ROVED,ROVEN,ROVER,ROVES,ROWAN,ROWDY,ROWED,' &&
      'ROWEL,ROWEN,ROWER,ROWIE,ROWME,ROWND,ROWTH,ROWTS,ROYAL,ROYNE,ROYST,ROZET,ROZIT,RUANA,RUBAI,RUBBY,RUBEL,RUBES,RUBIN,' &&
      'RUBLE,RUBLI,RUBUS,RUCHE,RUCKS,RUDAS,RUDDS,RUDDY,RUDER,RUDES,RUDIE,RUDIS,RUEDA,RUERS,RUFFE,RUFFS,RUGAE,RUGAL,RUGBY,' &&
      'RUGGY,RUING,RUINS,RUKHS,RULED,RULER,RULES,RUMAL,RUMBA,RUMBO,RUMEN,RUMES,RUMLY,RUMMY,RUMOR,RUMPO,RUMPS,RUMPY,RUNCH,' &&
      'RUNDS,RUNED,RUNES,RUNGS,RUNIC,RUNNY,RUNTS,RUNTY,RUPEE,RUPIA,RURAL,RURPS,RURUS,RUSAS,RUSES,RUSHY,RUSKS,RUSMA,RUSSE,' &&
      'RUSTS,RUSTY,RUTHS,RUTIN,RUTTY,RYALS,RYBAT,RYKED,RYKES,RYMME,RYNDS,RYOTS,RYPER,SAAGS,SABAL,SABED,SABER,SABES,SABHA,' &&
      'SABIN,SABIR,SABLE,SABOT,SABRA,SABRE,SACKS,SACRA,SADDO,SADES,SADHE,SADHU,SADIS,SADLY,SADOS,SADZA,SAFED,SAFER,SAFES,' &&
      'SAGAS,SAGER,SAGES,SAGGY,SAGOS,SAGUM,SAHEB,SAHIB,SAICE,SAICK,SAICS,SAIDS,SAIGA,SAILS,SAIMS,SAINE,SAINS,SAINT,SAIRS,' &&
      'SAIST,SAITH,SAJOU,SAKER,SAKES,SAKIA,SAKIS,SAKTI,SALAD,SALAL,SALAT,SALEP,SALES,SALET,SALIC,SALIX,SALLE,SALLY,SALMI,' &&
      'SALOL,SALON,SALOP,SALPA,SALPS,SALSA,SALSE,SALTO,SALTS,SALTY,SALUE,SALUT,SALVE,SALVO,SAMAN,SAMAS,SAMBA,SAMBO,SAMEK,' &&
      'SAMEL,SAMEN,SAMES,SAMEY,SAMFU,SAMMY,SAMPI,SAMPS,SANDS,SANDY,SANED,SANER,SANES,SANGA,SANGH,SANGO,SANGS,SANKO,SANSA,' &&
      'SANTO,SANTS,SAOLA,SAPAN,SAPID,SAPOR,SAPPY,SARAN,SARDS,SARED,SAREE,SARGE,SARGO,SARIN,SARIS,SARKS,SARKY,SAROD,SAROS,' &&
      'SARUS,SASER,SASIN,SASSE,SASSY,SATAI,SATAY,SATED,SATEM,SATES,SATIN,SATIS,SATYR,SAUBA,SAUCE,SAUCH,SAUCY,SAUGH,SAULS,' &&
      'SAULT,SAUNA,SAUNT,SAURY,SAUTE,SAUTS,SAVED,SAVER,SAVES,SAVEY,SAVIN,SAVOR,SAVOY,SAVVY,SAWAH,SAWED,SAWER,SAXES,SAYED,' &&
      'SAYER,SAYID,SAYNE,SAYON,SAYST,SAZES,SCABS,SCADS,SCAFF,SCAGS,SCAIL,SCALA,SCALD,SCALE,SCALL,SCALP,SCALY,SCAMP,SCAMS,' &&
      'SCAND,SCANS,SCANT,SCAPA,SCAPE,SCAPI,SCARE,SCARF,SCARP,SCARS,SCART,SCARY,SCATH,SCATS,SCATT,SCAUD,SCAUP,SCAUR,SCAWS,' &&
      'SCEAT,SCENA,SCEND,SCENE,SCENT,SCHAV,SCHMO,SCHUL,SCHWA,SCION,SCLIM,SCODY,SCOFF,SCOGS,SCOLD,SCONE,SCOOG,SCOOP,SCOOT,' &&
      'SCOPA,SCOPE,SCOPS,SCORE,SCORN,SCOTS,SCOUG,SCOUP,SCOUR,SCOUT,SCOWL,SCOWP,SCOWS,SCRAB,SCRAE,SCRAG,SCRAM,SCRAN,SCRAP,' &&
      'SCRAT,SCRAW,SCRAY,SCREE,SCREW,SCRIM,SCRIP,SCROB,SCROD,SCROG,SCROW,SCRUB,SCRUM,SCUBA,SCUDI,SCUDO,SCUDS,SCUFF,SCUFT,' &&
      'SCUGS,SCULK,SCULL,SCULP,SCULS,SCUMS,SCUPS,SCURF,SCURS,SCUSE,SCUTA,SCUTE,SCUTS,SCUZZ,SCYES,SDAYN,SDEIN,SEALS,SEAME,' &&
      'SEAMS,SEAMY,SEANS,SEARE,SEARS,SEASE,SEATS,SEAZE,SEBUM,SECCO,SECHS,SECTS,SEDAN,SEDER,SEDES,SEDGE,SEDGY,SEDUM,SEEDS,' &&
      'SEEDY,SEEKS,SEELD,SEELS,SEELY,SEEMS,SEEPS,SEEPY,SEERS,SEFER,SEGAR,SEGNI,SEGNO,SEGOL,SEGOS,SEGUE,SEHRI,SEIFS,SEILS,' &&
      'SEINE,SEIRS,SEISE,SEISM,SEITY,SEIZA,SEIZE,SEKOS,SEKTS,SELAH,SELES,SELFS,SELLA,SELLE,SELLS,SELVA,SEMEE,SEMEN,SEMES,' &&
      'SEMIE,SEMIS,SENAS,SENDS,SENES,SENGI,SENNA,SENOR,SENSA,SENSE,SENSI,SENTE,SENTI,SENTS,SENVY,SENZA,SEPAD,SEPAL,SEPIA,' &&
      'SEPIC,SEPOY,SEPTA,SEPTS,SERAC,SERAI,SERAL,SERED,SERER,SERES,SERFS,SERGE,SERIC,SERIF,SERIN,SERKS,SERON,SEROW,SERRA,' &&
      'SERRE,SERRS,SERRY,SERUM,SERVE,SERVO,SESEY,SESSA,SETAE,SETAL,SETON,SETTS,SETUP,SEVEN,SEVER,SEWAN,SEWAR,SEWED,SEWEL,' &&
      'SEWEN,SEWER,SEWIN,SEXED,SEXER,SEXES,SEXTO,SEXTS,SEYEN,SHACK,SHADE,SHADS,SHADY,SHAFT,SHAGS,SHAHS,SHAKE,SHAKO,SHAKT,' &&
      'SHAKY,SHALE,SHALL,SHALM,SHALT,SHALY,SHAMA,SHAME,SHAMS,SHAND,SHANK,SHANS,SHAPE,SHAPS,SHARD,SHARE,SHARK,SHARN,SHARP,' &&
      'SHASH,SHAUL,SHAVE,SHAWL,SHAWM,SHAWN,SHAWS,SHAYA,SHAYS,SHCHI,SHEAF,SHEAL,SHEAR,SHEAS,SHEDS,SHEEL,SHEEN,SHEEP,SHEER,' &&
      'SHEET,SHEIK,SHELF,SHELL,SHEND,SHENT,SHEOL,SHERD,SHERE,SHERO,SHETS,SHEVA,SHEWN,SHEWS,SHIAI,SHIED,SHIEL,SHIER,SHIES,' &&
      'SHIFT,SHILL,SHILY,SHIMS,SHINE,SHINS,SHINY,SHIPS,SHIRE,SHIRK,SHIRR,SHIRS,SHIRT,SHISH,SHISO,SHIST,SHITE,SHITS,SHIUR,' &&
      'SHIVA,SHIVE,SHIVS,SHLEP,SHLUB,SHMEK,SHMOE,SHOAL,SHOAT,SHOCK,SHOED,SHOER,SHOES,SHOGI,SHOGS,SHOJI,SHOJO,SHOLA,SHONE,' &&
      'SHOOK,SHOOL,SHOON,SHOOS,SHOOT,SHOPE,SHOPS,SHORE,SHORL,SHORN,SHORT,SHOTE,SHOTS,SHOTT,SHOUT,SHOVE,SHOWD,SHOWN,SHOWS,' &&
      'SHOWY,SHOYU,SHRED,SHREW,SHRIS,SHROW,SHRUB,SHRUG,SHTIK,SHTUM,SHTUP,SHUCK,SHULE,SHULN,SHULS,SHUNS,SHUNT,SHURA,SHUSH,' &&
      'SHUTE,SHUTS,SHWAS,SHYER,SHYLY,SIALS,SIBBS,SIBYL,SICES,SICHT,SICKO,SICKS,SICKY,SIDAS,SIDED,SIDER,SIDES,SIDHA,SIDHE,' &&
      'SIDLE,SIEGE,SIELD,SIENS,SIENT,SIETH,SIEUR,SIEVE,SIFTS,SIGHS,SIGHT,SIGIL,SIGLA,SIGMA,SIGNA,SIGNS,SIJOS,SIKAS,SIKER,' &&
      'SIKES,SILDS,SILED,SILEN,SILER,SILES,SILEX,SILKS,SILKY,SILLS,SILLY,SILOS,SILTS,SILTY,SILVA,SIMAR,SIMAS,SIMBA,SIMIS,' &&
      'SIMPS,SIMUL,SINCE,SINDS,SINED,SINES,SINEW,SINGE,SINGS,SINHS,SINKS,SINKY,SINUS,SIPED,SIPES,SIPPY,SIRED,SIREE,SIREN,' &&
      'SIRES,SIRIH,SIRIS,SIROC,SIRRA,SIRUP,SISAL,SISES,SISSY,SISTA,SISTS,SITAR,SITED,SITES,SITHE,SITKA,SITUP,SITUS,SIVER,' &&
      'SIXER,SIXES,SIXMO,SIXTE,SIXTH,SIXTY,SIZAR,SIZED,SIZEL,SIZER,SIZES,SKAGS,SKAIL,SKALD,SKANK,SKART,SKATE,SKATS,SKATT,' &&
      'SKAWS,SKEAN,SKEAR,SKEDS,SKEED,SKEEF,SKEEN,SKEER,SKEES,SKEET,SKEGG,SKEGS,SKEIN,SKELF,SKELL,SKELM,SKELP,SKENE,SKENS,' &&
      'SKEOS,SKEPS,SKERS,SKETS,SKEWS,SKIDS,SKIED,SKIER,SKIES,SKIEY,SKIFF,SKILL,SKIMP,SKIMS,SKINK,SKINS,SKINT,SKIOS,SKIPS,' &&
      'SKIRL,SKIRR,SKIRT,SKITE,SKITS,SKIVE,SKIVY,SKLIM,SKOAL,SKODY,SKOFF,SKOGS,SKOLS,SKOOL,SKORT,SKOSH,SKRAN,SKRIK,SKUAS,' &&
      'SKUGS,SKULK,SKULL,SKUNK,SKYED,SKYER,SKYEY,SKYFS,SKYRE,SKYRS,SKYTE,SLABS,SLACK,SLADE,SLAES,SLAGS,SLAID,SLAIN,SLAKE,' &&
      'SLAMS,SLANE,SLANG,SLANK,SLANT,SLAPS,SLART,SLASH,SLATE,SLATS,SLATY,SLAVE,SLAWS,SLAYS,SLEBS,SLEDS,SLEEK,SLEEP,SLEER,' &&
      'SLEET,SLEPT,SLEWS,SLEYS,SLICE,SLICK,SLIDE,SLIER,SLILY,SLIME,SLIMS,SLIMY,SLING,SLINK,SLIPE,SLIPS,SLIPT,SLISH,SLITS,' &&
      'SLIVE,SLOAN,SLOBS,SLOES,SLOGS,SLOID,SLOJD,SLOMO,SLOOM,SLOOP,SLOOT,SLOPE,SLOPS,SLOPY,SLORM,SLOSH,SLOTH,SLOTS,SLOVE,' &&
      'SLOWS,SLOYD,SLUBB,SLUBS,SLUED,SLUES,SLUFF,SLUGS,SLUIT,SLUMP,SLUMS,SLUNG,SLUNK,SLURB,SLURP,SLURS,SLUSE,SLUSH,SLUTS,' &&
      'SLYER,SLYLY,SLYPE,SMAAK,SMACK,SMAIK,SMALL,SMALM,SMALT,SMARM,SMART,SMASH,SMAZE,SMEAR,SMEEK,SMEES,SMEIK,SMEKE,SMELL,' &&
      'SMELT,SMERK,SMEWS,SMILE,SMIRK,SMIRR,SMIRS,SMITE,SMITH,SMITS,SMOCK,SMOGS,SMOKE,SMOKO,SMOKY,SMOLT,SMOOR,SMOOT,SMORE,' &&
      'SMORG,SMOTE,SMOUT,SMOWT,SMUGS,SMURS,SMUSH,SMUTS,SNABS,SNACK,SNAFU,SNAGS,SNAIL,SNAKE,SNAKY,SNAPS,SNARE,SNARF,SNARK,' &&
      'SNARL,SNARS,SNARY,SNASH,SNATH,SNAWS,SNEAD,SNEAK,SNEAP,SNEBS,SNECK,SNEDS,SNEED,SNEER,SNEES,SNELL,SNIBS,SNICK,SNIDE,' &&
      'SNIES,SNIFF,SNIFT,SNIGS,SNIPE,SNIPS,SNIPY,SNIRT,SNITS,SNOBS,SNODS,SNOEK,SNOEP,SNOGS,SNOKE,SNOOD,SNOOK,SNOOL,SNOOP,' &&
      'SNOOT,SNORE,SNORT,SNOTS,SNOUT,SNOWK,SNOWS,SNOWY,SNUBS,SNUCK,SNUFF,SNUGS,SNUSH,SNYES,SOAKS,SOAPS,SOAPY,SOARE,SOARS,' &&
      'SOAVE,SOBAS,SOBER,SOCAS,SOCES,SOCKO,SOCKS,SOCLE,SODAS,SODDY,SODIC,SODOM,SOFAR,SOFAS,SOFTA,SOFTS,SOFTY,SOGER,SOGGY,' &&
      'SOHUR,SOILS,SOILY,SOJAS,SOJUS,SOKAH,SOKEN,SOKES,SOKOL,SOLAH,SOLAN,SOLAR,SOLAS,SOLDE,SOLDI,SOLDO,SOLDS,SOLED,SOLEI,' &&
      'SOLER,SOLES,SOLID,SOLON,SOLOS,SOLUM,SOLUS,SOLVE,SOMAN,SOMAS,SONAR,SONCE,SONDE,SONES,SONGS,SONIC,SONLY,SONNE,SONNY,' &&
      'SONSE,SONSY,SOOEY,SOOKS,SOOKY,SOOLE,SOOLS,SOOMS,SOOPS,SOOTE,SOOTH,SOOTS,SOOTY,SOPHS,SOPHY,SOPOR,SOPPY,SOPRA,SORAL,' &&
      'SORAS,SORBO,SORBS,SORDA,SORDO,SORDS,SORED,SOREE,SOREL,SORER,SORES,SOREX,SORGO,SORNS,SORRA,SORRY,SORTA,SORTS,SORUS,' &&
      'SOTHS,SOTOL,SOUCE,SOUCT,SOUGH,SOUKS,SOULS,SOUMS,SOUND,SOUPS,SOUPY,SOURS,SOUSE,SOUTH,SOUTS,SOWAR,SOWCE,SOWED,SOWER,' &&
      'SOWFF,SOWFS,SOWLE,SOWLS,SOWMS,SOWND,SOWNE,SOWPS,SOWSE,SOWTH,SOYAS,SOYLE,SOYUZ,SOZIN,SPACE,SPACY,SPADE,SPADO,SPAED,' &&
      'SPAER,SPAES,SPAGS,SPAHI,SPAIL,SPAIN,SPAIT,SPAKE,SPALD,SPALE,SPALL,SPALT,SPAMS,SPANE,SPANG,SPANK,SPANS,SPARD,SPARE,' &&
      'SPARK,SPARS,SPART,SPASM,SPATE,SPATS,SPAUL,SPAWL,SPAWN,SPAWS,SPAYD,SPAYS,SPAZA,SPEAK,SPEAL,SPEAN,SPEAR,SPEAT,SPECK,' &&
      'SPECS,SPECT,SPEED,SPEEL,SPEER,SPEIL,SPEIR,SPEKS,SPELD,SPELK,SPELL,SPELT,SPEND,SPENT,SPEOS,SPERM,SPETS,SPEUG,SPEWS,' &&
      'SPEWY,SPIAL,SPICA,SPICE,SPICK,SPICY,SPIDE,SPIED,SPIEL,SPIER,SPIES,SPIFF,SPIFS,SPIKE,SPIKY,SPILE,SPILL,SPILT,SPIMS,' &&
      'SPINA,SPINE,SPINK,SPINS,SPINY,SPIRE,SPIRT,SPIRY,SPITE,SPITS,SPITZ,SPIVS,SPLAT,SPLAY,SPLIT,SPLOG,SPODE,SPODS,SPOIL,' &&
      'SPOKE,SPOOF,SPOOK,SPOOL,SPOOM,SPOON,SPOOR,SPOOT,SPORE,SPORK,SPORT,SPOSH,SPOTS,SPOUT,SPRAD,SPRAG,SPRAT,SPRAY,SPRED,' &&
      'SPREE,SPREW,SPRIG,SPRIT,SPROD,SPROG,SPRUE,SPRUG,SPUDS,SPUED,SPUER,SPUES,SPUGS,SPULE,SPUME,SPUMY,SPUNK,SPURN,SPURS,' &&
      'SPURT,SPUTA,SPYAL,SPYRE,SQUAB,SQUAD,SQUAT,SQUEG,SQUIB,SQUID,SQUIT,SQUIZ,STABS,STACK,STADE,STAFF,STAGE,STAGS,STAGY,' &&
      'STAID,STAIG,STAIN,STAIR,STAKE,STALE,STALK,STALL,STAMP,STAND,STANE,STANG,STANK,STAPH,STAPS,STARE,STARK,STARN,STARR,' &&
      'STARS,START,STASH,STATE,STATS,STAUN,STAVE,STAWS,STAYS,STEAD,STEAK,STEAL,STEAM,STEAN,STEAR,STEDD,STEDE,STEDS,STEED,' &&
      'STEEK,STEEL,STEEM,STEEN,STEEP,STEER,STEIL,STEIN,STELA,STELE,STELL,STEME,STEMS,STEND,STENO,STENS,STENT,STEPS,STEPT,' &&
      'STERE,STERN,STETS,STEWS,STEWY,STEYS,STICH,STICK,STIED,STIES,STIFF,STILB,STILE,STILL,STILT,STIME,STIMS,STIMY,STING,' &&
      'STINK,STINT,STIPA,STIPE,STIRE,STIRK,STIRP,STIRS,STIVE,STIVY,STOAE,STOAI,STOAS,STOAT,STOBS,STOCK,STOEP,STOGY,STOIC,' &&
      'STOIT,STOKE,STOLE,STOLN,STOMA,STOMP,STOND,STONE,STONG,STONK,STONN,STONY,STOOD,STOOK,STOOL,STOOP,STOOR,STOPE,STOPS,' &&
      'STOPT,STORE,STORK,STORM,STORY,STOSS,STOTS,STOTT,STOUN,STOUP,STOUR,STOUT,STOVE,STOWN,STOWP,STOWS,STRAD,STRAE,STRAG,' &&
      'STRAK,STRAP,STRAW,STRAY,STREP,STREW,STRIA,STRIG,STRIM,STRIP,STROP,STROW,STROY,STRUM,STRUT,STUBS,STUCK,STUDE,STUDS,' &&
      'STUDY,STUFF,STULL,STULM,STUMM,STUMP,STUMS,STUNG,STUNK,STUNS,STUNT,STUPA,STUPE,STURE,STURT,STYED,STYES,STYLE,STYLI,' &&
      'STYLO,STYME,STYMY,STYRE,STYTE,SUAVE,SUBAH,SUBAS,SUBBY,SUBER,SUBHA,SUCCI,SUCKS,SUCKY,SUCRE,SUDDS,SUDOR,SUDSY,SUEDE,' &&
      'SUENT,SUERS,SUETE,SUETS,SUETY,SUGAN,SUGAR,SUGHS,SUGOS,SUHUR,SUIDS,SUING,SUINT,SUITE,SUITS,SUJEE,SUKHS,SUKUK,SULCI,' &&
      'SULFA,SULFO,SULKS,SULKY,SULLY,SULPH,SULUS,SUMAC,SUMIS,SUMMA,SUMOS,SUMPH,SUMPS,SUNIS,SUNKS,SUNNA,SUNNS,SUNNY,SUNUP,' &&
      'SUPER,SUPES,SUPRA,SURAH,SURAL,SURAS,SURAT,SURDS,SURED,SURER,SURES,SURFS,SURFY,SURGE,SURGY,SURLY,SURRA,SUSED,SUSES,' &&
      'SUSHI,SUSUS,SUTOR,SUTRA,SUTTA,SWABS,SWACK,SWADS,SWAGE,SWAGS,SWAIL,SWAIN,SWALE,SWALY,SWAMI,SWAMP,SWAMY,SWANG,SWANK,' &&
      'SWANS,SWAPS,SWAPT,SWARD,SWARE,SWARF,SWARM,SWART,SWASH,SWATH,SWATS,SWAYL,SWAYS,SWEAL,SWEAR,SWEAT,SWEDE,SWEED,SWEEL,' &&
      'SWEEP,SWEER,SWEES,SWEET,SWEIR,SWELL,SWELT,SWEPT,SWERF,SWEYS,SWIES,SWIFT,SWIGS,SWILE,SWILL,SWIMS,SWINE,SWING,SWINK,' &&
      'SWIPE,SWIRE,SWIRL,SWISH,SWISS,SWITH,SWITS,SWIVE,SWIZZ,SWOBS,SWOLE,SWOLN,SWOON,SWOOP,SWOPS,SWOPT,SWORD,SWORE,SWORN,' &&
      'SWOTS,SWOUN,SWUNG,SYBBE,SYBIL,SYBOE,SYBOW,SYCEE,SYCES,SYCON,SYENS,SYKER,SYKES,SYLIS,SYLPH,SYLVA,SYMAR,SYNCH,SYNCS,' &&
      'SYNDS,SYNED,SYNES,SYNOD,SYNTH,SYPED,SYPES,SYPHS,SYRAH,SYREN,SYRUP,SYSOP,SYTHE,SYVER,TAALS,TAATA,TABBY,TABER,TABES,' &&
      'TABID,TABIS,TABLA,TABLE,TABOO,TABOR,TABUN,TABUS,TACAN,TACES,TACET,TACHE,TACHO,TACHS,TACIT,TACKS,TACKY,TACOS,TACTS,' &&
      'TAELS,TAFFY,TAFIA,TAGGY,TAGMA,TAHAS,TAHRS,TAIGA,TAIKO,TAILS,TAINS,TAINT,TAIRA,TAISH,TAITS,TAJES,TAKAS,TAKEN,TAKER,' &&
      'TAKES,TAKHI,TAKIN,TAKIS,TAKKY,TALAK,TALAQ,TALAR,TALAS,TALCS,TALCY,TALEA,TALER,TALES,TALKS,TALKY,TALLS,TALLY,TALMA,' &&
      'TALON,TALPA,TALUK,TALUS,TAMAL,TAMED,TAMER,TAMES,TAMIN,TAMIS,TAMMY,TAMPS,TANAS,TANGA,TANGI,TANGO,TANGS,TANGY,TANHS,' &&
      'TANKA,TANKS,TANKY,TANNA,TANSY,TANTI,TANTO,TANTY,TAPAS,TAPED,TAPEN,TAPER,TAPES,TAPET,TAPIR,TAPIS,TAPPA,TAPUS,TARAS,' &&
      'TARDO,TARDY,TARED,TARES,TARGA,TARGE,TARNS,TAROC,TAROK,TAROS,TAROT,TARPS,TARRE,TARRY,TARSI,TARTS,TARTY,TASAR,TASED,' &&
      'TASER,TASES,TASKS,TASSA,TASSE,TASSO,TASTE,TASTY,TATAR,TATER,TATES,TATHS,TATIE,TATOU,TATTS,TATTY,TATUS,TAUBE,TAULD,' &&
      'TAUNT,TAUON,TAUPE,TAUTS,TAVAH,TAVAS,TAVER,TAWAI,TAWAS,TAWED,TAWER,TAWIE,TAWNY,TAWSE,TAWTS,TAXED,TAXER,TAXES,TAXIS,' &&
      'TAXOL,TAXON,TAXOR,TAXUS,TAYRA,TAZZA,TAZZE,TEACH,TEADE,TEADS,TEAED,TEAKS,TEALS,TEAMS,TEARS,TEARY,TEASE,TEATS,TEAZE,' &&
      'TECHS,TECHY,TECTA,TEDDY,TEELS,TEEMS,TEEND,TEENE,TEENS,TEENY,TEERS,TEETH,TEFFS,TEGGS,TEGUA,TEGUS,TEHRS,TEIID,TEILS,' &&
      'TEIND,TEINS,TELAE,TELCO,TELES,TELEX,TELIA,TELIC,TELLS,TELLY,TELOI,TELOS,TEMED,TEMES,TEMPI,TEMPO,TEMPS,TEMPT,TEMSE,' &&
      'TENCH,TENDS,TENDU,TENES,TENET,TENGE,TENIA,TENNE,TENNO,TENNY,TENON,TENOR,TENSE,TENTH,TENTS,TENTY,TENUE,TEPAL,TEPAS,' &&
      'TEPEE,TEPID,TEPOY,TERAI,TERAS,TERCE,TEREK,TERES,TERFE,TERFS,TERGA,TERMS,TERNE,TERNS,TERRA,TERRY,TERSE,TERTS,TESLA,' &&
      'TESTA,TESTE,TESTS,TESTY,TETES,TETHS,TETRA,TETRI,TEUCH,TEUGH,TEWED,TEWEL,TEWIT,TEXAS,TEXES,TEXTS,THACK,THAGI,THAIM,' &&
      'THALE,THALI,THANA,THANE,THANG,THANK,THANS,THANX,THARM,THARS,THAWS,THAWY,THEBE,THECA,THEED,THEEK,THEES,THEFT,THEGN,' &&
      'THEIC,THEIN,THEIR,THELF,THEMA,THEME,THENS,THEOW,THERE,THERM,THESE,THESP,THETA,THETE,THEWS,THEWY,THICK,THIEF,THIGH,' &&
      'THIGS,THILK,THILL,THINE,THING,THINK,THINS,THIOL,THIRD,THIRL,THOFT,THOLE,THOLI,THONG,THORN,THORO,THORP,THOSE,THOUS,' &&
      'THOWL,THRAE,THRAW,THREE,THREW,THRID,THRIP,THROB,THROE,THROW,THRUM,THUDS,THUGS,THUJA,THUMB,THUMP,THUNK,THURL,THUYA,' &&
      'THYME,THYMI,THYMY,TIANS,TIARA,TIARS,TIBIA,TICAL,TICCA,TICED,TICES,TICHY,TICKS,TICKY,TIDAL,TIDDY,TIDED,TIDES,TIERS,' &&
      'TIFFS,TIFOS,TIFTS,TIGER,TIGES,TIGHT,TIGON,TIKAS,TIKES,TIKIS,TIKKA,TILAK,TILDE,TILED,TILER,TILES,TILLS,TILLY,TILTH,' &&
      'TILTS,TIMBO,TIMED,TIMER,TIMES,TIMID,TIMON,TIMPS,TINAS,TINCT,TINDS,TINEA,TINED,TINES,TINGE,TINGS,TINKS,TINNY,TINTS,' &&
      'TINTY,TIPIS,TIPPY,TIPSY,TIRED,TIRES,TIRLS,TIROS,TIRRS,TITAN,TITCH,TITER,TITHE,TITIS,TITLE,TITRE,TITTY,TITUP,TIYIN,' &&
      'TIYNS,TIZES,TIZZY,TOADS,TOADY,TOAST,TOAZE,TOCKS,TOCKY,TOCOS,TODAY,TODDE,TODDY,TOEAS,TOFFS,TOFFY,TOFTS,TOFUS,TOGAE,' &&
      'TOGAS,TOGED,TOGES,TOGUE,TOHOS,TOILE,TOILS,TOING,TOISE,TOITS,TOKAY,TOKED,TOKEN,TOKER,TOKES,TOKOS,TOLAN,TOLAR,TOLAS,' &&
      'TOLED,TOLES,TOLLS,TOLLY,TOLTS,TOLUS,TOLYL,TOMAN,TOMBS,TOMES,TOMIA,TOMMY,TOMOS,TONAL,TONDI,TONDO,TONED,TONER,TONES,' &&
      'TONEY,TONGA,TONGS,TONIC,TONKA,TONKS,TONNE,TONUS,TOOLS,TOOMS,TOONS,TOOTH,TOOTS,TOPAZ,TOPED,TOPEE,TOPEK,TOPER,TOPES,' &&
      'TOPHE,TOPHI,TOPHS,TOPIC,TOPIS,TOPOI,TOPOS,TOPPY,TOQUE,TORAH,TORAN,TORAS,TORCH,TORCS,TORES,TORIC,TORII,TOROS,TOROT,' &&
      'TORRS,TORSE,TORSI,TORSK,TORSO,TORTA,TORTE,TORTS,TORUS,TOSAS,TOSED,TOSES,TOSHY,TOSSY,TOTAL,TOTED,TOTEM,TOTER,TOTES,' &&
      'TOTTY,TOUCH,TOUGH,TOUKS,TOUNS,TOURS,TOUSE,TOUSY,TOUTS,TOUZE,TOUZY,TOWED,TOWEL,TOWER,TOWIE,TOWNS,TOWNY,TOWSE,TOWSY,' &&
      'TOWTS,TOWZE,TOWZY,TOXIC,TOXIN,TOYED,TOYER,TOYON,TOYOS,TOZED,TOZES,TOZIE,TRABS,TRACE,TRACK,TRACT,TRADE,TRADS,TRAGI,' &&
      'TRAIK,TRAIL,TRAIN,TRAIT,TRAMP,TRAMS,TRANK,TRANQ,TRANS,TRANT,TRAPE,TRAPS,TRAPT,TRASH,TRASS,TRATS,TRATT,TRAVE,TRAWL,' &&
      'TRAYF,TRAYS,TREAD,TREAT,TRECK,TREED,TREEN,TREES,TREFA,TREIF,TREKS,TREMA,TREMS,TREND,TRESS,TREST,TRETS,TREWS,TREYF,' &&
      'TREYS,TRIAC,TRIAD,TRIAL,TRIBE,TRICE,TRICK,TRIDE,TRIED,TRIER,TRIES,TRIFF,TRIGO,TRIGS,TRIKE,TRILD,TRILL,TRIMS,TRINE,' &&
      'TRINS,TRIOL,TRIOR,TRIOS,TRIPE,TRIPS,TRIPY,TRIST,TRITE,TROAD,TROAK,TROAT,TROCK,TRODE,TRODS,TROGS,TROIS,TROKE,TROLL,' &&
      'TROMP,TRONA,TRONC,TRONE,TRONK,TRONS,TROOP,TROOZ,TROPE,TROTH,TROTS,TROUT,TROVE,TROWS,TROYS,TRUCE,TRUCK,TRUED,TRUER,' &&
      'TRUES,TRUGO,TRUGS,TRULL,TRULY,TRUMP,TRUNK,TRUSS,TRUST,TRUTH,TRYER,TRYKE,TRYMA,TRYPS,TRYST,TSADE,TSADI,TSARS,TSKED,' &&
      'TSUBA,TSUBO,TUANS,TUART,TUATH,TUBAE,TUBAL,TUBAR,TUBAS,TUBBY,TUBED,TUBER,TUBES,TUCKS,TUFAS,TUFFE,TUFFS,TUFTS,TUFTY,' &&
      'TUGRA,TUILE,TUINA,TUISM,TUKTU,TULES,TULIP,TULLE,TULPA,TULSI,TUMID,TUMMY,TUMOR,TUMPS,TUMPY,TUNAS,TUNDS,TUNED,TUNER,' &&
      'TUNES,TUNGS,TUNIC,TUNNY,TUPEK,TUPIK,TUPLE,TUQUE,TURBO,TURDS,TURFS,TURFY,TURKS,TURME,TURMS,TURNS,TURNT,TURPS,TURRS,' &&
      'TUSHY,TUSKS,TUSKY,TUTEE,TUTOR,TUTTI,TUTTY,TUTUS,TUXES,TUYER,TWAES,TWAIN,TWALS,TWANG,TWANK,TWATS,TWAYS,TWEAK,TWEED,' &&
      'TWEEL,TWEEN,TWEEP,TWEER,TWEET,TWERK,TWERP,TWICE,TWIER,TWIGS,TWILL,TWILT,TWINE,TWINK,TWINS,TWINY,TWIRE,TWIRL,TWIRP,' &&
      'TWIST,TWITE,TWITS,TWIXT,TWOER,TWYER,TYEES,TYERS,TYING,TYIYN,TYKES,TYLER,TYMPS,TYNDE,TYNED,TYNES,TYPAL,TYPED,TYPES,' &&
      'TYPEY,TYPIC,TYPOS,TYPPS,TYPTO,TYRAN,TYRED,TYRES,TYROS,TYTHE,TZARS,UDALS,UDDER,UDONS,UGALI,UGGED,UHLAN,UHURU,UKASE,' &&
      'ULAMA,ULANS,ULCER,ULEMA,ULMIN,ULNAD,ULNAE,ULNAR,ULNAS,ULPAN,ULTRA,ULVAS,ULYIE,ULZIE,UMAMI,UMBEL,UMBER,UMBLE,UMBOS,' &&
      'UMBRA,UMBRE,UMIAC,UMIAK,UMIAQ,UMMAH,UMMAS,UMMED,UMPED,UMPHS,UMPIE,UMPTY,UMRAH,UMRAS,UNAIS,UNAPT,UNARM,UNARY,UNAUS,' &&
      'UNBAG,UNBAN,UNBAR,UNBED,UNBID,UNBOX,UNCAP,UNCES,UNCIA,UNCLE,UNCOS,UNCOY,UNCUS,UNCUT,UNDAM,UNDEE,UNDER,UNDID,UNDOS,' &&
      'UNDUE,UNDUG,UNETH,UNFED,UNFIT,UNFIX,UNGAG,UNGET,UNGOD,UNGOT,UNGUM,UNHAT,UNHIP,UNICA,UNIFY,UNION,UNITE,UNITS,UNITY,' &&
      'UNJAM,UNKED,UNKET,UNKID,UNLAW,UNLAY,UNLED,UNLET,UNLID,UNLIT,UNMAN,UNMET,UNMEW,UNMIX,UNPAY,UNPEG,UNPEN,UNPIN,UNRED,' &&
      'UNRID,UNRIG,UNRIP,UNSAW,UNSAY,UNSEE,UNSET,UNSEW,UNSEX,UNSOD,UNTAX,UNTIE,UNTIL,UNTIN,UNWED,UNWET,UNWIT,UNWON,UNZIP,' &&
      'UPBOW,UPBYE,UPDOS,UPDRY,UPEND,UPJET,UPLAY,UPLED,UPLIT,UPPED,UPPER,UPRAN,UPRUN,UPSEE,UPSET,UPSEY,UPTAK,UPTER,UPTIE,' &&
      'URAEI,URALI,URAOS,URARE,URARI,URASE,URATE,URBAN,URBEX,URBIA,URDEE,UREAL,UREAS,UREDO,UREIC,URENA,URENT,URGED,URGER,' &&
      'URGES,URIAL,URINE,URITE,URMAN,URNAL,URNED,URPED,URSAE,URSID,URSON,URUBU,URVAS,USAGE,USERS,USHER,USING,USNEA,USQUE,' &&
      'USUAL,USURE,USURP,USURY,UTERI,UTILE,UTTER,UVEAL,UVEAS,UVULA,VACUA,VADED,VADES,VAGAL,VAGUE,VAGUS,VAILS,VAIRE,VAIRS,' &&
      'VAIRY,VAKAS,VAKIL,VALES,VALET,VALID,VALIS,VALOR,VALSE,VALUE,VALVE,VAMPS,VAMPY,VANDA,VANED,VANES,VANGS,VANTS,VAPED,' &&
      'VAPER,VAPES,VAPID,VAPOR,VARAN,VARAS,VARDY,VAREC,VARES,VARIA,VARIX,VARNA,VARUS,VARVE,VASAL,VASES,VASTS,VASTY,VATIC,' &&
      'VATUS,VAUCH,VAULT,VAUNT,VAUTE,VAUTS,VAWTE,VAXES,VEALE,VEALS,VEALY,VEENA,VEEPS,VEERS,VEERY,VEGAN,VEGAS,VEGES,VEGIE,' &&
      'VEGOS,VEHME,VEILS,VEILY,VEINS,VEINY,VELAR,VELDS,VELDT,VELES,VELLS,VELUM,VENAE,VENAL,VENDS,VENEY,VENGE,VENIN,VENOM,' &&
      'VENTS,VENUE,VENUS,VERBS,VERGE,VERRA,VERRY,VERSE,VERSO,VERST,VERTS,VERTU,VERVE,VESPA,VESTA,VESTS,VETCH,VEXED,VEXER,' &&
      'VEXES,VEXIL,VEZIR,VIALS,VIAND,VIBES,VIBEX,VIBEY,VICAR,VICED,VICES,VICHY,VIDEO,VIERS,VIEWS,VIEWY,VIFDA,VIFFS,VIGAS,' &&
      'VIGIA,VIGIL,VIGOR,VILDE,VILER,VILLA,VILLI,VILLS,VIMEN,VINAL,VINAS,VINCA,VINED,VINER,VINES,VINEW,VINIC,VINOS,VINTS,' &&
      'VINYL,VIOLA,VIOLD,VIOLS,VIPER,VIRAL,VIRED,VIREO,VIRES,VIRGA,VIRGE,VIRID,VIRLS,VIRTU,VIRUS,VISAS,VISED,VISES,VISIE,' &&
      'VISIT,VISNE,VISON,VISOR,VISTA,VISTO,VITAE,VITAL,VITAS,VITEX,VITRO,VITTA,VIVAS,VIVAT,VIVDA,VIVER,VIVES,VIVID,VIXEN,' &&
      'VIZIR,VIZOR,VLEIS,VLIES,VLOGS,VOARS,VOCAB,VOCAL,VOCES,VODDY,VODKA,VODOU,VODUN,VOEMA,VOGIE,VOGUE,VOICE,VOIDS,VOILA,' &&
      'VOILE,VOIPS,VOLAE,VOLAR,VOLED,VOLES,VOLET,VOLKS,VOLTA,VOLTE,VOLTI,VOLTS,VOLVA,VOLVE,VOMER,VOMIT,VOTED,VOTER,VOTES,' &&
      'VOUCH,VOUGE,VOULU,VOWED,VOWEL,VOWER,VOXEL,VOZHD,VRAIC,VRILS,VROOM,VROUS,VROUW,VROWS,VUGGS,VUGGY,VUGHS,VUGHY,VULGO,' &&
      'VULNS,VULVA,VUTTY,VYING,WAACS,WACKE,WACKO,WACKS,WACKY,WADDS,WADDY,WADED,WADER,WADES,WADGE,WADIS,WADTS,WAFER,WAFFS,' &&
      'WAFTS,WAGED,WAGER,WAGES,WAGGA,WAGON,WAGYU,WAHOO,WAIDE,WAIFS,WAIFT,WAILS,WAINS,WAIRS,WAIST,WAITE,WAITS,WAIVE,WAKAS,' &&
      'WAKED,WAKEN,WAKER,WAKES,WAKFS,WALDO,WALDS,WALED,WALER,WALES,WALIE,WALIS,WALKS,WALLA,WALLS,WALLY,WALTY,WALTZ,WAMED,' &&
      'WAMES,WAMUS,WANDS,WANED,WANES,WANEY,WANGS,WANKS,WANKY,WANLE,WANLY,WANNA,WANTS,WANTY,WANZE,WAQFS,WARBS,WARBY,WARDS,' &&
      'WARED,WARES,WAREZ,WARKS,WARMS,WARNS,WARPS,WARRE,WARST,WARTS,WARTY,WASES,WASHY,WASMS,WASPS,WASPY,WASTE,WASTS,WATAP,' &&
      'WATCH,WATER,WATTS,WAUFF,WAUGH,WAUKS,WAULK,WAULS,WAURS,WAVED,WAVER,WAVES,WAVEY,WAWAS,WAWES,WAWLS,WAXED,WAXEN,WAXER,' &&
      'WAXES,WAYED,WAZIR,WAZOO,WEALD,WEALS,WEAMB,WEANS,WEARS,WEARY,WEAVE,WEBBY,WEBER,WECHT,WEDEL,WEDGE,WEDGY,WEEDS,WEEDY,' &&
      'WEEKE,WEEKS,WEELS,WEEMS,WEENS,WEENY,WEEPS,WEEPY,WEEST,WEETE,WEETS,WEFTE,WEFTS,WEIDS,WEIGH,WEILS,WEIRD,WEIRS,WEISE,' &&
      'WEIZE,WEKAS,WELCH,WELDS,WELKE,WELKS,WELKT,WELLS,WELLY,WELSH,WELTS,WEMBS,WENCH,WENDS,WENGE,WENNY,WENTS,WEROS,WERSH,' &&
      'WESTS,WETAS,WETLY,WEXED,WEXES,WHACK,WHALE,WHAMO,WHAMS,WHANG,WHAPS,WHARE,WHARF,WHATA,WHATS,WHAUP,WHAUR,WHEAL,WHEAR,' &&
      'WHEAT,WHEEL,WHEEN,WHEEP,WHEFT,WHELK,WHELM,WHELP,WHENS,WHERE,WHETS,WHEWS,WHEYS,WHICH,WHIDS,WHIFF,WHIFT,WHIGS,WHILE,' &&
      'WHILK,WHIMS,WHINE,WHINS,WHINY,WHIOS,WHIPS,WHIPT,WHIRL,WHIRR,WHIRS,WHISH,WHISK,WHISS,WHIST,WHITE,WHITS,WHITY,WHIZZ,' &&
      'WHOLE,WHOMP,WHOOF,WHOOP,WHOOT,WHOPS,WHORE,WHORL,WHORT,WHOSE,WHOSO,WHOWS,WHUMP,WHUPS,WHYDA,WICCA,WICKS,WICKY,WIDDY,' &&
      'WIDEN,WIDER,WIDES,WIDOW,WIDTH,WIELD,WIELS,WIFED,WIFES,WIFEY,WIFIE,WIFTY,WIGAN,WIGGY,WIGHT,WIKIS,WILCO,WILDS,WILED,' &&
      'WILES,WILGA,WILIS,WILJA,WILLS,WILLY,WILTS,WIMPS,WIMPY,WINCE,WINCH,WINDS,WINDY,WINED,WINES,WINEY,WINGE,WINGS,WINGY,' &&
      'WINKS,WINNA,WINNS,WINOS,WINZE,WIPED,WIPER,WIPES,WIRED,WIRER,WIRES,WIRRA,WISED,WISER,WISES,WISHA,WISHT,WISPS,WISPY,' &&
      'WISTS,WITAN,WITCH,WITED,WITES,WITHE,WITHS,WITHY,WITTY,WIVED,WIVER,WIVES,WIZEN,WIZES,WOADS,WOALD,WOCKS,WODGE,WOFUL,' &&
      'WOJUS,WOKEN,WOKER,WOKKA,WOLDS,WOLFS,WOLLY,WOLVE,WOMAN,WOMBS,WOMBY,WOMEN,WOMYN,WONGA,WONGI,WONKS,WONKY,WONTS,WOODS,' &&
      'WOODY,WOOED,WOOER,WOOFS,WOOFY,WOOLD,WOOLS,WOOLY,WOONS,WOOPS,WOOPY,WOOSE,WOOSH,WOOTZ,WOOZY,WORDS,WORDY,WORKS,WORLD,' &&
      'WORMS,WORMY,WORRY,WORSE,WORST,WORTH,WORTS,WOULD,WOUND,WOVEN,WOWED,WOWEE,WOXEN,WRACK,WRANG,WRAPS,WRAPT,WRAST,WRATE,' &&
      'WRATH,WRAWL,WREAK,WRECK,WRENS,WREST,WRICK,WRIED,WRIER,WRIES,WRING,WRIST,WRITE,WRITS,WROKE,WRONG,WROOT,WROTE,WROTH,' &&
      'WRUNG,WRYER,WRYLY,WUDDY,WUDUS,WULLS,WURST,WUSES,WUSHU,WUSSY,WUXIA,WYLED,WYLES,WYNDS,WYNNS,WYTED,WYTES,XEBEC,XENIA,' &&
      'XENIC,XENON,XERIC,XEROX,XERUS,XOANA,XRAYS,XYLAN,XYLEM,XYLIC,XYLOL,XYLYL,XYSTI,XYSTS,YAARS,YABAS,YABBA,YABBY,YACCA,' &&
      'YACHT,YACKA,YACKS,YAFFS,YAGER,YAGES,YAGIS,YAHOO,YAIRD,YAKKA,YAKOW,YALES,YAMEN,YAMPY,YAMUN,YANGS,YANKS,YAPOK,YAPON,' &&
      'YAPPS,YAPPY,YARAK,YARCO,YARDS,YARER,YARFA,YARKS,YARNS,YARRS,YARTA,YARTO,YATES,YAUDS,YAULD,YAUPS,YAWED,YAWEY,YAWLS,' &&
      'YAWNS,YAWNY,YAWPS,YBORE,YCLAD,YCLED,YCOND,YDRAD,YDRED,YEADS,YEAHS,YEALM,YEANS,YEARD,YEARN,YEARS,YEAST,YECCH,YECHS,' &&
      'YECHY,YEDES,YEEDS,YEESH,YEGGS,YELKS,YELLS,YELMS,YELPS,YELTS,YENTA,YENTE,YERBA,YERDS,YERKS,YESES,YESKS,YESTS,YESTY,' &&
      'YETIS,YETTS,YEUKS,YEUKY,YEVEN,YEVES,YEWEN,YEXED,YEXES,YFERE,YIELD,YIKED,YIKES,YILLS,YINCE,YIPES,YIPPY,YIRDS,YIRKS,' &&
      'YIRRS,YIRTH,YITES,YITIE,YLEMS,YLIKE,YLKES,YMOLT,YMPES,YOBBO,YOBBY,YOCKS,YODEL,YODHS,YODLE,YOGAS,YOGEE,YOGHS,YOGIC,' &&
      'YOGIN,YOGIS,YOICK,YOJAN,YOKED,YOKEL,YOKER,YOKES,YOKUL,YOLKS,YOLKY,YOMIM,YOMPS,YONIC,YONIS,YONKS,YOOFS,YOOPS,YORES,' &&
      'YORKS,YORPS,YOUKS,YOUNG,YOURN,YOURS,YOURT,YOUSE,YOUTH,YOWED,YOWES,YOWIE,YOWLS,YOWZA,YRAPT,YRENT,YRIVD,YRNEH,YSAME,' &&
      'YTOST,YUANS,YUCAS,YUCCA,YUCCH,YUCKO,YUCKS,YUCKY,YUFTS,YUGAS,YUKED,YUKES,YUKKY,YUKOS,YULAN,YULES,YUMMO,YUMMY,YUMPS,' &&
      'YUPON,YUPPY,YURTA,YURTS,YUZUS,ZABRA,ZACKS,ZAIDA,ZAIDY,ZAIRE,ZAKAT,ZAMAN,ZAMIA,ZANJA,ZANTE,ZANZA,ZANZE,ZAPPY,ZARFS,' &&
      'ZARIS,ZATIS,ZAXES,ZAYIN,ZAZEN,ZEALS,ZEBEC,ZEBRA,ZEBUB,ZEBUS,ZEDAS,ZEINS,ZENDO,ZERDA,ZERKS,ZEROS,ZESTS,ZESTY,ZETAS,' &&
      'ZEXES,ZEZES,ZHOMO,ZIBET,ZIFFS,ZIGAN,ZILAS,ZILCH,ZILLA,ZILLS,ZIMBI,ZIMBS,ZINCO,ZINCS,ZINCY,ZINEB,ZINES,ZINGS,ZINGY,' &&
      'ZINKE,ZINKY,ZIPPO,ZIPPY,ZIRAM,ZITIS,ZIZEL,ZIZIT,ZLOTE,ZLOTY,ZOAEA,ZOBOS,ZOBUS,ZOCCO,ZOEAE,ZOEAL,ZOEAS,ZOISM,ZOIST,' &&
      'ZOMBI,ZONAE,ZONAL,ZONDA,ZONED,ZONER,ZONES,ZONKS,ZOOEA,ZOOEY,ZOOID,ZOOKS,ZOOMS,ZOONS,ZOOTY,ZOPPA,ZOPPO,ZORIL,ZORIS,' &&
      'ZORRO,ZOUKS,ZOWEE,ZOWIE,ZULUS,ZUPAN,ZUPAS,ZUPPA,ZURFS,ZUZIM,ZYGAL,ZYGON,ZYMES,ZYMIC'.

    split lv_words at ',' into table word_tab.

  endmethod.


endclass.

" START-OF-SELECTION.
data wordle_assistant type ref to lcl_wordle.

create object wordle_assistant.

" Example:
"
" RANGE (A orange)
" ATLAS (ALS orange)
" SLASH (HL orange, SA green, EGNRT black)  <<< test case
" SHALL (all green)
"
" wordle_assistant->main(
"   i_letter_1       = 'S'
"   i_letter_2       = ''
"   i_letter_3       = 'A'
"   i_letter_4       = ''
"   i_letter_5       = ''
"   i_black_letters  = 'EGNRT'
"   i_orange_letters = 'HL'
" ).

wordle_assistant->main(
  i_letter_1       = ''
  i_letter_2       = ''
  i_letter_3       = ''
  i_letter_4       = ''
  i_letter_5       = ''
  i_black_letters  = ''
  i_orange_letters = ''
).