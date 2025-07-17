class investments.Representative extends investments.Project
{
   function Representative()
   {
      super();
      this.setLinkageName("representative");
      this.setPrice(_root.representativePrice);
      this.setMultiplier(_root.representativeMultiplier);
   }
   function toString()
   {
      return "One representative investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}