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
	import System.Linq.Option.Option;
	
	import flash.utils.Dictionary;
	
	COMPILE::FLEX
	{
		import mx.collections.ArrayCollection;
		import mx.collections.IList;
	}

	public class EnumerationExtender
	{
		public static function Initialize():void {
			InitializeClass(Array);
			//InitializeClass(XMLList);
		}
		
		public static function InitializeClass(c:Class):void {
			c.prototype.asEnumerable = function():IEnumerable {
				return Enumerable.from(this);
			};
			c.prototype.getEnumerator = function():IEnumerator {
				return Enumerable.from(this).getEnumerator();
			};
			c.prototype.where = function(predicate:Function):IEnumerable {
				return this.asEnumerable().where(predicate);
			};
			c.prototype.select = function(selector:Function):IEnumerable {
				return this.asEnumerable().select(selector);
			};
			c.prototype.selectMany = function(function1:Function, function2:Function = null):IEnumerable {
				return this.asEnumerable().selectMany(function1, function2);
			}
			c.prototype.take = function(count:int):IEnumerable {
				return this.asEnumerable().take(count);	
			}
			c.prototype.takeWhile = function(predicate:Function) {
				return this.asEnumerable().takeWhile(predicate);
			}
			c.prototype.skip = function(count:int):IEnumerable {
				return this.asEnumerable().skip(count);
			}
			c.prototype.skipWhile = function(predicate:Function):IEnumerable {
				return this.asEnumerable().skipWhile(predicate);
			}
			c.prototype.joinEnumerables = function(inner:IEnumerable, outerKeySelector:Function, innerKeySelector:Function, resultSelector:Function):IEnumerable {
				return this.asEnumerable().join(inner, outerKeySelector, innerKeySelector, resultSelector);
			}
			c.prototype.groupJoin = function(inner:IEnumerable, outerKeySelector:Function, innerKeySelector:Function, resultSelector:Function):IEnumerable {
				return this.asEnumerable().groupJoin(inner, outerKeySelector, innerKeySelector, resultSelector);
			}
			c.prototype.orderBy = function(keySelector:Function, comparer:IComparer=null):IOrderedEnumerable {
				return this.asEnumerable().orderBy(keySelector, comparer);
			}
			c.prototype.orderByDescending = function(keySelector:Function, comparer:IComparer=null):IOrderedEnumerable {
				return this.asEnumerable().orderByDescending(keySelector, comparer);
			}
			c.prototype.groupBy = function(keySelector:Function, elementSelector:Function=null, resultSelector:Function=null):IEnumerable {
				return this.asEnumerable().groupBy(keySelector, elementSelector, resultSelector);
			}
			c.prototype.concatEnumerable = function(second:IEnumerable):IEnumerable {
				return this.asEnumerable().concat(second);
			}
			c.prototype.zip = function(second:IEnumerable, resultSelector:Function):IEnumerable {
				return this.asEnumerable().zip(second, resultSelector);
			}
			c.prototype.distinct = function(comparer:IEqualityComparer=null):IEnumerable {
				return this.asEnumerable().distinct(comparer);
			}
			c.prototype.union = function(second:IEnumerable, comparer:IEqualityComparer=null):IEnumerable {
				return this.asEnumerable().union(second, comparer);
			}
			c.prototype.intersect = function(second:IEnumerable, comparer:IEqualityComparer=null):IEnumerable {
				return this.asEnumerable().intersect(second, comparer);
			}
			c.prototype.except = function(second:IEnumerable, comparer:IEqualityComparer=null):IEnumerable {
				return this.asEnumerable().except(second, comparer);
			}
			c.prototype.reverseEnumerate = function():IEnumerable {
				return this.asEnumerable().reverse();
			}
			c.prototype.sequenceEqual = function(second:IEnumerable, comparer:IEqualityComparer=null):Boolean {
				return this.asEnumerable().sequenceEqual(second, comparer);
			}
			c.prototype.toArray = function():Array {
				return this.asEnumerable().toArray();
			}
				
			COMPILE::FLEX
			{
				c.prototype.toArrayCollection = function():ArrayCollection {
					return this.asEnumerable().toArrayCollection();
				}
				c.prototype.toList = function():IList {
					return this.asEnumerable().toList();
				}
			}
			
			c.prototype.toVector = function(type:Class):* {
				return this.asEnumerable().toVector(type);
			}
			c.prototype.toDictionary = function(keySelector:Function, elementSelector:Function=null):Dictionary {
				return this.asEnumerable().toDictionary(keySelector, elementSelector);
			}
			c.prototype.toLookup = function(keySelector:Function, elementSelector:Function=null):ILookup {
				return this.asEnumerable().toLookup(keySelector, elementSelector);
			}
			c.prototype.noneIfEmpty = function():Option {
				return this.asEnumerable().noneIfEmpty();
			}
			c.prototype.ofType = function(type:Class):IEnumerable {
				return this.asEnumerable().ofType(type);
			}
			c.prototype.cast = function(type:Class):IEnumerable {
				return this.asEnumerable().cast(type);
			}
			c.prototype.first = function(predicate:Function=null):* {
				return this.asEnumerable().first(predicate);
			}
			c.prototype.firstOrNone = function(predicate:Function=null):Option {
				return this.asEnumerable().firstOrNone(predicate);
			}
			c.prototype.last = function(predicate:Function=null):* {
				return this.asEnumerable().last(predicate);
			}
			c.prototype.lastOrNone = function(predicate:Function=null):Option {
				return this.asEnumerable().lastOrNone(predicate);
			}
			c.prototype.single = function(predicate:Function=null):* {
				return this.asEnumerable().single(predicate);
			}
			c.prototype.singleOrNone = function(predicate:Function=null):* {
				return this.asEnumerable().singleOrNone(predicate);
			}
			c.prototype.elementAt = function(index:int):* {
				return this.asEnumerable().elementAt(index);
			}
			c.prototype.elementAtOrNone = function(index:int):Option {
				return this.asEnumerable().elementAtOrNone(index);
			}
			c.prototype.any = function(predicate:Function=null):Boolean {
				return this.asEnumerable().any(predicate);
			}		
			c.prototype.all = function(predicate:Function):Boolean {
				return this.asEnumerable().all(predicate);
			}
			c.prototype.count = function(predicate:Function=null):int {
				return this.asEnumerable().count(predicate);
			}
			c.prototype.contains = function(value:*, comparer:IEqualityComparer=null):Boolean {
				return this.asEnumerable().contains(value, comparer);
			}
			c.prototype.aggregate = function(funcOrSeed:*, func:Function=null, resultSelector:Function=null):* {
				return this.asEnumerable().aggregate(funcOrSeed, func, resultSelector);
			}
			c.prototype.sum =  function(selector:Function=null):* {
				return this.asEnumerable().sum(selector);
			}
			c.prototype.min = function(selector:Function=null):* {
				return this.asEnumerable().min(selector);
			}
			c.prototype.max = function(selector:Function=null):* {
				return this.asEnumerable().max(selector);
			}
			c.prototype.average = function(selector:Function=null):* {
				return this.asEnumerable().average(selector);
			}
			c.prototype.eachElement = function(action:Function):* {
				this.asEnumerable().eachElement(action);
			}
				
				
			var names:Array = [ "asEnumerable", "getEnumerator", "where", "select", 
								"selectMany", "take", "takeWhile", "skip", "skipWhile", 
								"joinEnumerables", "groupJoin", "orderBy", "orderByDescending", 
								"groupBy", "concatEnumerable", "zip", "distinct", "union", "intersect", 
								"except", "reverseEnumerate", "sequenceEqual", 
								"toArray", "toVector", "toDictionary", "toLookup", 
								"noneIfEmpty", "ofType", "cast", "first", "firstOrNone", "last", 
								"lastOrNone", "single", "singleOrNone", "elementAt", "elementAtOrNone",
								"any", "all", "count", "contains","aggregate", "sum", "min", "max", 
								"average", "eachElement"];
			
			COMPILE::FLEX
			{
				names = names.concat(["toArrayCollection", "toList"])
			}
			
			Enumerable.from(names).eachElement(function(name:String):void { c.prototype.setPropertyIsEnumerable(name, false) });
		}
	}
}