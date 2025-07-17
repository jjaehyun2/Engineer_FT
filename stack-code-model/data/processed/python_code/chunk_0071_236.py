package com.illuzor.bubbles.screens {
	
	import com.greensock.easing.Back;
	import com.greensock.TweenLite;
	import com.illuzor.bubbles.constants.ParticlesType;
	import com.illuzor.bubbles.constants.ScreenType;
	import com.illuzor.bubbles.events.ScreenEvent;
	import com.illuzor.bubbles.graphics.Circle;
	import com.illuzor.bubbles.graphics.PlayerCircle;
	import com.illuzor.bubbles.graphics.TextButton;
	import com.illuzor.bubbles.tools.DelayedDestroyer;
	import com.illuzor.bubbles.tools.ResourceManager;
	import com.illuzor.bubbles.utils.plusOrMinus;
	import com.illuzor.bubbles.utils.randomInt;
	import flash.geom.Point;
	import starling.core.Starling;
	import starling.events.Event;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	import starling.extensions.PDParticleSystem;
	import starling.text.TextField;
	import starling.text.TextFieldAutoSize;
	import starling.textures.Texture;
	import starling.textures.TextureAtlas;
	
	/**
	 * Класс игрового экрана.
	 * Тут происходт всё игровое действие
	 */
	
	public class GameScreen extends ScreenBase {
		
		/** @private набор цветов. для раскраски кругов в случайный цвет */
		private var colors:Vector.<uint> = new <uint>[0xC40000,0x008040, 0xFF8000, 0x7B9A01];
		/** @private список всех кругов (кроме круга игрока) */
		private var circles:Vector.<Circle> = new Vector.<Circle>();
		/** @private список всех систем частиц для хвостов */
		private var trails:Vector.<PDParticleSystem> = new Vector.<PDParticleSystem>();
		/** @private круг игрока */
		private var playerCircle:PlayerCircle;
		/** @private количество кругов */
		private var totalCircles:uint = 18;
		/** @private время рождения круга */
		private var bornTime:Number = .6;
		/** @private время жизни круга */
		private var lifeTime:Number = 1.1;
		/** @private текстура круга */
		private var circleTexture:Texture;
		/** @private нужно ли проверять столкновения в данный момент */
		private var needToCheckCollisions:Boolean;
		/** @private количество использованных кругов игрока */
		private var circlesUsed:uint;
		/** @private общее количество очков */
		private var scores:uint;
		/** @private множитель очков. увеличивается на 1 за каждый круг, врезавшийся в один и тот же круг игрока*/
		private var scoresMultiplier:uint = 1;
		/** @private текстовое поле для отображения количества использованных кругов */
		private var totCirclesTextField:TextField;
		/** @private текстовое поле для отображения набранных очков */
		private var scoreTextField:TextField;
		/** @private кнопка перезапуска игры */
		private var replayButton:TextButton;
		/** @private кнопка выхода в главное меню */
		private var exitButton:TextButton;
		
		/**
		 * Конструктор. Инициализация некоторых переменных
		 */
		public function GameScreen() {
			var config:Object = ResourceManager.getConfig(); // достаём конфиг и далее вытаскиваем нужные значения (если они существуют)
			if (config.hasOwnProperty("countPoints"))
				totalCircles = config.countPoints;
				
			if (config.hasOwnProperty("bornTime"))
				bornTime = config.bornTime;
				
			if (config.hasOwnProperty("lifeTime"))
				lifeTime = config.lifeTime;
				
			var atlas:TextureAtlas = ResourceManager.getAtlas();
			circleTexture = atlas.getTexture("circle"); // кэшируем текстуру круга
		}
		
		/**
		 * инициализация, добавление слушателей
		 */
		override protected function start():void {
			init();
			stage.addEventListener(TouchEvent.TOUCH, onTouch);
			addEventListener(Event.ENTER_FRAME, onUpdate);
		}
		
		/** 
		 * @private Создание кругов и их хвостов.
		 * Создание текстовых полей 
		 */
		private function init():void {
			for (var i:int = 0; i < totalCircles; i++) {
				// создание эффекта частиц для хвоста круга
				var trailParticle:PDParticleSystem = ResourceManager.getParticles(ParticlesType.TRAIL_PARTICLES);
				Starling.juggler.add(trailParticle);
				addChild(trailParticle);
				trailParticle.start();
				trails.push(trailParticle);
				
				// создание круга с рандомной скоростью и рандомными координатами
				var circle:Circle = new Circle(circleTexture, .5 + Math.random() * 3, .5 + Math.random() * 3);
				circle.color = colors[randomInt(0, colors.length - 1)];
				circle.directionX = plusOrMinus();
				circle.directionY = plusOrMinus();
				circle.x = randomInt(12, stageWidth - 12);
				circle.y = randomInt(12, stageWidth - 12);
				addChild(circle);
				circles.push(circle);
			}
			
			scoreTextField = new TextField(300, 30, "SCORE: 0", "font", 24, 0xFFFFFF);
			scoreTextField.autoSize = TextFieldAutoSize.BOTH_DIRECTIONS;
			addChild(scoreTextField);
			scoreTextField.x = 20;
			scoreTextField.y = stageHeight - scoreTextField.height - 50;
			
			totCirclesTextField = new TextField(300, 30, "CIRCLES USED: 0", "font", 24, 0xFFFFFF);
			totCirclesTextField.autoSize = TextFieldAutoSize.BOTH_DIRECTIONS;
			addChild(totCirclesTextField);
			totCirclesTextField.x = 20;
			totCirclesTextField.y = stageHeight - totCirclesTextField.height - 20;
		}
		
		/**
		 * @private обработчик клика.
		 * Если событие нулевое, прерываем выполнение функции.
		 * Если нет круга игрока, добавляем его в точку клика
		 * 
		 * @param	e событие тача (для клика)
		 */
		private function onTouch(e:TouchEvent):void {
			var touch:Touch = e.getTouch(stage, TouchPhase.ENDED);
			if (!touch) return;
			
			if (!playerCircle) {
				circlesUsed++; // инкреминируем количество использованных кругов
				totCirclesTextField.text = "CIRCLES USED: ".concat(circlesUsed); // обновление соответствующего текстфилда
				playerCircle = new PlayerCircle(circleTexture);
				playerCircle.color = 0x004080
				playerCircle.x = touch.globalX;
				playerCircle.y = touch.globalY;
				addChildAt(playerCircle, 0);
				playerCircle.scaleX = playerCircle.scaleY = 0;
				TweenLite.to(playerCircle, bornTime, { scaleX:1, scaleY:1, onComplete:hidePlayerCircle} );
			}
		}
		
		/** @private скрытие круга игрока */
		private function hidePlayerCircle():void {
			needToCheckCollisions = true; // включение проверки коллизий
			TweenLite.to(playerCircle, .5, { delay:lifeTime, scaleX:0, scaleY:0, onStart:disableCollisions, onComplete:killMainCircle, ease:Back.easeIn } );
		}
		
		/** @private выключение проверки коллизий и сброс множителя очков */
		private function disableCollisions():void {
			needToCheckCollisions = false;
			scoresMultiplier = 1;
		}
		/** @private удаление круга игрока */
		private function killMainCircle():void {
			removeChild(playerCircle);
			playerCircle.dispose();
			playerCircle = null;
		}
		
		/**
		 * @private Обновление состояния игры.
		 * Движение кругов, отражения от стен, смена направления
		 * @param	e событие enterFrame
		 */
		private function onUpdate(e:Event):void {
			if (!circles.length) { // если круги кончились
				end() // заканчиваем
				return;
			}
			
			for (var i:int = 0; i < circles.length; i++) {
				var circle:Circle = circles[i];
				circle.move();
				
				// случайная смена направления
				if (Math.random() < .0012) {
					var randomDirection:Number = Math.random();
					if (randomDirection <= .4) {
						circle.directionX *= -1;
					} else if (randomDirection < .4 && randomDirection >=.8) {
						circle.directionY *= -1;
					} else {
						circle.directionX *= -1;
						circle.directionY *= -1;
					}
				}
				
				// отражение от стен
				if (circle.directionX == -1 && circle.x <= 12) {
					circle.directionX = 1;
				}
				if (circle.directionX == 1 && circle.x >= stageWidth-12) {
					circle.directionX = -1;
				}
				if (circle.directionY == -1 && circle.y <= 12) {
					circle.directionY = 1;
				}
				if (circle.directionY == 1 && circle.y >= stageHeight-12) {
					circle.directionY = -1;
				}
				trails[i].emitterX = circle.x;
				trails[i].emitterY = circle.y;
			}
			if (needToCheckCollisions) checkCollisions(); // проверяем коллизии, если нужно
		}
		
		/**
		 * @private проверка столкновений летающих кругов с кругом игрока
		 */
		private function checkCollisions():void {
			var mainCirclePoint:Point = new Point(playerCircle.x, playerCircle.y); //координаты круга игрока
			for (var i:int = circles.length - 1; i >= 0; i--) {
				var currentCircle:Circle = circles[i];
				var currentCirclePoint:Point = new Point(currentCircle.x, currentCircle.y); //координаты круга
				if (Point.distance(mainCirclePoint, currentCirclePoint) <= 62) { // если расстояние меньше заданного, значит есть столкновение
					var currentScore:uint = 100 * scoresMultiplier; // считаем количество очков за данный круг
					scores += currentScore; // увеличиваем общее количество очков
					scoreTextField.text = "SCORE: ".concat(scores); // обновляем тестовое поле
					
					// частицы для взрыва круга при исчезновении
					var explosionParticles:PDParticleSystem = ResourceManager.getParticles(ParticlesType.EXPLOSION_PARTICLES);
					addChild(explosionParticles);
					Starling.juggler.add(explosionParticles);
					explosionParticles.emitterX = currentCircle.x;
					explosionParticles.emitterY = currentCircle.y;
					
					trails[i].stop(); // останавливаем соответствующий хвост
					
					// точка столкновения (нужна для отображения "искр" столкновения)
					var collisionPoint:Point = Point.interpolate(mainCirclePoint, currentCirclePoint, 0.24);
					// частицы для искр столкновения
					var collisionParticles:PDParticleSystem = ResourceManager.getParticles(ParticlesType.COLLISION_PARTICLES);
					addChild(collisionParticles);
					Starling.juggler.add(collisionParticles);
					collisionParticles.x = collisionPoint.x;
					collisionParticles.y = collisionPoint.y;
					collisionParticles.start(.23);
					
					// выскакивающее тестовое поле с количеством очков за данный круг
					var scoreTF:TextField = getScoreText(currentScore);
					scoreTF.x = currentCircle.x-3;
					scoreTF.y = currentCircle.y;
					addChild(scoreTF);
					scoreTF.scaleX = scoreTF.scaleY = 0;
					
					// показываем текстовое поле
					TweenLite.to(scoreTF, .38, { delay:bornTime, scaleX:1, scaleY:1, ease:Back.easeOut } );
					// прячем текстовое поле
					TweenLite.to(scoreTF, .5, { delay:lifeTime+bornTime, overwrite:false, scaleX:0, scaleY:0, ease:Back.easeIn } );
					// увеличиваем круг
					TweenLite.to(circles[i], bornTime, { width:100, height:100 } );
					// прячем круг
					TweenLite.to(circles[i], .15, { delay:bornTime+lifeTime, overwrite:false, alpha:0, onStart:explosionParticles.start, onStartParams:[.25] } );
					
					// списк систем частиц для деструктора
					var particlesList:Array = [explosionParticles, collisionParticles, trails.splice(i, 1)[0]];
					
					// создание деструктора
					new DelayedDestroyer(this, circles.splice(i, 1)[0], particlesList, scoreTF, (bornTime+lifeTime * 2) * 1000);
					scoresMultiplier++;
				}
			}
		}
		
		/**
		 * @private генератор выскакивающего текстовового поля с очками
		 * 
		 * @param	score количество очков
		 * @return готовое текстовое поле
		 */
		private function getScoreText(score:uint):TextField {
			var tf:TextField = new TextField(10, 10, String(score), "font", 32, 0xFFFFFF);
			tf.autoSize = TextFieldAutoSize.BOTH_DIRECTIONS;
			tf.pivotX = tf.width >> 1;
			tf.pivotY = tf.height >> 1;
			return tf;
		}
		
		/** @private конец игры 
		 * Отображение кнопок повтора и выхода */
		private function end():void {
			removeEventListener(Event.ENTER_FRAME, onUpdate);
			stage.removeEventListener(TouchEvent.TOUCH, onTouch);
			
			var butTexture:Texture = ResourceManager.getAtlas().getTexture("button_background");
			
			replayButton = new TextButton(butTexture, "REPLAY");
			replayButton.y = (stageHeight >> 1) - 80;
			addChild(replayButton);
			
			exitButton = new TextButton(butTexture, "EXIT");
			exitButton.y = (stageHeight >> 1) + 80;
			addChild(exitButton);
			replayButton.x = exitButton.x = stageWidth >> 1;
			replayButton.scaleX = replayButton.scaleY = exitButton.scaleX = exitButton.scaleY = 0;
			
			TweenLite.to(replayButton, .5, { scaleX:1, scaleY:1, ease:Back.easeOut, delay:1.5 } );
			TweenLite.to(exitButton, .5, { scaleX:1, scaleY:1, ease:Back.easeOut, delay:1.8 } );
			
			replayButton.addEventListener(Event.TRIGGERED, onButtonClick);
			exitButton.addEventListener(Event.TRIGGERED, onButtonClick);
		}
		
		private function onButtonClick(e:Event):void {
			replayButton.removeEventListener(Event.TRIGGERED, onButtonClick);
			exitButton.removeEventListener(Event.TRIGGERED, onButtonClick);
			if (e.target == replayButton) {
				dispatchEvent(new ScreenEvent(ScreenEvent.CHANGE_SCREEN, ScreenType.GAME_SCREEN));
			} else {
				dispatchEvent(new ScreenEvent(ScreenEvent.CHANGE_SCREEN, ScreenType.MAIN_MENU));
			}
		}
		
		/** метод-деструктор */
		override public function dispose():void {
			circleTexture.dispose();
			replayButton.dispose();
			exitButton.dispose();
			scoreTextField.dispose();
			totCirclesTextField.dispose();
			super.dispose();
		}
	}
}