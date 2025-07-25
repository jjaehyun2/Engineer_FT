package nape.phys
{
   import zpp_nape.phys.ZPP_Material;
   import nape.shape.ShapeList;
   import zpp_nape.util.ZPP_ShapeList;
   import flash._-2v;
   
   public class Material extends Object
   {
      
      public function Material(param1:Number = 0.0, param2:Number = 1.0, param3:Number = 2.0, param4:Number = 1, param5:Number = 0.01)
      {
         if(_-2v._-7E)
         {
            return;
         }
         if(ZPP_Material.zpp_pool == null)
         {
            zpp_inner = new ZPP_Material();
         }
         else
         {
            zpp_inner = ZPP_Material.zpp_pool;
            ZPP_Material.zpp_pool = zpp_inner.next;
            zpp_inner.next = null;
         }
         null;
         zpp_inner.outer = this;
         if(param1 != zpp_inner.elasticity)
         {
            zpp_inner.elasticity = param1 / 1;
            zpp_inner.invalidate(ZPP_Material.WAKE | ZPP_Material.ARBITERS);
         }
         zpp_inner.elasticity;
         if(param2 != zpp_inner.dynamicFriction)
         {
            zpp_inner.dynamicFriction = param2 / 1;
            zpp_inner.invalidate(ZPP_Material.WAKE | ZPP_Material.ANGDRAG | ZPP_Material.ARBITERS);
         }
         zpp_inner.dynamicFriction;
         if(param3 != zpp_inner.staticFriction)
         {
            zpp_inner.staticFriction = param3 / 1;
            zpp_inner.invalidate(ZPP_Material.WAKE | ZPP_Material.ARBITERS);
         }
         zpp_inner.staticFriction;
         if(param4 != zpp_inner.density * 1000)
         {
            zpp_inner.density = param4 / 1000;
            zpp_inner.invalidate(ZPP_Material.WAKE | ZPP_Material.PROPS);
         }
         zpp_inner.density * 1000;
         if(param5 != zpp_inner.rollingFriction)
         {
            zpp_inner.rollingFriction = param5 / 1;
            zpp_inner.invalidate(ZPP_Material.WAKE | ZPP_Material.ARBITERS);
         }
         zpp_inner.rollingFriction;
      }
      
      public static function wood() : Material
      {
         return new Material(0.4,0.2,0.38,0.7,0.005);
      }
      
      public static function steel() : Material
      {
         return new Material(0.2,0.57,0.74,7.8,0.001);
      }
      
      public static function ice() : Material
      {
         return new Material(0.3,0.03,0.1,0.9,1.0E-4);
      }
      
      public static function rubber() : Material
      {
         return new Material(0.8,1.0,1.4,1.5,0.01);
      }
      
      public static function glass() : Material
      {
         return new Material(0.4,0.4,0.94,2.6,0.002);
      }
      
      public static function sand() : Material
      {
         return new Material(-1.0,0.45,0.6,1.6,16.0);
      }
      
      public var zpp_inner:ZPP_Material;
      
      public function toString() : String
      {
         return "{ elasticity: " + zpp_inner.elasticity + " dynamicFriction: " + zpp_inner.dynamicFriction + " staticFriction: " + zpp_inner.staticFriction + " density: " + zpp_inner.density * 1000 + " rollingFriction: " + zpp_inner.rollingFriction + " }";
      }
      
      public function set staticFriction(param1:Number) : Number
      {
         if(param1 != zpp_inner.staticFriction)
         {
            zpp_inner.staticFriction = param1 / 1;
            zpp_inner.invalidate(ZPP_Material.WAKE | ZPP_Material.ARBITERS);
         }
         return zpp_inner.staticFriction;
      }
      
      public function set rollingFriction(param1:Number) : Number
      {
         if(param1 != zpp_inner.rollingFriction)
         {
            zpp_inner.rollingFriction = param1 / 1;
            zpp_inner.invalidate(ZPP_Material.WAKE | ZPP_Material.ARBITERS);
         }
         return zpp_inner.rollingFriction;
      }
      
      public function set elasticity(param1:Number) : Number
      {
         if(param1 != zpp_inner.elasticity)
         {
            zpp_inner.elasticity = param1 / 1;
            zpp_inner.invalidate(ZPP_Material.WAKE | ZPP_Material.ARBITERS);
         }
         return zpp_inner.elasticity;
      }
      
      public function set dynamicFriction(param1:Number) : Number
      {
         if(param1 != zpp_inner.dynamicFriction)
         {
            zpp_inner.dynamicFriction = param1 / 1;
            zpp_inner.invalidate(ZPP_Material.WAKE | ZPP_Material.ANGDRAG | ZPP_Material.ARBITERS);
         }
         return zpp_inner.dynamicFriction;
      }
      
      public function set density(param1:Number) : Number
      {
         if(param1 != zpp_inner.density * 1000)
         {
            zpp_inner.density = param1 / 1000;
            zpp_inner.invalidate(ZPP_Material.WAKE | ZPP_Material.PROPS);
         }
         return zpp_inner.density * 1000;
      }
      
      public function get userData() : *
      {
         if(zpp_inner.userData == null)
         {
            zpp_inner.userData = {};
         }
         return zpp_inner.userData;
      }
      
      public function get staticFriction() : Number
      {
         return zpp_inner.staticFriction;
      }
      
      public function get shapes() : ShapeList
      {
         if(zpp_inner.wrap_shapes == null)
         {
            zpp_inner.wrap_shapes = ZPP_ShapeList.get(zpp_inner.shapes,true);
         }
         return zpp_inner.wrap_shapes;
      }
      
      public function get rollingFriction() : Number
      {
         return zpp_inner.rollingFriction;
      }
      
      public function get elasticity() : Number
      {
         return zpp_inner.elasticity;
      }
      
      public function get dynamicFriction() : Number
      {
         return zpp_inner.dynamicFriction;
      }
      
      public function get density() : Number
      {
         return zpp_inner.density * 1000;
      }
      
      public function copy() : Material
      {
         var _loc1_:Material = new Material(zpp_inner.elasticity,zpp_inner.dynamicFriction,zpp_inner.staticFriction,zpp_inner.density * 1000,zpp_inner.rollingFriction);
         _loc1_.zpp_inner.userData = zpp_inner.userData;
         return _loc1_;
      }
   }
}