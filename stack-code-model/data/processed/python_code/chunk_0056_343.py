package devoron.components.multicontainers.table 
{
	/**
	 * ...
	 * @author Devoron
	 */
	public class ContainersButtonsControlPanel 
	{
		
		public function ContainersButtonsControlPanel() 
		{
			buttonsPanel = new JPanel();
			buttonsPanel.setWidth(200);
			/*for (var i:int = 0; i < 8; i++)
			   {
			   var ad:AboutButton = new AboutButton("Крутой скрипт" + String(i), null);
			   bg.append(ad);
			   //dsfa.append(a);
			 }*/
			
			buttonsGroup = new ButtonGroup();
			buttonsSP = new JScrollPane(buttonsPanel, JScrollPane.SCROLLBAR_NEVER, JScrollPane.SCROLLBAR_ALWAYS);
			buttonsSP.setPreferredWidth(100);
			//buttonsSP = new ButtonsViewport(buttonsPanel);
			//buttonsSP.setPreferredWidth(200);
			
			/*	containerTypesCB = new GrayCB();
			   containerTypesCB.setPreferredSize(new IntDimension(180, 24));
			 containerTypesCB.addActionListener(containerTypesCBChangeHandler);*/
			showContainersTableBtn = new JToggleButton("", new LoadIcon(GEOMETRY_ICON), showTable);
			showContainersTableBtn.addActionListener(showContainersTableBtnHandler);
			
			showFullFormBtn = new JToggleButton(dataContainerType, null, true);
			showFullFormBtn.setIconTextGap(0);
			showFullFormBtn.addActionListener(showFullFormBtnHandler);
			
			super.addLeftHoldRow(0, showFullFormBtn, 5, buttonsSP, showContainersTableBtn);
		}
		
		private function dataContainerButtonHandler(e:AWEvent):void
		{
			//var scriptPath:String = (e.currentTarget as ScriptButton)
			//AirMediator.currentMode::getFile(scriptPath, onScriptRead, true, errorHandler);
			
			if (!containersTable)
				return;
			
			var selId:int = containersTable.getSelectedRow();
			
			// если объект не выбран, то ничего предпринимать не следует
			if (selId == -1)
				return;
			
			currentContainerIdSDC.setData(selId);
			
			//var containerType:String = containerTypesCB.getSelectedItem();
			
			var containerType:String = (buttonsGroup as ButtonGroup).getSelectedButtonText();
			var containerData:Object = defaultDataFactory.getData(containerType);
			currentContainerForm = containerForms.get(containerType);
			
			if (currentContainerForm)
			{
				(currentContainerFR.getComponent(0) as Container).removeAll();
				(currentContainerFR.getComponent(0) as Container).append(currentContainerForm);
				currentContainerForm.setDataToContainer(containerData);
				
				//var dataObjects:Array = containersTable.getData();
				dataObjects.splice(selId, 1, {name: dataObjects[selId].name, data: {id: currentContainerForm.dataContainerName, data: containerData}});
				containersTable.setData(dataObjects);
				containersTable.getSelectionModel().setSelectionInterval(selId, selId);
			}
		
		}
		
			private function appendContainerButton(path:String, icon:Icon):ScriptButton
		{
			var btn:ScriptButton = new ScriptButton(path, "", dataContainerButtonHandler);
			btn.setIcon(icon);
			buttonsPanel.append(btn);
			buttonsGroup.append(btn);
			return btn;
		}
		
	}

}