package ru.kokorin.astream.valueobject {
import mx.collections.IList;

[AStreamAlias("AliasMetaVO")]
public class MetaVO {
    [AStreamOmitField]
    public var omit:Object;

    [AStreamOrder(10)]
    [AStreamAlias("AliasName")]
    public var name:String;

    [AStreamAsAttribute]
    public var attribute:int;

    [AStreamOrder(20)]
    [AStreamImplicit("listItem", itemType="String")]
    public var list:IList;

    [AStreamOrder(25)]
    [ArrayElementType("String")]
    [AStreamImplicit("list2Item")]
    public var list2:IList;

    [AStreamOrder(30)]
    [AStreamImplicit("vectorItem")]
    public var vector:Vector.<String>;

    [AStreamConverter("ru.kokorin.astream.converter.SomeConverter", params="someParam")]
    public var some:Object;
}
}