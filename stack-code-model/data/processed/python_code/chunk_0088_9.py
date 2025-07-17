package de.dittner.siegmar.view.common.form {
import de.dittner.async.IAsyncOperation;
import de.dittner.siegmar.model.domain.fileSystem.file.SiegmarFile;

public interface IBodyForm {
	function createNote(file:SiegmarFile):IAsyncOperation;
	function editNote(file:SiegmarFile):IAsyncOperation;
	function removeNote(file:SiegmarFile):IAsyncOperation;
	function clear():void;
}
}