// written by Rich Path, University of Wisconsin - Madison
// latest version 1.3 - 2/6/12
// adds answer key markup for long answer questions
// v 1.1 corrected T/F question weight value; adds IMG & TXT item types; different message display format; auto update check
// v 1.2 added recognition of question & answer feedback, question hints, and regular expressions used in answers; removal of extra line breaks at beginning and end of text
// v 1.2.1: match questions - extra choice import feature corrected; fixes bug of incorrect unique weights (%) for specific answers in SA question types
stop();
import flash.events.*;
import flash.filesystem.*;
import flash.system.Capabilities;
import flash.desktop.Updater;
import com.greensock.*;
import fl.data.DataProvider; 
import fl.events.ComponentEvent;
//import air.update.ApplicationUpdaterUI;
//import air.update.events.UpdateEvent;
//import air.update.events.DownloadErrorEvent;
//var appUpdater:ApplicationUpdaterUI = new ApplicationUpdaterUI();
var correctAnsCnt:uint;
var partialAnsCnt:uint;
var correctAnsValue:Number;
var partialAnsValue:Number;
var questionPointValue:uint;
var questionDifficulty:uint;
var advanceAmount:uint;
var questionImage:String;
var questionImageCaption:String;
var arrayLocation:uint;
var ansTrue:uint;
var ansFalse:uint;
var textArray:Array;
var questionType:String;
var nonMultiQuestion:Boolean;
var tempQuestion:String;
var fullQuestion:String;
var hintText:String;
var feedbackText:String;
var answerKeyText:String;
var initialText:String;
var choiceFeedback:String;
var trueFeedback:String;
var falseFeedback:String;
var answerWeight:String;
var answerArray:Array;
var feedbackArray:Array;
var matchArray:Array;
var choiceArray:Array;
var orderArray:Array;
var activeArrayLine:String;
var outputCSV:Array;
var questionOffset:uint;
var answerOffset:uint;
var matchDivide:uint;
var matchEnd:uint;
var i:uint;
var currentFile:File;
var stream:FileStream = new FileStream();
var defaultDirectory:File;
var savedText:savedMessage;
var partCorrectArray:Array = [0,20,25,33.33,40,50,60,66.67,75,80,100];
var alerttext:TextField;
var txtInputString:String;
var textLength:uint;
var infoWindow:helpScreen;
pointVal.value=1;
diffVal.value=1;

init();

function init():void {
	/*setApplicationVersion();
	appUpdater = new ApplicationUpdaterUI();
	appUpdater.updateURL = "https://academictech.doit.wisc.edu/files/QITool-update-descriptor.xml";
	appUpdater.isCheckForUpdateVisible = false;
	appUpdater.addEventListener(ErrorEvent.ERROR, onError);
	appUpdater.addEventListener(UpdateEvent.INITIALIZED, checkForUpdate);
	appUpdater.initialize();*/
	removeEnum.label="";
	partCorrectValue.dataProvider = new DataProvider(partCorrectArray); 
	buttonConvert.addEventListener(MouseEvent.CLICK, convertText);
	buttonClear.addEventListener(MouseEvent.CLICK, clearText);
	btnInfo.addEventListener(MouseEvent.CLICK, showInfo);
}

function convertText(e:MouseEvent):void {

	buttonConvert.removeEventListener(MouseEvent.CLICK, convertText);
	if (txtInput.text=="") {
		showAlertText("The main text box is empty - there is nothing to convert!");
	} else {
	defaultDirectory = File.documentsDirectory;
	txtInputString = txtInput.text;
	txtInputString = txtInputString.replace(/\r\n/g, "\n");
	txtInputString = txtInputString.replace(/\r/g, "\n");
	textLength = txtInputString.length;
	// delete any extra line breaks at beginning and end of text
	while (txtInputString.charAt(0)=="\n") {
		txtInputString = txtInputString.substring(1);
	}
	while (txtInputString.charAt(textLength-1)=="\n" && txtInputString.charAt(textLength-2)=="\n") {
		txtInputString = txtInputString.slice(0,textLength-1);
		textLength = txtInputString.length;
	}
	textArray=txtInputString.split("\n");
	arrayLocation=0;
	outputCSV = new Array();
	evalQuestion();
	}
}

