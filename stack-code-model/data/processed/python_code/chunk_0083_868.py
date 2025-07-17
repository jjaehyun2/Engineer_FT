class events.WellCavesInEvent extends events.Event
{
   function WellCavesInEvent()
   {
      super();
      this.image = "wellscaveinpic";
      this.title = _root.wellCavesInEventTitle;
      this.description = _root.wellCavesInEvDe;
      this.secDescription = _root.wellCavesInEvDe2nd;
      mvcFarm.FarmModel.getModel().handle_event("wellscavein");
   }
}