package zpp_nape.util
{
   import nape.constraint.ConstraintIterator;
   
   public class ZNPNode_ConstraintIterator extends Object
   {
      
      public function ZNPNode_ConstraintIterator()
      {
      }
      
      public static var zpp_pool:ZNPNode_ConstraintIterator;
      
      public var next:ZNPNode_ConstraintIterator;
      
      public var elt:ConstraintIterator;
   }
}