function evalQuestion():void {

	questionType="";
	nonMultiQuestion=false;
	correctAnsCnt=0;
	partialAnsCnt=0;
	questionPointValue=pointVal.value;

	questionDifficulty=diffVal.value;
	questionImage="";
	questionImageCaption="";
	hintText="";
	feedbackText="";
	answerKeyText="";
	initialText="";
	trueFeedback="";
	falseFeedback="";
	answerArray = new Array();
	feedbackArray = new Array();
	matchArray = new Array();
	choiceArray = new Array();
	orderArray = new Array();

	if (textArray[arrayLocation].length<2) {
		arrayLocation++;
		if (arrayLocation < (textArray.length-1)) {
			evalQuestion();
		} else {
			allDone();
		}
	}
	
	activeArrayLine=textArray[arrayLocation];
		
	if (activeArrayLine.substr(0,2)=="SA" || activeArrayLine.substr(0,2)=="sa") {
		questionType="SA";
		nonMultiQuestion=true;
		questionOffset=3;
		getQuestionText();
	} else if (activeArrayLine.substr(0,4)=="text" || activeArrayLine.substr(0,4)=="TEXT" || activeArrayLine.substr(0,4)=="Text") {
		questionType="TXT";
		nonMultiQuestion=true;
		questionOffset=5;
		getQuestionText();
	} else if (activeArrayLine.substr(0,5)=="image" || activeArrayLine.substr(0,5)=="IMAGE" || activeArrayLine.substr(0,5)=="Image") {
		questionType="IMG";
		nonMultiQuestion=true;
		questionOffset=6;
		getQuestionText();
	} else if (activeArrayLine.substr(0,5)=="match" || activeArrayLine.substr(0,5)=="MATCH" || activeArrayLine.substr(0,5)=="Match") {
		questionType="M";
		nonMultiQuestion=true;
		questionOffset=6;
		getQuestionText();
	} else if (activeArrayLine.substr(0,5)=="order" || activeArrayLine.substr(0,5)=="ORDER" || activeArrayLine.substr(0,5)=="Order") {
		questionType="O";
		nonMultiQuestion=true;
		questionOffset=6;
		getQuestionText();
	} else {
		questionOffset=0;
		getQuestionText();
	}
}

function getQuestionText():void {
	var separate:int=0;
	var period:int = activeArrayLine.indexOf("."); // find where the first period exists
	var paren:int = activeArrayLine.indexOf(")"); // find where the first right paranthesis exists
	var sp:int = activeArrayLine.indexOf(" ",questionOffset); // find where the first space exists after the previously set questionOffset value
	if (period==-1 || period>(3+questionOffset)) {separate=paren;}
	else if (paren==-1 || paren>(3+questionOffset)) {separate=period;}
	if (questionType=="IMG") {
		questionImageCaption=activeArrayLine.substring(questionOffset);
		arrayLocation++;
		evalAnswers();
		}
	if (separate==(sp-1)) //&& sp<(5+questionOffset)
		{
		tempQuestion=activeArrayLine.substring(sp+1);
		fullQuestion=activeArrayLine;
		arrayLocation++;
		evalAnswers();
		} else {
		tempQuestion=activeArrayLine.substring(questionOffset);
		fullQuestion=activeArrayLine;
		arrayLocation++;
		evalAnswers();
	}
}

