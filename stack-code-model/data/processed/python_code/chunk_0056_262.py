package 
{
	/**
	 * Commands
	 * @author Devoron
	 */
	public class Commands 
	{
		private var _commands:Array;
		
		public function Commands() 
		{
			_commands = [];
			_commands.push("-advanced-telemetry");
			_commands.push("-advanced-telemetry-password <string>");
			_commands.push("-compiler.accessible");
			_commands.push("-compiler.actionscript-file-encoding <string>");
			_commands.push("-compiler.allow-source-path-overlap");
			_commands.push("-compiler.as3");
			_commands.push("-compiler.compress");
			_commands.push("-compiler.context-root <context-path>");
			_commands.push("-compiler.debug");
			_commands.push("-compiler.defaults-css-files [filename] [...]");
			_commands.push("-compiler.defaults-css-url <string>");
			_commands.push("-compiler.define <name> <value>");
			_commands.push("-compiler.enable-runtime-design-layers");
			_commands.push("-compiler.es");
			_commands.push("-compiler.external-library-path [path-element] [...]");
			_commands.push("-compiler.fonts.advanced-anti-aliasing");
			_commands.push("-compiler.fonts.languages.language-range <lang> <range>");
			_commands.push("-compiler.fonts.local-font-paths [path-element] [...]");
			_commands.push("-compiler.fonts.local-fonts-snapshot <string>");
			_commands.push("-compiler.fonts.managers [manager-class] [...]");
			_commands.push("-compiler.fonts.max-cached-fonts <string>");
			_commands.push("-compiler.fonts.max-glyphs-per-face <string>");
			_commands.push("-compiler.headless-server");
			_commands.push("-compiler.include-libraries [library] [...]");
			_commands.push("-compiler.inline");
			_commands.push("-compiler.isolate-styles");
			_commands.push("-compiler.keep-all-type-selectors");
			_commands.push("-compiler.keep-as3-metadata [name] [...]");
			_commands.push("-compiler.library-path [path-element] [...]");
			_commands.push("-compiler.locale [locale-element] [...]");
			_commands.push("-compiler.minimum-supported-version <string>");
			_commands.push("-compiler.mobile");
			_commands.push("-compiler.mxml.compatibility-version <version>");
			_commands.push("-compiler.mxml.minimum-supported-version <string>");
			_commands.push("-compiler.namespaces.namespace [uri] [manifest] [...]");
			_commands.push("-compiler.omit-trace-statements");
			_commands.push("-compiler.optimize");
			_commands.push("-compiler.preloader <string>");
			_commands.push("-compiler.remove-dead-code");
			_commands.push("-compiler.report-invalid-styles-as-warnings");
			_commands.push("-compiler.report-missing-required-skin-parts-as-warnings");
			_commands.push("-compiler.services <filename>");
			_commands.push("-compiler.show-actionscript-warnings");
			_commands.push("-compiler.show-binding-warnings");
			_commands.push("-compiler.show-invalid-css-property-warnings");
			_commands.push("-compiler.show-multiple-definition-warnings");
			_commands.push("-compiler.show-shadowed-device-font-warnings");
			_commands.push("-compiler.show-unused-type-selector-warnings");
			_commands.push("-compiler.source-path [path-element] [...]");
			_commands.push("-compiler.strict");
			_commands.push("-compiler.theme [filename] [...]");
			_commands.push("-compiler.verbose-stacktraces");
			_commands.push("-compiler.warn-array-tostring-changes");
			_commands.push("-compiler.warn-assignment-within-conditional");
			_commands.push("-compiler.warn-bad-array-cast");
			_commands.push("-compiler.warn-bad-bool-assignment");
			_commands.push("-compiler.warn-bad-date-cast");
			_commands.push("-compiler.warn-bad-es3-type-method");
			_commands.push("-compiler.warn-bad-es3-type-prop");
			_commands.push("-compiler.warn-bad-nan-comparison");
			_commands.push("-compiler.warn-bad-null-assignment");
			_commands.push("-compiler.warn-bad-null-comparison");
			_commands.push("-compiler.warn-bad-undefined-comparison");
			_commands.push("-compiler.warn-boolean-constructor-with-no-args");
			_commands.push("-compiler.warn-changes-in-resolve");
			_commands.push("-compiler.warn-class-is-sealed");
			_commands.push("-compiler.warn-const-not-initialized");
			_commands.push("-compiler.warn-constructor-returns-value");
			_commands.push("-compiler.warn-deprecated-event-handler-error");
			_commands.push("-compiler.warn-deprecated-function-error");
			_commands.push("-compiler.warn-deprecated-property-error");
			_commands.push("-compiler.warn-duplicate-argument-names");
			_commands.push("-compiler.warn-duplicate-variable-def");
			_commands.push("-compiler.warn-for-var-in-changes");
			_commands.push("-compiler.warn-import-hides-class");
			_commands.push("-compiler.warn-instance-of-changes");
			_commands.push("-compiler.warn-internal-error");
			_commands.push("-compiler.warn-level-not-supported");
			_commands.push("-compiler.warn-missing-namespace-decl");
			_commands.push("-compiler.warn-negative-uint-literal");
			_commands.push("-compiler.warn-no-constructor");
			_commands.push("-compiler.warn-no-explicit-super-call-in-constructor");
			_commands.push("-compiler.warn-no-type-decl");
			_commands.push("-compiler.warn-number-from-string-changes");
			_commands.push("-compiler.warn-scoping-change-in-this");
			_commands.push("-compiler.warn-slow-text-field-addition");
			_commands.push("-compiler.warn-unlikely-function-value");
			_commands.push("-compiler.warn-xml-class-has-changed");
			_commands.push("-debug-password <string>");
			_commands.push("-default-background-color <int>");
			_commands.push("-default-frame-rate <int>");
			_commands.push("-default-script-limits <max-recursion-depth> <max-execution-time>");
			_commands.push("-default-size <width> <height>");
			_commands.push("-dependency-graph <filename>");
			_commands.push("-dump-config <filename>");
			_commands.push("-error-problems [class] [...]");
			_commands.push("-externs [symbol] [...]");
			_commands.push("-frames.frame [label] [classname] [...]");
			_commands.push("-help [keyword] [...]");
			_commands.push("-ignore-problems [class] [...]");
			_commands.push("-include-inheritance-dependencies-only");
			_commands.push("-include-resource-bundles [bundle] [...]");
			_commands.push("-includes [symbol] [...]");
			_commands.push("-link-report <filename>");
			_commands.push("-load-config <filename>");
			_commands.push("-load-externs <filename>");
			_commands.push("-metadata.contributor <name>");
			_commands.push("-metadata.creator <name>");
			_commands.push("-metadata.date <text>");
			_commands.push("-metadata.description <text>");
			_commands.push("-metadata.language <code>");
			_commands.push("-metadata.localized-description <text> <lang>");
			_commands.push("-metadata.localized-title <title> <lang>");
			_commands.push("-metadata.publisher <name>");
			_commands.push("-metadata.title <text>");
			_commands.push("-output <filename>");
			_commands.push("-raw-metadata <text>");
			_commands.push("-remove-unused-rsls");
			_commands.push("-resource-bundle-list <filename>");
			_commands.push("-runtime-shared-libraries [url] [...]");
			_commands.push("-runtime-shared-library-path [path-element] [rsl-url] [policy-file-url] [rsl-url] [policy-file-url]");
			_commands.push("-runtime-shared-library-settings.application-domain [path-element] [application-domain-target] [...]");
			_commands.push("-runtime-shared-library-settings.force-rsls [path-element] [...]");
			_commands.push("-single-thread");
			_commands.push("-size-report <filename>");
			_commands.push("-static-link-runtime-shared-libraries");
			_commands.push("-swf-version <int>");
			_commands.push("-target-player <version>");
			_commands.push("-tools-locale <string>");
			_commands.push("-use-direct-blit");
			_commands.push("-use-gpu");
			_commands.push("-use-network");
			_commands.push("-verify-digests");
			_commands.push("-version");
			_commands.push("-warning-problems [class] [...]");
			_commands.push("-warnings");
		}
		
		public function get commands():Array 
		{
			return _commands;
		}
		
	}

}