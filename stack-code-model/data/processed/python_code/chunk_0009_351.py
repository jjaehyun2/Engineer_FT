* Copyright 2019 IBM Corp. All Rights Reserved.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
"! <h1>Visual Recognition</h1>
"! The IBM Watson&trade; Visual Recognition service uses deep learning algorithms
"!  to identify scenes and objects in images that you upload to the service. You
"!  can create and train a custom classifier to identify subjects that suit your
"!  needs. <br/>
class ZCL_IBMC_VISUAL_RECOGNITION_V3 DEFINITION
  public
  inheriting from ZCL_IBMC_SERVICE_EXT
  create public .

public section.
  types:
    "!   Number of images processed for the API call.
      T_IMAGES_PROCESSED type Integer.
  types:
    "!   Result of a class within a classifier.
    begin of T_CLASS_RESULT,
      CLASS type STRING,
      SCORE type FLOAT,
      TYPE_HIERARCHY type STRING,
    end of T_CLASS_RESULT.
  types:
    "!   Classifier and score combination.
    begin of T_CLASSIFIER_RESULT,
      NAME type STRING,
      CLASSIFIER_ID type STRING,
      CLASSES type STANDARD TABLE OF T_CLASS_RESULT WITH NON-UNIQUE DEFAULT KEY,
    end of T_CLASSIFIER_RESULT.
  types:
    "!   Information about what might have caused a failure, such as an image that is too
    "!    large. Not returned when there is no error.
    begin of T_ERROR_INFO,
      CODE type INTEGER,
      DESCRIPTION type STRING,
      ERROR_ID type STRING,
    end of T_ERROR_INFO.
  types:
    "!   Results for one image.
    begin of T_CLASSIFIED_IMAGE,
      SOURCE_URL type STRING,
      RESOLVED_URL type STRING,
      IMAGE type STRING,
      ERROR type T_ERROR_INFO,
      CLASSIFIERS type STANDARD TABLE OF T_CLASSIFIER_RESULT WITH NON-UNIQUE DEFAULT KEY,
    end of T_CLASSIFIED_IMAGE.
  types:
    "!   Information about something that went wrong.
    begin of T_WARNING_INFO,
      WARNING_ID type STRING,
      DESCRIPTION type STRING,
    end of T_WARNING_INFO.
  types:
    "!   Results for all images.
    begin of T_CLASSIFIED_IMAGES,
      CUSTOM_CLASSES type INTEGER,
      IMAGES_PROCESSED type INTEGER,
      IMAGES type STANDARD TABLE OF T_CLASSIFIED_IMAGE WITH NON-UNIQUE DEFAULT KEY,
      WARNINGS type STANDARD TABLE OF T_WARNING_INFO WITH NON-UNIQUE DEFAULT KEY,
    end of T_CLASSIFIED_IMAGES.
  types:
    "!   Knowledge graph of the property. For example, `/fruit/pome/apple/eating
    "!    apple/Granny Smith`. Included only if identified.
      T_TYPE_HIERARCHY type String.
  types:
    "!   A category within a classifier.
    begin of T_CLASS,
      CLASS type STRING,
    end of T_CLASS.
  types:
    "!   Empty object.
      T_EMPTY type JSONOBJECT.
  types:
    "!   Error information.
    begin of T_ERROR_RESPONSE,
      CODE type INTEGER,
      ERROR type STRING,
    end of T_ERROR_RESPONSE.
  types:
    "!
    begin of T_INLINE_OBJECT1,
      NAME type STRING,
      POSITIVE_EXAMPLES type FILE,
      NEGATIVE_EXAMPLES type FILE,
    end of T_INLINE_OBJECT1.
  types:
    "!
    begin of T_INLINE_OBJECT,
      IMAGES_FILE type FILE,
      URL type STRING,
      THRESHOLD type FLOAT,
      OWNERS type STANDARD TABLE OF STRING WITH NON-UNIQUE DEFAULT KEY,
      CLASSIFIER_IDS type STANDARD TABLE OF STRING WITH NON-UNIQUE DEFAULT KEY,
    end of T_INLINE_OBJECT.
  types:
    "!
    begin of T_INLINE_OBJECT2,
      POSITIVE_EXAMPLES type FILE,
      NEGATIVE_EXAMPLES type FILE,
    end of T_INLINE_OBJECT2.
  types:
    "!   Information about a classifier.
    begin of T_CLASSIFIER,
      CLASSIFIER_ID type STRING,
      NAME type STRING,
      OWNER type STRING,
      STATUS type STRING,
      CORE_ML_ENABLED type BOOLEAN,
      EXPLANATION type STRING,
      CREATED type DATETIME,
      CLASSES type STANDARD TABLE OF T_CLASS WITH NON-UNIQUE DEFAULT KEY,
      RETRAINED type DATETIME,
      UPDATED type DATETIME,
    end of T_CLASSIFIER.
  types:
    "!   Number of custom classes identified in the images.
      T_CUSTOM_CLASSES_PROCESSED type Integer.
  types:
    "!   Confidence score for the property in the range of 0 to 1. A higher score
    "!    indicates greater likelihood that the class is depicted in the image. The
    "!    default threshold for returning scores from a classifier is 0.5.
      T_CONFIDENCE_SCORE type Float.
  types:
    "!   Relative path of the image file if uploaded directly. Not returned when the
    "!    image is passed by URL.
      T_IMAGE_FILE type String.
  types:
    "!   Error information.
    begin of T_ERROR_HTML,
      ERROR1 type STRING,
    end of T_ERROR_HTML.
  types:
    "!   Source of the image before any redirects. Not returned when the image is
    "!    uploaded.
      T_SOURCE_URL type String.
  types:
    "!   Fully resolved URL of the image after redirects are followed. Not returned when
    "!    the image is uploaded.
      T_RESOLVED_URL type String.
  types:
    "!   A container for the list of classifiers.
    begin of T_CLASSIFIERS,
      CLASSIFIERS type STANDARD TABLE OF T_CLASSIFIER WITH NON-UNIQUE DEFAULT KEY,
    end of T_CLASSIFIERS.

