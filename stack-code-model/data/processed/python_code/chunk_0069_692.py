class events.MarketPricesEvent extends events.Event
{
   function MarketPricesEvent()
   {
      super();
      this.image = "containershippic";
      this.title = _root.marketPricesEventTitle;
      this.description = _root.marketPricesEvDe;
      this.secDescription = _root.marketPricesEvDe2nd;
      mvcFarm.FarmModel.getModel().handle_event("marketprices");
   }
}