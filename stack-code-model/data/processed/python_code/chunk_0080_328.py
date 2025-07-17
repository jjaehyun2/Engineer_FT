class investments.Clinic extends investments.Project
{
   function Clinic()
   {
      super();
      this.setLinkageName("clinic");
      this.setPrice(_root.clinicPrice);
      this.setMultiplier(_root.clinicMultiplier);
   }
   function toString()
   {
      return "One clinic investment, positionMC = " + this.getPositionMC() + " linkage: " + this.getLinkageName() + " Price: " + this.getPrice() + "$";
   }
}