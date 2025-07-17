class investments.School extends investments.Project
{
   function School()
   {
      super();
      this.setLinkageName("school");
      this.setPrice(_root.schoolPrice);
      this.setMultiplier(_root.schoolMultiplier);
   }
   function toString()
   {
      return "One school investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}