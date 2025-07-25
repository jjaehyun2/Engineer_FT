package com.company.assembleegameclient.ui.panels.itemgrids {
import com.company.assembleegameclient.objects.GameObject;
import com.company.assembleegameclient.objects.ObjectLibrary;
import com.company.assembleegameclient.objects.Player;
import com.company.assembleegameclient.parameters.Parameters;
import com.company.assembleegameclient.ui.panels.itemgrids.itemtiles.InteractiveItemTile;

import flash.utils.getTimer;

public class ContainerGrid extends ItemGrid {


    private const NUM_SLOTS:uint = 8;

    public function ContainerGrid(gridOwner:GameObject, currentPlayer:Player) {
        var tile:InteractiveItemTile = null;
        super(gridOwner, currentPlayer, 0);
        this.tiles = new Vector.<InteractiveItemTile>(this.NUM_SLOTS);
        for (var i:int = 0; i < this.NUM_SLOTS; i++) {
            tile = new InteractiveItemTile(i + indexOffset, this, interactive);
            addToGrid(tile, 2, i);
            this.tiles[i] = tile;
        }
    }
    private var tiles:Vector.<InteractiveItemTile>;

    override public function setItems(items:Vector.<int>, itemIndexOffset:int = 0):void {
        var numItems:int = 0;
        var i:int = 0;
        if (items) {
            numItems = items.length;
            for (i = 0; i < this.NUM_SLOTS; i++) {
                if (i + indexOffset < numItems) {
                    this.tiles[i].setItem(items[i + indexOffset]);
                } else {
                    this.tiles[i].setItem(-1);
                }
            }
        }
    }
}
}