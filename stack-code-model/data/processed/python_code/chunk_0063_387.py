class investments.Chicken extends investments.Livestock
{
   function Chicken()
   {
      super();
      this.setLinkageName("chicken");
      this.setPrice(_root.chickenPrice);
      this.setMultiplier(_root.chickenMultiplier);
   }
   function toString()
   {
      return "One chicken investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}