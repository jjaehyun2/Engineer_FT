package eu.stefaner.relationbrowser.layout {
	import eu.stefaner.relationbrowser.ui.Edge;
	import eu.stefaner.relationbrowser.ui.Node;

	import flare.util.Shapes;
	import flare.vis.data.DataSprite;
	import flare.vis.data.NodeSprite;
	import flare.vis.data.render.ArrowType;
	import flare.vis.data.render.EdgeRenderer;

	import flash.display.Graphics;
	import flash.geom.Point;

	/**
	 * @author mo
	 */
	public class RelationBrowserEdgeRenderer extends EdgeRenderer {
		private static const ROOT3 : Number = Math.sqrt(3);
		public static var CURVE_ALL_EDGES : Boolean;
		public static var CURVE_SCALE : Number = 1.1;
		public static var CURVE_SCALE_RADIUS : Number = 800;

		public function RelationBrowserEdgeRenderer() {
		}

		private static var _instance : RelationBrowserEdgeRenderer = new RelationBrowserEdgeRenderer();

		/** Static EdgeRenderer instance. */
		public static function get instance() : EdgeRenderer {
			return _instance;
		}

		// temporary variables
		private var _p : Point = new Point(), _q : Point = new Point();
		private var _pts : Array = new Array(20);

		/** @inheritDoc */
		override public function render(d : DataSprite) : void {
			var e : Edge = d as Edge;
			if (e == null) {
				return;
			}
			// TODO: throw exception?
			var s : NodeSprite = e.source;
			var t : NodeSprite = e.target;
			var g : Graphics = e.graphics;
			var ctrls : Array = e.points as Array;

			var x1 : Number = e.x1, y1 : Number = e.y1;
			var x2 : Number = e.x2, y2 : Number = e.y2;

			if (e.source.shape == Shapes.BLOCK) {
				e.x1 = x1 = e.source.u + e.source.w * .5;
				e.y1 = y1 = e.source.v + e.source.h * .5;
			}
			if (e.target.shape == Shapes.BLOCK) {
				e.x2 = x2 = e.target.u + e.target.w * .5;
				e.y2 = y2 = e.target.v + e.target.h * .5;
			}

			var xL : Number = ctrls == null ? x1 : ctrls[ctrls.length - 2];
			var yL : Number = ctrls == null ? y1 : ctrls[ctrls.length - 1];
			var dx : Number, dy : Number, dd : Number;
			// cuvred lines for outer edges: should be configurable!
			//var curved : Boolean = CURVE_ALL_EDGES || t.props.distance == 2 || s.props.distance == 2;
			var curved : Boolean = CURVE_ALL_EDGES || e.curved;
			// modify end points as needed to accomodate arrow
			if (e.arrowType != ArrowType.NONE && e.directed) {
				// determine arrow head size
				var ah : Number = e.arrowHeight, aw : Number = e.arrowWidth / 2;
				if (ah < 0 && aw < 0) aw = 1.5 * e.lineWidth;
				if (ah < 0) {
					ah = ROOT3 * aw;
				} else if (aw < 0) {
					aw = ah / ROOT3;
				}
				// temp endpoint
				_p.x = x2;
				_p.y = y2;
				// get unit vector along arrow line
				dx = _p.x - xL;
				dy = _p.y - yL;
				dd = Math.sqrt(dx * dx + dy * dy);
				dx /= dd;
				dy /= dd;
				// look for edge radius property, otherwsie use half width
				var tRad : Number;
				if (t is Node) {
					tRad = (t as Node).edgeRadius;
				} else {
					tRad = t.width * .5;
				}
				var sRad : Number;
				if (s is Node) {
					sRad = (s as Node).edgeRadius;
				} else {
					sRad = s.width * .5;
				}
				// move endpoint half the width of target node to center
				_p.x -= tRad * dx;
				_p.y -= tRad * dy;
				// move startpoint half the width of source node to center
				x1 += sRad * dx;
				y1 += sRad * dy;
				// set final point positions
				var dd2 : Number = e.lineWidth / 2;
				// if drawing as lines, offset arrow tip by half the line width
				if (e.arrowType == ArrowType.LINES) {
					_p.x -= dd2 * dx;
					_p.y -= dd2 * dy;
					dd2 += e.lineWidth;
				}
				// offset the anchor point (the end point for the edge connector)
				// so that edge doesn't "overshoot" the arrow head
				dd2 = ah - dd2;
				x2 = _p.x - dd2 * dx;
				y2 = _p.y - dd2 * dy;
			} else {
				// just do edge radius thing
				// temp endpoint
				_p.x = x2;
				_p.y = y2;
				// get unit vector along arrow line
				dx = _p.x - xL;
				dy = _p.y - yL;
				dd = Math.sqrt(dx * dx + dy * dy);
				dx /= dd;
				dy /= dd;

				// look for edge radius property, otherwsie use half width
				if (t is Node) {
					tRad = (t as Node).edgeRadius;
				} else {
					tRad = t.width * .5;
				}

				if (s is Node) {
					sRad = (s as Node).edgeRadius;
				} else {
					sRad = s.width * .5;
				}

				// adjust startpoint and endpoint
				x1 += sRad * dx;
				y1 += sRad * dy;
				x2 -= tRad * dx;
				y2 -= tRad * dy;
			}

			// insert curve
			if (curved) {
				var diffX : Number = x2 - x1;
				var diffY : Number = y2 - y1;
				var scaleFactor : Number = 1 + CURVE_SCALE * (Math.sqrt(diffX * diffX + diffY * diffY) / CURVE_SCALE_RADIUS);
				ctrls = [e.origin.x + scaleFactor * (x1 + diffX * .5 - e.origin.x), e.origin.y + scaleFactor * (y1 + diffY * .5 - e.origin.y)];
			} else {
				ctrls = null;
			}

			if (e.props.isBidirectional) {
				// draw only one half
				x1 = x1 + (x2 - x1) * .5;
				y1 = y1 + (y2 - y1) * .5;
			}

			// draw the edge
			g.clear();

			// draw a triangle
			if (e.arrowType == ArrowType.TAPERED) {
				g.lineStyle();
				g.beginFill(e.lineColor, e.lineAlpha);

				// width at source
				var sw : Number;
				// width at target
				var tw : Number;

				// e.props.directionBalance = 0 -> fully expressed at source
				// e.props.directionBalance = 0.5 -> balanced
				// e.props.directionBalance = 1 -> fully expressed at target

				if (e.props.directionBalance != null) {
					sw = 2 * (1 - e.props.directionBalance) * e.lineWidth;
					tw = 2 * e.props.directionBalance * e.lineWidth;
				} else {
					sw = 1.5 * e.lineWidth;
					tw = .5 * e.lineWidth;
				}

				if (curved) {
					var sourceNormal : Point = getNormal(ctrls[0] - x1, ctrls[1] - y1, new Point(x1, y1));
					var midNormal : Point = getNormal(dx, dy, new Point(ctrls[0], ctrls[1]));
					var targetNormal : Point = getNormal(ctrls[0] - x2, ctrls[1] - y2, new Point(x2, y2));

					g.moveTo(x1 - sw * sourceNormal.x, y1 - sw * sourceNormal.y);
					g.lineTo(x1 + sw * sourceNormal.x, y1 + sw * sourceNormal.y);
					g.curveTo(ctrls[0] + midNormal.x * (sw + tw) * .5, ctrls[1] + midNormal.y * (sw + tw) * .5, x2 + tw * targetNormal.x, y2 + tw * targetNormal.y);
					g.lineTo(x2 - tw * targetNormal.x, y2 - tw * targetNormal.y);
					g.curveTo(ctrls[0] - midNormal.x * (sw + tw) * .5, ctrls[1] - midNormal.y * (sw + tw) * .5, x1 - sw * sourceNormal.x, y1 - sw * sourceNormal.y);
					g.endFill();

					/*
					// debug
					g.moveTo(x1 - sw * sourceNormal.x, y1 - sw * sourceNormal.y);
					g.lineTo(x1 + sw * sourceNormal.x, y1 + sw * sourceNormal.y);
					g.lineTo(x2 + tw * targetNormal.x, y2 + tw * targetNormal.y);
					g.lineTo(x2 - tw * targetNormal.x, y2 - tw * targetNormal.y);
					g.endFill();
					 * 
					 */
				} else {
					var normal : Point = getNormal(dx, dy);

					g.moveTo(x1 - sw * normal.x, y1 - sw * normal.y);
					g.lineTo(x1 + sw * normal.x, y1 + sw * normal.y);
					g.lineTo(x2 + tw * normal.x, y2 + tw * normal.y);
					g.lineTo(x2 - tw * normal.x, y2 - tw * normal.y);
					g.endFill();
				}
				return;
			}

			setLineStyle(e, g);
			// set the line style
			g.moveTo(x1, y1);

			if (ctrls != null) {
				g.curveTo(ctrls[0], ctrls[1], x2, y2);
			} else {
				g.lineTo(x2, y2);
			}

			if (e.arrowType != ArrowType.NONE && e.directed) {
				// get other arrow points
				x1 = _p.x - ah * dx + aw * dy;
				y1 = _p.y - ah * dy - aw * dx;
				x2 = _p.x - ah * dx - aw * dy;
				y2 = _p.y - ah * dy + aw * dx;

				if (e.arrowType == ArrowType.TRIANGLE) {
					g.lineStyle();
					g.moveTo(_p.x, _p.y);
					g.beginFill(e.lineColor, e.lineAlpha);
					g.lineTo(x1, y1);
					g.lineTo(x2, y2);
					g.endFill();
				} else if (e.arrowType == ArrowType.LINES) {
					g.moveTo(x1, y1);
					g.lineTo(_p.x, _p.y);
					g.lineTo(x2, y2);
				}
			}
		}

		private function getNormal(dx : Number, dy : Number, ref : Point = null) : Point {
			var normal : Point = new Point(dy, -dx);
			normal.normalize(1);
			if (ref) {
				if (new Point(ref.x + normal.x, ref.y + normal.y).length < new Point(ref.x - normal.x, ref.y - normal.y).length) {
					normal.x *= -1;
					normal.y *= -1;
				}
			}

			return normal;
		}
	}
}