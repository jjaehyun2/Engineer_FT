class investments.Cotton extends investments.Crop
{
   function Cotton()
   {
      super();
      this.setLinkageName("cotton");
      this.setPrice(_root.cottonPrice);
      this.setMultiplier(_root.cottonMultiplier);
   }
   function toString()
   {
      return "One cotton investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}