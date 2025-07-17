class investments.Well extends investments.Construction
{
   function Well()
   {
      super();
      this.setLinkageName("well");
      this.setPrice(_root.wellPrice);
      this.setMultiplier(_root.wellMultiplier);
   }
   function toString()
   {
      return "One Well investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}