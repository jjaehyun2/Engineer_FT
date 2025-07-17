package com.github.knose1.utils.timer {
	import com.github.knose1.utils.error.Warning;
	import flash.display.Stage;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	
	/**
	 * Distribué lorsqu’un objet FrameCounter atteint un intervalle spécifié conformément à la propriété FrameCounter.delay.
	 * @eventType	com.github.knose1.utils.timer.FrameCounterEvent.TIMER
	 */
	[Event(name="timer", type="com.github.knose1.utils.timer.FrameCounterEvent")] 

	/**
	 * Distribué lorsque le traitement du nombre de requêtes défini par Timer.totalLoop est terminé.
	 * @eventType	com.github.knose1.utils.timer.FrameCounterEvent.TIMER_COMPLETE
	 */
	[Event(name="timerComplete", type="com.github.knose1.utils.timer.FrameCounterEvent")] 

	/**
	 * Distribué à chaque appel de gotoNextFrame.
	 * @eventType	com.github.knose1.utils.timer.FrameCounterEvent.TICK
	 */
	[Event(name="tick", type="com.github.knose1.utils.timer.FrameCounterEvent")] 
	
	/*
	 * Fonctionnement du FrameCounter :
	 *		
	 *		Si totalLoop = 2 et delay = 2 :
	 *		
	 *		voila le trace(_currentFrame, _currentLoop) avec des commentaires en plus
	 *		0 0	//Etat initial au start
	 *		1 0	//Event Tick
	 *		2 0	//Event Tick && Event TIMER
	 *		1 1 //Event Tick
	 *		2 1 //Event Tick && Event TIMER && TIMER_COMPLETE 
	 */
	
	/**
	 * Un compteur de frame sur le modèle de la classe Timer
	 * @author Knose1
	 */
	public class FrameCounter extends EventDispatcher {
		
		/**
		 * Un stage utilisé pour compter les frames
		 */
		private var stageFrameCounter:Stage;

		/**
		 * Nombre de répétitions à faire; si totalLoop vaux 0 alors la loop se répettera à l'infini
		 * @throws Warning stop() must be called before changing totalLoop (setter)
		 */
		public function get totalLoop():uint {
			 return _totalLoop;
		}
		public function set totalLoop(pValue:uint):void {
			if (running) {
				trace(new Warning("stop() must be called before changing totalLoop").getStackTrace());
				return;
			}
			
			_totalLoop = pValue;
		}
		private var _totalLoop:uint;
		
		/**
		 * Nombre de répétitions faites (retourne -1 si le FrameCounter n'est pas en marche)
		 */
		public function get currentLoop():int {
			return _currentLoop;
		}
		private var _currentLoop:int = -1;

		/**
		 * Nombre de frames avant qu'une boucle soit faite
		 * @throws Warning stop() must be called before changing delay (setter)
		 */
		public function get delay():uint {
			 return _delay;
		}
		public function set delay(pValue:uint):void {
			if (running) {
				trace(new Warning("stop() must be called before changing delay").getStackTrace());
				return;
			}
			
			_delay = Math.max(1,pValue);
		}
		private var _delay:uint;
		
		/**
		 * Frames actuelle au sein de la boucle (retourne -1 si le FrameCounter n'est pas en marche)
		 */
		public function get currentFrame():Number {
			return _currentFrame;
		}
		private var _currentFrame:Number = -1;
		
		/**
		 * Le status du FrameCounter; vrai s'il est en marche, sinon faux
		 */
		public function get running():Boolean {
			return _running;
		}
		private var _running:Boolean = false;
		
		/**
		 * Indentement automatique :
		 * - Si vrai, l'instance créra une gameloop qui indentera automatiquement le currentFrame.
		 * - Si faux, il faudra appeller gotoNextFrame() dans votre gameloop 
		 * @throws Warning stop() must be called before changing autoIndent (setter)
		 */
		public function get autoIndent():Boolean {
			return _autoIndent;
		}
		public function set autoIndent(pValue:Boolean):void {
			if (running) {
				trace(new Warning("stop() must be called before changing autoIndent").getStackTrace());
				return;
			}
			_autoIndent = pValue;
		}
		
		private var _autoIndent:Boolean;
		
		/**
		 * Spécifie l'indentement de currentFrame à chaque frame
		 */
		public function get indentMultiplier():Number {
			return _indentMultiplier;
		}
		public function set indentMultiplier(pValue:Number):void {
			_indentMultiplier = Math.max(0, pValue);
		}
		private var _indentMultiplier:Number = 1
		
		/**
		 * Constructeur de la classe
		 * @param	pStage Référence du stage pour le frameRate (Passez null en paramètre pour désactiver l'indentement automatique)
		 * @param	pTimer Nombre de frames avant qu'une boucle soit faite
		 * @param	pLoop Nombre de répétition; si pLoop vaux 0 alors la loop se répettera à l'infini
		 */
		public function FrameCounter(pStage:Stage, pDelay:uint, pLoop:uint = 0) {
			totalLoop = pLoop;
			delay = pDelay;
			_autoIndent = Boolean(pStage);
			
			stageFrameCounter = pStage;
		}
		
		/**
		 * Détruit l'instance
		 */
		public function destroy():void {
			if (_autoIndent) stageFrameCounter.removeEventListener(Event.ENTER_FRAME, onEnterFrame);
		}
		
		/**
		 * Initialise et met en marche le compteur s'il n'est pas en marche
		 */
		public function start():void {
			
			if (_running) {
				return;
			}
			
			reset();
			_running = true;
			
			if (_autoIndent) {
				stageFrameCounter.addEventListener(Event.ENTER_FRAME, onEnterFrame);
			}
			
		}
		
		/**
		 * Arrète et réinitialise le compteur
		 */
		public function stop():void {
			if (_autoIndent) stageFrameCounter.removeEventListener(Event.ENTER_FRAME, onEnterFrame);
			
			_running = false;
			_currentLoop = -1;
			_currentFrame = -1;
		}
		
		/**
		 * Réinitialise le compteur
		 */
		public function reset():void {
			_currentLoop = 0;
			_currentFrame = 0;
		}
		
		/**
		 * Incrémente automatiquement les frames via l'event EnterFrame posé sur le stage
		 */
		private function onEnterFrame(pEvent:Event):void {
			gotoNextFrame();
		}
		
		/**
		 * Fonction qui indente la currentFrame tout en prenant en compte le nombre de loop
		 */
		public function gotoNextFrame():void {
			
			//Change de loop ou stop le FrameCounter celon le nombre de loop restant
			//-> Permet de faire le test _currentFrame == _delay
			if (_currentFrame >= _delay) {
				_currentLoop += 1;
				_currentFrame = 0;
			}
			
			_currentFrame += _indentMultiplier;
			
			//Envoie l'event quand le délai est atteint
			if (_currentFrame >= _delay) {
				
				//Si le nombre de loop n'est pas infini et que l'on a attein le nombre total de loop à faire on arrète le compteur et on envoie l'event complete
				if (_totalLoop && _currentLoop + 1 >= _totalLoop) {
					stop();
					dispatchEvent(new FrameCounterEvent(FrameCounterEvent.TIMER_COMPLETE));
				}
				
				dispatchEvent(new FrameCounterEvent(FrameCounterEvent.TIMER));
			}
			
			dispatchEvent(new FrameCounterEvent(FrameCounterEvent.TICK));
			
			//Les event sont à la fin pour que au stop, les objects event.target aient running=false
		}
		
		/**
		 * @inheritDoc 
		 */
		override public function toString():String {
			return "[FrameCounter totalLoop=" + totalLoop + " currentLoop=" + currentLoop + " delay=" + delay + " currentFrame=" + currentFrame + " running=" + running + "]";
		}
	}
}