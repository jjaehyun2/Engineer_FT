package org.osflash.dom.path
{
	import asunit.asserts.assertEquals;

	import org.osflash.dom.element.DOMDocument;
	import org.osflash.dom.element.DOMNode;
	import org.osflash.dom.element.IDOMDocument;
	import org.osflash.dom.element.IDOMNode;
	/**
	 * @author Simon Richardson - simon@ustwo.co.uk
	 */
	public class DOMPathNameIndexAccessTest
	{
		
		protected var document : IDOMDocument;

		[Before]
		public function setUp() : void
		{
			document = new DOMDocument();
		}

		[After]
		public function tearDown() : void
		{
			document = null;
		}
		
		[Tester]
		public function add_elements_and_path_select_node1_index1() : void
		{
			const node0 : DOMNode = new DOMNode('node1');
			const node1 : DOMNode = new DOMNode('node1');
			
			document.add(node0);
			document.add(node1);
			
			const result : Vector.<IDOMNode> = document.select('node1[1]');
			
			assertEquals('Result length should be 1', 1, result.length);
			assertEquals('Result item at 0 index should be same as node1', node1, result[0]);
		}
		
		[Tester]
		public function add_elements_and_path_select_node1_index1_in_context() : void
		{
			const node0 : DOMNode = new DOMNode('node1');
			const node1 : DOMNode = new DOMNode('node1');
			
			document.add(node0);
			document.add(node1);
			
			const result : Vector.<IDOMNode> = document.select('/node1[1]');
			
			assertEquals('Result length should be 1', 1, result.length);
			assertEquals('Result item at 0 index should be same as node1', node1, result[0]);
		}
		
		[Tester]
		public function add_elements_and_path_select_node1_index1_in_document() : void
		{
			const node0 : DOMNode = new DOMNode('node1');
			const node1 : DOMNode = new DOMNode('node1');
			
			document.add(node0);
			document.add(node1);
			
			const result : Vector.<IDOMNode> = document.select('//node1[1]');
			
			assertEquals('Result length should be 1', 1, result.length);
			assertEquals('Result item at 0 index should be same as node1', node1, result[0]);
		}
		
		[Tester]
		public function add_elements_and_path_select_node1_then_subnode1_index1() : void
		{
			const node0 : DOMNode = new DOMNode('node1');
			const node1 : DOMNode = new DOMNode('node1');
			
			const subnode0 : DOMNode = new DOMNode('subnode1');
			const subnode1 : DOMNode = new DOMNode('subnode1');
			
			document.add(node0);
			document.add(node1);
			
			node1.add(subnode0);
			node1.add(subnode1);
			
			const result : Vector.<IDOMNode> = document.select('node1/subnode1[1]');
			
			assertEquals('Result length should be 1', 1, result.length);
			assertEquals('Result item at 0 index should be same as subnode1', subnode1, result[0]);
		}
		
		[Tester]
		public function add_elements_and_path_select_node1_then_subnode1_index1_in_context() : void
		{
			const node0 : DOMNode = new DOMNode('node1');
			const node1 : DOMNode = new DOMNode('node1');
			
			const subnode0 : DOMNode = new DOMNode('subnode1');
			const subnode1 : DOMNode = new DOMNode('subnode1');
			
			document.add(node0);
			document.add(node1);
			
			node1.add(subnode0);
			node1.add(subnode1);
			
			const result : Vector.<IDOMNode> = document.select('/node1/subnode1[1]');
			
			assertEquals('Result length should be 1', 1, result.length);
			assertEquals('Result item at 0 index should be same as subnode1', subnode1, result[0]);
		}
		
		[Tester]
		public function add_elements_and_path_select_node1_then_subnode1_index1_in_document() : void
		{
			const node0 : DOMNode = new DOMNode('node1');
			const node1 : DOMNode = new DOMNode('node1');
			
			const subnode0 : DOMNode = new DOMNode('subnode1');
			const subnode1 : DOMNode = new DOMNode('subnode1');
			
			document.add(node0);
			document.add(node1);
			
			node1.add(subnode0);
			node1.add(subnode1);
			
			const result : Vector.<IDOMNode> = document.select('//node1/subnode1[1]');
			
			assertEquals('Result length should be 1', 1, result.length);
			assertEquals('Result item at 0 index should be same as subnode1', subnode1, result[0]);
		}
		
		[Tester]
		public function add_elements_and_path_select_node1_then_subnode1_then_subsubnode0_index0() : void
		{
			const node0 : DOMNode = new DOMNode('node1');
			const node1 : DOMNode = new DOMNode('node1');
			
			const subnode0 : DOMNode = new DOMNode('subnode1');
			const subnode1 : DOMNode = new DOMNode('subnode1');
			
			const subsubnode0 : DOMNode = new DOMNode('subsubnode0');
			
			document.add(node0);
			document.add(node1);
			
			node1.add(subnode0);
			node1.add(subnode1);
			
			subnode0.add(subsubnode0);
			
			const result : Vector.<IDOMNode> = document.select('node1/subnode1/subsubnode0[0]');
			
			assertEquals('Result length should be 1', 1, result.length);
			assertEquals('Result item at 0 index should be same as subsubnode0', 
																				subsubnode0, 
																				result[0]
																				);
		}
		
		[Tester]
		public function add_elements_and_path_select_node1_then_subnode1_then_subsubnode0_index0_in_context() : void
		{
			const node0 : DOMNode = new DOMNode('node1');
			const node1 : DOMNode = new DOMNode('node1');
			
			const subnode0 : DOMNode = new DOMNode('subnode1');
			const subnode1 : DOMNode = new DOMNode('subnode1');
			
			const subsubnode0 : DOMNode = new DOMNode('subsubnode0');
			
			document.add(node0);
			document.add(node1);
			
			node1.add(subnode0);
			node1.add(subnode1);
			
			subnode0.add(subsubnode0);
			
			const result : Vector.<IDOMNode> = document.select('/node1/subnode1/subsubnode0[0]');
			
			assertEquals('Result length should be 1', 1, result.length);
			assertEquals('Result item at 0 index should be same as subsubnode0', 
																				subsubnode0, 
																				result[0]
																				);
		}
		
		
		[Tester]
		public function add_elements_and_path_select_node1_then_subnode1_then_subsubnode0_index0_in_document() : void
		{
			const node0 : DOMNode = new DOMNode('node1');
			const node1 : DOMNode = new DOMNode('node1');
			
			const subnode0 : DOMNode = new DOMNode('subnode1');
			const subnode1 : DOMNode = new DOMNode('subnode1');
			
			const subsubnode0 : DOMNode = new DOMNode('subsubnode0');
			
			document.add(node0);
			document.add(node1);
			
			node1.add(subnode0);
			node1.add(subnode1);
			
			subnode0.add(subsubnode0);
			
			const result : Vector.<IDOMNode> = document.select('//node1/subnode1/subsubnode0[0]');
			
			assertEquals('Result length should be 1', 1, result.length);
			assertEquals('Result item at 0 index should be same as subsubnode0', 
																				subsubnode0, 
																				result[0]
																				);
		}
		
		[Tester]
		public function add_elements_and_path_select_node1_index1_then_subnode1() : void
		{
			const node0 : DOMNode = new DOMNode('node1');
			const node1 : DOMNode = new DOMNode('node1');
			
			const subnode0 : DOMNode = new DOMNode('subnode1');
			const subnode1 : DOMNode = new DOMNode('subnode1');
			
			document.add(node0);
			document.add(node1);
			
			node1.add(subnode0);
			node1.add(subnode1);
			
			const result : Vector.<IDOMNode> = document.select('node1[1]/subnode1');
			
			assertEquals('Result length should be 2', 2, result.length);
			assertEquals('Result item at 0 index should be same as subnode0', subnode0, result[0]);
		}
		
		[Tester]
		public function add_elements_and_path_select_node1_index1_then_subnode1_in_context() : void
		{
			const node0 : DOMNode = new DOMNode('node1');
			const node1 : DOMNode = new DOMNode('node1');
			
			const subnode0 : DOMNode = new DOMNode('subnode1');
			const subnode1 : DOMNode = new DOMNode('subnode1');
			
			document.add(node0);
			document.add(node1);
			
			node1.add(subnode0);
			node1.add(subnode1);
			
			const result : Vector.<IDOMNode> = document.select('/node1[1]/subnode1');
			
			assertEquals('Result length should be 2', 2, result.length);
			assertEquals('Result item at 0 index should be same as subnode0', subnode0, result[0]);
		}
		
		
		[Tester]
		public function add_elements_and_path_select_node1_index1_then_subnode1_in_document() : void
		{
			const node0 : DOMNode = new DOMNode('node1');
			const node1 : DOMNode = new DOMNode('node1');
			
			const subnode0 : DOMNode = new DOMNode('subnode1');
			const subnode1 : DOMNode = new DOMNode('subnode1');
			
			document.add(node0);
			document.add(node1);
			
			node1.add(subnode0);
			node1.add(subnode1);
			
			const result : Vector.<IDOMNode> = document.select('//node1[1]/subnode1');
			
			assertEquals('Result length should be 2', 2, result.length);
			assertEquals('Result item at 0 index should be same as subnode0', subnode0, result[0]);
		}
		
		[Tester]
		public function add_elements_and_path_select_node1_index1_then_subnode1_index0_then_subsubnode0() : void
		{
			const node0 : DOMNode = new DOMNode('node1');
			const node1 : DOMNode = new DOMNode('node1');
			
			const subnode0 : DOMNode = new DOMNode('subnode1');
			const subnode1 : DOMNode = new DOMNode('subnode1');
			
			const subsubnode0 : DOMNode = new DOMNode('subsubnode0');
			
			document.add(node0);
			document.add(node1);
			
			node1.add(subnode0);
			node1.add(subnode1);
			
			subnode0.add(subsubnode0);
			
			const result : Vector.<IDOMNode> = document.select('node1[1]/subnode1[0]/subsubnode0');
			
			assertEquals('Result length should be 1', 1, result.length);
			assertEquals('Result item at 0 index should be same as subsubnode0', subsubnode0, result[0]);
		}
		
		[Tester]
		public function add_elements_and_path_select_node1_index1_then_subnode1_index0_then_subsubnode0_in_context() : void
		{
			const node0 : DOMNode = new DOMNode('node1');
			const node1 : DOMNode = new DOMNode('node1');
			
			const subnode0 : DOMNode = new DOMNode('subnode1');
			const subnode1 : DOMNode = new DOMNode('subnode1');
			
			const subsubnode0 : DOMNode = new DOMNode('subsubnode0');
			
			document.add(node0);
			document.add(node1);
			
			node1.add(subnode0);
			node1.add(subnode1);
			
			subnode0.add(subsubnode0);
			
			const result : Vector.<IDOMNode> = document.select('/node1[1]/subnode1[0]/subsubnode0');
			
			assertEquals('Result length should be 1', 1, result.length);
			assertEquals('Result item at 0 index should be same as subsubnode0', subsubnode0, result[0]);
		}
		
		[Tester]
		public function add_elements_and_path_select_node1_index1_then_subnode1_index0_then_subsubnode0_in_document() : void
		{
			const node0 : DOMNode = new DOMNode('node1');
			const node1 : DOMNode = new DOMNode('node1');
			
			const subnode0 : DOMNode = new DOMNode('subnode1');
			const subnode1 : DOMNode = new DOMNode('subnode1');
			
			const subsubnode0 : DOMNode = new DOMNode('subsubnode0');
			
			document.add(node0);
			document.add(node1);
			
			node1.add(subnode0);
			node1.add(subnode1);
			
			subnode0.add(subsubnode0);
			
			const result : Vector.<IDOMNode> = document.select('//node1[1]/subnode1[0]/subsubnode0');
			
			assertEquals('Result length should be 1', 1, result.length);
			assertEquals('Result item at 0 index should be same as subsubnode0', subsubnode0, result[0]);
		}
		
		[Test]
		public function path_select_node1_with_index1_then_subnode1() : void
		{
			const node0 : IDOMNode = new DOMNode('node1');
			const node1 : IDOMNode = new DOMNode('node1');
			
			const subnode0 : IDOMNode = new DOMNode('subnode1');
			const subnode1 : IDOMNode = new DOMNode('subnode1');
			const subnode2 : IDOMNode = new DOMNode('subnode1');
			const subnode3 : IDOMNode = new DOMNode('subnode1');
			const subnode4 : IDOMNode = new DOMNode('subnode2');
			const subnode5 : IDOMNode = new DOMNode('subnode2');
			const subnode6 : IDOMNode = new DOMNode('subnode3');
			
			const subsubnode0 : IDOMNode = new DOMNode('subsubnode0');
			
			document.add(node0);
			document.add(node1);
			
			node0.add(subnode0);
			
			node1.add(subnode1);
			node1.add(subnode2);
			node1.add(subnode3);
			node1.add(subnode4);
			node1.add(subnode5);
			node1.add(subnode6);
			
			subnode0.add(subsubnode0);
			
			const result : Vector.<IDOMNode> = document.select('node1[1]/subnode1');
			assertEquals('Result length should be 3', 3, result.length);
		}
		
		[Test]
		public function path_select_node1_with_index1_then_subnode1_in_context() : void
		{
			const node0 : IDOMNode = new DOMNode('node1');
			const node1 : IDOMNode = new DOMNode('node1');
			
			const subnode0 : IDOMNode = new DOMNode('subnode1');
			const subnode1 : IDOMNode = new DOMNode('subnode1');
			const subnode2 : IDOMNode = new DOMNode('subnode1');
			const subnode3 : IDOMNode = new DOMNode('subnode1');
			const subnode4 : IDOMNode = new DOMNode('subnode2');
			const subnode5 : IDOMNode = new DOMNode('subnode2');
			const subnode6 : IDOMNode = new DOMNode('subnode3');
			
			const subsubnode0 : IDOMNode = new DOMNode('subsubnode0');
			
			document.add(node0);
			document.add(node1);
			
			node0.add(subnode0);
			
			node1.add(subnode1);
			node1.add(subnode2);
			node1.add(subnode3);
			node1.add(subnode4);
			node1.add(subnode5);
			node1.add(subnode6);
			
			subnode0.add(subsubnode0);
			
			const result : Vector.<IDOMNode> = document.select('/node1[1]/subnode1');
			assertEquals('Result length should be 3', 3, result.length);
		}
		
		[Test]
		public function path_select_node1_with_index1_then_subnode1_in_document() : void
		{
			const node0 : IDOMNode = new DOMNode('node1');
			const node1 : IDOMNode = new DOMNode('node1');
			
			const subnode0 : IDOMNode = new DOMNode('subnode1');
			const subnode1 : IDOMNode = new DOMNode('subnode1');
			const subnode2 : IDOMNode = new DOMNode('subnode1');
			const subnode3 : IDOMNode = new DOMNode('subnode1');
			const subnode4 : IDOMNode = new DOMNode('subnode2');
			const subnode5 : IDOMNode = new DOMNode('subnode2');
			const subnode6 : IDOMNode = new DOMNode('subnode3');
			
			const subsubnode0 : IDOMNode = new DOMNode('subsubnode0');
			
			document.add(node0);
			document.add(node1);
			
			node0.add(subnode0);
			
			node1.add(subnode1);
			node1.add(subnode2);
			node1.add(subnode3);
			node1.add(subnode4);
			node1.add(subnode5);
			node1.add(subnode6);
			
			subnode0.add(subsubnode0);
			
			const result : Vector.<IDOMNode> = document.select('//node1[1]/subnode1');
			assertEquals('Result length should be 3', 3, result.length);
		}
	}
}