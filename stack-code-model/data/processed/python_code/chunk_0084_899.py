package devoron.components.pcfs 
{
	import devoron.components.pcfs.PathChooserForm;
	/**
	 * SwfPCF
	 * @author Devoron
	 */
	public class SwfPCF extends PathChooserForm
	{
		public function SwfPCF(title:String, listener:Function) 
		{
			super(title);
			setExtensions(["swf"]);
			setFileSelectionMode(PathChooserForm.FILES_ONLY);
			addActionListener(listener);
		}
		
	}

}