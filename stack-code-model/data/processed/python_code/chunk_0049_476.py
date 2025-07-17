class events.CottonFailedEvent extends events.Event
{
   function CottonFailedEvent()
   {
      super();
      this;
      this.image = "cotton-failed-eventpic";
      this.title = _root.cottonFailedEventTitle;
      this.description = _root.cottonFailedEvDe;
      this.secDescription = _root.cottonFailedEvDe2nd;
      mvcFarm.FarmModel.getModel().handle_event("cotton");
   }
}