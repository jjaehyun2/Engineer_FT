package spendr.models {
  import org.restfulx.collections.ModelsCollection;
  
  import org.restfulx.models.RxModel;
  
  [Resource(name="users")]
  [Bindable]
  public class User extends RxModel {
    public static const LABEL:String = "login";

    public var name:String = "";

    public var email:String = "";

    public var login:String = "";

    public var cryptedPassword:String = "";

    public var salt:String = "";

    public var rememberToken:String = "";

    [DateTime]
    public var rememberTokenExpiresAt:Date = new Date;

    public var avatarFileName:String = "";

    public var avatarContentType:String = "";

    public var avatarFileSize:int = 0;

    [DateTime]
    public var avatarUpdateAt:Date = new Date;

    [HasMany]
    public var expenditures:ModelsCollection;
    
    [HasMany]
    public var categories:ModelsCollection;
    
    public function User() {
      super(LABEL);
    }
  }
}