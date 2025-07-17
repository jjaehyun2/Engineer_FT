class investments.Scythe extends investments.Tool
{
   function Scythe()
   {
      super();
      this.setLinkageName("scythe");
      this.setPrice(_root.scythePrice);
      this.setMultiplier(_root.scytheMultiplier);
   }
   function toString()
   {
      return "One scythe investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}