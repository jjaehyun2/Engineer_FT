////////////////////////////////////////////////////////////////////////////////
//
//  Licensed to the Apache Software Foundation (ASF) under one or more
//  contributor license agreements.  See the NOTICE file distributed with
//  this work for additional information regarding copyright ownership.
//  The ASF licenses this file to You under the Apache License, Version 2.0
//  (the "License"); you may not use this file except in compliance with
//  the License.  You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
//
////////////////////////////////////////////////////////////////////////////////
package flashx.textLayout.edit
{
	import flash.utils.getQualifiedClassName;
	
	import flashx.textLayout.conversion.ConverterBase;
	import flashx.textLayout.debug.assert;
	import flashx.textLayout.elements.ContainerFormattedElement;
	import flashx.textLayout.elements.DivElement;
	import flashx.textLayout.elements.FlowElement;
	import flashx.textLayout.elements.FlowGroupElement;
	import flashx.textLayout.elements.FlowLeafElement;
	import flashx.textLayout.elements.LinkElement;
	import flashx.textLayout.elements.ListItemElement;
	import flashx.textLayout.elements.ParagraphElement;
	import flashx.textLayout.elements.SpanElement;
	import flashx.textLayout.elements.SubParagraphGroupElementBase;
	import flashx.textLayout.elements.TCYElement;
	import flashx.textLayout.elements.TextFlow;
	import flashx.textLayout.formats.ITextLayoutFormat;
	import flashx.textLayout.formats.TextLayoutFormat;
	import flashx.textLayout.tlf_internal;

	use namespace tlf_internal;
	
	[ExcludeClass]
	/**
	 * Encapsulates all methods necessary for dynamic editing of a text.  The methods are all static member functions of this class.
     * @private - because we can't make it tlf_internal. Used by the operations package 
	 */	
	public class TextFlowEdit
	{
		tlf_internal static function deleteRange(textFlow:TextFlow, startPos:int, endPos:int):ParagraphElement
		{
			var mergePara:ParagraphElement;

			// If the range to be deleted contains the paragraph end, we may have to merge up the paragraphs when we're done.
			if (endPos > startPos)
			{
				var firstLeafInRange:FlowLeafElement = textFlow.findLeaf(startPos);
				var lastLeafInRange:FlowLeafElement = textFlow.findLeaf(endPos - 1);
				var firstParagraphInRange:ParagraphElement = firstLeafInRange.getParagraph();
				var lastParagraphInRange:ParagraphElement = lastLeafInRange.getParagraph();
				var firstParaStart:int = firstParagraphInRange.getAbsoluteStart();
				var lastParaEnd:int = lastParagraphInRange.getAbsoluteStart() + lastParagraphInRange.textLength;
				// If the selection is inside a single paragraph, merge only if the terminator is included and the start of the paragraph is not.
				// If the two paragraphs are different, merge unless the start and end match exactly
				// Don't merge if the paragraph is an empty paragraph in a list item that has other content (it will just come back again in normalize)
				var doMerge:Boolean = false;
				if (firstParagraphInRange == lastParagraphInRange)
					doMerge = (endPos == lastParaEnd && startPos != firstParaStart);
				else
					doMerge = (startPos != firstParaStart);
				if (doMerge)
				{
					var followingLeaf:FlowLeafElement = textFlow.findLeaf(endPos);
					if (followingLeaf)
					{
						mergePara = followingLeaf.getParagraph();
						if (mergePara.textLength == 1 && mergePara.parent is ListItemElement && mergePara.parent.numChildren > 1)
							mergePara = null;
					}
				}
			}

			deleteRangeInternal(textFlow, startPos, endPos - startPos);
	
			if (mergePara)
			{
				var previousLeaf:FlowLeafElement = mergePara.getFirstLeaf().getPreviousLeaf();
				mergePara = previousLeaf ? previousLeaf.getParagraph() : null;
			}
			
			return mergePara;
		}
		
		private static function deleteRangeInternal(element:FlowGroupElement, relativeStart:int, numToDelete:int):void
		{
			var pendingDeleteStart:int = -1;
			var pendingDeleteCount:int = 0;
			
			var childIndex:int = element.findChildIndexAtPosition(relativeStart);
			while (numToDelete > 0 && childIndex < element.numChildren)
			{
				var child:FlowElement = element.getChildAt(childIndex);
				if (relativeStart <= child.parentRelativeStart && numToDelete >= child.textLength)	// remove the entire child
				{
					if (pendingDeleteStart < 0)
						pendingDeleteStart = childIndex;
					pendingDeleteCount++;
					numToDelete -= child.textLength;
				}
				else // deleting part of the child
				{
					if (pendingDeleteStart >= 0)
					{
						element.replaceChildren(pendingDeleteStart, pendingDeleteStart + pendingDeleteCount);
						childIndex -= pendingDeleteCount;
						pendingDeleteStart = -1;
						pendingDeleteCount = 0;
					}
					var childStart:int = child.parentRelativeStart;
					var childRelativeStart:int = Math.max(relativeStart - childStart, 0);
					var childNumToDelete:int = Math.min(child.textLength - childRelativeStart, numToDelete);
					if (child is SpanElement)
					{
						var span:SpanElement = child as SpanElement;
						span.replaceText(childRelativeStart, childRelativeStart + childNumToDelete, "");
						numToDelete -= childNumToDelete;
					}
					else
					{
						CONFIG::debug { assert (child is FlowGroupElement, "Expected FlowGroupElement"); }
						deleteRangeInternal(child as FlowGroupElement, childRelativeStart, childNumToDelete);
						numToDelete -= childNumToDelete;
					}
				}
				childIndex++
			}
			if (pendingDeleteStart >= 0)
				element.replaceChildren(pendingDeleteStart, pendingDeleteStart + pendingDeleteCount);
		}
				
		// Find the lowest possible FlowElement ancestor of element that can accept prospectiveChild as a child element.
		private static function findLowestPossibleParent(element:FlowGroupElement, prospectiveChild:FlowElement):FlowGroupElement
		{
			while (element && !element.canOwnFlowElement(prospectiveChild))
				element = element.parent;
			return element;
		}
		
		private static function removePasteAttributes(element:FlowElement):void
		{
			if (!element)
				return;
			
			if (element is FlowGroupElement && element.format)
			{
				var flowGroupElement:FlowGroupElement = FlowGroupElement(element);
				if (element.format.getStyle(ConverterBase.MERGE_TO_NEXT_ON_PASTE) !== undefined)
					removePasteAttributes(flowGroupElement.getChildAt(flowGroupElement.numChildren - 1));
			}
			element.setStyle(ConverterBase.MERGE_TO_NEXT_ON_PASTE, undefined);		
		}
		
		// Apply the formatting attributes from the (soon to be) previous element to the insertThis element(s). Used when we're about to 
		// insert the element(s) and we want it to adopt the formatting of its context.
		private static function applyFormatToElement(destinationElement:FlowGroupElement, childIndex:int, insertThis:Object):void
		{
			var formatSourceSibling:FlowElement;
			
			// find the previous sibling and use its formats for the new siblings
			if (childIndex > 0)
				formatSourceSibling = destinationElement.getChildAt(childIndex - 1);
			else
				formatSourceSibling = destinationElement.getChildAt(0);
			if (formatSourceSibling)
			{ 
				var spanFormat:ITextLayoutFormat;
				if (formatSourceSibling is FlowGroupElement)	// take all levels from the sibling down to the root into account
				{
					var element:FlowElement = FlowGroupElement(formatSourceSibling).getLastLeaf();
					var concatFormat:TextLayoutFormat;
					while (element != formatSourceSibling.parent)
					{
						if (element.format)
						{
							if (!concatFormat)
								concatFormat = new TextLayoutFormat(element.format);
							else 
								concatFormat.concatInheritOnly(element.format);
						}
						element = element.parent;
					}
					spanFormat = concatFormat;
				}
				else 
					spanFormat = formatSourceSibling.format;
					
				if (insertThis is Array)
				{
					for each (var scrapElement:FlowElement in insertThis)
						if (scrapElement is FlowLeafElement)
							scrapElement.format = spanFormat;
						else
							scrapElement.format = formatSourceSibling.format;
				}
				else if (insertThis is FlowLeafElement)
					insertThis.format = spanFormat;
				else
					insertThis.format = formatSourceSibling.format;
			}
		}
		/**
		 * Replaces the range of text positions that the <code>startPos</code> and
		 * <code>endPos</code> parameters specify with the <code>textScrap</code> parameter in
		 * <code>theFlow</code>.
		 * <p>To delete elements, pass <code>null</code> for <code>newTextFlow</code>.</p>
		 * <p>To insert an element, pass the same value for <code>startPos</code> and <code>endPos</code>.
		 * <p>The new element will be inserted before the specified index.</p>
		 * <p>To append the TextFlow, pass <code>theFlow.length</code> for <code>startPos</code> and <code>endPos</code>.</p>
		 * 
		 * @param textFlow The TextFlow that is being inserted into.
		 * @param absoluteStart The index value of the first position of the replacement range in the TextFlow.
		 * @param textScrap The TextScrap to be pasted into theFlow.
		 */				
		public static function insertTextScrap(textFlow:TextFlow, absoluteStart:int, textScrap:TextScrap, applyFormat:Boolean):int
		{
			if (!textScrap)
				return absoluteStart;
			
			var scrapFlow:TextFlow = textScrap.textFlow.deepCopy() as TextFlow;
			var scrapLeaf:FlowLeafElement = scrapFlow.getFirstLeaf();

			var destinationLeaf:FlowLeafElement = textFlow.findLeaf(absoluteStart);		
			var insertPosition:int = absoluteStart;
			
			var firstParagraph:Boolean = true;
			var doSplit:Boolean = false;
			
			while (scrapLeaf)
			{
				removePasteAttributes(scrapLeaf);
				var scrapElement:FlowElement = scrapLeaf;		// highest level complete element in the scrap

				// On the first paragraph, it always merges in to the destination paragraph if the destination paragraph has content
				var destinationParagraph:ParagraphElement = destinationLeaf.getParagraph();
				if (firstParagraph && (destinationParagraph.textLength > 1 || applyFormat))
				{
					var scrapParagraph:ParagraphElement = scrapLeaf.getParagraph();
					if (!scrapParagraph.format || scrapParagraph.format.getStyle(ConverterBase.MERGE_TO_NEXT_ON_PASTE) === undefined)
						doSplit = true;
					scrapElement = scrapParagraph.getChildAt(0);
				}
				else
				{
					if (applyFormat && firstParagraph)
					{
						destinationElement = findLowestPossibleParent(destinationLeaf.parent, scrapElement);
						var currentIndex:int = destinationElement.findChildIndexAtPosition(insertPosition - destinationElement.getAbsoluteStart());
						applyFormatToElement(destinationElement, currentIndex, scrapElement);
					}
					// Normally the root element of the scrap is marked as partial, but if not, just assume that its partial (we never paste the TextFlow element)
					while (scrapElement && scrapElement.parent && (!scrapElement.parent.format || scrapElement.parent.format.getStyle(ConverterBase.MERGE_TO_NEXT_ON_PASTE) === undefined) && !(scrapElement.parent is TextFlow))
						scrapElement = scrapElement.parent;
				}
				

				// Find the lowest level parent in the TextFlow that can accept the scrapElement as a child. 
				// If necessary, copy higher up the scrapElement hierarchy to find a match.
				var destinationElement:FlowGroupElement = findLowestPossibleParent(destinationLeaf.parent, scrapElement);
				while (!destinationElement)
				{
					// Nothing in the TextFlow element hierarchy can accept the incoming scrap element.
					// Go up the scrapElement's hierarchy of partial nodes until we find one that can be inserted.
					scrapElement = scrapElement.parent;
					CONFIG::debug { assert(scrapElement != null, "Couldn't find scrapElement that could be pasted"); }
					destinationElement = findLowestPossibleParent(destinationLeaf.parent, scrapElement);
				}
				CONFIG::debug { assert(destinationElement != null, "insertTextScrap failed to find a FlowElement that can take the scrap element"); }
				
				removePasteAttributes(scrapElement);

				var destinationStart:int = destinationElement.getAbsoluteStart();
				if (firstParagraph && doSplit)
				{
					// Split the paragraph, and merge the scrap paragraph to the end of the first paragraph of the destination
					CONFIG::debug { assert(destinationElement is ParagraphElement, "We should be splitting a paragraph"); }
					ModelEdit.splitElement(textFlow, destinationElement, insertPosition - destinationStart);
					var scrapParent:FlowGroupElement = scrapElement.parent;
					var scrapChildren:Array = scrapParent.mxmlChildren;
					scrapParent.replaceChildren(0, scrapParent.numChildren);
					if (scrapParent.parent)
						scrapParent.parent.removeChild(scrapParent);
					if (applyFormat)
						applyFormatToElement(destinationElement, destinationElement.numChildren, scrapChildren);
					destinationElement.replaceChildren(destinationElement.numChildren, destinationElement.numChildren, scrapChildren);
					scrapElement = destinationElement.getChildAt(destinationElement.numChildren - 1);		// last span pasted, so we'll paste next after this
					firstParagraph = false;
				}
				else
				{
					// We're going to add scrapElement as a child of destinationElement at the insertPosition.
					// Split the children of destinationElement if necessary.
					var childIndex:int = destinationElement.findChildIndexAtPosition(insertPosition - destinationElement.getAbsoluteStart());
					var child:FlowElement = destinationElement.getChildAt(childIndex);
					var childStart:int = child.getAbsoluteStart();
					if (insertPosition == childStart + child.textLength)
						++childIndex;
					else if (insertPosition > childStart)
					{
						if (child is FlowLeafElement)
							child.splitAtPosition(insertPosition - childStart);
						else
							ModelEdit.splitElement(textFlow, child as FlowGroupElement, insertPosition - childStart);
						++childIndex;
					}
					if (applyFormat)
						applyFormatToElement(destinationElement, childIndex, scrapElement);
					destinationElement.replaceChildren(childIndex, childIndex, scrapElement);
				}

				
				// Advance to the next destination leaf
				destinationLeaf = (scrapElement is FlowLeafElement) ? FlowLeafElement(scrapElement).getNextLeaf() : FlowGroupElement(scrapElement).getLastLeaf().getNextLeaf();
				insertPosition = destinationLeaf ? destinationLeaf.getAbsoluteStart() : textFlow.textLength - 1;
				
				scrapLeaf = scrapFlow.getFirstLeaf();
			}
			
			return insertPosition;
		}

		/**
		 * Creates a TCY run out of the selected positions.
		 * @param theFlow The TextFlow of interest.
		 * @param startPos The index value of the first position of the TextFlow to be turned into a TCY run.
		 * @param endPos The index value following the end position of the TextFlow to be turned into a TCY run.
		 */	
		public static function makeTCY(theFlow:TextFlow, startPos:int, endPos:int):Boolean
		{
			var madeTCY:Boolean = true;
			var curPara:ParagraphElement = theFlow.findAbsoluteParagraph(startPos);
			if(!curPara)
				return false;
			while(curPara)
			{
				var paraEnd:int = curPara.getAbsoluteStart() + curPara.textLength;
				var curEndPos:int = Math.min(paraEnd, endPos);
				
				//we have an entire para selected and the para only contains a kParaTerminator char, which cannot be
				//made into TCY. 
				if(canInsertSPBlock(theFlow, startPos, curEndPos, TCYElement) && curPara.textLength > 1)
				{
					var new_tcyElem:TCYElement = new TCYElement();
					
					//don't hide an error!
					madeTCY = madeTCY && insertNewSPBlock(theFlow, startPos, curEndPos, new_tcyElem, TCYElement);
				}
				else
					madeTCY = false;
				
				if(paraEnd < endPos)
				{
					curPara = theFlow.findAbsoluteParagraph(curEndPos);	
					startPos = curEndPos;
				}
				else
					curPara = null;
			}
			
			return madeTCY;
		}
		
		/**
		 * Creates one or more LinkElements out of the selected positions. It will go through
		 * every paragraph within the selected position and make links.
		 * @param theFlow The TextFlow of interest.
		 * @param startPos The index value of the first position of the TextFlow to be turned into a link.
		 * @param endPos The index value following the end position of the TextFlow to be turned into a link.
		 * @param urlString The url string to be associated with the link.
		 */			
		public static function makeLink(theFlow:TextFlow, startPos:int, endPos:int, urlString:String, target:String):Boolean
		{
			var madeLink:Boolean = true;
			var curPara:ParagraphElement = theFlow.findAbsoluteParagraph(startPos);
			if(!curPara)
				return false;
				
			while(curPara)
			{
				var paraEnd:int = curPara.getAbsoluteStart() + curPara.textLength;
				var curEndPos:int = Math.min(paraEnd, endPos);
				var linkEndPos:int = (curEndPos == paraEnd) ? (curEndPos - 1) : curEndPos;
				if (linkEndPos > startPos)
				{
					//if the end of the paragraph is < endPos, we are going across bounds
					if(!canInsertSPBlock(theFlow, startPos, linkEndPos, LinkElement))
					{
						return false;
					}
				
					var newLinkElement:LinkElement = new LinkElement();
					newLinkElement.href = urlString;
					newLinkElement.target = target;
				
					//don't hide an error!
					madeLink = madeLink && insertNewSPBlock(theFlow, startPos, linkEndPos, newLinkElement, LinkElement);
				}	
				if(paraEnd < endPos)
				{
					curPara = theFlow.findAbsoluteParagraph(curEndPos);	
					startPos = curEndPos;
				}
				else
					curPara = null;
			}
			
			return madeLink;
		}
		
		
		/**
		 * Removes the TCY block at the selected positions. 
		 * @param theFlow The TextFlow of interest.
		 * @param startPos The index value of the first position of the TextFlow.
		 * @param endPos The index value following the end position of the TextFlow.
		 */			
		public static function removeTCY(theFlow:TextFlow, startPos:int, endPos:int):Boolean
		{
			if (endPos <= startPos)
			{
				return false;
			}
			
			return findAndRemoveFlowGroupElement(theFlow, startPos, endPos, TCYElement);
		}
		
		/**
		 * Removes all LinkElements under the selected positions. It will go through
		 * every paragraph within the selected position and remove any link.
		 * @param theFlow The TextFlow of interest.
		 * @param startPos The index value of the first position of the TextFlow.
		 * @param endPos The index value following the end position of the TextFlow.
		 */			
		public static function removeLink(theFlow:TextFlow, startPos:int, endPos:int):Boolean
		{
			if (endPos <= startPos)
			{
				return false;
			}
			
			return findAndRemoveFlowGroupElement(theFlow, startPos, endPos, LinkElement);
		}
		
		/**
		 * @private
		 * insertNewSPBlock - add a SubParagraphGroupElementBase (spg) to <code>theFlow</code> at the indicies specified by <code>startPos</code> and
		 * <code>endPos</code>.  The <code>newSPB</code> will take ownership of any FlowElements within the range and will split them
		 * as needed.  If the parent of the FlowGroupElement indicated by <code>startPos</code> is the same as <code>spgClass</code> then
		 * the method fails and returns false because a spg cannot own children of the same class as itself.  Any spg of type <code>spgClass</code>
		 * found within the indicies, however, is subsumed into <code>newSPB</code>, effectively replacing it.
		 *
		 * @param theFlow:TextFlow - The TextFlow that is the destination for the newSPB
		 * @param startPos:int - The absolute index value of the first position of the range in the TextFlow to perform the insertion.
		 * @param endPos:int - The index value following the end position of the range in the TextFlow to perform the insertion.
		 * @param newSPB:SubParagraphGroupElementBase - The new SubParagraphElement which is to be added into theFlow.
		 * @param spgClass:Class - the class of the fbe we intend to add.
		 * 
		 * Examples: Simple and complex where insertion is of <code>spgClass</code> b.  Selection is l~o
		 *		1) <a><span>ghijklmnop</span></a>
		 * 		2) <a><span>ghij</span><b><span>klm</span></b><span>nop</span></a>
		 * 		3) <a><span>ghijk</span><c><span>lmn</span></c><span>op</span></a>
		 * 
		 */
		tlf_internal static function insertNewSPBlock(theFlow:TextFlow, startPos:int, endPos:int, newSPB:SubParagraphGroupElementBase, spgClass:Class):Boolean
		{
			var curPos:int = startPos;
			var curFBE:FlowGroupElement = theFlow.findAbsoluteFlowGroupElement(curPos);
			var elementIdx:int = 0;
			
			CONFIG::debug{ assert(curFBE != null, "No FBE at location curPos(" + curPos + ")!");}
			
			//if we are at the last "real" glyph of the paragraph, include the terminator.
			var paraEl:ParagraphElement = curFBE.getParagraph();
			if(endPos == (paraEl.getAbsoluteStart() + paraEl.textLength - 1))
				++endPos;
			
			//before processing this any further, we need to make sure that we are not
			//splitting a spg which is contained within the same type of spg as the curFBE's parent.
			//for example, if we had a tcyElement inside a linkElement, then we cannot allow a link element
			//to be made within the tcyElement as the link would not function.  As a rule, a SubParagraphElement
			//cannot own a child of the same class.
			//
			//However, if the curFBE is parented by a spg and the objects have the same start and end, then we are doing
			//a replace and we're not splitting the parent. Check if the bounds are the same and if so, don't skip it...
			var parentStart:int = curFBE.parent.getAbsoluteStart();
			var curFBEStart:int = curFBE.getAbsoluteStart();
			if(curFBE.parent && curFBE.parent is spgClass && 
				!(parentStart == curFBEStart && parentStart + curFBE.parent.textLength == curFBEStart + curFBE.textLength))
			{
				return false;
			}
			
			//entire FBE is selected and is not a paragraph, get its parent.
			if(!(curFBE is ParagraphElement) && curPos == curFBEStart && curPos + curFBE.textLength <= endPos)
			{
				elementIdx = curFBE.parent.getChildIndex(curFBE);
				curFBE = curFBE.parent;
			}
			//first, if the curFBE is of the same class as the newSPB, then we need to split it to allow for insertion
			//of the new one IF the start position is > the start of the curFBE
			//
			//running example after this block:
			//	1) <a><span>ghijk</span><span>lmnop</span></a>
			//	2) <a><span>ghij</span><b><span>k</span></b><b><span>lm</span></b><span>nop</span></a>
			//	3) <a><span>ghijk</span><c><span>lmn</span></c><span>op</span></a> - no change
			if(curPos >= curFBEStart)
			{
				if(!(curFBE is spgClass))
					elementIdx = findAndSplitElement(curFBE, elementIdx, curPos, true);
				else
				{
					elementIdx = findAndSplitElement(curFBE.parent, curFBE.parent.getChildIndex(curFBE), curPos, false);
					curFBE = curFBE.parent;
				}
			}
			
			//now that the curFBE has been split, we want to insert the newSPB into the flow and then start absorbing the
			//contents...
			//running example after this block:
			//	1) <a><span>ghijk</span><b></b><span>lmnop</span></a>
			//	2) <a><span>ghij</span><b><span>k</span></b><b></b><b><span>lm</span></b><span>nop</span></a>
			//	3) <a><span>ghijk</span><b></b><c><span>lmn</span></c><span>op</span></a> - no change
			//
		//	we need another use case here where selection is entire sbp and selection runs from the head of a spg to
		//	part way through it - so that a) does into parent and b) goes into spg
			
			// if this is case 2, then the new element must go into the parent...
			if(curFBE is spgClass)
			{
				curFBEStart = curFBE.getAbsoluteStart();
				elementIdx = curFBE.parent.getChildIndex(curFBE);
				if(curPos > curFBEStart)//we're splitting the element, not replacing it...
					elementIdx += 1;
				
				//if the spg, curFBE is entirely selected then we want to use the parent, not the item itself.
				while(endPos >= curFBEStart + curFBE.textLength)
				{
					//we need access to the parent, which contains both the start and end not the FBE we just split
					curFBE = curFBE.parent;
				}
				curFBE.replaceChildren(elementIdx, elementIdx, newSPB);
			}
			else
			{
				//we're inserting into the curFBE
				curFBE.replaceChildren(elementIdx, elementIdx, newSPB);
			}
			
			//see subsumeElementsToSPBlock to see effects on running example
			subsumeElementsToSPBlock(curFBE, elementIdx + 1, curPos, endPos, newSPB, spgClass);
			
			return true;
		}
		
		
		/**
		 * @private
		 * splitElement - split <code>elem</code> at the relative index of <code>splitPos</code>.  If <code>splitSubBlockContents</code>
		 * is true, split the contents of <code>elem</code> if it is a SubParagraphGroupElementBase, otherwise just split <code>elem</code>
		 * 
		 * @param elem:FlowElement - the FlowElement to split
		 * @param splitPos:int - The elem relative index indicating where to split
		 * @param splitSubBlockContents:Boolean - boolean indicating whether a SubParagraphGroupElementBase is to be split OR that it's contents
		 * should be split.  For example, are we splitting a link or are we splitting the child of the link
		 * 
		 * <spg><span>ABCDEF</span></spg>
		 * 
		 * if <code>splitPos</code> indicated index between C and D, then if <code>splitSubBlockContents</code> equals true,
		 * result is:
		 * 
		 * <spg><span>ABC</span><span>DEF</span></spg>
		 * 
		 * if <code>splitSubBlockContents</code> equals false, result is:
		 * 
		 * <spg><span>ABC</span></spg><spg><span>DEF</span></spg>
		 */
		tlf_internal static function splitElement(elem:FlowElement, splitPos:int, splitSubBlockContents:Boolean):void
		{
			CONFIG::debug{ assert(splitPos < elem.textLength, "trying to splic FlowElement at illegal index!"); }
			if (elem is SpanElement)
			{
				SpanElement(elem).splitAtPosition(splitPos);
			}
			else if(elem is SubParagraphGroupElementBase && splitSubBlockContents)
			{
				var subBlock:SubParagraphGroupElementBase = SubParagraphGroupElementBase(elem);
				// Split the SpanElement of the block at splitPos.  If the item at the splitPos is not a SpanElement, no action occurs.
				var tempElem:SpanElement = subBlock.findLeaf(splitPos) as SpanElement;
				if (tempElem)
					tempElem.splitAtPosition(splitPos - tempElem.getElementRelativeStart(subBlock));
			}
			else if (elem is FlowGroupElement)
			{
				FlowGroupElement(elem).splitAtPosition(splitPos);
			}
			else
			{
				CONFIG::debug { assert(false, "Trying to split on an illegal FlowElement"); }				
			}
		}
		
		/**
		 * @private
		 * findAndSplitElement - starting at the child <code>elementIdx</code> of <code>fbe</code>, iterate
		 * through the elements untill we find the one located at the aboslute index of <code>startIdx</code>. Upon
		 * locating the child, split either the element itself OR its children based on the value of <code>splitSubBlockContents</code>
		 * 
		 * @param fbe:FlowGroupElement - the FBE into which the newSPB is being inserted.
		 * @param elementIdx:int - The index into the <code>fbe's</code> child list to start
		 * @param startIdx:int - The absolute index value into the TextFlow.
		 * @param splitSubBlockContents:Boolean - boolean indicating whether a subElement is to be split OR that it's contents
		 * should be split.  For example, are we splitting a link or are we splitting the child of the link
		 * 
		 * <p>ZYX<link>ABCDEF</link>123</p>
		 * 
		 * if we are inserting a TCY into the link, splitSubBlockContents should be false. We want to split the span ABCDEF such that result is:
		 * <p>ZYX<link>AB<tcy>CD</tcy>EF</link>123</p>
		 * 
		 * if we are creating a new link from X to B, then we want the link to split and splitSubBlockContents should be false:
		 * 
		 * <p>ZY<link>XAB</link><link>CDEF</link>123</p>
		 * 
		 * @return int - the index of the last child of <code>fbe</code> processed.
		 */
		tlf_internal static function findAndSplitElement(fbe:FlowGroupElement, elementIdx:int, startIdx:int, splitSubBlockContents:Boolean):int
		{
			var curFlowEl:FlowElement = null;
			var curIndexInPar:int = startIdx - fbe.getAbsoluteStart();
			
			while(elementIdx < fbe.numChildren)
			{
				curFlowEl = fbe.getChildAt(elementIdx);
				if (curIndexInPar == curFlowEl.parentRelativeStart)
					return elementIdx;
				if ((curIndexInPar > curFlowEl.parentRelativeStart) && (curIndexInPar < curFlowEl.parentRelativeEnd))
				{
					splitElement(curFlowEl, curIndexInPar - curFlowEl.parentRelativeStart, splitSubBlockContents); 
				}
				++elementIdx;
			}
			return elementIdx;
		}
		
		/**
		 * @private
		 * subsumeElementsToSPBlock - incorporates all elements of <code>parentFBE</code> into
		 * the <code>newSPB</code> between the <code>curPos</code> and <code>endPos</code>.  If a child of
		 * <code>parentFBE</code> is of type <code>spgClass</code> then the child's contents are removed from the child,
		 * added to the <code>newSPB</code>, the child is then removed from the <code>parentFBE</code>
		 * 
		 * @param parentFBE:FlowGroupElement - the FBE into which the newSPB is being inserted.
		 * @param startPos:int - The index value of the first position of the replacement range in the TextFlow.
		 * @param endPos:int - The index value following the end position of the replacement range in the TextFlow.
		 * @param newSPB:SubParagraphGroupElementBase - the new SubParagraphGroupElementBase we intend to insert.
		 * @param spgClass:Class - the class of the fbe we intend to insert.
		 * 
		 * @return int - the aboslute index in the text flow after insertion.
		 * 
		 *  Examples: Simple and complex where insertion is of <code>spgClass</class> b.  Selection is l~o
		 *		1) <a><span>ghijk</span><b></b><span>lmnop</span></a>
		 *		2) <a><span>ghij</span><b><span>k</span></b><b></b><b><span>lm</span></b><span>nop</span></a>
		 * 
		 * 	parentFBE = <a>
		 *  elementIdx = 1) 2, 2) 3
		 *  curPos = 5
		 *  endPos = 9
		 *  newSPB is of type <b>
		 */
		tlf_internal static function subsumeElementsToSPBlock(parentFBE:FlowGroupElement, elementIdx:int, curPos:int, endPos:int, newSPB:SubParagraphGroupElementBase, spgClass:Class):int
		{
			var curFlowEl:FlowElement = null;
			
			//if we have an invalid index, then skip out.  elementIdx will always point one
			//element beyond the one we are inserting....
			if(elementIdx >= parentFBE.numChildren)
				return curPos;
			
			while (curPos < endPos)
			{
				//running example: curFlowEl is the element immediately after the inserted newSPB:
				//	1) <a><span>ghijk</span><b></b><span>lmnop</span></a>
				//		points to span-lmnop
				//	2) <a><span>ghij</span><b><span>k</span></b><b></b><b><span>lm</span></b><span>nop</span></a>
				//		points to b-lm
				curFlowEl = parentFBE.getChildAt(elementIdx);
				
				//if the curFlowEl is of the Class we are adding (spgClass), and the entire thing is selected,
				//then we are adding the entire block, but not spliting it - perform the split on the next block
				
				//I think this can be safely removed from here as ownership of contents is handled below.
				//leaving in commented out code in case we need to revert - gak 05.01.08
			/*	if(curFlowEl is spgClass && curPos == curFlowEl.getAbsoluteStart() && curFlowEl.getAbsoluteStart() + curFlowEl.textLength <= endPos)
				{
					curPos = parentFBE.getAbsoluteStart() + parentFBE.textLength;
					continue;
				}*/
				
				//if the endPos is less than the length of the curFlowEl, then we need to split it.
				//if the curFlowEl is NOT of class type spgClass, then we need to break it
				//
				//Use case: splitting a link in two (or three as will be the result with head and tail sharing
				//attributes...
				//running example 1 hits this, but 2 does not. Using variation of 2:
				//
				// example: 1) <a><span>ghijk</span><b></b><span>lmnop</span></a>
				// 			2a) <a><span>fo</span><b></b><b><span>obar</span></b></a> - selection: from o~a
				//
				// after this code:
				//			1) <a><span>ghijk</span><b></b><span>lmno</span><span>p</span></a>
				//			2a) <a><span>fo</span><b></b><b><span>oba</span></b><b><span>or</span></b></a>
				if ((curPos + curFlowEl.textLength) > endPos)
				{
					splitElement(curFlowEl, endPos - curFlowEl.getAbsoluteStart(), !(curFlowEl is spgClass));  //changed to curFlowEl from newSPB as newSPB should be of type spgClass
				}
				
				//add the length before replacing the elements
				curPos += curFlowEl.textLength;
				
				//running example: after parentFBE.replaceChildren
				//
				//	1) curFlowEl = <span>lmno</span>
				//		<a><span>ghijk</span><b></b>{curFlowEl}<span>p</span></a>
				//
				//	2) curFlowEl = <b><span>lm</span></b>
				//		<a><span>ghij</span><b><span>k</span></b><b></b>{curFlowEl}<span>nop</span></a>
				parentFBE.replaceChildren(elementIdx, elementIdx + 1);
				
				//if the curFlowEl is of type spgClass, then we need to take its children and
				//add them to the newSPB because a spg cannot contain a child of the same class
				//as itself
				//
				// exmaple: 2) curFlowEl = <b><span>lm</span></b>
				if (curFlowEl is spgClass)
				{
					var subBlock:SubParagraphGroupElementBase = curFlowEl as SubParagraphGroupElementBase;
					//elementCount == 1 - <span>lm</span>
					while (subBlock.numChildren > 0)
					{
						//fe[0] = <span>lm</span>
						var fe:FlowElement = subBlock.getChildAt(0);
						//<span></span>
						subBlock.replaceChildren(0, 1);
						//<b><span>lm</span></b>
						newSPB.replaceChildren(newSPB.numChildren, newSPB.numChildren, fe);
					}
					//when compelete, example 2 is:
					//2) <a><span>ghij</span><b><span>k</span></b><b><span>lm</span></b><span>nop</span></a>
				}
				else 
				{
					//example 1, curFlowEl is <span>lmno</span>, so this is not hit
					//
					// extending element <a> from foo~other
					// <a>foo</a><b>bar<a>other</a><b>
					// curFlowEl = <b>bar<a>other</a><b>
					//
					// since <b> is a spg, we need to walk it's contents and remove any <a> elements
					if(curFlowEl is SubParagraphGroupElementBase)
					{
						//we need to dive into this spgClass and remove any fbes of type spgClass
						//pass in the curFlowEl as the newSPB, remove any spgs of type spgClass, then 
						//perform the replace on the newSPB passed in here
						//
						//ignore the return value of the recursive call as the length has already been
						//accounted for above
						flushSPBlock(curFlowEl as SubParagraphGroupElementBase, spgClass);
					}
					newSPB.replaceChildren(newSPB.numChildren, newSPB.numChildren, curFlowEl);
					
					if(newSPB.numChildren == 1 && curFlowEl is SubParagraphGroupElementBase)
					{
						var childSPGE:SubParagraphGroupElementBase = curFlowEl as SubParagraphGroupElementBase;
						//running example:
						//a.precedence = 800, tcy.precedence = kMinSPGEPrecedence
						//this = <tcy><a><span>fooBar</span></a><tcy>
						//childSPGE = <a><span>fooBar</span></a>
						if(childSPGE.textLength == newSPB.textLength && (curPos >= endPos))
						{
							CONFIG::debug { assert(childSPGE.precedence != newSPB.precedence, "normalizeRange found two equal SPGEs"); }
	
							//if the child's precedence is higher than mine, I need to swap
							if(childSPGE.precedence > newSPB.precedence)
							{
								//first, remove the child
								//this = <tcy></tcy>
								newSPB.replaceChildren(0,1);
								
								//we need to flop this object for the child
								while(childSPGE.numChildren > 0)
								{
									//tempFE = <span>fooBar</span>
									var tempFE:FlowElement = childSPGE.getChildAt(0);
									//child = <a></a>
									childSPGE.replaceChildren(0,1);
									//this = <tcy><span>fooBar</span></tcy>
									newSPB.replaceChildren(newSPB.numChildren, newSPB.numChildren, tempFE);
								}
								
								var myIdx:int = newSPB.parent.getChildIndex(newSPB);
								CONFIG::debug{ assert(myIdx >= 0, "Invalid index!  How can a SubParagraphGroupElementBase normalizing not have a parent!"); }
								
								//add childSPGE in my place
								newSPB.parent.replaceChildren(myIdx, myIdx + 1, childSPGE)
								
								//childSPGE = <tcy><a><span>fooBar</span></a></tcy>
								childSPGE.replaceChildren(0,0,newSPB);
							}
						}
					}
				}
				
			}
	
			return curPos;
		}
		
		/**
		 * @private
		 * findAndRemoveFlowGroupElement 
		 *
		 * @param theFlow The TextFlow that is containing the elements to remove.
		 * @param startPos The index value of the first position of the range in the TextFlow where we want to perform removal.
		 * @param endPos The index value following the end position of the range in the TextFlow where we want to perform removal.
		 * @param fbeClass Class the class of the fbe we intend to remove.
		 * 
		 * Walks through the elements of <code>theFlow</code> looking for any FlowGroupElement of type <code>fbeClass</class>
		 * On finding one, it removes the FBE's contents and adds them back into the FBE's parent.  If the class of object is
		 * embedded within another spg and this removal would break the parent spg, then the method does nothing.
		 * 
		 * Example:
		 * 	<link>ABC<tcy>DEF</tcy>GHI</link>
		 * 	Selection is on E and removal of link is attempted.
		 * 	Because E is a child of a spg (tcy), and removing the link from E would split the parent spg (link),
		 *  the action is disallowed.
		 * 
		 * Running example:
		 * 	1) <link><tcy><span>foo</span></tcy><span>bar</span></link>
		 * @return Boolean - true if items are removed or none are found.  false if operation is illegal.
		 */ 
		tlf_internal static function findAndRemoveFlowGroupElement(theFlow:TextFlow, startPos:int, endPos:int, fbeClass:Class):Boolean
		{
			var curPos:int = startPos;
			var curEl:FlowElement;
			
			//walk through the elements
			while (curPos < endPos)
			{
				var containerFBE:FlowGroupElement = theFlow.findAbsoluteFlowGroupElement(curPos);
				
				//if the start of the parent is the same as the start of the current containerFBE, then
				//we potentially have the wrong object.  We need to walk up the parents until we get to
				//the one which starts at our start AND is the topmost object at that index.
				//example: <a><b>foo</b> bar</a> - getting the object at "f" will yield the <b> element, not <a>
				while(containerFBE.parent && containerFBE.parent.getAbsoluteStart() == containerFBE.getAbsoluteStart() && 
					!(containerFBE.parent is ParagraphElement) && !(containerFBE is ParagraphElement)) //don't go beyond paragraph
				{
					containerFBE = containerFBE.parent;
				}
				
				//if the absoluteFBE is the item we are trying to remove, we need to work with its parent, so
				//reassign containerFBE.  For example, if an entire link were selected, we'd need to get it's parent to
				//perform the removal
				if(containerFBE is fbeClass)
					containerFBE = containerFBE.parent;
					
				//before processing this any further, we need to make sure that we are not
				//splitting a spg which is contained within the same type of spg as the curFBE's parent.
				//for example, if we had a tcyElement inside a linkElement, then we cannot allow a link element
				//to be broken within the tcyElement as the link would have to split the TCY.
				var ancestorOfFBE:FlowGroupElement = containerFBE.parent;
				while(ancestorOfFBE != null && !(ancestorOfFBE is fbeClass))
				{
					if(ancestorOfFBE.parent is fbeClass)
					{
						return false;
					}
					ancestorOfFBE = ancestorOfFBE.parent;
				}
				
				//if this is a sbe block contained in another sbe, and it is entire within the 
				//selection bounds, we need to use the parent sbe's container.  If it is splitting
				//the child sbe, we don't allow this and it is handled later...
				var containerFBEStart:int = containerFBE.getAbsoluteStart();
				if(ancestorOfFBE is fbeClass && (containerFBEStart >= curPos && containerFBEStart + containerFBE.textLength <= endPos))
					containerFBE = ancestorOfFBE.parent;
					
				var childIdx:int = containerFBE.findChildIndexAtPosition(curPos - containerFBEStart);
				curEl = containerFBE.getChildAt(childIdx);
				if(curEl is fbeClass)
				{
					CONFIG::debug{ assert(curEl is SubParagraphGroupElementBase, "Wrong FBE type!  Trying to remove illeage FBE!"); }
					var curFBE:FlowGroupElement = curEl as FlowGroupElement;
					
					//get it's parent and the index of the curFBE
					var parentBlock:FlowGroupElement = curFBE.parent;
					var idxInParent:int = parentBlock.getChildIndex(curFBE);
					
					//if the curPos is not at the head of the SPB, then we need to split it here
					//curFBE will point to the FBE starting at curPos
					if(curPos > curFBE.getAbsoluteStart())
					{
						splitElement(curFBE, curPos - curFBE.getAbsoluteStart(), false);
						curPos = curFBE.getAbsoluteStart() + curFBE.textLength;
						continue;
					}
					
					//if curFBE goes beyond the endPos, then we need to split off the tail.
					if (curFBE.getAbsoluteStart() + curFBE.textLength > endPos)
					{
						splitElement(curFBE, endPos - curFBE.getAbsoluteStart(), false);
					}
				
					//apply the length of the curFBE to the curPos tracker.  Do this before 
					//removing the contents or it will be 0!
					curPos = curFBE.getAbsoluteStart() + curFBE.textLength;
					
					//walk all the contents of the FBE into it's parent container
					while (curFBE.numChildren > 0)
					{
						var childFE:FlowElement = curFBE.getChildAt(0);
						curFBE.replaceChildren(0, 1);
						parentBlock.replaceChildren(idxInParent, idxInParent, childFE);
						idxInParent++; 
					}
					
					//remove the curFBE
					parentBlock.replaceChildren(idxInParent, idxInParent + 1);
				}
				else if(curEl is SubParagraphGroupElementBase) //check all the parents...
				{
					var curSPB:SubParagraphGroupElementBase = SubParagraphGroupElementBase(curEl);
					if(curSPB.numChildren == 1)
						curPos = curSPB.getAbsoluteStart() + curSPB.textLength;
					else
					{
						curEl = curSPB.getChildAt(curSPB.findChildIndexAtPosition(curPos - curSPB.getAbsoluteStart()));
						curPos = curEl.getAbsoluteStart() + curEl.textLength;
					}
				}
				else
				{
					//the current block isn't the type we're looking for, so just go to the end of the
					//FlowElement and continue
					curPos = curEl.getAbsoluteStart() + curEl.textLength;
				}
				
			}
			
			return true;
		}
		
		/**
		 * @private
		 * canInsertSPBlock 
		 * 
		 * validate that we a valid selection to allow for insertion of a subBlock.  The rules are as
		 * follows:
		 * 	endPos > start
		 * 	the new block will not span multiple paragraphs
		 *  if the block is going into a SubParagraphGroupElementBase, it must not split the block:
		 * 		example:  Text 		- ABCDEFG with a link on CDE
		 * 		legal new Block		- D, CD, CDE, [n-chars]CDE[n1-chars]
		 * 		illegal new Block 	- [1 + n-chars]C[D], [D]E[1 + n-chars]
		 * 			exception - if the newBlock is the same class as the one we are trying to split
		 * 			then we can truncate the original and add its contents to the new one, or extend it
		 * 			as appropriate
		 * 
		 * @param theFlow The TextFlow that is containing the elements to validate.
		 * @param startPos The index value of the first position of the range in the TextFlow to test.
		 * @param endPos The index value following the end position of the range in the TextFlow to test.
		 * @param blockClass Class the class of the fbe we intend to insert.
		 */
		tlf_internal static function canInsertSPBlock(theFlow:TextFlow, startPos:int, endPos:int, blockClass:Class):Boolean
		{
			if(endPos <= startPos)
				return false;
				
			var anchorFBE:FlowGroupElement = theFlow.findAbsoluteFlowGroupElement(startPos);
			if(anchorFBE.getParentByType(blockClass))
				anchorFBE = anchorFBE.getParentByType(blockClass) as FlowGroupElement;
				
			var tailFBE:FlowGroupElement = theFlow.findAbsoluteFlowGroupElement(endPos - 1);
			if(tailFBE.getParentByType(blockClass))
				tailFBE = tailFBE.getParentByType(blockClass) as FlowGroupElement;
			
			//if these are the same FBEs then we are safe to insert a SubParagraphGroupElementBase
			if(anchorFBE == tailFBE)
				return true;
			//make sure that the two FBEs belong to the same paragraph!
			else if(anchorFBE.getParagraph() != tailFBE.getParagraph())
				return false;
			else if(anchorFBE is blockClass && tailFBE is blockClass)//they're the same class, OK to merge, split, etc...
				return true;
			else if(anchorFBE is SubParagraphGroupElementBase && !(anchorFBE is blockClass))
			{
				var anchorStart:int = anchorFBE.getAbsoluteStart();
				if(startPos > anchorStart && endPos > anchorStart + anchorFBE.textLength)
					return false;
			}
			else if((anchorFBE.parent is SubParagraphGroupElementBase || tailFBE.parent is SubParagraphGroupElementBase)
				&& anchorFBE.parent != tailFBE.parent)
			{
				//if either FBE parent is a SPGE and they are not the same, prevent the split.  
				return false;
			}	
			
			//if we got here, then the anchorFBE is OK, check the tail.  If endPos is pointing to the
			//0th character of a FlowGroupElement, we don't need to worry about the tail.
			if(tailFBE is SubParagraphGroupElementBase && !(tailFBE is blockClass) && endPos > tailFBE.getAbsoluteStart())
			{
				var tailStart:int = tailFBE.getAbsoluteStart();
				if(startPos < tailStart && endPos < tailStart + tailFBE.textLength)
					return false;
			}	
			return true;
		}
		
		/**
		 * @private flushSPBlock recursively walk a spg looking for elements of type spgClass.  On finding one,
		 * remove it's children and then remove the object itself.  Since spg's cannot hold children of the same type
		 * as themselves, recursion is only needed for spg's of a class other than that of spgClass.
		 * 
		 * example: subPB = <b>bar<a>other</a><b> extending an <a> element to include all of "other"
		 */ 
		tlf_internal static function flushSPBlock(subPB:SubParagraphGroupElementBase, spgClass:Class):void
		{
			var subParaIter:int = 0;
	
			//example, subPB has 2 elements, <span>bar</span> and <a><span>other</span></a>
			while(subParaIter < subPB.numChildren)
			{
				//subParaIter == 0, subFE = <span>bar</span> skip the FE and move to next
				//subParaIter == 1, subFE = <a><span>other</span></a> - is a spgClass
				var subFE:FlowElement = subPB.getChildAt(subParaIter);
				if(subFE is spgClass)
				{
					//subParaIter == 1, subFE = <a><span>other</span></a>
					var subChildFBE:FlowGroupElement = subFE as FlowGroupElement;
					while(subChildFBE.numChildren > 0)
					{
						//subFEChild = <span>other</span>
						var subFEChild:FlowElement = subChildFBE.getChildAt(0);
						//subFEChild = <a></a>
						subChildFBE.replaceChildren(0, 1);
						//subPB = <b>barother<a></a><b>
						subPB.replaceChildren(subParaIter, subParaIter, subFEChild);
					}
					
					//increment so that subParaIter points to the element we just emptied
					++subParaIter;
					//remove the empty child
					//subPB = <b>barother<b>
					subPB.replaceChildren(subParaIter, subParaIter + 1);
				}
				else if(subFE is SubParagraphGroupElementBase)
				{
					flushSPBlock(subFE as SubParagraphGroupElementBase, spgClass);
					++subParaIter;
				}
				else
					++subParaIter;//go to next child
			}
		}
		
		/** returns next paragraph in reading order after para. Used for merging paragraphs after delete.  */
		tlf_internal static function findNextParagraph(para:ParagraphElement):ParagraphElement
		{
			if (para)
			{
				var leaf:FlowLeafElement = para.getLastLeaf();
				leaf = leaf.getNextLeaf();
				if (leaf)
					return leaf.getParagraph();
			}
			return null;
		/*	var sibParagraph:ParagraphElement;
			if (para && para.parent)
			{
				var child:FlowGroupElement = para;
				var parent:FlowGroupElement = para.parent;
				
				var myidx:int = parent.getChildIndex(child);
				
				// go up the chain till not on last child
				while(myidx == parent.numChildren-1)
				{
					child = parent;
					parent = parent.parent;
					myidx = parent.getChildIndex(child);
				}
				if (myidx != parent.numChildren-1)
				{
					// go down the first child descendents till reach a paragraph
					var sibElement:FlowGroupElement = parent.getChildAt(myidx+1) as FlowGroupElement;
					while(sibElement && !(sibElement is ParagraphElement))
					{
						sibElement = sibElement.getChildAt(0) as FlowGroupElement;	
					}
					sibParagraph = sibElement as ParagraphElement;
				}
			}
			return sibParagraph; */
		}
		
		/** if parent is a singleton element, deletes it, then repeats deletion of singletons up the parent chain.  Used after paragraph merge. */
		tlf_internal static function removeEmptyParentChain(parent:FlowGroupElement):IMemento
		{
			var mementoList:MementoList = new MementoList(parent.getTextFlow());
			while(parent && (parent.numChildren == 0))
			{
				var grandParent:FlowGroupElement = parent.parent;
				if(grandParent)
				{
					var parentIdx:int = grandParent.getChildIndex(parent);
					mementoList.push(ModelEdit.removeElements(grandParent.getTextFlow(), grandParent, parentIdx, 1));
					//grandParent.replaceChildren(parentIdx, parentIdx+1);
				}
				parent = grandParent;
			}
			return mementoList;
		}
		
		/** Joins this paragraph's next sibling to this if it is a paragraph */
		static public function joinNextParagraph(para:ParagraphElement, inSameParent:Boolean):IMemento
		{		
			var nextPara:ParagraphElement = findNextParagraph(para);
			if (nextPara && (!inSameParent || para.parent == nextPara.parent))
				return joinToElement(para, nextPara);
			return null;
		}

		/** Joins this paragraph's next sibling to this if it is a paragraph */
		static public function joinToNextParagraph(para:ParagraphElement, inSameParent:Boolean):MementoList
		{		
			var sibParagraph:ParagraphElement = findNextParagraph(para);
			if (sibParagraph && (!inSameParent || para.parent == sibParagraph.parent))
				return joinToNextElement(para, sibParagraph);
			return null;
		}

		/** Joins this element2 to element1 -- all children of element2 added to end of element1 */
		static public function joinToElement(element1:FlowGroupElement, element2:FlowGroupElement):IMemento
		{	
			var list:MementoList;
			
			if (element1 && element2)
			{
		/*		list = new MementoList(element1.getTextFlow());
				
				var elementList:Array = element2.mxmlChildren;
				
				list.push(ModelEdit.removeElements(element2.getTextFlow(), element2, 0, element2.numChildren)); // remove children of the second element

				for(var i:int=0; i<elementList.length; ++i) // add them to the first element
				{
					list.push(ModelEdit.addElement(element1.getTextFlow(), elementList[i], element1, element1.numChildren));
				}
				// remove (empty) element2 and chain of any empty parents
				list.push(removeEmptyParentChain(element2));
				return list;
				*/
				return ModelEdit.joinElement(element2.getTextFlow(), element1, element2);
			}
			return list;
		}
		
		/** Joins this element1 to element2 -- all children of element1 added to front of element2 */
		static public function joinToNextElement(element1:FlowGroupElement, element2:FlowGroupElement):MementoList
		{		
			var list:MementoList;

			if (element1 && element2)
			{
				list = new MementoList(element1.getTextFlow());

				var elementList:Array = element1.mxmlChildren;
				list.push(ModelEdit.removeElements(element1.getTextFlow(), element1, 0, element1.numChildren)); // remove children of the first element
				for(var i:int=elementList.length - 1; i>=0; --i) // add them to the second element
				{
					list.push(ModelEdit.addElement(element2.getTextFlow(), elementList[i], element2, 0));
				}
				// remove (empty) element1 and chain of any empty parents
				list.push(removeEmptyParentChain(element1));
				return list;
			}
			return list;
		}
		
								
	}
}