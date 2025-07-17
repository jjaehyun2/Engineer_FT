package com.macys.marketing.sema
{
	 import mx.rpc.xml.Schema
	 public class BasePortfolioServiceSchema
	{
		 public var schemas:Array = new Array();
		 public var targetNamespaces:Array = new Array();
		 public function BasePortfolioServiceSchema():void
{		
			 var xsdXML0:XML = <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.xmlsoap.org/wsdl/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://schemas.macys.com/api/ad/v1" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" attributeFormDefault="unqualified" elementFormDefault="unqualified">
    <xsd:import namespace="https://adwords.google.com/api/adwords/v11" schemaLocation="http://192.168.1.27:8081/SEMAServices/services/v1/PortfolioService?xsd=1"/>
</xsd:schema>
;
			 var xsdSchema0:Schema = new Schema(xsdXML0);
			schemas.push(xsdSchema0);
			targetNamespaces.push(new Namespace('','null'));
			 var xsdXML1:XML = <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="https://adwords.google.com/api/adwords/v11" xmlns:ns1="http://schemas.macys.com/api/ad/v1" attributeFormDefault="unqualified" elementFormDefault="unqualified" targetNamespace="https://adwords.google.com/api/adwords/v11">
    <xs:import namespace="http://schemas.macys.com/api/ad/v1" schemaLocation="http://192.168.1.27:8081/SEMAServices/services/v1/PortfolioService?xsd=3"/>
    <xs:element name="fault" nillable="true" type="xs:anyType"/>
</xs:schema>
;
			 var xsdSchema1:Schema = new Schema(xsdXML1);
			schemas.push(xsdSchema1);
			targetNamespaces.push(new Namespace('','https://adwords.google.com/api/adwords/v11'));
			 var xsdXML2:XML = <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:ns1="http://schemas.macys.com/definitions/ad/v1" xmlns:tns="http://schemas.macys.com/api/ad/v1" attributeFormDefault="unqualified" elementFormDefault="unqualified" targetNamespace="http://schemas.macys.com/api/ad/v1">
    <xs:import namespace="http://schemas.macys.com/definitions/ad/v1" schemaLocation="http://192.168.1.27:8081/SEMAServices/services/v1/PortfolioService?xsd=2"/>
    <xs:element name="getAllPortfolios" type="tns:getAllPortfolios"/>
    <xs:element name="getAllPortfoliosResponse" type="tns:getAllPortfoliosResponse"/>
    <xs:element name="getPortfolioList" type="tns:getPortfolioList"/>
    <xs:element name="getPortfolioListResponse" type="tns:getPortfolioListResponse"/>
    <xs:element name="putPortfolios" type="tns:putPortfolios"/>
    <xs:element name="putPortfoliosResponse" type="tns:putPortfoliosResponse"/>
    <xs:complexType name="getPortfolioList">
        <xs:sequence>
            <xs:element maxOccurs="unbounded" minOccurs="0" ref="ns1:PortfolioIds"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="getPortfolioListResponse">
        <xs:sequence>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="return" type="tns:Portfolio"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="Portfolio">
        <xs:sequence>
            <xs:element minOccurs="0" name="Id" type="xs:long"/>
            <xs:element name="PortfolioGroupId" type="xs:long"/>
            <xs:element name="Status" type="tns:SemaStatusType"/>
            <xs:element name="Name" type="xs:string"/>
            <xs:element name="Description" type="xs:string"/>
            <xs:element minOccurs="0" name="State" nillable="true" type="tns:SemaStateType"/>
            <xs:element minOccurs="0" name="CreatedDate" nillable="true" type="xs:dateTime"/>
            <xs:element minOccurs="0" name="ModifiedDate" nillable="true" type="xs:dateTime"/>
            <xs:element minOccurs="0" name="CreatedBy" nillable="true" type="xs:string"/>
            <xs:element minOccurs="0" name="ModifiedBy" nillable="true" type="xs:string"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="ServiceException">
        <xs:sequence>
            <xs:element minOccurs="0" name="exceptionInfo" type="tns:exceptionInfo"/>
            <xs:element minOccurs="0" name="message" type="xs:string"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="exceptionInfo">
        <xs:sequence>
            <xs:element minOccurs="0" name="DefaultExceptionInfoDetail" type="tns:ExceptionInfoDetail"/>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="ExceptionInfoDetail" type="tns:ExceptionInfoDetail"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="ExceptionInfoDetail">
        <xs:sequence>
            <xs:element minOccurs="0" name="Code" type="xs:long"/>
            <xs:element minOccurs="0" name="DisplayMessage" type="xs:string"/>
            <xs:element minOccurs="0" name="Message" type="xs:string"/>
            <xs:element minOccurs="0" name="Trigger" type="xs:string"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="SchemaValidationException">
        <xs:sequence>
            <xs:element minOccurs="0" name="exceptionInfo" type="tns:exceptionInfo"/>
            <xs:element minOccurs="0" name="message" type="xs:string"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="getAllPortfolios">
        <xs:sequence>
            <xs:element minOccurs="0" ref="ns1:PortfolioGroupId"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="getAllPortfoliosResponse">
        <xs:sequence>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="return" type="tns:Portfolio"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="putPortfolios">
        <xs:sequence>
            <xs:element maxOccurs="unbounded" minOccurs="0" ref="ns1:Portfolios"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="putPortfoliosResponse">
        <xs:sequence>
            <xs:element maxOccurs="unbounded" minOccurs="0" name="return" type="tns:Portfolio"/>
        </xs:sequence>
    </xs:complexType>
    <xs:simpleType name="SemaStatusType">
        <xs:restriction base="xs:string">
            <xs:enumeration value="Enabled"/>
            <xs:enumeration value="Paused"/>
            <xs:enumeration value="Deleted"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="SemaStateType">
        <xs:restriction base="xs:string">
            <xs:enumeration value="New"/>
            <xs:enumeration value="Allocated"/>
            <xs:enumeration value="Attached"/>
            <xs:enumeration value="Detached"/>
            <xs:enumeration value="Published"/>
            <xs:enumeration value="Modified"/>
            <xs:enumeration value="Replicated"/>
            <xs:enumeration value="FailedPublish"/>
            <xs:enumeration value="Synchronized"/>
            <xs:enumeration value="Unpublishable"/>
        </xs:restriction>
    </xs:simpleType>
</xs:schema>
;
			 var xsdSchema2:Schema = new Schema(xsdXML2);
			schemas.push(xsdSchema2);
			targetNamespaces.push(new Namespace('','http://schemas.macys.com/api/ad/v1'));
			 var xsdXML3:XML = <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.macys.com/definitions/ad/v1" xmlns:ns1="http://schemas.macys.com/api/ad/v1" attributeFormDefault="unqualified" elementFormDefault="unqualified" targetNamespace="http://schemas.macys.com/definitions/ad/v1">
    <xs:import namespace="http://schemas.macys.com/api/ad/v1" schemaLocation="http://192.168.1.27:8081/SEMAServices/services/v1/PortfolioService?xsd=3"/>
    <xs:element name="ExceptionInfo" type="ns1:exceptionInfo"/>
    <xs:element name="PortfolioGroupId" type="xs:long"/>
    <xs:element name="PortfolioIds" type="xs:long"/>
    <xs:element name="Portfolios" type="ns1:Portfolio"/>
    <xs:element name="portfolioBean" type="ns1:Portfolio"/>
    <xs:element name="userName" nillable="true" type="xs:string"/>
</xs:schema>
;
			 var xsdSchema3:Schema = new Schema(xsdXML3);
			schemas.push(xsdSchema3);
			targetNamespaces.push(new Namespace('','http://schemas.macys.com/definitions/ad/v1'));
			xsdSchema0.addImport(new Namespace("https://adwords.google.com/api/adwords/v11"), xsdSchema1)
			xsdSchema1.addImport(new Namespace("http://schemas.macys.com/api/ad/v1"), xsdSchema2)
			xsdSchema2.addImport(new Namespace("http://schemas.macys.com/definitions/ad/v1"), xsdSchema3)
			xsdSchema3.addImport(new Namespace("http://schemas.macys.com/api/ad/v1"), xsdSchema2)
		}
	}
}