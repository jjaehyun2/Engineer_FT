//Copyright 2010 SRT Solutions
//
//Licensed under the Apache License, Version 2.0 (the "License");
//you may not use this file except in compliance with the License.
//	You may obtain a copy of the License at
//
//http://www.apache.org/licenses/LICENSE-2.0
//
//Unless required by applicable law or agreed to in writing, software
//distributed under the License is distributed on an "AS IS" BASIS,
//WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//	See the License for the specific language governing permissions and
//limitations under the License.

package System.Linq
{
	import System.Collection.Generic.IComparer;
	import System.Collection.Generic.IEnumerable;
	import System.Collection.Generic.IEnumerator;
	import System.Collection.Generic.IEqualityComparer;
	import System.Collection.Generic.ILookup;
	import System.Collection.Generic.IOrderedEnumerable;
	import System.Linq.FunctionBuilder.identity;
	import System.Linq.Option.Option;
	import System.Linq.Option.none;
	import System.Linq.Option.some;
	
	import flash.utils.Dictionary;
	import flash.utils.Proxy;
	import flash.utils.flash_proxy;
	import flash.utils.getDefinitionByName;
	import flash.utils.getQualifiedClassName;
	
	COMPILE::FLEX
	{
		import mx.collections.ArrayCollection;
		import mx.collections.ArrayList;
		import mx.collections.IList;
	}
	
	public class Enumerable extends Proxy implements IEnumerable
	{
		private var source:*;
		private var enumeratorFactory:Function;
		
		public function Enumerable(source:*, enumeratorFactory:Function) {	
			this.source = source;
			this.enumeratorFactory = enumeratorFactory;	
		} 
		
		public static function from(obj:Object) : IEnumerable {
			if(obj is IEnumerable)
				return obj as IEnumerable;
			
			if(obj is Array)
				return new Enumerable( obj as Array,
					function(source:*):IEnumerator { return new ArrayEnumerator(source as Array) });
			
			COMPILE::FLEX
			{
				if(obj is IList)
					return new Enumerable(obj as IList,
						function(source:*):IEnumerator { return new ListEnumerator(obj as IList) });
			}
			
			if(obj is XMLList)
				return new Enumerable(obj as XMLList,
					function(source:*):IEnumerator { return new XMLListEnumerator(obj as XMLList) });
			
			if("length" in obj)
				return new Enumerable(obj as Vector,
					function (source:*):IEnumerator { return new VectorEnumerator(obj) });
			
			return null;
		}
		
		public function getEnumerator():IEnumerator
		{
			return enumeratorFactory(source);
		}
		
		public function where(predicate:Function):IEnumerable {
			throwIfArgumentIsNull(predicate, "predicate");
			
			return new Enumerable(this,
				function(source:*):IEnumerator {
					return new WhereEnumerator(source, predicate) });
		}
		
		public function select(selector:Function):IEnumerable {
			throwIfArgumentIsNull(selector, "selector");
			
			return new Enumerable(this,
				function(source:*):IEnumerator {
					return new SelectEnumerator(source, selector) });
		}
		
		public function selectMany(collectionSelector:Function, resultsSelector:Function = null):IEnumerable {
			throwIfArgumentIsNull(collectionSelector, "collectionSelector");
			
			return new Enumerable(this,
				function(source:*):IEnumerator {
					return new SelectManyEnumerator(source, collectionSelector, resultsSelector) });
		}
		
		public function take(count:int):IEnumerable {
			return takeWhile(function(x:*,i:int){return i < count});
		}
		
		public function takeWhile(predicate:Function):IEnumerable {
			throwIfArgumentIsNull(predicate, "predicate");
			
			return new Enumerable(this,
				function(source:*):IEnumerator {
					return new TakeEnumerator(source, predicate) });
		}
		
		public function skip(count:int):IEnumerable {
			return skipWhile(function(x:*,i:int){return i < count});
		}
		
		public function skipWhile(predicate:Function):IEnumerable {
			throwIfArgumentIsNull(predicate, "predicate");
			
			return new Enumerable(this,
				function(source:*):IEnumerator {
					return new SkipEnumerator(source, predicate) });
		}
		
		private function throwIfArgumentIsNull(test:*, name:String):void {
			if(test == null)
				throw new ArgumentError(name + " was null");
		}
		
		public function join(inner:IEnumerable, outerKeySelector:Function, innerKeySelector:Function, resultSelector:Function):IEnumerable {
			throwIfArgumentIsNull(inner, "inner");
			throwIfArgumentIsNull(outerKeySelector, "outerKeySelector");
			throwIfArgumentIsNull(innerKeySelector, "innerKeySelector");
			throwIfArgumentIsNull(resultSelector, "resultSelector");
			
			var innerLookup:ILookup = inner.toLookup(innerKeySelector);
			
			return selectMany(function(outerItem) { return innerLookup.lookup(outerKeySelector(outerItem)) }, resultSelector);
		}
		
		public function groupJoin(inner:IEnumerable, outerKeySelector:Function, innerKeySelector:Function, resultSelector:Function):IEnumerable {
			throwIfArgumentIsNull(inner, "inner");
			throwIfArgumentIsNull(outerKeySelector, "outerKeySelector");
			throwIfArgumentIsNull(innerKeySelector, "innerKeySelector");
			throwIfArgumentIsNull(resultSelector, "resultSelector");
			
			var lookup:ILookup = inner.toLookup(innerKeySelector);
			return select(function(x:*):* { return resultSelector(x, lookup.lookup(outerKeySelector(x))) });
		}
		
		public function orderBy(keySelector:Function, comparer:IComparer=null):IOrderedEnumerable {
			throwIfArgumentIsNull(keySelector, "keySelector");
			
			return new OrderedEnumerable(this, keySelector, [], comparer);
		}
		
		public function orderByDescending(keySelector:Function, comparer:IComparer=null):IOrderedEnumerable {
			throwIfArgumentIsNull(keySelector, "keySelector");
			
			return new OrderedEnumerable(this, keySelector, [], comparer, true);
		}
		
		public function groupBy(keySelector:Function, elementSelector:Function=null, resultSelector:Function=null):IEnumerable {
			if(resultSelector == null)
				resultSelector = function(key, all) { return all };
			
			return toLookup(keySelector, elementSelector).select(function(x) { return resultSelector(x.key, x) });
		}
		
		public function concat(second:IEnumerable):IEnumerable {
			throwIfArgumentIsNull(second, "second");
			
			return new Enumerable(this,
				function(source:*):IEnumerator {
					return new ConcatEnumerator(source, second) });
		}
		
		public function zip(second:IEnumerable, resultSelector:Function):IEnumerable {
			throwIfArgumentIsNull(second, "second");
			throwIfArgumentIsNull(resultSelector, "resultSelector");
			
			return new Enumerable(this,
				function(source:*):IEnumerator {
					return new ZipEnumerator(source, second, resultSelector) });
		}
		
		public function distinct(comparer:IEqualityComparer=null):IEnumerable {
			return new Enumerable(this,
				function(source:*):IEnumerator {
					return new DistinctEnumerator(source, comparer) });
		}
		
		public function union(second:IEnumerable, comparer:IEqualityComparer=null):IEnumerable {
			return concat(second).distinct(comparer);
		}
		
		public function intersect(second:IEnumerable, comparer:IEqualityComparer=null):IEnumerable {
			throwIfArgumentIsNull(second, "second");
			
			return new Enumerable(this,
				function(source:*):IEnumerator {
					return new IntersectEnumerator(source, second, comparer) });
		}
		
		public function except(second:IEnumerable, comparer:IEqualityComparer=null):IEnumerable {
			throwIfArgumentIsNull(second, "second");
			
			return new Enumerable(this,
				function(source:*):IEnumerator {
					return new IntersectEnumerator(source, second, comparer, true) });
		}
		
		public function reverse():IEnumerable {
			return Enumerable.from(toArray().reverse());
		}
		
		public function sequenceEqual(second:IEnumerable, comparer:IEqualityComparer=null):Boolean {
			throwIfArgumentIsNull(second, "second");
			
			var compare:Function = comparer != null ? comparer.Equals : function(f,s) { return f == s };
			
			var firstEnumerator:IEnumerator = getEnumerator();
			var secondEnumerator:IEnumerator = second.getEnumerator();
			
			while(firstEnumerator.MoveNext())
			{
				if(!secondEnumerator.MoveNext())
					return false;
				
				if(!compare(firstEnumerator.Current(),secondEnumerator.Current()))
					return false;
			}
			
			return !secondEnumerator.MoveNext();
		}
		
		public function toArray():Array {
			return populateContainer(new Array(), function(al, item) { al.push(item) });
		}
		
		COMPILE::FLEX
		{
			public function toArrayCollection():ArrayCollection {
				return populateContainer(new ArrayCollection(), function(al, item) { al.addItem(item) });	
			}
			
			public function toList():IList {
				return populateContainer(new ArrayList(), function(al, item) { al.addItem(item) });	
			}
		}
		
		public function toVector(type:Class):* {
			var typedVectorName:String = getQualifiedClassName(Vector) + ".<" + getQualifiedClassName(type)+ ">";
			var typedVectorClass:Class = getDefinitionByName(typedVectorName) as Class;
			
			return populateContainer(new typedVectorClass(), function(v,item) { v.push(item)} );
		}
		
		private function addLengthToDictionary(dictionary:Dictionary):Dictionary {
			
			dictionary.length = function():uint { 
				var length:uint = 0;
				for(var item:* in dictionary)
					if(item != "length")
						length++;
				return length;
			};
				
			dictionary.setPropertyIsEnumerable("length", false);
			
			return dictionary;
		}
		
		public function toDictionary(keySelector:Function, elementSelector:Function=null):Dictionary {
			throwIfArgumentIsNull(keySelector, "keySelector");
			
			if(elementSelector == null)
				elementSelector = identity;
					
			var result:Dictionary = new Dictionary();
			
			for each(var item in this)
			{
				var key:* = keySelector(item);
				
				if(key == null)
					throw new ArgumentError("keySelector for [" + item.toString() + "] returned null");
				
				if(key in result)
					throw new ArgumentError("keySelector for [" + item.toString() + "] returned a duplicate key");
				
				result[key] = elementSelector(item);
			}
			
			return addLengthToDictionary(result);
		}
		
		public function toLookup(keySelector:Function, elementSelector:Function=null):ILookup {
			throwIfArgumentIsNull(keySelector, "keySelector");
			
			if(elementSelector == null)
				elementSelector = identity;
			
			var result:Lookup = new Lookup();
			
			eachElement(function(x:*):void { result.add(keySelector(x), elementSelector(x)) });
			
			return result;
		}
		
		private function populateContainer(container:*, add:Function):* {
			var enumerator:IEnumerator = getEnumerator();
			
			while(enumerator.MoveNext())
				add(container, enumerator.Current());
			
			return container;	
		}
		
		public function noneIfEmpty():Option {
			return any() ? some(this) : none;
		}
		
		public function ofType(type:Class):IEnumerable {
			return where(function(x){ return x is type });
		}
		
		public function cast(type:Class):IEnumerable {
			return select(function(x) { return type(x) });
		}
		
		public function first(predicate:Function=null):* {
			var result:Option = firstOrNone(predicate);
			
			if(result.isNone)
				throw new RangeError("Seqnence contains no elements");
				
			return result.value; 
		}
		
		public function firstOrNone(predicate:Function=null):Option {
			if(predicate == null)
				predicate = function(x) { return true; };
			
			var filteredEnumerator:IEnumerator = where(predicate).getEnumerator();
			
			if(!filteredEnumerator.MoveNext())
				return none;
			
			return some(filteredEnumerator.Current()); 
		}
		
		public function last(predicate:Function=null):* {
			var result:Option = lastOrNone(predicate);
			
			if(result.isNone)
				throw new RangeError("Seqnence contains no elements");
			
			return result.value;
		}
		
		public function lastOrNone(predicate:Function=null):Option {
			if(predicate == null)
				predicate = function(x) { return true; };
			
			return where(predicate).aggregate(none, function(acc, x) { return some(x)});
		}
		
		public function single(predicate:Function=null):* {
			var result:Option = singleOrNone(predicate);
			
			if(result.isNone)
				throw new RangeError("Sequence does not contain one element");
			
			return result.value;
		}
		
		public function singleOrNone(predicate:Function=null):Option {
			if(predicate == null)
				predicate = function(x) { return true; };
			
			var enumerator:IEnumerator = where(predicate).getEnumerator();
			
			if(!enumerator.MoveNext())
				return none;
			
			var result:Option = some(enumerator.Current());
			
			if(enumerator.MoveNext())
				throw new RangeError("Sequence does not contain one element");
			
			return result;
		}
		
		public function elementAt(index:int):* {
			var result:Option = elementAtOrNone(index);
			
			if(result.isNone)
				throw new RangeError("Index was out of range");
			
			return result.value;
		}
		
		public function elementAtOrNone(index:int):Option {
			var count:int = 0;
			return firstOrNone(function(x) {return (count++ == index);});
		}
			
		
		public function any(predicate:Function=null):Boolean {
			if(predicate == null)
				predicate = function(x) { return true; };
			
			return where(predicate).getEnumerator().MoveNext();
		}
		
		public function all(predicate:Function):Boolean {
			throwIfArgumentIsNull(predicate, "predicate");
			
			var enumerator:IEnumerator = getEnumerator();
			while(enumerator.MoveNext())
			{
				if(!predicate(enumerator.Current()))
					return false;
			}
					
			return true;
		}
		
		public function count(predicate:Function=null):int {
			var enumerator:IEnumerator = predicate != null ? where(predicate).getEnumerator() : getEnumerator();
			
			if("internalCount" in enumerator)
				return (enumerator as Object).internalCount;
			
			var count:int = 0;
			
			while(enumerator.MoveNext())
				count++;
			
			return count;
		}
		
		public function contains(value:*, comparer:IEqualityComparer=null):Boolean {
			if(comparer == null) {
			    var result:Option = firstOrNone(function(x) { return x == value });
			}
			else {
				var result:Option = firstOrNone(function(x) { return comparer.Equals(x, value) });
			}
			
			return result.isSome;
		}
		
		public function aggregate(funcOrSeed:*, func:Function=null, resultSelector:Function=null):* {
			
			var enumerator:IEnumerator = getEnumerator();
			
			if(funcOrSeed is Function)
			{
				if(!enumerator.MoveNext())
					throw new RangeError("Sequence contains no elements");
					
				var aggregate = enumerator.Current();
				var aggregator:Function = funcOrSeed as Function;
			}
			else
			{
				var aggregate = funcOrSeed;
				var aggregator = func;
			}
			
			if(resultSelector == null)
				resultSelector = identity;
			
			while(enumerator.MoveNext()) {
				aggregate = aggregator(aggregate, enumerator.Current());
			}
			
			return resultSelector(aggregate);
		}
		
		public function sum(selector:Function=null):* {
			if(selector == null)
				selector = identity;
			
			return aggregate(0.0, function(accumulator:*, item:*) { return accumulator + selector(item) });
		}
		
		public function average(selector:Function=null):* {
			if(selector == null)
				selector = identity;
			
			var count:int = 0;
			var sum:* = aggregate(0.0, function(accumulator:*, item:*) 
			{
				count++;
				return accumulator + selector(item) 
			});
			
			return sum / count;
		}
		
		private function ExtremeSelector(comparitor:Function, selector:Function=null):* {
			if(selector == null)
				selector = identity;
			
			var extreme = null;
			var enumerator:IEnumerator = getEnumerator();
			while(enumerator.MoveNext()) {
				var selectedItem = selector(enumerator.Current());
				if(extreme == null || comparitor(selectedItem, extreme))
					extreme = selectedItem;
			}
			
			if(extreme == null)
				throw new RangeError("Sequence contains no elements");
			
			return extreme;
		}
		
		public function min(selector:Function=null):* {
			return ExtremeSelector(
				function(left:*, right:*):* { return left < right },
				selector);
		}
		
		public function max(selector:Function=null):* {
			return ExtremeSelector(
				function(left:*, right:*):* { return left > right },
				selector);
		}
		
		public static function range(start:int, count:int=-1):IEnumerable {
			if(count < 0)
			{
				count = start;
				start = 0;
			}
			
			return new Enumerable(null,
				function(source:*):IEnumerator {
					return new RangeEnumerator(start, count) });
		}
	
		public static function repeat(element:*, count:int):IEnumerable {
			if(count < 0)
				throw new RangeError("Count was less than zero");
			
			return new Enumerable(null,
				function(source:*):IEnumerator {
					return new RepeatEnumerator(element, count) });
		}
		
		public static const empty:IEnumerable = from([]);
		
		public static function times(count:int, action:Function):void {
			range(count).eachElement(action);
		}
		
		public function eachElement(action:Function):void {
			var enumerator:IEnumerator = getEnumerator();
			while(enumerator.MoveNext())
				action(enumerator.Current());
		}
		
		private var currentEnumerator:IEnumerator;
		
		override flash_proxy function nextNameIndex (index:int):int {
			if(index <= 0)
			{
				currentEnumerator = getEnumerator();
			}
			
			return currentEnumerator.MoveNext() ? index + 1 : 0;
		}
		
		override flash_proxy function nextValue(index:int):* {
			return currentEnumerator.Current();
		}
	}
}