function evalAnswers():void {
	activeArrayLine=new String(textArray[arrayLocation]);
	//check for end of input text array
	if (arrayLocation == (textArray.length)) {
		addQuestion();
	} else //check for end of answer list
	if (activeArrayLine.length==0) { 
		addQuestion();
	} else //set question point value if present
	if (activeArrayLine.charAt(0)=="=") {
		questionPointValue=uint(activeArrayLine.substring(1));
		arrayLocation++;
		evalAnswers();
	} else //set question difficulty value if present
	if (activeArrayLine.charAt(0)=="!") {
		questionDifficulty=uint(activeArrayLine.substring(1));
		arrayLocation++;
		evalAnswers();
	} else //check for hint text
	if (activeArrayLine.charAt(0)=="?") {
		hintText=activeArrayLine.substring(1);
		arrayLocation++;
		evalAnswers();
	} else //check for main question feedback
	if (activeArrayLine.charAt(0)=="@" && activeArrayLine.charAt(1)!="@") {
		feedbackText=activeArrayLine.substring(1);
		arrayLocation++;
		evalAnswers();	
	} else //check for answer key markup
	if (activeArrayLine.charAt(0)=="&") {
		answerKeyText=activeArrayLine.substring(1);
		arrayLocation++;
		evalAnswers();
	} else //check for initial text markup
	if (activeArrayLine.charAt(0)=="|") {
		initialText=activeArrayLine.substring(1);
		arrayLocation++;
		evalAnswers();
	} else //check for image file reference
	if (activeArrayLine.substr(0,4)=="img=" || activeArrayLine.substr(0,4)=="IMG=" || activeArrayLine.substr(0,4)=="Img=") {
		questionImage=activeArrayLine.substring(4);
		arrayLocation++;
		evalAnswers();
	} else //check for short answer
	if (questionType=="SA") {
		answerArray.push(activeArrayLine);
		arrayLocation++;
		evalAnswers();
	} else //check for matching answers
	if (questionType=="M") {
		matchDivide=0;
		answerOffset=0;
		if ((activeArrayLine.charAt(1)=="." || activeArrayLine.charAt(1)==")") && activeArrayLine.charAt(2)==" ") {
			activeArrayLine = activeArrayLine.substring(3);
		}
		matchDivide=(activeArrayLine.indexOf("/"));
		if (activeArrayLine.charAt(0)=="/" ) {
			choiceArray.push(activeArrayLine.substring(matchDivide+2));
			matchArray.push("");
			answerArray.push(activeArrayLine);
			arrayLocation++;
			evalAnswers();
			} else {
			matchEnd=matchDivide-1;
			choiceArray.push(activeArrayLine.substring(matchDivide+2));
			matchArray.push(activeArrayLine.substring(0,matchEnd));
			answerArray.push(activeArrayLine);
			arrayLocation++;
			evalAnswers();
			}
	} else //check for Ordering answers
	if (questionType=="O") {
		answerOffset=0;
		if (removeEnum.selected==true) {
			if ((activeArrayLine.charAt(1)=="." || activeArrayLine.charAt(1)==")") && activeArrayLine.charAt(2)==" ") {
			answerOffset=3;
			}
		}
		orderArray.push(activeArrayLine.substring(answerOffset));
		answerArray.push(activeArrayLine.substring(answerOffset));
		arrayLocation++;
		evalAnswers();
	} else	//check for True/False answer
	if (activeArrayLine=="T"||activeArrayLine=="t"||activeArrayLine=="True"||activeArrayLine=="true"||activeArrayLine=="TRUE") {
		questionType="TF";
		nonMultiQuestion=true;
		ansTrue=100;
		ansFalse=0;
		arrayLocation++;
		evalAnswers();
	} else	
	if (activeArrayLine=="F"||activeArrayLine=="f"||activeArrayLine=="False"||activeArrayLine=="false"||activeArrayLine=="FALSE") {
		questionType="TF";
		nonMultiQuestion=true;
		ansTrue=0;
		ansFalse=100;
		arrayLocation++;
		evalAnswers();
	} else  // check for True response feedback
	if (activeArrayLine.substr(0,3)=="T@@" && questionType=="TF") {
		trueFeedback=activeArrayLine.substring(3);
		arrayLocation++;
		evalAnswers();
	} else  // check for False response feedback
	if (activeArrayLine.substr(0,3)=="F@@" && questionType=="TF") {
		falseFeedback=activeArrayLine.substring(3);
		arrayLocation++;
		evalAnswers();
	} else  //check for correct answer mark
	if (activeArrayLine.charAt(0)=="*") {
		++correctAnsCnt;
		answerArray.push(activeArrayLine);
		arrayLocation++;
		evalAnswers();
	} else //check for partially correct answer mark
	if (activeArrayLine.charAt(0)=="+") {
		++partialAnsCnt;
		answerArray.push(activeArrayLine);
		arrayLocation++;
		evalAnswers();
	} else //check for regular answer line
	if ((activeArrayLine.charAt(1)=="." || activeArrayLine.charAt(1)==")") && (activeArrayLine.charAt(2)==" ")) {
		answerArray.push(activeArrayLine);
		arrayLocation++;
		evalAnswers();
	} else {
		answerArray.push(activeArrayLine);
		arrayLocation++;
		evalAnswers();
	}
}

