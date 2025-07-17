class investments.Peanut extends investments.Crop
{
   function Peanut()
   {
      super();
      this.setLinkageName("peanut");
      this.setPrice(_root.peanutPrice);
      this.setMultiplier(_root.peanutMultiplier);
   }
   function toString()
   {
      return "One peanut investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}