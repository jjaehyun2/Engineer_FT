/**
 * Created by ricardo_neves at bytesfromouterspace.com on 28/02/2015.
 */
package com.bytesfromouterspace.stockbrokers.model {
    import com.bytesfromouterspace.stockbrokers.event.GameEvent;

    public class GameModel extends BaseModel {

        public static const VERSION:String = "1.0.1";

        public var turn:TurnModel;
        public var market:MarketModel;
        public var reputation:ReputationModel;
        public var investors:InvestorsModel;
        public var generator:SoundRandomGeneratorModel;

        public function GameModel() {
            super();

            generator = new SoundRandomGeneratorModel('assets/audio/sample1_cut.mp3');

            // Prepare Market
            market = new MarketModel(generator);
            // Set starting cash
            market.startingCash = 250000;
            // generator influences 30% of stock price
            market.generatorInfluenceRatio = 0.3;
            // transactions may influence 10% of stock price
            market.transactionInfluenceRatio = 0.1;
            // initialize market
            market.initialize();

            // Prepare reputation, set bonus & penalties
            reputation = new ReputationModel();
            reputation.reputationValueSuccessfulBuy = 10;
            reputation.reputationValueSuccessfulSell = 15;
            reputation.reputationValueFraudInsFunds = -50;
            reputation.reputationValueFraudQtdBuy = -5;
            reputation.reputationValueFraudQtdSell = -20;

            // Prepare turn timer
            turn = new TurnModel(12);

            // Prepare investors & kingpins
            investors = new InvestorsModel();


        }

        public function endGame():void {
            turn.running = false;
            dispatchEvent(new GameEvent(GameEvent.GAME_OVER));
        }

        public function getGameStatsSession():GameStatsSessionModel {
            var statsSource:GameStatsSessionModel = new GameStatsSessionModel();
            statsSource.agregateStats("inv", investors.stats);
            statsSource.agregateStats("fund",market.funds.stats);
            statsSource.agregateStats("mark",market.stats);
            statsSource.agregateStats("rep", reputation.stats);
            statsSource.agregateStats("turn", turn.stats);
            return statsSource;
        }
    }
}