constants:
  begin of C_REQUIRED_FIELDS,
    T_CLASS_RESULT type string value '|CLASS|SCORE|',
    T_CLASSIFIER_RESULT type string value '|NAME|CLASSIFIER_ID|CLASSES|',
    T_ERROR_INFO type string value '|CODE|DESCRIPTION|ERROR_ID|',
    T_CLASSIFIED_IMAGE type string value '|CLASSIFIERS|',
    T_WARNING_INFO type string value '|WARNING_ID|DESCRIPTION|',
    T_CLASSIFIED_IMAGES type string value '|IMAGES|',
    T_CLASS type string value '|CLASS|',
    T_ERROR_RESPONSE type string value '|CODE|ERROR|',
    T_INLINE_OBJECT1 type string value '|NAME|POSITIVE_EXAMPLES|',
    T_INLINE_OBJECT type string value '|',
    T_INLINE_OBJECT2 type string value '|',
    T_CLASSIFIER type string value '|CLASSIFIER_ID|NAME|',
    T_ERROR_HTML type string value '|',
    T_CLASSIFIERS type string value '|CLASSIFIERS|',
    __DUMMY type string value SPACE,
  end of C_REQUIRED_FIELDS .

constants:
  begin of C_ABAPNAME_DICTIONARY,
     WARNING_ID type string value 'warning_id',
     DESCRIPTION type string value 'description',
     CODE type string value 'code',
     ERROR_ID type string value 'error_id',
     CLASSIFIERS type string value 'classifiers',
     CLASSIFIER_ID type string value 'classifier_id',
     NAME type string value 'name',
     OWNER type string value 'owner',
     STATUS type string value 'status',
     CORE_ML_ENABLED type string value 'core_ml_enabled',
     EXPLANATION type string value 'explanation',
     CREATED type string value 'created',
     CLASSES type string value 'classes',
     RETRAINED type string value 'retrained',
     UPDATED type string value 'updated',
     CLASS type string value 'class',
     SOURCE_URL type string value 'source_url',
     RESOLVED_URL type string value 'resolved_url',
     IMAGE type string value 'image',
     ERROR type string value 'error',
     ERROR1 type string value 'Error',
     SCORE type string value 'score',
     TYPE_HIERARCHY type string value 'type_hierarchy',
     CUSTOM_CLASSES type string value 'custom_classes',
     IMAGES_PROCESSED type string value 'images_processed',
     IMAGES type string value 'images',
     WARNINGS type string value 'warnings',
     IMAGES_FILE type string value 'images_file',
     URL type string value 'url',
     THRESHOLD type string value 'threshold',
     OWNERS type string value 'owners',
     CLASSIFIER_IDS type string value 'classifier_ids',
     CLASSIFIERID type string value 'classifierId',
     POSITIVE_EXAMPLES type string value 'positive_examples',
     NEGATIVE_EXAMPLES type string value 'negative_examples',
  end of C_ABAPNAME_DICTIONARY .


  methods GET_APPNAME
    redefinition .
  methods GET_REQUEST_PROP
    redefinition .
  methods GET_SDK_VERSION_DATE
    redefinition .


    "! Classify images.
    "!
    "! @parameter I_images_file |
    "!   An image file (.gif, .jpg, .png, .tif) or .zip file with images. Maximum image
    "!    size is 10 MB. Include no more than 20 images and limit the .zip file to 100
    "!    MB. Encode the image and .zip file names in UTF-8 if they contain non-ASCII
    "!    characters. The service assumes UTF-8 encoding if it encounters non-ASCII
    "!    characters.
    "!
    "!   You can also include an image with the **url** parameter.
    "! @parameter I_images_filename |
    "!   The filename for imagesFile.
    "! @parameter I_images_file_content_type |
    "!   The content type of imagesFile.
    "! @parameter I_url |
    "!   The URL of an image (.gif, .jpg, .png, .tif) to analyze. The minimum recommended
    "!    pixel density is 32X32 pixels, but the service tends to perform better with
    "!    images that are at least 224 x 224 pixels. The maximum image size is 10 MB.
    "!
    "!   You can also include images with the **images_file** parameter.
    "! @parameter I_threshold |
    "!   The minimum score a class must have to be displayed in the response. Set the
    "!    threshold to `0.0` to return all identified classes.
    "! @parameter I_owners |
    "!   The categories of classifiers to apply. The **classifier_ids** parameter
    "!    overrides **owners**, so make sure that **classifier_ids** is empty.
    "!   - Use `IBM` to classify against the `default` general classifier. You get the
    "!    same result if both **classifier_ids** and **owners** parameters are empty.
    "!   - Use `me` to classify against all your custom classifiers. However, for better
    "!    performance use **classifier_ids** to specify the specific custom classifiers
    "!    to apply.
    "!   - Use both `IBM` and `me` to analyze the image against both classifier
    "!    categories.
    "! @parameter I_classifier_ids |
    "!   Which classifiers to apply. Overrides the **owners** parameter. You can specify
    "!    both custom and built-in classifier IDs. The built-in `default` classifier is
    "!    used if both **classifier_ids** and **owners** parameters are empty.
    "!
    "!   The following built-in classifier IDs require no training:
    "!   - `default`: Returns classes from thousands of general tags.
    "!   - `food`: Enhances specificity and accuracy for images of food items.
    "!   - `explicit`: Evaluates whether the image might be pornographic.
    "! @parameter I_Accept_Language |
    "!   The desired language of parts of the response. See the response for details.
    "! @parameter E_RESPONSE |
    "!   Service return value of type T_CLASSIFIED_IMAGES
    "!
  methods CLASSIFY
    importing
      !I_images_file type FILE optional
      !I_images_filename type STRING optional
      !I_images_file_content_type type STRING optional
      !I_url type STRING optional
      !I_threshold type FLOAT optional
      !I_owners type TT_STRING optional
      !I_classifier_ids type TT_STRING optional
      !I_Accept_Language type STRING default 'en'
      !I_contenttype type string default 'multipart/form-data'
      !I_accept      type string default 'application/json'
    exporting
      !E_RESPONSE type T_CLASSIFIED_IMAGES
    raising
      ZCX_IBMC_SERVICE_EXCEPTION .

    "! Create a classifier.
    "!
    "! @parameter I_name |
    "!   The name of the new classifier. Encode special characters in UTF-8.
    "! @parameter I_positive_examples |
    "!   A .zip file of images that depict the visual subject of a class in the new
    "!    classifier. You can include more than one positive example file in a call.
    "!
    "!   Specify the parameter name by appending `_positive_examples` to the class name.
    "!    For example, `goldenretriever_positive_examples` creates the class
    "!    **goldenretriever**.
    "!
    "!   Include at least 10 images in .jpg or .png format. The minimum recommended image
    "!    resolution is 32X32 pixels. The maximum number of images is 10,000 images or
    "!    100 MB per .zip file.
    "!
    "!   Encode special characters in the file name in UTF-8.
    "! @parameter I_negative_examples |
    "!   A .zip file of images that do not depict the visual subject of any of the
    "!    classes of the new classifier. Must contain a minimum of 10 images.
    "!
    "!   Encode special characters in the file name in UTF-8.
    "! @parameter I_negative_examples_filename |
    "!   The filename for negativeExamples.
    "! @parameter E_RESPONSE |
    "!   Service return value of type T_CLASSIFIER
    "!
  methods CREATE_CLASSIFIER
    importing
      !I_name type STRING
      !I_positive_examples type TT_MAP_FILE
      !I_negative_examples type FILE optional
      !I_negative_examples_filename type STRING optional
      !I_positive_examples_CT type STRING default ZIF_IBMC_SERVICE_ARCH~C_MEDIATYPE-ALL
      !I_negative_examples_CT type STRING default ZIF_IBMC_SERVICE_ARCH~C_MEDIATYPE-ALL
      !I_contenttype type string default 'multipart/form-data'
      !I_accept      type string default 'application/json'
    exporting
      !E_RESPONSE type T_CLASSIFIER
    raising
      ZCX_IBMC_SERVICE_EXCEPTION .
    "! Retrieve a list of classifiers.
    "!
    "! @parameter I_verbose |
    "!   Specify `true` to return details about the classifiers. Omit this parameter to
    "!    return a brief list of classifiers.
    "! @parameter E_RESPONSE |
    "!   Service return value of type T_CLASSIFIERS
    "!
  methods LIST_CLASSIFIERS
    importing
      !I_verbose type BOOLEAN optional
      !I_accept      type string default 'application/json'
    exporting
      !E_RESPONSE type T_CLASSIFIERS
    raising
      ZCX_IBMC_SERVICE_EXCEPTION .
    "! Retrieve classifier details.
    "!
    "! @parameter I_classifier_id |
    "!   The ID of the classifier.
    "! @parameter E_RESPONSE |
    "!   Service return value of type T_CLASSIFIER
    "!
  methods GET_CLASSIFIER
    importing
      !I_classifier_id type STRING
      !I_accept      type string default 'application/json'
    exporting
      !E_RESPONSE type T_CLASSIFIER
    raising
      ZCX_IBMC_SERVICE_EXCEPTION .
    "! Update a classifier.
    "!
    "! @parameter I_classifier_id |
    "!   The ID of the classifier.
    "! @parameter I_positive_examples |
    "!   A .zip file of images that depict the visual subject of a class in the
    "!    classifier. The positive examples create or update classes in the classifier.
    "!    You can include more than one positive example file in a call.
    "!
    "!   Specify the parameter name by appending `_positive_examples` to the class name.
    "!    For example, `goldenretriever_positive_examples` creates the class
    "!    `goldenretriever`.
    "!
    "!   Include at least 10 images in .jpg or .png format. The minimum recommended image
    "!    resolution is 32X32 pixels. The maximum number of images is 10,000 images or
    "!    100 MB per .zip file.
    "!
    "!   Encode special characters in the file name in UTF-8.
    "! @parameter I_negative_examples |
    "!   A .zip file of images that do not depict the visual subject of any of the
    "!    classes of the new classifier. Must contain a minimum of 10 images.
    "!
    "!   Encode special characters in the file name in UTF-8.
    "! @parameter I_negative_examples_filename |
    "!   The filename for negativeExamples.
    "! @parameter E_RESPONSE |
    "!   Service return value of type T_CLASSIFIER
    "!
  methods UPDATE_CLASSIFIER
    importing
      !I_classifier_id type STRING
      !I_positive_examples type TT_MAP_FILE optional
      !I_negative_examples type FILE optional
      !I_negative_examples_filename type STRING optional
      !I_positive_examples_CT type STRING default ZIF_IBMC_SERVICE_ARCH~C_MEDIATYPE-ALL
      !I_negative_examples_CT type STRING default ZIF_IBMC_SERVICE_ARCH~C_MEDIATYPE-ALL
      !I_contenttype type string default 'multipart/form-data'
      !I_accept      type string default 'application/json'
    exporting
      !E_RESPONSE type T_CLASSIFIER
    raising
      ZCX_IBMC_SERVICE_EXCEPTION .
    "! Delete a classifier.
    "!
    "! @parameter I_classifier_id |
    "!   The ID of the classifier.
    "!
  methods DELETE_CLASSIFIER
    importing
      !I_classifier_id type STRING
      !I_accept      type string default 'application/json'
    raising
      ZCX_IBMC_SERVICE_EXCEPTION .

    "! Retrieve a Core ML model of a classifier.
    "!
    "! @parameter I_classifier_id |
    "!   The ID of the classifier.
    "! @parameter E_RESPONSE |
    "!   Service return value of type FILE
    "!
  methods GET_CORE_ML_MODEL
    importing
      !I_classifier_id type STRING
      !I_accept      type string default 'application/octet-stream'
    exporting
      !E_RESPONSE type FILE
    raising
      ZCX_IBMC_SERVICE_EXCEPTION .

    "! Delete labeled data.
    "!
    "! @parameter I_customer_id |
    "!   The customer ID for which all data is to be deleted.
    "!
  methods DELETE_USER_DATA
    importing
      !I_customer_id type STRING
      !I_accept      type string default 'application/json'
    raising
      ZCX_IBMC_SERVICE_EXCEPTION .


