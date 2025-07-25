package zpp_nape.geom
{
   import nape.geom.GeomVertexIterator;
   import flash._-2v;
   
   public class ZPP_GeomVertexIterator extends Object
   {
      
      public function ZPP_GeomVertexIterator()
      {
         if(_-2v._-7E)
         {
            return;
         }
         outer = new GeomVertexIterator();
      }
      
      public static var zpp_pool:ZPP_GeomVertexIterator;
      
      public static function get(param1:ZPP_GeomVert, param2:Boolean) : GeomVertexIterator
      {
         var _loc3_:* = null as ZPP_GeomVertexIterator;
         if(ZPP_GeomVertexIterator.zpp_pool == null)
         {
            _loc3_ = new ZPP_GeomVertexIterator();
         }
         else
         {
            _loc3_ = ZPP_GeomVertexIterator.zpp_pool;
            ZPP_GeomVertexIterator.zpp_pool = _loc3_.next;
            _loc3_.next = null;
         }
         null;
         _loc3_.outer.zpp_inner = _loc3_;
         _loc3_.ptr = param1;
         _loc3_.forward = param2;
         _loc3_.start = param1;
         _loc3_.first = !(param1 == null);
         return _loc3_.outer;
      }
      
      public var start:ZPP_GeomVert;
      
      public var ptr:ZPP_GeomVert;
      
      public var outer:GeomVertexIterator;
      
      public var next:ZPP_GeomVertexIterator;
      
      public var forward:Boolean;
      
      public var first:Boolean;
   }
}