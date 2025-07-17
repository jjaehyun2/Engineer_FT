class investments.Elephant extends investments.Livestock
{
   function Elephant()
   {
      super();
      this.setLinkageName("elephant");
      this.setPrice(_root.elephantPrice);
      this.setMultiplier(_root.elephantMultiplier);
   }
   function toString()
   {
      return "One elephant investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}