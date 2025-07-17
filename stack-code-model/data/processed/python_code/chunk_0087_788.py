package devoron.components.pcfs
{
	import devoron.components.pcfs.PathChooserForm;
	
	/**
	 * ImagePCF
	 * @author Devoron
	 */
	public class ImagePCF extends PathChooserForm
	{
		public function ImagePCF(title:String, listener:Function = null)
		{
			super(title);
			setExtensions(["jpg", "jpeg", "png", "gif"]);
			setFileSelectionMode(PathChooserForm.FILES_ONLY);
			if (listener != null)
				addActionListener(listener);
		}
	
	}

}