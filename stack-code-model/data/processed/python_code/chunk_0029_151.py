package devoron.aslc.moduls.project.recent 
{
	import devoron.dataui.DataStructursTableModel;
	import devoron.dataui.DataStructursTable;
	import org.aswing.JTable;
	import org.aswing.table.DefaultTableModel;
	/**
	 * ProjectsTable
	 * @author Devoron
	 */
	public class ProjectsTable extends DataStructursTable
	{
		
		public function ProjectsTable(dataName:String = "data", model:DefaultTableModel = null, dataStructurClass:Class = null)
		{
			//this.dataName = dataName;
			var dataStructursTableModel:DataStructursTableModel = new DataStructursTableModel([]);
			//dataStructursTableModel.getN
			super(dataStructursTableModel, dataStructurClass);
			setTableHeader(null);
			
			// здесь я тестирую данные
			dataStructursTableModel.setData([generateNewValue(), generateNewValue(), generateNewValue()]);
			
			setSelectionMode(JTable.MULTIPLE_SELECTION);
			
			//getTableHeader().setPreferredWidth(900);;q
			//setSelectionMode(JTable.MULTIPLE_SELECTION);
		/*	dataStructursTableSelectionModel = dataStructursTable.getSelectionModel();
			dataStructursTable.addSelectionListener(dataTableSelectionHandler);
			dataStructursTable.addEventListener(TableCellEditEvent.EDITING_STOPPED, onEditingStoped);
			dataStructursTableScP = new JScrollPane(dataStructursTable, JScrollPane.SCROLLBAR_ALWAYS, JScrollPane.SCROLLBAR_NEVER);
			dataStructursTableScP.getHorizontalScrollBar().setEnabled(false);
			dataStructursTableScP.setPreferredSize(new IntDimension(267, 180));
			var tableForm:Form = new Form();
			tableForm.addLeftHoldRow(0, dataStructursTableScP);
			
			var addDataStructurBtn:JButton = createButton("add " + dataName, addDataStructurBtnHandler);
			var removeDataStructurBtn:JButton = createButton("remove", removeDataStructurBtnHandler);
			var copyDataStructurBtn:JButton = createButton("copy", copyDataStructurBtnHandler);
			tableForm.addLeftHoldRow(0, addDataStructurBtn, 3, removeDataStructurBtn, 3, copyDataStructurBtn);
			
			var composite:Form = new Form();
			var tableFR:FormRow = composite.addLeftHoldRow(0, tableForm);
			
			modulForm.addLeftHoldRow(0, composite)
			return composite;*/
		}
		
		public function setProjects(projects:Array):void
		{
			setDataStructurs(projects);
		}
		
		public function getProjects():Array
		{
			return getDataStructurs();
		}
		
	}

}