function addQuestion():void {
	
	//set questionType if Long Answer question
	if ((answerArray.length<1) && (questionType!="TF") && (questionType!="TXT") && (questionType!="IMG")) {
		questionType="LA";
		nonMultiQuestion=true;
	}
	//set questionType if Multiselect question
	if (correctAnsCnt>=2) {
		questionType="MS";
	}
	//set questionType if Multiple Choice question
	if (correctAnsCnt==1) {
		questionType="MC";
	}
	//error check MC/MS question
	if (!nonMultiQuestion && correctAnsCnt==0) {
		showAlertText("A correct answer is not identified for the following question:\n\n"+fullQuestion+"\n\nPlease correct this in the main text box.");
		return;
	} 
	answerOffset=0;
	outputCSV.push( ['NewQuestion',questionType,'','','']);
	outputCSV.push( ['Title','','','','']);
	if (questionType!="IMG") {
		outputCSV.push( ['QuestionText',String.fromCharCode(34)+tempQuestion+String.fromCharCode(34),'','','']);
	}
	if (questionType!="TXT" && questionType!="IMG") {
		outputCSV.push( ['Points',questionPointValue,'','','']);
		outputCSV.push( ['Difficulty',questionDifficulty,'','','']);
	}
	if (questionImage!="") {
		outputCSV.push( ['Image',questionImage,'','','']);
	}
	
	//add data for Long Answer question
	if (questionType=="LA" && initialText!="") {
		outputCSV.push( ['InitialText',String.fromCharCode(34)+initialText+String.fromCharCode(34),'','','']);
	}
	if (questionType=="LA" && answerKeyText!="") {
		outputCSV.push( ['AnswerKey',String.fromCharCode(34)+answerKeyText+String.fromCharCode(34),'','','']);
	}

	//format data for Image question
	if (questionType=="IMG") {
		if (questionImageCaption=="") {
			showAlertText("The following image information entry requires an image caption:\n\n"+fullQuestion+"\n\nPlease correct this in the main text box.\nUse the imgcap= tag directly in front of text to include the caption.");
			return;
		} else {
		outputCSV.push( ['Caption',String.fromCharCode(34)+questionImageCaption+String.fromCharCode(34),'','','']);
		}
	}

	//format data for True/False question
	if (questionType=="TF") {
		outputCSV.push( ['TRUE',ansTrue,String.fromCharCode(34)+trueFeedback+String.fromCharCode(34),'','']);
		outputCSV.push( ['FALSE',ansFalse,String.fromCharCode(34)+falseFeedback+String.fromCharCode(34),'','']);
	}

	//format data for Multiple Choice question
	if (questionType=="MC") {
			for (i=0; i<=(answerArray.length-1); i++) {
			correctAnsValue=0;
			answerOffset=0;
			choiceFeedback="";
			if (answerArray[i].charAt(0)=="*") {
				correctAnsValue=100;
				answerOffset+=1;
			}
			if (answerArray[i].charAt(0)=="+") {
				correctAnsValue=partCorrectValue.selectedItem.data;
				answerOffset+=1;
			}
			if (removeEnum.selected==true) {
				if ((answerArray[i].charAt(answerOffset+1)=="." || answerArray[i].charAt(answerOffset+1)==")") && (answerArray[i].charAt(answerOffset+2)==" ")) {
					answerOffset+=3;
				}
			}
			if (i+1<=(answerArray.length-1) && answerArray[i+1].substr(0,2)=="@@") {
				outputCSV.push( ['Option',correctAnsValue.toFixed(2),String.fromCharCode(34)+answerArray[i].substring(answerOffset)+String.fromCharCode(34),'',String.fromCharCode(34)+answerArray[i+1].substring(2)+String.fromCharCode(34)]);
				i++;
			} 
			else {
				outputCSV.push( ['Option',correctAnsValue.toFixed(2),String.fromCharCode(34)+answerArray[i].substring(answerOffset)+String.fromCharCode(34),'','']);
			}
		}
	}

	//format data for Multiselect question
	if (questionType=="MS") {
		for (i=0; i<=(answerArray.length-1); i++) {
			correctAnsValue=0;
			answerOffset=0;
			if (answerArray[i].charAt(0)=="*") {
				correctAnsValue=1;
				answerOffset+=1;
			}
			if (removeEnum.selected==true) {
				if ((answerArray[i].charAt(answerOffset+1)=="." || answerArray[i].charAt(answerOffset+1)==")") && (answerArray[i].charAt(answerOffset+2)==" ")) {
					answerOffset+=3;
				}
			}
			if (i+1<=(answerArray.length-1) && answerArray[i+1].substr(0,2)=="@@") {
				outputCSV.push( ['Option',correctAnsValue.toFixed(0),String.fromCharCode(34)+answerArray[i].substring(answerOffset)+String.fromCharCode(34),'',String.fromCharCode(34)+answerArray[i+1].substring(2)+String.fromCharCode(34)]);
				i++;
			} else {
				outputCSV.push( ['Option',correctAnsValue.toFixed(0),String.fromCharCode(34)+answerArray[i].substring(answerOffset)+String.fromCharCode(34),'','']);
			}
		}
	}
	
	//format data for Matching question
	if (questionType=="M") {
		outputCSV.push( ['Scoring','EquallyWeighted','','',''] );
		for (i=0; i<=(matchArray.length-1); i++) {
			outputCSV.push( ['Choice',i+1,choiceArray[i],'',''] );
			if (matchArray[i]!="") {
				outputCSV.push( ['Match',i+1,matchArray[i],'',''] );
			}
		}
	}
	//format data for Ordering question
	if (questionType=="O") {
		outputCSV.push( ['Scoring','RightMinusWrong','','',''] );
		for (i=0; i<=(orderArray.length-1); i++) {
			if (i+1<=(orderArray.length-1) && orderArray[i+1].substr(0,2)=="@@") {
				outputCSV.push( ['Item',orderArray[i],'NOT HTML',String.fromCharCode(34)+orderArray[i+1].substring(2)+String.fromCharCode(34)] );
				i++; 
			} else {
				outputCSV.push( ['Item',orderArray[i],'NOT HTML',''] );
			}
		}
	}
	//format data for Short Answer question
	if (questionType=="SA") {
		outputCSV.push( ['InputBox','3','40','','']);
		for (i=0; i<=(answerArray.length-1); i++) {
			advanceAmount=0;
			correctAnsValue=100;
			// check one line ahead for unique weight value of answer
			if (i+1<=(answerArray.length-1) && answerArray[i+1].charAt(0)=="%") {
				correctAnsValue=Number(answerArray[i+1].substring(1)); // sets the unique weight value for answer
				advanceAmount=1; // skips line beginning with "%"
			}
			if (answerArray[i].substr(0,2)=="E$" || answerArray[i].substr(0,2)=="e$") {
				answerOffset=2;
				outputCSV.push( ['Answer',correctAnsValue.toFixed(2),String.fromCharCode(34)+answerArray[i].substring(answerOffset)+String.fromCharCode(34),'regexp','']);
			} else {
				answerOffset=0;
				outputCSV.push( ['Answer',correctAnsValue.toFixed(2),String.fromCharCode(34)+answerArray[i].substring(answerOffset)+String.fromCharCode(34),'','']);
			}
			i+=advanceAmount;
		}
	}
	//add question hint and feedback if present
	if (questionType!="TXT" && questionType!="IMG") {
		if (hintText!="") {
			outputCSV.push( ['Hint',String.fromCharCode(34)+hintText+String.fromCharCode(34),'','','']);
		}
		if (feedbackText!="") {
			outputCSV.push( ['Feedback',String.fromCharCode(34)+feedbackText+String.fromCharCode(34),'','','']);
		}
	}
	
	arrayLocation++;

	if (arrayLocation >= (textArray.length-1)) {
		allDone();
	} else {
		evalQuestion();
	}
}

