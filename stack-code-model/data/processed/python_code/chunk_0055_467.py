package zpp_nape.util
{
   import nape.phys.CompoundIterator;
   
   public class ZNPNode_CompoundIterator extends Object
   {
      
      public function ZNPNode_CompoundIterator()
      {
      }
      
      public static var zpp_pool:ZNPNode_CompoundIterator;
      
      public var next:ZNPNode_CompoundIterator;
      
      public var elt:CompoundIterator;
   }
}