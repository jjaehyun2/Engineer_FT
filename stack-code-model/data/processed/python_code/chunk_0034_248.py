package zpp_nape.util
{
   import nape.geom.RayResult;
   
   public class ZNPNode_RayResult extends Object
   {
      
      public function ZNPNode_RayResult()
      {
      }
      
      public static var zpp_pool:ZNPNode_RayResult;
      
      public var next:ZNPNode_RayResult;
      
      public var elt:RayResult;
   }
}