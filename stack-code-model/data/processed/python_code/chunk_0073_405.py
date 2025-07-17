package
{
    public class Dialogue
    {
        public static var tree:Object = {
            name:  "Abraham",
            religion: {name: "Atheist", you: "How did you become atheist?", them: "Simpler without ...uh... mythical creatures.",
                        microexpression: "afraid",
                trust: {health: -0.25, you: "Science is simple. And priests are creeps!", them: "Yeah ... uh ... you know your creeps.", microexpression: "afraid"}, 
                doubt: {you: "You: Faith is simpler than organic chemistry.", them: "Abraham: You're right! Life is mysterious.",
                    microexpression: "joyful", health: 0.25}
            },
            profession: {name: "Biologist", you: "How did you become a biologist?", them: "I like ...poking the mystery of life.",
                trust: {you: "Yes, phlebotomy fascinates me!", them: "It's great fun to ...prick stuff.", microexpression: "afraid", health: -0.25},
                doubt: {you: "You bonded with carbon and hydrogen?", them: "Yeah, and uh, oxygen, too.",
                        microexpression: "afraid", health: 0.25}
            },
            interest: {name: "Cooking", you: "How do you like cooking?", them: "I have this divine recipe for lamb!",
                microexpression: "joyful",
                trust: {you: "I know a bloody mary recipe for lamb!", them: "We could drink that with a steak!",
                    microexpression: "afraid", health: 0.25},
                doubt: {you: "I don't care for lamb, unless it's raw.", them: "Heh.  You are ... rare.",
                    microexpression: "afraid"}
            },
            all: {you: "I feel like I know our chemistry.", them: "Want dinner and see what heats up?",
                doubt: {you: "Holier than thous are not my type.", them: "No... I made a stake just for you...", health: 1.00},
                trust: {you: "Wanna cook me dinner?", them: "How about a stake... in your heart!", health: -1.0}
            }
        }
    }
}