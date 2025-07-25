/**
 * This license does NOT supersede the original license of GPC.  Please see:
 * http://www.cs.man.ac.uk/~toby/alan/software/#Licensing
 *
 * This license does NOT supersede the original license of SEISW GPC Java port.  Please see:
 * http://www.seisw.com/GPCJ/GpcjLicenseAgreement.txt
 *
 * Copyright (c) 2009, Jakub Kaniewski, jakub.kaniewsky@gmail.com
 * BMnet software http://www.bmnet.pl/
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *   - Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   - Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *   - Neither the name of the BMnet software nor the
 *     names of its contributors may be used to endorse or promote products
 *     derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY JAKUB KANIEWSKI, BMNET ''AS IS'' AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL JAKUB KANIEWSKI, BMNET BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

package pl.bmnet.gpcas.geometry{
	import pl.bmnet.gpcas.util.ArrayList;
	import pl.bmnet.gpcas.util.List;
	
 
   
   public class EdgeTable
   {
      private var m_List:List= new ArrayList();
   
      public function addNode( x:Number, y:Number):void {
         var node:EdgeNode= new EdgeNode();
         node.vertex.x = x ;
         node.vertex.y = y ;
         m_List.add( node );
      }
      
      public function getNode( index:int):EdgeNode {
         return m_List.get(index) as EdgeNode;
      }
      
      public function FWD_MIN( i:int):Boolean {
         var prev:EdgeNode= EdgeNode(m_List.get(Clip.PREV_INDEX(i, m_List.size())));
         var next:EdgeNode= EdgeNode(m_List.get(Clip.NEXT_INDEX(i, m_List.size())));
         var ith:EdgeNode= EdgeNode(m_List.get(i));
         return ((prev.vertex.y >= ith.vertex.y) &&
                 (next.vertex.y >  ith.vertex.y));
      }

      public function NOT_FMAX( i:int):Boolean {
         var next:EdgeNode= EdgeNode(m_List.get(Clip.NEXT_INDEX(i, m_List.size())));
         var ith:EdgeNode= EdgeNode(m_List.get(i));
         return(next.vertex.y > ith.vertex.y);
      }

      public function REV_MIN( i:int):Boolean {
         var prev:EdgeNode= EdgeNode(m_List.get(Clip.PREV_INDEX(i, m_List.size())));
         var next:EdgeNode= EdgeNode(m_List.get(Clip.NEXT_INDEX(i, m_List.size())));
         var ith:EdgeNode= EdgeNode(m_List.get(i));
         return ((prev.vertex.y >  ith.vertex.y) &&
                 (next.vertex.y >= ith.vertex.y));
      }
      
      public function NOT_RMAX( i:int):Boolean {
         var prev:EdgeNode= EdgeNode(m_List.get(Clip.PREV_INDEX(i, m_List.size())));
         var ith:EdgeNode= EdgeNode(m_List.get(i));
         return (prev.vertex.y > ith.vertex.y) ;
      }
   }


}