protected section.

private section.

  methods SET_DEFAULT_QUERY_PARAMETERS
    changing
      !C_URL type TS_URL .

ENDCLASS.

class ZCL_IBMC_VISUAL_RECOGNITION_V3 IMPLEMENTATION.

* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_IBMC_VISUAL_RECOGNITION_V3->GET_APPNAME
* +-------------------------------------------------------------------------------------------------+
* | [<-()] E_APPNAME                      TYPE        STRING
* +--------------------------------------------------------------------------------------</SIGNATURE>
  method GET_APPNAME.

    e_appname = 'Visual Recognition'.

  endmethod.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Protected Method ZCL_IBMC_VISUAL_RECOGNITION_V3->GET_REQUEST_PROP
* +-------------------------------------------------------------------------------------------------+
* | [--->] I_AUTH_METHOD                  TYPE        STRING (default =C_DEFAULT)
* | [<-()] E_REQUEST_PROP                 TYPE        TS_REQUEST_PROP
* +--------------------------------------------------------------------------------------</SIGNATURE>
method GET_REQUEST_PROP.

  data:
    lv_auth_method type string  ##NEEDED.

  e_request_prop = super->get_request_prop( ).

  lv_auth_method = i_auth_method.
  if lv_auth_method eq c_default.
    lv_auth_method = 'IAM'.
  endif.
  if lv_auth_method is initial.
    e_request_prop-auth_basic      = c_boolean_false.
    e_request_prop-auth_oauth      = c_boolean_false.
    e_request_prop-auth_apikey     = c_boolean_false.
  elseif lv_auth_method eq 'IAM'.
    e_request_prop-auth_name       = 'IAM'.
    e_request_prop-auth_type       = 'apiKey'.
    e_request_prop-auth_headername = 'Authorization'.
    e_request_prop-auth_header     = c_boolean_true.
  else.
  endif.

  e_request_prop-url-protocol    = 'http'.
  e_request_prop-url-host        = 'localhost'.
  e_request_prop-url-path_base   = '/visual-recognition/api'.

