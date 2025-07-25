package io.decagames.rotmg.pets.commands {
   import com.company.assembleegameclient.editor.Command;
   import io.decagames.rotmg.pets.data.PetsModel;
   
   public class DeletePetCommand extends Command {
       
      
      [Inject]
      public var petID:int;
      
      [Inject]
      public var petsModel:PetsModel;
      
      public function DeletePetCommand() {
         super();
      }
      
      override public function execute() : void {
         this.petsModel.deletePet(this.petID);
      }
   }
}