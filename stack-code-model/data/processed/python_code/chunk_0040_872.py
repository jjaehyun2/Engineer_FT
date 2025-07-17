package data  {
	
	import flash.net.FileReference;
	import flash.utils.Dictionary;
	
	/**
	 * ...
	 * @author Adam Vernon
	 */
	public class Solver {
		
		[Embed(source="../../lib/list.txt", mimeType="application/octet-stream")]
		private const WordList:Class;
		
		private const _connections:Vector.<Vector.<int>> = new <Vector.<int>>[
			new <int>[1,4,5],		//0
			new <int>[0,2,4,5,6],	//1
			new <int>[1,3,5,6,7],	//2, etc.
			new <int>[2,6,7],
			new <int>[0,1,5,8,9],
			new <int>[0,1,2,4,6,8,9,10],
			new <int>[1,2,3,5,7,9,10,11],
			new <int>[2,3,6,10,11],
			new <int>[4,5,9,12,13],
			new <int>[4,5,6,8,10,12,13,14],
			new <int>[5,6,7,9,11,13,14,15],
			new <int>[6,7,10,14,15],
			new <int>[8,9,13],
			new <int>[8,9,10,12,14],
			new <int>[9,10,11,13,15],
			new <int>[10,11,14]
		];
		
		private var _foundWords:Vector.<String> = new <String>[];
		
		private var _free:Vector.<Boolean> = new <Boolean>[];
		private var _letters:Vector.<String> = new <String>[];
		private var _candidate:String;
		private var _candidateIndices:Vector.<int>;
		
		private var _words:Vector.<String> = new <String>[];
		private var _wordList:String;
		private var _prefixRanges:Dictionary = new Dictionary();
		
		
		public function Solver() {
			data_init();
		}
		
		private function data_init():void {
			_wordList = String(new WordList());
			var wordsArr:Array = _wordList.split("\n");
			
			prefixes_process(wordsArr);
		}
		
		private function prefixes_process(wordsArr:Array):void {
			var pre1:String = "";
			var pre2:String = "";
			var pre3:String = "";
			var curPre1:String;
			var curPre2:String;
			var curPre3:String;
			var rangeStart1:int = 0;
			var rangeStart2:int = 0;
			var rangeStart3:int = 0;
			var index:int = 0;
			
			for each (var word:String in wordsArr) {
				_words.push(word);
				
				curPre1 = word.substr(0, 1);
				curPre2 = word.substr(0, 2);
				curPre3 = word.substr(0, 3);
				
				if (pre1 == "") {
					pre1 = curPre1;
				} else if (curPre1 != pre1) {
					_prefixRanges[pre1] = new RangeRecord(pre1, rangeStart1, index-1);
					rangeStart1 = index;
					pre1 = curPre1;
				}
				if (pre2 == "") {
					pre2 = curPre2;
				} else if (curPre2 != pre2) {
					_prefixRanges[pre2] = new RangeRecord(pre2, rangeStart2, index-1);
					rangeStart2 = index;
					pre2 = curPre2;
				}
				if (pre3 == "") {
					pre3 = curPre3;
				} else if (curPre3 != pre3) {
					_prefixRanges[pre3] = new RangeRecord(pre3, rangeStart3, index-1);
					rangeStart3 = index;
					pre3 = curPre3;
				}
				
				index ++;
			}
		}
		
		public function words_find(startAt:int = -1):void {
			if (startAt == -1) {
				_foundWords = new <String>[];
				for (var i:int = 0; i < 16; i++) {
					words_find(i);
				}
				//trace(_foundWords);
				return;
			}
			
			_free = new <Boolean>[true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true];
			_free[startAt] = false;
			_candidate = _letters[startAt];
			_candidateIndices = new <int>[startAt];
			word_continue();
		}
		
		private function word_continue():void {
			//Is viable?//
			var preFixCheck:String = _candidate;
			if (_candidate.length > 3) {
				preFixCheck = _candidate.substr(0, 3);
			}
			if (! (preFixCheck in _prefixRanges)) {
				if (search_backtrack()) word_continue();
				return;		//Exits current function, ending search altogether if backtrack is impossible
			}
			
			//Is still viable or full word?//
			var rr:RangeRecord = _prefixRanges[preFixCheck];
			var viable:Boolean = true;
			if (_candidate.length > 2) {
				viable = false;
				for (var i:int = rr.firstI; i <= rr.lastI; i++) {
					if (_words[i] == _candidate) {
						if ((_candidate.length > 2) && (_foundWords.indexOf(_candidate) == -1)) _foundWords.push(_words[i]);
						viable = true;
						break;
					}
					if (_words[i].length >= _candidate.length) {
						if (_words[i].substr(0, _candidate.length) == _candidate) viable = true;
					}
				}
			}
			
			if (! viable) {
				if (search_backtrack()) word_continue();
				return;		//Exits current function, ending search altogether if backtrack is impossible
			}
			
			//Next!//
			if (search_advance()) word_continue();
			else if (search_backtrack()) word_continue();
		}
		
		private function search_advance():Boolean {
			var conSet:Vector.<int> = _connections[_candidateIndices[_candidateIndices.length-1]];
			
			for (var i:int = 0; i < conSet.length; i++) {
				if (_free[conSet[i]]) {
					_free[conSet[i]] = false;
					_candidate += _letters[conSet[i]];
					_candidateIndices.push(conSet[i]);
					return true;
				}
			}
			
			return false;
		}
		
		private function search_backtrack():Boolean {
			if (_candidateIndices.length < 2) return false;
			
			var lastIndex:int = _candidateIndices.pop();
			_free[lastIndex] = true;
			if (_letters[lastIndex] == "QU") _candidate = _candidate.substr(0, _candidate.length-2);
			else _candidate = _candidate.substr(0, _candidate.length-1);
			
			var conSet:Vector.<int> = _connections[_candidateIndices[_candidateIndices.length - 1]];
			var nextCon:int = conSet.indexOf(lastIndex) + 1;
			while ((nextCon < conSet.length) && (! _free[conSet[nextCon]])) {
				nextCon ++;
			}
			if (nextCon >= conSet.length) return search_backtrack();
			
			_free[conSet[nextCon]] = false;
			_candidate += _letters[conSet[nextCon]];
			_candidateIndices.push(conSet[nextCon]);
			
			return true;
		}
		
		public function set letters(value:Vector.<String>):void { _letters = value; }
		
		public function get foundWords():Vector.<String> { return _foundWords; }
		
		
		//Defunct//
		private function words_exclude(wordsArr:Array):void {
			var out:String = "";
			for each (var word:String in wordsArr) {
				if ((word.length > 2) && (word.length < 17)) out += word + "\n";
			}
			var fr:FileReference = new FileReference();
			fr.save(out, "list.txt");
		}
		
	}

}