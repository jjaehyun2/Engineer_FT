//
// Flump - Copyright 2013 Flump Authors

package flump.export {

import aspire.util.Arrays;
import aspire.util.Log;

import flash.desktop.NativeApplication;
import flash.display.Loader;
import flash.display.LoaderInfo;
import flash.display.NativeMenuItem;
import flash.events.Event;
import flash.events.InvokeEvent;
import flash.filesystem.File;
import flash.media.SoundMixer;
import flash.media.SoundTransform;
import flash.net.FileFilter;

import flump.Util;
import flump.xfl.XflLibrary;

public class FlumpApp
{
    public static const NA :NativeApplication = NativeApplication.nativeApplication;

    public static function get app () :FlumpApp {
        return _app;
    }

    public function FlumpApp () {
        if (_app != null) {
            throw new Error("FlumpApp is a singleton");
        }
        _app = this;
    }

    public function get loaderInfo () :LoaderInfo { return _loaderInfo; }

    public function run (loaderInfo :LoaderInfo) :void {
        _loaderInfo = loaderInfo;
        // Disable sound completely. A SWF that plays sound on its stage will be
        // noisy as soon as we load it.
        SoundMixer.soundTransform = new SoundTransform(0);

        // Setup our global menu if we support it
        setupGlobalMenus();

        Log.setLevel("", Log.INFO);

        var launched :Boolean = false;
        NA.addEventListener(InvokeEvent.INVOKE, function (event :InvokeEvent) :void {
            if (event.arguments.length > 1 && event.arguments[0] == "--export") {
                var headless :AutomaticExporter = new AutomaticExporter(new File(event.arguments[1]));
                headless.complete.connectNotify(function (complete :Boolean) :void {
                    if (!complete) return;

                    // Even on Mac, running from the command line spawns a new instance of the app,
                    // so we can safely assume it's OK to explicitly shut down here (as the command
                    // line script expects us to).
                    NA.exit();
                });
                return;
            }

            if (event.arguments.length > 0) {
                // A project file has been double-clicked. Open it.
                openProject(new File(event.arguments[0]));
            }

            if (!launched) {
                launched = true;
                if (FlumpSettings.projectWindowSettings.length > 0) {
                    // The app has been launched directly. Open the previously-opened projects.
                    for each (var pws :ProjectWindowSettings in FlumpSettings.projectWindowSettings) {
                        var file :File = new File(pws.configFilePath);
                        if (file.exists) {
                            var project :ProjectController = openProject(file);
                            project.win.nativeWindow.x = pws.windowX;
                            project.win.nativeWindow.y = pws.windowY;
                        }
                    }
                }
            }

            // If no projects are open, create a new one.
            if (_projects.length == 0) {
                newProject();
            }
        });

        // When we quit, save the list of currently-open projects
        NA.addEventListener(Event.EXITING, function (..._) :void {
            var projectWindowSettings :Array = [];
            for each (var project :ProjectController in _projects) {
                if (project.configFile != null) {
                    projectWindowSettings.push(ProjectWindowSettings.fromProject(project));
                }
            }

            FlumpSettings.projectWindowSettings = projectWindowSettings;
        });
    }

    public function showPreviewWindow (project :ProjectConf, lib :XflLibrary) :void {
        if (_previewController == null) {
            _previewController = new PreviewController();
        }
        _previewController.show(project, lib);
    }

    public function newProject () :ProjectController {
        return openProject(null);
    }

    public function openProject (configFile :File) :ProjectController {
        // This project may already be open.
        if (configFile != null) {
            for each (var ctrl :ProjectController in _projects) {
                if (ctrl.configFile != null && ctrl.configFile.nativePath == configFile.nativePath) {
                    ctrl.win.activate();
                    return ctrl;
                }
            }
        }

        var controller :ProjectController = new ProjectController(configFile);
        controller.win.addEventListener(Event.CLOSE, Util.callbackOnce(closeProject, controller));
        _projects.push(controller);

        return controller;
    }

    public function showOpenProjectDialog () :void {
        var file :File = new File();
        file.addEventListener(Event.SELECT, function (..._) :void {
            FlumpApp.app.openProject(file);
        });
        file.browseForOpen("Open Flump Project", [
            new FileFilter("Flump project (*.flump)", "*.flump") ]);
    }

    protected function closeProject (controller :ProjectController) :void {
        Arrays.removeFirst(_projects, controller);
        // NativeApplication.autoExit is not working for us. On Windows and Linux, we exit
        // when all project windows are closed.
        if (!NativeApplication.supportsMenu && _projects.length == 0) {
            NA.exit();
        }
    }

    protected function getActiveProject () :ProjectController {
        for each (var project :ProjectController in _projects) {
            if (NA.activeWindow == project.win.nativeWindow) {
                return project;
            }
        }

        return null;
    }

    protected function setupGlobalMenus () :void {
        if (!NativeApplication.supportsMenu) {
            return;
        }
        // Grab the existing menu on macs. Use an index to get it as it's not going to be
        // 'File' in all languages
        var fileMenuItem :NativeMenuItem = NA.menu.getItemAt(1);
        // Add a separator before the existing close command
        fileMenuItem.submenu.addItemAt(new NativeMenuItem("Sep", /*separator=*/true), 0);

        // Add save and save as by index to work with the existing items on Mac
        // Mac menus have an existing "Close" item, so everything we add should go ahead of that
        var newMenuItem :NativeMenuItem = fileMenuItem.submenu.addItemAt(new NativeMenuItem("New Project"), 0);
        newMenuItem.keyEquivalent = "n";
        newMenuItem.addEventListener(Event.SELECT, function (..._) :void {
            newProject();
        });

        var openMenuItem :NativeMenuItem =
            fileMenuItem.submenu.addItemAt(new NativeMenuItem("Open Project..."), 1);
        openMenuItem.keyEquivalent = "o";
        openMenuItem.addEventListener(Event.SELECT, function (..._) :void {
            showOpenProjectDialog();
        });
        fileMenuItem.submenu.addItemAt(new NativeMenuItem("Sep", /*separator=*/true), 2);

        const saveMenuItem :NativeMenuItem =
            fileMenuItem.submenu.addItemAt(new NativeMenuItem("Save Project"), 3);
        saveMenuItem.keyEquivalent = "s";
        saveMenuItem.addEventListener(Event.SELECT, function (..._) :void {
            var project :ProjectController = getActiveProject();
            if (project != null) {
                project.save();
            }
        });

        const saveAsMenuItem :NativeMenuItem =
            fileMenuItem.submenu.addItemAt(new NativeMenuItem("Save Project As..."), 4);
        saveAsMenuItem.keyEquivalent = "S";
        saveAsMenuItem.addEventListener(Event.SELECT, function (..._) :void {
            var project :ProjectController = getActiveProject();
            if (project != null) {
                project.saveAs();
            }
        });
    }

    protected var _loaderInfo :LoaderInfo;
    protected var _projects :Array = [];
    protected var _previewController :PreviewController;

    protected static var _app :FlumpApp;
}
}