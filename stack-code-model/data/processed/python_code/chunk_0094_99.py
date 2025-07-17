package devoron.components.multicontainers.table 
{
	/**
	 * ...
	 * @author Devoron
	 */
	public class ContainersComboBoxControlPanel 
	{
		
		public function ContainersComboBoxControlPanel() 
		{
			containerTypesCB = new GrayCB();
			containerTypesCB.setPreferredSize(new IntDimension(180, 24));
			//containerTypesCB.addActionListener(containerTypesCBChangeHandler);
			showContainersTableBtn = new JToggleButton("", new LoadIcon(GEOMETRY_ICON), showTable);
			showContainersTableBtn.addActionListener(showContainersTableBtnHandler);
			
			//showFullFormBtn = new DataContainerTitleLabel(dataContainerType, null, JLabel.LEFT, containersTableFR);
			//showFullFormBtn.setPreferredSize(null);
			
			//showFullFormBtn = new JToggleButton(dataContainerType, null, JLabel.LEFT, containersTableFR);
			
			showFullFormBtn = new JToggleButton(dataContainerType, null, true);
			showFullFormBtn.setIconTextGap(0);
			showFullFormBtn.addActionListener(showFullFormBtnHandler);
			//showFullFormBtn.tgb.setVisible(false);
			//showFullFormBtn.removeChild(tgb);
			//showContainersTableBtn.setRelatedDataContainer(dataContainer);
			
			super.addLeftHoldRow(0, showFullFormBtn, 5, containerTypesCB, showContainersTableBtn);
		}
		
	}

}