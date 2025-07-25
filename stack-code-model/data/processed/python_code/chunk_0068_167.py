package org.jbei.registry.mediators
{
	import flash.display.DisplayObject;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.net.FileReference;
	import flash.net.URLLoader;
	import flash.net.URLLoaderDataFormat;
	import flash.net.URLRequest;
	import flash.net.URLRequestMethod;
	import flash.net.URLVariables;
	import flash.utils.Dictionary;
	
	import mx.controls.Alert;
	import mx.core.Application;
	import mx.core.IChildList;
	import mx.core.UIComponent;
	import mx.core.mx_internal;
	import mx.managers.PopUpManager;
	import mx.managers.SystemManager;
	
	import org.jbei.lib.data.RestrictionEnzymeGroup;
	import org.jbei.lib.ui.dialogs.ModalDialog;
	import org.jbei.lib.ui.dialogs.ModalDialogEvent;
	import org.jbei.lib.ui.dialogs.SimpleDialog;
	import org.jbei.lib.utils.Logger;
	import org.jbei.lib.utils.LoggerEvent;
	import org.jbei.lib.utils.SystemUtils;
	import org.jbei.registry.ApplicationFacade;
	import org.jbei.registry.Constants;
	import org.jbei.registry.Notifications;
	import org.jbei.registry.models.FeaturedDNASequence;
	import org.jbei.registry.models.VectorEditorProject;
	import org.jbei.registry.view.dialogs.AboutDialogForm;
	import org.jbei.registry.view.dialogs.DSDNADialogForm;
	import org.jbei.registry.view.dialogs.DiversificationDialogForm;
	import org.jbei.registry.view.dialogs.DiversificationInputDialogForm;
	import org.jbei.registry.view.dialogs.FeatureDialogForm;
	import org.jbei.registry.view.dialogs.FullReplacementDialogForm;
	import org.jbei.registry.view.dialogs.FullReplacementInputDialogForm;
	import org.jbei.registry.view.dialogs.GelDigestDialogForm;
	import org.jbei.registry.view.dialogs.GoToDialogForm;
	import org.jbei.registry.view.dialogs.PCRDialogForm;
	import org.jbei.registry.view.dialogs.PreferencesDialogForm;
	import org.jbei.registry.view.dialogs.ProjectPropertiesDialogForm;
	import org.jbei.registry.view.dialogs.PropertiesDialogForm;
	import org.jbei.registry.view.dialogs.RestrictionEnzymeManagerForm;
	import org.jbei.registry.view.dialogs.SelectDialogForm;
	import org.jbei.registry.view.dialogs.mageDialogs.MageParameterDialogMenuForm;
	import org.jbei.registry.view.ui.ApplicationPanel;
	import org.jbei.registry.view.ui.PropertiesDialog;
	import org.puremvc.as3.interfaces.INotification;
	import org.puremvc.as3.patterns.mediator.Mediator;

    /**
     * @author Zinovii Dmytriv
     */
	public class ApplicationMediator extends Mediator
	{
		private const NAME:String = "ApplicationMediator";
		
        private var applicationPanel:ApplicationPanel;
        private var applicationFacade:ApplicationFacade;
        private var importSequenceFileReference:FileReference;
        
		// Constructor
        public function ApplicationMediator(viewComponent:Object=null)
		{
			super(NAME);
            
            Logger.getInstance().addEventListener(LoggerEvent.LOG, onLogMessage);
            
            applicationPanel = viewComponent as ApplicationPanel;
            
            applicationFacade = ApplicationFacade.getInstance();
            
            applicationFacade.registerMediator(new MainMenuMediator(applicationPanel.mainPanel.mainMenu));
            applicationFacade.registerMediator(new MainControlBarMediator(applicationPanel.mainPanel.mainControlBar));
            applicationFacade.registerMediator(new MainContentPanelMediator(applicationPanel.mainPanel.mainContentPanel));
            applicationFacade.registerMediator(new StatusBarMediator(applicationPanel.mainPanel.statusBar));
            applicationFacade.registerMediator(new FindPanelMediator(applicationPanel.mainPanel.findPanel));
			// Registered Mediator
			applicationFacade.registerMediator(new MageBarMediator(applicationPanel.mainPanel.MageBar));
		}
		
		// Public Methods
		public override function listNotificationInterests():Array
		{
			return [
                Notifications.LOCK
                , Notifications.UNLOCK
                , Notifications.SHOW_ACTION_PROGRESSBAR
                , Notifications.HIDE_ACTION_PROGRESSBAR
                , Notifications.APPLICATION_FAILURE
				
                , Notifications.EXPORT_OLIGOS
				, Notifications.DOWNLOAD_MASCPCR
				, Notifications.SHOW_DSDNA_DIALOG
				, Notifications.SHOW_PCR_DIALOG
				, Notifications.SAVE_TO_REGISTRY
                , Notifications.SAVE_PROJECT
                , Notifications.SAVE_PROJECT_AS
                , Notifications.SHOW_PROJECT_PROPERTIES_DIALOG
                , Notifications.IMPORT_SEQUENCE
                , Notifications.DOWNLOAD_SEQUENCE
                , Notifications.SEQUENCE_FILE_GENERATED
                , Notifications.PROJECT_UPDATED
                , Notifications.SEQUENCE_UPDATED
                
                , Notifications.SEQUENCE_PROVIDER_CHANGED
                , Notifications.UNDO
                , Notifications.REDO
                , Notifications.REBASE_SEQUENCE
                
				, Notifications.SHOW_DIVERSIFICATION_INPUT_DIALOG
				, Notifications.DIVERSIFICATION_TABLE_LOADED
				, Notifications.SHOW_FULL_REPLACEMENT_INPUT_DIALOG
				, Notifications.FULL_REPLACEMENT_TABLE_LOADED
				, Notifications.SHOW_PREFERENCES_DIALOG
				, Notifications.SHOW_PROPERTIES_DIALOG
				, Notifications.SHOW_ABOUT_DIALOG
				, Notifications.SHOW_CREATE_NEW_FEATURE_DIALOG
				, Notifications.SHOW_RESTRICTION_ENZYMES_MANAGER_DIALOG
                , Notifications.SHOW_SIMULATE_DIGESTION_DIALOG
				, Notifications.SHOW_GOTO_DIALOG
				, Notifications.SHOW_SELECTION_BY_RANGE_DIALOG
                
                , Notifications.GO_REPORT_BUG
                , Notifications.GO_SUGGEST_FEATURE
			];
		}
		
		public override function handleNotification(notification:INotification):void
		{
			switch(notification.getName()) {
                case Notifications.APPLICATION_FAILURE:
                    var failureMessage:String = notification.getBody() as String;
                    
                    lockApplication(failureMessage);
                    
                    Alert.show(failureMessage, "Application Failure");
                    
                    break;
                case Notifications.ACTION_MESSAGE:
                    logActionMessage(notification.getBody() as String);
                    
                    break;
                case Notifications.LOCK:
                    lockApplication(notification.getBody() as String);
                    
                    break;
                case Notifications.UNLOCK:
                    unlockApplication();
                    
                    break;
                case Notifications.SHOW_ACTION_PROGRESSBAR:
                    showActionProgressBar(notification.getBody() as String);
                    
                    break;
                case Notifications.HIDE_ACTION_PROGRESSBAR:
                    hideActionProgressBar();
                    
                    break;
                case Notifications.SAVE_TO_REGISTRY:
                    saveToRegistry();
                    
                    break;
				case Notifications.EXPORT_OLIGOS:
					exportOligos();
					
					break;				
                case Notifications.DOWNLOAD_SEQUENCE:
                    generateSequence();
                    
                    break;
                case Notifications.SEQUENCE_FILE_GENERATED:
                    downloadSequence(notification.getBody() as String);
                    
                    break;
                case Notifications.SAVE_PROJECT:
                    saveProject();
                    
                    break;
                case Notifications.SAVE_PROJECT_AS:
                    saveAsProject();
                    
                    break;
                case Notifications.SHOW_PROJECT_PROPERTIES_DIALOG:
                    showProjectPropertiesDialog();
                    
                    break;
                case Notifications.PROJECT_UPDATED:
                    updateProject(notification.getBody() as VectorEditorProject);
                    
                    break;
                case Notifications.SEQUENCE_UPDATED:
                    applicationFacade.updateSequence(notification.getBody() as FeaturedDNASequence);
                    
                    break;
                case Notifications.UNDO:
                    applicationFacade.undo();
                    
                    break;
                case Notifications.REDO:
                    applicationFacade.redo();
                    
                    break;
                case Notifications.SEQUENCE_PROVIDER_CHANGED:
                    //applicationFacade.updateBrowserSaveTitleState(false);
                    
                    break;
				case Notifications.GO_REPORT_BUG:
					reportBug();
					
					break;
				case Notifications.GO_SUGGEST_FEATURE:
					suggestFeature();
					
					break;
				case Notifications.SHOW_SELECTION_BY_RANGE_DIALOG:
					showSelectionDialog();
					
					break;
				case Notifications.SHOW_PREFERENCES_DIALOG:
					showPreferencesDialog();
					
					break;
				case Notifications.SHOW_PROPERTIES_DIALOG:
					showPropertiesDialog();
					
					break;
				case Notifications.SHOW_CREATE_NEW_FEATURE_DIALOG:
					showCreateNewFeatureDialog();
					
					break;
				case Notifications.SHOW_RESTRICTION_ENZYMES_MANAGER_DIALOG:
					showRestrictionEnzymesManagerDialog();
					
                    break;
                case Notifications.SHOW_SIMULATE_DIGESTION_DIALOG:
                    showSimulateDigestionDialog();
                    
					break;
				case Notifications.SHOW_DIVERSIFICATION_INPUT_DIALOG:
					loadDiversificationInputDialog();
					
					break;
				case Notifications.DIVERSIFICATION_TABLE_LOADED:
					showDiversificationInputDialog();
					
					break;					
				case Notifications.SHOW_FULL_REPLACEMENT_INPUT_DIALOG:
					loadFullReplacementInputDialog();
					
					break;
				case Notifications.FULL_REPLACEMENT_TABLE_LOADED:
					showFullReplacementInputDialog();
					
					break;
				case Notifications.SHOW_DSDNA_DIALOG:
					showDSDNADialog();
					
					break;	
				case Notifications.SHOW_PCR_DIALOG:
					showPCRDialog();
					
					break;
				case Notifications.SHOW_GOTO_DIALOG:
					showGoToDialog();
					
					break;
				case Notifications.SHOW_ABOUT_DIALOG:
					showAboutDialog();
					
					break;
                case Notifications.IMPORT_SEQUENCE:
                    importSequence();
                    
                    break;
                case Notifications.REBASE_SEQUENCE:
                    rebaseSequence();
                    
                    break;
			}
		}
		
        // Event Handlers
        private function onLogMessage(event:LoggerEvent):void
        {
            applicationPanel.loggerTextArea.text += event.message + "\n";
        }
        
        private function onSelectDialogSubmit(event:ModalDialogEvent):void
        {
            var selectionArray:Array = event.data as Array;
            
            if(selectionArray.length != 2) { return; }
            
            sendNotification(Notifications.SELECTION_CHANGED, selectionArray);
        }
        
        private function onGoToDialogSubmit(event:ModalDialogEvent):void
        {
            sendNotification(Notifications.CARET_POSITION_CHANGED, (event.data as int));
        }
		
		private function onPCRDialogSubmit(event:ModalDialogEvent):void
		{
			var dict:Dictionary = event.data as Dictionary;
			applicationFacade.getMASCPCRPrimers(dict);
		}
		
		private function loadDiversificationInputDialog():void
		{
			applicationFacade.diversificationChartMode = 1;
			applicationFacade.loadDiversificationTable();
		}
		
		private function showDiversificationInputDialog():void
		{
			//applicationFacade.loadDiversificationTable();
			var diversificationInputDialog:ModalDialog = new ModalDialog(DiversificationInputDialogForm,null);
			diversificationInputDialog.title = "Enter number of MAGE cycles";
			diversificationInputDialog.open();
			diversificationInputDialog.addEventListener(ModalDialogEvent.SUBMIT, onDiversificationInputDialogSubmit);
		}
		

		private function onDiversificationInputDialogSubmit(event:ModalDialogEvent):void
		{
					//ApplicationFacade.getInstance().sendNotification(Notifications.SELECTION_CHANGED, new Array(feature.start, feature.end));	
			//var diversityTable:String = applicationFacade.getDiversificationTable();
			//var table:String = event.data as String;
			//applicationFacade.diversificationCycles = event.data as int;
			
			showDiversificationDialog(event.data as int);
			//diversificationDialog.addEventListener(ModalDialogEvent.SUBMIT, onDiversificationDialogSubmit);
		}
		
		public function showDiversificationDialog(cycles:int):void{
			var diversificationDialog:ModalDialog = new ModalDialog(DiversificationDialogForm, cycles);
			diversificationDialog.title = "Population Diversity by MERLIN Cycle";
			//diversificationDialog.mx_internal::ModalDialog.
			diversificationDialog.open();
		}
		
		private function loadFullReplacementInputDialog():void
		{
			applicationFacade.diversificationChartMode = 2;
			applicationFacade.loadDiversificationTable();
		}
		
		private function showFullReplacementInputDialog():void
		{
			var fullReplacementInputDialog:ModalDialog = new ModalDialog(FullReplacementInputDialogForm,null);
			fullReplacementInputDialog.title = "Enter screening parameters";
			fullReplacementInputDialog.open();
			fullReplacementInputDialog.addEventListener(ModalDialogEvent.SUBMIT, onFullReplacementInputDialogSubmit);
		}
		
		private function onFullReplacementInputDialogSubmit(event:ModalDialogEvent):void
		{
			//applicationFacade.diversificationCycles = event.data.cycles as int;
			//applicationFacade.replacementClones = event.data.clones as int;
			showFullReplacementDialog();
		}
		
		private function showFullReplacementDialog():void
		{
			var dialog:ModalDialog = new ModalDialog(FullReplacementDialogForm,null);
			dialog.title = "Probability of isolating a comepletely modified clone";
			dialog.open();
		}
		
		private function onDSDNADialogSubmit(event:ModalDialogEvent):void
		{
			//sendNotification(Notifications.DSDNA_DIALOG_SUBMITTED, event.data);
			var tmp:int = 1;
			var dict:Dictionary = event.data as Dictionary;
			var left:int = dict["left"];
			var right:int = dict["right"];
			var sequence:String = dict["sequence"];
			
			//remove all whitespace from sequence
			var rex:RegExp = /[\s\r\n]+/gim;
			sequence = sequence.replace(rex,'');
			
			applicationFacade.loadDSDNAPrimer(left, right, sequence);			
		}
        		
        private function onRestrictionEnzymeManagerDialogSubmit(event:ModalDialogEvent):void
        {
            sendNotification(Notifications.USER_RESTRICTION_ENZYMES_CHANGED);
        }
        
        private function onCreateProjectPropertiesDialogSubmit(event:ModalDialogEvent):void
        {
            applicationFacade.createProject();
        }
        
        private function onProjectPropertiesDialogSubmit(event:ModalDialogEvent):void
        {
            var showCircular:Boolean = event.data as Boolean;
            if (showCircular) {
                sendNotification(Notifications.SHOW_PIE);
            } else {
                sendNotification(Notifications.SHOW_RAIL);
            }
            
            CONFIG::standalone {
            
                return;
            }
            
            if(applicationFacade.project.uuid != null && applicationFacade.project.uuid != "") {
                applicationFacade.saveProject();
            } else {
                applicationFacade.createProject();
            }
        }
        
        private function onImportSequenceFileReferenceSelect(event:Event):void
        {
            importSequenceFileReference.load();
        }
        
        private function onImportSequenceFileReferenceComplete(event:Event):void
        {
            if(importSequenceFileReference.data == null) {
                showFileImportErrorAlert("Empty file!");
                
                return;
            }
            
            CONFIG::standalone {
                ApplicationFacade.getInstance().importSequence(importSequenceFileReference.data.toString());
            }
            CONFIG::entryEdition {
                ApplicationFacade.getInstance().importSequenceViaServer(importSequenceFileReference.data.toString());
            }

        }
        
        private function onImportSequenceFileReferenceLoadError(event:IOErrorEvent):void
        {
            showFileImportErrorAlert(event.text);
        }
        
		// Private Methods
		private function reportBug():void
		{
			goToUrl(Constants.REPORT_BUG_URL);
		}
		
		private function suggestFeature():void
		{
			goToUrl(Constants.SUGGEST_FEATURE_URL);
		}
		
		private function goToUrl(url:String):void
		{
			SystemUtils.goToUrl(url);
		}
		
		private function showSelectionDialog():void
		{
			var positions:Array = new Array();
			
			if(applicationFacade.selectionStart > 0 && applicationFacade.selectionEnd > 0) {
				positions.push(applicationFacade.selectionStart);
				positions.push(applicationFacade.selectionEnd);
			} else {
				positions.push(0);
				positions.push(10);
			}
			
			var selectDialog:ModalDialog = new ModalDialog(SelectDialogForm, positions);
			selectDialog.title = "Select ...";
			selectDialog.open();
			
			selectDialog.addEventListener(ModalDialogEvent.SUBMIT, onSelectDialogSubmit);
		}
		
		private function showPreferencesDialog():void
		{
			var preferencesDialog:ModalDialog = new ModalDialog(PreferencesDialogForm, null);
			preferencesDialog.title = "Preferences";
			preferencesDialog.open();
		}
		
		private function showPropertiesDialog():void
		{
			var propertiesDialog:PropertiesDialog = new PropertiesDialog(PropertiesDialogForm);
			propertiesDialog.title = "Properties";
			propertiesDialog.open();
		}
		
		private function showCreateNewFeatureDialog():void
		{
			var featureDialog:ModalDialog = new ModalDialog(FeatureDialogForm, null);
			featureDialog.title = "Create New Feature";
			featureDialog.open();
		}
		
		private function showRestrictionEnzymesManagerDialog():void
		{
			var restrictionEnzymeManagerDialog:ModalDialog = new ModalDialog(RestrictionEnzymeManagerForm, new RestrictionEnzymeGroup("tmp"));
			restrictionEnzymeManagerDialog.title = "Restriction Enzyme Manager";
			restrictionEnzymeManagerDialog.open();
            
            restrictionEnzymeManagerDialog.addEventListener(ModalDialogEvent.SUBMIT, onRestrictionEnzymeManagerDialogSubmit);
		}
		
        private function showSimulateDigestionDialog():void
        {
            var gelDigestDialog:SimpleDialog = new SimpleDialog(GelDigestDialogForm);
            gelDigestDialog.title = "Gel Digest";
            gelDigestDialog.open();
        }
			
		//private function getMASCPCRPrimers():void
		//{
		//	applicationFacade.getMASCPCRPrimers();
		//}
		
		private function showGoToDialog():void
		{
			var gotoDialog:ModalDialog = new ModalDialog(GoToDialogForm, applicationFacade.caretPosition);
			gotoDialog.title = "Go To...";
			gotoDialog.open();
			
			gotoDialog.addEventListener(ModalDialogEvent.SUBMIT, onGoToDialogSubmit);
		}
		
		private function showDSDNADialog():void
		{
			var dsdnaDialog:ModalDialog = new ModalDialog(DSDNADialogForm,null);
			dsdnaDialog.title = "Enter a replacement sequence";
			dsdnaDialog.open();
			
			dsdnaDialog.addEventListener(ModalDialogEvent.SUBMIT, onDSDNADialogSubmit);
		}
		
		private function showPCRDialog():void
		{
			var pcrDialog:ModalDialog = new ModalDialog(PCRDialogForm,null);
			pcrDialog.title = "PCR Primer Generation";
			pcrDialog.addEventListener(ModalDialogEvent.SUBMIT, onPCRDialogSubmit);
			pcrDialog.open();
		}
		
		private function showAboutDialog():void
		{
			var aboutDialog:SimpleDialog = new SimpleDialog(AboutDialogForm);
            aboutDialog.title = Constants.APPLICATION_NAME;
			aboutDialog.open();
		}
		
        private function logActionMessage(message:String):void
        {
            Logger.getInstance().info(message);
        }
        
        private function lockApplication(lockMessage:String = ""):void
        {
            applicationPanel.mainPanel.enabled = false;
            
            sendNotification(Notifications.SHOW_ACTION_PROGRESSBAR, lockMessage);
            
            if(lockMessage != null && lockMessage != "") {
                sendNotification(Notifications.ACTION_MESSAGE, lockMessage);
            }
        }
        
        private function unlockApplication():void
        {
            applicationPanel.mainPanel.enabled = true;
            
            sendNotification(Notifications.HIDE_ACTION_PROGRESSBAR);
        }
        
        private function showActionProgressBar(message:String = ""):void
        {
            applicationPanel.actionProgressBar.visible = true;
            applicationPanel.actionProgressBar.label = message;
            applicationPanel.actionProgressBar.x = applicationPanel.width / 2 - applicationPanel.actionProgressBar.width / 2;
            applicationPanel.actionProgressBar.y = applicationPanel.height / 2 - applicationPanel.actionProgressBar.height / 2;
        }
        
        private function hideActionProgressBar():void
        {
            applicationPanel.actionProgressBar.visible = false;
        }
        
        private function saveProject():void
        {
            var project:VectorEditorProject = applicationFacade.project;
            
            if(project.uuid == null || project.uuid == "") { // project not saved
                var createProjectPropertiesDialog:ModalDialog = new ModalDialog(ProjectPropertiesDialogForm, project);
                createProjectPropertiesDialog.title = "Save Project";
                createProjectPropertiesDialog.addEventListener(ModalDialogEvent.SUBMIT, onCreateProjectPropertiesDialogSubmit);
                createProjectPropertiesDialog.open();
            } else { // project was saved before
                applicationFacade.saveProject();
            }
        }
        
        private function saveAsProject():void
        {
            var project:VectorEditorProject = applicationFacade.project;
            
            var createProjectPropertiesDialog:ModalDialog = new ModalDialog(ProjectPropertiesDialogForm, project);
            createProjectPropertiesDialog.title = "Save As ...";
            createProjectPropertiesDialog.addEventListener(ModalDialogEvent.SUBMIT, onCreateProjectPropertiesDialogSubmit);
            createProjectPropertiesDialog.open();
        }
        
        private function showProjectPropertiesDialog():void
        {
            var propertiesDialog:ModalDialog = new ModalDialog(ProjectPropertiesDialogForm, applicationFacade.project);
            propertiesDialog.title = "Properties";
            propertiesDialog.addEventListener(ModalDialogEvent.SUBMIT, onProjectPropertiesDialogSubmit);
            propertiesDialog.open();
        }
        
        private function updateProject(project:VectorEditorProject):void
        {
            applicationFacade.updateProject(project);
        }
        
        private function importSequence():void
        {
            importSequenceFileReference = new FileReference();
            importSequenceFileReference.addEventListener(Event.SELECT, onImportSequenceFileReferenceSelect);
            importSequenceFileReference.addEventListener(Event.COMPLETE, onImportSequenceFileReferenceComplete);
            importSequenceFileReference.addEventListener(IOErrorEvent.IO_ERROR, onImportSequenceFileReferenceLoadError);
            importSequenceFileReference.browse();
        }
        
        private function showFileImportErrorAlert(message:String):void
        {
            Alert.show("Failed to open file!", message);
        }
        
        private function rebaseSequence():void
        {
            if(!applicationFacade.sequenceProvider || !applicationFacade.sequenceProvider.circular || applicationFacade.sequenceProvider.sequence.length == 0 || applicationFacade.caretPosition <= 0) {
                return;
            }
            
            applicationFacade.sequenceProvider.rebaseSequence(applicationFacade.caretPosition);
        }
        
        private function saveToRegistry():void
        {
            applicationFacade.saveSequence();
        }
		
		private function exportOligos():void
		{
			applicationFacade.exportOligos();	
		}
        
        private function generateSequence():void
        {
            CONFIG::standalone {
                applicationFacade.generateSequence();
            }
            CONFIG::entryEdition {
                applicationFacade.generateSequenceOnServer();
			}
		}
		
		private function downloadSequence(content:String):void
		{
			applicationFacade.downloadSequence(content);
		}
		
	}
}