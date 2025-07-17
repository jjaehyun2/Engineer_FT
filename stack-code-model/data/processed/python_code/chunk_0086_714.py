class events.DrySeasonEvent extends events.Event
{
   function DrySeasonEvent()
   {
      super();
      this.image = "dryseason1pic";
      this.title = _root.drySeasonEventTitle;
      this.description = _root.drySeasonEvDe;
      this.secDescription = _root.drySeasonEvDe2nd;
      trace(_root.drySeasonEvDe);
      mvcFarm.FarmModel.getModel().handle_event("Crop");
   }
}