endmethod.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_IBMC_VISUAL_RECOGNITION_V3->GET_SDK_VERSION_DATE
* +-------------------------------------------------------------------------------------------------+
* | [<-()] E_SDK_VERSION_DATE             TYPE        STRING
* +--------------------------------------------------------------------------------------</SIGNATURE>
  method get_sdk_version_date.

    e_sdk_version_date = '20191002122854'.

  endmethod.



* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_IBMC_VISUAL_RECOGNITION_V3->CLASSIFY
* +-------------------------------------------------------------------------------------------------+
* | [--->] I_images_file        TYPE FILE(optional)
* | [--->] I_images_filename        TYPE STRING(optional)
* | [--->] I_images_file_content_type        TYPE STRING(optional)
* | [--->] I_url        TYPE STRING(optional)
* | [--->] I_threshold        TYPE FLOAT(optional)
* | [--->] I_owners        TYPE TT_STRING(optional)
* | [--->] I_classifier_ids        TYPE TT_STRING(optional)
* | [--->] I_Accept_Language        TYPE STRING (default ='en')
* | [--->] I_contenttype       TYPE string (default ='multipart/form-data')
* | [--->] I_accept            TYPE string (default ='application/json')
* | [<---] E_RESPONSE                    TYPE        T_CLASSIFIED_IMAGES
* | [!CX!] ZCX_IBMC_SERVICE_EXCEPTION
* +--------------------------------------------------------------------------------------</SIGNATURE>
method CLASSIFY.

    data:
      ls_request_prop type ts_request_prop,
      lv_separator(1) type c  ##NEEDED,
      lv_sep(1)       type c  ##NEEDED,
      lo_response     type to_rest_response,
      lv_json         type string  ##NEEDED.

    ls_request_prop-url-path = '/v3/classify'.

    " standard headers
    ls_request_prop-header_content_type = I_contenttype.
    ls_request_prop-header_accept = I_accept.
    set_default_query_parameters(
      changing
        c_url =  ls_request_prop-url ).



    " process header parameters
    data:
      lv_headerparam type string  ##NEEDED.

    if i_Accept_Language is supplied.
    lv_headerparam = I_Accept_Language.
    add_header_parameter(
      exporting
        i_parameter  = 'Accept-Language'
        i_value      = lv_headerparam
      changing
        c_headers    = ls_request_prop-headers )  ##NO_TEXT.
    endif.


    " process form parameters
    data:
      ls_form_part     type ts_form_part,
      lt_form_part     type tt_form_part,
      lv_formdata      type string value is initial ##NEEDED,
      lv_value         type string ##NEEDED,
      lv_index(3)      type n value '000' ##NEEDED,
      lv_keypattern    type string ##NEEDED,
      lv_base_name     type string ##NEEDED,
      lv_extension     type string ##NEEDED.


    if not i_url is initial.
      clear ls_form_part.
      ls_form_part-content_type = ZIF_IBMC_SERVICE_ARCH~C_MEDIATYPE-TEXT_PLAIN.
      ls_form_part-content_disposition = 'form-data; name="url"'  ##NO_TEXT.
      lv_formdata = i_url.
      ls_form_part-cdata = lv_formdata.
      append ls_form_part to lt_form_part.
    endif.

    if not i_threshold is initial.
      clear ls_form_part.
      ls_form_part-content_type = ZIF_IBMC_SERVICE_ARCH~C_MEDIATYPE-TEXT_PLAIN.
      ls_form_part-content_disposition = 'form-data; name="threshold"'  ##NO_TEXT.
      lv_formdata = i_threshold.
      ls_form_part-cdata = lv_formdata.
      append ls_form_part to lt_form_part.
    endif.

    if not i_owners is initial.
      clear ls_form_part.
      ls_form_part-content_type = ZIF_IBMC_SERVICE_ARCH~C_MEDIATYPE-TEXT_PLAIN.
      ls_form_part-content_disposition = 'form-data; name="owners"'  ##NO_TEXT.
      field-symbols:
        <l_owners> like line of i_owners.
      loop at i_owners assigning <l_owners>.