function allDone():void {
	var fileChooser:File;
	if (currentFile)
		{
			fileChooser = currentFile;
		}
		else
		{
			fileChooser = defaultDirectory;
		}
	fileChooser.browseForSave("Save As (note: the CSV extension will be automatically added after you click Save)");
	fileChooser.addEventListener(Event.SELECT, saveAsFileSelected);
	fileChooser.addEventListener(Event.CANCEL, cancelSave);
}

function cancelSave(event:Event):void
{
	currentFile = event.target as File;
	currentFile.removeEventListener(Event.CANCEL, cancelSave);
	currentFile.removeEventListener(Event.SELECT, saveAsFileSelected);
	buttonConvert.addEventListener(MouseEvent.CLICK, convertText);
}

function saveAsFileSelected(event:Event):void 
{
	currentFile = event.target as File;
	if(!currentFile.extension || currentFile.extension != "csv"){
		currentFile.nativePath += ".csv";
	}
	saveFile();
	currentFile.removeEventListener(Event.SELECT, saveAsFileSelected);
	currentFile.removeEventListener(Event.CANCEL, cancelSave);
	buttonConvert.addEventListener(MouseEvent.CLICK, convertText);
}

function removeSavedMessage():void
{
	removeChild(savedText);
}

function saveFile(event:MouseEvent = null):void 
{
	if (stream != null)	
	{
		stream.close();
	}
	stream = new FileStream();
	stream.openAsync(currentFile, FileMode.WRITE);
	stream.addEventListener(IOErrorEvent.IO_ERROR, writeIOErrorHandler);
	stream.addEventListener(Event.CLOSE, displaySavedMessage);
	var str:String = outputCSV.join('\n');
	str = str.replace(/\n/g, File.lineEnding);
	stream.writeUTFBytes(str);
	stream.close();
}

