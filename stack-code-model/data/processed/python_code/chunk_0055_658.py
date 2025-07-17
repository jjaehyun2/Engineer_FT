
class resolumeCom.parameters.Parameter {

	public var name:String;
	public var type:Number;
	private var events:Object;
	
	public function Parameter() {
		events = new Object();
		AsBroadcaster.initialize(events);
	}
	
	public function parameterChanged() {
		events.broadcastMessage("parameterChanged", this);
	}
	
	public function addParameterListener(listener:Object)
	{
		events.addListener( listener );
	}

	public function getName() : String {
		return this.name;
	}
	
	public function getType() : Number {
		return this.type;
	}

	public function getXmlRep(): String
	{
		return "";		
	}
	
}