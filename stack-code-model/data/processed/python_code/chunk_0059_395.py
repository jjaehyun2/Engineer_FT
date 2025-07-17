class investments.Communications extends investments.Project
{
   function Communications()
   {
      super();
      this.setLinkageName("communications");
      this.setPrice(_root.communicationsPrice);
      this.setMultiplier(_root.communicationsMultiplier);
   }
   function toString()
   {
      return "One communications investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}