function displaySavedMessage(event:Event):void
{
	savedText = new savedMessage;
	savedText.x=stage.width/2
	savedText.y=stage.height/2
	addChild(savedText);
	TweenLite.to(savedText, 4, {alpha:0, onComplete:removeSavedMessage});
}

function writeIOErrorHandler(event:Event):void 
{
	showAlertText("An error was encountered while trying to save the file. \nPlease check your Save As destination choice.");
}

function clearText(event:MouseEvent):void
{
	txtInput.text="";
}

/*function checkForUpdate(event:UpdateEvent):void
{
	appUpdater.removeEventListener(ErrorEvent.ERROR, onError);
	appUpdater.removeEventListener(UpdateEvent.INITIALIZED, checkForUpdate);
	appUpdater.checkNow();
}

// Find the current version for our Label below
function setApplicationVersion():void
{
	var appXML:XML = NativeApplication.nativeApplication.applicationDescriptor;
	var ns:Namespace = appXML.namespace();
}
	
function onError(event:ErrorEvent):void
{
	appUpdater.removeEventListener(ErrorEvent.ERROR, onError);
	appUpdater.removeEventListener(UpdateEvent.INITIALIZED, checkForUpdate);
	showAlertText("An error occurred while checking for program updates. \nYou might be offline, or the update site is unavailable at this time.\n"+event);
}*/

function showAlertText(t:String):void {
	alerttext = new TextField();
	var newFormat:TextFormat = new TextFormat();
	alerttext.width = 550;
	alerttext.text = t;
	alerttext.x = (stage.width/2)-275;
	alerttext.y = (stage.height/2)-175;
	alerttext.background = true;
	alerttext.backgroundColor = 0xF7F7F7;
	alerttext.border = true;
	alerttext.borderColor = 0xDDDDDD;
    alerttext.wordWrap = true;
	alerttext.selectable = false;
    alerttext.autoSize = TextFieldAutoSize.CENTER;
	newFormat.align = TextFormatAlign.CENTER;
	newFormat.size = 16;
    newFormat.font = "Arial";
	newFormat.bold = true;
	newFormat.italic = true;
	newFormat.color = 0xAA0000;
    alerttext.setTextFormat(newFormat);
	alerttext.appendText("\n\nClick this box to close this alert.");
	addChild(alerttext);
	buttonConvert.removeEventListener(MouseEvent.CLICK, convertText);
	buttonClear.removeEventListener(MouseEvent.CLICK, clearText);
	alerttext.addEventListener(MouseEvent.CLICK, removeAlertText);
}

function removeAlertText(e:MouseEvent):void {
	alerttext.removeEventListener(MouseEvent.CLICK, removeAlertText);
	buttonConvert.addEventListener(MouseEvent.CLICK, convertText);
	buttonClear.addEventListener(MouseEvent.CLICK, clearText);
	removeChild(alerttext);
}

function showInfo(e:MouseEvent):void {
	buttonConvert.removeEventListener(MouseEvent.CLICK, convertText);
	buttonClear.removeEventListener(MouseEvent.CLICK, clearText);
	btnInfo.removeEventListener(MouseEvent.CLICK, showInfo);
	infoWindow = new helpScreen();
	infoWindow.x = 350;
	infoWindow.y = 242;
	addChild(infoWindow);
	infoWindow.closeWindow.addEventListener(MouseEvent.CLICK, removeInfo);
}

function removeInfo(e:MouseEvent):void {
	infoWindow.closeWindow.removeEventListener(MouseEvent.CLICK, removeInfo);
	removeChild(infoWindow);
	buttonConvert.addEventListener(MouseEvent.CLICK, convertText);
	buttonClear.addEventListener(MouseEvent.CLICK, clearText);
	btnInfo.addEventListener(MouseEvent.CLICK, showInfo);	
}