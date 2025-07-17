class investments.Barn extends investments.Construction
{
   function Barn()
   {
      super();
      this.setLinkageName("barn");
      this.setPrice(_root.barnPrice);
      this.setMultiplier(_root.barnMultiplier);
   }
   function toString()
   {
      return "One barn investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}