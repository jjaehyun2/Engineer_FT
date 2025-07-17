class mvcFarm.FarmInfo
{
   function FarmInfo(money, familyMembers, investments, family)
   {
      this.money = money;
      this.familyMembers = familyMembers;
      this.investments = investments;
      this.family = family;
   }
   function getMoney()
   {
      return this.money;
   }
   function getFamilyMembers()
   {
      return this.familyMembers;
   }
   function getInvestments()
   {
      return this.investments;
   }
   function getFamily()
   {
      return this.family;
   }
}