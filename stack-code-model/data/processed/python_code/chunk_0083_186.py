class investments.Corn extends investments.Crop
{
   function Corn()
   {
      super();
      this.setLinkageName("corn");
      this.setPrice(_root.cornPrice);
      this.setMultiplier(_root.cornMultiplier);
   }
   function toString()
   {
      return "One corn investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}