class events.TheftEvent extends events.Event
{
   function TheftEvent()
   {
      super();
      this.image = "theftpic";
      this.title = _root.theftEventTitle;
      this.description = _root.theftEvDe;
      this.secDescription = _root.theftEvDe2nd;
      mvcFarm.FarmModel.getModel().handle_event("theft");
   }
}