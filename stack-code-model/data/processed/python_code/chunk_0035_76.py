package flexUnitTests
{
	import System.Collection.Generic.IEnumerable;
	import System.Collection.Generic.IGrouping;
	import System.Collection.Generic.ILookup;
	import System.Linq.Grouping;
	import System.Linq.Lookup;
	
	import org.flexunit.assertThat;
	import org.hamcrest.collection.array;
	import org.hamcrest.object.equalTo;

	public class LookupTests extends EnumerableTestsBase
	{		
		[Test]
		public function Lookup_is_an_IEnumerable_of_IGroupings():void {
			var lookup:ILookup = new Lookup([new Grouping("a"), new Grouping("b")]);
			var items:Array = lookup.toArray();
			
			assertThat(items.length, equalTo(2));
			assertThat(items[0] is IGrouping);
			assertThat(items[1] is IGrouping);
		}
		
		[Test(expected="ArgumentError")]
		public function Lookup_with_items_not_IGrouping_throws_ArgumentError():void {
			var lookup:ILookup = new Lookup([""]);
		}
		
		[Test]
		public function Lookup_with_no_items_is_just_empty():void {
			var lookup:Array = new Lookup().toArray();
			
			assertThat(lookup.length, equalTo(0));
		}
		
		[Test]
		public function adding_item_to_lookup_generates_IGrouping():void {
			var lookup:Lookup = new Lookup();
			
			lookup.add("111", 2);
			
			var items:Array = lookup.toArray();
			
			assertThat(items.length, equalTo(1));
			assertThat(items[0] is IGrouping);
			assertThat(items[0].key, equalTo("111"));
			assertThat(items[0].toArray(), array(2));
		}
		
		[Test]
		public function adding_two_items_with_different_keys_generates_two_IGroupings():void {
			var lookup:Lookup = new Lookup();
			
			lookup.add("111", 2);
			lookup.add("222", 4);
			
			var items:Array = lookup.toArray();
			
			assertThat(items.length, equalTo(2));
			assertThat(items[0] is IGrouping);
			assertThat(items[1] is IGrouping);
		}
		
		[Test]
		public function adding_two_items_with_same_key_generates_one_IGrouping():void {
			var lookup:Lookup = new Lookup();
			
			lookup.add("111", 2);
			lookup.add("111", 4);
			
			var items:Array = lookup.toArray();
			
			assertThat(items.length, equalTo(1));
			assertThat(items[0].key, equalTo("111"));
			assertThat(items[0].toArray(), array(2,4));
		}
		
		[Test]
		public function lookup_will_find_grouping_by_key():void {
			var lookup:Lookup = new Lookup();
			
			lookup.add("111", 2);
			lookup.add("111", 4);
			lookup.add("222", 6);
			lookup.add("222", 8);
			
			var group111:IGrouping = lookup.lookup("111");
			var group222:IGrouping = lookup.lookup("222");
			
			assertThat(group111.key, equalTo("111"));
			assertThat(group111.toArray(), array(2,4));
			assertThat(group222.key, equalTo("222"));
			assertThat(group222.toArray(), array(6,8));
		}
		
		[Test]
		public function toLookup_translates_collection_to_lookup():void {
			var lookup:ILookup = ["one", "two", "three", "four"]
				.toLookup(function(x:String):int { return x.length });
			
			assertThat(lookup.lookup(3).toArray(), array("one", "two"));
			assertThat(lookup.lookup(4).toArray(), array("four"));
			assertThat(lookup.lookup(5).toArray(), array("three"));
		}
		
		[Test]
		public function toLookup_with_elementSelector_translates_collection_to_lookup():void {
			var data:Array = [
				{ Company: "Coho Vineyard", Weight: 25.2, TrackingNumber: 89453312 },
				{ Company: "Lucerne Publishing", Weight: 18.7, TrackingNumber: 89112755 },
				{ Company: "Wingtip Toys", Weight: 6.0, TrackingNumber: 299456122 },
				{ Company: "Contoso Pharmaceuticals", Weight: 9.3, TrackingNumber: 670053128 },
				{ Company: "Wide World Importers", Weight: 33.8, TrackingNumber: 4665518773 }
				];
			
			var lookup:Lookup = data.toLookup(function(x) { return x.Company.charAt(0) }, function(x) { return x.Company + " " + x.TrackingNumber });
			
			assertThat(lookup.lookup("C").toArray()[0], equalTo("Coho Vineyard 89453312"));
			assertThat(lookup.lookup("C").toArray()[1], equalTo("Contoso Pharmaceuticals 670053128"));
			assertThat(lookup.lookup("L").toArray()[0], equalTo("Lucerne Publishing 89112755"));
			assertThat(lookup.lookup("W").toArray()[0], equalTo("Wingtip Toys 299456122"));
			assertThat(lookup.lookup("W").toArray()[1], equalTo("Wide World Importers 4665518773"));
		}
		
		[Test(expected="ArgumentError")]
		public function toLookup_throws_ArgumentError_when_keySelector_is_null():void {
			var lookup:ILookup = [1,2,3].toLookup(null);
		}
		
		[Test(expected="ArgumentError")]
		public function toLookup_throws_ArgumentError_when_keySelector_returns_null():void {
			var lookup:ILookup = [1,2,3].toLookup(function(x) { return null; });
		}
	}
}