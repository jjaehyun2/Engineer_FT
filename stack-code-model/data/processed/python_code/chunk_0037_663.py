package com.tonyfendall.cards.controller
{
	import com.tonyfendall.cards.core.Block;
	import com.tonyfendall.cards.core.Board;
	import com.tonyfendall.cards.core.Card;
	import com.tonyfendall.cards.core.CardAttack;
	import com.tonyfendall.cards.core.Game;
	import com.tonyfendall.cards.core.Item;
	import com.tonyfendall.cards.enum.Position;
	import com.tonyfendall.cards.event.BlockEvent;
	import com.tonyfendall.cards.event.CardEvent;
	import com.tonyfendall.cards.event.GameEvent;
	import com.tonyfendall.cards.player.Hand;
	import com.tonyfendall.cards.player.PlayerBase;
	
	import flash.sampler.startSampling;
	
	import starling.core.Starling;
	
	
	public class GameController
	{
		
		public var game:Game;
		
		private var board:Board;
		
		private var blueHand:Hand;
		private var redHand:Hand;
		
		
		public function GameController(game:Game)
		{
			this.game = game;
			this.board = game.board;
			
			this.game.player1.controller = this;
			this.game.player2.controller = this;
		}
		
		
		
		public function beginGame():void
		{
			var positions:Array = new Array();
			var i:int;
			for(i=0; i<16; i++) {
				positions.push( new Position( i%4, Math.floor(i/4) ) );
			}
			
			var numBlocks:int = 0;
			for(i=0; i<6; i++) {
				if(Math.random() < 0.5)
					continue;
				
				
				var idx:int = Math.random()*positions.length;
				var position:Position = positions.splice(idx, 1)[0] as Position;
				
				Starling.juggler.delayCall(createBlock, numBlocks*0.3, position);
				numBlocks++;
			}
			
			Starling.juggler.delayCall(selectStartingPlayer, 0.5 + numBlocks*0.3);
		}
		
		private function createBlock(position:Position):void
		{
			var block:Block = new Block();
			board.placeItem(position, block);
			game.dispatchEvent(new BlockEvent(BlockEvent.PLACED, block));
		}
		
		
		private function selectStartingPlayer():void
		{
			if(Math.random() > 0.5)
				game.activePlayer = game.player1;
			else
				game.activePlayer = game.player2;

			game.gameStarted = true;
			game.dispatchEvent( new GameEvent(GameEvent.GAME_START, game) );
			
			Starling.juggler.delayCall(makePlayable, 0.8);
		}
		
		private function makePlayable():void
		{
			trace("Game has begun");
			game.dispatchEvent( new GameEvent(GameEvent.TURN_START, game) );
			board.state = Board.STATE_PLAYABLE;
		}

		
		public function handCardSelect(card:Card):void
		{
			var hand:Hand = card.originalOwner.hand;
			hand.selectedCard = card;
			
			for(var i:int = 0; i<hand.size; i++) {
				var tmp:Card = hand.getCard(i);
				if(tmp != card)
					tmp.dispatchEvent(new CardEvent(CardEvent.DIM, tmp));
				else
					tmp.dispatchEvent(new CardEvent(CardEvent.UNDIM, tmp));
			}
		}
		

		/**
		 * 
		 */
		public function boardClicked(position:Position):void
		{
			trace("Board clicked: "+position);
			
			var handToPlay:Hand = game.activePlayer.hand;
			
			if(handToPlay.selectedCard != null)
				playMove(handToPlay, handToPlay.selectedCard, position);
			else
				trace("No card was selected in "+game.activePlayer.name+"'s hand");
		}
		
		
		public function playMove(hand:Hand, card:Card, p:Position):void
		{
			if(hand == game.player1.hand) {
				for(var i:int = 0; i<hand.size; i++) {
					var tmp:Card = hand.getCard(i);
					if(tmp != card)
						tmp.dispatchEvent(new CardEvent(CardEvent.UNDIM, tmp));
				}
			}
			
			trace("Play move");
			board.state = Board.STATE_NORMAL;
			board.placeItem(p, card);
			
			game.dispatchEvent(new CardEvent(CardEvent.PLACED, card));

			hand.removeCard(card);
		
			Starling.juggler.delayCall(checkIfFightRequired, 1, card);
		}	
			
			
		private function checkIfFightRequired(card:Card):void
		{
			var lines:Array = card.getLinesOfAttack(board, true);
			
			if(lines.length == 0) 
			{
				Starling.juggler.delayCall(checkIfUnopposed, 0.5, card);
			}
			else if( lines.length == 1)
			{
				Starling.juggler.delayCall(initiateFight, 0.5, lines[0]);
			}
			else
			{
				for each(var item:Item in board.items) {
					var other:Card = item as Card;
					if(!other) continue;
					
					var found:Boolean = false;
					for each(var line:CardAttack in lines) {
						if(line.target == other) {
							found = true;
							break;
						}
					}
					
					if(found) {
						line.target.state = Card.STATE_SELECTABLE;
						line.target.dispatchEvent(new CardEvent(CardEvent.SELECTABLE, line.target));
					} else {
						other.dispatchEvent(new CardEvent(CardEvent.DIM, other));
					}
				}

				board.currentlySelectableFights = lines;
				
				game.dispatchEvent( new GameEvent(GameEvent.TARGET_SELECTABLE, game) );
			}
		}
		
		private function checkIfUnopposed(card:Card):void
		{
			// Should only get here if all previous fights have been resolved
			
			var lines:Array = card.getLinesOfAttack(board, false);
			
			if(lines.length > 0) {
				for each(var line:CardAttack in lines) {
					if(line.target.currentOwner == card.currentOwner)
						continue;
					
					line.target.currentOwner = card.currentOwner;
					line.target.dispatchEvent(new CardEvent(CardEvent.COLOUR_CHANGE, line.target, line));
				}
			}
			
			Starling.juggler.delayCall( endTurn, 0.5 );
		}
		
		
		/**
		 * 
		 */
		public function cardSelected(card:Card):void
		{
			var fight:CardAttack;
			var tmp:CardAttack;
			for(var i:int=0; i<board.currentlySelectableFights.length; i++) {
				tmp = board.currentlySelectableFights[i] as CardAttack;
				
				if(tmp.target == card) {
					fight = tmp;
					break;
				}
			}
			
			if(fight == null)
				return; // This is not the card we are looking for
			
			trace("Card Selected");
			
			for each(var other:CardAttack in board.currentlySelectableFights) {
				other.target.state = Card.STATE_NORMAL;
				other.target.dispatchEvent(new CardEvent(CardEvent.UNSELECTABLE, other.target));
			}
			
			for each(var item:Item in board.items) {
				var otherCard:Card = item as Card;
				if(!otherCard) continue;
				
				otherCard.dispatchEvent(new CardEvent(CardEvent.UNDIM, otherCard));
			}
			
			board.currentlySelectableFights = [];
			
			Starling.juggler.delayCall(initiateFight, 0.5, fight);
		}
		
		
		private function initiateFight(fight:CardAttack):void
		{
			trace("Initiate Fight");
			
			var attacker:Card = fight.origin;
			var defender:Card = fight.target;
			
			attacker.state = Card.STATE_FIGHTING;
			attacker.hp = attacker.getAttackValue();
			
			defender.state = Card.STATE_FIGHTING;
			defender.hp = defender.getDefenseValue(attacker.type);
			
			attacker.dispatchEvent(new CardEvent(CardEvent.FIGHT_START, attacker, fight));
			defender.dispatchEvent(new CardEvent(CardEvent.FIGHT_START, defender, fight));

			Starling.juggler.delayCall(executeFight, 1, fight);
		}
		
		
		private function executeFight(fight:CardAttack):void
		{
			trace("Execute Fight");
			var attacker:Card = fight.origin;
			var defender:Card = fight.target;
			
			attacker.hp -= Math.floor( Math.random()*attacker.hp );
			defender.hp -= Math.floor( Math.random()*defender.hp );
			
			attacker.dispatchEvent(new CardEvent(CardEvent.FIGHT_EXECUTE, attacker, fight));
			defender.dispatchEvent(new CardEvent(CardEvent.FIGHT_EXECUTE, defender, fight));
			
			if(attacker.hp == defender.hp) {
				// If it's a tie then run the fight again
				Starling.juggler.delayCall(initiateFight, 2, fight);
				
			} else {
				Starling.juggler.delayCall(completeFight, 2, fight);
			}
		}
		
		private function completeFight(fight:CardAttack):void
		{
			trace("Complete Fight");
			var attacker:Card = fight.origin;
			var defender:Card = fight.target;
			
			var winner:Card;
			var loser:Card;
			
			// Should never get here unless a clear winner exists
			if( attacker.hp > defender.hp) {
				winner = attacker;
				loser = defender;
			} else {
				winner = defender;
				loser = attacker;
			}

			attacker.state = Card.STATE_NORMAL;
			defender.state = Card.STATE_NORMAL;
			
			attacker.dispatchEvent(new CardEvent(CardEvent.FIGHT_COMPLETE, attacker, fight));
			defender.dispatchEvent(new CardEvent(CardEvent.FIGHT_COMPLETE, defender, fight));
			
			// Flip card
			loser.currentOwner = winner.currentOwner;
			loser.dispatchEvent(new CardEvent(CardEvent.COLOUR_CHANGE, loser, fight));
			
			Starling.juggler.delayCall(combo, 0.5, fight, loser);
		}
		
		private function combo(fight:CardAttack, loser:Card):void
		{
			trace("Combo");
			var attacker:Card = fight.origin;
			
			var lines:Array = loser.getLinesOfAttack(board, false);
			
			if(lines.length > 0) {
				for each(var line:CardAttack in lines) {
					if(line.target.currentOwner == loser.currentOwner)
						continue;
					
					line.target.currentOwner = loser.currentOwner;
					var e:CardEvent = new CardEvent(CardEvent.COLOUR_CHANGE, line.target, line);
						e.wasComboed = true;
					trace("COMBO: "+line.direction);
					line.target.dispatchEvent(e);
				}
			}

			// If the original attacker won then there might still be another card available to fight
			if(attacker != loser)
				Starling.juggler.delayCall(checkIfFightRequired, 0.2, attacker);
			else
				Starling.juggler.delayCall( endTurn, 0.5 );
		}
		
		
		private function endTurn():void
		{
			trace("End Turn");
			
			if(game.activePlayer == game.player1)
				game.activePlayer = game.player2;
			else
				game.activePlayer = game.player1;
			
			
			if( game.activePlayer.hand.size == 0 ) {
				game.activePlayer = null;
				
				game.turnsComplete = true;
				game.dispatchEvent( new GameEvent(GameEvent.TURNS_COMPELTE, game) );
				
				Starling.juggler.delayCall(prizeSelection, 2);
				
				recordResult();
				
			} else {
				// Allow next player to make a move
				board.state = Board.STATE_PLAYABLE;
				
				game.dispatchEvent( new GameEvent(GameEvent.TURN_START, game) );
			}
		}
		
		
		private function recordResult():void
		{
			// TODO record result
		}
		
		
		private function prizeSelection():void
		{
			if(game.winningPlayer != null) {
				trace("Prize Selectable");
				game.dispatchEvent( new GameEvent(GameEvent.PRIZE_SELECTABLE, game) );
		
			} else {
				trace("End Game");
				endGame();
			}
		}
		
		public function prizeChosen(prize:Card):void
		{
			var winner:PlayerBase = game.winningPlayer;
			var loser:PlayerBase = game.losingPlayer;

			if(prize.currentOwner != winner || prize.originalOwner != loser) {
				trace("Wrong prize selection");
				return;
			}
			
			trace("Prize Selected");
			game.dispatchEvent( new GameEvent(GameEvent.PRIZE_SELECTED, game, prize) );
			
			
			loser.loseCard(prize);
			winner.receiveCard(prize);
		}
		
		
		/**
		 * The player can review their prize for a long time, 
		 * so we need the view to tell us when they're done
		 */
		public function prizeReceived():void
		{
			Starling.juggler.delayCall(endGame, 0.5);
		}
		
		
		private function endGame():void
		{
			resetCards();
			game.dispatchEvent( new GameEvent(GameEvent.GAME_COMPLETE, game) );
		}
		
		private function resetCards():void
		{
			var items:Array = board.items;
			
			for(var i:int=0; i<items.length; i++) {
				var card:Card = items[i] as Card;
				if(card == null)
					continue;
				
				card.currentOwner = card.originalOwner;
				card.position = null;
				card.dispatchEvent(new CardEvent(CardEvent.COLOUR_CHANGE, card));
				
				
				if(card.originalOwner == game.player1) { // human player
					var changed:Boolean = false;
					
					if(card.type == "P" || card.type == "M") {
						if(Math.random() <= 0.0156) {
							card.type = "X";
							changed = true;
						}
					} else if(card.type == "X") {
						if(Math.random() <= 0.0056) {
							card.type = "A";
							changed = true;
						}
					}
					
					if(changed) {
						game.player1.deck.updateCard(card);
						card.dispatchEvent(new CardEvent(CardEvent.TYPE_CHANGE, card));
					}
				}
			}
		}
		
	}
}