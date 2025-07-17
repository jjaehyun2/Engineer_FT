package devoron.components.tables.nativecommands
{
	import devoron.components.darktable.DarkTableCellEditor;
	import devoron.components.decorators.ResizedGradientBackgroundDecorator;
	import devoron.components.icons.IconCellRenderer;
	import devoron.components.tables.DSTable;
	import devoron.components.tables.PathCellEditor;
	import devoron.components.tables.arrays.DefaultArrayCellEditor;
	import devoron.components.tables.icons.IconsTableChangeListener;
	import devoron.components.tables.nativecommands.NativeCommandsTableModel;
	import devoron.studio.core.project.processor.forms.ApplicationCellRenderer;
	import devoron.studio.tools.bookmarkmanager.CommentCellEditor;
	import devoron.studio.tools.bookmarkmanager.commands.editors.CommandCellEditor;
	import flash.geom.Matrix;
	import org.aswing.ASColor;
	import org.aswing.JTable;
	import org.aswing.border.SideLineBorder;
	import org.aswing.decorators.GradientBackgroundDecorator;
	import org.aswing.event.AWEvent;
	import org.aswing.table.GeneralTableCellFactory;
	
	public class NativeCommandsTable extends DSTable
	{
		private var actionsTableModel:NativeCommandsTableModel;
		
		public function NativeCommandsTable()
		{
			super();
			
			actionsTableModel = new NativeCommandsTableModel();
			setModel(actionsTableModel);
			setDefaultEditor("Icon", new PathCellEditor());
			setDefaultCellFactory("Icon", new GeneralTableCellFactory(IconCellRenderer));
			setDefaultEditor("Application", new PathCellEditor());
			setDefaultCellFactory("Application", new GeneralTableCellFactory(ApplicationCellRenderer));
			setDefaultEditor("String", new DarkTableCellEditor());
			setDefaultEditor("Comment", new CommentCellEditor());
			setDefaultEditor("Command", new CommandCellEditor());
			setDefaultEditor("Array", new DefaultArrayCellEditor());
			setRowHeight(48);
			//setDefaultEditor("Object", new DarkTableCompoundCellEditor());
			
			getSelectionModel().setSelectionMode(JTable.MULTIPLE_SELECTION);
			setColumnsResizable(false);
			
			var clr:uint = 0x000000;
			var colors:Array = [clr, clr, clr, clr, clr];
			var alphas:Array = [0.14, 0.08, 0.04, 0.02, 0.01];
			var ratios:Array = [0, 70, 145, 200, 255];
			var matrix:Matrix = new Matrix();
			matrix.createGradientBox(270, 19, 0, 0, 0);
			//super.getTableHeader().set
			var bg:ResizedGradientBackgroundDecorator = new ResizedGradientBackgroundDecorator(GradientBackgroundDecorator.LINEAR, colors, alphas, ratios, matrix, "pad", "rgb", 0, null, 0);
			//bg.setGaps(-1, 0, 4, 1); rltb
			bg.setGaps(0, 0, 0, 2);
			getTableHeader().setBackgroundDecorator(bg);
			
			getTableHeader().setBorder(new SideLineBorder(new SideLineBorder(null, SideLineBorder.WEST, new ASColor(0x000000, 0.14), 0.5), SideLineBorder.EAST, new ASColor(0x000000, 0.14), 0.5));
			// слушатель изменения значений для связи ячеек: функция - аргументы
			//getModel().addTableModelListener(new OmgEbala(this));
			
			// слушатель изменения значений в событий
			getModel().addTableModelListener(new IconsTableChangeListener(this));
			
			
		}
		
		
		public function getNativeCommands():Array
		{
			return actionsTableModel.getData();
		}
		
		public function setNativeCommands(paths:Array):void
		{
			actionsTableModel.setData(paths);
		}
	
	}
}