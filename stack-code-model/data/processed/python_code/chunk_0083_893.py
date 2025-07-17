package com.vmware.simplivity.citrixplugin
{
   /**
    * Simple data model for the settings page.
    *
    * See the java equivalent, CitrixData.java, in the citrixplugin-service project.
    * For more complex types see the Actionscript-Java serialization documentation.
    */
    [Bindable]
   [RemoteClass(alias="com.vmware.simplivity.citrixplugin.CitrixData")]
   
   public class CitrixData
   {
      // Note: only public fields can be serialized to Java
      public var citrixKey:String;
      public var customerName:String;
      public var clientId:String;
	  public var resourceLocation:String;
   }
}