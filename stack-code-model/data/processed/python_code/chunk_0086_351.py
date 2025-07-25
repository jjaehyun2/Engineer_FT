package visuals.ui.elements.item
{
   import com.playata.framework.display.Sprite;
   import com.playata.framework.display.lib.flash.FlashDisplayObjectContainer;
   import com.playata.framework.display.lib.flash.FlashLabel;
   import com.playata.framework.display.lib.flash.FlashSprite;
   import com.playata.framework.display.ui.controls.ILabel;
   import flash.display.MovieClip;
   import visuals.ui.elements.icons.SymbolIconCriticalHitRatingGeneric;
   import visuals.ui.elements.icons.SymbolIconDodgeRatingGeneric;
   import visuals.ui.elements.icons.SymbolIconStaminaGeneric;
   import visuals.ui.elements.icons.SymbolIconStrengthGeneric;
   import visuals.ui.elements.icons.SymbolIconWeaponDamageGeneric;
   
   public class SymbolItemTooltipSetInfoStatGeneric extends Sprite
   {
       
      
      private var _nativeObject:SymbolItemTooltipSetInfoStat = null;
      
      public var txtParts:ILabel = null;
      
      public var iconWeaponDamage:SymbolIconWeaponDamageGeneric = null;
      
      public var iconBrawn:SymbolIconStrengthGeneric = null;
      
      public var iconBrain:SymbolIconCriticalHitRatingGeneric = null;
      
      public var iconAwareness:SymbolIconDodgeRatingGeneric = null;
      
      public var iconToughness:SymbolIconStaminaGeneric = null;
      
      public var txtStat:ILabel = null;
      
      public function SymbolItemTooltipSetInfoStatGeneric(param1:MovieClip = null)
      {
         if(param1)
         {
            _nativeObject = param1 as SymbolItemTooltipSetInfoStat;
         }
         else
         {
            _nativeObject = new SymbolItemTooltipSetInfoStat();
         }
         super(null,FlashSprite.fromNative(_nativeObject));
         var _loc2_:FlashDisplayObjectContainer = _sprite as FlashDisplayObjectContainer;
         txtParts = FlashLabel.fromNative(_nativeObject.txtParts);
         iconWeaponDamage = new SymbolIconWeaponDamageGeneric(_nativeObject.iconWeaponDamage);
         iconBrawn = new SymbolIconStrengthGeneric(_nativeObject.iconBrawn);
         iconBrain = new SymbolIconCriticalHitRatingGeneric(_nativeObject.iconBrain);
         iconAwareness = new SymbolIconDodgeRatingGeneric(_nativeObject.iconAwareness);
         iconToughness = new SymbolIconStaminaGeneric(_nativeObject.iconToughness);
         txtStat = FlashLabel.fromNative(_nativeObject.txtStat);
      }
      
      public function setNativeInstance(param1:SymbolItemTooltipSetInfoStat) : void
      {
         FlashSprite.setNativeInstance(_sprite,param1);
         _nativeObject = param1;
         syncInstances();
      }
      
      public function syncInstances() : void
      {
         FlashLabel.setNativeInstance(txtParts,_nativeObject.txtParts);
         if(_nativeObject.iconWeaponDamage)
         {
            iconWeaponDamage.setNativeInstance(_nativeObject.iconWeaponDamage);
         }
         if(_nativeObject.iconBrawn)
         {
            iconBrawn.setNativeInstance(_nativeObject.iconBrawn);
         }
         if(_nativeObject.iconBrain)
         {
            iconBrain.setNativeInstance(_nativeObject.iconBrain);
         }
         if(_nativeObject.iconAwareness)
         {
            iconAwareness.setNativeInstance(_nativeObject.iconAwareness);
         }
         if(_nativeObject.iconToughness)
         {
            iconToughness.setNativeInstance(_nativeObject.iconToughness);
         }
         FlashLabel.setNativeInstance(txtStat,_nativeObject.txtStat);
      }
   }
}