package devoron.components.pcfs 
{
	import devoron.components.pcfs.PathChooserForm;
	/**
	 * TextPCF
	 * @author Devoron
	 */
	public class TextPCF extends PathChooserForm
	{
		
		public function TextPCF(title:String, listener:Function) 
		{
			super(title);
			setExtensions(["txt"]);
			setFileSelectionMode(PathChooserForm.FILES_ONLY);
			addActionListener(listener);
		}
		
	}

}