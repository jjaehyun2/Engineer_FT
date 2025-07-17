package devoron.components.multicontainers.table 
{
	import devoron.components.multicontainers.gridlist.ContainerGridListCell;
	/**
	 * ...
	 * @author Devoron
	 */
	public class ContainersGridListControlPanel 
	{
		
		public function ContainersGridListControlPanel() 
		{
			model = new VectorListModel();
			containersGridList = new GridList(model, new GeneralGridListCellFactory(ContainerGridListCell));
			containersGridList.addSelectionListener(selectContentViewListener);
			//containersGridListSP.addEventListener(
			//containersGridList.setTracksHeight(true);
			containersGridListSP = new JScrollPane(containersGridList, JScrollPane.SCROLLBAR_ALWAYS, JScrollPane.SCROLLBAR_NEVER);
			containersGridListSP.setPreferredSize(new IntDimension(267, 100));
			
			showContainersTableBtn = new JToggleButton("", new LoadIcon(GEOMETRY_ICON), showTable);
			showContainersTableBtn.addActionListener(showContainersTableBtnHandler);
			
			showContainersGridListBtn = new JToggleButton("", new LoadIcon(GEOMETRY_ICON), showTable);
			showContainersGridListBtn.addActionListener(showContainersGridListBtnHandler);
			
			var groupButtonsPanel:JPanel = new JPanel(new FlowLayout(FlowLayout.LEFT, 2));
			for (var i:int = 0; i < 10; i++)
			{
				groupButtonsPanel.append(new JToggleButton("", new LoadIcon(GEOMETRY_ICON), false), FlowLayout.LEFT)
			}
			
			addItemBtn = new CircleButton("");
			addItemBtn.setPreferredSize(new IntDimension(30, 30));
			addItemBtn.setMaximumSize(new IntDimension(30, 30));
			
			circleMenu = new CircleMenu();
			circleMenu.addEventListener(AWEvent.HIDDEN, onHidden);
			circleMenu.addActionListener(circleMenuSelectionHandler);
			
			addItemBtn.setRelatedObject(circleMenu, AWEvent.SHOWN, showMenu, AWEvent.HIDDEN, circleMenu.hide);
			
			//showFullFormBtn = new JToggleButton(dataContainerType, null, true);
			showFullFormBtn = new JToggleButton("", new AssetIcon(new preferencesIcon), true);
			//showFullFormBtn.setMaximumHeight(22);
			showFullFormBtn.setIconTextGap(0);
			showFullFormBtn.addActionListener(showFullFormBtnHandler);
			
			var jp:JPanel = new JPanel(new BorderLayout());
			jp.setPreferredWidth(270);
			jp.setWidth(270);
			//jp.setPreferredHeight(
			jp.setMinimumWidth(270);
			
			var jp3:JPanel = new JPanel(new VerticalCenterLayout());
			dcf = new DataContainersForm();
			var bb:JDropDownButton = new JDropDownButton(dataContainerType, null, false, dcf);
			bb.setPopupAlignment(JDropDownButton.RIGHT);
			bb.setForeground(new ASColor(0xFFFFFF, 0.8));
			//bb.setFont(bb.getFont().changeBold(true));
			bb.setFont(bb.getFont().changeUnderline(true));
			bb.setBackgroundDecorator(null);
			bb.setPreferredWidth(100);
			//jp3.appendAll(new DSLabel(dataContainerType), showFullFormBtn);
			jp3.appendAll(bb);
			
			var jp4:JPanel = new JPanel(new VerticalCenterLayout());
			var jp5:JPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
			jp5.appendAll( /*addItemBtn,*/ /*showContainersGridListBtn, */showContainersTableBtn);
			jp4.append(jp5);
			
			selectedLB = new JToggleButton("");
			
			var jp2:JPanel = new JPanel(new VerticalCenterLayout());
			jp2.append(selectedLB);
			
			jp.append(jp3, BorderLayout.WEST);
			jp.append(jp2, BorderLayout.CENTER);
			jp.append(jp4, BorderLayout.EAST);
			
			/*var jp6:JPanel = new JPanel(new VerticalCenterLayout());
			   jp6.append(addItemBtn);
			
			   var jp2:JPanel = new JPanel(new HorizontalCenterLayout());
			 jp2.append(jp6);*/
			//var jp2:JPanel = new JPanel(new CenterLayout());
			//jp2.append(addItemBtn);
			
			//jp.append(jp2, BorderLayout.CENTER);
			//super.addLeftHoldRow(0, showFullFormBtn, showContainersTableBtn);
			super.addLeftHoldRow(0, jp);
			//super.addCenterHoldRow(0, showFullFormBtn, addItemBtn, showContainersTableBtn);
			//super.addLeftHoldRow(0, containersGridListSP);
		}
		
	}

}