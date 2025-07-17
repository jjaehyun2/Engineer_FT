package com.sixfootsoftware.engine {
import com.sixfootsoftware.pitstop.*;
    public class LinkedListBuilder {
        public static function addToLinkedList( prev:DoubleLinkedList, next:DoubleLinkedList ):DoubleLinkedList {
            next.setPrev( prev );
            if ( prev ) {
                prev.setNext( next );
            }
            return next;
        }
        public static function retrieveFirstItem( item:DoubleLinkedList ):DoubleLinkedList {
            while( item.getPrev() ) {
                item = item.getPrev();
            }
            return item;
        }
    }
}