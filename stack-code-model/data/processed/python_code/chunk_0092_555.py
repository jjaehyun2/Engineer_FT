package devoron.aslc.moduls.output
{
	import devoron.components.buttons.DSButton;
	import devoron.components.textfields.DSTextArea;
	import devoron.studio.core.managers.output.stack.view.StackTraceListCellRenderer;
	import devoron.dataui.DataContainerForm;
	import devoron.components.labels.DSLabel;
	import devoron.components.labels.TitleLabel;
	import devoron.studio.moduls.code.tools.resultslist.CompilerMessagesList;
	import org.aswing.ASColor;
	import org.aswing.AssetIcon;
	import org.aswing.event.AWEvent;
	import org.aswing.ext.Form;
	import org.aswing.GeneralListCellFactory;
	import org.aswing.geom.IntDimension;
	import org.aswing.Icon;
	import org.aswing.JLabel;
	import org.aswing.JList;
	import org.aswing.JPanel;
	import org.aswing.JScrollPane;
	import org.aswing.layout.FlowLayout;
	import org.aswing.VectorListModel;
	
	/**
	 * OutputForm
	 * @author Devoron
	 */
	public class OutputForm extends DataContainerForm
	{
		[Embed(source="../../../../../assets/icons/commons/output_icon20.png")]
		private const OUTPUT_ICON20:Class;
		private static var msgTA:DSTextArea;
		
		public static var stackTraceList:JList;
		public var messagesModel:VectorListModel = new VectorListModel();
		public static var stackTraceModel:VectorListModel = new VectorListModel();
		
		public function OutputForm(dataContainerName:String = "", dataContainerType:String = "", dataContainerIcon:Icon = null, dataCollectionMode:String = DataContainerForm.SINGLE_COMPONENT_DATA_COLLECTION, dataLiveMode:Boolean = false)
		{
			super(dataContainerName, dataContainerType, new AssetIcon(new OUTPUT_ICON20), dataCollectionMode, dataLiveMode);
			
			//var lb:JLabel = new DSLabel("Output");
			//lb.setFont(lb.getFont().changeSize(14));
			//super.addLeftHoldRow(0, lb);
			
			var btn1:DSButton = new DSButton("M", null, null, 20, 20);
			var btn2:DSButton = new DSButton("W", null, null, 20, 20);
			var btn3:DSButton = new DSButton("E", null, null, 20, 20);
			super.addRightHoldRow(0, btn1, btn2, btn3);
			
			super.addLeftHoldRow(0, createMessagesOutputFieldForm());
			//super.addLeftHoldRow(0, [0,5]);
			//super.addLeftHoldRow(0, createStackTraceForm());
			var pan:JPanel = new JPanel(new FlowLayout());
			//hash = new HashMap();
		/*	for each (var item:DataContainerForm in modulComponents)
		   {
		   var btn:AboutButton = new AboutButton(item.dataContainerName);
		   btn.setPreferredWidth(200);
		   pan.append(btn);
		   bg.append(btn);
		   hash.put(item.dataContainerName, item);
		   btn.setEnabled(true);
		   //bg
		
		
		   }
		 */
		
		/*	var lb:JLabel = new DSLabel("Settings");
		   lb.setFont(lb.getFont().changeSize(14));
		   addLeftHoldRow(0, lb);
		
		   addLeftHoldRow(0, pan);
		   contentContainer = new JPanel();
		 addLeftHoldRow(0, contentContainer);*/
		
		}
		
		private function onAct(e:AWEvent):void
		{
		/*	var form:DataContainerForm = hash.get(bg.getSelectedButtonText()) as DataContainerForm;
		   if (form) {
		   contentContainer.removeAll();
		   contentContainer.append(form);
		   contentContainer.pack();
		
		 }*/
		}
		
		public static function log(text:String):void
		{
			if (msgTA)
				msgTA.appendText(text+"\n");
			//msgTA.append(text);
			//msgTA
		}
		
		private function createMessagesOutputFieldForm():Form
		{
			var messagesForm:Form = new Form();
			var messagesLB:TitleLabel = new TitleLabel("Messages list");
			//messagesLB.setBackgroundDecorator(new ColorDecorator(new ASColor(0xFFFFFF, 0.08), new ASColor(0x000000, 0)));
			messagesLB.setPreferredWidth(1000);
			messagesForm.addLeftHoldRow(0, messagesLB);
			//outputPanels.setPreferredSize(new IntDimension(1000, 150));
			
			//messagesModel = new VectorListModel();
			msgTA = new DSTextArea();
			//msgList.setModel(messagesModel);
			//msgList.setPreferredCellWidthWhenNoCount(980);
			//windowsTP.appendTab(msgList, "Results");
			//msgList.setPreferredSize(new IntDimension(600, 150));
			
			var messagesListJsP:JScrollPane = new JScrollPane(msgTA, JScrollPane.SCROLLBAR_ALWAYS, JScrollPane.SCROLLBAR_AS_NEEDED);
			messagesListJsP.getHorizontalScrollBar().setEnabled(false);
			//outputTAScP.setPreferredSize(new IntDimension(600, 180));
			//messagesListJsP.setPreferredSize(new IntDimension(1000, 600));
			messagesListJsP.setPreferredSize(new IntDimension(1000, 300));
			
			messagesForm.addLeftHoldRow(0, messagesListJsP);
			//messagesForm.setPreferredSize(new IntDimension(850, 200));
			messagesLB.setRelatedComponent(messagesForm);
			return messagesForm;
			//messagesForm.setBackgroundDecorator(new ColorDecorator(new ASColor(0x000000, 0), new ASColor(0xFFFFFF, 0.14)));
			//txt = new JTextArea();
		
		/*txt.setBackgroundDecorator(new ColorDecorator(new ASColor(0x000000, 0), new ASColor(0x000000, 0)));
		   txt.setForeground(new ASColor(0xFFFFFF, 0.54));
		   bTabs.appendTab(txt,"Reference");
		   var under:String = 'Under construction :D\n\nBut, come on, why don\'t YOU do it? ' + 'Piece of cake, it\'s Actionscript!';
		 txt.setText(under);*/
		}
		
		private function createMessagesListForm():Form
		{
			var messagesForm:Form = new Form();
			var messagesLB:TitleLabel = new TitleLabel("Messages list");
			//messagesLB.setBackgroundDecorator(new ColorDecorator(new ASColor(0xFFFFFF, 0.08), new ASColor(0x000000, 0)));
			messagesLB.setPreferredWidth(1000);
			messagesForm.addLeftHoldRow(0, messagesLB);
			//outputPanels.setPreferredSize(new IntDimension(1000, 150));
			
			//messagesModel = new VectorListModel();
			var msgList:CompilerMessagesList = new CompilerMessagesList;
			msgList.setModel(messagesModel);
			msgList.setPreferredCellWidthWhenNoCount(980);
			//windowsTP.appendTab(msgList, "Results");
			//msgList.setPreferredSize(new IntDimension(600, 150));
			
			var messagesListJsP:JScrollPane = new JScrollPane(msgList, JScrollPane.SCROLLBAR_ALWAYS, JScrollPane.SCROLLBAR_AS_NEEDED);
			messagesListJsP.getHorizontalScrollBar().setEnabled(false);
			//outputTAScP.setPreferredSize(new IntDimension(600, 180));
			messagesListJsP.setPreferredSize(new IntDimension(1000, 300));
			
			messagesForm.addLeftHoldRow(0, messagesListJsP);
			//messagesForm.setPreferredSize(new IntDimension(850, 200));
			messagesLB.setRelatedComponent(messagesForm);
			return messagesForm;
			//messagesForm.setBackgroundDecorator(new ColorDecorator(new ASColor(0x000000, 0), new ASColor(0xFFFFFF, 0.14)));
			//txt = new JTextArea();
		
		/*txt.setBackgroundDecorator(new ColorDecorator(new ASColor(0x000000, 0), new ASColor(0x000000, 0)));
		   txt.setForeground(new ASColor(0xFFFFFF, 0.54));
		   bTabs.appendTab(txt,"Reference");
		   var under:String = 'Under construction :D\n\nBut, come on, why don\'t YOU do it? ' + 'Piece of cake, it\'s Actionscript!';
		 txt.setText(under);*/
		}
		
		private function createStackTraceForm():Form
		{
			var form:Form = new Form();
			var messagesLB:TitleLabel = new TitleLabel("Stack trace");
			//messagesLB.setBackgroundDecorator(new ColorDecorator(new ASColor(0xFFFFFF, 0.08), new ASColor(0x000000, 0)));
			messagesLB.setPreferredWidth(1000);
			//messagesLB.setRelatedComponent(messagesForm);
			form.addLeftHoldRow(0, messagesLB);
			form.addLeftHoldRow(0, createStackTraceList());
			return form;
		}
		
		public function setStackTraceModel(model:VectorListModel):void
		{
			stackTraceModel = model;
		}
		
		public function getStackTraceModel():VectorListModel
		{
			return stackTraceModel;
		}
		
		public function createStackTraceList():JScrollPane
		{
			var stackTraceListSpR:JScrollPane;
			
			//if (!stackTraceList)
			//{
			//fchsTableModel = new FileChooserHelpersTableModel(null);
			stackTraceModel = new VectorListModel();
			//errorsList = new JList(["ByteArrayHexdump", "JSONParser", "StageUtil", "StatsOutputUtil", "SystemInfoUtil","StatsOutputUtil", "SystemInfoUtil","StatsOutputUtil", "SystemInfoUtil","StatsOutputUtil", "SystemInfoUtil","StatsOutputUtil", "SystemInfoUtil", "MediaTesterUtil", "RemoteDebugger", "ByteArrayHexdump", "JSONParser", "StageUtil", "StatsOutputUtil", "SystemInfoUtil", "MediaTesterUtil", "RemoteDebugger"]);
			stackTraceList = new JList(stackTraceModel);
			stackTraceList.setForeground(new ASColor(0xFFFFFF, 0.45));
			stackTraceList.setSelectionBackground(new ASColor(0x000000, 0.14));
			stackTraceList.setSelectionForeground(new ASColor(0XFFFFFF, 0.65));
			stackTraceList.setPreferredCellWidthWhenNoCount(980);
			//stackTraceList.setPreferredCellWidthWhenNoCount(800);
			stackTraceList.setCellFactory(new GeneralListCellFactory(StackTraceListCellRenderer, true, true, 20));
			//errorsModel.addListDataListener(onListDataChange);
			//stackTraceModel.addListDataListener(this);
			//scriptsListSP = new JScrollPane(scriptsList);
			//errorsList.setPreferredHeight(400);
			//stackTraceList.setSize(new IntDimension(980, 200));
			//fchsTableSP.setMinimumSize(new IntDimension(200, 100));
			
			/*scriptsListSP.setVerticalScrollBarPolicy(JScrollPane.SCROLLBAR_ALWAYS);
			   scriptsListSP.setHorizontalScrollBarPolicy(JScrollPane.SCROLLBAR_NEVER);
			 scriptsListSP.buttonMode = true;*/
			//}
			//super.addLeftHoldRow(0, mobsListPane);	
			stackTraceListSpR = new JScrollPane(stackTraceList, JScrollPane.SCROLLBAR_ALWAYS, JScrollPane.SCROLLBAR_AS_NEEDED);
			stackTraceListSpR.setSize(new IntDimension(1000, 300));
			stackTraceListSpR.setPreferredSize(new IntDimension(1000, 300));
			//stackTraceListSpR.setMinimumSize(new IntDimension(600, 200));
			return stackTraceListSpR;
		}
	
	}

}