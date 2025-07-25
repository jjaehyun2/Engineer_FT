/*
 * =BEGIN CLOSED LICENSE
 *
 *  Copyright(c) 2014 Andras Csizmadia.
 *  http://www.vpmedia.eu
 *
 *  For information about the licensing and copyright please
 *  contact Andras Csizmadia at andras@vpmedia.eu.
 *
 *  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 *  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 *  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 *  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 *  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 *  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 *  THE SOFTWARE.
 *
 * =END CLOSED LICENSE
 */
package hu.vpmedia.ui {
import flash.events.ContextMenuEvent;
import flash.ui.ContextMenuItem;

/**
 * TBD
 */
public class BaseContextMenuItem {

    /**
     * TBD
     */
    public var content:ContextMenuItem;

    /**
     * TBD
     */
    protected var title:String;

    /**
     * Constructor
     */
    public function BaseContextMenuItem() {
        initialize();
    }

    //----------------------------------
    //  ContextMenu
    //----------------------------------
    /**
     * ContextMenu initializer
     */
    protected function initialize():void {
        content = new ContextMenuItem(title);
        content.addEventListener(ContextMenuEvent.MENU_ITEM_SELECT, eventHandler);
    }

    /**
     * Context menu event handler
     */
    protected function eventHandler(event:ContextMenuEvent):void {
        throw new Error("AbstractContextMenuItem::execute() error, must override.");
        // OVERRIDE
    }
}
}