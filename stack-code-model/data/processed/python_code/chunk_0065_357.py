package asunit.framework {
    import asunit.asserts.assertTrue;
    import asunit.errors.AssertionFailedError;
    
    import flash.errors.IllegalOperationError;
    import flash.events.EventDispatcher;
    import flash.utils.getQualifiedClassName;

    /**
     * A set of assert methods.  Messages are only displayed when an assert fails.
     */

    public class Assert extends EventDispatcher {
        /**
         * Protect constructor since it is a static only class
         */
        public function Assert() {
        }

        /**
         * Asserts that a condition is true. If it isn't it throws
         * an AssertionFailedError with the given message.
         */
        static public function assertTrue(...args:Array):void {
            var message:String;
            var actual:Object;

            if(args.length == 1) {
                message = "";
                actual = args[0];
            }
            else if(args.length == 2) {
                message = args[0];
                actual = args[1];
            }
            else {
                throw new IllegalOperationError("Invalid argument count");
            }

            if(!actual) {
				throw new AssertionFailedError(format(message, true, actual));
            }
        }
        /**
         * Asserts that a condition is false. If it isn't it throws
         * an AssertionFailedError with the given message.
         */
        static public function assertFalse(...args:Array):void {
            var message:String;
            var actual:Object;

            if(args.length == 1) {
                message = "";
                actual = args[0];
            }
            else if(args.length == 2) {
                message = args[0];
                actual = args[1];
            }
            else {
                throw new IllegalOperationError("Invalid argument count");
            }

            if(actual) {
				throw new AssertionFailedError(format(message, false, actual));
            }
        }
        /**
         *  Fails a test with the given message.
         *
         *  @example This method can be called anytime you want to break out and fail
         *  the current test.
         *
         *  <listing>
         *  public function testSomething():void {
         *      var instance:MyClass = new MyClass();
         *      if(instance.foo()) {
         *          fail('The foo should not have been there');
         *      }
         *  }
         *  </listing>
         */
        static public function fail(message:String):void {
            throw new AssertionFailedError(message);
        }

        /**
        *  Asserts that the provided block throws an exception that matches
        *  the type provided.
        *
        *  <listing>
        *  public function testFailingCode():void {
        *     assertThrows(CustomError, function():void {
        *           var instance:Sprite = new Sprite();
        *           instance.callMethodThatThrows();
        *     });
        *  }
        *  </listing>
        **/
        static public function assertThrows(errorType:Class, block:Function):void {
			try {
				block.call();
			}
			catch(e:Error) {
				if(!(e is errorType)) {
					throw new AssertionFailedError("expected error type:<" + getQualifiedClassName(errorType)
						+"> but was:<" + getQualifiedClassName(e) + ">");
				}
				return;
			}
			throw new AssertionFailedError("expected error type:<" + getQualifiedClassName(errorType) + "> but none was thrown." );
        }

        /**
         *  Asserts that two objects are equal. If they are not
         *  an AssertionFailedError is thrown with the given message.
         *
         *  This assertion should be (by far) the one you use the most.
         *  It automatically provides useful information about what
         *  the failing values were.
         *
         *  <listing>
         *  public function testNames():void {
         *      var name1:String = "Federico Aubele";
         *      var name2:String = "Frederico Aubele";
         *
         *      assertEquals(name1, name2);
         *  }
         *  </listing>
         */
        static public function assertEquals(...args:Array):void {
            var message:String;
            var expected:Object;
            var actual:Object;

            if(args.length == 2) {
                message = "";
                expected = args[0];
                actual = args[1];
            }
            else if(args.length == 3) {
                message = args[0];
                expected = args[1];
                actual = args[2];
            }
            else {
                throw new IllegalOperationError("Invalid argument count");
            }

            if(expected == null && actual == null) {
                return;
            }

            try {
                if(expected != null && expected.equals(actual)) {
                    return;
                }
            }
            catch(e:Error) {
                if(expected != null && expected == actual) {
                    return;
                }
            }

            throw new AssertionFailedError(format(message, expected, actual));
        }
        /**
         * Asserts that an object isn't null. If it is
         * an AssertionFailedError is thrown with the given message.
         */
        static public function assertNotNull(...args:Array):void {
            var message:String;
            var actual:Object;

            if(args.length == 1) {
                message = "";
                actual = args[0];
            }
            else if(args.length == 2) {
                message = args[0] + " ";
                actual = args[1];
            }
            else {
                throw new IllegalOperationError("Invalid argument count");
            }

			if(actual == null) {
				throw new AssertionFailedError(message + "expected not null but was:<" + actual + ">");
			}
        }
        /**
         * Asserts that an object is null.  If it is not
         * an AssertionFailedError is thrown with the given message.
         */
        static public function assertNull(...args:Array):void {
            var message:String;
            var actual:Object;

            if(args.length == 1) {
                message = "";
                actual = args[0];
            }
            else if(args.length == 2) {
                message = args[0];
                actual = args[1];
            }
            else {
                throw new IllegalOperationError("Invalid argument count");
            }
			
			if(actual != null) {
				throw new AssertionFailedError(format(message, null, actual));
			}
        }
        /**
         * Asserts that two objects refer to the same object. If they are not
         * an AssertionFailedError is thrown with the given message.
         */
        static public function assertSame(...args:Array):void {
            var message:String;
            var expected:Object;
            var actual:Object;

            if(args.length == 2) {
                message = "";
                expected = args[0];
                actual = args[1];
            }
            else if(args.length == 3) {
                message = args[0] + " ";
                expected = args[1];
                actual = args[2];
            }
            else {
                throw new IllegalOperationError("Invalid argument count");
            }

            if(expected !== actual) {
				throw new AssertionFailedError(message + "expected same as:<" + expected + "> but was:<" + actual + ">");
            }
        }
         /**
          * Asserts that two objects do not refer to the same object. If they do,
          * an AssertionFailedError is thrown with the given message.
          */
        static public function assertNotSame(...args:Array):void {
            var message:String;
            var expected:Object;
            var actual:Object;

            if(args.length == 2) {
                message = "";
                expected = args[0];
                actual = args[1];
            }
            else if(args.length == 3) {
                message = args[0] + " ";
                expected = args[1];
                actual = args[2];
            }
            else {
                throw new IllegalOperationError("Invalid argument count");
            }

            if(expected === actual) {
				throw new AssertionFailedError(message + "expected not same but both were:<" + actual + ">");
			}
        }

        /**
         * Asserts that two numerical values are equal within a tolerance range.
         * If they are not an AssertionFailedError is thrown with the given message.
         */
        static public function assertEqualsFloat(...args:Array):void {
            var message:String;
            var expected:Number;
            var actual:Number;
            var tolerance:Number = 0;

            if(args.length == 3) {
                message = "";
                expected = args[0];
                actual = args[1];
                tolerance = args[2];
            }
            else if(args.length == 4) {
                message = args[0];
                expected = args[1];
                actual = args[2];
                tolerance = args[3];
            }
            else {
                throw new IllegalOperationError("Invalid argument count");
            }
            if (isNaN(tolerance)) tolerance = 0;
            if(Math.abs(expected - actual) <= tolerance) {
                   return;
            }
            throw new AssertionFailedError(format(message, expected, actual));
        }

        /**
         * Asserts that two arrays have the same length and contain the same
         * objects in the same order. If the arrays are not equal by this
         * definition an AssertionFailedError is thrown with the given message.
         */
        static public function assertEqualsArrays(...args:Array):void {
            var message:String;
            var expected:Array;
            var actual:Array;

            if(args.length == 2) {
                message = "";
                expected = args[0];
                actual = args[1];
            }
            else if(args.length == 3) {
                message = args[0];
                expected = args[1];
                actual = args[2];
            }
            else {
                throw new IllegalOperationError("Invalid argument count");
            }

            if (expected == null && actual == null) {
                return;
            }
            if ((expected == null && actual != null) || (expected != null && actual == null)) {
                failNotEquals(message, expected, actual);
            }
            // from here on: expected != null && actual != null
            if (expected.length != actual.length) {
                failNotEquals(message, expected, actual);
            }
            for (var i : int = 0; i < expected.length; i++) {
                assertEquals(expected[i], actual[i]);
            }
        }

		
		/**
		 * Asserts that two arrays have the same length and contain the same
		 * objects in the same order. If the arrays are not equal by this
		 * definition an AssertionFailedError is thrown with the given message.
		 */
		static public function assertEqualsArraysRecursive(...args:Array):void {
			if(args.length < 2) throw new ArgumentError("need at least <expected> and <actual>");
			var actual:* = args.pop();
			var expected:* = args.pop();
			var message:String = args.pop() || "";
			
			if (expected == null && actual == null) {
				return;
			}
			if(expected == null)
				assertNull(message,actual);
			else 
				assertNotNull(message, actual);
	
			// from here on: expected != null && actual != null
			if (expected.length != actual.length) {
				failNotEquals(message + "lengths differ", expected, actual);
			}
			for (var i : int = 0; i < expected.length; i++) {
				if(expected[i] is Array || actual[i] is Array || expected[i] is Vector || actual[i] is Vector) 
					assertEqualsArraysRecursive(message+ "["+i+"]", expected[i], actual[i]);
				 else 
					assertEquals(message + "["+i+"]",expected[i], actual[i]);
			}
		}
        /**
         * Asserts that two arrays have the same length and contain the same
         * objects. The order of the objects in the arrays is ignored. If they
         * are not equal by this definition an AssertionFailedError is thrown
         * with the given message.
         */
        static public function assertEqualsArraysIgnoringOrder(...args:Array):void {
            if(args.length < 2) 
				throw new IllegalOperationError("Invalid argument count");

			
			var message:String;
            var expected:Array;
            var actual:Array;

            if(args.length == 2) {
                message = "";
                expected = args[0];
                actual = args[1];
            }
            else if(args.length == 3) {
                message = args[0];
                expected = args[1];
                actual = args[2];
            }
            else {
            }

            if (expected == null && actual == null) {
                return;
            }
            if ((expected == null && actual != null) || (expected != null && actual == null)) {
                failNotEquals(message, expected, actual);
            }
            // from here on: expected != null && actual != null
            if (expected.length != actual.length) {
                failNotEquals(message, expected, actual);
            }
            for (var i : int = 0; i < expected.length; i++) {
                var foundMatch : Boolean = false;
                var expectedMember : Object = expected[i];
                for (var j : int = 0; j < actual.length; j++) {
                    var actualMember : Object = actual[j];
                    try {
                        assertEquals(expectedMember, actualMember);
                        foundMatch = true;
                        break;
                    }
                    catch (e : AssertionFailedError) {
                        //  no match, try next
                    }
                }
                if (!foundMatch) {
                    failNotEquals("Found no match for " + expectedMember + ";", expected, actual);
                }
            }
        }

		
		static public function assertEqualsObject(...args):void {
			if(args.length < 2) throw new ArgumentError("need at least <expected> and <actual>");
			var b:* = args.pop();
			var a:* = args.pop();
			var message:String = args.pop() || "";
			
			if(a === b) return;
			
			assertSameKeys(a,b);
			
			for(var key:* in a) {
				assertEquals("map entry:" + key, a[key].toString(), b[key].toString());
			}
		}
		static public function assertSameKeys(...args):void {
			if(args.length < 2) throw new ArgumentError("need at least <expected> and <actual>");
			var b:* = args.pop();
			var a:* = args.pop();
			var message:String = args.pop() || "";
			
			assertAllKeys(message + ":missing key:",a,b);
			assertAllKeys(message + ":extra key:",b,a);
		}
		
		static private function assertAllKeys(message:String, a:Object, b:Object):void {
			if(a === b) return;
			for(var key:* in a) 
				if(key in b) continue;
				else fail(message + key);
		}
		
		
		static public function assertIsA(...rest):void {
			if(rest.length < 2) throw new ArgumentError("need at least <expected> and <actual>");
			var objectInstance:* = rest.pop();
			var expectedClass:Class = rest.pop();
			var message:String = rest.pop() || "";
		
			if(objectInstance is expectedClass)
				return;
			fail(message + " expected instance of <"+expectedClass+"> but received object <"+objectInstance+">");
		}
		
		
		
        static private function failNotEquals(message:String, expected:Object, actual:Object):void {
            fail(format(message, expected, actual));
        }

        static private function format(message:String, expected:Object, actual:Object):String {
            var formatted:String = "";
            if(message != null) {
                formatted = message + " ";
            }
            return formatted + "expected:<" + expected + "> but was:<" + actual + ">";
        }
    }
}