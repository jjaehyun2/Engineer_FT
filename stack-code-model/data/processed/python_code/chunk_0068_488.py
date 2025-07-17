class events.CorruptOfficialsEvent extends events.Event
{
   function CorruptOfficialsEvent()
   {
      super();
      this.image = "corruptofficialspic";
      this.title = _root.corruptOfficialsEventTitle;
      this.description = _root.corruptOfficialsEvDe;
      this.secDescription = _root.corruptOfficialsEvDe2nd;
      mvcFarm.FarmModel.getModel().handle_event("corrupt");
   }
}