package net.psykosoft.psykopaint2.paint.commands.saving.sync
{

	import eu.alebianco.robotlegs.utils.impl.AsyncCommand;
	
	import net.psykosoft.psykopaint2.core.io.CanvasPPPISerializer;
	import net.psykosoft.psykopaint2.core.model.CanvasModel;
	import net.psykosoft.psykopaint2.core.model.UserPaintSettingsModel;
	import net.psykosoft.psykopaint2.core.models.SavingProcessModel;
	import net.psykosoft.psykopaint2.core.rendering.CanvasRenderer;
	import net.psykosoft.psykopaint2.core.views.debug.ConsoleView;

	public class SerializeIPPCommand extends AsyncCommand
	{
		[Inject]
		public var saveVO : SavingProcessModel;

		[Inject]
		public var canvasRenderer:CanvasRenderer;

		[Inject]
		public var canvas:CanvasModel;

		[Inject]
		public var paintSettings : UserPaintSettingsModel;

		override public function execute() : void
		{
			ConsoleView.instance.log( this, "execute()" );

			var dateMs:Number = new Date().getTime();
			
			if ( saveVO.paintingId == null ) saveVO.paintingId = "psyko-" + dateMs
			var paintingDate:Number = Number( saveVO.paintingId.split( "-" )[ 1 ] );
			// eww:
			if (isNaN(paintingDate))
				saveVO.paintingId = "psyko-" + dateMs;

			var serializer:CanvasPPPISerializer = new CanvasPPPISerializer();
			saveVO.infoBytes = serializer.serialize(saveVO.paintingId, paintingDate, canvas, canvasRenderer, paintSettings, saveVO.dataBytes);
			dispatchComplete(true);
		}
	}
}