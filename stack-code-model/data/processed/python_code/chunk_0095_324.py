/* Copyright 2018 Tua Rua Ltd.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 */

package com.tuarua.spotlight {
/** Constants that describe common mailbox names.*/
public final class MailboxIdentifier {
    /** An inbox.*/
    public static const inbox:String = "mailbox.inbox";
    /** A drafts mailbox.*/
    public static const drafts:String = "mailbox.drafts";
    /** A sent mailbox.*/
    public static const sent:String = "mailbox.sent";
    /** A junk mailbox.*/
    public static const junk:String = "mailbox.junk";
    /** A trash mailbox.*/
    public static const trash:String = "mailbox.trash";
    /** An archive mailbox.*/
    public static const archive:String = "mailbox.archive";
}
}