package ro.ciacob.desktop.ui {
	
	public final class BlueprintKeys {
		
		public function BlueprintKeys() {}
		
		// Blueprint fields
		public static const TYPE : String = 'endPointType';
		public static const SOURCE : String = 'endPointSource';
		public static const NAME : String = 'endPointName';
		public static const LABEL : String = 'endPointLabel';
		public static const DEFAULT : String = 'endPointDefault';
		
		// Additional (optional) accessor metadata
		public static const INDEX : String = 'Index';
		public static const DESCRIPTION:String = 'Description';
		public static const MAXIMUM : String = 'Maximum';
		public static const MINIMUM : String = 'Minimum';
		
		// Custom components related
		public static const CUSTOM_COMPONENT : String = 'CustomComponent';
		public static const CLASS_FQN : String = 'classFqn';
		public static const HIDE_LABEL : String = 'hideLabel';
		public static const DATAPROVIDER_NAME : String = 'dataproviderName';
		public static const BINDING_SOURCE : String = 'bindingSource';
		public static const BINDING_TARGET : String = 'bindingTarget';
		public static const CHANGE_EVENT_NAME : String = 'changeEventName';
		
		// Events and Binding related
		public static const BOUND_EVENT : String = 'boundEvent';
		public static const BOUND_FUNCTION : String = 'boundFunction';
		public static const BOUND_COMPONENT : String = 'boundComponent'; 
		public static const BOUND_CHANGE_WATCHER : String = 'boundChangeWatcher';
		
		// Helpers for simple Object originators
		public static const UI_GENERATOR_CONFIG : String = 'uiGeneratorConfig';
	}
}