*        ls_form_part-cdata = <l_owners>.
*        append ls_form_part to lt_form_part.
        if ls_form_part-cdata is initial.
        ls_form_part-cdata = <l_owners>.
        else.
          ls_form_part-cdata = ls_form_part-cdata && `,` && <l_owners>.
        endif.
      endloop.
      append ls_form_part to lt_form_part.
    endif.

    if not i_classifier_ids is initial.
      clear ls_form_part.
      ls_form_part-content_type = ZIF_IBMC_SERVICE_ARCH~C_MEDIATYPE-TEXT_PLAIN.
      ls_form_part-content_disposition = 'form-data; name="classifier_ids"'  ##NO_TEXT.
      field-symbols:
        <l_classifier_ids> like line of i_classifier_ids.
      loop at i_classifier_ids assigning <l_classifier_ids>.
*        ls_form_part-cdata = <l_classifier_ids>.
*        append ls_form_part to lt_form_part.
        if ls_form_part-cdata is initial.
        ls_form_part-cdata = <l_classifier_ids>.
        else.
          ls_form_part-cdata = ls_form_part-cdata && `,` && <l_classifier_ids>.
        endif.

      endloop.
            append ls_form_part to lt_form_part.

    endif.



    if not i_images_file is initial.
      if not I_images_filename is initial.
        lv_value = `form-data; name="images_file"; filename="` && I_images_filename && `"`  ##NO_TEXT.
      else.
      lv_extension = get_file_extension( I_images_file_content_type ).
      lv_value = `form-data; name="images_file"; filename="file` && lv_index && `.` && lv_extension && `"`  ##NO_TEXT.
      endif.
      lv_index = lv_index + 1.
      clear ls_form_part.
      ls_form_part-content_type = I_images_file_content_type.
      ls_form_part-content_disposition = lv_value.
      ls_form_part-xdata = i_images_file.
      append ls_form_part to lt_form_part.
    endif.


    " execute HTTP POST request
    lo_response = HTTP_POST_MULTIPART( i_request_prop = ls_request_prop it_form_part = lt_form_part ).




    " retrieve JSON data
    lv_json = get_response_string( lo_response ).
    parse_json(
      exporting
        i_json       = lv_json
        i_dictionary = c_abapname_dictionary
      changing
        c_abap       = e_response ).

