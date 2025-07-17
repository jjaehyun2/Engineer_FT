package org.ro.core.event {
public class ObjectObserver implements ILogEventObserver {
    
    var objectUrl:String;
    
    public function ObjectObserver(baseUrl:String) {
        this.objectUrl = baseUrl;
    }
    
    public function update(le:LogEntry):void {
        //check if all required data has arrived and open tab
        // minimum requirement: - Layout
        
        //TODO how can be determined, which observer should be assigned to LE?
        // where should this take place? I ResponseHandler? In LE?
    }
}
}