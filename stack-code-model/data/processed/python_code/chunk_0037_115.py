package zpp_nape.util
{
   import nape.dynamics.ArbiterIterator;
   
   public class ZNPNode_ArbiterIterator extends Object
   {
      
      public function ZNPNode_ArbiterIterator()
      {
      }
      
      public static var zpp_pool:ZNPNode_ArbiterIterator;
      
      public var next:ZNPNode_ArbiterIterator;
      
      public var elt:ArbiterIterator;
   }
}