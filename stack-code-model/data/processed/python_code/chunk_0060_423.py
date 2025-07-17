package devoron.components.filechooser.contentviews
{
	import devoron.components.filechooser.renderers.FileCellRenderer;
	import devoron.file.FileInfo;
	import flash.events.MouseEvent;
	import garbage.FileGridListCell;
	import org.aswing.AssetIcon;
	import org.aswing.Component;
	import org.aswing.JList;
	import org.aswing.JScrollPane;
	import org.aswing.VectorListModel;
	import org.aswing.event.ListItemEvent;
	import org.aswing.ext.GeneralGridListCellFactory;
	import org.aswing.ext.GridList;
	import org.aswing.geom.IntDimension;
	
	/**
	 * FIsGridForm
	 * @author Devoron
	 */
	public class FIsGridForm extends BaseFIsContentViewForm
	{
		//[Embed(source = "../../../../../assets/icons/FileChooser/grid_icon16.png")]
		[Embed(source="../../../../../assets/icons/commons/view_mode_grid_list_icon20.png")]
		private var GRID_ICON16:Class;
		private var filesPane:JScrollPane;
		private var filesList:GridList;
		private var filesModel:VectorListModel;
		
		public function FIsGridForm()
		{
			//super.setLayout(
			//setIcon(new AssetIcon(new GRID_ICON16));
			setName("Grid");
			append(createIconButton(new AssetIcon(new GRID_ICON16), "Grid"));
			//setName("Grid");
			createFileInfosList();
		}
		
		override public function getViewFIComponent():Component
		{
			return filesPane;
		}
		
		override protected function selectFile(fileName:String):void
		{
			//super.selectFile(name);
			
			var files:Array = (filesList.getModel() as VectorListModel).toArray();
			var file:FileInfo;
			var exists:Boolean = false;
			for each (file in files)
			{
				if (file.name == fileName)
				{
					exists = true;
					break;
				}
			}
			
			if (exists)
			{
				filesList.setSelectedValue(file);
			}
		
		/*while ((files[i] as FileInfo).name != name) {
		
		   }*/
		}
		
		private function selectFiles(... objects):void
		{
			//objects.length
			// распарсить все объекты по типа
			// к каждой последовательности типов должна быть привязка определённой функции
			//var types:Array = 
		}
		
		protected function createFileInfosList():void
		{
			filesModel = new VectorListModel();
			
			//filesList = new GridList(filesModel, new GeneralGridListCellFactory(FileGridListCell), 4, 8);
			filesList = new GridList(filesModel, new GeneralGridListCellFactory(FileGridListCell), 13, 5);
			filesList.doubleClickEnabled = true;
			filesList.addEventListener(ListItemEvent.ITEM_DOUBLE_CLICK, onDoubleClick);
			//filesList.addSelectionListener(selectContentViewListener);
			filesList.setTileWidth(160);
			filesList.setTileHeight(140);
			
			filesList.setVGap(5);
			filesList.setHGap(5);
			
			//filesList.setPreferredCellWidthWhenNoCount(280);
			//filesList.setPreferredCellWidthWhenNoCount(80);
			//filesList.addSelectionListener(filesListSelectionHandler);
			filesList.setSelectionMode(JList.SINGLE_SELECTION);
			
			filesPane = new JScrollPane(filesList);
			filesPane.setPreferredHeight(300);
			filesPane.setSize(new IntDimension(490, 300));
			filesPane.setMinimumSize(new IntDimension(490, 300));
			filesPane.setPreferredSize(new IntDimension(490, 300));
			filesPane.setVerticalScrollBarPolicy(JScrollPane.SCROLLBAR_ALWAYS);
			//filesPane.setHorizontalScrollBarPolicy(JScrollPane.SCROLLBAR_AS_NEEDED);
			filesPane.setHorizontalScrollBarPolicy(JScrollPane.SCROLLBAR_ALWAYS);
			//filesPane.buttonMode = true;
		}
		
		override public function clear():void
		{
			(filesList.getModel() as VectorListModel).clear();
		}
		
		/*private function selectContentViewListener(e:AWEvent):void
		   {
		   contentView = e.currentTarget as IContentView;
		   viewComp = contentView.getViewFIComponent();
		   dispatchEvent(new Event(Event.CHANGE));
		   }*/
		
		private function onDoubleClick(e:ListItemEvent):void
		{
			dispatchEvent(new FIContentViewEvent(FIContentViewEvent.ITEM_DOUBLE_CLICK, e.getValue(), e.clone() as MouseEvent));
		}
		
		override public function setData(dataArray:Array):void
		{
			data = dataArray;
			filesModel.clear();
			filesModel.appendAll(dataArray);
			filesList.updateUI();
		}
		
		override public function getData():Array
		{
			return filesModel.toArray();
		}
		
		override public function setFilesModel(model:VectorListModel):void
		{
			//super.setFilesModel(model);
			//filesList.setModel(null);
			filesModel = model;
			filesList.setModel(model);
			//filesList.revalidate();
			filesList.updateUI();
		}
		
		override public function getSelectedValue():*
		{
			return filesList.getSelectedValue();
		}
	
	}

}