endmethod.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_IBMC_VISUAL_RECOGNITION_V3->CREATE_CLASSIFIER
* +-------------------------------------------------------------------------------------------------+
* | [--->] I_name        TYPE STRING
* | [--->] I_positive_examples        TYPE TT_MAP_FILE
* | [--->] I_negative_examples        TYPE FILE(optional)
* | [--->] I_negative_examples_filename        TYPE STRING(optional)
* | [--->] I_positive_examples_CT     TYPE STRING (default = ZIF_IBMC_SERVICE_ARCH~C_MEDIATYPE-all)
* | [--->] I_negative_examples_CT     TYPE STRING (default = ZIF_IBMC_SERVICE_ARCH~C_MEDIATYPE-all)
* | [--->] I_contenttype       TYPE string (default ='multipart/form-data')
* | [--->] I_accept            TYPE string (default ='application/json')
* | [<---] E_RESPONSE                    TYPE        T_CLASSIFIER
* | [!CX!] ZCX_IBMC_SERVICE_EXCEPTION
* +--------------------------------------------------------------------------------------</SIGNATURE>
method CREATE_CLASSIFIER.

    data:
      ls_request_prop type ts_request_prop,
      lv_separator(1) type c  ##NEEDED,
      lv_sep(1)       type c  ##NEEDED,
      lo_response     type to_rest_response,
      lv_json         type string  ##NEEDED.

    ls_request_prop-url-path = '/v3/classifiers'.

    " standard headers
    ls_request_prop-header_content_type = I_contenttype.
    ls_request_prop-header_accept = I_accept.
    set_default_query_parameters(
      changing
        c_url =  ls_request_prop-url ).





    " process form parameters
    data:
      ls_form_part     type ts_form_part,
      lt_form_part     type tt_form_part,
      lv_formdata      type string value is initial ##NEEDED,
      lv_value         type string ##NEEDED,
      lv_index(3)      type n value '000' ##NEEDED,
      lv_keypattern    type string ##NEEDED,
      lv_base_name     type string ##NEEDED,
      lv_extension     type string ##NEEDED.


    if not i_name is initial.
      clear ls_form_part.
      ls_form_part-content_type = ZIF_IBMC_SERVICE_ARCH~C_MEDIATYPE-TEXT_PLAIN.
      ls_form_part-content_disposition = 'form-data; name="name"'  ##NO_TEXT.
      lv_formdata = i_name.
      ls_form_part-cdata = lv_formdata.
      append ls_form_part to lt_form_part.
    endif.



    if not i_positive_examples is initial.
      lv_extension = get_file_extension( I_positive_examples_CT ).
      field-symbols:
        <lv_map_positive_examples> type line of TT_MAP_FILE.
      find regex '(\{.*\})' in '{{classname}}_positive_examples' submatches lv_keypattern.
      loop at i_positive_examples assigning <lv_map_positive_examples>.
        lv_base_name = '{{classname}}_positive_examples'.
        replace lv_keypattern in lv_base_name with <lv_map_positive_examples>-key.
        lv_value = `form-data; name="` && lv_base_name && `"; filename="file` && lv_index && `.` && lv_extension && `"`  ##NO_TEXT.
        lv_index = lv_index + 1.
        clear ls_form_part.
        ls_form_part-content_type = I_positive_examples_CT.
        ls_form_part-content_disposition = lv_value.
        ls_form_part-xdata = <lv_map_positive_examples>-data.
        append ls_form_part to lt_form_part.
      endloop.
    endif.

    if not i_negative_examples is initial.
      if not I_negative_examples_filename is initial.
        lv_value = `form-data; name="negative_examples"; filename="` && I_negative_examples_filename && `"`  ##NO_TEXT.
      else.
      lv_extension = get_file_extension( I_negative_examples_CT ).
      lv_value = `form-data; name="negative_examples"; filename="file` && lv_index && `.` && lv_extension && `"`  ##NO_TEXT.
      endif.
      lv_index = lv_index + 1.
      clear ls_form_part.
      ls_form_part-content_type = I_negative_examples_CT.
      ls_form_part-content_disposition = lv_value.
      ls_form_part-xdata = i_negative_examples.
      append ls_form_part to lt_form_part.
    endif.


    " execute HTTP POST request
    lo_response = HTTP_POST_MULTIPART( i_request_prop = ls_request_prop it_form_part = lt_form_part ).




    " retrieve JSON data
    lv_json = get_response_string( lo_response ).
    parse_json(
      exporting
        i_json       = lv_json
        i_dictionary = c_abapname_dictionary
      changing
        c_abap       = e_response ).

endmethod.

* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_IBMC_VISUAL_RECOGNITION_V3->LIST_CLASSIFIERS
* +-------------------------------------------------------------------------------------------------+
* | [--->] I_verbose        TYPE BOOLEAN(optional)
* | [--->] I_accept            TYPE string (default ='application/json')
* | [<---] E_RESPONSE                    TYPE        T_CLASSIFIERS
* | [!CX!] ZCX_IBMC_SERVICE_EXCEPTION
* +--------------------------------------------------------------------------------------</SIGNATURE>
method LIST_CLASSIFIERS.

    data:
      ls_request_prop type ts_request_prop,
      lv_separator(1) type c  ##NEEDED,
      lv_sep(1)       type c  ##NEEDED,
      lo_response     type to_rest_response,
      lv_json         type string  ##NEEDED.

    ls_request_prop-url-path = '/v3/classifiers'.

    " standard headers
    ls_request_prop-header_accept = I_accept.
    set_default_query_parameters(
      changing
        c_url =  ls_request_prop-url ).

    " process query parameters
    data:
      lv_queryparam type string.

    if i_verbose is supplied.
    lv_queryparam = i_verbose.
    add_query_parameter(
      exporting
        i_parameter  = `verbose`
        i_value      = lv_queryparam
        i_is_boolean = c_boolean_true
      changing
        c_url        = ls_request_prop-url )  ##NO_TEXT.
    endif.






    " execute HTTP GET request
    lo_response = HTTP_GET( i_request_prop = ls_request_prop ).


    " retrieve JSON data
    lv_json = get_response_string( lo_response ).
    parse_json(
      exporting
        i_json       = lv_json
        i_dictionary = c_abapname_dictionary
      changing
        c_abap       = e_response ).

