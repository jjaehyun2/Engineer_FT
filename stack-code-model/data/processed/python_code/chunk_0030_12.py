package com.wordnik.client.model {

[XmlRootNode(name="User")]
public class User {
    [XmlElement(name="id")]
    public var id:Number = 0.0;

    [XmlElement(name="firstName")]
    public var firstName:String = null;

    [XmlElement(name="username")]
    public var username:String = null;

    [XmlElement(name="lastName")]
    public var lastName:String = null;

    [XmlElement(name="email")]
    public var email:String = null;

    [XmlElement(name="password")]
    public var password:String = null;

    [XmlElement(name="phone")]
    public var phone:String = null;

    /* User Status */
    [XmlElement(name="userStatus")]
    public var userStatus:Number = 0.0;

    public function toString():String {
        var str:String = "User: ";
        str += " (id: " + id + ")";
        str += " (firstName: " + firstName + ")";
        str += " (username: " + username + ")";
        str += " (lastName: " + lastName + ")";
        str += " (email: " + email + ")";
        str += " (password: " + password + ")";
        str += " (phone: " + phone + ")";
        str += " (userStatus: " + userStatus + ")";
        return str;
    }


}
}