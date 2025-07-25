﻿package com.flashblocks.blocks {
    import com.flashblocks.blocks.args.ArgumentBlock;
    import com.flashblocks.blocks.render.BlockCapTop;
    import com.flashblocks.blocks.sockets.SocketType;
    import com.flashblocks.events.BlockConnectionEvent;
    import flash.display.DisplayObject;
    import flash.events.MouseEvent;
    import flash.filters.GlowFilter;
    import flash.utils.getQualifiedClassName;

    import mx.containers.Canvas;
    import mx.effects.Resize;
    import mx.events.PropertyChangeEvent;

    /**
     * ...
     * @author Trevor Rundell
     */

    [Event(name="dragStart", type="com.flashblocks.events.BlockDragEvent")]
    [Event(name="dragComplete", type="com.flashblocks.events.BlockDragEvent")]
    [Event(name="dragDrop", type="com.flashblocks.events.BlockDragEvent")]
    [Event(name="connect", type="com.flashblocks.events.BlockConnectionEvent")]
    [Event(name="disconnect", type="com.flashblocks.events.BlockConnectionEvent")]
    public class Block extends Canvas {

        protected var _socketType:String = SocketType.ROUND;
        protected var _blockType:String;
        protected var _blockName:String;
        protected var _blockColor:uint = 0x66FF66;
        protected var _blockValue:*;
        protected var _enableConnections:Boolean;
        protected var _highlight:Boolean;

        protected var _before:Block;
        protected var _after:Block;
        protected var _inner:Block;
        protected var _nested:Array;

        protected var dragging:Boolean = false;

        protected const HIGHLIGHT_FILTER:GlowFilter = new GlowFilter(0x00FFFF, 1.0, 2, 2, 255, 3, true);

        public function Block(blockName:String, blockValue:*=null) {
            super();

            this._blockName = blockName;
            this.blockValue = blockValue;
            this._nested = new Array();
            this.clipContent = false;

            setStyle("verticalGap", 0);

            addEventListener(MouseEvent.MOUSE_DOWN, onMouseDown);
            addEventListener(MouseEvent.MOUSE_UP, onMouseUp);
            addEventListener(MouseEvent.MOUSE_MOVE, onMouseMove);

            redraw();
        }

        public function redraw():void {
            // override
        }

        //
        // Bindable Getters / Setters
        //

        [Bindable(event="propertyChange")]
        public function get socketType():String { return _socketType; }

        public function set socketType(value:String):void {
            _socketType = value;
            redraw();
            dispatchEvent(new PropertyChangeEvent(PropertyChangeEvent.PROPERTY_CHANGE));
        }

        [Bindable(event="propertyChange")]
        public function get blockName():String { return _blockName; }

        [Bindable(event="propertyChange")]
        public function get blockType():String { return _blockType; }

        public function set blockType(value:String):void {
            _blockType = value;
            redraw();
            dispatchEvent(new PropertyChangeEvent(PropertyChangeEvent.PROPERTY_CHANGE));
        }

        [Bindable(event="propertyChange")]
        public function get blockColor():uint { return _blockColor; }

        public function set blockColor(value:uint):void {
            _blockColor = value;
            redraw();
            dispatchEvent(new PropertyChangeEvent(PropertyChangeEvent.PROPERTY_CHANGE));
        }

        [Bindable(event="propertyChange")]
        public function get blockValue():* { return _blockValue; }

        public function set blockValue(value:*):void {
            _blockValue = value;
            dispatchEvent(new PropertyChangeEvent(PropertyChangeEvent.PROPERTY_CHANGE));
        }

        // non-bindable properties

        public function get enableConnections():Boolean { return _enableConnections; }

        public function set enableConnections(value:Boolean):void {
            _enableConnections = value;
        }

        public function get highlight():Boolean {
            return _highlight;
        }

        public function set highlight(value:Boolean):void {
            _highlight = value;
        }

        public function get before():Block { return _before; }

        public function set before(value:Block):void {
            _before = value;
        }

        public function get after():Block { return _after; }

        public function set after(value:Block):void {
            _after = value;
        }

        public function get inner():Block { return _inner; }

        public function set inner(value:Block):void {
            _inner = value;
        }

        public function get nested():Array {
            return _nested;
        }

        //
        // CONTENT METHODS - Adding and removing content to a block. This
        //   includes argument blocks as well as any labels, text or icons.
        //

        public function addContent(content:DisplayObject):void {
            // override
        }

        public function removeContent(content:DisplayObject):void {
            // override
        }

        public function getContent():Array {
            return [ ];
        }

        public function addArgument(block:ArgumentBlock):void {
            // override
        }

        public function removeArgument(block:ArgumentBlock):void {
            // override
        }

        public function removeAllArguments():void {
            // override
        }

        public function getArguments():Array {
            return [ ]; // override
        }

        public function getArgument(i:uint=0):ArgumentBlock {
            return getArguments()[i];
        }

        //
        // PORT EXISTENCE TESTS -- Test if a block as a particular port.
        //
        //   Before Port -- Notch at top of block
        //   After Port -- Notch at bottom of block
        //   Nested Port -- Nested connection for control logic
        //   Inner Port -- Inner connection for arguments
        //

        public function hasBefore():Boolean {
            return false; // override
        }

        public function hasAfter():Boolean {
            return false; // override
        }

        public function hasInner():Boolean {
            return false; // override
        }

        public function numNested():uint {
            return nested.length; // override
        }

        public function numArguments():uint {
            return getArguments().length;
        }

        //
        // CONNECTION TESTS -- Test if two blocks are able to connect at
        //   specific ports. Some possible conditions for comparison are
        //   port locations, block position, current connections, socket
        //   types or custom connection rules.
        //

        public function testBeforeConnection(block:Block):Boolean {
            return false; // override
        }

        public function testAfterConnection(block:Block):Boolean {
            return false; // override
        }

        public function testInnerConnection(block:Block):Boolean {
            return false; // override
        }

        public function testNestedConnection(level:uint, block:Block):Boolean {
            return false; // override
        }

        //
        // CONNECTION METHODS -- Connect blocks together at specific ports.
        //

        public function connectBefore(block:Block):void {
            // override
        }

        public function connectAfter(block:Block):void {
            // override
        }

        public function connectInner(block:Block):void {
            // override
        }

        public function connectNested(level:uint, block:Block):void {
            // override
        }

        //
        // HOVER METHODS -- Preview block connections at specific ports.
        //

        public function overBefore(block:Block):void {
            // override
        }

        public function overAfter(block:Block):void {
            // override
        }

        public function overInner(block:Block):void {
            // override
        }

        public function overNested(level:uint, block:Block):void {
            // override
        }

        public function outBefore(block:Block):void {
            // override
        }

        public function outAfter(block:Block):void {
            // override
        }

        public function outInner(block:Block):void {
            // override
        }

        public function outNested(level:uint, block:Block):void {
            // override
        }

        public function outAll(block:Block):void {
            outBefore(block);
            outAfter(block);
            outInner(block);
            for (var i:uint = 0; i < numNested(); i++) {
                outNested(i, block);
            }
        }

        //
        // Dragging Methods
        //

        public function isDragging():Boolean {
            return dragging;
        }

        public function setDragging(value:Boolean):void {
            if (canDrag())
                dragging = value;
            if (value)
                dispatchEvent(new BlockConnectionEvent(BlockConnectionEvent.DISCONNECT));
        }

        public function canDrag():Boolean {
            return true; // override
        }

        public function canDrop(block:Block):Boolean {
            return false; // override
        }

        //
        // Utility Methods
        //

        public function cleanConnections(recursive:Boolean=false):void {
            cleanBeforeConnections(recursive);
            cleanAfterConnections(recursive);
            cleanInnerConnections(recursive);
            cleanNestedConnections(recursive);

            for each (var arg:ArgumentBlock in getArguments()) {
                arg.cleanConnections(recursive);
            }
        }

        public function cleanBeforeConnections(recursive:Boolean=false):void {
            if (before) {
                if (this.parent != before) {
                    before = null;
                }
            }
        }

        public function cleanAfterConnections(recursive:Boolean=false):void {
            if (after) {
                if (recursive) {
                    after.cleanConnections(true);
                }
                if (after.parent != this) {
                    after = null;
                }
            }
        }

        public function cleanInnerConnections(recursive:Boolean=false):void {
            if (inner) {
                if (recursive) {
                    inner.cleanConnections(true);
                }
                if (inner.parent != this) {
                    inner = null;
                }
            }
        }

        public function cleanNestedConnections(recursive:Boolean=false):void {
            for (var i:uint = 0; i < nested.length; i++) {
                if (nested[i]) {
                    if (recursive) {
                        nested[i].cleanConnections(true);
                    }
                    if (nested[i].parent != this) {
                        nested[i] = null;
                    }
                }
            }
        }

        public function toJSON():Object {
            var i:int;
            var o:Object = {
                name: blockName,
                value: blockValue
            };
            var args:Array = getArguments();
            if (args) {
                o.args = [];
                for (i = 0; i < numArguments(); i++) {
                    o.args[i] = args[i].toJSON();
                }
            }
            if (numNested() > 0) {
                o.nested = [];
                for (i = 0; i < numNested(); i++) {
                    if (nested[i]) {
                        o.nested[i] = nested[i].toJSON();
                    }
                }
            }
            if (inner) {
                o.inner = inner.toJSON();
            }
            if (after) {
                var afterJSON:Object = after.toJSON();
                if (afterJSON is Array) {
                    return [ o ].concat(afterJSON);
                } else {
                    return [ o , afterJSON ];
                }
            }
            return o;
        }

        //
        // MOUSE HANDLERS -- Prevents progagation of mouse events to avoid
        //   dragging a parent block when the child is being used.
        //

        private function onMouseMove(e:MouseEvent):void {
            e.stopPropagation();
        }

        private function onMouseUp(e:MouseEvent):void {
            e.stopPropagation();
        }

        private function onMouseDown(e:MouseEvent):void {
            e.stopPropagation();
        }
    }
}