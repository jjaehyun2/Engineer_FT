class investments.Insurance extends investments.Project
{
   function Insurance()
   {
      super();
      this.setLinkageName("insurance");
      this.setPrice(_root.insurancePrice);
      this.setMultiplier(_root.insuranceMultiplier);
   }
   function toString()
   {
      return "One insurance investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}