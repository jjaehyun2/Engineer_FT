package flexUnitTests
{
	import System.Collection.Generic.IEnumerable;
	
	import org.flexunit.assertThat;
	import org.hamcrest.collection.array;
	import org.hamcrest.object.equalTo;
	import org.hamcrest.object.nullValue;

	public class JoinTests extends EnumerableTestsBase
	{		
		[Test]
		public function join_joins_two_collections_into_a_collection_of_a_new_type():void {
			var magnus:* = { Name: "Hedlund, Magnus" };
			var terry:* = { Name: "Adams, Terry" };
			var charlotte:* = { Name: "Weiss, Charlotte" };
			
			var barley:* = { Name: "Barley", Owner: terry };
			var boots:* = { Name: "Boots", Owner: terry };
			var whiskers:* = { Name: "Whiskers", Owner: charlotte };
			var daisy:* = { Name: "Daisy", Owner: magnus };
			
			var people:Array = [ magnus, terry, charlotte ];
			var pets:Array = [ barley, boots, whiskers, daisy ];
			
			var query:IEnumerable = people.joinEnumerables(pets.asEnumerable(), 
					function(person:*):* {return person},
					function(pet:*):* { return pet.Owner},
					function(person, pet) { return {OwnerName: person.Name, Pet: pet.Name}; });
			
			var output:Array = query.toArray();
			
			assertThat(output[0].OwnerName, equalTo("Hedlund, Magnus"));
			assertThat(output[0].Pet, equalTo("Daisy"));
			assertThat(output[1].OwnerName, equalTo("Adams, Terry"));
			assertThat(output[1].Pet, equalTo("Barley"));
			assertThat(output[2].OwnerName, equalTo("Adams, Terry"));
			assertThat(output[2].Pet, equalTo("Boots"));
			assertThat(output[3].OwnerName, equalTo("Weiss, Charlotte"));
			assertThat(output[3].Pet, equalTo("Whiskers"));
		}
		
		private function noOp(x, y=null) {}
		
		[Test(expected="ArgumentError")]
		public function join_throws_ArgumentError_when_inner_is_null():void {
			var query:IEnumerable = [1,2,3].asEnumerable().join(null, noOp, noOp, noOp);
		}
		
		[Test(expected="ArgumentError")]
		public function join_throws_ArgumentError_when_outerKeySelector_is_null():void {
			var query:IEnumerable = [1,2,3].asEnumerable().join([].asEnumerable(), null, noOp, noOp);
		}
		
		[Test(expected="ArgumentError")]
		public function join_throws_ArgumentError_when_innerKeySelector_is_null():void {
			var query:IEnumerable = [1,2,3].asEnumerable().join([].asEnumerable(), noOp, null, noOp);
		}
		
		[Test(expected="ArgumentError")]
		public function join_throws_ArgumentError_when_resultSelector_is_null():void {
			var query:IEnumerable = [1,2,3].asEnumerable().join([].asEnumerable(), noOp, noOp, null);
		}
		
		
		[Test]
		public function groupJoin_corelates_elements_based_on_groups():void {
			var magnus:* = { Name: "Hedlund, Magnus" };
			var terry:* = { Name: "Adams, Terry" };
			var charlotte:* = { Name: "Weiss, Charlotte" };
			
			var barley:* = { Name: "Barley", Owner: terry };
			var boots:* = { Name: "Boots", Owner: terry };
			var whiskers:* = { Name: "Whiskers", Owner: charlotte };
			var daisy:* = { Name: "Daisy", Owner: magnus };
			
			var people:Array = [ magnus, terry, charlotte ];
			var pets:Array = [ barley, boots, whiskers, daisy ];
			
			var query:IEnumerable = people.groupJoin(pets.asEnumerable(),
				function(person) { return person },
				function(pet) { return pet.Owner },
				function(person, petCollection) { return { OwnerName: person.Name, Pets: petCollection.select(function(pet) { return pet.Name }) }});
			
			var output:Array = query.toArray();
			
			assertThat(output[0].OwnerName, equalTo("Hedlund, Magnus"));
			assertThat(output[0].Pets.toArray(), array("Daisy"));
			assertThat(output[1].OwnerName, equalTo("Adams, Terry"));
			assertThat(output[1].Pets.toArray(), array("Barley", "Boots"));
			assertThat(output[2].OwnerName, equalTo("Weiss, Charlotte"));
			assertThat(output[2].Pets.toArray(), array("Whiskers"));
		}
				
		[Test(expected="ArgumentError")]
		public function groupJoin_throws_ArgumentError_when_inner_is_null():void {
			var query:IEnumerable = [1,2,3].asEnumerable().groupJoin(null, noOp, noOp, noOp);
		}
		
		[Test(expected="ArgumentError")]
		public function groupJoin_throws_ArgumentError_when_outerKeySelector_is_null():void {
			var query:IEnumerable = [1,2,3].asEnumerable().groupJoin([].asEnumerable(), null, noOp, noOp);
		}
		
		[Test(expected="ArgumentError")]
		public function groupJoin_throws_ArgumentError_when_innerKeySelector_is_null():void {
			var query:IEnumerable = [1,2,3].asEnumerable().groupJoin([].asEnumerable(), noOp, null, noOp);
		}
		
		[Test(expected="ArgumentError")]
		public function groupJoin_throws_ArgumentError_when_resultSelector_is_null():void {
			var query:IEnumerable = [1,2,3].asEnumerable().groupJoin([].asEnumerable(), noOp, noOp, null);
		}	
		
	}
}