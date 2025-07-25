package net.psykosoft.psykopaint2.core.drawing.brushes.shapes
{
	import flash.display.Stage3D;
	import flash.display3D.Context3D;
	
	import net.psykosoft.psykopaint2.base.remote.PsykoSocket;
	import net.psykosoft.psykopaint2.core.configuration.CoreSettings;
	
	public class BrushShapeLibrary
	{
		[Inject]
		public var stage3D : Stage3D;

		private var _shapes : Object;

		public function BrushShapeLibrary()
		{
			_shapes = {};
		}

		public function init() : void
		{
			registerDefaultShapes(stage3D.context3D);
		}
		
		public function dispose() : void
		{
			for ( var id:String in _shapes )
			{
				_shapes[id].dispose();
			}
			_shapes = {};
		}

		private function registerDefaultShapes(context3D : Context3D) : void
		{
			//SPRAYCAN USES: NoisyBrushShape2.NAME,
			/*	AlmostCircularRoughShape.NAME,
				BasicCircularShape.NAME,
				SplatterSprayShape.NAME,
				SplatterSprayShape.NAME,
				EraserBrushShape.NAME*/
			//PENCIL USES: 
			/*	DotsBrushShape.NAME,
				LineBrushShape.NAME,
				PencilSketchBrushShape.NAME,
				PencilSketchBrushShape.NAME,
				PaintBrushShape1.NAME,
				PaintBrushShape1.NAME,
				EraserBrushShape.NAME*/
			//BRISTLE BRUSH
			/*	PaintBrushShape1.NAME,
				PaintbrushShape.NAME,
				SplotchBrushShape.NAME,
				PaintBrushShape1.NAME*/
			//WATERCOLOR
			/*	WetBrushShape2.NAME,
				WetBrushShape.NAME,
				AlmostCircularHardShape.NAME*/
			//PAINTGUN
			/*	InkSplatsShape.NAME,
				SplatsShape.NAME,
				SprayShape.NAME,
				CrayonShape.NAME,
				SplotchBrushShape.NAME,
				SplotchBrushShape.NAME,
				EraserBrushShape.NAME*/
			//SPRAYCAN
			registerShape(new AlmostCircularRoughShape(context3D));
			registerShape(new BasicCircularShape(context3D));
			registerShape(new EraserBrushShape(context3D));
			registerShape(new SplatterSprayShape(context3D));
			registerShape(new NoisyBrushShape2(context3D));


			registerShape(new DotsBrushShape(context3D));
			registerShape(new LineBrushShape(context3D));
			registerShape(new PencilSketchBrushShape(context3D));
			registerShape(new PaintBrushShape1(context3D));

			registerShape(new PaintbrushShape(context3D));
			registerShape(new SplotchBrushShape(context3D));
			
			//WATERCOLOR
			registerShape(new WetBrushShape(context3D));
			registerShape(new WetBrushShape2(context3D));
			registerShape(new AlmostCircularHardShape(context3D));
			
			registerShape(new InkSplatsShape(context3D));
			registerShape(new SplatsShape(context3D));
			registerShape(new SprayShape(context3D));
			registerShape(new CrayonShape(context3D));

			
			/*
			
			registerShape(new BasicBrushShape(context3D));
			registerShape(new BasicSmoothBrushShape(context3D));
			registerShape(new DotBrushShape(context3D));
			registerShape(new LineBrushShape(context3D));
			registerShape(new PaintbrushShape(context3D));
			registerShape(new PencilSketchBrushShape(context3D));
			registerShape(new RenderTextureBrushShape(context3D));
			registerShape(new ScalesBrushShape(context3D));
			registerShape(new SplatBrushShape(context3D));
			registerShape(new SumiShape(context3D));
			registerShape(new VarnishBrushShape(context3D));
			registerShape(new VectorSplatShape(context3D));
			
			
			//disabled unused shapes
			
			registerShape(new SquareBrushShape(context3D));
			registerShape(new SquareSmoothBrushShape(context3D));
			
			registerShape(new PencilBrushShape(context3D));
			registerShape(new SplatBrushShape2(context3D));
			registerShape(new DotBrushShape(context3D));
			registerShape(new InkDotShape1(context3D));
			registerShape(new ObjectTestShape1(context3D));
			registerShape(new AntialiasedTriangleBrushShape(context3D));
			registerShape(new PrecisionTestShape(context3D));
			registerShape(new SphereBrushShape(context3D));
			
			*/
			if ( CoreSettings.ENABLE_PSYKOSOCKET_CONNECTION )
			{
				sendAvailableShapes();
				PsykoSocket.addMessageCallback("BrushShapeLibrary.*",this, onSocketMessage );
			}
		}

		public function registerShape(shape : AbstractBrushShape) : void
		{
			if (_shapes[shape.id]) {
				trace("Brush shape with id '" + shape.id + "' already registered");
				//	throw "Brush shape with id '" + shape.id + "' already registered";
			}else {
				_shapes[shape.id] = shape;
			}
		}

		public function getBrushShape(id : String) : AbstractBrushShape
		{
			if ( id == null ) return null;
			if (!_shapes[id]) throw "No brush shape with id '" + id + "' registered";
			return _shapes[id];
		}
		
		
		private function sendAvailableShapes():void
		{
			var answer:XML = <msg src="BrushShapeLibrary.sendAvailableShapes" />;
			for ( var id:String in _shapes )
			{
				answer.appendChild(<shape id={id} />);
			}
			PsykoSocket.sendString( answer.toXMLString() );
		}
		
		private function onSocketMessage( message:XML):void
		{
			var target:String = String( message.@target ).split(".")[1];
			switch ( target )
			{
				case "getAvailableShapes":
					sendAvailableShapes();
					break;
			}
		}
	}
}