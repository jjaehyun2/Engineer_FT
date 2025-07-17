class investments.Harvester extends investments.Tool
{
   function Harvester()
   {
      super();
      this.setLinkageName("harvester");
      this.setPrice(_root.harvesterPrice);
      this.setMultiplier(_root.harvesterMultiplier);
   }
   function toString()
   {
      return "One harvester investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}