class investments.Shovel extends investments.Tool
{
   function Shovel()
   {
      super();
      this.setLinkageName("shovel");
      this.setPrice(_root.shovelPrice);
      this.setMultiplier(_root.shovelMultiplier);
   }
   function toString()
   {
      return "One shovel investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}