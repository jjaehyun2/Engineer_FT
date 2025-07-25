package org.flemit.bytecode
{
	import flash.utils.Dictionary;
	
	import org.flemit.reflection.MethodInfo;
	import org.flemit.reflection.Type;
	import org.flemit.util.ClassUtility;
	
	
	public class ByteCodeLayoutBuilder implements IByteCodeLayoutBuilder
	{
		private var _types : Array = new Array();
		private var _methods : Dictionary = new Dictionary();
		
		private var _ignoredPackages : Array = [
			"flash.*", "mx.*", "fl.*", ":Object"
			];
		
		public function ByteCodeLayoutBuilder()
		{
		}
		
		public function registerType(type : Type) : void
		{
			if (_types.indexOf(type) == -1)
			{
				/* if (type.isGeneric)
				{
					registerType(type.genericTypeDefinition);
				} */
				
				if (type.baseType != type && type.baseType != null)
				{
					registerType(type.baseType);
				}
				
				for each(var interfaceType : Type in type.getInterfaces())
				{
					registerType(interfaceType);
				}
				
				_types.push(type);
			}
		}
		
		public function registerMethodBody(method : MethodInfo, methodBody : DynamicMethod) : void
		{
			_methods[method] = methodBody;
		}
		
		public function createLayout() : IByteCodeLayout
		{
			var layout : ByteCodeLayout = new ByteCodeLayout();
			
			for each(var type : Type in this._types)
			{
				var dynamicClass : DynamicClass = type as DynamicClass;
				
				if (isIgnored(type) || dynamicClass == null)
				{
					layout.registerMultiname(type.multiname);
					layout.registerMultiname(type.multiNamespaceName);
				}
				else
				{
					if (dynamicClass.getMethodBody(dynamicClass.scriptInitialiser) == null)
					{
						dynamicClass.addMethodBody(dynamicClass.scriptInitialiser,
							generateScriptInitialier(dynamicClass));
					}
					
					layout.registerClass(type);
					
					for each (var methodBody : DynamicMethod in dynamicClass.methodBodies)
					{
						layout.registerMethodBody(methodBody.method, methodBody);
					}
				}
			}
			
			return layout;
		}
		
		private function isIgnored(type : Type) : Boolean
		{
			for each(var ignoredPackage : String in _ignoredPackages)
			{
				if (ClassUtility.isMatch(ignoredPackage, type.fullName))
				{
					return true;
				}
			}
			
			return false;
		}
		
		private function pushUniqueValue(array : Array, value : IEqualityComparable) : uint
		{
			for (var i:uint =0; i<array.length; i++)
			{
				if (value.equals(array[i]))
					return i;
			}
			
			array.push(value);
			
			return array.length - 1;
		}
		
		private function generateScriptInitialier(dynamicClass : Type) : DynamicMethod
		{
			var clsNamespaceSet : NamespaceSet = new NamespaceSet(
				[new BCNamespace(dynamicClass.packageName, NamespaceKind.PACKAGE_NAMESPACE)]);
			
			with (Instructions)
			{
				if (dynamicClass.isInterface)
				{
					return new DynamicMethod(dynamicClass.scriptInitialiser, 3, 2, 1, 3, [
						[GetLocal_0],
						[PushScope],
						[FindPropertyStrict, new MultipleNamespaceName(dynamicClass.name, clsNamespaceSet)], 
						[PushNull],
						[NewClass, dynamicClass],
						[InitProperty, dynamicClass.qname],
						[ReturnVoid]
					]); 
				}
				else
				{
					// TODO: Support where base class is not Object
					return new DynamicMethod(dynamicClass.scriptInitialiser, 3, 2, 1, 3, [
						[GetLocal_0],
						[PushScope],
						//[GetScopeObject, 0],
						[FindPropertyStrict, dynamicClass.multiNamespaceName], 
						[GetLex, dynamicClass.baseType.qname],
						[PushScope],
						[GetLex, dynamicClass.baseType.qname],
						[NewClass, dynamicClass],
						[PopScope],
						[InitProperty, dynamicClass.qname],
						[ReturnVoid]
					]);
				}
			}
		}
	}
}