endmethod.

* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_IBMC_VISUAL_RECOGNITION_V3->GET_CLASSIFIER
* +-------------------------------------------------------------------------------------------------+
* | [--->] I_classifier_id        TYPE STRING
* | [--->] I_accept            TYPE string (default ='application/json')
* | [<---] E_RESPONSE                    TYPE        T_CLASSIFIER
* | [!CX!] ZCX_IBMC_SERVICE_EXCEPTION
* +--------------------------------------------------------------------------------------</SIGNATURE>
method GET_CLASSIFIER.

    data:
      ls_request_prop type ts_request_prop,
      lv_separator(1) type c  ##NEEDED,
      lv_sep(1)       type c  ##NEEDED,
      lo_response     type to_rest_response,
      lv_json         type string  ##NEEDED.

    ls_request_prop-url-path = '/v3/classifiers/{classifier_id}'.
    replace all occurrences of `{classifier_id}` in ls_request_prop-url-path with i_classifier_id ignoring case.

    " standard headers
    ls_request_prop-header_accept = I_accept.
    set_default_query_parameters(
      changing
        c_url =  ls_request_prop-url ).








    " execute HTTP GET request
    lo_response = HTTP_GET( i_request_prop = ls_request_prop ).


    " retrieve JSON data
    lv_json = get_response_string( lo_response ).
    parse_json(
      exporting
        i_json       = lv_json
        i_dictionary = c_abapname_dictionary
      changing
        c_abap       = e_response ).

endmethod.

* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_IBMC_VISUAL_RECOGNITION_V3->UPDATE_CLASSIFIER
* +-------------------------------------------------------------------------------------------------+
* | [--->] I_classifier_id        TYPE STRING
* | [--->] I_positive_examples        TYPE TT_MAP_FILE(optional)
* | [--->] I_negative_examples        TYPE FILE(optional)
* | [--->] I_negative_examples_filename        TYPE STRING(optional)
* | [--->] I_positive_examples_CT     TYPE STRING (default = ZIF_IBMC_SERVICE_ARCH~C_MEDIATYPE-all)
* | [--->] I_negative_examples_CT     TYPE STRING (default = ZIF_IBMC_SERVICE_ARCH~C_MEDIATYPE-all)
* | [--->] I_contenttype       TYPE string (default ='multipart/form-data')
* | [--->] I_accept            TYPE string (default ='application/json')
* | [<---] E_RESPONSE                    TYPE        T_CLASSIFIER
* | [!CX!] ZCX_IBMC_SERVICE_EXCEPTION
* +--------------------------------------------------------------------------------------</SIGNATURE>
method UPDATE_CLASSIFIER.

    data:
      ls_request_prop type ts_request_prop,
      lv_separator(1) type c  ##NEEDED,
      lv_sep(1)       type c  ##NEEDED,
      lo_response     type to_rest_response,
      lv_json         type string  ##NEEDED.

    ls_request_prop-url-path = '/v3/classifiers/{classifier_id}'.
    replace all occurrences of `{classifier_id}` in ls_request_prop-url-path with i_classifier_id ignoring case.

    " standard headers
    ls_request_prop-header_content_type = I_contenttype.
    ls_request_prop-header_accept = I_accept.
    set_default_query_parameters(
      changing
        c_url =  ls_request_prop-url ).





    " process form parameters
    data:
      ls_form_part     type ts_form_part,
      lt_form_part     type tt_form_part,
      lv_formdata      type string value is initial ##NEEDED,
      lv_value         type string ##NEEDED,
      lv_index(3)      type n value '000' ##NEEDED,
      lv_keypattern    type string ##NEEDED,
      lv_base_name     type string ##NEEDED,
      lv_extension     type string ##NEEDED.




    if not i_positive_examples is initial.
      lv_extension = get_file_extension( I_positive_examples_CT ).
      field-symbols:
        <lv_map_positive_examples> type line of TT_MAP_FILE.
      find regex '(\{.*\})' in '{{classname}}_positive_examples' submatches lv_keypattern.
      loop at i_positive_examples assigning <lv_map_positive_examples>.
        lv_base_name = '{{classname}}_positive_examples'.
        replace lv_keypattern in lv_base_name with <lv_map_positive_examples>-key.
        lv_value = `form-data; name="` && lv_base_name && `"; filename="file` && lv_index && `.` && lv_extension && `"`  ##NO_TEXT.
        lv_index = lv_index + 1.
        clear ls_form_part.
        ls_form_part-content_type = I_positive_examples_CT.
        ls_form_part-content_disposition = lv_value.
        ls_form_part-xdata = <lv_map_positive_examples>-data.
        append ls_form_part to lt_form_part.
      endloop.
    endif.

    if not i_negative_examples is initial.
      if not I_negative_examples_filename is initial.
        lv_value = `form-data; name="negative_examples"; filename="` && I_negative_examples_filename && `"`  ##NO_TEXT.
      else.
      lv_extension = get_file_extension( I_negative_examples_CT ).
      lv_value = `form-data; name="negative_examples"; filename="file` && lv_index && `.` && lv_extension && `"`  ##NO_TEXT.
      endif.
      lv_index = lv_index + 1.
      clear ls_form_part.
      ls_form_part-content_type = I_negative_examples_CT.
      ls_form_part-content_disposition = lv_value.
      ls_form_part-xdata = i_negative_examples.
      append ls_form_part to lt_form_part.
    endif.


    " execute HTTP POST request
    lo_response = HTTP_POST_MULTIPART( i_request_prop = ls_request_prop it_form_part = lt_form_part ).




    " retrieve JSON data
    lv_json = get_response_string( lo_response ).
    parse_json(
      exporting
        i_json       = lv_json
        i_dictionary = c_abapname_dictionary
      changing
        c_abap       = e_response ).

