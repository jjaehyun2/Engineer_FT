class events.ChickenDiseaseEvent extends events.Event
{
   function ChickenDiseaseEvent()
   {
      super();
      this.image = "deadchickens1pic";
      this.title = _root.chickenDiseaseEventTitle;
      this.description = _root.chickenDiseaseEvDe;
      this.secDescription = _root.chickenDiseaseEvDe2nd;
      mvcFarm.FarmModel.getModel().handle_event("chicken");
   }
}