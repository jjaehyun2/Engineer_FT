package devoron.aslc.moduls.project 
{
	import devoron.components.multicontainers.table.ContainersAssetsControlPanel;
	/**
	 * ...
	 * @author ...
	 */
	public class TemplatesForm 
	{
		private var templatesCACP:ContainersAssetsControlPanel;
		
		public function TemplatesForm() 
		{
			// 5. шаблоны проекта
			if (!templatesCACP)
			{
				templatesCACP = new ContainersAssetsControlPanel("template");
				templatesCACP.setPreferredWidth(50);
			}
		}
		
	}

}