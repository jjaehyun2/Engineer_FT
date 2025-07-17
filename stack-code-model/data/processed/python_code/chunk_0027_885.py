class investments.Investment
{
   static var idCount = 0;
   var id = 1;
   function Investment(positionMC)
   {
      this.setPositionMC(this.positionMC);
      this.id = investments.Investment.idCount;
      investments.Investment.idCount = investments.Investment.idCount + 1;
   }
   function setCategoryName(categoryName)
   {
      this.categoryName = categoryName;
   }
   function getCategoryName()
   {
      return this.categoryName;
   }
   function setLinkageName(linkageName)
   {
      this.linkageName = linkageName;
   }
   function getLinkageName()
   {
      return this.linkageName;
   }
   function setPrice(price)
   {
      this.price = price;
   }
   function getPrice()
   {
      return this.price;
   }
   function setAmount(amount)
   {
      this.amount = amount;
   }
   function getAmount()
   {
      return this.amount;
   }
   function setMultiplier(multiplier)
   {
      this.multiplier = multiplier;
   }
   function getMultiplier()
   {
      return this.multiplier;
   }
   function setPositionMC(positionMC)
   {
      this.positionMC = positionMC;
   }
   function getPositionMC()
   {
      return this.positionMC;
   }
   function paint()
   {
      var _loc3_ = _root.investmentTarget.attachMovie(this.getLinkageName(),this.getLinkageName(),this.getPositionMC()._y * 10);
      _loc3_._x = this.positionMC._x;
      _loc3_._y = this.positionMC._y;
   }
   function toString()
   {
   }
}