endmethod.

* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_IBMC_VISUAL_RECOGNITION_V3->DELETE_CLASSIFIER
* +-------------------------------------------------------------------------------------------------+
* | [--->] I_classifier_id        TYPE STRING
* | [--->] I_accept            TYPE string (default ='application/json')
* | [!CX!] ZCX_IBMC_SERVICE_EXCEPTION
* +--------------------------------------------------------------------------------------</SIGNATURE>
method DELETE_CLASSIFIER.

    data:
      ls_request_prop type ts_request_prop,
      lv_separator(1) type c  ##NEEDED,
      lv_sep(1)       type c  ##NEEDED,
      lo_response     type to_rest_response,
      lv_json         type string  ##NEEDED.

    ls_request_prop-url-path = '/v3/classifiers/{classifier_id}'.
    replace all occurrences of `{classifier_id}` in ls_request_prop-url-path with i_classifier_id ignoring case.

    " standard headers
    ls_request_prop-header_accept = I_accept.
    set_default_query_parameters(
      changing
        c_url =  ls_request_prop-url ).








    " execute HTTP DELETE request
    lo_response = HTTP_DELETE( i_request_prop = ls_request_prop ).



endmethod.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_IBMC_VISUAL_RECOGNITION_V3->GET_CORE_ML_MODEL
* +-------------------------------------------------------------------------------------------------+
* | [--->] I_classifier_id        TYPE STRING
* | [--->] I_accept            TYPE string (default ='application/octet-stream')
* | [<---] E_RESPONSE                    TYPE        FILE
* | [!CX!] ZCX_IBMC_SERVICE_EXCEPTION
* +--------------------------------------------------------------------------------------</SIGNATURE>
method GET_CORE_ML_MODEL.

    data:
      ls_request_prop type ts_request_prop,
      lv_separator(1) type c  ##NEEDED,
      lv_sep(1)       type c  ##NEEDED,
      lo_response     type to_rest_response,
      lv_json         type string  ##NEEDED.

    ls_request_prop-url-path = '/v3/classifiers/{classifier_id}/core_ml_model'.
    replace all occurrences of `{classifier_id}` in ls_request_prop-url-path with i_classifier_id ignoring case.

    " standard headers
    ls_request_prop-header_accept = I_accept.
    set_default_query_parameters(
      changing
        c_url =  ls_request_prop-url ).








    " execute HTTP GET request
    lo_response = HTTP_GET( i_request_prop = ls_request_prop ).


    " retrieve file data
    e_response = get_response_binary( lo_response ).

endmethod.


* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Public Method ZCL_IBMC_VISUAL_RECOGNITION_V3->DELETE_USER_DATA
* +-------------------------------------------------------------------------------------------------+
* | [--->] I_customer_id        TYPE STRING
* | [--->] I_accept            TYPE string (default ='application/json')
* | [!CX!] ZCX_IBMC_SERVICE_EXCEPTION
* +--------------------------------------------------------------------------------------</SIGNATURE>
method DELETE_USER_DATA.

    data:
      ls_request_prop type ts_request_prop,
      lv_separator(1) type c  ##NEEDED,
      lv_sep(1)       type c  ##NEEDED,
      lo_response     type to_rest_response,
      lv_json         type string  ##NEEDED.

    ls_request_prop-url-path = '/v3/user_data'.

    " standard headers
    ls_request_prop-header_accept = I_accept.
    set_default_query_parameters(
      changing
        c_url =  ls_request_prop-url ).

    " process query parameters
    data:
      lv_queryparam type string.

    lv_queryparam = escape( val = i_customer_id format = cl_abap_format=>e_uri_full ).
    add_query_parameter(
      exporting
        i_parameter  = `customer_id`
        i_value      = lv_queryparam
      changing
        c_url        = ls_request_prop-url )  ##NO_TEXT.






    " execute HTTP DELETE request
    lo_response = HTTP_DELETE( i_request_prop = ls_request_prop ).



endmethod.




* <SIGNATURE>---------------------------------------------------------------------------------------+
* | Instance Private Method ZCL_IBMC_VISUAL_RECOGNITION_V3->SET_DEFAULT_QUERY_PARAMETERS
* +-------------------------------------------------------------------------------------------------+
* | [<-->] C_URL                          TYPE        TS_URL
* +--------------------------------------------------------------------------------------</SIGNATURE>
  method set_default_query_parameters.
    if not p_version is initial.
      add_query_parameter(
        exporting
          i_parameter = `version`
          i_value     = p_version
        changing
          c_url       = c_url ).
    endif.
  endmethod.

ENDCLASS.