class investments.Wheat extends investments.Crop
{
   function Wheat()
   {
      super();
      this.setLinkageName("wheat");
      this.setPrice(_root.wheatPrice);
      this.setMultiplier(_root.wheatMultiplier);
   }
   function toString()
   {
      return "One wheat investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}